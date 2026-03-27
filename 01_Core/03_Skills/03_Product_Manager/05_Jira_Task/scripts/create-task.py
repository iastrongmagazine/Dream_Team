#!/usr/bin/env python3
"""
Task Generator

Generates Jira task structure from description.
"""

import sys
from datetime import datetime


BUG_TEMPLATE = """# [BUG] {title}

## Description

**Current State:**
- {current_state}

**Expected State:**
- {expected_state}

## Acceptance Criteria
- [ ] Fix the bug
- [ ] Add regression test

## Technical Notes
- Affected files: `{files}`

## Testing
- [ ] Reproduce bug
- [ ] Verify fix
- [ ] Run regression tests

## Priority
High (blocking users)

Generated: {date}
"""

FEATURE_TEMPLATE = """# [FEATURE] {title}

## Description
{description}

## User Story
As a {user}, I want to {action} so that {benefit}.

## Acceptance Criteria
- [ ] Feature works as described
- [ ] Tests pass
- [ ] Documentation updated

## Child Tasks
- [ ] [FEATURE] {title} (API)
- [ ] [FEATURE] {title} (UI)

## Priority
Medium

Generated: {date}
"""


def generate_task(task_type, title, details=""):
    """Generate task structure."""
    template = BUG_TEMPLATE if task_type == "bug" else FEATURE_TEMPLATE

    print(
        template.format(
            title=title,
            current_state=details or "Describe current broken state",
            expected_state="Describe expected behavior",
            files="path/to/affected/file",
            description=details or f"Implement {title}",
            user="user",
            action=f"use {title}",
            benefit=f"improved experience",
            date=datetime.now().strftime("%Y-%m-%d"),
        )
    )


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python create-task.py <bug|feature> <title>")
        sys.exit(1)

    generate_task(sys.argv[1], " ".join(sys.argv[2:]))
