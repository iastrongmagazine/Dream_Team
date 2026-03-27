#!/usr/bin/env python3
"""
PR Creator Helper

Helps create pull requests with proper format.
"""

import sys
import subprocess
from datetime import datetime


PR_TEMPLATE = """## Linked Issue
Closes #{issue_number}

## PR Type
- [ ] Bug fix → `type:bug`
- [x] New feature → `type:feature`
- [ ] Documentation → `type:docs`
- [ ] Refactoring → `type:refactor`
- [ ] Maintenance → `type:chore`

## Summary
{summary}

## Changes
| File | Change |
|------|--------|
{changes}

## Test Plan
- [ ] Scripts run without errors
- [ ] Manually tested functionality
- [ ] Skills load correctly

## Checklist
- [ ] Linked approved issue
- [ ] Added type:* label
- [ ] Ran shellcheck on scripts
- [ ] No Co-Authored-By trailers
"""


def get_current_branch():
    """Get current git branch."""
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except:
        return "unknown"


def get_changed_files():
    """Get list of changed files."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "origin/main...HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return [f for f in result.stdout.strip().split("\n") if f]
    except:
        return []


def generate_pr(issue_number, summary="Feature implementation"):
    """Generate PR body."""
    files = get_changed_files()

    changes = ""
    for f in files[:5]:  # Limit to 5 files
        changes += f"| `{f}` | Modified |\n"

    if not changes:
        changes = "| `path/to/file` | What changed |\n"

    print(
        PR_TEMPLATE.format(issue_number=issue_number, summary=summary, changes=changes)
    )


if __name__ == "__main__":
    branch = get_current_branch()
    print(f"Current branch: {branch}\n")

    if len(sys.argv) < 2:
        print("Usage: python create-pr.py <issue-number> [summary]")
        sys.exit(1)

    summary = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else "Feature implementation"
    generate_pr(sys.argv[1], summary)
