#!/usr/bin/env python3
"""
Lottie Validator - Validate Lottie JSON schema and structure

Checks if Lottie JSON files are:
- Valid JSON
- Contain required Lottie properties
- Have proper structure for animation
- Compatible with common renderers
"""

import json
import sys
from pathlib import Path


def validate_lottie(lottie_path: str | Path) -> tuple[bool, dict]:
    """
    Validate a Lottie JSON file.

    Args:
        lottie_path: Path to Lottie JSON file

    Returns:
        Tuple of (passes: bool, info: dict with validation details)
    """
    lottie_path = Path(lottie_path)

    if not lottie_path.exists():
        return False, {'error': f'File not found: {lottie_path}'}

    info = {
        'path': str(lottie_path),
        'file_size_kb': lottie_path.stat().st_size / 1024,
        'passes': True,
        'errors': [],
        'warnings': [],
        'details': {}
    }

    # Try to parse JSON
    try:
        with open(lottie_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print("✓ Valid JSON file")
    except json.JSONDecodeError as e:
        info['errors'].append(f'Invalid JSON: {e}')
        info['passes'] = False
        return False, info
    except Exception as e:
        info['errors'].append(f'Cannot read file: {e}')
        info['passes'] = False
        return False, info

    # Check required Lottie properties
    required_props = ['v', 'fr', 'ip', 'op', 'w', 'h', 'layers']
    missing_props = [prop for prop in required_props if prop not in data]

    if missing_props:
        info['errors'].append(f'Missing required properties: {", ".join(missing_props)}')
        info['passes'] = False
    else:
        print("✓ All required Lottie properties present")

    # Extract details
    if 'v' in data:
        info['details']['version'] = data['v']
        print(f"✓ Lottie version: {data['v']}")

    if 'fr' in data:
        info['details']['frame_rate'] = data['fr']
        fps = data['fr']
        if fps < 15:
            info['warnings'].append(f'Low frame rate ({fps} fps). Consider 24-60 fps for smoother animation.')
        elif fps > 120:
            info['warnings'].append(f'Very high frame rate ({fps} fps). May cause performance issues.')
        else:
            print(f"✓ Frame rate: {fps} fps")

    if 'ip' in data and 'op' in data:
        in_point = data['ip']
        out_point = data['op']
        info['details']['in_point'] = in_point
        info['details']['out_point'] = out_point

        if 'fr' in data:
            duration_frames = out_point - in_point
            duration_seconds = duration_frames / data['fr']
            info['details']['duration_seconds'] = duration_seconds

            if duration_seconds < 1:
                info['warnings'].append(f'Very short animation ({duration_seconds:.1f}s)')
            elif duration_seconds > 10:
                info['warnings'].append(f'Long animation ({duration_seconds:.1f}s). May increase file size.')
            else:
                print(f"✓ Duration: {duration_seconds:.1f} seconds ({duration_frames} frames)")

    if 'w' in data and 'h' in data:
        width = data['w']
        height = data['h']
        info['details']['dimensions'] = (width, height)

        if width < 100 or height < 100:
            info['warnings'].append(f'Small dimensions ({width}x{height})')
        elif width > 2048 or height > 2048:
            info['warnings'].append(f'Large dimensions ({width}x{height}). May affect performance.')
        else:
            print(f"✓ Dimensions: {width}x{height}")

    if 'layers' in data:
        num_layers = len(data['layers'])
        info['details']['num_layers'] = num_layers

        if num_layers == 0:
            info['errors'].append('No layers found. Animation will be empty.')
            info['passes'] = False
        elif num_layers > 50:
            info['warnings'].append(f'Many layers ({num_layers}). May impact performance.')
            print(f"⚠ {num_layers} layers (complex animation)")
        else:
            print(f"✓ {num_layers} layer(s)")

    # Check for assets (images, fonts, etc.)
    if 'assets' in data and len(data['assets']) > 0:
        num_assets = len(data['assets'])
        info['details']['num_assets'] = num_assets
        print(f"✓ {num_assets} asset(s)")

        # Check asset types and sizes
        for i, asset in enumerate(data['assets']):
            asset_id = asset.get('id', f'asset_{i}')
            is_embedded = asset.get('e', 0) == 1

            if 'p' in asset:
                path = asset['p']

                if is_embedded and path.startswith('data:image'):
                    # Embedded base64 image
                    # Calculate approximate decoded size
                    if ',' in path:
                        base64_data = path.split(',', 1)[1]
                    else:
                        base64_data = path

                    # Base64 size / 1.33 ≈ decoded size
                    base64_size = len(base64_data)
                    decoded_size_bytes = (base64_size * 3) / 4
                    decoded_size_kb = decoded_size_bytes / 1024

                    asset_dims = f"{asset.get('w', '?')}x{asset.get('h', '?')}"

                    if decoded_size_kb > 500:
                        info['warnings'].append(
                            f'Asset "{asset_id}" ({asset_dims}): Very large embedded image ({decoded_size_kb:.1f}KB). '
                            f'Strongly recommend optimization with prepare_logo.py or use external reference.'
                        )
                        print(f"⚠ Asset {i} ({asset_id}): {decoded_size_kb:.1f}KB embedded - very large!")
                    elif decoded_size_kb > 100:
                        info['warnings'].append(
                            f'Asset "{asset_id}" ({asset_dims}): Large embedded image ({decoded_size_kb:.1f}KB). '
                            f'May cause Cairo rendering issues. Consider: 1) Use external file reference for rendering, '
                            f'2) Optimize with prepare_logo.py.'
                        )
                        print(f"⚠ Asset {i} ({asset_id}): {decoded_size_kb:.1f}KB embedded - may cause Cairo issues")
                    else:
                        print(f"✓ Asset {i} ({asset_id}): {decoded_size_kb:.1f}KB embedded (good size)")

                elif not is_embedded:
                    # External file reference
                    info['warnings'].append(
                        f'External asset "{asset_id}": {path}. Ensure file exists at render time.'
                    )

    # File size check
    if info['file_size_kb'] > 500:
        info['warnings'].append(f'Large file size ({info["file_size_kb"]:.1f}KB). Consider optimizing.')
        print(f"⚠ File size: {info['file_size_kb']:.1f}KB (consider optimizing)")
    else:
        print(f"✓ File size: {info['file_size_kb']:.1f}KB")

    return info['passes'], info


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_lottie.py <path/to/animation.json>")
        print("\nValidates Lottie JSON files for proper structure")
        print("Checks: JSON validity, required properties, dimensions, duration, layers")
        sys.exit(1)

    lottie_path = sys.argv[1]
    print(f"🔍 Validating Lottie JSON: {lottie_path}\n")

    passes, info = validate_lottie(lottie_path)

    if passes:
        print(f"\n✅ Lottie file is valid")
        if info['warnings']:
            print(f"\n⚠️  {len(info['warnings'])} warning(s):")
            for warning in info['warnings']:
                print(f"   - {warning}")
    else:
        print(f"\n❌ Lottie validation failed")
        for error in info['errors']:
            print(f"   Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
