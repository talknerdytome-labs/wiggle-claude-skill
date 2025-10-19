# Changelog

All notable changes to the Wiggle Claude Code Skill will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.0.0] - 2025-10-19

### Initial Release

Complete logo animation skill for Claude Code with professional motion design capabilities.

### Added

#### Core Features
- Professional logo animation system using Lottie JSON format
- Multiple animation patterns: fade, bounce, pulse, rotate, wiggle, waveforms
- Multi-element support for icon + text animations
- Format support: Lottie JSON, GIF, MP4, PNG sequences
- Philosophy-first workflow for motion design
- Loop validation for seamless animations

#### Rendering Engine (`render_lottie.py`)
- ✅ Automatic asset validation (checks for missing external files before rendering)
- ✅ Smart asset path resolution (relative to JSON file location)
- ✅ Output verification (detects blank/corrupted output files)
- ✅ Preview mode (`--preview-frames N`) - renders only first N frames for quick iteration
- ✅ Test mode (`--test-render`) - small test render with size warnings and confirmation
- ✅ Working directory management (changes to JSON directory, restores after)
- Support for both GIF (Cairo) and MP4 (FFmpeg) rendering
- QuickTime-compatible MP4 encoding

#### Helper Scripts
- `prepare_logo.py` - Optimize and convert logo images (PNG/SVG/JPG)
- `extract_svg_elements.py` - Extract individual elements from SVG files
- `validate_lottie.py` - Check Lottie JSON structure and warn about large assets
- `validate_loop.py` - Verify perfect loops (first frame = last frame)
- `batch_export.py` - Export to multiple formats at once
- `check_dependencies.py` - Validate Python package installation
- `optimize_lottie.py` - Reduce Lottie JSON file sizes
- `verify_animation.py` - Comprehensive animation validation

#### Documentation
- **SKILL.md** - Complete skill documentation with workflow, patterns, and examples
- **README.md** - Repository overview and quick start guide
- **references/animation_theory.md** - Motion design principles and easing theory
- **references/detailed_examples.md** - Full Lottie JSON code examples for all patterns
- **references/preset_library.md** - Complete preset collection with real-world examples
- **references/text_animation_guide.md** - Specialized text animation workflows
- **references/anti_patterns.md** - Common mistakes with solutions
- **references/troubleshooting.md** - Comprehensive troubleshooting guide
- **references/script_usage.md** - Detailed script documentation
- **references/lottie_spec.md** - Lottie JSON specification reference

#### Real-World Examples
Production animations from major brands:
- Reddit - Playful elastic bounce
- Slack - Professional restrained pinch
- Medium - Gentle editorial fade
- Flickr - Camera shutter effect
- Discord - Character wink
- SoundCloud - Audio waveform
- Snapchat - Ghost reveal
- Renren - Circular cycle
- Indie Hackers - Path drawing

#### Assets
- Example logo SVG for testing
- Font guidelines and recommendations
- Asset optimization presets

### Technical Details

**Dependencies:**
- lottie[all] - Lottie animation manipulation
- Pillow - Image processing
- pycairo - Cairo rendering for GIF export
- FFmpeg (external) - MP4 video export

**File Statistics:**
- 37 files
- 10,794+ lines of code and documentation
- 8 Python helper scripts
- 9 real-world example animations
- 8 comprehensive reference documents

### Workflow Improvements

1. **Asset Validation** - Prevents wasted time on renders with missing assets
2. **Preview Mode** - Test animations in seconds instead of minutes
3. **Path Resolution** - Automatic handling of relative paths from JSON location
4. **Output Verification** - Catches blank/corrupted outputs immediately
5. **Philosophy-First** - 30 seconds planning prevents 15-30 minutes iteration

### Known Limitations

- External assets must be in same directory as Lottie JSON file
- Cairo renderer has memory limits with embedded base64 images >100KB
- Recommended workflow: use external references during development, embed after

### Credits

Created for [Claude Code](https://claude.com/claude-code) by Anthropic.

🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>
