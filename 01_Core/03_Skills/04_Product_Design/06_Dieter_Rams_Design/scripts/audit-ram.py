#!/usr/bin/env python3
"""
Dieter Rams Audit Helper

Generates audit template for Dieter Rams principles.
"""

import sys
from datetime import datetime


AUDIT_TEMPLATE = """# Dieter Rams Audit

**Date:** {date}
**Design:** {design_name}

---

## 10 Principles Score

| Principle | Score | Notes |
|-----------|-------|-------|
| 1. Innovative | /100 | |
| 2. Useful | /100 | |
| 3. Aesthetic | /100 | |
| 4. Understandable | /100 | |
| 5. Unobtrusive | /100 | |
| 6. Honest | /100 | |
| 7. Long-lasting | /100 | |
| 8. Thorough | /100 | |
| 9. Environmentally friendly | /100 | |
| 10. Little design as possible | /100 | |

**Overall:** /100

---

## Red Flags

- [ ] Add red flags here

---

## 5 Steps to Simplify

1. Remove:
2. Reduce:
3. Clarify:
4. Unify:
5. Focus on:

---

## Verdict

[ ] Pass
[ ] Needs revision

---

*"Less, but better" - Dieter Rams*
"""


def generate_audit(design_name):
    """Generate audit template."""
    print(
        AUDIT_TEMPLATE.format(
            date=datetime.now().strftime("%Y-%m-%d"), design_name=design_name
        )
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python audit-ram.py <design-name>")
        sys.exit(1)

    generate_audit(" ".join(sys.argv[1:]))
