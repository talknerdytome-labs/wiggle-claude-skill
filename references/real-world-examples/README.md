# Real-World Logo Animation Examples

This directory contains production Lottie JSON files from well-known brands for study and reference.

## Files

| Brand | File | Size | Duration | Layers | Animation Style |
|-------|------|------|----------|--------|-----------------|
| **Reddit** | `reddit-hover-pinch.json` | 85KB | 3.17s | 5 | Pinch/squeeze with elastic bounce |
| **Discord** | `discord-hover-wink.json` | 168KB | 4.28s | 6 | Character wink/blink effect |
| **Slack** | `slack-hover-pinch.json` | 157KB | 3.17s | 5 | Professional pinch/squeeze |
| **Medium** | `medium-hover-pinch.json` | 82KB | 2.67s | 5 | Gentle pinch with elegance |
| **Snapchat** | `snapchat-hover-pinch.json` | 170KB | 3.17s | 6 | Energetic pinch with bold movement |
| **SoundCloud** | `soundcloud-hover-pinch.json` | 156KB | 2.67s | 6 | Rhythmic pinch with audio-inspired timing |
| **Flickr** | `flickr-hover-shutter.json` | 57KB | 2.67s | 6 | Camera shutter/aperture effect |
| **Indie Hackers** | `indie-hackers-hover-draw.json` | 67KB | 4.83s | 6 | Draw-on/sketch progressive reveal |
| **Renren** | `renren-hover-cycle.json` | 124KB | 4.07s | 5 | Continuous rotation/cycle |

## Common Characteristics

- **Frame Rate**: All at 60fps for premium smoothness
- **Dimensions**: All 430x430px (standard hover icon size)
- **Context**: Hover/interaction animations (not entrance animations)
- **Duration**: 2.5-5s range (longer than typical entrance animations)

## Usage

These files can be:
1. **Studied** - Open in LottieFiles editor to understand layer structure and keyframe timing
2. **Referenced** - Use as inspiration for your own brand animations
3. **Customized** - Adapt the techniques to your own logo (change colors, timing, intensity)
4. **Analyzed** - Run through validation scripts to understand complexity and optimization

## Rendering Examples

To generate GIF previews of these animations:

```bash
# Single file
python scripts/render_lottie.py references/real-world-examples/reddit-hover-pinch.json reddit-preview.gif

# Batch render all examples
cd references/real-world-examples/
for file in *.json; do
  python ../../scripts/render_lottie.py "$file" "previews/${file%.json}.gif" 430 430 60
done
```

## Key Learnings

### 1. Pinch/Squeeze Pattern Dominates
5 out of 9 examples use pinch/squeeze - it's a safe, effective choice that works across industries.

### 2. Brand Personality Through Intensity
- **Conservative**: Medium (subtle, editorial)
- **Balanced**: Slack (professional + friendly)
- **Energetic**: Reddit, Snapchat (playful, bold)

### 3. Metaphor-Based Animations Stand Out
- Flickr's camera shutter
- Indie Hackers' hand-drawn sketch
- SoundCloud's rhythmic timing

These create stronger brand associations than generic scale/fade patterns.

### 4. Multi-Layer Depth
All examples use 5-6 layers to create depth and visual interest, not just a single animated image layer.

### 5. 60fps is the Standard
Despite larger file sizes, all examples prioritize smoothness with 60fps rather than 30fps.

## Documentation

Full analysis and pattern breakdown available in `../preset_library.md` under "Real-World Examples Collection".

## Attribution

These Lottie files are from publicly accessible brand websites and are included here for educational reference purposes only. All trademarks and brand identities belong to their respective owners.
