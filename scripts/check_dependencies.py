#!/usr/bin/env python3
"""
Dependency Checker - Verify all required dependencies are installed

Checks for:
- Python packages (lottie, pillow, imageio, etc.)
- System libraries (cairo, ffmpeg, potrace)
- Import paths and API availability

Run this after installation to verify setup.
"""

import sys
import subprocess
from pathlib import Path


def check_python_package(package_name: str, import_name: str = None) -> bool:
    """Check if a Python package is installed and importable."""
    if import_name is None:
        import_name = package_name

    try:
        __import__(import_name)
        print(f"✅ {package_name}: Installed")
        return True
    except ImportError:
        print(f"❌ {package_name}: NOT installed")
        print(f"   Install with: pip install {package_name}")
        return False


def check_lottie_library() -> bool:
    """Check lottie-python library with specific imports."""
    print("\n📦 Checking lottie-python library...")

    all_ok = True

    # Check base package
    try:
        import lottie
        print("✅ lottie: Base package installed")
    except ImportError:
        print("❌ lottie: NOT installed")
        print("   Install with: pip install lottie[all]")
        return False

    # Check parse_tgs
    try:
        from lottie.parsers.tgs import parse_tgs
        print("✅ lottie.parsers.tgs: parse_tgs available")
    except ImportError as e:
        print(f"❌ lottie.parsers.tgs: Import failed - {e}")
        all_ok = False

    # Check GIF export
    try:
        from lottie.exporters.gif import export_gif
        print("✅ lottie.exporters.gif: export_gif available")
    except ImportError as e:
        print(f"⚠️  lottie.exporters.gif: Import failed - {e}")
        print("   This is expected if Cairo is not installed")
        print("   Cairo is REQUIRED for GIF rendering")

    # Check Cairo
    try:
        import cairo
        print("✅ cairo: Installed (GIF rendering available)")
    except ImportError:
        print("⚠️  cairo: NOT installed (REQUIRED for GIF rendering)")
        print("   Installation:")
        print("     macOS: brew install cairo pkg-config && pip install pycairo")
        print("     Linux: sudo apt-get install libcairo2-dev pkg-config python3-dev && pip install pycairo")

    # Check MP4 export
    try:
        from lottie.exporters.core import export_mp4
        print("✅ lottie.exporters.core: export_mp4 available")
    except ImportError as e:
        print(f"⚠️  lottie.exporters.core: Import failed - {e}")
        print("   MP4 export may not be available")

    return all_ok


def check_system_command(command: str, package_name: str = None, install_hint: str = None) -> bool:
    """Check if a system command is available."""
    if package_name is None:
        package_name = command

    try:
        result = subprocess.run(
            [command, '--version'],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            print(f"✅ {package_name}: Installed")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    print(f"⚠️  {package_name}: NOT installed")
    if install_hint:
        print(f"   {install_hint}")
    return False


def main():
    print("🔍 Wiggle Skill Dependency Checker\n")

    print("=" * 60)
    print("REQUIRED DEPENDENCIES")
    print("=" * 60)

    required_ok = True

    # Python packages
    print("\n📦 Python Packages:")
    required_ok &= check_python_package("pillow", "PIL")
    required_ok &= check_python_package("imageio")

    # Lottie library
    required_ok &= check_lottie_library()

    print("\n" + "=" * 60)
    print("OPTIONAL DEPENDENCIES")
    print("=" * 60)

    print("\n🔧 System Tools:")

    # FFmpeg for MP4
    check_system_command(
        "ffmpeg",
        "ffmpeg (for MP4 export)",
        "macOS: brew install ffmpeg | Linux: sudo apt-get install ffmpeg"
    )

    # Potrace for PNG→SVG
    check_system_command(
        "potrace",
        "potrace (for PNG→SVG conversion)",
        "macOS: brew install potrace | Linux: sudo apt-get install potrace"
    )

    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)

    if required_ok:
        print("\n✅ All required dependencies are installed!")
        print("   The skill is ready to use.")
    else:
        print("\n❌ Some required dependencies are missing.")
        print("   Install missing packages before using the skill.")
        sys.exit(1)

    print("\n💡 Tips:")
    print("   - Cairo is optional but recommended for best GIF quality")
    print("   - FFmpeg is needed only for MP4 export")
    print("   - Potrace is needed only for PNG→SVG conversion")
    print("\n   Run this script again after installing dependencies to verify.")


if __name__ == "__main__":
    main()
