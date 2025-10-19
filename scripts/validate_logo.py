#!/usr/bin/env python3
"""
Logo Validator - Check if logo files meet requirements for animation

Validates PNG/SVG/JPG files for:
- File format validity
- Alpha channel presence (transparency)
- Dimensions and file size
- Image readability
"""

from pathlib import Path
from PIL import Image
import sys


def validate_logo(logo_path: str | Path) -> tuple[bool, dict]:
    """
    Validate a logo file for animation compatibility.

    Args:
        logo_path: Path to logo file (PNG/SVG/JPG)

    Returns:
        Tuple of (passes: bool, info: dict with validation details)
    """
    logo_path = Path(logo_path)

    if not logo_path.exists():
        return False, {'error': f'File not found: {logo_path}'}

    info = {
        'path': str(logo_path),
        'file_size_bytes': logo_path.stat().st_size,
        'file_size_mb': logo_path.stat().st_size / (1024 * 1024),
        'format': None,
        'dimensions': None,
        'has_alpha': False,
        'mode': None,
        'passes': True,
        'warnings': [],
        'errors': []
    }

    # Check file extension
    ext = logo_path.suffix.lower()
    if ext == '.svg':
        # SVG validation - just check if it's readable text
        try:
            with open(logo_path, 'r', encoding='utf-8') as f:
                content = f.read(1000)
                if '<svg' not in content.lower():
                    info['errors'].append('File does not appear to be valid SVG')
                    info['passes'] = False
                else:
                    info['format'] = 'SVG'
                    print(f"✓ Valid SVG file")
        except Exception as e:
            info['errors'].append(f'Cannot read SVG file: {e}')
            info['passes'] = False

        return info['passes'], info

    elif ext in ['.png', '.jpg', '.jpeg']:
        # Raster image validation using PIL
        try:
            with Image.open(logo_path) as img:
                info['format'] = img.format
                info['dimensions'] = img.size
                info['mode'] = img.mode
                info['has_alpha'] = img.mode in ('RGBA', 'LA', 'PA') or (
                    img.mode == 'P' and 'transparency' in img.info
                )

                width, height = img.size

                # Format check
                print(f"✓ Valid {img.format} file ({width}x{height})")

                # Alpha channel check
                if info['has_alpha']:
                    print(f"✓ Has transparency/alpha channel ({img.mode})")
                else:
                    info['warnings'].append(f'No transparency detected ({img.mode}). Logo may have background.')
                    print(f"⚠ No transparency ({img.mode}). Consider using PNG with alpha channel for better results.")

                # Dimension check
                if width < 100 or height < 100:
                    info['warnings'].append(f'Small dimensions ({width}x{height}). May appear pixelated.')
                    print(f"⚠ Small dimensions ({width}x{height}). Larger logos animate better.")
                elif width > 4096 or height > 4096:
                    info['warnings'].append(f'Very large dimensions ({width}x{height}). Consider resizing.')
                    print(f"⚠ Large dimensions ({width}x{height}). May slow rendering.")
                else:
                    print(f"✓ Good dimensions ({width}x{height})")

                # File size check
                if info['file_size_mb'] > 10:
                    info['warnings'].append(f'Large file size ({info["file_size_mb"]:.1f}MB)')
                    print(f"⚠ Large file ({info['file_size_mb']:.1f}MB). Consider compressing.")
                else:
                    print(f"✓ Reasonable file size ({info['file_size_mb']:.2f}MB)")

        except Exception as e:
            info['errors'].append(f'Cannot read image file: {e}')
            info['passes'] = False
            return False, info

    else:
        info['errors'].append(f'Unsupported file format: {ext}. Use PNG, SVG, or JPG.')
        info['passes'] = False
        return False, info

    return info['passes'], info


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_logo.py <path/to/logo.png|svg|jpg>")
        print("\nValidates logo files for animation compatibility")
        print("Checks: format validity, transparency, dimensions, file size")
        sys.exit(1)

    logo_path = sys.argv[1]
    print(f"🔍 Validating logo: {logo_path}\n")

    passes, info = validate_logo(logo_path)

    if passes:
        print(f"\n✅ Logo is ready for animation")
        if info['warnings']:
            print(f"\n⚠️  {len(info['warnings'])} warning(s) - review above")
    else:
        print(f"\n❌ Logo validation failed")
        for error in info['errors']:
            print(f"   Error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
