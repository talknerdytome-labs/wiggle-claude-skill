# Troubleshooting Guide

Comprehensive solutions for common issues when creating logo animations.

## Table of Contents

- [GIF Rendering Issues](#gif-rendering-issues)
- [Cairo and Dependencies](#cairo-and-dependencies)
- [Loop Validation Problems](#loop-validation-problems)
- [Animation Quality Issues](#animation-quality-issues)
- [File Size Problems](#file-size-problems)
- [Script Errors](#script-errors)
- [Workflow Issues](#workflow-issues)

## GIF Rendering Issues

### MemoryError: "cairo returned CAIRO_STATUS_NO_MEMORY"

**Symptoms:**
- Script crashes during GIF rendering
- Error message mentions "out of memory" or "CAIRO_STATUS_NO_MEMORY"
- Large logo files (>100KB embedded base64)

**Root Cause:**
Cairo renderer has memory limitations when processing embedded base64 PNG images, especially:
- Images >100KB embedded size
- High-resolution logos (>1024px)
- Complex PNG structures with alpha channels

**Solution: Use External File Reference (REQUIRED)**

```json
// ❌ DON'T: Embedded base64 (causes MemoryError)
"assets": [{
  "id": "logo_image",
  "w": 512,
  "h": 256,
  "p": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAA...",  // Long base64
  "e": 1  // 1 = embedded
}]

// ✅ DO: External file reference (works perfectly)
"assets": [{
  "id": "logo_image",
  "w": 512,
  "h": 256,
  "p": "logo_optimized.png",  // External file path
  "e": 0  // 0 = external (not embedded)
}]
```

**Step-by-Step Fix:**

1. **Optimize logo first:**
   ```bash
   python scripts/prepare_logo.py logo.png --max-size 500 --optimize
   # Creates: logo_optimized.png (small, <50KB)
   ```

2. **Use external reference in Lottie JSON:**
   - Set `"e": 0` in assets
   - Use filename path in `"p"` field

3. **Render GIF successfully:**
   ```bash
   python scripts/render_lottie.py animation.json output.gif
   # No MemoryError! Cairo handles external files perfectly
   ```

4. **Optional: Embed base64 AFTER rendering for distribution:**
   - Only if you need standalone JSON file
   - Replace external path with base64 from `logo_base64.txt`
   - But keep external version for future edits/rendering

**Why This Works:**
- ✅ Cairo works perfectly with external file references
- ✅ Full easing curve support (no simplified rendering)
- ✅ All Lottie features supported
- ✅ Better error messages if something goes wrong
- ✅ Faster rendering times

**Prevention:**
- Run `validate_lottie.py` before rendering - it warns about large embedded assets
- Keep embedded images under 100KB for final distribution
- **Always use external references during ALL development/rendering**

---

### Blank/Empty GIF Output

**Symptoms:**
- GIF renders without errors but shows blank frames
- File size is very small (<10KB)
- Lottie JSON is valid

**Common Causes:**

**1. Incorrect Asset Paths:**
```bash
# Check if image exists
ls -lh logo_optimized.png

# Verify image path in Lottie JSON matches actual file
grep '"p":' animation.json
```

**Solution:** Use absolute paths or ensure images are in same directory as JSON file.

**2. Missing Asset References:**
```json
// Check that refId matches asset id
"layers": [{
  "refId": "logo_image"  // Must match asset id below
}],
"assets": [{
  "id": "logo_image"  // Must match refId above
}]
```

**3. Incomplete Base64 Data:**
```bash
# If using embedded base64, verify it's complete
grep '"p": "data:image' animation.json | head -c 100
# Should show: "p": "data:image/png;base64,iVBORw0KG..."
```

**4. Layer Visibility Issues:**
```json
// Check opacity is not 0
"o": {"a": 0, "k": 100}  // ✅ Visible
"o": {"a": 0, "k": 0}    // ❌ Invisible!
```

**Debugging Steps:**
```bash
# 1. Validate Lottie structure
python scripts/validate_lottie.py animation.json

# 2. Check image can be loaded
python3 -c "from PIL import Image; img = Image.open('logo.png'); print(f'{img.size} OK')"

# 3. Test with simple animation first
# Create minimal test JSON with just opacity fade

# 4. Render with verbose output
python scripts/render_lottie.py animation.json test.gif --verbose
```

---

### Choppy/Low Quality Animation

**Symptoms:**
- Animation looks stuttery or mechanical
- Motion is not smooth
- GIF playback is jumpy

**Solutions:**

**1. Increase Frame Rate:**
```bash
# Default (often 30fps)
python scripts/render_lottie.py animation.json output.gif

# Higher quality (60fps)
python scripts/render_lottie.py animation.json output.gif 800 600 60
```

**2. Add More Keyframes for Organic Motion:**
```json
// ❌ Too few keyframes (stuttery)
"k": [
  {"t": 0, "s": [100]},
  {"t": 90, "s": [110]}
]

// ✅ More keyframes (smoother) - especially for continuous motion
"k": [
  {"t": 0, "s": [100], "e": [103]},
  {"t": 15, "s": [103], "e": [106]},
  {"t": 30, "s": [106], "e": [108]},
  {"t": 45, "s": [108], "e": [106]},
  {"t": 60, "s": [106], "e": [103]},
  {"t": 75, "s": [103], "e": [100]},
  {"t": 90, "s": [100]}
]
```

**3. Use Better Easing Curves:**
```json
// ❌ Linear easing (mechanical)
"i": {"x": [1], "y": [1]}, "o": {"x": [0], "y": [0]}

// ✅ Ease-in-out (smooth)
"i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}

// ✅ Organic easing (for waveforms/continuous motion)
"i": {"x": [0.25], "y": [1]}, "o": {"x": [0.75], "y": [0]}
```

**4. Use MP4 Instead of GIF:**
```bash
# GIFs have limited color palette and compression
python scripts/render_lottie.py animation.json output.mp4

# Or batch export
python scripts/batch_export.py animation.json ./output mp4
```

**5. Increase Render Dimensions:**
```bash
# Render at 2x size then scale down
python scripts/render_lottie.py animation.json output.gif 1600 1200 60
# Then scale to 800x600 in post-processing
```

---

## Cairo and Dependencies

### "Cairo not available" Error

**Solution for macOS:**
```bash
# Install Cairo with Homebrew
brew install cairo pkg-config

# Install Python bindings
pip install pycairo

# Verify installation
python3 -c "import cairo; print('Cairo OK')"
```

**Solution for Linux (Ubuntu/Debian):**
```bash
# Install Cairo development libraries
sudo apt-get update
sudo apt-get install libcairo2-dev pkg-config python3-dev

# Install Python bindings
pip install pycairo

# Verify
python3 -c "import cairo; print('Cairo OK')"
```

**Solution for Windows:**
```bash
# Download Cairo from https://www.cairographics.org/
# Or use pre-built wheel:
pip install pipwin
pipwin install pycairo

# Verify
python -c "import cairo; print('Cairo OK')"
```

---

### "lottie-python not installed" Error

**Solution:**
```bash
# Install with all optional dependencies
pip install lottie[all]

# Verify installation
python3 -c "from lottie.parsers.tgs import parse_tgs; print('Lottie OK')"

# If still errors, try upgrading
pip install --upgrade lottie[all]
```

**Specific Import Errors:**

```bash
# ImportError: No module named 'lottie.exporters.gif'
pip install pillow  # Required for GIF export

# ImportError: No module named 'lottie.exporters.cairo'
pip install pycairo  # See Cairo installation above
```

---

### Pillow/PIL Issues

**Error: "cannot import name 'Image' from 'PIL'"**

**Solution:**
```bash
# Uninstall conflicting packages
pip uninstall PIL Pillow

# Reinstall Pillow
pip install Pillow

# Verify
python3 -c "from PIL import Image; print('Pillow OK')"
```

---

## Loop Validation Problems

### "Loop issues detected" Warning

**Symptoms:**
```bash
python scripts/validate_loop.py animation.json
# Output:
# ❌ Scale: First [100,100], Last [102,102] - MISMATCH!
```

**Cause:**
First and last keyframe values don't match - loop will have visible "jump".

**Solution:**
```json
// ❌ Loop will jump (last frame doesn't match first)
"s": {
  "a": 1,
  "k": [
    {"t": 0, "s": [100, 100], "e": [105, 105]},
    {"t": 90, "s": [105, 105], "e": [100, 100]},
    {"t": 180, "s": [102, 102]}  // ❌ Should be [100, 100]!
  ]
}

// ✅ Perfect loop (last matches first)
"s": {
  "a": 1,
  "k": [
    {"t": 0, "s": [100, 100], "e": [105, 105]},
    {"t": 90, "s": [105, 105], "e": [100, 100]},
    {"t": 180, "s": [100, 100]}  // ✅ Matches t:0
  ]
}
```

**Validation Workflow:**
```bash
# 1. Create animation with loop
# 2. Validate BEFORE rendering
python scripts/validate_loop.py animation.json

# 3. Fix any mismatches identified
# 4. Re-validate
python scripts/validate_loop.py animation.json
# ✅ Perfect loop! All properties match.

# 5. Render
python scripts/render_lottie.py animation.json output.gif
```

**Special Case: Rotation Loops:**
```json
// For 360° rotation, these are equivalent:
{"t": 0, "s": [0]}    // Start
{"t": 300, "s": [360]}  // End (visually identical to 0°)

// Script accounts for 360° wrapping
```

---

### "AttributeError: 'int' object has no attribute 'get'"

**Cause:**
Older versions of `validate_loop.py` didn't handle static properties (`"a": 0`) correctly.

**Solution:**
```bash
# Ensure you have latest version of validate_loop.py
# Script now properly handles both:
# - Animated properties: "a": 1
# - Static properties: "a": 0
```

**Workaround if using old script:**
```json
// Convert static to animated with single keyframe
// Old (causes error):
"o": {"a": 0, "k": 100}

// New (works with old script):
"o": {"a": 1, "k": [{"t": 0, "s": [100]}]}
```

---

## Animation Quality Issues

### Animation Doesn't Match Philosophy

**Problem:** Animation looks wrong for brand personality.

**Solution: Define Philosophy First**

Use the philosophy-first workflow before creating animation:

1. **What personality?** (playful, professional, bold, elegant)
2. **What emotion?** (excitement, trust, creativity, confidence)
3. **What motion metaphor?** (organic growth, burst, reveal, pulse)

**Examples:**

```
Corporate brand → Slow fade + gentle scale (0.42/0.58 easing, 8-12 keyframes)
Playful brand → Bounce + wiggle (bounce easing, 15-25 keyframes)
Audio brand → Waveform pulse (0.25/0.75 easing, 30-45 keyframes, 60fps)
```

See main SKILL.md "Animation Philosophy Creation" section.

---

### Motion Feels Mechanical/Robotic

**Cause:** Using linear easing or too few keyframes.

**Solution:**

```json
// ❌ Linear (robotic)
"i": {"x": [1], "y": [1]}, "o": {"x": [0], "y": [0]}

// ✅ Ease-in-out (natural)
"i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}

// ✅ Organic (for continuous motion)
"i": {"x": [0.25], "y": [1]}, "o": {"x": [0.75], "y": [0]}
```

**Add more keyframes for organic motion:**
- Corporate/Static: 8-12 keyframes
- Organic/Continuous: 25-45 keyframes
- Cinematic: 50-120 keyframes

---

### Text Looks Wrong/Different from Logo

**Problem:** Used PIL/ImageDraw to recreate text instead of extracting from logo.

**❌ NEVER DO THIS:**
```python
# Creates DIFFERENT text (wrong font, color, positioning)
from PIL import ImageDraw
draw.text((100, 100), "Logo Text", font=some_font)
```

**✅ ALWAYS DO THIS:**
```bash
# Extract ACTUAL text from logo SVG
python scripts/extract_svg_elements.py logo.svg --output-dir ./elements/
# Creates: elements/text_0.svg (your REAL logo text)

# Convert to PNG
python scripts/prepare_logo.py elements/text_0.svg --max-size 200
```

See [references/text_animation_guide.md](text_animation_guide.md) for complete workflow.

---

## File Size Problems

### GIF File Too Large (>5MB)

**Causes:**
- High frame rate (60fps+)
- Large dimensions (>1000px)
- Long duration (>5s)
- Many frames/complex animation

**Solutions:**

**1. Reduce Dimensions:**
```bash
# Instead of 1920x1080
python scripts/render_lottie.py animation.json output.gif 800 600 30
# Much smaller file, still good quality
```

**2. Reduce Frame Rate:**
```bash
# 60fps is often overkill for simple animations
python scripts/render_lottie.py animation.json output.gif 800 600 30
# 30fps is plenty for most logo animations
```

**3. Shorten Duration:**
```json
// 5s animation = lots of frames
"op": 300  // 10 seconds at 30fps = 300 frames

// 2-3s is usually optimal
"op": 90   // 3 seconds at 30fps = 90 frames
```

**4. Optimize Lottie JSON First:**
```bash
python scripts/optimize_lottie.py animation.json animation_optimized.json
# Removes unnecessary keyframes, rounds values
```

**5. Use MP4 Instead:**
```bash
# MP4 has MUCH better compression than GIF
python scripts/render_lottie.py animation.json output.mp4
# Often 10x smaller for same quality
```

**6. Reduce Color Palette (GIF-specific):**
```python
# When using Pillow for GIF export
image.save('output.gif', optimize=True, colors=128)
# Default is 256 colors, reducing to 128 saves space
```

---

### Lottie JSON File Too Large

**Cause:** Embedded base64 images or too many keyframes.

**Solutions:**

**1. Use External Image References:**
```json
// Small Lottie JSON (5-20KB)
"assets": [{"id": "logo", "p": "logo.png", "e": 0}]

// Large Lottie JSON (100KB+)
"assets": [{"id": "logo", "p": "data:image/png;base64,...", "e": 1}]
```

**2. Optimize Keyframes:**
```bash
python scripts/optimize_lottie.py animation.json animation_optimized.json
# Removes redundant keyframes, rounds numbers
```

**3. Reduce Precision:**
```python
# Round keyframe values to 2 decimal places instead of 10
100.123456789 → 100.12
```

---

## Script Errors

### ImportError: No module named 'lottie.exporters.gif'

**Cause:** Old error from previous script versions.

**Solution:**
```python
# ✅ Correct import (current version)
from lottie.exporters.gif import export_gif

# ❌ Incorrect import (old version)
from lottie.exporters import export_gif  # This module doesn't exist
```

Ensure you have latest script versions from `scripts/` directory.

---

### TypeError: 'dict' object has no attribute 'seek'

**Cause:** Passing JSON dict instead of filename to `parse_tgs()`.

**Solution:**
```python
# ❌ Wrong (passing dict)
with open('animation.json') as f:
    data = json.load(f)
    animation = parse_tgs(data)  # Error!

# ✅ Correct (passing filename)
animation = parse_tgs(str(lottie_path))
# OR
animation = parse_tgs('animation.json')
```

---

### "No such file or directory: logo_optimized.png"

**Cause:** Image path in Lottie JSON doesn't match actual file location.

**Solution:**

**1. Check file exists:**
```bash
ls -lh logo_optimized.png
# If missing, create it:
python scripts/prepare_logo.py logo.png --max-size 500 --optimize
```

**2. Use absolute paths:**
```json
// Relative path (can fail if CWD is wrong)
"p": "logo.png"

// Absolute path (always works)
"p": "/full/path/to/logo.png"
```

**3. Ensure same directory:**
```bash
# Put Lottie JSON and images in same folder
ls
# animation.json
# logo_optimized.png
# icon.png
# text.png
```

---

## Workflow Issues

### Forgot to Run Logo Analysis

**Problem:** Created animation without understanding logo structure - now have wrong approach.

**Solution:**
Always run analysis BEFORE creating animation:

```bash
# 1. Identify structure
python scripts/extract_svg_elements.py logo.svg --list
# Output shows: text elements, paths, groups, etc.

# 2. Decide on approach based on output
# - Single element → Animate as one
# - Multi-element → Extract and animate separately
# - Has text → See text_animation_guide.md

# 3. THEN create animation
```

See "Logo Analysis & Preparation" in main SKILL.md.

---

### Rendering Takes Forever

**Cause:** Creating full 3-5s animation at 60fps on first try.

**Solution: Use Preview Workflow**

```bash
# 1. Create SHORT test animation (1 cycle, 30-60 frames)
# Edit JSON: "op": 60 instead of "op": 180

# 2. Test render (takes 5 seconds instead of 2 minutes)
python scripts/render_lottie.py test.json preview.gif

# 3. Verify motion looks correct

# 4. If good → Extend to full duration and render
# Edit JSON: "op": 180
python scripts/render_lottie.py animation.json final.gif

# 5. If bad → Adjust and repeat from step 2
```

**Always test with preview before full render!**

---

### Multi-Element Animation Looks Wrong

**Problem:** Elements don't sync properly, timing feels off.

**Common Mistakes:**

**1. Different easing curves:**
```json
// ❌ Icon and text have different easing
Icon:  "i": {"x": [0.42], "y": [1]}
Text:  "i": {"x": [0.25], "y": [1]}  // Different!

// ✅ Same easing for simultaneous entrance
Both:  "i": {"x": [0.42], "y": [1]}
```

**2. Wrong stagger timing:**
```json
// For 30-frame stagger at 60fps (0.5s delay):
Icon: {"t": 0, "s": [0], "e": [100]}   // Starts immediately
Text: {"t": 30, "s": [0], "e": [100]}  // Starts 0.5s later
```

**3. Elements too large/small:**
```bash
# Extract elements at appropriate sizes
python scripts/prepare_logo.py icon.svg --max-size 200    # Small elements
python scripts/prepare_logo.py text.svg --max-size 300    # Text slightly larger
# NOT 1000px for everything!
```

See [references/detailed_examples.md](detailed_examples.md) for multi-element patterns.

---

## Quick Diagnostic Checklist

When something goes wrong, check these in order:

### Before Creating Animation:
- [ ] Ran logo analysis (`extract_svg_elements.py --list`)
- [ ] Defined motion philosophy (personality + emotion + metaphor)
- [ ] Identified text elements (if any)
- [ ] Chose appropriate motion type (Static/Organic/Cinematic)

### Before Rendering:
- [ ] Using external image references (`"e": 0`)
- [ ] Images are optimized (<100KB each)
- [ ] Validated Lottie JSON (`validate_lottie.py`)
- [ ] Validated loop if needed (`validate_loop.py`)
- [ ] Created preview first (30-60 frames)

### After Rendering Issues:
- [ ] Cairo installed correctly
- [ ] lottie-python installed with `[all]` extras
- [ ] Image paths are correct
- [ ] Frame rate appropriate (30fps usually fine)
- [ ] Duration reasonable (2-3s optimal)

### For Quality Issues:
- [ ] Easing curves used (not linear)
- [ ] Enough keyframes for motion type
- [ ] Philosophy matches brand personality
- [ ] Text extracted from logo (not recreated)

---

## Getting More Help

If issue persists after trying these solutions:

1. **Validate your files:**
   ```bash
   python scripts/validate_lottie.py animation.json
   python scripts/validate_loop.py animation.json
   ```

2. **Test with minimal example:**
   - Create simplest possible animation (single fade)
   - If that works, gradually add complexity
   - Identifies exactly where problem occurs

3. **Check dependencies:**
   ```bash
   python3 -c "import cairo; import lottie; from PIL import Image; print('All OK')"
   ```

4. **Read referenced docs:**
   - [lottie_spec.md](lottie_spec.md) - Lottie JSON format
   - [script_usage.md](script_usage.md) - Script parameters and options
   - [text_animation_guide.md](text_animation_guide.md) - Text-specific issues

---

## Related Documentation

- **Script Usage**: [references/script_usage.md](script_usage.md)
- **Text Animation**: [references/text_animation_guide.md](text_animation_guide.md)
- **Lottie Spec**: [references/lottie_spec.md](lottie_spec.md)
- **Examples**: [references/detailed_examples.md](detailed_examples.md)
