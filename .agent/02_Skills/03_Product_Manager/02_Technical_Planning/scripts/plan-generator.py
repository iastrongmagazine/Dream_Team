#!/usr/bin/env python3
"""
Plan Generator

Generates implementation plan skeletons.
"""

import sys
from datetime import datetime


PLAN_TEMPLATE = """# {feature_name} Implementation Plan

> **For Claude:** Use executing-plans to implement this plan task-by-task.

**Goal:** {goal}

**Architecture:** [Describe approach]

**Tech Stack:** [Key technologies]

---

## Tasks

### Task 1: {task_1_name}

**Files:**
- Create: `path/to/file.py`
- Test: `tests/path/to/test.py`

**Step 1: Write the failing test**
```python
def test_{task_1_name}():
    # TODO: Add test
    pass
```

**Step 2: Implement**
```python
# TODO: Add implementation
```

**Step 3: Commit**
```bash
git add -A && git commit -m "feat: {task_1_name}"
```

---

*Generated: {date}*
"""


def generate_plan(feature_name, goal):
    """Generate a plan skeleton."""
    print(
        PLAN_TEMPLATE.format(
            feature_name=feature_name,
            goal=goal,
            task_1_name=feature_name.lower().replace(" ", "-"),
            date=datetime.now().strftime("%Y-%m-%d"),
        )
    )


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python plan-generator.py <feature-name> <goal>")
        sys.exit(1)

    generate_plan(sys.argv[1], " ".join(sys.argv[2:]))
