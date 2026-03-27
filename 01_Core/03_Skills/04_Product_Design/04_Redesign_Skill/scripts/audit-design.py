#!/usr/bin/env python3
"""
Design Audit Script

Scans codebase for generic design patterns.
"""

import sys
from pathlib import Path


GENERIC_PATTERNS = {
    "inter": "Replace with Geist, Outfit, Satoshi",
    "roboto": "Replace with premium font",
    "shadow-md": "Use ultra-diffuse shadow",
    "shadow-lg": "Use ultra-diffuse shadow",
    "#000000": "Use #111111 or #2F3437",
    "fontawesome": "Use Phosphor or Radix icons",
    "lucide": "Check if appropriate for premium",
    "text-gray-500": "Use #787774 for muted text",
}


def audit_file(filepath):
    """Audit a single file for generic patterns."""
    issues = []

    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")

        for pattern, suggestion in GENERIC_PATTERNS.items():
            if pattern.lower() in content.lower():
                issues.append(
                    {
                        "file": str(filepath),
                        "pattern": pattern,
                        "suggestion": suggestion,
                    }
                )
    except Exception as e:
        pass

    return issues


def audit_project(project_dir):
    """Audit entire project."""
    print("=" * 50)
    print("🔍 DESIGN AUDIT")
    print("=" * 50)

    all_issues = []
    exts = {".tsx", ".jsx", ".css", ".scss", ".vue", ".html"}

    for ext in exts:
        for filepath in Path(project_dir).rglob(f"*{ext}"):
            issues = audit_file(filepath)
            all_issues.extend(issues)

    if all_issues:
        print(f"\n⚠️  Found {len(all_issues)} issues:\n")
        for i, issue in enumerate(all_issues[:20], 1):
            print(f"{i}. {issue['pattern']}")
            print(f"   File: {issue['file']}")
            print(f"   → {issue['suggestion']}\n")
    else:
        print("\n✅ No generic patterns found!")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python audit-design.py <project-dir>")
        sys.exit(1)

    audit_project(sys.argv[1])
