#!/usr/bin/env python3
"""
Premium Design Validator

Validates design output against Awwwards-tier rules.
"""

import sys
import re


BANNED_FONTS = ["inter", "roboto", "arial", "open sans", "helvetica"]
BANNED_ICONS = ["fontawesome", "material icons", "lucide"]
PREMIUM_FONTS = ["geist", "clash display", "pp editorial", "plus jakarta sans"]


def validate_premium(content):
    """Validate content against premium rules."""
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

    # Check for premium font
    for font in PREMIUM_FONTS:
        if font in content_lower:
            passed.append(f"✅ Premium font found: {font}")
            break

    # Check for banned icons
    for icon in BANNED_ICONS:
        if icon in content_lower:
            issues.append(f"❌ Banned icon library: {icon}")
            break
    else:
        passed.append("✅ No banned icons")

    # Check for h-screen
    if "h-screen" in content_lower:
        issues.append("❌ Uses h-screen (should use min-h-[100dvh])")
    else:
        passed.append("✅ Uses correct min-height")

    # Check for harsh shadows
    if "shadow-md" in content_lower or "rgba(0,0,0,0.3)" in content_lower:
        issues.append("❌ Harsh shadow detected")
    else:
        passed.append("✅ No harsh shadows")

    return passed, issues


if __name__ == "__main__":
    print("=" * 50)
    print("✨ PREMIUM DESIGN VALIDATOR")
    print("=" * 50)

    if len(sys.argv) < 2:
        print("\nUsage: python validate-premium.py <file>")
        print("       python validate-premium.py --check 'content'")
        sys.exit(1)

    if sys.argv[1] == "--check":
        content = " ".join(sys.argv[2:])
    else:
        with open(sys.argv[1], "r", encoding="utf-8") as f:
            content = f.read()

    passed, issues = validate_premium(content)

    print(f"\n✅ Passed: {len(passed)}")
    for p in passed:
        print(f"   {p}")

    if issues:
        print(f"\n❌ Issues: {len(issues)}")
        for issue in issues:
            print(f"   {issue}")
    else:
        print("\n🎉 Premium design validated!")
