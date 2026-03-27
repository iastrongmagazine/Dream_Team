#!/usr/bin/env python3
"""
Double Code Review Runner

Runs structured 6-hat review process.
"""

import sys
from datetime import datetime


REVIEW_TEMPLATE = """# Double Code Review

**Date:** {date}
**Target:** {target}

---

## Phase 1: Planning Status

- [ ] Objectives clear and measurable
- [ ] Scope defined
- [ ] Dependencies identified
- [ ] Success criteria explicit
- [ ] Execution order clear

---

## Phase 2: 6 Hats Review

### 🔵 Information Hat
- What data do we have?
- What information is missing?

### 🔴 Emotions Hat
- How does the team feel?
- Any resistance or concerns?

### 🟡 Benefits Hat
- What do we gain if it works?
- Quick wins?

### 🟢 Risks Hat
- What could go wrong?
- Worst case scenarios?

### 🟣 Meta Hat
- Are we doing the right thing?
- Better approaches?

### ⚪ Process Hat
- Does the order make sense?
- Missing steps?

---

## Phase 3: Verification

- [ ] All tasks completed
- [ ] Quality meets standards
- [ ] Documentation updated

---

## Verdict: [PASS / CONDITIONAL / FAIL]
"""


def run_review(target):
    """Generate review template."""
    print(
        REVIEW_TEMPLATE.format(
            date=datetime.now().strftime("%Y-%m-%d %H:%M"), target=target
        )
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run-review.py <target>")
        sys.exit(1)

    run_review(" ".join(sys.argv[1:]))
