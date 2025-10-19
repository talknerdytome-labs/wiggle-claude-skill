# Detailed Animation Examples

Complete Lottie JSON code examples for all animation patterns. These are referenced from the main SKILL.md but kept separate to reduce context load.

## Table of Contents

- [Single-Element Patterns](#single-element-patterns)
- [Multi-Element Coordination](#multi-element-coordination)
- [Text Animation Patterns](#text-animation-patterns)
- [Shape Layer Examples](#shape-layer-examples)
- [Advanced Compositions](#advanced-compositions)

## Single-Element Patterns

### 1. Wiggle/Jello

Quick oscillating motion. Perfect for notifications or playful brands.

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 24,
  "w": 400,
  "h": 200,
  "layers": [{
    "ind": 1,
    "ty": 2,
    "nm": "Logo",
    "refId": "logo_image",
    "ks": {
      "r": {
        "a": 1,
        "k": [
          {"t": 0, "s": [-5], "e": [5], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
          {"t": 12, "s": [5], "e": [-5], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
          {"t": 24, "s": [-5]}
        ]
      },
      "p": {"a": 0, "k": [200, 100]},
      "a": {"a": 0, "k": [128, 64]},
      "s": {"a": 0, "k": [100, 100]},
      "o": {"a": 0, "k": 100}
    },
    "ip": 0,
    "op": 24
  }],
  "assets": [{"id": "logo_image", "w": 256, "h": 128, "p": "logo.png", "e": 0}]
}
```

**Parameters:**
- Duration: 0.8s (24 frames at 30fps)
- Rotation: ±5° oscillation
- Easing: Standard ease-in-out (0.42/0.58)

**Usage:** Notification badges, playful CTAs, attention-grabbing elements

---

### 2. Bounce Entrance

Dynamic entrance with physics-based landing.

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 36,
  "w": 800,
  "h": 400,
  "layers": [{
    "ind": 1,
    "ty": 2,
    "nm": "Logo",
    "refId": "logo_image",
    "ks": {
      "p": {
        "a": 1,
        "k": [
          {"t": 0, "s": [400, 100], "e": [400, 200], "i": {"x": [0.175], "y": [0.885]}, "o": {"x": [0.32], "y": [1.275]}},
          {"t": 36, "s": [400, 200]}
        ]
      },
      "o": {
        "a": 1,
        "k": [
          {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [1], "y": [0]}},
          {"t": 20, "s": [100]}
        ]
      },
      "s": {
        "a": 1,
        "k": [
          {"t": 0, "s": [80, 80], "e": [105, 105], "i": {"x": [0.175], "y": [0.885]}, "o": {"x": [0.32], "y": [1.275]}},
          {"t": 24, "s": [105, 105], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 36, "s": [100, 100]}
        ]
      },
      "a": {"a": 0, "k": [256, 128]},
      "r": {"a": 0, "k": 0}
    },
    "ip": 0,
    "op": 36
  }],
  "assets": [{"id": "logo_image", "w": 512, "h": 256, "p": "logo.png", "e": 0}]
}
```

**Parameters:**
- Duration: 1.2s (36 frames at 30fps)
- Combined: Position (drop), Opacity (fade in), Scale (bounce)
- Easing: Custom bounce curve for physics feel

**Usage:** Startup splash screens, energetic brand moments, mobile app launches

---

### 3. Smooth 360° Rotation

Continuous rotation for loading or tech brands.

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 300,
  "w": 400,
  "h": 400,
  "layers": [{
    "ind": 1,
    "ty": 2,
    "nm": "Logo",
    "refId": "logo_image",
    "ks": {
      "r": {
        "a": 1,
        "k": [
          {"t": 0, "s": [0], "e": [360], "i": {"x": [1], "y": [1]}, "o": {"x": [0], "y": [0]}},
          {"t": 300, "s": [360]}
        ]
      },
      "p": {"a": 0, "k": [200, 200]},
      "a": {"a": 0, "k": [128, 128]},
      "s": {"a": 0, "k": [100, 100]},
      "o": {"a": 0, "k": 100}
    },
    "ip": 0,
    "op": 300
  }],
  "assets": [{"id": "logo_image", "w": 256, "h": 256, "p": "logo.png", "e": 0}]
}
```

**Parameters:**
- Duration: 10s (300 frames at 30fps)
- Rotation: Full 360° rotation
- Easing: Linear (1/1 and 0/0) for constant speed

**Usage:** Loading indicators, tech logos, processing states

---

### 4. Scale Pulse (Breathing Effect)

Gentle scale animation for CTAs or idle states.

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 90,
  "w": 400,
  "h": 200,
  "layers": [{
    "ind": 1,
    "ty": 2,
    "nm": "Logo",
    "refId": "logo_image",
    "ks": {
      "s": {
        "a": 1,
        "k": [
          {"t": 0, "s": [100, 100], "e": [103, 103], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
          {"t": 45, "s": [103, 103], "e": [100, 100], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
          {"t": 90, "s": [100, 100]}
        ]
      },
      "p": {"a": 0, "k": [200, 100]},
      "a": {"a": 0, "k": [128, 64]},
      "r": {"a": 0, "k": 0},
      "o": {"a": 0, "k": 100}
    },
    "ip": 0,
    "op": 90
  }],
  "assets": [{"id": "logo_image", "w": 256, "h": 128, "p": "logo.png", "e": 0}]
}
```

**Parameters:**
- Duration: 3s loop (90 frames at 30fps)
- Scale: 100% → 103% → 100%
- Easing: Smooth ease-in-out

**Usage:** Idle logo states, subtle CTAs, email signature animations

---

### 5. Fade + Gentle Scale In

Professional entrance for corporate brands.

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 45,
  "w": 800,
  "h": 400,
  "layers": [{
    "ind": 1,
    "ty": 2,
    "nm": "Logo",
    "refId": "logo_image",
    "ks": {
      "o": {
        "a": 1,
        "k": [
          {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 45, "s": [100]}
        ]
      },
      "s": {
        "a": 1,
        "k": [
          {"t": 0, "s": [95, 95], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 45, "s": [100, 100]}
        ]
      },
      "p": {"a": 0, "k": [400, 200]},
      "a": {"a": 0, "k": [256, 128]},
      "r": {"a": 0, "k": 0}
    },
    "ip": 0,
    "op": 45
  }],
  "assets": [{"id": "logo_image", "w": 512, "h": 256, "p": "logo.png", "e": 0}]
}
```

**Parameters:**
- Duration: 1.5s (45 frames at 30fps)
- Opacity: 0% → 100%
- Scale: 95% → 100% (subtle growth)

**Usage:** Corporate intros, B2B brands, professional presentations

---

### 6. Slide In from Left

Directional entrance with optional overshoot.

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 30,
  "w": 800,
  "h": 400,
  "layers": [{
    "ind": 1,
    "ty": 2,
    "nm": "Logo",
    "refId": "logo_image",
    "ks": {
      "p": {
        "a": 1,
        "k": [
          {"t": 0, "s": [100, 200], "e": [400, 200], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 30, "s": [400, 200]}
        ]
      },
      "o": {
        "a": 1,
        "k": [
          {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 20, "s": [100]}
        ]
      },
      "a": {"a": 0, "k": [256, 128]},
      "s": {"a": 0, "k": [100, 100]},
      "r": {"a": 0, "k": 0}
    },
    "ip": 0,
    "op": 30
  }],
  "assets": [{"id": "logo_image", "w": 512, "h": 256, "p": "logo.png", "e": 0}]
}
```

**Parameters:**
- Duration: 1s (30 frames at 30fps)
- Position: Off-screen left → Center
- Opacity: Fade in during slide

**Usage:** Website hero sections, presentation slides, directional reveals

---

### 7. Vertical Bar Waveform (Organic Motion)

Audio visualizer effect - demonstrates dense keyframes for smooth organic motion.

**Motion Type**: Organic/Continuous (30 keyframes, 0.25/0.75 easing, 60fps)

```json
{
  "v": "5.7.4",
  "fr": 60,
  "ip": 0,
  "op": 180,
  "w": 800,
  "h": 800,
  "layers": [{
    "ind": 1,
    "ty": 2,
    "nm": "Logo",
    "refId": "logo_image",
    "ks": {
      "s": {
        "a": 1,
        "k": [
          {"t": 0, "s": [100, 100, 100], "e": [100, 105, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 6, "s": [100, 105, 100], "e": [100, 110, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 12, "s": [100, 110, 100], "e": [100, 108, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 18, "s": [100, 108, 100], "e": [100, 103, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 24, "s": [100, 103, 100], "e": [100, 97, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 30, "s": [100, 97, 100], "e": [100, 92, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 36, "s": [100, 92, 100], "e": [100, 90, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 42, "s": [100, 90, 100], "e": [100, 93, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 48, "s": [100, 93, 100], "e": [100, 98, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 54, "s": [100, 98, 100], "e": [100, 105, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 60, "s": [100, 105, 100], "e": [100, 112, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 66, "s": [100, 112, 100], "e": [100, 115, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 72, "s": [100, 115, 100], "e": [100, 113, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 78, "s": [100, 113, 100], "e": [100, 108, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 84, "s": [100, 108, 100], "e": [100, 102, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 90, "s": [100, 102, 100], "e": [100, 95, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 96, "s": [100, 95, 100], "e": [100, 88, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 102, "s": [100, 88, 100], "e": [100, 85, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 108, "s": [100, 85, 100], "e": [100, 87, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 114, "s": [100, 87, 100], "e": [100, 92, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 120, "s": [100, 92, 100], "e": [100, 100, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 126, "s": [100, 100, 100], "e": [100, 107, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 132, "s": [100, 107, 100], "e": [100, 110, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 138, "s": [100, 110, 100], "e": [100, 108, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 144, "s": [100, 108, 100], "e": [100, 104, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 150, "s": [100, 104, 100], "e": [100, 98, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 156, "s": [100, 98, 100], "e": [100, 93, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 162, "s": [100, 93, 100], "e": [100, 95, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 168, "s": [100, 95, 100], "e": [100, 98, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 174, "s": [100, 98, 100], "e": [100, 100, 100],
           "i": {"x": [0.25, 0.25, 0.25], "y": [1, 1, 1]},
           "o": {"x": [0.75, 0.75, 0.75], "y": [0, 0, 0]}},
          {"t": 180, "s": [100, 100, 100]}
        ]
      },
      "p": {"a": 0, "k": [400, 400, 0]},
      "a": {"a": 0, "k": [256, 256, 0]},
      "r": {"a": 0, "k": 0},
      "o": {"a": 0, "k": 100}
    },
    "ip": 0,
    "op": 180
  }],
  "assets": [{"id": "logo_image", "w": 512, "h": 512, "p": "logo.png", "e": 0}]
}
```

**Parameters:**
- Duration: 3s (180 frames at 60fps)
- Keyframes: 30 (1 every 6 frames for smoothness)
- Easing: 0.25/0.75 (organic, softer than standard)
- Scale Y: Varies 85-115% for waveform effect

**Usage:** Audio apps, podcast logos, speech AI platforms, music streaming, sound design

**Why this works:**
- 30 keyframes create fluid, organic motion (not mechanical)
- 0.25/0.75 easing feels natural (softer than corporate 0.42/0.58)
- 60fps essential for continuous motion smoothness
- Varied timing creates natural rhythm

**Customization:**
- Vary scale_y values (85-115) for intensity
- Keep scale_x at 100 for pure vertical motion
- Add keyframes (up to 45) for MORE smoothness
- Remove keyframes (down to 15) for LESS smoothness
- **Critical:** Maintain 60fps and 0.25/0.75 easing

---

## Multi-Element Coordination

### Pattern: Simultaneous Icon + Text Entrance

Both elements appear together with synchronized timing.

```json
{
  "v": "5.7.4",
  "fr": 60,
  "ip": 0,
  "op": 60,
  "w": 1000,
  "h": 500,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Icon",
      "refId": "icon_image",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 60, "s": [100]}
          ]
        },
        "s": {
          "a": 1,
          "k": [
            {"t": 0, "s": [70, 70], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 60, "s": [100, 100]}
          ]
        },
        "p": {"a": 0, "k": [300, 250]},
        "a": {"a": 0, "k": [128, 128]},
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 180
    },
    {
      "ind": 2,
      "ty": 2,
      "nm": "Text",
      "refId": "text_image",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 60, "s": [100]}
          ]
        },
        "s": {
          "a": 1,
          "k": [
            {"t": 0, "s": [70, 70], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 60, "s": [100, 100]}
          ]
        },
        "p": {"a": 0, "k": [650, 250]},
        "a": {"a": 0, "k": [200, 64]},
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 180
    }
  ],
  "assets": [
    {"id": "icon_image", "w": 256, "h": 256, "p": "icon.png", "e": 0},
    {"id": "text_image", "w": 400, "h": 128, "p": "text.png", "e": 0}
  ]
}
```

**Key Points:**
- Both layers start at `t: 0`
- Identical keyframe timing (0→60)
- Same easing curves
- Creates unified, cohesive entrance

**Use for:** Unified brand identities, SaaS logos, simultaneous reveals

---

### Pattern: Staggered Icon → Text Entrance

Icon establishes first, then text reinforces.

```json
{
  "v": "5.7.4",
  "fr": 60,
  "ip": 0,
  "op": 90,
  "w": 1000,
  "h": 500,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Icon",
      "refId": "icon_image",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 45, "s": [100]}
          ]
        },
        "s": {
          "a": 1,
          "k": [
            {"t": 0, "s": [70, 70], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 45, "s": [100, 100]}
          ]
        },
        "p": {"a": 0, "k": [300, 250]},
        "a": {"a": 0, "k": [128, 128]},
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 180
    },
    {
      "ind": 2,
      "ty": 2,
      "nm": "Text",
      "refId": "text_image",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {"t": 30, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 75, "s": [100]}
          ]
        },
        "s": {
          "a": 1,
          "k": [
            {"t": 30, "s": [70, 70], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 75, "s": [100, 100]}
          ]
        },
        "p": {"a": 0, "k": [650, 250]},
        "a": {"a": 0, "k": [200, 64]},
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 180
    }
  ],
  "assets": [
    {"id": "icon_image", "w": 256, "h": 256, "p": "icon.png", "e": 0},
    {"id": "text_image", "w": 400, "h": 128, "p": "text.png", "e": 0}
  ]
}
```

**Key Points:**
- Icon: t:0 → t:45
- Text: t:30 → t:75 (30 frame delay = 0.5s at 60fps)
- Creates narrative sequence

**Timing Guidelines:**
- 15 frames (0.25s): Subtle stagger
- 30 frames (0.5s): Noticeable sequence
- 45 frames (0.75s): Dramatic two-act reveal

**Use for:** Product logos, tech brands, storytelling-focused identities

---

## Text Animation Patterns

### Simple Text Fade (Extracted from SVG)

Animate text extracted as separate element.

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 60,
  "w": 800,
  "h": 300,
  "layers": [{
    "ind": 1,
    "ty": 2,
    "nm": "Logo Text",
    "refId": "text_element",
    "ks": {
      "o": {
        "a": 1,
        "k": [
          {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 60, "s": [100]}
        ]
      },
      "s": {"a": 0, "k": [100, 100]},
      "p": {"a": 0, "k": [400, 150]},
      "a": {"a": 0, "k": [300, 75]},
      "r": {"a": 0, "k": 0}
    },
    "ip": 0,
    "op": 120
  }],
  "assets": [{"id": "text_element", "w": 600, "h": 150, "p": "text_extracted.png", "e": 0}]
}
```

**Workflow:**
1. Extract text: `python scripts/extract_svg_elements.py logo.svg --output-dir ./elements/`
2. Convert to PNG: `python scripts/prepare_logo.py elements/text_0.svg --max-size 200`
3. Animate as single layer with opacity

**Use for:** Professional text animations, wordmarks, corporate logos

---

### Two-Phase: Entrance + Loop

Logo enters, then subtle loop for idle state.

```json
{
  "v": "5.7.4",
  "fr": 60,
  "ip": 0,
  "op": 180,
  "w": 800,
  "h": 400,
  "layers": [{
    "ind": 1,
    "ty": 2,
    "nm": "Logo",
    "refId": "logo_image",
    "ks": {
      "s": {
        "a": 1,
        "k": [
          {"t": 0, "s": [70, 70], "e": [100, 100],
           "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 60, "s": [100, 100], "e": [105, 105],
           "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 120, "s": [105, 105], "e": [100, 100],
           "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 180, "s": [100, 100]}
        ]
      },
      "o": {
        "a": 1,
        "k": [
          {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 45, "s": [100]}
        ]
      },
      "p": {"a": 0, "k": [400, 200]},
      "a": {"a": 0, "k": [256, 128]},
      "r": {"a": 0, "k": 0}
    },
    "ip": 0,
    "op": 180
  }],
  "assets": [{"id": "logo_image", "w": 512, "h": 256, "p": "logo.png", "e": 0}]
}
```

**Structure:**
- Phase 1 (0-60): Entrance with fade + scale
- Phase 2 (60-180): Subtle pulse loop (100% → 105% → 100%)
- Total: 3s with seamless loop from frame 60

**Use for:** Loading screens, splash screens, website hero sections

---

## Shape Layer Examples

### Draw-On Effect (Trim Path)

Line reveal using Trim Path modifier.

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 60,
  "w": 800,
  "h": 400,
  "layers": [{
    "ind": 1,
    "ty": 4,
    "nm": "Circle Shape",
    "ks": {
      "p": {"a": 0, "k": [400, 200, 0]},
      "a": {"a": 0, "k": [0, 0, 0]},
      "s": {"a": 0, "k": [100, 100, 100]},
      "r": {"a": 0, "k": 0},
      "o": {"a": 0, "k": 100}
    },
    "shapes": [
      {
        "ty": "el",
        "nm": "Circle",
        "p": {"a": 0, "k": [0, 0]},
        "s": {"a": 0, "k": [200, 200]}
      },
      {
        "ty": "st",
        "nm": "Stroke",
        "c": {"a": 0, "k": [0.2, 0.4, 0.8, 1]},
        "w": {"a": 0, "k": 8},
        "lc": 2,
        "lj": 2
      },
      {
        "ty": "tm",
        "nm": "Trim Path",
        "s": {"a": 0, "k": 0},
        "e": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 60, "s": [100]}
          ]
        },
        "o": {"a": 0, "k": 0},
        "m": 1
      }
    ],
    "ip": 0,
    "op": 60
  }]
}
```

**Parameters:**
- Shape: Ellipse (circle)
- Stroke: 8px blue outline
- Trim Path end: 0% → 100% (draws on)

**Use for:** Line logos, signature animations, text outlines, minimalist brands

**Customization:**
- Change `ty: "el"` to `ty: "rc"` for rectangle
- Use `ty: "sr"` for star/polygon shapes
- Animate `s` (start) for reverse reveal
- Add `ty: "fl"` (fill) for solid shapes

---

### Geometric Pulsing Circle

Programmatic shape with scale animation.

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 90,
  "w": 800,
  "h": 800,
  "layers": [{
    "ind": 1,
    "ty": 4,
    "nm": "Pulsing Circle",
    "ks": {
      "p": {"a": 0, "k": [400, 400, 0]},
      "a": {"a": 0, "k": [0, 0, 0]},
      "s": {
        "a": 1,
        "k": [
          {"t": 0, "s": [100, 100, 100], "e": [110, 110, 100],
           "i": {"x": [0.42, 0.42, 0.42], "y": [1, 1, 1]},
           "o": {"x": [0.58, 0.58, 0.58], "y": [0, 0, 0]}},
          {"t": 45, "s": [110, 110, 100], "e": [100, 100, 100],
           "i": {"x": [0.42, 0.42, 0.42], "y": [1, 1, 1]},
           "o": {"x": [0.58, 0.58, 0.58], "y": [0, 0, 0]}},
          {"t": 90, "s": [100, 100, 100]}
        ]
      },
      "r": {"a": 0, "k": 0},
      "o": {"a": 0, "k": 100}
    },
    "shapes": [
      {
        "ty": "el",
        "nm": "Circle",
        "p": {"a": 0, "k": [0, 0]},
        "s": {"a": 0, "k": [200, 200]}
      },
      {
        "ty": "fl",
        "nm": "Fill",
        "c": {"a": 0, "k": [0.2, 0.4, 0.8, 1]},
        "o": {"a": 0, "k": 100}
      }
    ],
    "ip": 0,
    "op": 90
  }]
}
```

**Parameters:**
- Shape: Filled circle (200x200px)
- Scale: 100% → 110% → 100%
- No external image required

**Use for:** Geometric logos, badges, icons, minimalist tech brands

**Shape Layer vs Image Layer:**
- ✅ Shape: Simple geometry, line art, minimalist designs, small file size
- ✅ Image: Complex logos, gradients, photos, detailed artwork

---

## Advanced Compositions

### Bounce + Wiggle (Impact Effect)

Combine position bounce with rotation wiggle.

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 48,
  "w": 800,
  "h": 400,
  "layers": [{
    "ind": 1,
    "ty": 2,
    "nm": "Logo",
    "refId": "logo_image",
    "ks": {
      "p": {
        "a": 1,
        "k": [
          {"t": 0, "s": [400, 150], "e": [400, 200], "i": {"x": [0.175], "y": [0.885]}, "o": {"x": [0.32], "y": [1.275]}},
          {"t": 24, "s": [400, 200], "e": [400, 190], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 36, "s": [400, 190], "e": [400, 200], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 48, "s": [400, 200]}
        ]
      },
      "r": {
        "a": 1,
        "k": [
          {"t": 24, "s": [0], "e": [-3], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
          {"t": 30, "s": [-3], "e": [3], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
          {"t": 36, "s": [3], "e": [-2], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
          {"t": 42, "s": [-2], "e": [0], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
          {"t": 48, "s": [0]}
        ]
      },
      "s": {"a": 0, "k": [100, 100]},
      "a": {"a": 0, "k": [256, 128]},
      "o": {"a": 0, "k": 100}
    },
    "ip": 0,
    "op": 48
  }],
  "assets": [{"id": "logo_image", "w": 512, "h": 256, "p": "logo.png", "e": 0}]
}
```

**Effect:**
- Position: Drops down with bounce (0-24 frames)
- Rotation: Wiggles after landing (24-48 frames)
- Creates "impact + settle" effect

**Use for:** Notification alerts, playful interactions, game UI

---

### Fade + Scale + Rotate (Triple Property)

Maximum impact entrance animation.

```json
{
  "v": "5.7.4",
  "fr": 60,
  "ip": 0,
  "op": 90,
  "w": 800,
  "h": 400,
  "layers": [{
    "ind": 1,
    "ty": 2,
    "nm": "Logo",
    "refId": "logo_image",
    "ks": {
      "o": {
        "a": 1,
        "k": [
          {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 60, "s": [100]}
        ]
      },
      "s": {
        "a": 1,
        "k": [
          {"t": 0, "s": [60, 60], "e": [110, 110], "i": {"x": [0.175], "y": [0.885]}, "o": {"x": [0.32], "y": [1.275]}},
          {"t": 60, "s": [110, 110], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 90, "s": [100, 100]}
        ]
      },
      "r": {
        "a": 1,
        "k": [
          {"t": 0, "s": [-15], "e": [5], "i": {"x": [0.175], "y": [0.885]}, "o": {"x": [0.32], "y": [1.275]}},
          {"t": 60, "s": [5], "e": [0], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
          {"t": 90, "s": [0]}
        ]
      },
      "p": {"a": 0, "k": [400, 200]},
      "a": {"a": 0, "k": [256, 128]}
    },
    "ip": 0,
    "op": 90
  }],
  "assets": [{"id": "logo_image", "w": 512, "h": 256, "p": "logo.png", "e": 0}]
}
```

**Properties:**
- Opacity: 0% → 100% (fade in)
- Scale: 60% → 110% → 100% (overshoot)
- Rotation: -15° → 5° → 0° (spin + settle)

**Use for:** Energetic brand moments, startup intros, bold marketing

---

## Usage Notes

**External References During Development:**
Always use external file references (`"e": 0`) during development and rendering:

```json
"assets": [{"id": "logo_image", "w": 512, "h": 256, "p": "logo.png", "e": 0}]
```

**Converting to Embedded Base64 (Distribution):**
After successful rendering, optionally embed for distribution:

```json
"assets": [{"id": "logo_image", "w": 512, "h": 256, "p": "data:image/png;base64,iVBORw0KG...", "e": 1}]
```

Use `scripts/prepare_logo.py` to generate base64 strings automatically.

---

## Related Documentation

- **Animation Theory**: See [references/animation_theory.md](animation_theory.md)
- **Lottie Spec**: See [references/lottie_spec.md](lottie_spec.md)
- **Preset Library**: See [references/preset_library.md](preset_library.md)
- **Script Usage**: See [references/script_usage.md](script_usage.md)
- **Text Animation**: See [references/text_animation_guide.md](text_animation_guide.md)
