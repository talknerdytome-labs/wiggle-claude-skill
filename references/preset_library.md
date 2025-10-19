# Logo Animation Preset Library

Curated collection of production-ready Lottie JSON templates for common logo animation patterns.

## How to Use Presets

Each preset is a complete Lottie JSON structure. To use:

1. Replace placeholder values (width, height, duration, colors)
2. Add your logo as an image asset or shape layers
3. Adjust easing and timing to match brand personality
4. Validate with `validate_lottie.py`
5. Render with `render_lottie.py`

## Branding Style Presets

### 1. Corporate Subtle - Fade + Gentle Scale

Professional entrance for corporate brands. Minimal movement, maximum confidence.

**Use case**: B2B, finance, consulting, legal
**Duration**: 1.5s
**Loop**: No (one-time entrance)

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 45,
  "w": 800,
  "h": 400,
  "layers": [
    {
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
        "p": {"a": 0, "k": [400, 200]},
        "a": {"a": 0, "k": [256, 128]},
        "s": {
          "a": 1,
          "k": [
            {"t": 0, "s": [95, 95], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 45, "s": [100, 100]}
          ]
        },
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 45,
      "st": 0
    }
  ],
  "assets": [
    {
      "id": "logo_image",
      "w": 512,
      "h": 256,
      "p": "logo.png",
      "u": "",
      "e": 0
    }
  ]
}
```

### 2. Startup Energetic - Bounce + Overshoot

Dynamic entrance with personality. Shows energy and approachability.

**Use case**: Startups, tech, creative agencies
**Duration**: 1.2s
**Loop**: No

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 36,
  "w": 800,
  "h": 400,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Logo",
      "refId": "logo_image",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [1], "y": [0]}},
            {"t": 20, "s": [100]}
          ]
        },
        "p": {
          "a": 1,
          "k": [
            {"t": 0, "s": [400, 100], "e": [400, 200], "i": {"x": [0.175], "y": [0.885]}, "o": {"x": [0.32], "y": [1.275]}},
            {"t": 36, "s": [400, 200]}
          ]
        },
        "a": {"a": 0, "k": [256, 128]},
        "s": {
          "a": 1,
          "k": [
            {"t": 0, "s": [80, 80], "e": [105, 105], "i": {"x": [0.175], "y": [0.885]}, "o": {"x": [0.32], "y": [1.275]}},
            {"t": 24, "s": [105, 105], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 36, "s": [100, 100]}
          ]
        },
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 36,
      "st": 0
    }
  ],
  "assets": [
    {
      "id": "logo_image",
      "w": 512,
      "h": 256,
      "p": "logo.png",
      "u": "",
      "e": 0
    }
  ]
}
```

### 3. Luxury Elegant - Slow Fade + Minimal Scale

Sophisticated, restrained entrance. Premium feel through slow, deliberate motion.

**Use case**: Luxury brands, fashion, jewelry, high-end services
**Duration**: 3s
**Loop**: No

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 90,
  "w": 800,
  "h": 400,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Logo",
      "refId": "logo_image",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0], "e": [100], "i": {"x": [0.25], "y": [0.1]}, "o": {"x": [0.25], "y": [1]}},
            {"t": 90, "s": [100]}
          ]
        },
        "p": {"a": 0, "k": [400, 200]},
        "a": {"a": 0, "k": [256, 128]},
        "s": {
          "a": 1,
          "k": [
            {"t": 0, "s": [98, 98], "e": [100, 100], "i": {"x": [0.25], "y": [0.1]}, "o": {"x": [0.25], "y": [1]}},
            {"t": 90, "s": [100, 100]}
          ]
        },
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 90,
      "st": 0
    }
  ],
  "assets": [
    {
      "id": "logo_image",
      "w": 512,
      "h": 256,
      "p": "logo.png",
      "u": "",
      "e": 0
    }
  ]
}
```

### 4. Tech Glitch - Digital Disruption Effect

Glitchy, digital entrance. Perfect for tech, gaming, cybersecurity brands.

**Use case**: Tech startups, gaming, digital products, cybersecurity
**Duration**: 1s
**Loop**: No

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 30,
  "w": 800,
  "h": 400,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Logo",
      "refId": "logo_image",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0], "e": [0], "i": {"x": [1], "y": [1]}, "o": {"x": [0], "y": [0]}},
            {"t": 3, "s": [0], "e": [100], "i": {"x": [1], "y": [1]}, "o": {"x": [0], "y": [0]}},
            {"t": 6, "s": [100], "e": [0], "i": {"x": [1], "y": [1]}, "o": {"x": [0], "y": [0]}},
            {"t": 9, "s": [0], "e": [100], "i": {"x": [1], "y": [1]}, "o": {"x": [0], "y": [0]}},
            {"t": 12, "s": [100], "e": [100], "i": {"x": [1], "y": [1]}, "o": {"x": [0], "y": [0]}},
            {"t": 30, "s": [100]}
          ]
        },
        "p": {
          "a": 1,
          "k": [
            {"t": 0, "s": [400, 200], "e": [405, 200], "i": {"x": [1], "y": [1]}, "o": {"x": [0], "y": [0]}},
            {"t": 3, "s": [405, 200], "e": [395, 200], "i": {"x": [1], "y": [1]}, "o": {"x": [0], "y": [0]}},
            {"t": 6, "s": [395, 200], "e": [402, 200], "i": {"x": [1], "y": [1]}, "o": {"x": [0], "y": [0]}},
            {"t": 9, "s": [402, 200], "e": [400, 200], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 30, "s": [400, 200]}
          ]
        },
        "a": {"a": 0, "k": [256, 128]},
        "s": {"a": 0, "k": [100, 100]},
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 30,
      "st": 0
    }
  ],
  "assets": [
    {
      "id": "logo_image",
      "w": 512,
      "h": 256,
      "p": "logo.png",
      "u": "",
      "e": 0
    }
  ]
}
```

## Use Case Presets

### 5. Website Hero - Quick Professional Entrance

Fast, polished entrance for website headers. Doesn't delay content viewing.

**Duration**: 0.8s
**Loop**: No
**Optimized for**: Above-the-fold hero sections

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 24,
  "w": 300,
  "h": 100,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Logo",
      "refId": "logo_image",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 24, "s": [100]}
          ]
        },
        "p": {
          "a": 1,
          "k": [
            {"t": 0, "s": [120, 50], "e": [150, 50], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 24, "s": [150, 50]}
          ]
        },
        "a": {"a": 0, "k": [128, 64]},
        "s": {"a": 0, "k": [100, 100]},
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 24,
      "st": 0
    }
  ],
  "assets": [
    {
      "id": "logo_image",
      "w": 256,
      "h": 128,
      "p": "logo.png",
      "u": "",
      "e": 0
    }
  ]
}
```

### 6. Email Signature - Subtle Loop

Gentle, non-distracting loop for email signatures. Professional and polished.

**Duration**: 3s loop
**Loop**: Yes (infinite)
**Optimized for**: Small file size, subtle motion

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 90,
  "w": 200,
  "h": 80,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Logo",
      "refId": "logo_image",
      "ks": {
        "o": {"a": 0, "k": 100},
        "p": {"a": 0, "k": [100, 40]},
        "a": {"a": 0, "k": [64, 32]},
        "s": {
          "a": 1,
          "k": [
            {"t": 0, "s": [100, 100], "e": [102, 102], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
            {"t": 45, "s": [102, 102], "e": [100, 100], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
            {"t": 90, "s": [100, 100]}
          ]
        },
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 90,
      "st": 0
    }
  ],
  "assets": [
    {
      "id": "logo_image",
      "w": 128,
      "h": 64,
      "p": "logo.png",
      "u": "",
      "e": 0
    }
  ]
}
```

### 7. Social Media Intro - Bold Entrance

Eye-catching animation for social media video intros. Grabs attention quickly.

**Duration**: 2s
**Loop**: No
**Optimized for**: Instagram, TikTok, YouTube intros

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 60,
  "w": 1080,
  "h": 1080,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Logo",
      "refId": "logo_image",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [1], "y": [0]}},
            {"t": 30, "s": [100]}
          ]
        },
        "p": {"a": 0, "k": [540, 540]},
        "a": {"a": 0, "k": [256, 256]},
        "s": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0, 0], "e": [110, 110], "i": {"x": [0.175], "y": [0.885]}, "o": {"x": [0.32], "y": [1.5]}},
            {"t": 40, "s": [110, 110], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 60, "s": [100, 100]}
          ]
        },
        "r": {
          "a": 1,
          "k": [
            {"t": 0, "s": [90], "e": [0], "i": {"x": [0.175], "y": [0.885]}, "o": {"x": [0.32], "y": [1.275]}},
            {"t": 60, "s": [0]}
          ]
        }
      },
      "ip": 0,
      "op": 60,
      "st": 0
    }
  ],
  "assets": [
    {
      "id": "logo_image",
      "w": 512,
      "h": 512,
      "p": "logo.png",
      "u": "",
      "e": 0
    }
  ]
}
```

### 8. Splash Screen - Brand Moment

Impactful opening for app splash screens. Creates memorable brand moment.

**Duration**: 2.5s
**Loop**: No
**Optimized for**: Mobile app launches

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 75,
  "w": 1080,
  "h": 1920,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Logo",
      "refId": "logo_image",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 40, "s": [100], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 65, "s": [100], "e": [0], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
            {"t": 75, "s": [0]}
          ]
        },
        "p": {"a": 0, "k": [540, 960]},
        "a": {"a": 0, "k": [256, 256]},
        "s": {
          "a": 1,
          "k": [
            {"t": 0, "s": [90, 90], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 40, "s": [100, 100], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 65, "s": [100, 100], "e": [110, 110], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
            {"t": 75, "s": [110, 110]}
          ]
        },
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 75,
      "st": 0
    }
  ],
  "assets": [
    {
      "id": "logo_image",
      "w": 512,
      "h": 512,
      "p": "logo.png",
      "u": "",
      "e": 0
    }
  ]
}
```

## Style Pattern Presets

### 9. Minimal Fade In

Simplest possible entrance. When subtlety is paramount.

**Duration**: 1s
**Keyframes**: 2
**Perfect for**: Minimalist brands, when logo should be understated

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 30,
  "w": 600,
  "h": 300,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Logo",
      "refId": "logo_image",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 30, "s": [100]}
          ]
        },
        "p": {"a": 0, "k": [300, 150]},
        "a": {"a": 0, "k": [256, 128]},
        "s": {"a": 0, "k": [100, 100]},
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 30,
      "st": 0
    }
  ],
  "assets": [
    {
      "id": "logo_image",
      "w": 512,
      "h": 256,
      "p": "logo.png",
      "u": "",
      "e": 0
    }
  ]
}
```

### 10. Bouncy Entrance

Fun, playful bounce. Communicates energy and approachability.

**Duration**: 1.5s
**Easing**: Bounce out
**Perfect for**: Youth brands, entertainment, food & beverage

See preset #2 (Startup Energetic) for implementation.

### 11. 3D Rotation

Simulated 3D flip rotation using scale manipulation.

**Duration**: 1.2s
**Effect**: Appears to flip in 3D space
**Perfect for**: Tech, innovation, transformation brands

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 36,
  "w": 800,
  "h": 400,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Logo",
      "refId": "logo_image",
      "ks": {
        "o": {"a": 0, "k": 100},
        "p": {"a": 0, "k": [400, 200]},
        "a": {"a": 0, "k": [256, 128]},
        "s": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0, 100], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 36, "s": [100, 100]}
          ]
        },
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 36,
      "st": 0
    }
  ],
  "assets": [
    {
      "id": "logo_image",
      "w": 512,
      "h": 256,
      "p": "logo.png",
      "u": "",
      "e": 0
    }
  ]
}
```

### 12. Particle Burst (Advanced)

Logo appears with particle burst effect. Requires additional shape layers.

**Duration**: 2s
**Complexity**: High (multiple layers)
**Perfect for**: Celebrations, launches, announcements

*Note: This is a simplified version. Full particle system requires many shape layers.*

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 60,
  "w": 800,
  "h": 400,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Logo",
      "refId": "logo_image",
      "ks": {
        "o": {
          "a": 1,
          "k": [
            {"t": 15, "s": [0], "e": [100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 35, "s": [100]}
          ]
        },
        "p": {"a": 0, "k": [400, 200]},
        "a": {"a": 0, "k": [256, 128]},
        "s": {
          "a": 1,
          "k": [
            {"t": 15, "s": [90, 90], "e": [105, 105], "i": {"x": [0.175], "y": [0.885]}, "o": {"x": [0.32], "y": [1.275]}},
            {"t": 35, "s": [105, 105], "e": [100, 100], "i": {"x": [0.42], "y": [1]}, "o": {"x": [0.58], "y": [0]}},
            {"t": 60, "s": [100, 100]}
          ]
        },
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 60,
      "st": 0
    }
  ],
  "assets": [
    {
      "id": "logo_image",
      "w": 512,
      "h": 256,
      "p": "logo.png",
      "u": "",
      "e": 0
    }
  ]
}
```

## Loop Animation Presets

### 13. Subtle Float (Perfect Loop)

Gentle up-and-down motion. Ideal for idle states.

**Duration**: 4s loop
**Motion**: Vertical float ±10px
**Perfect for**: Website heroes, loading states

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 120,
  "w": 400,
  "h": 200,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Logo",
      "refId": "logo_image",
      "ks": {
        "o": {"a": 0, "k": 100},
        "p": {
          "a": 1,
          "k": [
            {"t": 0, "s": [200, 100], "e": [200, 90], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
            {"t": 60, "s": [200, 90], "e": [200, 100], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
            {"t": 120, "s": [200, 100]}
          ]
        },
        "a": {"a": 0, "k": [128, 64]},
        "s": {"a": 0, "k": [100, 100]},
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 120,
      "st": 0
    }
  ],
  "assets": [
    {
      "id": "logo_image",
      "w": 256,
      "h": 128,
      "p": "logo.png",
      "u": "",
      "e": 0
    }
  ]
}
```

### 14. Gentle Pulse (Perfect Loop)

Breathing effect through subtle scale changes.

**Duration**: 3s loop
**Motion**: Scale 100% → 103% → 100%
**Perfect for**: CTAs, emphasis without distraction

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 90,
  "w": 400,
  "h": 200,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Logo",
      "refId": "logo_image",
      "ks": {
        "o": {"a": 0, "k": 100},
        "p": {"a": 0, "k": [200, 100]},
        "a": {"a": 0, "k": [128, 64]},
        "s": {
          "a": 1,
          "k": [
            {"t": 0, "s": [100, 100], "e": [103, 103], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
            {"t": 45, "s": [103, 103], "e": [100, 100], "i": {"x": [0.42], "y": [0]}, "o": {"x": [0.58], "y": [1]}},
            {"t": 90, "s": [100, 100]}
          ]
        },
        "r": {"a": 0, "k": 0}
      },
      "ip": 0,
      "op": 90,
      "st": 0
    }
  ],
  "assets": [
    {
      "id": "logo_image",
      "w": 256,
      "h": 128,
      "p": "logo.png",
      "u": "",
      "e": 0
    }
  ]
}
```

### 15. Slow Rotation (Perfect Loop)

Continuous rotation. Conveys progress, loading, or perpetual motion.

**Duration**: 10s loop (slower is better for logos)
**Motion**: 360° rotation
**Perfect for**: Loading indicators, tech/science brands

```json
{
  "v": "5.7.4",
  "fr": 30,
  "ip": 0,
  "op": 300,
  "w": 400,
  "h": 400,
  "layers": [
    {
      "ind": 1,
      "ty": 2,
      "nm": "Logo",
      "refId": "logo_image",
      "ks": {
        "o": {"a": 0, "k": 100},
        "p": {"a": 0, "k": [200, 200]},
        "a": {"a": 0, "k": [128, 128]},
        "s": {"a": 0, "k": [100, 100]},
        "r": {
          "a": 1,
          "k": [
            {"t": 0, "s": [0], "e": [360], "i": {"x": [1], "y": [1]}, "o": {"x": [0], "y": [0]}},
            {"t": 300, "s": [360]}
          ]
        }
      },
      "ip": 0,
      "op": 300,
      "st": 0
    }
  ],
  "assets": [
    {
      "id": "logo_image",
      "w": 256,
      "h": 256,
      "p": "logo.png",
      "u": "",
      "e": 0
    }
  ]
}
```

## Customization Tips

### Adjusting Preset Values

**Change duration:**
- Modify `"op"` value (out point)
- Adjust keyframe `"t"` values proportionally
- Example: 2x longer = multiply all `t` values by 2

**Change dimensions:**
- Modify root `"w"` and `"h"` values
- Adjust `"p"` (position) to center logo
- Update asset dimensions

**Change easing:**
- Modify `"i"` and `"o"` bezier values
- See animation_theory.md for easing presets

**Add your logo:**
- Replace `"p": "logo.png"` with your filename
- Or embed as base64 in `"p"` with `"e": 1`

### Combining Presets

Mix multiple animation properties:
1. Take opacity animation from one preset
2. Take position animation from another
3. Combine in single layer `"ks"` object
4. Ensure all keyframe timings align

### Performance Optimization

- Reduce decimal precision to 1-2 places
- Remove unused properties
- Combine similar keyframes
- Use `optimize_lottie.py` script

## Real-World Logo Animation Examples

This section contains references to real-world logo animations for inspiration and learning. **GIF/MP4 references are perfectly fine** - visual inspiration and timing references are often more valuable than having the exact Lottie JSON.

### How to Add Examples

When adding examples, include:

1. **Link to animation** (website, CodePen, LottieFiles, Dribbble, etc.)
2. **Brand/company name** (helps with searchability)
3. **Animation style** (bounce, fade, waveform, rotation, etc.)
4. **Why it works** (brand alignment, emotional impact, technical execution)
5. **Key technique** (what makes it effective - easing, timing, property combination)
6. **Lottie approximation** (optional - if no JSON available, describe how to recreate)

### Format Template

Copy this template for each new example:

```markdown
**[Brand Name]** - [Link Text](https://example.com/animation.gif)
- **Format**: GIF / MP4 / Lottie JSON / Website
- **Style**: [Specific animation type - e.g., "Elastic bounce with color transition"]
- **Duration**: [e.g., "1.5s entrance" or "3s loop"]
- **Industry**: [e.g., "Tech", "Finance", "Entertainment"]
- **Why it works**: [Brand personality alignment, emotional impact, UX considerations]
- **Key technique**: [Specific implementation detail - easing, timing, property combination]
- **Lottie approximation**: [If no JSON - describe how to recreate using Lottie properties]
  ```json
  // Optional: Lottie JSON snippet or key properties
  "s": {
    "a": 1,
    "k": [
      {"t": 0, "s": [80, 80, 100], "e": [110, 110, 100],
       "i": {"x": [0.175, 0.175, 0.42], "y": [0.885, 0.885, 1]},
       "o": {"x": [0.32, 0.32, 0.58], "y": [1.275, 1.275, 0]}}
    ]
  }
  ```

---
```

### Example Categories

Organize examples by type for easier reference:

**Corporate/Professional**
- Fade-ins with gentle scaling
- Minimal movement, high confidence
- Slow easing, subtle transforms

**Playful/Energetic**
- Bounces with overshoot
- Multiple properties animated
- Fast timing, elastic easing

**Tech/Modern**
- Glitch effects
- Geometric transformations
- Precise, mechanical movements

**Audio/Music**
- Waveform effects
- Rhythmic pulsing
- Frequency-based animations

### Real-World Examples Collection

Full Lottie JSON files available in `references/real-world-examples/` directory. All examples are hover animations at 60fps, 430x430px.

---

**Reddit** - [reddit-hover-pinch.json](real-world-examples/reddit-hover-pinch.json)
- **Format**: Lottie JSON (85KB, 5 layers)
- **Style**: Pinch/squeeze scale animation with elastic bounce
- **Duration**: 3.17s hover interaction
- **Industry**: Social Media / Community Platform
- **Why it works**: Playful personality aligns with Reddit's friendly, informal brand; pinch effect feels tactile and responsive
- **Key technique**: Inward scale squeeze followed by elastic overshoot bounce; smooth 60fps creates premium feel
- **Lottie properties**: Combined X/Y scale animation with bezier easing for squeeze → bounce transition

---

**Discord** - [discord-hover-wink.json](real-world-examples/discord-hover-wink.json)
- **Format**: Lottie JSON (168KB, 6 layers)
- **Style**: Character animation with wink/blink effect
- **Duration**: 4.28s hover interaction
- **Industry**: Communication / Gaming
- **Why it works**: Mascot-based logo benefits from personality animation; wink adds friendliness and playfulness matching Discord's casual gaming culture
- **Key technique**: Layer-based character animation with opacity/position changes to simulate eye movement
- **Lottie properties**: Multiple layer orchestration with staggered timing for natural character motion

---

**Slack** - [slack-hover-pinch.json](real-world-examples/slack-hover-pinch.json)
- **Format**: Lottie JSON (157KB, 5 layers)
- **Style**: Pinch/squeeze with professional subtle movement
- **Duration**: 3.17s hover interaction
- **Industry**: Business Communication / Productivity
- **Why it works**: More restrained than Reddit's version - professional but still friendly; suggests responsiveness and activity
- **Key technique**: Conservative scale range (minimal pinch) with smooth easing maintains professional tone while adding personality
- **Lottie properties**: Synchronized multi-layer scale animation with controlled overshoot

---

**Medium** - [medium-hover-pinch.json](real-world-examples/medium-hover-pinch.json)
- **Format**: Lottie JSON (82KB, 5 layers)
- **Style**: Gentle pinch with understated elegance
- **Duration**: 2.67s hover interaction
- **Industry**: Publishing / Content Platform
- **Why it works**: Minimal, sophisticated movement matches Medium's editorial focus; doesn't distract from content
- **Key technique**: Shorter duration and smaller scale range than social platforms; literary sophistication through restraint
- **Lottie properties**: Subtle scale variation with ease-in-out for smooth, non-distracting motion

---

**Snapchat** - [snapchat-hover-pinch.json](real-world-examples/snapchat-hover-pinch.json)
- **Format**: Lottie JSON (170KB, 6 layers)
- **Style**: Energetic pinch with bold movement
- **Duration**: 3.17s hover interaction
- **Industry**: Social Media / Camera App
- **Why it works**: High-energy animation matches Snapchat's young, dynamic audience; bold movement suggests camera capture/snap action
- **Key technique**: Aggressive scale range with fast timing; multiple layers create depth and visual interest
- **Lottie properties**: Amplified scale keyframes with sharp easing curves for punchy, attention-grabbing effect

---

**SoundCloud** - [soundcloud-hover-pinch.json](real-world-examples/soundcloud-hover-pinch.json)
- **Format**: Lottie JSON (156KB, 6 layers)
- **Style**: Rhythmic pinch with audio-inspired timing
- **Duration**: 2.67s hover interaction
- **Industry**: Audio Streaming / Music Platform
- **Why it works**: Movement rhythm suggests audio waveform compression; timing feels musical and dynamic
- **Key technique**: Keyframe timing variations create rhythmic feel rather than mechanical motion
- **Lottie properties**: Organic timing with varied keyframe spacing suggesting beat/pulse patterns

---

**Flickr** - [flickr-hover-shutter.json](real-world-examples/flickr-hover-shutter.json)
- **Format**: Lottie JSON (57KB, 6 layers)
- **Style**: Camera shutter / aperture closing effect
- **Duration**: 2.67s hover interaction
- **Industry**: Photo Sharing / Photography Platform
- **Why it works**: Shutter animation is perfect metaphor for photography platform; instantly communicates brand purpose
- **Key technique**: Radial/circular animation pattern simulating camera aperture blades
- **Lottie properties**: Multi-layer rotation + scale coordination creates mechanical shutter effect

---

**Indie Hackers** - [indie-hackers-hover-draw.json](real-world-examples/indie-hackers-hover-draw.json)
- **Format**: Lottie JSON (67KB, 6 layers)
- **Style**: Draw-on/sketch effect with progressive reveal
- **Duration**: 4.83s hover interaction
- **Industry**: Tech Community / Entrepreneurship
- **Why it works**: Hand-drawn aesthetic matches indie/bootstrap culture; progressive reveal suggests building/creating
- **Key technique**: Trim Path animation creates stroke-drawing effect; timing is slower to emphasize craftsmanship
- **Lottie properties**: Shape layer with Trim Path modifier (`s: 0→100`) creating progressive stroke reveal

---

**Renren** - [renren-hover-cycle.json](real-world-examples/renren-hover-cycle.json)
- **Format**: Lottie JSON (124KB, 5 layers)
- **Style**: Continuous rotation/cycle effect
- **Duration**: 4.07s hover interaction
- **Industry**: Social Network
- **Why it works**: Circular motion suggests connection, community cycle, social interaction flow
- **Key technique**: Smooth rotation with multiple elements creating orbital/planetary feel
- **Lottie properties**: Coordinated rotation across layers with offset timing for depth and visual interest

---

### Pattern Analysis Summary

From these 9 examples, we can identify key patterns:

**1. Pinch/Squeeze is Most Common** (Reddit, Slack, Medium, Snapchat, SoundCloud)
- Universal hover interaction pattern
- Works across industries with intensity variations
- Professional ↔ Playful spectrum achieved through scale range and timing

**2. Duration Sweet Spot: 2.5-3.5s**
- Long enough to appreciate detail
- Short enough for responsive feel
- Hover interactions are longer than entrance animations

**3. 60fps for Premium Feel**
- All examples use 60fps (not 30fps)
- Smooth motion signals quality and polish
- Worth the extra file size for hover interactions

**4. Industry-Specific Metaphors Work Best**
- Flickr: Camera shutter (photography)
- Indie Hackers: Hand-drawn sketch (indie/bootstrap)
- SoundCloud: Rhythmic timing (audio)
- Discord: Character wink (gaming/casual)

**5. File Size Range: 57KB-170KB**
- Acceptable for hover interactions (non-blocking)
- Multiple layers add personality but increase size
- Consider lazy-loading for below-fold logos

---

### Tips for Finding Examples

**Where to look**:
- **Brand websites**: Check splash screens, hero sections, loading animations
- **Dribbble**: Search "logo animation", filter by "Animation"
- **Behance**: Search "animated logo" or "motion graphics"
- **CodePen**: Search "logo animation lottie" or "svg logo animation"
- **LottieFiles**: Browse trending animations, search by category
- **Motion Design showcases**: Motionographer, Motion Array
- **Award sites**: Awwwards (Site of the Day), CSS Design Awards

**What to capture**:
- URL to the animation
- Screenshot/GIF if embedding might disappear
- Note the timing (use a stopwatch!)
- Identify which properties are animated
- Feel the easing curve (fast start? slow end? bounce?)

**Analysis framework**:
1. **Visual**: What moves? How much? In what direction?
2. **Timing**: How long? Does it loop? Entrance only?
3. **Personality**: What emotion? Professional? Playful? Bold?
4. **Technical**: Which Lottie properties would recreate this?

### Contributing Your Findings

When you find great examples:
1. Use the template above
2. Be specific about techniques
3. Include timing details (crucial for recreation)
4. Note easing characteristics (bounce, smooth, sharp?)
5. Describe how it aligns with brand personality

**Remember**: Even without Lottie JSON, a GIF + good description is extremely valuable for inspiration and timing reference!
