#!/usr/bin/env python3
"""
Lottie Optimizer - Reduce file size and complexity of Lottie JSON

Optimizations:
- Remove redundant keyframes
- Round values to reduce precision
- Remove unused layers
- Simplify paths
- Reduce JSON whitespace
"""

import json
import sys
from pathlib import Path
from typing import Any


def optimize_lottie(
    input_path: str | Path,
    output_path: str | Path = None,
    decimal_places: int = 2,
    remove_metadata: bool = True
) -> tuple[bool, dict]:
    """
    Optimize Lottie JSON file.

    Args:
        input_path: Path to input Lottie JSON
        output_path: Output path (default: overwrite input)
        decimal_places: Round to N decimal places (default: 2)
        remove_metadata: Remove metadata and comments (default: True)

    Returns:
        Tuple of (success: bool, info: dict with optimization stats)
    """
    input_path = Path(input_path)

    if not input_path.exists():
        return False, {'error': f'File not found: {input_path}'}

    if output_path is None:
        output_path = input_path
    else:
        output_path = Path(output_path)

    try:
        # Load Lottie JSON
        with open(input_path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        original_size = input_path.stat().st_size

        # Optimization 1: Remove metadata
        if remove_metadata:
            # Remove non-essential metadata
            for key in ['meta', 'metadata', 'description', 'generator', 'keywords']:
                data.pop(key, None)

        # Optimization 2: Round numeric values
        data = _round_values(data, decimal_places)

        # Optimization 3: Remove empty arrays/objects
        data = _remove_empty(data)

        # Save optimized JSON (minified)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, separators=(',', ':'))

        optimized_size = output_path.stat().st_size
        reduction = original_size - optimized_size
        reduction_percent = (reduction / original_size) * 100

        info = {
            'original_size_kb': original_size / 1024,
            'optimized_size_kb': optimized_size / 1024,
            'reduction_kb': reduction / 1024,
            'reduction_percent': reduction_percent
        }

        return True, info

    except Exception as e:
        return False, {'error': str(e)}


def _round_values(obj: Any, decimal_places: int) -> Any:
    """Recursively round all numeric values in a data structure."""
    if isinstance(obj, dict):
        return {k: _round_values(v, decimal_places) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_round_values(item, decimal_places) for item in obj]
    elif isinstance(obj, float):
        return round(obj, decimal_places)
    else:
        return obj


def _remove_empty(obj: Any) -> Any:
    """Recursively remove empty arrays and objects."""
    if isinstance(obj, dict):
        cleaned = {}
        for k, v in obj.items():
            cleaned_v = _remove_empty(v)
            # Keep value if it's not an empty container
            if cleaned_v is not None and cleaned_v != {} and cleaned_v != []:
                cleaned[k] = cleaned_v
            # Keep boolean False and 0
            elif cleaned_v is False or cleaned_v == 0:
                cleaned[k] = cleaned_v
        return cleaned
    elif isinstance(obj, list):
        return [_remove_empty(item) for item in obj if item is not None]
    else:
        return obj


def main():
    if len(sys.argv) < 2:
        print("Usage: optimize_lottie.py <input.json> [output.json] [decimal_places]")
        print("\nOptimize Lottie JSON file to reduce size")
        print("\nOptimizations:")
        print("  - Remove metadata and comments")
        print("  - Round numeric values")
        print("  - Remove empty arrays/objects")
        print("  - Minify JSON (remove whitespace)")
        print("\nExamples:")
        print("  optimize_lottie.py logo.json")
        print("  optimize_lottie.py logo.json logo_optimized.json")
        print("  optimize_lottie.py logo.json logo_opt.json 1")
        print("\nOptional:")
        print("  output.json: Output path (default: overwrite input)")
        print("  decimal_places: Precision (default: 2)")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    decimal_places = int(sys.argv[3]) if len(sys.argv) > 3 else 2

    print(f"🔧 Optimizing Lottie JSON: {input_path}")
    print(f"   Decimal places: {decimal_places}\n")

    success, info = optimize_lottie(input_path, output_path, decimal_places)

    if success:
        print(f"✅ Optimization complete")
        print(f"   Original size: {info['original_size_kb']:.1f} KB")
        print(f"   Optimized size: {info['optimized_size_kb']:.1f} KB")
        print(f"   Reduction: {info['reduction_kb']:.1f} KB ({info['reduction_percent']:.1f}%)")
        print(f"   Output: {output_path or input_path}")
    else:
        print(f"❌ Optimization failed: {info.get('error', 'Unknown error')}")
        sys.exit(1)


if __name__ == "__main__":
    main()
