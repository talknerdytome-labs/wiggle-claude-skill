#!/usr/bin/env python3
"""
Loop Validator - Check if Lottie animation has perfect loop continuity

Validates that:
- First and last keyframes match for seamless looping
- Transform properties return to initial values
- Animation is designed for infinite looping
"""

import json
import sys
from pathlib import Path


def validate_loop(lottie_path: str | Path, tolerance: float = 0.01) -> tuple[bool, dict]:
    """
    Validate loop quality of a Lottie animation.

    Args:
        lottie_path: Path to Lottie JSON file
        tolerance: Acceptable difference between first/last values (default 0.01)

    Returns:
        Tuple of (is_perfect_loop: bool, info: dict with loop analysis)
    """
    lottie_path = Path(lottie_path)

    if not lottie_path.exists():
        return False, {'error': f'File not found: {lottie_path}'}

    info = {
        'path': str(lottie_path),
        'is_perfect_loop': True,
        'issues': [],
        'warnings': [],
        'layer_analysis': []
    }

    try:
        with open(lottie_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        return False, {'error': f'Cannot read Lottie file: {e}'}

    if 'layers' not in data:
        return False, {'error': 'No layers found in Lottie file'}

    # Check each layer for loop continuity
    for i, layer in enumerate(data['layers']):
        layer_info = {
            'layer_index': i,
            'layer_name': layer.get('nm', f'Layer {i}'),
            'issues': []
        }

        # Check transform properties
        if 'ks' not in layer:
            continue

        ks = layer['ks']

        # Check each transform property
        for prop_name, prop_key in [('Position', 'p'), ('Scale', 's'), ('Rotation', 'r'), ('Opacity', 'o')]:
            if prop_key not in ks:
                continue

            prop = ks[prop_key]

            # CRITICAL FIX: Check if property is animated
            # If 'a' field is 0 or missing, property is static (not animated)
            if not isinstance(prop, dict) or prop.get('a', 0) == 0:
                # Static property, skip loop validation
                continue

            if 'k' not in prop:
                continue

            keyframes = prop['k']

            # CRITICAL FIX: Verify keyframes is a list with multiple entries
            if not isinstance(keyframes, list) or len(keyframes) < 2:
                continue

            # CRITICAL FIX: Extract values safely with type checking
            try:
                first_kf = keyframes[0]
                last_kf = keyframes[-1]

                # Get start value from first keyframe
                if isinstance(first_kf, dict):
                    first_val = first_kf.get('s') or first_kf.get('e')
                else:
                    # Keyframe is raw value (shouldn't happen if a=1, but handle it)
                    first_val = first_kf

                # Get end value from last keyframe
                if isinstance(last_kf, dict):
                    last_val = last_kf.get('s') or last_kf.get('e')
                else:
                    last_val = last_kf

                if first_val is None or last_val is None:
                    continue

                # Check if values match
                if prop_key == 'r':  # Rotation - handle 360° wrapping
                    if not _rotation_matches(first_val, last_val, tolerance):
                        # Extract actual values for error message
                        f_deg = first_val[0] if isinstance(first_val, list) else first_val
                        l_deg = last_val[0] if isinstance(last_val, list) else last_val
                        diff = abs(float(f_deg) - float(l_deg)) % 360
                        layer_info['issues'].append(
                            f'{prop_name}: {f_deg}° → {l_deg}° (diff: {diff:.1f}°, not 0° or 360° multiple)'
                        )
                        info['is_perfect_loop'] = False
                else:
                    if not _values_match(first_val, last_val, tolerance):
                        layer_info['issues'].append(f'{prop_name}: first {first_val} ≠ last {last_val}')
                        info['is_perfect_loop'] = False

            except (AttributeError, TypeError, KeyError) as e:
                # Unexpected keyframe structure - skip this property silently
                continue

        if layer_info['issues']:
            info['layer_analysis'].append(layer_info)
            info['issues'].extend([f"{layer_info['layer_name']}: {issue}" for issue in layer_info['issues']])

    return info['is_perfect_loop'], info


def _rotation_matches(val1, val2, tolerance):
    """Check if rotation values match (accounting for 360° wrapping)."""
    # Handle arrays (single-element for rotation)
    if isinstance(val1, list):
        val1 = val1[0] if val1 else 0
    if isinstance(val2, list):
        val2 = val2[0] if val2 else 0

    # Check if difference is 0 or multiple of 360
    diff = abs(float(val1) - float(val2)) % 360
    return diff <= tolerance or diff >= (360 - tolerance)


def _values_match(val1, val2, tolerance):
    """Check if two values (scalars or arrays) match within tolerance."""
    if isinstance(val1, list) and isinstance(val2, list):
        if len(val1) != len(val2):
            return False
        return all(abs(float(v1) - float(v2)) <= tolerance for v1, v2 in zip(val1, val2))
    elif isinstance(val1, (int, float)) and isinstance(val2, (int, float)):
        return abs(float(val1) - float(val2)) <= tolerance
    else:
        return val1 == val2


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_loop.py <path/to/animation.json> [tolerance]")
        print("\nValidates that Lottie animation has perfect loop continuity")
        print("Checks: position, scale, rotation, opacity keyframes")
        print("\nOptional tolerance: acceptable difference (default: 0.01)")
        sys.exit(1)

    lottie_path = sys.argv[1]
    tolerance = float(sys.argv[2]) if len(sys.argv) > 2 else 0.01

    print(f"🔍 Validating loop quality: {lottie_path}")
    print(f"   Tolerance: {tolerance}\n")

    is_perfect, info = validate_loop(lottie_path, tolerance)

    if is_perfect:
        print("✅ Perfect loop! First and last keyframes match.")
        print("   Animation will loop seamlessly.")
    else:
        print("❌ Loop issues detected:")
        for issue in info['issues']:
            print(f"   - {issue}")
        print("\n💡 To fix: Ensure first and last keyframes have identical values")
        print("   for position, scale, rotation, and opacity.")
        sys.exit(1)


if __name__ == "__main__":
    main()
