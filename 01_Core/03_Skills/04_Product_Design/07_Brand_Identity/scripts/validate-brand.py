#!/usr/bin/env python3
"""
Brand Validator

Validates brand consistency in content.
"""

import sys


def validate_brand(content, brand_name="Brand"):
    """Validate content against brand guidelines."""
    issues = []
    passed = []

    # Check for generic words
    generic_words = ["lorem ipsum", "john doe", "acme corp", "example.com"]
    for word in generic_words:
        if word.lower() in content.lower():
            issues.append(f"❌ Generic placeholder: {word}")

    if not any("Generic" in i for i in issues):
        passed.append("✅ No generic placeholders")

    # Check for banned AI copy
    ai_cliches = ["elevate", "seamless", "unleash", "next-gen", "game-changer"]
    for cliche in ai_cliches:
        if cliche.lower() in content.lower():
            issues.append(f"⚠️  AI cliché detected: {cliche}")

    if not issues:
        passed.append("✅ Content looks brand-aligned")

    return passed, issues


if __name__ == "__main__":
    print("=" * 50)
    print("🏷️ BRAND VALIDATOR")
    print("=" * 50)

    if len(sys.argv) < 2:
        print("\nUsage: python validate-brand.py <file>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        content = f.read()

    passed, issues = validate_brand(content)

    print(f"\n✅ Passed: {len(passed)}")
    for p in passed:
        print(f"   {p}")

    if issues:
        print(f"\n⚠️  Issues: {len(issues)}")
        for issue in issues:
            print(f"   {issue}")
    else:
        print("\n🎉 Brand identity validated!")
