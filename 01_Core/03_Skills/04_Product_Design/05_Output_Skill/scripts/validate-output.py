#!/usr/bin/env python3
"""
Output Validator

Validates that output is complete without banned patterns.
"""

import sys
import re


BANNED_PATTERNS = [
    r"//\s*\.\.\.",
    r"//\s*rest of code",
    r"//\s*implement here",
    r"//\s*TODO",
    r"/\*\s*\.\.\.\s*\*/",
    r"//\s*similar to above",
    r"//\s*continue pattern",
    r"//\s*add more as needed",
    r"Let me know if you want me to continue",
    r"I can provide more details if needed",
    r"for brevity",
    r"the rest follows the same pattern",
    r"I'll leave that as an exercise",
]


def validate_output(content):
    """Validate content for banned patterns."""
    issues = []
    passed = []

    for pattern in BANNED_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            issues.append(f"❌ Banned pattern: {pattern}")

    if not issues:
        passed.append("✅ No banned patterns found")

    # Check for completeness hints
    if content.strip().endswith("..."):
        issues.append("❌ Ends with ... (suspicious truncation)")
    else:
        passed.append("✅ No truncation at end")

    return passed, issues


if __name__ == "__main__":
    print("=" * 50)
    print("📝 OUTPUT VALIDATOR")
    print("=" * 50)

    if len(sys.argv) < 2:
        print("\nUsage: python validate-output.py <file>")
        sys.exit(1)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        content = f.read()

    passed, issues = validate_output(content)

    print(f"\n✅ Passed: {len(passed)}")
    for p in passed:
        print(f"   {p}")

    if issues:
        print(f"\n❌ Issues: {len(issues)}")
        for issue in issues:
            print(f"   {issue}")
    else:
        print("\n🎉 Output is complete and clean!")
