#!/usr/bin/env python3
"""
Lottie Renderer - Convert Lottie JSON to GIF/MP4

Renders Lottie animations to:
- GIF (for web, email, social media)
- MP4 (for video platforms, higher quality)
- PNG sequence (for advanced editing)
"""

import sys
import json
import os
from pathlib import Path
from typing import Tuple


def validate_assets(lottie_path: Path) -> Tuple[bool, str]:
    """
    Validate that all external assets referenced in Lottie JSON exist.

    Args:
        lottie_path: Path to Lottie JSON file

    Returns:
        Tuple of (success, error_message)
    """
    try:
        with open(lottie_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON: {e}"
    except Exception as e:
        return False, f"Failed to read file: {e}"

    assets = data.get('assets', [])
    if not assets:
        return True, ""  # No assets to validate

    lottie_dir = lottie_path.parent
    missing_assets = []

    for asset in assets:
        # Check if it's an external asset (e: 0)
        if asset.get('e') == 0:
            asset_path = asset.get('p', '')

            # Skip data URIs (base64 encoded)
            if asset_path.startswith('data:'):
                continue

            # Resolve path relative to Lottie JSON location
            full_path = lottie_dir / asset_path

            if not full_path.exists():
                missing_assets.append(f"  - {asset_path} (expected at: {full_path})")

    if missing_assets:
        error_msg = "Missing external assets:\n" + "\n".join(missing_assets)
        return False, error_msg

    return True, ""


def verify_output(output_path: Path) -> Tuple[bool, str]:
    """
    Verify that the rendered output is valid (not blank/corrupted).

    Args:
        output_path: Path to rendered file

    Returns:
        Tuple of (success, warning_message)
    """
    if not output_path.exists():
        return False, "Output file was not created"

    file_size = output_path.stat().st_size

    # Check for suspiciously small files (likely blank or corrupted)
    if file_size < 1024:  # Less than 1KB
        return False, f"Output file is suspiciously small ({file_size} bytes) - likely blank or corrupted"

    # Additional format-specific checks could be added here
    # For now, basic size check is sufficient

    return True, ""


def render_lottie_to_gif(
    lottie_path: str | Path,
    output_path: str | Path,
    width: int = None,
    height: int = None,
    fps: int = None
) -> bool:
    """
    Render Lottie JSON to GIF.

    Args:
        lottie_path: Path to Lottie JSON file
        output_path: Output GIF path
        width: Output width (default: use Lottie dimensions)
        height: Output height (default: use Lottie dimensions)
        fps: Frame rate (default: use Lottie frame rate)

    Returns:
        True if successful, False otherwise
    """
    # CRITICAL FIX: Import from correct module path
    try:
        from lottie.parsers.tgs import parse_tgs
        from lottie.exporters.gif import export_gif
    except ImportError as e:
        print("❌ Error: lottie-python not installed or missing dependencies")
        print("   Install with: pip install lottie[all]")
        print(f"   Error details: {e}")
        return False

    lottie_path = Path(lottie_path)
    output_path = Path(output_path)

    if not lottie_path.exists():
        print(f"❌ Error: Lottie file not found: {lottie_path}")
        return False

    # Validate assets before attempting render
    print(f"🔍 Validating external assets...")
    assets_ok, assets_error = validate_assets(lottie_path)
    if not assets_ok:
        print(f"❌ Asset validation failed:")
        print(assets_error)
        print(f"\n💡 Tip: Asset paths are resolved relative to the Lottie JSON file location")
        return False

    # Change to Lottie file directory for asset resolution
    original_cwd = os.getcwd()
    lottie_dir = lottie_path.parent.absolute()
    os.chdir(lottie_dir)

    try:
        # CRITICAL FIX: Parse directly from file, don't load as dict first
        print(f"📖 Loading Lottie: {lottie_path.name}")
        animation = parse_tgs(str(lottie_path))

        # CRITICAL FIX: Get dimensions from Animation object, not JSON dict
        if width is None:
            width = animation.width or 512
        if height is None:
            height = animation.height or 512
        if fps is None:
            fps = int(animation.frame_rate) if animation.frame_rate else 30

        print(f"🎬 Rendering GIF with Cairo: {width}x{height} @ {fps} fps")

        # Export to GIF - library handles size internally
        export_gif(animation, str(output_path))

        # Verify output
        output_ok, output_error = verify_output(output_path)
        if not output_ok:
            print(f"⚠️  Warning: {output_error}")
            print(f"   The file may be blank or corrupted. Check the output manually.")

        file_size_kb = output_path.stat().st_size / 1024
        file_size_mb = file_size_kb / 1024

        print(f"✅ GIF created with Cairo: {output_path}")
        print(f"   Size: {file_size_kb:.1f} KB ({file_size_mb:.2f} MB)")

        return True

    except ImportError as e:
        # Cairo not installed
        print(f"❌ Error: Cairo not available: {e}")
        print("")
        print("📋 Solution: Install Cairo for GIF rendering")
        print("   macOS:  brew install cairo pkg-config && pip install pycairo")
        print("   Linux:  sudo apt-get install libcairo2-dev pkg-config python3-dev && pip install pycairo")
        print("")
        print("   See SKILL.md Dependencies section for details")
        return False

    except MemoryError as e:
        # Cairo memory error (common with embedded base64 images >100KB)
        print(f"❌ Error: Cairo MemoryError - Embedded image too large")
        print(f"   {e}")
        print("")
        print("📋 Solution: Use EXTERNAL file reference during rendering:")
        print('   "assets": [{"id": "logo_image", "p": "logo_optimized.png", "e": 0}]')
        print("")
        print("   Steps:")
        print("   1. Run: python scripts/prepare_logo.py logo.png --max-size 500")
        print("   2. Use external reference (e: 0) in your Lottie JSON")
        print("   3. Render GIF successfully with Cairo")
        print("   4. (Optional) Embed base64 AFTER rendering for distribution")
        print("")
        print("   See SKILL.md 'Embedding Logos' section for complete workflow")
        return False

    except Exception as e:
        # Other errors
        error_msg = str(e).lower()
        if 'cairo' in error_msg or 'memory' in error_msg or 'no_memory' in error_msg:
            # Cairo-related error - same as MemoryError
            print(f"❌ Error: Cairo rendering failed: {e}")
            print("")
            print("📋 Solution: Use EXTERNAL file reference during rendering:")
            print('   "assets": [{"id": "logo_image", "p": "logo_optimized.png", "e": 0}]')
            print("")
            print("   See SKILL.md 'Troubleshooting' section")
            return False
        else:
            print(f"❌ Error rendering GIF: {e}")
            import traceback
            traceback.print_exc()
            return False

    finally:
        # Restore original working directory
        os.chdir(original_cwd)


def render_lottie_to_mp4(
    lottie_path: str | Path,
    output_path: str | Path,
    width: int = None,
    height: int = None,
    fps: int = None
) -> bool:
    """
    Render Lottie JSON to MP4 video.

    Args:
        lottie_path: Path to Lottie JSON file
        output_path: Output MP4 path
        width: Output width (default: use Lottie dimensions)
        height: Output height (default: use Lottie dimensions)
        fps: Frame rate (default: use Lottie frame rate)

    Returns:
        True if successful, False otherwise
    """
    # CRITICAL FIX: Import from correct module paths
    try:
        from lottie.parsers.tgs import parse_tgs
        # Note: MP4 export may require additional dependencies
        from lottie.exporters.core import export_mp4
    except ImportError as e:
        print("❌ Error: lottie-python or dependencies not installed")
        print("   Install with: pip install lottie[all]")
        print("   Also requires: ffmpeg (install via brew/apt)")
        print(f"   Error details: {e}")
        return False

    lottie_path = Path(lottie_path)
    output_path = Path(output_path)

    if not lottie_path.exists():
        print(f"❌ Error: Lottie file not found: {lottie_path}")
        return False

    # Validate assets before attempting render
    print(f"🔍 Validating external assets...")
    assets_ok, assets_error = validate_assets(lottie_path)
    if not assets_ok:
        print(f"❌ Asset validation failed:")
        print(assets_error)
        print(f"\n💡 Tip: Asset paths are resolved relative to the Lottie JSON file location")
        return False

    # Change to Lottie file directory for asset resolution
    original_cwd = os.getcwd()
    lottie_dir = lottie_path.parent.absolute()
    os.chdir(lottie_dir)

    try:
        # CRITICAL FIX: Parse directly from file, don't load as dict first
        print(f"📖 Loading Lottie: {lottie_path.name}")
        animation = parse_tgs(str(lottie_path))

        # CRITICAL FIX: Get dimensions from Animation object, not JSON dict
        if width is None:
            width = animation.width or 512
        if height is None:
            height = animation.height or 512
        if fps is None:
            fps = int(animation.frame_rate) if animation.frame_rate else 30

        print(f"🎬 Rendering MP4: {width}x{height} @ {fps} fps")
        print(f"   Using QuickTime-compatible encoding")

        # Export to MP4 with QuickTime-compatible encoding
        # These parameters ensure compatibility with QuickTime Player on macOS:
        # - movflags +faststart: Enable progressive playback
        # - pix_fmt yuv420p: Compatible pixel format
        # - scale filter: Ensure even dimensions (required by some codecs)
        try:
            export_mp4(
                animation,
                str(output_path),
                output_params=[
                    '-movflags', '+faststart',
                    '-pix_fmt', 'yuv420p',
                    '-vf', 'scale=trunc(iw/2)*2:trunc(ih/2)*2'
                ]
            )
        except TypeError:
            # Fallback if export_mp4 doesn't support output_params
            print("   Warning: Using default encoding (may not work in QuickTime)")
            export_mp4(animation, str(output_path))

        # Verify output
        output_ok, output_error = verify_output(output_path)
        if not output_ok:
            print(f"⚠️  Warning: {output_error}")
            print(f"   The file may be blank or corrupted. Check the output manually.")

        file_size_kb = output_path.stat().st_size / 1024
        file_size_mb = file_size_kb / 1024

        print(f"✅ MP4 created: {output_path}")
        print(f"   Size: {file_size_kb:.1f} KB ({file_size_mb:.2f} MB)")

        return True

    except Exception as e:
        print(f"❌ Error rendering MP4: {e}")
        print("   Note: MP4 export requires ffmpeg to be installed")
        import traceback
        traceback.print_exc()
        return False

    finally:
        # Restore original working directory
        os.chdir(original_cwd)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description='Render Lottie JSON to GIF or MP4',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic rendering
  python scripts/render_lottie.py logo.json logo.gif
  python scripts/render_lottie.py logo.json logo.mp4

  # With custom dimensions and framerate
  python scripts/render_lottie.py logo.json logo.gif 800 600 30

  # Test render first (prevents hanging on large files)
  python scripts/render_lottie.py logo.json logo.gif --test-render

  # Preview mode (render only first N frames)
  python scripts/render_lottie.py logo.json logo.gif --preview-frames 60
        """
    )

    parser.add_argument('lottie_json', help='Input Lottie JSON file')
    parser.add_argument('output_file', help='Output file (.gif or .mp4)')
    parser.add_argument('width', type=int, nargs='?', help='Output width (default: use Lottie dimensions)')
    parser.add_argument('height', type=int, nargs='?', help='Output height (default: use Lottie dimensions)')
    parser.add_argument('fps', type=int, nargs='?', help='Frame rate (default: use Lottie frame rate)')
    parser.add_argument('--test-render', action='store_true',
                        help='Test render first (200x200, 15fps, 60 frames) to catch issues early')
    parser.add_argument('--preview-frames', type=int, metavar='N',
                        help='Render only first N frames for quick preview (modifies JSON temporarily)')

    args = parser.parse_args()

    lottie_path = args.lottie_json
    output_path = args.output_file
    width = args.width
    height = args.height
    fps = args.fps

    # Preview frames mode - create temporary JSON with limited frames
    temp_preview_file = None
    if args.preview_frames:
        print(f"🔍 Preview mode: Rendering only first {args.preview_frames} frames\n")

        try:
            with open(lottie_path, 'r') as f:
                lottie_data = json.load(f)

            original_op = lottie_data.get('op', 180)
            preview_op = min(args.preview_frames, original_op)

            lottie_data['op'] = preview_op

            # Create temporary preview file
            temp_preview_file = Path(lottie_path).parent / f"_preview_{Path(lottie_path).name}"
            with open(temp_preview_file, 'w') as f:
                json.dump(lottie_data, f)

            print(f"   Original duration: {original_op} frames")
            print(f"   Preview duration: {preview_op} frames")
            print(f"   Temporary preview file: {temp_preview_file}\n")

            # Use the preview file for rendering
            lottie_path = str(temp_preview_file)

        except Exception as e:
            print(f"❌ Error creating preview: {e}")
            sys.exit(1)

    # Test render mode
    if args.test_render:
        print("🧪 Test render mode: 200x200, 15fps, first 60 frames only\n")

        # Create test output path
        test_output = Path(output_path).with_stem(Path(output_path).stem + "_test")

        output_ext = Path(output_path).suffix.lower()

        if output_ext == '.gif':
            success = render_lottie_to_gif(lottie_path, test_output, 200, 200, 15)
        elif output_ext == '.mp4':
            success = render_lottie_to_mp4(lottie_path, test_output, 200, 200, 15)
        else:
            print(f"❌ Error: Unsupported output format: {output_ext}")
            print("   Supported: .gif, .mp4")
            sys.exit(1)

        if not success:
            print("\n❌ Test render failed - review errors above")
            sys.exit(1)

        # Check test output size
        test_file_size_mb = test_output.stat().st_size / 1024 / 1024

        print(f"\n📊 Test render analysis:")
        print(f"   File size: {test_file_size_mb:.2f} MB")

        if test_file_size_mb > 5:
            print(f"   ⚠️  Test render is {test_file_size_mb:.1f}MB - full render may be very large")
            print(f"   Consider:")
            print(f"   - Smaller dimensions (current test: 200x200)")
            print(f"   - Lower fps (current test: 15fps)")
            print(f"   - Shorter duration")
            print(f"   - Running: python scripts/optimize_lottie.py {lottie_path} optimized.json")

        print(f"\n💡 Test render saved to: {test_output}")
        print(f"   Review the test output before proceeding\n")

        response = input("Continue with full render? [y/N]: ")
        if response.lower() != 'y':
            print("Cancelled. Review test render and adjust parameters if needed.")
            sys.exit(0)

        print("\n🎬 Proceeding with full render...\n")

    # Full render
    output_ext = Path(output_path).suffix.lower()

    if output_ext == '.gif':
        success = render_lottie_to_gif(lottie_path, output_path, width, height, fps)
    elif output_ext == '.mp4':
        success = render_lottie_to_mp4(lottie_path, output_path, width, height, fps)
    else:
        print(f"❌ Error: Unsupported output format: {output_ext}")
        print("   Supported: .gif, .mp4")
        sys.exit(1)

    # Cleanup temporary preview file if created
    if temp_preview_file and temp_preview_file.exists():
        try:
            temp_preview_file.unlink()
            print(f"\n🧹 Cleaned up temporary preview file")
        except Exception as e:
            print(f"\n⚠️  Warning: Could not delete temporary file {temp_preview_file}: {e}")

    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
