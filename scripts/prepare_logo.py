#!/usr/bin/env python3
"""
Logo Preparation Tool - Optimize images for Lottie animation

Features:
- Resize images to optimal dimensions
- Optimize PNG compression
- Validate transparency and color modes
- Generate base64 encoded version
- Warn about potential rendering issues

Usage:
    python prepare_logo.py logo.png
    python prepare_logo.py logo.png --max-size 500 --optimize
    python prepare_logo.py logo.png --base64-only
    python prepare_logo.py logo.png --output-dir ./prepared
"""

import sys
import argparse
import base64
from pathlib import Path
from typing import Dict

try:
    from PIL import Image
except ImportError:
    print("❌ Error: Pillow not installed")
    print("   Install with: pip install pillow")
    sys.exit(1)


def check_image_properties(img: Image.Image, filepath: Path) -> Dict:
    """Analyze image and return property report."""
    properties = {
        'dimensions': img.size,
        'mode': img.mode,
        'format': img.format,
        'has_transparency': img.mode in ('RGBA', 'LA', 'P') or 'transparency' in img.info,
        'file_size': filepath.stat().st_size if filepath.exists() else 0,
    }

    # Check if image has actual transparency data
    if img.mode == 'RGBA':
        alpha = img.split()[3]
        extrema = alpha.getextrema()
        properties['has_alpha_channel'] = True
        properties['alpha_range'] = extrema
        properties['fully_opaque'] = extrema == (255, 255)
    else:
        properties['has_alpha_channel'] = False

    return properties


def optimize_logo(
    input_path: Path,
    max_size: int = None,
    optimize: bool = True,
    output_dir: Path = None,
    base64_only: bool = False
) -> Dict:
    """
    Prepare logo for Lottie animation.

    Args:
        input_path: Path to input image
        max_size: Maximum dimension (width or height)
        optimize: Whether to optimize PNG compression
        output_dir: Where to save output files (default: same as input)
        base64_only: Only create base64, don't save optimized PNG

    Returns:
        Dictionary with paths and info about generated files
    """
    if output_dir is None:
        output_dir = input_path.parent
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

    # Load image
    print(f"📖 Loading image: {input_path}")
    img = Image.open(input_path)

    # Analyze original
    original_props = check_image_properties(img, input_path)
    print(f"\n📊 Original Image:")
    print(f"   Dimensions: {original_props['dimensions'][0]}x{original_props['dimensions'][1]}")
    print(f"   Mode: {original_props['mode']}")
    print(f"   File size: {original_props['file_size']/1024:.1f} KB")
    print(f"   Has transparency: {original_props['has_transparency']}")

    # Recommendations
    recommendations = []

    # Check dimensions
    max_dim = max(img.size)
    if max_dim > 1024:
        recommendations.append(f"Image is large ({max_dim}px). Consider --max-size 512 for better performance")

    # Check file size
    if original_props['file_size'] > 200_000:
        recommendations.append(f"File is {original_props['file_size']/1024:.1f}KB. Large embedded images may cause Cairo rendering issues")

    # Check transparency
    if not original_props['has_transparency']:
        recommendations.append("Image has no transparency. Logo animations typically work better with transparent backgrounds")

    # Check mode
    if img.mode not in ('RGBA', 'RGB'):
        recommendations.append(f"Image mode is {img.mode}. Converting to RGBA recommended")

    if recommendations:
        print(f"\n💡 Recommendations:")
        for rec in recommendations:
            print(f"   - {rec}")

    # Process image
    processed_img = img.copy()

    # Ensure RGBA mode for logos
    if processed_img.mode != 'RGBA':
        print(f"\n🔄 Converting {processed_img.mode} → RGBA")
        if processed_img.mode == 'P':
            # Palette mode - preserve transparency
            processed_img = processed_img.convert('RGBA')
        elif processed_img.mode == 'RGB':
            # Add alpha channel
            processed_img = processed_img.convert('RGBA')
        else:
            processed_img = processed_img.convert('RGBA')

    # Resize if needed
    if max_size and max(processed_img.size) > max_size:
        ratio = max_size / max(processed_img.size)
        new_size = tuple(int(dim * ratio) for dim in processed_img.size)
        print(f"\n🔍 Resizing: {processed_img.size} → {new_size}")
        processed_img = processed_img.resize(new_size, Image.Resampling.LANCZOS)

    result = {
        'original': input_path,
        'dimensions': processed_img.size,
        'original_size': original_props['file_size'],
    }

    # Save optimized PNG
    if not base64_only:
        output_path = output_dir / f"{input_path.stem}_optimized.png"
        print(f"\n💾 Saving optimized PNG: {output_path}")

        save_kwargs = {
            'format': 'PNG',
        }
        if optimize:
            save_kwargs['optimize'] = True
            save_kwargs['compress_level'] = 9

        processed_img.save(output_path, **save_kwargs)

        optimized_size = output_path.stat().st_size
        compression_ratio = (1 - optimized_size / original_props['file_size']) * 100

        print(f"   Original: {original_props['file_size']/1024:.1f} KB")
        print(f"   Optimized: {optimized_size/1024:.1f} KB")
        print(f"   Saved: {compression_ratio:.1f}%")

        result['optimized_png'] = output_path
        result['optimized_size'] = optimized_size

        # Warn about Cairo issues
        if optimized_size > 100_000:
            print(f"\n⚠️  Warning: Optimized file is still {optimized_size/1024:.1f}KB")
            print(f"   Embedded images >100KB may cause Cairo rendering issues")
            print(f"   Suggestions:")
            print(f"   - Use smaller --max-size (current: {max(processed_img.size)}px)")
            print(f"   - Use external file reference during rendering")
            print(f"   - Only embed base64 for final distribution")

    # Generate base64
    base64_path = output_dir / f"{input_path.stem}_base64.txt"
    print(f"\n🔐 Generating base64: {base64_path}")

    # Save processed image to bytes
    from io import BytesIO
    buffer = BytesIO()
    processed_img.save(buffer, format='PNG', optimize=optimize)
    image_bytes = buffer.getvalue()

    b64_string = base64.b64encode(image_bytes).decode('utf-8')
    data_url = f'data:image/png;base64,{b64_string}'

    with open(base64_path, 'w') as f:
        f.write(data_url)

    base64_size = len(data_url.encode('utf-8'))
    print(f"   Base64 size: {base64_size/1024:.1f} KB")

    result['base64_file'] = base64_path
    result['base64_size'] = base64_size

    # Final warnings
    if base64_size > 100_000:
        print(f"\n⚠️  Warning: Base64 encoding is {base64_size/1024:.1f}KB")
        print(f"   This may cause Cairo rendering issues when embedded in Lottie JSON")

    # Summary
    print(f"\n✅ Logo prepared successfully!")
    print(f"\n📝 Usage in Lottie JSON:")
    print(f"\n   For development/rendering (recommended):")
    print(f"   {{")
    print(f"     \"assets\": [{{")
    print(f"       \"id\": \"logo_image\",")
    print(f"       \"w\": {processed_img.size[0]},")
    print(f"       \"h\": {processed_img.size[1]},")
    if not base64_only:
        print(f"       \"p\": \"{output_path.name}\",")
    else:
        print(f"       \"p\": \"{input_path.name}\",")
    print(f"       \"e\": 0  // External file")
    print(f"     }}]")
    print(f"   }}")
    print(f"\n   For distribution (embedded):")
    print(f"   {{")
    print(f"     \"assets\": [{{")
    print(f"       \"id\": \"logo_image\",")
    print(f"       \"w\": {processed_img.size[0]},")
    print(f"       \"h\": {processed_img.size[1]},")
    print(f"       \"p\": \"<paste contents of {base64_path.name}>\",")
    print(f"       \"e\": 1  // Embedded base64")
    print(f"     }}]")
    print(f"   }}")

    return result


def main():
    parser = argparse.ArgumentParser(
        description='Prepare logo images for Lottie animation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic optimization
  python prepare_logo.py logo.png

  # Resize to max 500px and optimize
  python prepare_logo.py logo.png --max-size 500 --optimize

  # Only generate base64 (no optimized PNG)
  python prepare_logo.py logo.png --base64-only

  # Save to specific directory
  python prepare_logo.py logo.png --output-dir ./prepared

  # Aggressive optimization for small size
  python prepare_logo.py logo.png --max-size 400 --optimize
        """
    )

    parser.add_argument('input', type=Path, help='Input image path')
    parser.add_argument('--max-size', type=int, help='Maximum dimension (width or height)')
    parser.add_argument('--optimize', action='store_true', default=True, help='Optimize PNG compression (default: True)')
    parser.add_argument('--no-optimize', action='store_true', help='Disable PNG optimization')
    parser.add_argument('--base64-only', action='store_true', help='Only generate base64, skip optimized PNG')
    parser.add_argument('--output-dir', type=Path, help='Output directory (default: same as input)')

    args = parser.parse_args()

    # Validate input
    if not args.input.exists():
        print(f"❌ Error: File not found: {args.input}")
        sys.exit(1)

    if not args.input.suffix.lower() in ('.png', '.jpg', '.jpeg', '.gif', '.bmp'):
        print(f"❌ Error: Unsupported format: {args.input.suffix}")
        print("   Supported: .png, .jpg, .jpeg, .gif, .bmp")
        sys.exit(1)

    # Handle optimize flags
    optimize = args.optimize and not args.no_optimize

    # Process
    try:
        result = optimize_logo(
            args.input,
            max_size=args.max_size,
            optimize=optimize,
            output_dir=args.output_dir,
            base64_only=args.base64_only
        )
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
