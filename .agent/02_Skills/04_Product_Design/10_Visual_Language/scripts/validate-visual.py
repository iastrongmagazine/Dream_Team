#!/usr/bin/env python3
"""
Visual Language Validator

Validates visual consistency for Engram dashboard.
"""

import sys
import re


def validate_visual(content):
    """Validate content against visual rules."""
    issues = []
    passed = []

    # Check for generic SaaS indicators
    generic_indicators = ["admin-panel", "dashboard-template", "saas-kit"]
    for indicator in generic_indicators:
        if indicator in content.lower():
            issues.append(f"❌ Generic SaaS indicator: {indicator}")

    if not issues:
        passed.append("✅ No generic SaaS patterns")

    # Check for proper hierarchy (h1, h2, h3)
    has_h1 = bool(re.search(r"<h1", content))
    has_h2 = bool(re.search(r"<h2", content))

    if has_h1:
        passed.append("✅ Has H1 for main heading")
    else:
        issues.append("⚠️  No H1 found - ensure proper hierarchy")

    # Check for excessive containers
    div_count = content.count("<div")
    if div_count > 20:
        issues.append(f"⚠️  Many divs ({div_count}) - consider fewer containers")

    # Check for spacing classes
    has_spacing = any(s in content for s in ["padding", "margin", "gap", "spacing"])
    if has_spacing:
        passed.append("✅ Has spacing defined")

    return passed, issues


if __name__ == "__main__":
    print("=" * 50)
    print("🎨 VISUAL LANGUAGE VALIDATOR")
    print("=" * 50)

    if len(sys.argv) < 2:
        print("\nUsage: python validate-visual.py <file>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        content = f.read()

    passed, issues = validate_visual(content)

    print(f"\n✅ Passed: {len(passed)}")
    for p in passed:
        print(f"   {p}")

    if issues:
        print(f"\n⚠️  Issues: {len(issues)}")
        for issue in issues:
            print(f"   {issue}")
    else:
        print("\n🎉 Visual language validated!")
