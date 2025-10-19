# Lottie JSON Specification Reference

Comprehensive reference for creating Lottie animations programmatically.

## Core Structure

Every Lottie JSON file has this root structure:

```json
{
  "v": "5.7.4",        // Lottie version (bodymovin version)
  "fr": 30,            // Frame rate (frames per second)
  "ip": 0,             // In point (start frame)
  "op": 150,           // Out point (end frame)
  "w": 512,            // Width in pixels
  "h": 512,            // Height in pixels
  "nm": "Animation",   // Name (optional)
  "ddd": 0,            // 3D layers (0 = 2D, 1 = 3D)
  "assets": [],        // External assets (images, fonts)
  "layers": []         // Animation layers (main content)
}
```

## Layers

Layers are the building blocks of Lottie animations. Each layer can contain shapes, images, or other layers.

### Layer Types

**Shape Layer** (`ty: 4`):
```json
{
  "ddd": 0,
  "ind": 1,             // Layer index
  "ty": 4,              // Type: 4 = Shape layer
  "nm": "Shape Layer",  // Name
  "sr": 1,              // Time stretch
  "ks": {},             // Transform properties
  "ao": 0,              // Auto-orient
  "shapes": [],         // Shape elements
  "ip": 0,              // In point
  "op": 150,            // Out point
  "st": 0,              // Start time
  "bm": 0               // Blend mode
}
```

**Image Layer** (`ty: 2`):
```json
{
  "ty": 2,              // Type: 2 = Image layer
  "refId": "image_0",   // Reference to asset
  "ks": {},             // Transform
  "ip": 0,
  "op": 150
}
```

**Null/Empty Layer** (`ty: 3`):
Useful as parent for grouping and controlling other layers.

## Transform Properties (ks)

The `ks` object defines position, scale, rotation, opacity, and anchor point:

```json
"ks": {
  "o": {              // Opacity
    "a": 0,           // Animated (0 = static, 1 = animated)
    "k": 100          // Value (0-100)
  },
  "r": {              // Rotation
    "a": 0,
    "k": 0            // Degrees (0-360)
  },
  "p": {              // Position
    "a": 0,
    "k": [256, 256]   // [x, y] in pixels
  },
  "a": {              // Anchor point
    "a": 0,
    "k": [0, 0]       // [x, y] relative to layer
  },
  "s": {              // Scale
    "a": 0,
    "k": [100, 100]   // [x%, y%]
  }
}
```

### Animated Transform (Keyframes)

For animated properties, set `"a": 1` and provide keyframes in `k`:

```json
"p": {
  "a": 1,             // Animated
  "k": [              // Keyframes array
    {
      "i": {"x": [0.833], "y": [0.833]},  // In tangent (easing)
      "o": {"x": [0.167], "y": [0.167]},  // Out tangent (easing)
      "t": 0,                              // Time (frame number)
      "s": [100, 256],                     // Start value
      "e": [400, 256],                     // End value
      "to": [50, 0],                       // Tangent out
      "ti": [-50, 0]                       // Tangent in
    },
    {
      "t": 60,                   // Final keyframe
      "s": [400, 256]            // Final value
    }
  ]
}
```

## Easing Functions (Bezier Curves)

Easing is defined by bezier control points in `i` (in tangent) and `o` (out tangent):

- **Linear**: `"i": {"x": [0], "y": [0]}, "o": {"x": [0], "y": [0]}`
- **Ease In**: `"i": {"x": [0.42], "y": [0]}, "o": {"x": [1], "y": [1]}`
- **Ease Out**: `"i": {"x": [0], "y": [0]}, "o": {"x": [0.58], "y": [1]}`
- **Ease In-Out**: `"i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}`

Common easing presets:

| Name | In X | In Y | Out X | Out Y |
|------|------|------|-------|-------|
| Linear | 0 | 0 | 0 | 0 |
| Ease In | 0.42 | 0 | 1 | 1 |
| Ease Out | 0 | 0 | 0.58 | 1 |
| Ease In-Out | 0.42 | 0 | 0.58 | 1 |
| Ease In Back | 0.6 | -0.28 | 0.735 | 0.045 |
| Ease Out Back | 0.175 | 0.885 | 0.32 | 1.275 |

## Shapes

Shape layers contain shape elements in the `shapes` array:

### Rectangle

```json
{
  "ty": "rc",         // Type: rectangle
  "d": 1,             // Direction
  "s": {              // Size
    "a": 0,
    "k": [200, 200]   // [width, height]
  },
  "p": {              // Position
    "a": 0,
    "k": [0, 0]
  },
  "r": {              // Rounded corners
    "a": 0,
    "k": 0
  }
}
```

### Ellipse

```json
{
  "ty": "el",         // Type: ellipse
  "d": 1,
  "s": {              // Size
    "a": 0,
    "k": [100, 100]   // [width, height]
  },
  "p": {              // Position
    "a": 0,
    "k": [0, 0]
  }
}
```

### Path (Custom Shape)

```json
{
  "ty": "sh",         // Type: shape/path
  "ks": {
    "a": 0,
    "k": {
      "i": [[0, 0], [0, 0], [0, 0]],      // In tangents
      "o": [[0, 0], [0, 0], [0, 0]],      // Out tangents
      "v": [[0, 0], [100, 0], [50, 100]], // Vertices
      "c": true                            // Closed path
    }
  }
}
```

### Fill

```json
{
  "ty": "fl",         // Type: fill
  "c": {              // Color
    "a": 0,
    "k": [1, 0, 0, 1] // [r, g, b, a] (0-1 range)
  },
  "o": {              // Opacity
    "a": 0,
    "k": 100          // 0-100
  }
}
```

### Stroke

```json
{
  "ty": "st",         // Type: stroke
  "c": {              // Color
    "a": 0,
    "k": [0, 0, 0, 1]
  },
  "o": {              // Opacity
    "a": 0,
    "k": 100
  },
  "w": {              // Width
    "a": 0,
    "k": 2
  },
  "lc": 1,            // Line cap (1=butt, 2=round, 3=square)
  "lj": 1             // Line join (1=miter, 2=round, 3=bevel)
}
```

### Gradient Fill

```json
{
  "ty": "gf",         // Type: gradient fill
  "o": {"a": 0, "k": 100},
  "g": {
    "p": 3,           // Number of color stops
    "k": {
      "a": 0,
      "k": [
        0, 1, 0, 0,   // Position 0: RGB(1,0,0) red
        0.5, 0, 1, 0, // Position 0.5: RGB(0,1,0) green
        1, 0, 0, 1    // Position 1: RGB(0,0,1) blue
      ]
    }
  },
  "s": {"a": 0, "k": [0, 0]},      // Start point
  "e": {"a": 0, "k": [100, 100]},  // End point
  "t": 1                            // Type (1=linear, 2=radial)
}
```

### Transform (Shape Group)

```json
{
  "ty": "tr",         // Type: transform
  "p": {"a": 0, "k": [256, 256]},  // Position
  "a": {"a": 0, "k": [0, 0]},      // Anchor
  "s": {"a": 0, "k": [100, 100]},  // Scale
  "r": {"a": 0, "k": 0},           // Rotation
  "o": {"a": 0, "k": 100},         // Opacity
  "sk": {"a": 0, "k": 0},          // Skew
  "sa": {"a": 0, "k": 0}           // Skew axis
}
```

## Assets

External resources referenced by layers:

### Image Asset

```json
{
  "id": "image_0",
  "w": 512,           // Width
  "h": 512,           // Height
  "u": "images/",     // Path (folder)
  "p": "logo.png",    // Filename
  "e": 0              // Embedded (0=external, 1=embedded base64)
}
```

### Embedded Base64 Image

```json
{
  "id": "image_0",
  "w": 512,
  "h": 512,
  "p": "data:image/png;base64,iVBORw0KGgo...",  // Base64 data
  "e": 1
}
```

## Effects

### Drop Shadow

```json
{
  "ty": 25,           // Type: drop shadow
  "nm": "Drop Shadow",
  "ef": [
    {"ty": 2, "v": {"a": 0, "k": 0}},       // Shadow color
    {"ty": 0, "v": {"a": 0, "k": 50}},      // Opacity
    {"ty": 0, "v": {"a": 0, "k": 135}},     // Direction
    {"ty": 0, "v": {"a": 0, "k": 10}},      // Distance
    {"ty": 0, "v": {"a": 0, "k": 15}}       // Softness
  ]
}
```

## Complete Example: Bouncing Circle

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 60,
  "w": 512,
  "h": 512,
  "layers": [
    {
      "ddd": 0,
      "ind": 1,
      "ty": 4,
      "nm": "Circle",
      "ks": {
        "p": {
          "a": 1,
          "k": [
            {"t": 0, "s": [256, 100], "e": [256, 400], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
            {"t": 30, "s": [256, 400], "e": [256, 100], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
            {"t": 60, "s": [256, 100]}
          ]
        },
        "a": {"a": 0, "k": [0, 0]},
        "s": {"a": 0, "k": [100, 100]},
        "r": {"a": 0, "k": 0},
        "o": {"a": 0, "k": 100}
      },
      "shapes": [
        {
          "ty": "gr",
          "it": [
            {
              "ty": "el",
              "s": {"a": 0, "k": [80, 80]},
              "p": {"a": 0, "k": [0, 0]}
            },
            {
              "ty": "fl",
              "c": {"a": 0, "k": [0.2, 0.6, 1, 1]},
              "o": {"a": 0, "k": 100}
            },
            {
              "ty": "tr",
              "p": {"a": 0, "k": [0, 0]},
              "a": {"a": 0, "k": [0, 0]},
              "s": {"a": 0, "k": [100, 100]},
              "r": {"a": 0, "k": 0},
              "o": {"a": 0, "k": 100}
            }
          ]
        }
      ],
      "ip": 0,
      "op": 60,
      "st": 0
    }
  ]
}
```

## Shape Layers (Programmatic Graphics)

Shape layers allow creating vector graphics directly in Lottie JSON without external image files. This is useful for simple geometric logos, text-based designs, or programmatically-generated graphics.

### Layer Types Comparison

**Image Layer (ty: 2)** - Current focus
- References external or embedded PNG/SVG/JPG
- Transforms with position/scale/rotation/opacity
- Best for: Existing logo files, photographic elements

**Shape Layer (ty: 4)** - Programmatic vector graphics
- Creates shapes directly in Lottie JSON
- Primitives: Ellipse, Rectangle, PolyStar, Path (custom bezier curves)
- Styles: Fill, Stroke, Gradient Fill, Gradient Stroke
- Modifiers: Trim Path, Rounded Corners, Offset Path, Merge Paths, Twist
- Best for: Geometric logos, simple icons, text-based designs, avoiding image dependencies

### Shape Layer Structure

```json
{
  "ty": 4,              // Shape layer type
  "nm": "Shape Layer",
  "ip": 0,
  "op": 60,
  "ks": { /* transforms */ },
  "shapes": [           // Array of shape elements
    {
      "ty": "gr",       // Group
      "nm": "Group 1",
      "it": [           // Items in group
        {
          "ty": "el",   // Ellipse shape
          "p": {"a": 0, "k": [256, 256]},  // Position
          "s": {"a": 0, "k": [200, 200]}   // Size
        },
        {
          "ty": "fl",   // Fill style
          "o": {"a": 0, "k": 100},         // Opacity
          "c": {"a": 0, "k": [1, 0, 0]}    // Color (RGB 0-1)
        },
        {
          "ty": "tr",   // Transform for group
          "p": {"a": 0, "k": [0, 0]},
          "a": {"a": 0, "k": [0, 0]},
          "s": {"a": 0, "k": [100, 100]},
          "r": {"a": 0, "k": 0},
          "o": {"a": 0, "k": 100}
        }
      ]
    }
  ]
}
```

### Shape Primitives

#### Ellipse (`ty: "el"`)

Creates circles and ellipses.

```json
{
  "ty": "el",
  "nm": "Ellipse",
  "p": {"a": 0, "k": [256, 256]},  // Position (center point)
  "s": {"a": 0, "k": [200, 200]},  // Size [width, height]
  "d": 1                            // Drawing direction (1=clockwise, 3=counterclockwise)
}
```

**Animated ellipse**:
```json
{
  "ty": "el",
  "p": {"a": 0, "k": [256, 256]},
  "s": {
    "a": 1,  // Animated
    "k": [
      {"t": 0, "s": [100, 100], "e": [200, 200]},
      {"t": 30, "s": [200, 200]}
    ]
  }
}
```

#### Rectangle (`ty: "rc"`)

Creates rectangles and rounded rectangles.

```json
{
  "ty": "rc",
  "nm": "Rectangle",
  "p": {"a": 0, "k": [256, 256]},  // Position (center point)
  "s": {"a": 0, "k": [300, 200]},  // Size [width, height]
  "r": {"a": 0, "k": 20}           // Corner roundness (0=sharp, higher=rounder)
}
```

#### PolyStar (`ty: "sr"`)

Creates stars and polygons.

```json
{
  "ty": "sr",
  "nm": "Star",
  "p": {"a": 0, "k": [256, 256]},   // Position (center)
  "sy": 1,                          // Star type: 1=star, 2=polygon
  "pt": {"a": 0, "k": 5},           // Number of points
  "or": {"a": 0, "k": 100},         // Outer radius
  "ir": {"a": 0, "k": 50},          // Inner radius (stars only)
  "r": {"a": 0, "k": 0}             // Rotation
}
```

**Polygon** (set `sy: 2`, omit `ir`):
```json
{
  "ty": "sr",
  "sy": 2,                          // Polygon (not star)
  "pt": {"a": 0, "k": 6},           // Hexagon (6 sides)
  "or": {"a": 0, "k": 100}
}
```

#### Path (`ty: "sh"`)

Custom bezier curve paths.

```json
{
  "ty": "sh",
  "nm": "Path",
  "ks": {
    "a": 0,  // Static path
    "k": {
      "c": true,  // Closed path
      "v": [      // Vertices [x, y]
        [100, 100],
        [200, 100],
        [200, 200],
        [100, 200]
      ],
      "i": [[0,0], [0,0], [0,0], [0,0]],  // In tangents
      "o": [[0,0], [0,0], [0,0], [0,0]]   // Out tangents
    }
  }
}
```

### Style Elements

Styles apply to all preceding shapes in the same group.

#### Fill (`ty: "fl"`)

Solid color fill.

```json
{
  "ty": "fl",
  "nm": "Fill",
  "o": {"a": 0, "k": 100},           // Opacity (0-100)
  "c": {"a": 0, "k": [1, 0, 0, 1]}   // Color RGBA (0-1)
}
```

**Animated fill color**:
```json
{
  "ty": "fl",
  "o": {"a": 0, "k": 100},
  "c": {
    "a": 1,
    "k": [
      {"t": 0, "s": [1, 0, 0, 1], "e": [0, 0, 1, 1]},  // Red → Blue
      {"t": 30, "s": [0, 0, 1, 1]}
    ]
  }
}
```

#### Stroke (`ty: "st"`)

Outline stroke.

```json
{
  "ty": "st",
  "nm": "Stroke",
  "o": {"a": 0, "k": 100},           // Opacity
  "c": {"a": 0, "k": [0, 0, 0, 1]},  // Color
  "w": {"a": 0, "k": 5},             // Width in pixels
  "lc": 2,                           // Line cap: 1=butt, 2=round, 3=square
  "lj": 2                            // Line join: 1=miter, 2=round, 3=bevel
}
```

### Modifiers

Modifiers change the appearance of shapes without creating new ones.

#### Trim Path (`ty: "tm"`)

Animate drawing/revealing paths (the "draw-on" effect).

```json
{
  "ty": "tm",
  "nm": "Trim Paths",
  "s": {                    // Start (0-100%)
    "a": 1,
    "k": [
      {"t": 0, "s": [0], "e": [100]},
      {"t": 30, "s": [100]}
    ]
  },
  "e": {"a": 0, "k": [100]},  // End (0-100%)
  "o": {"a": 0, "k": [0]},    // Offset (rotation offset)
  "m": 1                      // Multiple shapes: 1=simultaneously, 2=individually
}
```

**Draw-on animation**:
- Start: 0% → 100% (reveals path from start to end)
- End: stays at 100%
- Creates signature "drawing" effect

**Draw-off animation**:
- Start: stays at 0%
- End: 100% → 0% (hides path from end to start)

#### Rounded Corners (`ty: "rd"`)

Add rounded corners to paths.

```json
{
  "ty": "rd",
  "nm": "Round Corners",
  "r": {"a": 0, "k": 10}  // Radius in pixels
}
```

### Complete Shape Layer Example: Pulsing Circle

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 60,
  "w": 512,
  "h": 512,
  "layers": [
    {
      "ty": 4,
      "nm": "Circle Layer",
      "ip": 0,
      "op": 60,
      "ks": {
        "p": {"a": 0, "k": [256, 256, 0]},
        "a": {"a": 0, "k": [0, 0, 0]},
        "s": {"a": 0, "k": [100, 100, 100]},
        "r": {"a": 0, "k": 0},
        "o": {"a": 0, "k": 100}
      },
      "shapes": [
        {
          "ty": "gr",
          "nm": "Circle Group",
          "it": [
            {
              "ty": "el",
              "nm": "Circle",
              "p": {"a": 0, "k": [0, 0]},
              "s": {
                "a": 1,
                "k": [
                  {"t": 0, "s": [100, 100], "e": [150, 150],
                   "i": {"x": [0.42, 0.42], "y": [1, 1]},
                   "o": {"x": [0.58, 0.58], "y": [0, 0]}},
                  {"t": 30, "s": [150, 150], "e": [100, 100],
                   "i": {"x": [0.42, 0.42], "y": [1, 1]},
                   "o": {"x": [0.58, 0.58], "y": [0, 0]}},
                  {"t": 60, "s": [100, 100]}
                ]
              }
            },
            {
              "ty": "fl",
              "nm": "Fill",
              "o": {"a": 0, "k": 100},
              "c": {"a": 0, "k": [0.2, 0.5, 1, 1]}
            },
            {
              "ty": "tr",
              "nm": "Transform",
              "p": {"a": 0, "k": [0, 0]},
              "a": {"a": 0, "k": [0, 0]},
              "s": {"a": 0, "k": [100, 100]},
              "r": {"a": 0, "k": 0},
              "o": {"a": 0, "k": 100}
            }
          ]
        }
      ]
    }
  ]
}
```

### When to Use Shape Layers vs Image Layers

**Use Shape Layers when**:
- Creating simple geometric logos programmatically
- Want to avoid external image dependencies
- Need draw-on effects (Trim Path)
- Logo is text-based or very simple geometry
- File size is critical (shapes can be smaller than embedded images)

**Use Image Layers when**:
- Have existing logo file (PNG/SVG/JPG)
- Logo is complex (photos, gradients, many colors)
- Logo was designed in graphic design software
- Need to maintain exact visual fidelity

**Combine both**:
- Background shape layer + foreground image layer
- Text as shapes + icon as image
- Geometric frame (shapes) + logo (image)

## Tips for Creating Lottie Animations

1. **Keep it simple**: Fewer layers and shapes = smaller file size and better performance
2. **Optimize paths**: Use fewer vertices in custom shapes
3. **Reuse assets**: Reference the same image/shape multiple times instead of duplicating
4. **Round values**: 2-3 decimal places is usually sufficient
5. **Test compatibility**: Use lottie-web player to preview before deploying
6. **Perfect loops**: Ensure first and last keyframe values match exactly
7. **Frame rate**: 30-60 fps for smooth animation, 24 fps for more "cinematic" feel
8. **Duration**: 2-5 seconds is ideal for logo animations
