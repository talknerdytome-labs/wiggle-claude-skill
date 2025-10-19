# Wiggle - Logo Animation Skill for Claude Code

Create professional logo animations using Lottie JSON format. Transform static logos (PNG/SVG/JPG) into animated GIFs and MP4s with professionally-crafted motion patterns.

## Overview

**Wiggle** is a Claude Code skill that enables you to:
- 🎬 Animate static logos with professional motion design patterns
- 📦 Generate Lottie JSON animations with automatic GIF/MP4 rendering
- ✨ Apply various animation effects: fade, bounce, pulse, rotate, wiggle, waveforms
- 🎨 Extract and animate multi-element logos (icon + text)
- 🔄 Create perfect loops with validation
- 🚀 Preview animations quickly before full rendering

## Features

### Core Capabilities
- **Multiple Animation Patterns**: Fade, bounce, scale pulse, rotation, wiggle, waveforms
- **Multi-Element Support**: Animate icon and text separately or together
- **Format Support**: Lottie JSON, GIF, MP4, PNG sequences
- **Smart Asset Handling**: Automatic validation and path resolution
- **Preview Mode**: Render only first N frames for quick iteration
- **Loop Validation**: Ensure seamless looping animations

### New in Latest Version ✨
- ✅ Automatic asset validation (checks for missing external files)
- ✅ Asset path resolution (relative to JSON file location)
- ✅ Output verification (detects blank/corrupted files)
- ✅ Preview mode (`--preview-frames N`) - renders only first N frames
- ✅ Test mode (`--test-render`) - small test render with confirmation prompt

## Installation

### For Claude Code Users

Install the skill via the Claude Code marketplace:

```bash
# Add the marketplace (if not already added)
/plugin marketplace add anthropics/skills

# Install wiggle skill
/plugin install wiggle@anthropic-agent-skills
```

Or install from this repository:

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/wiggle-claude-skill.git

# Install as a local skill in Claude Code
# Copy/symlink to your Claude Code skills directory
```

### Dependencies

The skill requires these Python packages:

```bash
pip install lottie[all]    # Lottie manipulation
pip install Pillow         # Image processing
pip install pycairo        # Cairo rendering (for GIF)
```

#### Cairo Installation

**macOS:**
```bash
brew install cairo pkg-config
pip install pycairo
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt-get install libcairo2-dev pkg-config python3-dev
pip install pycairo
```

**Verify:**
```bash
python3 -c "import cairo; print('Cairo OK')"
```

## Quick Start

### Basic Usage with Claude Code

1. **Ask Claude to animate your logo:**
```
Animate my logo with a bounce entrance effect
```

2. **Provide your logo file** (PNG, SVG, or JPG)

3. **Claude will:**
   - Analyze your logo structure
   - Define appropriate motion philosophy
   - Prepare optimized assets
   - Create Lottie JSON animation
   - Render preview and final outputs

### Example Requests

```
"Create a pulsing animation for my logo"
"Make my logo wiggle when it appears"
"Add a professional fade-in effect to my brand logo"
"Create a waveform animation for my audio app logo"
"Animate my logo with a bounce entrance, then loop it"
```

## Scripts Reference

| Script | Purpose | Example |
|--------|---------|---------|
| `prepare_logo.py` | Optimize and convert logo images | `python scripts/prepare_logo.py logo.png --max-size 500` |
| `extract_svg_elements.py` | Extract elements from SVG | `python scripts/extract_svg_elements.py logo.svg --list` |
| `validate_lottie.py` | Check Lottie structure | `python scripts/validate_lottie.py animation.json` |
| `validate_loop.py` | Verify perfect loop | `python scripts/validate_loop.py animation.json` |
| `render_lottie.py` | Render to GIF/MP4 | `python scripts/render_lottie.py animation.json output.gif` |
| `render_lottie.py --preview-frames N` | Quick preview | `python scripts/render_lottie.py animation.json preview.gif --preview-frames 60` |
| `render_lottie.py --test-render` | Test mode with warnings | `python scripts/render_lottie.py animation.json test.gif --test-render` |
| `batch_export.py` | Export multiple formats | `python scripts/batch_export.py animation.json ./output gif,mp4` |

## Animation Patterns

### Single-Element Patterns

- **Fade + Gentle Scale**: Corporate entrances (1.5s)
- **Bounce Entrance**: Energetic brands (1.2s)
- **Scale Pulse**: Idle states, CTAs (3s loop)
- **Smooth Rotation**: Loading, tech logos (10s loop)
- **Wiggle/Jello**: Playful notifications (0.8s)
- **Vertical Waveform**: Audio/speech brands (3s loop)

### Multi-Element Coordination

- **Simultaneous Entrance**: Both elements appear together (cohesive brand)
- **Staggered Entrance**: Icon first, text follows (storytelling)

See [SKILL.md](SKILL.md) for complete documentation and [references/detailed_examples.md](references/detailed_examples.md) for code examples.

## Workflow

```
1. Define Motion Philosophy (30s)
   └─ What personality? What emotion? What motion metaphor?

2. Analyze Logo Structure (30s)
   └─ Text? Multi-element? SVG or PNG?

3. Prepare Assets
   └─ python scripts/prepare_logo.py logo.png --max-size 500

4. Create Lottie JSON Animation
   └─ Use external references ("e": 0) during development

5. Validate
   └─ python scripts/validate_lottie.py animation.json

6. Render with Preview
   └─ python scripts/render_lottie.py animation.json preview.gif --preview-frames 60

7. Full Render
   └─ python scripts/render_lottie.py animation.json logo.gif
```

## Known Limitations

### Asset Path Resolution

External assets (PNGs/SVGs) are resolved **relative to the Lottie JSON file location**. Place assets in the same directory as your JSON file:

```
✅ Correct:
project/
├── animation.json
└── logo_optimized.png

❌ Wrong:
project/
├── animations/
│   └── animation.json  (references "../logo_optimized.png")
└── logo_optimized.png
```

### Embedded Base64 vs External References

**Recommended workflow:**
1. Use external references (`"e": 0`) during development/rendering
2. Optionally embed base64 AFTER successful rendering for distribution
3. Keep external version for future edits

**Why?** Cairo renderer crashes with embedded images >100KB.

## Troubleshooting

### Asset not found errors
- **Fix:** Move assets to JSON file's directory
- **Validation:** `render_lottie.py` validates assets before rendering

### Blank/corrupted output
- **Fix:** Check asset validation messages, verify file sizes
- **Detection:** Output verification runs automatically

### MemoryError during rendering
- **Fix:** Use external reference (`"e": 0`) instead of embedded base64

### Preview renders save time
- **Tip:** Use `--preview-frames 60` to validate concept before full render
- **Tip:** Use `--test-render` for interactive testing

See [SKILL.md](SKILL.md) troubleshooting section for comprehensive guide.

## Documentation

- **[SKILL.md](SKILL.md)** - Complete skill documentation and workflow
- **[references/detailed_examples.md](references/detailed_examples.md)** - Full Lottie JSON code examples
- **[references/animation_theory.md](references/animation_theory.md)** - Motion design principles
- **[references/preset_library.md](references/preset_library.md)** - Complete preset collection
- **[references/text_animation_guide.md](references/text_animation_guide.md)** - Text animation workflows
- **[references/troubleshooting.md](references/troubleshooting.md)** - Comprehensive troubleshooting
- **[references/real-world-examples/](references/real-world-examples/)** - Production animations from major brands

## File Size Guidelines

| Use Case | Lottie JSON | GIF | MP4 | Image Assets |
|----------|-------------|-----|-----|--------------|
| Email signature | 20-50KB | 500KB-1MB | 200-500KB | <30KB each |
| Website hero | 30-80KB | 1-3MB | 500KB-1.5MB | <50KB each |
| Social media | 50-150KB | 3-8MB | 1-3MB | <80KB each |
| Splash screen | 30-100KB | 2-5MB | 800KB-2MB | <60KB each |

## Examples

Check out [references/real-world-examples/](references/real-world-examples/) for production animations from:
- Reddit - Playful elastic bounce
- Slack - Professional restrained pinch
- Medium - Gentle editorial fade
- Flickr - Camera shutter effect
- Discord - Character wink

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for:
- New animation patterns
- Bug fixes
- Documentation improvements
- Additional helper scripts

## License

See [LICENSE.txt](LICENSE.txt) for details.

## Credits

Created for use with [Claude Code](https://claude.com/claude-code) by Anthropic.

Part of the [Anthropic Agent Skills](https://github.com/anthropics/skills) collection.
