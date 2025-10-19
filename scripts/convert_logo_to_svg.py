#!/usr/bin/env python3
"""
Logo to SVG Converter - Convert raster logos (PNG/JPG) to vector SVG

Uses image tracing to convert bitmap images to SVG paths.
This is useful for Lottie animations which work better with vector graphics.

Requires: potrace (install via: brew install potrace / apt-get install potrace)
"""

import sys
import subprocess
from pathlib import Path
from PIL import Image


def convert_logo_to_svg(
    input_path: str | Path,
    output_path: str | Path = None,
    threshold: int = 128,
    optimize: bool = True
) -> tuple[bool, str]:
    """
    Convert PNG/JPG logo to SVG using image tracing.

    Args:
        input_path: Path to input image (PNG/JPG)
        output_path: Output SVG path (default: same name with .svg)
        threshold: Threshold for bitmap conversion (0-255, default 128)
        optimize: Simplify SVG paths for smaller file size

    Returns:
        Tuple of (success: bool, output_path: str)
    """
    input_path = Path(input_path)

    if not input_path.exists():
        print(f"❌ Error: Input file not found: {input_path}")
        return False, ""

    if output_path is None:
        output_path = input_path.with_suffix('.svg')
    else:
        output_path = Path(output_path)

    # Check if potrace is installed
    try:
        subprocess.run(['potrace', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Error: potrace is not installed")
        print("   Install with:")
        print("     macOS: brew install potrace")
        print("     Linux: sudo apt-get install potrace")
        print("     Windows: Download from http://potrace.sourceforge.net/")
        return False, ""

    try:
        # Step 1: Convert to PBM (Portable Bitmap) format for potrace
        print(f"📖 Loading image: {input_path}")
        img = Image.open(input_path)

        # Convert to grayscale
        if img.mode != 'L':
            img = img.convert('L')

        # Apply threshold to create binary image
        img = img.point(lambda x: 255 if x > threshold else 0, mode='1')

        # Save as PBM
        pbm_path = input_path.with_suffix('.pbm')
        img.save(pbm_path)
        print(f"✓ Created bitmap: {pbm_path}")

        # Step 2: Trace bitmap to SVG using potrace
        print(f"🎨 Tracing to SVG...")

        potrace_cmd = ['potrace', str(pbm_path), '-s', '-o', str(output_path)]

        if optimize:
            potrace_cmd.extend(['-O', '0.2'])  # Optimization tolerance

        subprocess.run(potrace_cmd, check=True, capture_output=True)

        # Cleanup temporary PBM
        pbm_path.unlink()

        # Check output
        if output_path.exists():
            file_size_kb = output_path.stat().st_size / 1024
            print(f"✅ SVG created: {output_path}")
            print(f"   Size: {file_size_kb:.1f} KB")
            return True, str(output_path)
        else:
            print(f"❌ Error: SVG was not created")
            return False, ""

    except Exception as e:
        print(f"❌ Error during conversion: {e}")
        # Cleanup on error
        if pbm_path and pbm_path.exists():
            pbm_path.unlink()
        return False, ""


def main():
    if len(sys.argv) < 2:
        print("Usage: convert_logo_to_svg.py <input.png|jpg> [output.svg] [threshold]")
        print("\nConvert raster logo to vector SVG using image tracing")
        print("\nExamples:")
        print("  convert_logo_to_svg.py logo.png")
        print("  convert_logo_to_svg.py logo.png logo_vector.svg")
        print("  convert_logo_to_svg.py logo.png logo.svg 150")
        print("\nOptional:")
        print("  output.svg: Output path (default: same name with .svg)")
        print("  threshold: Bitmap threshold 0-255 (default: 128)")
        print("             Lower = more black, Higher = more white")
        print("\nRequires: potrace (brew install potrace)")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    threshold = int(sys.argv[3]) if len(sys.argv) > 3 else 128

    print(f"🚀 Converting logo to SVG")
    print(f"   Input: {input_path}")
    print(f"   Threshold: {threshold}\n")

    success, output = convert_logo_to_svg(input_path, output_path, threshold)

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
