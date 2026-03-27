#!/usr/bin/env python3
"""
Design Validator

Validates design output against Taste Skill rules.
"""

import sys
import re


def validate_design(content):
    """Validate design content against rules."""
    issues = []
    passed = []

    # Check for emojis
    emoji_pattern = re.compile(
        r"[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U0001F1E0-\U0001F1FF]"
    )
    if emoji_pattern.search(content):
        issues.append("❌ Contains emojis (violates Anti-Emoji Policy)")
    else:
        passed.append("✅ No emojis found")

    # Check for banned purple
    purple_patterns = ["purple", "#8b5cf6", "#a855f7", "#7c3aed", "#9333ea"]
    for pattern in purple_patterns:
        if pattern.lower() in content.lower():
            issues.append(f"❌ Contains banned purple color: {pattern}")
            break
    else:
        passed.append("✅ No banned purple colors")

    # Check for h-screen
    if "h-screen" in content:
        issues.append("❌ Uses h-screen (should use min-h-[100dvh])")
    else:
        passed.append("✅ Uses correct min-height")

    # Check for serif in tech UI context
    serif_fonts = ["serif", "Times", "Georgia", "Playfair"]
    for font in serif_fonts:
        if font.lower() in content.lower():
            issues.append(f"⚠️  Serif font found: {font} (check if appropriate)")
            break

    return passed, issues


if __name__ == "__main__":
    print("=" * 50)
    print("🎨 DESIGN VALIDATOR")
    print("=" * 50)

    if len(sys.argv) < 2:
        print("\nUsage: python validate-design.py <file>")
        print("       python validate-design.py --check 'content'")
        sys.exit(1)

    if sys.argv[1] == "--check":
        content = " ".join(sys.argv[2:])
    else:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            content = f.read()

    passed, issues = validate_design(content)

    print(f"\n✅ Passed: {len(passed)}")
    for p in passed:
        print(f"   {p}")

    if issues:
        print(f"\n❌ Issues: {len(issues)}")
        for issue in issues:
            print(f"   {issue}")
    else:
        print("\n🎉 All checks passed!")
