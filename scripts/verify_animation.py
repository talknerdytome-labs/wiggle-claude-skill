#!/usr/bin/env python3
"""
Verify Lottie animation matches described approach.

This script validates a Lottie JSON file against expectations to catch
promise-implementation mismatches before rendering. It checks layer counts,
timing strategies, asset references, and file sizes.

Usage:
    python scripts/verify_animation.py animation.json
    python scripts/verify_animation.py animation.json --expect-layers 5
    python scripts/verify_animation.py animation.json --expect-sequential
    python scripts/verify_animation.py animation.json --expect-layers 5 --expect-sequential --max-size 200

Checks:
    - Number of layers vs expected element count
    - Asset references (external vs embedded)
    - Staggered timing if "sequential" animation expected
    - File size is reasonable for complexity
    - Each layer has unique refId
    - Animation duration and frame rate
    - Asset sizes and optimization opportunities

Why This Matters:
    Catches the gap between "I'll animate each element separately" and
    actually implementing everything as one layer. Prevents user disappointment
    and wasted rendering time on problematic animations.

Example Output:
    ✓ Animation has 5 layers (expected: 5)
    ✓ Assets use external references (good for rendering)
    ✗ WARNING: All layers start at frame 0 (expected: sequential stagger)
    ✗ WARNING: Total file size 618KB exceeds recommended 200KB
    ⚠  SUGGESTION: Use prepare_logo.py --max-size 600 to optimize assets
"""

import json
import argparse
import sys
from pathlib import Path
import base64


def load_lottie(lottie_path):
    """Load and parse Lottie JSON file."""
    try:
        with open(lottie_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"❌ Error: File not found: {lottie_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ Error parsing JSON: {e}")
        sys.exit(1)


def get_file_size(lottie_path):
    """Get file size in KB."""
    return Path(lottie_path).stat().st_size / 1024


def check_layer_count(data, expected=None):
    """Check number of layers in animation."""
    layers = data.get('layers', [])
    layer_count = len(layers)

    if expected:
        if layer_count == expected:
            print(f"✅ Animation has {layer_count} layer(s) (expected: {expected})")
            return True
        else:
            print(f"❌ WARNING: Animation has {layer_count} layer(s) (expected: {expected})")
            return False
    else:
        print(f"ℹ️  Animation has {layer_count} layer(s)")
        return True


def check_unique_layer_ids(data):
    """Check that each layer has a unique refId for assets."""
    layers = data.get('layers', [])
    ref_ids = []
    duplicates = []

    for layer in layers:
        ref_id = layer.get('refId')
        if ref_id:
            if ref_id in ref_ids:
                duplicates.append(ref_id)
            ref_ids.append(ref_id)

    if duplicates:
        print(f"❌ WARNING: Duplicate asset references found: {set(duplicates)}")
        print(f"   Each layer should reference a unique asset")
        return False
    elif ref_ids:
        print(f"✅ All {len(ref_ids)} layer asset references are unique")
        return True
    else:
        print(f"ℹ️  No asset references found (shape-only animation)")
        return True


def check_sequential_timing(data):
    """Check if layers have staggered start times (sequential animation)."""
    layers = data.get('layers', [])
    start_times = [layer.get('st', layer.get('ip', 0)) for layer in layers]

    # Check if all layers start at the same time
    if len(set(start_times)) == 1:
        return False, start_times[0]

    # Check if start times are increasing (staggered)
    is_staggered = all(start_times[i] < start_times[i+1] for i in range(len(start_times)-1))

    return is_staggered, start_times


def check_timing_strategy(data, expect_sequential=False):
    """Check timing strategy (simultaneous vs sequential)."""
    is_staggered, start_times = check_sequential_timing(data)

    if expect_sequential:
        if is_staggered:
            print(f"✅ Layers have staggered timing (sequential animation)")
            print(f"   Start times: {start_times}")
            return True
        else:
            if len(set(start_times)) == 1:
                print(f"❌ WARNING: All layers start at frame {start_times[0]} (expected: sequential stagger)")
                print(f"   Described as sequential but implemented as simultaneous")
                return False
            else:
                print(f"⚠️  Layers have non-sequential timing pattern: {start_times}")
                return True
    else:
        if is_staggered:
            print(f"ℹ️  Layers use sequential timing (staggered start times)")
        else:
            print(f"ℹ️  Layers use simultaneous timing (all start together)")
        return True


def check_asset_references(data):
    """Check if assets use external references or embedded base64."""
    assets = data.get('assets', [])

    if not assets:
        print(f"ℹ️  No assets found (shape-only animation or missing assets)")
        return True

    external_count = 0
    embedded_count = 0
    embedded_sizes = []

    for asset in assets:
        is_embedded = asset.get('e', 0) == 1
        has_path = bool(asset.get('p'))
        has_embedded_data = bool(asset.get('p', '').startswith('data:'))

        if is_embedded or has_embedded_data:
            embedded_count += 1
            # Try to estimate size if base64
            if has_embedded_data:
                data_str = asset.get('p', '')
                if 'base64,' in data_str:
                    base64_data = data_str.split('base64,')[1]
                    decoded_size = len(base64_data) * 3 / 4 / 1024  # Approximate KB
                    embedded_sizes.append(decoded_size)
        else:
            external_count += 1

    print(f"ℹ️  Assets: {external_count} external, {embedded_count} embedded")

    if external_count > 0 and embedded_count == 0:
        print(f"✅ All assets use external references (good for Cairo rendering)")
        return True
    elif embedded_count > 0:
        print(f"⚠️  {embedded_count} asset(s) are embedded (may cause Cairo MemoryError >100KB)")
        if embedded_sizes:
            for i, size in enumerate(embedded_sizes):
                if size > 100:
                    print(f"   Asset {i}: ~{size:.1f}KB embedded (likely to cause issues)")
        print(f"   Consider: Use external references during rendering, embed after")
        return False

    return True


def check_file_size(lottie_path, max_size_kb=None):
    """Check total Lottie JSON file size."""
    file_size_kb = get_file_size(lottie_path)

    if max_size_kb:
        if file_size_kb <= max_size_kb:
            print(f"✅ File size {file_size_kb:.1f}KB (under {max_size_kb}KB limit)")
            return True
        else:
            print(f"❌ WARNING: File size {file_size_kb:.1f}KB exceeds recommended {max_size_kb}KB")
            print(f"   Large files may cause rendering issues")
            return False
    else:
        # Default thresholds
        if file_size_kb < 100:
            print(f"✅ File size {file_size_kb:.1f}KB (excellent)")
            return True
        elif file_size_kb < 300:
            print(f"ℹ️  File size {file_size_kb:.1f}KB (good)")
            return True
        elif file_size_kb < 500:
            print(f"⚠️  File size {file_size_kb:.1f}KB (acceptable but large)")
            return True
        else:
            print(f"❌ WARNING: File size {file_size_kb:.1f}KB (very large, may cause issues)")
            return False


def check_animation_properties(data):
    """Check basic animation properties (duration, fps, dimensions)."""
    width = data.get('w', 0)
    height = data.get('h', 0)
    frame_rate = data.get('fr', 30)
    in_point = data.get('ip', 0)
    out_point = data.get('op', 0)

    duration_frames = out_point - in_point
    duration_seconds = duration_frames / frame_rate if frame_rate > 0 else 0

    print(f"\n📊 Animation Properties:")
    print(f"   Dimensions: {width}x{height}")
    print(f"   Frame rate: {frame_rate} fps")
    print(f"   Duration: {duration_seconds:.2f}s ({duration_frames} frames)")

    # Sanity checks
    issues = []
    if width == 0 or height == 0:
        issues.append("Dimensions are 0 (invalid)")
    if duration_seconds == 0:
        issues.append("Duration is 0 (empty animation)")
    if frame_rate > 120:
        issues.append(f"Very high frame rate ({frame_rate} fps) - may cause performance issues")

    if issues:
        print(f"⚠️  Issues found:")
        for issue in issues:
            print(f"   - {issue}")
        return False

    return True


def provide_suggestions(all_checks_passed, file_size_kb, data):
    """Provide optimization suggestions based on results."""
    if all_checks_passed:
        print(f"\n✅ All checks passed!")
        return

    print(f"\n💡 Suggestions:")

    # File size suggestions
    if file_size_kb > 300:
        print(f"   1. Reduce file size:")
        print(f"      - Use external asset references during rendering")
        print(f"      - Run: python scripts/optimize_lottie.py animation.json optimized.json")
        print(f"      - Optimize images: python scripts/prepare_logo.py logo.png --max-size 600")

    # Asset suggestions
    assets = data.get('assets', [])
    if any(asset.get('e', 0) == 1 for asset in assets):
        print(f"   2. Asset optimization:")
        print(f"      - Change embedded assets (e: 1) to external references (e: 0)")
        print(f"      - Render GIF with external references")
        print(f"      - Embed base64 AFTER successful rendering if needed")

    # Layer timing suggestions
    layers = data.get('layers', [])
    if layers:
        start_times = [layer.get('st', layer.get('ip', 0)) for layer in layers]
        if len(set(start_times)) == 1 and len(layers) > 1:
            print(f"   3. For sequential animation:")
            print(f"      - Add staggered start times (st property)")
            print(f"      - Example: layer 0 starts at frame 0, layer 1 at frame 10, etc.")


def main():
    parser = argparse.ArgumentParser(
        description='Verify Lottie animation matches described approach',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic verification
  python scripts/verify_animation.py animation.json

  # Verify expected layer count
  python scripts/verify_animation.py animation.json --expect-layers 5

  # Verify sequential animation with size limit
  python scripts/verify_animation.py animation.json --expect-sequential --max-size 200

  # Full verification
  python scripts/verify_animation.py animation.json --expect-layers 5 --expect-sequential --max-size 300
        """
    )

    parser.add_argument('lottie_json', help='Lottie JSON file to verify')
    parser.add_argument('--expect-layers', type=int, help='Expected number of layers')
    parser.add_argument('--expect-sequential', action='store_true', help='Expect sequential/staggered timing')
    parser.add_argument('--max-size', type=float, help='Maximum file size in KB (e.g., 200)')

    args = parser.parse_args()

    # Load Lottie
    print(f"📖 Loading Lottie: {args.lottie_json}\n")
    data = load_lottie(args.lottie_json)

    # Run checks
    checks_passed = []

    # Layer count
    checks_passed.append(check_layer_count(data, args.expect_layers))

    # Unique layer IDs
    checks_passed.append(check_unique_layer_ids(data))

    # Timing strategy
    checks_passed.append(check_timing_strategy(data, args.expect_sequential))

    # Asset references
    checks_passed.append(check_asset_references(data))

    # File size
    checks_passed.append(check_file_size(args.lottie_json, args.max_size))

    # Animation properties
    checks_passed.append(check_animation_properties(data))

    # Summary
    all_passed = all(checks_passed)
    file_size_kb = get_file_size(args.lottie_json)

    # Provide suggestions
    provide_suggestions(all_passed, file_size_kb, data)

    # Exit code
    if all_passed:
        print(f"\n🎬 Animation is ready to render!")
        sys.exit(0)
    else:
        print(f"\n⚠️  Review warnings above before rendering")
        sys.exit(0)  # Don't fail, just warn


if __name__ == '__main__':
    main()
