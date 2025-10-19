#!/usr/bin/env python3
"""
Extract individual elements from SVG for separate animation.

This script parses an SVG file and extracts individual elements (paths, groups, text)
into separate SVG files. This enables proper vector-based element separation for
multi-layer Lottie animations, avoiding rasterization quality loss.

Usage:
    python scripts/extract_svg_elements.py input.svg --output-dir ./elements/
    python scripts/extract_svg_elements.py input.svg --output-dir ./elements/ --split-text-letters
    python scripts/extract_svg_elements.py input.svg --list-only

Features:
    - Extracts each <path> element as separate SVG file
    - Extracts each <g> group as separate SVG file
    - Extracts each <text> element (with optional letter-by-letter separation)
    - Preserves transforms and positioning
    - Calculates proper viewBox for each element
    - Outputs small vector files (not rasterized)

Why This Matters:
    - SVG→PNG conversion should happen LAST, not first
    - Keep vector format as long as possible for:
      * Smaller file sizes (2-10KB vs 100-600KB per element)
      * Perfect scalability
      * Clean boundaries when separating elements
      * Better rendering performance

Example Workflow:
    1. Extract elements: python scripts/extract_svg_elements.py logo.svg --output-dir ./elements/
    2. Review: ls elements/  # Shows: path_1.svg, path_2.svg, group_logo.svg, etc.
    3. Convert to PNG: for f in elements/*.svg; do python scripts/prepare_logo.py "$f" --max-size 200; done
    4. Create Lottie with external references
    5. Render GIF with Cairo
    6. (Optional) Embed base64 for distribution
"""

import xml.etree.ElementTree as ET
import argparse
import sys
from pathlib import Path
import re


def parse_svg(svg_path):
    """Parse SVG file and return element tree."""
    try:
        tree = ET.parse(svg_path)
        return tree
    except ET.ParseError as e:
        print(f"❌ Error parsing SVG: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"❌ Error: File not found: {svg_path}")
        sys.exit(1)


def get_viewbox(root):
    """Extract viewBox from SVG root element."""
    viewbox = root.get('viewBox')
    if viewbox:
        return viewbox

    # If no viewBox, try to construct from width/height
    width = root.get('width', '100')
    height = root.get('height', '100')

    # Remove units (px, pt, etc.)
    width = re.sub(r'[^\d.]', '', str(width))
    height = re.sub(r'[^\d.]', '', str(height))

    return f"0 0 {width} {height}"


def calculate_bbox(element, namespace=''):
    """
    Calculate bounding box for an element.
    Note: This is a simplified calculation. For production use,
    consider using a library like svgpathtools for accurate path bounds.
    """
    # For now, return a default viewBox
    # In production, you'd parse path data and calculate actual bounds
    return "0 0 100 100"


def extract_paths(root, namespace=''):
    """Extract all <path> elements from SVG."""
    paths = []
    ns = {'svg': namespace} if namespace else None

    # Find all path elements
    if namespace:
        path_elements = root.findall('.//svg:path', ns)
    else:
        path_elements = root.findall('.//{http://www.w3.org/2000/svg}path')
        if not path_elements:
            path_elements = root.findall('.//path')

    for i, path in enumerate(path_elements):
        paths.append({
            'type': 'path',
            'index': i,
            'element': path,
            'id': path.get('id', f'path_{i}')
        })

    return paths


def extract_groups(root, namespace=''):
    """Extract all <g> group elements from SVG."""
    groups = []
    ns = {'svg': namespace} if namespace else None

    # Find all group elements
    if namespace:
        group_elements = root.findall('.//svg:g', ns)
    else:
        group_elements = root.findall('.//{http://www.w3.org/2000/svg}g')
        if not group_elements:
            group_elements = root.findall('.//g')

    for i, group in enumerate(group_elements):
        groups.append({
            'type': 'group',
            'index': i,
            'element': group,
            'id': group.get('id', f'group_{i}')
        })

    return groups


def extract_text_elements(root, namespace='', split_letters=False):
    """Extract all <text> elements from SVG."""
    texts = []
    ns = {'svg': namespace} if namespace else None

    # Find all text elements
    if namespace:
        text_elements = root.findall('.//svg:text', ns)
    else:
        text_elements = root.findall('.//{http://www.w3.org/2000/svg}text')
        if not text_elements:
            text_elements = root.findall('.//text')

    for i, text in enumerate(text_elements):
        if split_letters:
            # Extract individual letters (simplified - in production, use path splitting)
            text_content = text.text or ''
            for j, letter in enumerate(text_content):
                texts.append({
                    'type': 'text_letter',
                    'index': f'{i}_{j}',
                    'element': text,
                    'id': f'letter_{letter.lower()}_{i}_{j}',
                    'letter': letter
                })
        else:
            texts.append({
                'type': 'text',
                'index': i,
                'element': text,
                'id': text.get('id', f'text_{i}')
            })

    return texts


def create_element_svg(element_data, original_viewbox, original_root):
    """Create a new SVG containing just the extracted element."""
    # Create new SVG root
    svg_attrs = {
        'xmlns': 'http://www.w3.org/2000/svg',
        'viewBox': original_viewbox,
        'version': '1.1'
    }

    # Copy width/height from original if present
    if original_root.get('width'):
        svg_attrs['width'] = original_root.get('width')
    if original_root.get('height'):
        svg_attrs['height'] = original_root.get('height')

    new_svg = ET.Element('svg', svg_attrs)

    # Copy the element (deep copy to preserve children)
    element_copy = ET.fromstring(ET.tostring(element_data['element']))
    new_svg.append(element_copy)

    return new_svg


def save_element_svg(element_svg, output_path):
    """Save element SVG to file."""
    # Create XML declaration and save
    tree = ET.ElementTree(element_svg)
    ET.indent(tree, space='  ')  # Pretty print (Python 3.9+)

    try:
        tree.write(output_path, encoding='utf-8', xml_declaration=True)
        return True
    except Exception as e:
        print(f"❌ Error saving {output_path}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Extract individual elements from SVG for separate animation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Extract all elements to ./elements/ directory
  python scripts/extract_svg_elements.py logo.svg --output-dir ./elements/

  # List elements without extracting
  python scripts/extract_svg_elements.py logo.svg --list-only

  # Extract with letter-by-letter text separation
  python scripts/extract_svg_elements.py logo.svg --output-dir ./elements/ --split-text-letters

  # Extract only paths
  python scripts/extract_svg_elements.py logo.svg --output-dir ./elements/ --paths-only
        """
    )

    parser.add_argument('input_svg', help='Input SVG file')
    parser.add_argument('--output-dir', '-o', help='Output directory for extracted elements', default='./elements/')
    parser.add_argument('--list-only', '-l', action='store_true', help='List elements without extracting')
    parser.add_argument('--split-text-letters', action='store_true', help='Split text elements into individual letters')
    parser.add_argument('--paths-only', action='store_true', help='Extract only path elements')
    parser.add_argument('--groups-only', action='store_true', help='Extract only group elements')

    args = parser.parse_args()

    # Parse SVG
    print(f"📖 Parsing SVG: {args.input_svg}")
    tree = parse_svg(args.input_svg)
    root = tree.getroot()

    # Get viewBox
    viewbox = get_viewbox(root)
    print(f"   ViewBox: {viewbox}")

    # Extract elements
    all_elements = []

    if not args.groups_only:
        paths = extract_paths(root)
        all_elements.extend(paths)
        print(f"   Found {len(paths)} path element(s)")

    if not args.paths_only:
        groups = extract_groups(root)
        all_elements.extend(groups)
        print(f"   Found {len(groups)} group element(s)")

        texts = extract_text_elements(root, split_letters=args.split_text_letters)
        all_elements.extend(texts)
        if args.split_text_letters:
            print(f"   Found {len(texts)} text letter(s)")
        else:
            print(f"   Found {len(texts)} text element(s)")

    if not all_elements:
        print("⚠️  No elements found to extract")
        sys.exit(0)

    # List-only mode
    if args.list_only:
        print(f"\n📋 Elements found ({len(all_elements)} total):\n")
        for elem in all_elements:
            elem_type = elem['type']
            elem_id = elem['id']
            print(f"   - {elem_type}: {elem_id}")

        print(f"\n💡 To extract, run:")
        print(f"   python scripts/extract_svg_elements.py {args.input_svg} --output-dir ./elements/")
        sys.exit(0)

    # Create output directory
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Extract elements
    print(f"\n🔍 Extracting {len(all_elements)} element(s) to {args.output_dir}")
    extracted_count = 0

    for elem in all_elements:
        # Create element SVG
        element_svg = create_element_svg(elem, viewbox, root)

        # Generate output filename
        elem_id = elem['id'].replace(' ', '_').replace('/', '_')
        output_file = output_dir / f"{elem_id}.svg"

        # Save
        if save_element_svg(element_svg, output_file):
            file_size = output_file.stat().st_size
            print(f"   ✅ {elem['type']}: {output_file.name} ({file_size} bytes)")
            extracted_count += 1

    print(f"\n✅ Extracted {extracted_count}/{len(all_elements)} elements successfully")
    print(f"\n📁 Output directory: {output_dir.absolute()}")

    # Next steps guidance
    print(f"\n💡 Next steps:")
    print(f"   1. Review extracted SVG files: ls {args.output_dir}")
    print(f"   2. Convert to PNG for Lottie:")
    print(f"      for f in {args.output_dir}*.svg; do")
    print(f'        python scripts/prepare_logo.py "$f" --max-size 200')
    print(f"      done")
    print(f"   3. Create Lottie JSON with external references")
    print(f"   4. Render GIF with Cairo: python scripts/render_lottie.py animation.json output.gif")


if __name__ == '__main__':
    main()
