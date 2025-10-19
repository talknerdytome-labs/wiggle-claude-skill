# Script Usage Guide

Comprehensive documentation for all wiggle skill helper scripts.

## Quick Reference

| Script | Purpose | Common Usage |
|--------|---------|--------------|
| prepare_logo.py | Optimize images for Lottie | `prepare_logo.py logo.png --max-size 500` |
| **extract_svg_elements.py** | **Extract SVG elements for multi-layer animation** | `extract_svg_elements.py logo.svg --output-dir ./elements/` |
| validate_logo.py | Check logo compatibility | `validate_logo.py logo.png` |
| validate_lottie.py | Verify Lottie JSON structure | `validate_lottie.py animation.json` |
| **verify_animation.py** | **Verify animation matches expectations** | `verify_animation.py animation.json --expect-layers 5` |
| validate_loop.py | Check loop continuity | `validate_loop.py animation.json` |
| render_lottie.py | Convert Lottie to GIF/MP4 | `render_lottie.py animation.json output.gif` |
| convert_logo_to_svg.py | Raster to vector conversion | `convert_logo_to_svg.py logo.png logo.svg` |
| optimize_lottie.py | Reduce file size | `optimize_lottie.py animation.json optimized.json` |
| batch_export.py | Export multiple formats | `batch_export.py animation.json ./output gif,mp4` |
| check_dependencies.py | Verify installation | `check_dependencies.py` |

---

## Image Preparation & Validation

### prepare_logo.py

Optimize and prepare logo images for Lottie animation. This is the RECOMMENDED FIRST STEP before creating animations.

#### Usage

```bash
python scripts/prepare_logo.py <input> [options]
```

#### Arguments

- `input` (required): Path to input image (PNG, JPG, GIF, BMP)
- `--max-size SIZE`: Maximum dimension (width or height) in pixels
- `--optimize`: Enable PNG compression optimization (default: True)
- `--no-optimize`: Disable PNG optimization
- `--base64-only`: Only generate base64, skip optimized PNG
- `--output-dir DIR`: Output directory (default: same as input)

#### Examples

```bash
# Basic optimization
python scripts/prepare_logo.py logo.png

# Resize to max 500px and optimize
python scripts/prepare_logo.py logo.png --max-size 500 --optimize

# Aggressive optimization for small size
python scripts/prepare_logo.py logo.png --max-size 400 --optimize

# Only generate base64 (no optimized PNG)
python scripts/prepare_logo.py logo.png --base64-only

# Save to specific directory
python scripts/prepare_logo.py logo.png --output-dir ./prepared
```

#### Output Files

- `{name}_optimized.png`: Optimized PNG file with RGBA mode
- `{name}_base64.txt`: Base64 data URL for embedding in Lottie JSON

#### Features

- Automatic resize to optimal dimensions
- PNG compression optimization (level 9)
- RGBA mode conversion (ensures transparency)
- File size warnings (>100KB triggers Cairo warning)
- Recommendations for further optimization
- Usage examples for Lottie JSON

#### What It Checks

✅ Original file size and compression opportunities
✅ Color mode and transparency
✅ Image dimensions (warns if too large)
✅ Potential Cairo rendering issues
✅ Base64 encoded size

#### Typical Workflow

1. Run `prepare_logo.py` FIRST before any animation work
2. Use the `_optimized.png` in Lottie JSON as external reference
3. After successful rendering, replace with `_base64.txt` contents for distribution

---

### validate_logo.py

Check logo file compatibility before creating animations.

#### Usage

```bash
python scripts/validate_logo.py <logo_path>
```

#### Arguments

- `logo_path` (required): Path to logo file (PNG, SVG, JPG)

#### What It Validates

✅ File format (PNG/SVG/JPG supported)
✅ Alpha channel presence (transparency)
✅ Image dimensions
✅ File size
✅ Color mode

#### Example Output

```
🔍 Validating logo: logo.png

✓ Valid image file
✓ Format: PNG
✓ Dimensions: 512x512
✓ Has transparency: Yes
✓ File size: 45.2 KB

✅ Logo is valid and ready for animation
```

#### Warnings

- Missing alpha channel (suggests adding transparency)
- Very large dimensions (>2048px)
- Very small dimensions (<100px)
- Large file size (>500KB)

---

### extract_svg_elements.py

Extract individual elements from SVG files for multi-layer animation. Essential for proper SVG-first workflow when animating letters, icons, or logo components separately.

#### Usage

```bash
python scripts/extract_svg_elements.py <input.svg> --output-dir <directory>
python scripts/extract_svg_elements.py <input.svg> --list-only
python scripts/extract_svg_elements.py <input.svg> --output-dir ./elements/ --split-text-letters
```

#### Arguments

- `input.svg` (required): SVG file to extract elements from
- `--output-dir`, `-o`: Output directory for extracted SVG files (default: `./elements/`)
- `--list-only`, `-l`: List elements without extracting (preview mode)
- `--split-text-letters`: Split text elements into individual letters
- `--paths-only`: Extract only path elements
- `--groups-only`: Extract only group elements

#### Why This Script Matters

**Problem**: Converting SVG→PNG→Pixel cropping results in:
- Large file sizes (100-600KB per element)
- Quality loss and fuzzy edges
- Cairo MemoryError during rendering

**Solution**: Extract SVG elements → Convert to small PNGs (100-200px) → Clean multi-layer animation
- File sizes: 2-10KB per element
- Perfect boundaries
- Cairo renders smoothly

#### Example Workflow

```bash
# 1. Preview elements
python scripts/extract_svg_elements.py logo.svg --list-only

# Output:
#   Found 5 path elements
#   - path: letter_c
#   - path: letter_a
#   - path: letter_n
#   - path: letter_v
#   - path: letter_a

# 2. Extract all elements
python scripts/extract_svg_elements.py logo.svg --output-dir ./elements/

# 3. Convert each to small PNG
for f in elements/*.svg; do
  python scripts/prepare_logo.py "$f" --max-size 200
done

# 4. Create Lottie with 5 layers (one per element)
# 5. Render with Cairo - no MemoryError!
```

#### Output Example

```
📖 Parsing SVG: logo.svg
   ViewBox: 0 0 100 100
   Found 5 path element(s)
   Found 1 group element(s)

🔍 Extracting 6 element(s) to ./elements/
   ✅ path: letter_c.svg (842 bytes)
   ✅ path: letter_a.svg (756 bytes)
   ✅ path: letter_n.svg (923 bytes)
   ✅ path: letter_v.svg (801 bytes)
   ✅ path: letter_a_1.svg (756 bytes)
   ✅ group: logo_group.svg (2.1 KB)

✅ Extracted 6/6 elements successfully

💡 Next steps:
   1. Review extracted SVG files: ls ./elements/
   2. Convert to PNG for Lottie:
      for f in ./elements/*.svg; do
        python scripts/prepare_logo.py "$f" --max-size 200
      done
```

#### When to Use

✅ **Use this script when**:
- User requests "animate each letter separately"
- Multi-element logo animation (icons, components)
- Text-based logo letter animation
- SVG source file is available

❌ **Don't use when**:
- Only have PNG/JPG (no SVG)
- Single logo animation (no element separation needed)
- Photo-realistic content

#### File Size Comparison

| Approach | Per-Element | Total | Lottie JSON |
|----------|-------------|-------|-------------|
| **SVG extraction** | 3-8KB PNG | 15-40KB | 50-100KB ✅ |
| **PNG pixel cropping** | 100-600KB | 500KB-3MB | 600KB-3MB ❌ |

---

## Lottie JSON Validation

### validate_lottie.py

Verify Lottie JSON structure, properties, and catch potential issues.

#### Usage

```bash
python scripts/validate_lottie.py <lottie_path>
```

#### Arguments

- `lottie_path` (required): Path to Lottie JSON file

#### What It Validates

**Required Properties**:
- ✅ Valid JSON syntax
- ✅ Lottie version (`v`)
- ✅ Frame rate (`fr`)
- ✅ In/out points (`ip`, `op`)
- ✅ Dimensions (`w`, `h`)
- ✅ Layers array

**Quality Checks**:
- Frame rate (warns if <15 or >120 fps)
- Duration (warns if <1s or >10s)
- Dimensions (warns if too small or large)
- Layer count (warns if >50 layers)
- **Asset sizes** (warns if embedded images >100KB)

#### Example Output

```
🔍 Validating Lottie JSON: animation.json

✓ Valid JSON file
✓ All required Lottie properties present
✓ Lottie version: 5.7.4
✓ Frame rate: 30 fps
✓ Duration: 3.0 seconds (90 frames)
✓ Dimensions: 800x800
✓ 2 layer(s)
✓ 1 asset(s)
⚠ Asset 0 (logo_image): 120.5KB embedded - may cause Cairo issues

✅ Lottie file is valid

⚠️ 1 warning(s):
   - Asset "logo_image" (512x512): Large embedded image (120.5KB).
     May cause Cairo rendering issues. Consider:
     1) Use external file reference for rendering
     2) Optimize with prepare_logo.py
```

#### Asset Size Warnings

- **>100KB**: May cause Cairo MemoryError
- **>500KB**: Very large, strongly recommend optimization

Provides specific remediation steps for each issue.

---

### verify_animation.py

Verify Lottie animation matches described approach. Catches promise-implementation mismatches before rendering.

#### Usage

```bash
python scripts/verify_animation.py <lottie.json>
python scripts/verify_animation.py <lottie.json> --expect-layers 5
python scripts/verify_animation.py <lottie.json> --expect-sequential
python scripts/verify_animation.py <lottie.json> --expect-layers 5 --expect-sequential --max-size 300
```

#### Arguments

- `lottie_json` (required): Lottie JSON file to verify
- `--expect-layers N`: Expected number of layers (checks layer count)
- `--expect-sequential`: Expect sequential/staggered timing (not simultaneous)
- `--max-size KB`: Maximum file size in KB (e.g., 200, 300)

#### Why This Script Matters

**Problem**: Describing "I'll animate each element separately" then implementing everything as one layer.

**Solution**: Pre-render verification catches:
- Layer count mismatches
- Timing strategy mismatches (sequential vs simultaneous)
- File size issues before waiting for slow renders
- Missing asset references

#### Checks Performed

1. **Layer Count**: Matches expected element count
2. **Unique Asset References**: Each layer has unique refId
3. **Timing Strategy**: Sequential (staggered) vs simultaneous
4. **Asset References**: External (e: 0) vs embedded (e: 1)
5. **File Size**: Reasonable for complexity
6. **Animation Properties**: Duration, FPS, dimensions

#### Example Output

```bash
python scripts/verify_animation.py animation.json --expect-layers 5 --expect-sequential --max-size 200
```

**Output**:
```
📖 Loading Lottie: animation.json

✅ Animation has 5 layers (expected: 5)
✅ All 5 layer asset references are unique
❌ WARNING: All layers start at frame 0 (expected: sequential stagger)
   Described as sequential but implemented as simultaneous
⚠️  5 asset(s) are embedded (may cause Cairo MemoryError >100KB)
   Consider: Use external references during rendering, embed after
❌ WARNING: File size 618.3KB exceeds recommended 200KB
   Large files may cause rendering issues

📊 Animation Properties:
   Dimensions: 800x800
   Frame rate: 30 fps
   Duration: 3.00s (90 frames)

💡 Suggestions:
   1. Reduce file size:
      - Use external asset references during rendering
      - Run: python scripts/optimize_lottie.py animation.json optimized.json
      - Optimize images: python scripts/prepare_logo.py logo.png --max-size 600

   2. Asset optimization:
      - Change embedded assets (e: 1) to external references (e: 0)
      - Render GIF with external references
      - Embed base64 AFTER successful rendering if needed

   3. For sequential animation:
      - Add staggered start times (st property)
      - Example: layer 0 starts at frame 0, layer 1 at frame 10, etc.

⚠️  Review warnings above before rendering
```

#### Use Cases

**Before rendering complex animations**:
```bash
# Check if multi-element animation matches expectations
python scripts/verify_animation.py logo_letters.json --expect-layers 5 --expect-sequential
```

**Before test render**:
```bash
# Verify file size is reasonable
python scripts/verify_animation.py animation.json --max-size 300
```

**After creating Lottie JSON**:
```bash
# General validation
python scripts/verify_animation.py animation.json
```

#### Integration with render_lottie.py

Recommended workflow:
```bash
# 1. Verify before rendering
python scripts/verify_animation.py animation.json --expect-layers 5 --max-size 300

# 2. Fix any issues found

# 3. Test render
python scripts/render_lottie.py animation.json output.gif --test-render

# 4. Full render only after both pass
python scripts/render_lottie.py animation.json output.gif
```

---

### validate_loop.py

Ensure perfect loop continuity for infinite animations.

#### Usage

```bash
python scripts/validate_loop.py <lottie_path>
```

#### Arguments

- `lottie_path` (required): Path to Lottie JSON file

#### What It Checks

For each animated property, validates that first and last keyframe values match:

- Position (`p`)
- Scale (`s`)
- Rotation (`r`) - accounts for 360° wrapping
- Opacity (`o`)

#### Example Output

```
🔍 Validating loop continuity: animation.json

Layer 0: Logo
  ✓ Position: loops perfectly
  ✓ Scale: loops perfectly
  ✓ Rotation: loops perfectly (0° = 360°)
  ✓ Opacity: loops perfectly

✅ Animation loops perfectly
```

#### Loop Issues Example

```
Layer 0: Logo
  ✓ Position: loops perfectly
  ✗ Scale: loop mismatch
     First: [100, 100, 100]
     Last:  [100, 105, 100]
     Fix: Change last keyframe 's' to [100, 100, 100]

❌ Loop issues detected
   Check output above and fix keyframe values
```

#### Rotation Wrapping

The validator understands that 0° and 360° are equivalent for rotation, so these match:
- First: `[0]`, Last: `[360]` ✅
- First: `[360]`, Last: `[0]` ✅

---

## Rendering

### render_lottie.py

Convert Lottie JSON to GIF or MP4 with automatic fallback handling.

#### Usage

```bash
python scripts/render_lottie.py <input.json> <output.gif|mp4> [width] [height] [fps]
```

#### Arguments

- `input.json` (required): Path to Lottie JSON file
- `output` (required): Output file path (.gif or .mp4)
- `width` (optional): Output width in pixels (default: use Lottie dimensions)
- `height` (optional): Output height in pixels (default: use Lottie dimensions)
- `fps` (optional): Frame rate (default: use Lottie frame rate)
- `--test-render`: Test render first (200x200, 15fps) to catch issues before full render

#### Examples

```bash
# Basic GIF rendering (uses Lottie dimensions and fps)
python scripts/render_lottie.py animation.json output.gif

# GIF with custom dimensions
python scripts/render_lottie.py animation.json output.gif 800 600

# GIF with custom dimensions and fps
python scripts/render_lottie.py animation.json output.gif 800 600 30

# MP4 rendering
python scripts/render_lottie.py animation.json output.mp4

# MP4 with high quality
python scripts/render_lottie.py animation.json output.mp4 1920 1080 60

# Test render first (prevents hanging on large files)
python scripts/render_lottie.py animation.json output.gif --test-render
```

#### Test Render Feature

The `--test-render` flag performs an incremental rendering strategy:

1. **Creates test output** at 200x200, 15fps, first 60 frames
2. **Analyzes file size** - warns if test is >5MB (full render may be huge)
3. **Prompts for confirmation** before proceeding with full render
4. **Prevents hanging** on problematic animations

**Example workflow**:
```bash
python scripts/render_lottie.py logo.json logo.gif --test-render
```

**Output**:
```
🧪 Test render mode: 200x200, 15fps, first 60 frames only

📖 Loading Lottie: logo.json
🎬 Rendering GIF with Cairo: 200x200 @ 15 fps
✅ GIF created with Cairo: logo_test.gif
   Size: 450.2 KB

📊 Test render analysis:
   File size: 0.44 MB

💡 Test render saved to: logo_test.gif
   Review the test output before proceeding

Continue with full render? [y/N]:
```

**When test shows issues**:
```
⚠️  Test render is 6.2MB - full render may be very large
   Consider:
   - Smaller dimensions (current test: 200x200)
   - Lower fps (current test: 15fps)
   - Shorter duration
   - Running: python scripts/optimize_lottie.py animation.json optimized.json
```

#### Features

**Rendering**:
- Uses Cairo renderer for full easing support and quality
- On MemoryError with embedded images → shows helpful error message directing to external file references
- Clear messaging about render status

**Supported Formats**:
- **GIF**: Uses Cairo, good for web/social
- **MP4**: Requires ffmpeg, best quality and file size (QuickTime-compatible encoding)

#### Output Messages

**Success with Cairo**:
```
📖 Loading Lottie: animation.json
🎬 Rendering GIF with Cairo: 800x800 @ 30 fps
✅ GIF created with Cairo: output.gif
   Size: 1.2 MB
```

**Cairo MemoryError (embedded image too large)**:
```
📖 Loading Lottie: animation.json
🎬 Rendering GIF with Cairo: 800x800 @ 30 fps
❌ Error: Cairo MemoryError - Embedded image too large

📋 Solution: Use EXTERNAL file reference during rendering:
   "assets": [{"id": "logo_image", "p": "logo_optimized.png", "e": 0}]

   Steps:
   1. Run: python scripts/prepare_logo.py logo.png --max-size 500
   2. Use external reference (e: 0) in your Lottie JSON
   3. Render GIF successfully with Cairo
   4. (Optional) Embed base64 AFTER rendering for distribution
```

#### Requirements

- **GIF**: `lottie[all]` + Cairo for full quality
- **MP4**: `lottie[all]` + ffmpeg system package

---

## Conversion & Optimization

### convert_logo_to_svg.py

Convert raster logos (PNG/JPG) to vector SVG for better animation quality.

#### Usage

```bash
python scripts/convert_logo_to_svg.py <input> [output.svg] [threshold]
```

#### Arguments

- `input` (required): Path to raster image (PNG or JPG)
- `output` (optional): Output SVG path (default: `{input_name}.svg`)
- `threshold` (optional): Tracing threshold 0-255 (default: 128)

#### Examples

```bash
# Basic conversion
python scripts/convert_logo_to_svg.py logo.png

# Custom output path
python scripts/convert_logo_to_svg.py logo.png vector_logo.svg

# Adjust threshold for better tracing
python scripts/convert_logo_to_svg.py logo.png logo.svg 100
```

#### Requirements

**System dependency**: potrace

```bash
# macOS
brew install potrace

# Linux
sudo apt-get install potrace
```

#### Threshold Guide

- **Lower (50-100)**: More detail, more complex paths
- **Medium (100-150)**: Balanced detail
- **Higher (150-200)**: Simpler, cleaner paths

Experiment with different values to find the best result for your logo.

---

### optimize_lottie.py

Reduce Lottie JSON file size by removing redundant data and rounding values.

#### Usage

```bash
python scripts/optimize_lottie.py <input.json> [output.json] [decimal_places]
```

#### Arguments

- `input.json` (required): Path to Lottie JSON file
- `output.json` (optional): Output path (default: `{input}_optimized.json`)
- `decimal_places` (optional): Decimal precision 0-4 (default: 2)

#### Examples

```bash
# Basic optimization (2 decimal places)
python scripts/optimize_lottie.py animation.json

# Custom output path
python scripts/optimize_lottie.py animation.json optimized.json

# Aggressive optimization (1 decimal place)
python scripts/optimize_lottie.py animation.json optimized.json 1

# Maximum precision (4 decimal places)
python scripts/optimize_lottie.py animation.json optimized.json 4
```

#### Optimizations Applied

1. **Remove metadata**: Strips `nm` (name) fields
2. **Round numeric values**: Reduces decimal precision
3. **Remove empty arrays/objects**: Cleans up unused data
4. **Minify JSON**: Removes whitespace

#### File Size Comparison

Typical savings:
- **Before**: 250 KB (formatted JSON)
- **After**: 45 KB (optimized, 2 decimals)
- **Savings**: ~82%

#### Decimal Precision Trade-offs

| Decimals | Quality | File Size | Use Case |
|----------|---------|-----------|----------|
| 0 | Low | Smallest | Simple animations, mobile |
| 1 | Medium | Small | Most animations |
| 2 | High | Medium | Production (recommended) |
| 3-4 | Very High | Larger | Complex animations, precision needed |

---

## Batch Operations

### batch_export.py

Export Lottie animation to multiple formats at once.

#### Usage

```bash
python scripts/batch_export.py <input.json> [output_dir] [formats]
```

#### Arguments

- `input.json` (required): Path to Lottie JSON file
- `output_dir` (optional): Output directory (default: `./output`)
- `formats` (optional): Comma-separated formats (default: `gif,mp4,json`)

#### Examples

```bash
# Export all formats (GIF, MP4, optimized JSON)
python scripts/batch_export.py animation.json

# Custom output directory
python scripts/batch_export.py animation.json ./exports

# Specific formats only
python scripts/batch_export.py animation.json ./exports gif,json

# Only GIF
python scripts/batch_export.py animation.json ./exports gif
```

#### Supported Formats

- `gif`: Animated GIF (via render_lottie.py)
- `mp4`: MP4 video (requires ffmpeg)
- `json`: Optimized Lottie JSON (via optimize_lottie.py)

#### Output Structure

```
output/
  animation.gif
  animation.mp4
  animation_optimized.json
```

---

## Utilities

### check_dependencies.py

Verify all required dependencies are installed and provide installation instructions.

#### Usage

```bash
python scripts/check_dependencies.py
```

#### What It Checks

**Required Python Packages**:
- ✅ pillow (image processing)
- ✅ imageio (GIF creation)
- ✅ lottie (Lottie library)

**Lottie Library Imports**:
- ✅ parse_tgs (JSON parsing)
- ✅ export_gif (GIF export)
- ✅ export_mp4 (MP4 export)

**Optional System Tools**:
- ⚠️ cairo (full GIF rendering quality)
- ⚠️ ffmpeg (MP4 export)
- ⚠️ potrace (PNG→SVG conversion)

#### Example Output

```
🔍 Wiggle Skill Dependency Checker

============================================================
REQUIRED DEPENDENCIES
============================================================

📦 Python Packages:
✅ pillow: Installed
✅ imageio: Installed

📦 Checking lottie-python library...
✅ lottie: Base package installed
✅ lottie.parsers.tgs: parse_tgs available
✅ lottie.exporters.gif: export_gif available
⚠️ cairo: NOT installed (will use fallback renderer)
   For full quality:
     macOS: brew install cairo pkg-config && pip install pycairo
     Linux: sudo apt-get install libcairo2-dev pkg-config python3-dev && pip install pycairo
✅ lottie.exporters.core: export_mp4 available

============================================================
OPTIONAL DEPENDENCIES
============================================================

🔧 System Tools:
✅ ffmpeg (for MP4 export): Installed
⚠️ potrace (for PNG→SVG conversion): NOT installed
   macOS: brew install potrace | Linux: sudo apt-get install potrace

============================================================
SUMMARY
============================================================

✅ All required dependencies are installed!
   The skill is ready to use.

💡 Tips:
   - Cairo is optional but recommended for best GIF quality
   - FFmpeg is needed only for MP4 export
   - Potrace is needed only for PNG→SVG conversion

   Run this script again after installing dependencies to verify.
```

---

## Workflow Integration

### Recommended Workflow

**For New Animations**:

1. `prepare_logo.py logo.png --max-size 500`
2. `validate_logo.py logo_optimized.png`
3. Create Lottie JSON (use patterns from SKILL.md)
4. `validate_lottie.py animation.json`
5. `validate_loop.py animation.json` (if loop)
6. `render_lottie.py animation.json preview.gif`
7. `batch_export.py animation.json ./output`

**For Troubleshooting**:

1. `check_dependencies.py` - Verify setup
2. `validate_lottie.py animation.json` - Check for warnings
3. `prepare_logo.py logo.png --max-size 400` - Aggressive optimization for Cairo compatibility

**For Distribution**:

1. `optimize_lottie.py animation.json final.json 2`
2. Replace external references with base64 (from prepare_logo.py)
3. `validate_lottie.py final.json` - Final check
4. `batch_export.py final.json ./dist gif,mp4`

---

## Troubleshooting Scripts

### Script Won't Run

**Error**: `python: command not found`
- **Fix**: Use `python3` instead: `python3 scripts/validate_logo.py ...`

**Error**: `Permission denied`
- **Fix**: Make script executable: `chmod +x scripts/validate_logo.py`

**Error**: `No module named 'PIL'`
- **Fix**: Install dependencies: `pip install pillow imageio lottie[all]`

### Script-Specific Issues

**prepare_logo.py: "Unsupported format"**
- Only PNG, JPG, GIF, BMP supported
- Convert to PNG first if using other format

**render_lottie.py: Cairo MemoryError**
- This is expected with large embedded images (>100KB base64)
- Solution: Use external file references during rendering (`"e": 0`)
- Run `prepare_logo.py` to optimize images, then use external reference
- After successful rendering, you can embed base64 for distribution if needed

**convert_logo_to_svg.py: potrace not found**
- Install potrace: `brew install potrace` (macOS) or `sudo apt-get install potrace` (Linux)

**batch_export.py: MP4 export fails**
- Install ffmpeg: `brew install ffmpeg` (macOS) or `sudo apt-get install ffmpeg` (Linux)

---

## Advanced Usage

### Chaining Scripts

```bash
# Full pipeline
prepare_logo.py logo.png --max-size 500 && \
validate_logo.py logo_optimized.png && \
# ... create animation.json ... && \
validate_lottie.py animation.json && \
validate_loop.py animation.json && \
batch_export.py animation.json ./output
```

### Custom Parameters

Most scripts accept environment variables for advanced configuration. See script source code for details.

### Parallel Processing

For batch processing multiple animations:

```bash
for file in animations/*.json; do
  python scripts/render_lottie.py "$file" "output/$(basename $file .json).gif"
done
```
