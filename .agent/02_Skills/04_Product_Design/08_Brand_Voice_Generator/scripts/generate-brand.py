#!/usr/bin/env python3
"""
Brand File Generator

Generates skeleton brand files.
"""

import sys
import json
from datetime import datetime


BRAND_JSON = {
    "name": "Brand Name",
    "tagline": "Your tagline here",
    "colors": {
        "primary": "#3B82F6",
        "secondary": "#10B981",
        "accent": "#F59E0B",
        "background": "#FFFFFF",
        "text": "#1F2937",
    },
    "fonts": {"heading": "Geist", "body": "Geist Sans", "mono": "Geist Mono"},
    "audience": {
        "primary": "Your target audience",
        "pain_points": ["Pain point 1"],
        "goals": ["Goal 1"],
    },
    "values": ["Value 1", "Value 2", "Value 3"],
}

TONE_OF_VOICE = """# Tone of Voice

## Brand Personality
[Describe your brand personality]

## Voice Attributes
- **Formal/Casual:** [Choose one]
- **Technical/Accessible:** [Choose one]  
- **Serious/Playful:** [Choose one]

## Writing Guidelines

### Do
- Use active voice
- Be clear and specific
- Write for your audience

### Don't
- Use jargon without explanation
- Be vague or generic
- Copy competitor language

## Examples

### Good
"[Example of good copy]"

### Bad
"[Example of bad copy]"
"""


def generate_brand_files(name):
    """Generate brand file skeletons."""
    BRAND_JSON["name"] = name

    print("Generated files:")
    print(f"\n📁 brand.json:\n{json.dumps(BRAND_JSON, indent=2)}")
    print(f"\n📁 tone-of-voice.md:\n{TONE_OF_VOICE}")
    print(f"\n📁 brand-system.md: [Create with brand philosophy]")
    print(f"\n📁 config.json: [Create with output settings]")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate-brand.py <brand-name>")
        sys.exit(1)

    generate_brand_files(" ".join(sys.argv[1:]))
