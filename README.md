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

### New in Latest Version
- ✅ Automatic asset validation (checks for missing external files)
- ✅ Asset path resolution (relative to JSON file location)
- ✅ Output verification (detects blank/corrupted files)
- ✅ Preview mode - renders only first N frames for quick testing
- ✅ Test mode - small test render with confirmation prompt

## Installation

1. **[Download this skill](https://github.com/talknerdytome-labs/wiggle-claude-skill/archive/refs/heads/main.zip)** as a ZIP file
2. **Add to Claude** following the [official skills guide](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
3. **Start animating!** Claude Code handles all dependencies automatically

That's it! No manual dependency installation needed - Claude Code manages the Python environment.

## Quick Start

### Basic Usage

Simply ask Claude to animate your logo:

```
Animate my logo with a bounce entrance effect
```

Then provide your logo file (PNG, SVG, or JPG).

Claude will:
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

## Typical Workflow

When you work with Claude using this skill:

```
1. Define Motion Philosophy (30s)
   └─ What personality? What emotion? What motion metaphor?

2. Analyze Logo Structure (30s)
   └─ Text? Multi-element? SVG or PNG?

3. Prepare Assets
   └─ Claude optimizes your logo automatically

4. Create Lottie JSON Animation
   └─ Uses external references for reliability

5. Validate & Preview
   └─ Quick preview render to verify concept

6. Full Render
   └─ Generate final GIF/MP4 outputs
```

## Troubleshooting

### Asset not found errors
- Assets must be in the same directory as the Lottie JSON file
- Claude validates assets before rendering

### Blank or corrupted output
- Check asset validation messages
- Verify file sizes aren't too large

### Want to iterate faster?
- Ask Claude to render a preview first (only first 60 frames)
- Use test mode for quick concept validation

See [references/troubleshooting.md](references/troubleshooting.md) for comprehensive troubleshooting guide.

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
