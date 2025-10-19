# Fonts for Text-Based Logo Generation

When users don't provide a logo image, generate simple text-based logos using these recommended fonts.

## Recommended Professional Fonts

### For Modern/Tech Brands
- **Inter** - Clean, modern sans-serif
  - Download: https://fonts.google.com/specimen/Inter
  - License: Open Font License
  - Use: Tech startups, SaaS, digital products

- **Poppins** - Geometric sans-serif
  - Download: https://fonts.google.com/specimen/Poppins
  - License: Open Font License
  - Use: Creative agencies, apps, friendly brands

### For Corporate/Professional
- **Roboto** - Neutral, versatile
  - Download: https://fonts.google.com/specimen/Roboto
  - License: Apache License 2.0
  - Use: Business, finance, consulting

- **Work Sans** - Clean professional sans-serif
  - Download: https://fonts.google.com/specimen/Work+Sans
  - License: Open Font License
  - Use: Corporate, B2B, services

### For Luxury/Premium
- **Playfair Display** - Elegant serif
  - Download: https://fonts.google.com/specimen/Playfair+Display
  - License: Open Font License
  - Use: Fashion, jewelry, high-end services

- **Cinzel** - Classical serif
  - Download: https://fonts.google.com/specimen/Cinzel
  - License: Open Font License
  - Use: Luxury, heritage brands, law firms

## Installation

Download fonts from Google Fonts and install system-wide, or reference them in Lottie animations.

For Lottie text layers, use system fonts or embed font data.

## Usage in Lottie

When creating text-based logos in Lottie JSON:

```json
{
  "ty": 5,  // Text layer
  "t": {
    "d": {
      "k": [
        {
          "s": {
            "s": 72,           // Font size
            "f": "Inter-Bold", // Font name
            "t": "BRAND",      // Text content
            "j": 2,            // Alignment (2 = center)
            "tr": 0,           // Tracking
            "lh": 86.4,        // Line height
            "fc": [0,0,0]      // Fill color RGB
          }
        }
      ]
    }
  }
}
```

## Fallback Strategy

If specified font isn't available:
1. Use system default sans-serif
2. Convert text to vector paths (font-independent)
3. Or ask user to provide logo image instead
