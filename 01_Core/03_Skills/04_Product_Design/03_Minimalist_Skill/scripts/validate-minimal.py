#!/usr/bin/env python3
"""
Minimalist Design Validator

Validates design output against minimalist rules.
"""

import sys
import re


BANNED_FONTS = ["inter", "roboto", "open sans"]
BANNED_COLORS = ["gradient", "neon", "#00ff", "#ff00", "glassmorphism"]


def validate_minimal(content):
    """Validate content against minimalist rules."""
    content_lower = content.lower()
    issues = []
    passed = []

    # Check banned fonts
    for font in BANNED_FONTS:
        if font in content_lower:
            issues.append(f"❌ Banned font: {font}")
            break
    else:
        passed.append("✅ No banned fonts")

    # Check for gradients
    if "gradient" in content_lower:
        issues.append("❌ Gradients detected (minimalist = flat)")
    else:
        passed.append("✅ No gradients")

    # Check for heavy shadows
    if any(s in content_lower for s in ["shadow-md", "shadow-lg", "shadow-xl"]):
        issues.append("❌ Heavy shadows detected")
    else:
        passed.append("✅ No heavy shadows")

    # Check for emojis
    emoji_pattern = re.compile(r"[\U0001F600-\U0001F64F]")
    if emoji_pattern.search(content):
        issues.append("❌ Emojis detected")
    else:
        passed.append("✅ No emojis")

    # Check for pure black
    if "#000000" in content_lower:
        issues.append("❌ Pure black (#000000) — use #111111 or #2F3437")
    else:
        passed.append("✅ No pure black")

    return passed, issues


if __name__ == "__main__":
    print("=" * 50)
    print("⬛ MINIMALIST DESIGN VALIDATOR")
    print("=" * 50)

    if len(sys.argv) < 2:
        print("\nUsage: python validate-minimal.py <file>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        content = f.read()

    passed, issues = validate_minimal(content)

    print(f"\n✅ Passed: {len(passed)}")
    for p in passed:
        print(f"   {p}")

    if issues:
        print(f"\n❌ Issues: {len(issues)}")
        for issue in issues:
            print(f"   {issue}")
    else:
        print("\n🎉 Minimalist design validated!")
