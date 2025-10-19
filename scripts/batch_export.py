#!/usr/bin/env python3
"""
Batch Exporter - Export Lottie animation to multiple formats at once

Exports:
- Lottie JSON (optimized)
- GIF preview
- MP4 video (optional)
- PNG frames (optional)
"""

import sys
import json
from pathlib import Path
import subprocess


def batch_export(
    lottie_path: str | Path,
    output_dir: str | Path = None,
    formats: list[str] = None,
    optimize: bool = True
) -> dict:
    """
    Export Lottie animation to multiple formats.

    Args:
        lottie_path: Path to Lottie JSON file
        output_dir: Output directory (default: same as input)
        formats: List of formats to export ['gif', 'mp4', 'json']
        optimize: Optimize Lottie JSON before export

    Returns:
        Dict with paths to exported files and any errors
    """
    lottie_path = Path(lottie_path)

    if not lottie_path.exists():
        return {'error': f'File not found: {lottie_path}'}

    if output_dir is None:
        output_dir = lottie_path.parent
    else:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

    if formats is None:
        formats = ['json', 'gif']  # Default: optimized JSON + GIF

    base_name = lottie_path.stem
    results = {
        'input': str(lottie_path),
        'output_dir': str(output_dir),
        'exports': {},
        'errors': []
    }

    # Get script directory (same directory as this script)
    script_dir = Path(__file__).parent

    # Export optimized JSON
    if 'json' in formats:
        json_output = output_dir / f"{base_name}_optimized.json"
        print(f"📦 Exporting optimized JSON...")

        if optimize:
            optimize_script = script_dir / 'optimize_lottie.py'
            if optimize_script.exists():
                try:
                    subprocess.run(
                        ['python3', str(optimize_script), str(lottie_path), str(json_output)],
                        check=True,
                        capture_output=True
                    )
                    results['exports']['json'] = str(json_output)
                    print(f"   ✓ JSON: {json_output}")
                except subprocess.CalledProcessError as e:
                    error_msg = f"JSON optimization failed: {e.stderr.decode()}"
                    results['errors'].append(error_msg)
                    print(f"   ✗ {error_msg}")
            else:
                # Fallback: just copy
                import shutil
                shutil.copy(lottie_path, json_output)
                results['exports']['json'] = str(json_output)
        else:
            # Just copy without optimization
            import shutil
            shutil.copy(lottie_path, json_output)
            results['exports']['json'] = str(json_output)
            print(f"   ✓ JSON: {json_output}")

    # Export GIF
    if 'gif' in formats:
        gif_output = output_dir / f"{base_name}.gif"
        print(f"🎬 Exporting GIF...")

        render_script = script_dir / 'render_lottie.py'
        if render_script.exists():
            try:
                subprocess.run(
                    ['python3', str(render_script), str(lottie_path), str(gif_output)],
                    check=True,
                    capture_output=True
                )
                results['exports']['gif'] = str(gif_output)
                print(f"   ✓ GIF: {gif_output}")
            except subprocess.CalledProcessError as e:
                error_msg = f"GIF render failed: {e.stderr.decode()}"
                results['errors'].append(error_msg)
                print(f"   ✗ {error_msg}")
        else:
            error_msg = "render_lottie.py not found"
            results['errors'].append(error_msg)
            print(f"   ✗ {error_msg}")

    # Export MP4
    if 'mp4' in formats:
        mp4_output = output_dir / f"{base_name}.mp4"
        print(f"🎥 Exporting MP4...")

        render_script = script_dir / 'render_lottie.py'
        if render_script.exists():
            try:
                subprocess.run(
                    ['python3', str(render_script), str(lottie_path), str(mp4_output)],
                    check=True,
                    capture_output=True
                )
                results['exports']['mp4'] = str(mp4_output)
                print(f"   ✓ MP4: {mp4_output}")
            except subprocess.CalledProcessError as e:
                error_msg = f"MP4 render failed (ffmpeg required): {e.stderr.decode()}"
                results['errors'].append(error_msg)
                print(f"   ✗ {error_msg}")
        else:
            error_msg = "render_lottie.py not found"
            results['errors'].append(error_msg)
            print(f"   ✗ {error_msg}")

    return results


def main():
    if len(sys.argv) < 2:
        print("Usage: batch_export.py <animation.json> [output_dir] [formats]")
        print("\nBatch export Lottie animation to multiple formats")
        print("\nExamples:")
        print("  batch_export.py logo.json")
        print("  batch_export.py logo.json ./output")
        print("  batch_export.py logo.json ./output gif,mp4,json")
        print("\nOptional:")
        print("  output_dir: Output directory (default: same as input)")
        print("  formats: Comma-separated list (default: json,gif)")
        print("           Options: json, gif, mp4")
        sys.exit(1)

    lottie_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    formats = sys.argv[3].split(',') if len(sys.argv) > 3 else ['json', 'gif']

    print(f"📦 Batch Export: {lottie_path}")
    print(f"   Formats: {', '.join(formats)}")
    if output_dir:
        print(f"   Output: {output_dir}")
    print()

    results = batch_export(lottie_path, output_dir, formats)

    print(f"\n✅ Export complete")
    print(f"   Exported {len(results['exports'])} file(s)")

    if results['errors']:
        print(f"\n⚠️  {len(results['errors'])} error(s):")
        for error in results['errors']:
            print(f"   - {error}")


if __name__ == "__main__":
    main()
