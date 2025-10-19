# Text in Logos - Complete Implementation Guide

**Purpose:** Detailed technical reference for animating text in logos. Load this when working with multi-element logos containing text.

**When to use:** Logo contains text elements that need animation or synchronization with icon elements.

## Text Type Identification

### Quick SVG Text Detection

```bash
python scripts/extract_svg_elements.py logo.svg --list-only
```

**Expected output examples:**
```
- text: text_0 (SVG <text> element - scalable, animatable)
- path: converted_text (Text converted to paths - what Canva uses)
- group: text_group (Text grouped with other elements)
```

### Text Type Comparison Table

| Text Type | Difficulty | Best Animation Method | File Size | Recommendation |
|-----------|-----------|----------------------|-----------|----------------|
| **SVG `<text>` element** | Medium | Fade-in, Transform, or Stroke reveal | 2-5KB | ✅ Extract as separate element |
| **SVG `<path>` (text-as-curves)** | Medium | Fade-in or Transform only | 3-8KB | ✅ Extract as separate element |
| **PNG/JPG text (rasterized)** | Easy-Medium | Fade-in or Transform only | 15-50KB | ✅ Extract if separate from icon |
| **Embedded font text** | Hard | Render to PNG first | N/A | ⚠️  Convert to PNG before animating |

---

## Method 1: Fade-In (Detailed Implementation)

### When to Use
- **Best for:** 90% of logo animations
- **Brand types:** Corporate, professional, modern, playful
- **Technical ease:** Simple (no complex calculations)
- **Time to implement:** 5-10 minutes

### Advantages
- ✅ Works with ANY text format (SVG text, paths, or PNG)
- ✅ Syncs easily with icon animations
- ✅ No stroke-dasharray calculations needed
- ✅ Compatible with all browsers/players

### Disadvantages
- ❌ Text becomes semi-transparent during fade (brief moment)
- ❌ Loses stroke outline detail during transition
- ❌ Less "premium" feel than stroke reveal

### Technical Implementation Steps

**Step 1: Extract Text Element**
```bash
# If SVG logo
python scripts/extract_svg_elements.py logo.svg --output-dir ./elements/

# Review extracted elements
ls elements/
# Output: circle.svg, text_0.svg, path_1.svg

# Identify which is the text element
python scripts/extract_svg_elements.py logo.svg --list-only
```

**Step 2: Convert to Optimized PNG**
```bash
# Size appropriately (200-300px for text elements)
python scripts/prepare_logo.py elements/text_0.svg --max-size 250

# Output: text_0_optimized.png (typically 5-20KB)
```

**Step 3: Create Lottie JSON Layer**

**Complete Lottie JSON Example:**
```json
{
  "v": "5.7.4",
  "fr": 60,
  "ip": 0,
  "op": 180,
  "w": 800,
  "h": 400,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Logo Text",
      "refId": "text_element",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {
              "t": 0,
              "s": [0],
              "e": [100],
              "i": {"x": [0.42], "y": [1]},
              "o": {"x": [0.58], "y": [0]}
            },
            {"t": 60, "s": [100]}
          ]
        },
        "p": {"a": 0, "k": [400, 200]},
        "a": {"a": 0, "k": [125, 40]},
        "s": {"a": 0, "k": [100, 100]},
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 180
    }
  ],
  "assets": [
    {
      "id": "text_element",
      "w": 250,
      "h": 80,
      "p": "text_0_optimized.png",
      "e": 0
    }
  ]
}
```

**Key Properties Explained:**
- `"o"`: Opacity animation (0→100%)
- `"t": 0`: Start at frame 0
- `"t": 60`: End at frame 60 (1 second at 60fps)
- `"i": {"x": [0.42], "y": [1]}`: Ease-in curve
- `"o": {"x": [0.58], "y": [0]}`: Ease-out curve
- `"e": 0`: External file reference (not embedded)

### Variations by Brand Philosophy

**Playful/Energetic (Canva, Figma):**
```json
{
  "o": {
    "k": [
      {"t": 0, "s": [0], "e": [100], "i": {"x": [0.25], "y": [1]}, "o": {"x": [0.75], "y": [0]}},
      {"t": 60, "s": [100]}
    ]
  },
  "s": {
    "k": [
      {"t": 0, "s": [70, 70], "e": [100, 100], "i": {"x": [0.25, 0.25], "y": [1, 1]}, "o": {"x": [0.75, 0.75], "y": [0, 0]}},
      {"t": 60, "s": [100, 100]}
    ]
  }
}
```
- Combines fade + scale for energy
- Softer easing (0.25/0.75) = more organic
- 1s duration = quick, modern

**Professional/Corporate (IBM, Deloitte):**
```json
{
  "o": {
    "k": [
      {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
      {"t": 90, "s": [100]}
    ]
  },
  "s": {"a": 0, "k": [100, 100]}
}
```
- Fade only, no scale
- Standard easing (0.42/0.58) = professional
- 1.5s duration = slower, deliberate

**Creative/Modern (Agencies, Startups):**
```json
{
  "o": {
    "k": [
      {"t": 0, "s": [0], "e": [100]},
      {"t": 60, "s": [100]}
    ]
  },
  "p": {
    "k": [
      {"t": 0, "s": [400, 220], "e": [400, 200]},
      {"t": 60, "s": [400, 200]}
    ]
  }
}
```
- Fade + subtle upward float
- Creates "rising" reveal effect
- Modern, sophisticated

---

## Method 2: Stroke Reveal (Advanced)

### When to Use
- **Best for:** Premium brands, luxury, hand-drawn aesthetics
- **Brand types:** Jewelry, fashion, high-end, editorial
- **Technical ease:** Hard (requires shape layers)
- **Time to implement:** 30-60 minutes

### Requirements
- SVG text must have `stroke` property (outline)
- Text in `<text>` element OR outlined paths with stroke data
- Cannot use rasterized text (PNG/JPG)
- Requires Lottie shape layers (not image layers)

### Technical Limitations
- ❌ Won't work if text is filled `<path>` without stroke
- ❌ Complex to implement (stroke-dasharray calculations)
- ❌ May not render consistently across all players
- ❌ Not suitable for time-constrained projects

### Implementation (Shape Layer Approach)

**Step 1: Verify Text Has Stroke**
```bash
# Check SVG source
grep -i "stroke" logo.svg

# Should see something like:
# <text stroke="#000000" stroke-width="2">Brand Name</text>
```

**Step 2: Convert to Shape Layer Path**

This requires manual path extraction or using Lottie shape layers with Trim Path modifier. See Pattern #9 in SKILL.md for draw-on effect implementation.

**Not recommended for first-time users** - use fade-in method instead unless client specifically requests stroke reveal.

---

## Method 3: Transform Entrance (Scale/Rotate)

### When to Use
- **Best for:** Energetic brands, tech companies, dynamic feel
- **Brand types:** Startups, tech products, creative agencies
- **Technical ease:** Medium
- **Time to implement:** 10-15 minutes

### Complete Implementation

**Scale Entrance:**
```json
{
  "ind": 1,
  "ty": 2,
  "nm": "Text Scale Entrance",
  "refId": "text_element",
  "ks": {
    "o": {
      "a": 1,
      "k": [
        {"t": 0, "s": [0], "e": [100]},
        {"t": 45, "s": [100]}
      ]
    },
    "s": {
      "a": 1,
      "k": [
        {
          "t": 0,
          "s": [70, 70],
          "e": [100, 100],
          "i": {"x": [0.25, 0.25], "y": [1, 1]},
          "o": {"x": [0.75, 0.75], "y": [0, 0]}
        },
        {"t": 45, "s": [100, 100]}
      ]
    },
    "p": {"a": 0, "k": [400, 200]},
    "a": {"a": 0, "k": [125, 40]}
  }
}
```

**Rotate + Scale Entrance (More Dynamic):**
```json
{
  "s": {
    "k": [
      {"t": 0, "s": [60, 60], "e": [100, 100]},
      {"t": 45, "s": [100, 100]}
    ]
  },
  "r": {
    "k": [
      {"t": 0, "s": [5], "e": [0], "i": {"x": [0.25], "y": [1]}, "o": {"x": [0.75], "y": [0]}},
      {"t": 45, "s": [0]}
    ]
  }
}
```

**Bounce Entrance (Playful):**
```json
{
  "s": {
    "k": [
      {"t": 0, "s": [60, 60], "e": [110, 110], "i": {"x": [0.175], "y": [0.885]}, "o": {"x": [0.32], "y": [1.275]}},
      {"t": 30, "s": [110, 110], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
      {"t": 45, "s": [100, 100]}
    ]
  }
}
```

### Easing Recommendations
- **Tech/Innovation**: Sharp ease-in (0.42/1.0)
- **Playful**: Bounce/overshoot (0.175/0.885, 0.32/1.275)
- **Professional**: Standard ease-out (0.42/0.58)

---

## Multi-Element Synchronization

### Pattern A: Simultaneous Entrance (Detailed)

**Use Case:** Canva-style unified brand (circle + text are one identity)

**Complete Implementation:**
```json
{
  "v": "5.7.4",
  "fr": 60,
  "ip": 0,
  "op": 180,
  "w": 800,
  "h": 400,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Circle Icon",
      "refId": "circle_element",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0], "e": [100], "i": {"x": [0.25], "y": [1]}, "o": {"x": [0.75], "y": [0]}},
            {"t": 60, "s": [100]}
          ]
        },
        "s": {
          "a": 1,
          "k": [
            {"t": 0, "s": [70, 70], "e": [100, 100], "i": {"x": [0.25, 0.25], "y": [1, 1]}, "o": {"x": [0.75, 0.75], "y": [0, 0]}},
            {"t": 60, "s": [100, 100], "e": [112, 112]},
            {"t": 120, "s": [112, 112], "e": [100, 100]},
            {"t": 180, "s": [100, 100]}
          ]
        },
        "p": {"a": 0, "k": [300, 200]},
        "a": {"a": 0, "k": [100, 100]}
      },
      "ip": 0,
      "op": 180
    },
    {
      "ind": 2,
      "ty": 2,
      "nm": "Text",
      "refId": "text_element",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0], "e": [100], "i": {"x": [0.25], "y": [1]}, "o": {"x": [0.75], "y": [0]}},
            {"t": 60, "s": [100]}
          ]
        },
        "s": {
          "a": 1,
          "k": [
            {"t": 0, "s": [70, 70], "e": [100, 100], "i": {"x": [0.25, 0.25], "y": [1, 1]}, "o": {"x": [0.75, 0.75], "y": [0, 0]}},
            {"t": 60, "s": [100, 100]}
          ]
        },
        "p": {"a": 0, "k": [500, 200]},
        "a": {"a": 0, "k": [125, 40]}
      },
      "ip": 0,
      "op": 180
    }
  ],
  "assets": [
    {"id": "circle_element", "w": 200, "h": 200, "p": "circle_optimized.png", "e": 0},
    {"id": "text_element", "w": 250, "h": 80, "p": "text_optimized.png", "e": 0}
  ]
}
```

**Key Synchronization Points:**
- Both layers: `"t": 0` (start together)
- Both layers: Same easing curves (0.25/0.75)
- Both layers: Same entrance duration (60 frames)
- Icon continues with pulse (frames 60-180)
- Text stays static during loop (optional)

### Pattern B: Staggered Entrance (Detailed)

**Use Case:** Two-part narrative (icon explains product, text reveals name)

**Timing Calculation:**
```
Icon entrance: Frames 0-45 (0.75s at 60fps)
Overlap period: Frames 30-45 (both visible, text fading in)
Text entrance: Frames 30-75 (0.75s at 60fps)
Total duration: 75 frames (1.25s at 60fps)
```

**Complete Implementation:**
```json
{
  "layers": [
    {
      "ind": 1,
      "nm": "Icon",
      "ks": {
        "o": {
          "k": [
            {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 45, "s": [100]}
          ]
        },
        "s": {
          "k": [
            {"t": 0, "s": [80, 80], "e": [100, 100]},
            {"t": 45, "s": [100, 100]}
          ]
        }
      },
      "ip": 0,
      "op": 180
    },
    {
      "ind": 2,
      "nm": "Text",
      "ks": {
        "o": {
          "k": [
            {"t": 30, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 75, "s": [100]}
          ]
        },
        "s": {
          "k": [
            {"t": 30, "s": [80, 80], "e": [100, 100]},
            {"t": 75, "s": [100, 100]}
          ]
        }
      },
      "ip": 0,
      "op": 180
    }
  ]
}
```

**Stagger Timing Guide:**
- 15 frames (0.25s at 60fps): Subtle stagger
- 30 frames (0.5s at 60fps): Noticeable sequence ← Recommended
- 45 frames (0.75s at 60fps): Dramatic two-act reveal

---

## Troubleshooting Guide

### Problem: Text is Blurry/Pixelated

**Symptoms:**
- Text edges look fuzzy
- Letters have jagged edges
- Quality worse than original logo

**Causes:**
1. Rendered at too low resolution
2. PNG compression too aggressive
3. Scaled up from small source

**Solutions:**
```bash
# Solution 1: Render at 2x size
python scripts/prepare_logo.py elements/text.svg --max-size 500  # Double the target

# Solution 2: Disable aggressive optimization
python scripts/prepare_logo.py elements/text.svg --max-size 250 --quality 95

# Solution 3: Check source SVG quality
# Ensure SVG has sufficient detail, not upscaled raster
```

### Problem: Text Doesn't Sync with Icon

**Symptoms:**
- Text appears before/after icon when both should be simultaneous
- Timing offset doesn't match expectations

**Causes:**
1. Different `"t"` values in keyframes
2. Different animation durations
3. Different `ip`/`op` values

**Solutions:**
```json
// Verify BOTH layers start at same frame
// Layer 1 (Icon)
"o": {"k": [{"t": 0, "s": [0]}, {"t": 60, "s": [100]}]}

// Layer 2 (Text) - Must also start at t:0 for simultaneous
"o": {"k": [{"t": 0, "s": [0]}, {"t": 60, "s": [100]}]}

// For staggered, offset the text start:
"o": {"k": [{"t": 30, "s": [0]}, {"t": 75, "s": [100]}]}
```

### Problem: Wrong/Random Text Appears

**Symptoms:**
- Text in animation doesn't match logo
- Different font, color, or content

**Cause:**
Using PIL ImageDraw to create text instead of extracting from logo

**Wrong Code:**
```python
# NEVER DO THIS
from PIL import Image, ImageDraw
draw = ImageDraw.Draw(img)
draw.text((100, 50), "Brand Name", fill='black')
```

**Solution:**
```bash
# Extract actual text from logo SVG
python scripts/extract_svg_elements.py logo.svg --output-dir ./elements/
python scripts/prepare_logo.py elements/text_0.svg --max-size 250
```

### Problem: Text Overlaps Icon Incorrectly

**Symptoms:**
- Text positioned wrong relative to icon
- Elements don't align as in original logo

**Causes:**
1. Wrong anchor points (`"a"` property)
2. Wrong positions (`"p"` property)
3. ViewBox mismatch between SVG and Lottie

**Solutions:**
```json
// Verify anchor points match element centers
"a": {"a": 0, "k": [125, 40]}  // Half of text element width/height

// Verify positions use absolute coordinates
"p": {"a": 0, "k": [500, 200]}  // Actual pixel position in canvas

// Ensure Lottie canvas matches SVG viewBox
// SVG viewBox="0 0 800 400"
// Lottie "w": 800, "h": 400
```

---

## Philosophy Alignment Reference

### Complete Brand Type → Method Matrix

| Brand Type | Text Method | Icon Method | Timing | Easing | Sync Pattern | Why |
|-----------|-------------|-------------|--------|--------|--------------|-----|
| **Canva/Figma** | Fade+Scale | Fade+Scale+Pulse | 1s entrance, 2s pulse | 0.25/0.75 | Simultaneous | Creative energy, unified tool |
| **IBM/Deloitte** | Fade only | Fade+subtle scale | 2s slow | 0.42/0.58 | Simultaneous | Conservative, professional |
| **Tiffany/Rolex** | Stroke reveal | Fade slow | 3-4s | Ease-in-out | Simultaneous | Premium "drawing" feel |
| **Stripe/Vercel** | Scale entrance | Scale+rotate | 1-1.5s sharp | Ease-in | Staggered | Modern, tech-forward |
| **Pixar/Disney** | Bounce | Bounce+squash | 1.5s | Overshoot | Simultaneous | Playful, character |
| **NYT/Medium** | Fade subtle | Fade very subtle | 2-3s | 0.42/0.58 | Simultaneous | Editorial, refined |

---

## Element Extraction Workflow (Complete)

### Step-by-Step: Multi-Element Logo Animation

**Starting Point:** logo.svg with icon + text

**Step 1: List Elements**
```bash
python scripts/extract_svg_elements.py logo.svg --list-only
```

**Expected Output:**
```
📋 Elements found (3 total):
   - path: circle_background
   - path: text_path
   - group: combined
```

**Step 2: Extract Elements**
```bash
python scripts/extract_svg_elements.py logo.svg --output-dir ./elements/
```

**Output:**
```
✅ path: circle_background.svg (2.3 KB)
✅ path: text_path.svg (4.1 KB)
✅ group: combined.svg (6.5 KB)
```

**Step 3: Convert to Optimized PNGs**
```bash
# Icon element - small size
python scripts/prepare_logo.py elements/circle_background.svg --max-size 200

# Text element - medium size
python scripts/prepare_logo.py elements/text_path.svg --max-size 250
```

**Output:**
```
✅ circle_background_optimized.png (8.2 KB)
✅ text_path_optimized.png (12.4 KB)
```

**Step 4: Create Lottie JSON**
Use multi-element compositing example from above (Pattern A or Pattern B)

**Step 5: Verify**
```bash
python scripts/verify_animation.py animation.json --expect-layers 2
```

**Step 6: Render**
```bash
python scripts/render_lottie.py animation.json output.gif
```

**Total Time:** 10-15 minutes for clean multi-element animation

---

## Quick Reference Cheat Sheet

### Method Selection
```
Simple logo → Fade-in (Method 1)
Premium brand → Stroke reveal (Method 2)
Energetic brand → Transform entrance (Method 3)
```

### Synchronization Pattern
```
Unified brand → Simultaneous (both t:0)
Two-part story → Staggered (text t:30)
Icon dominates → Staggered (text t:45)
```

### File Sizes
```
Full logo (single): 500-600px
Icon element: 150-200px
Text element: 200-300px
Small badge: 100-150px
```

### Timing Guidelines
```
Simultaneous entrance: Both start t:0, same duration
Subtle stagger: 15 frame offset (0.25s at 60fps)
Standard stagger: 30 frame offset (0.5s at 60fps)
Dramatic stagger: 45 frame offset (0.75s at 60fps)
```
