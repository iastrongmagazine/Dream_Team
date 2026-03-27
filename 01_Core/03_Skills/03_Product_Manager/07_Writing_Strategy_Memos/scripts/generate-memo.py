#!/usr/bin/env python3
"""
Strategy Memo Generator

Generates FocusFlow strategy memo skeleton.
"""

import sys
from datetime import datetime


MEMO_TEMPLATE = """# Strategy Memo: {title}

> Generated: {date}
> Framework: FocusFlow

---

## Problem (2-3 sentences max)

{problem_placeholder}

**Customer quote:**
> "{customer_quote}"

---

## Vision (1 sentence)

{vision_placeholder}

---

## Principles (3 max)

| Principle | Trade-off |
|-----------|-----------|
| {principle_1} | {tradeoff_1} |
| {principle_2} | {tradeoff_2} |
| {principle_3} | {tradeoff_3} |

---

## Goals

### Output (1 measurable result)
- {output_placeholder}

### Inputs (2-4 levers)
- {input_1}
- {input_2}
- {input_3}

---

## Solution (3-4 initiatives)

1. **{initiative_1}**
   - {detail_1}

2. **{initiative_2}**
   - {detail_2}

3. **{initiative_3}**
   - {detail_3}

---

## Non-Priorities (2-4 points)

- ❌ {non_priority_1}
- ❌ {non_priority_2}
- ❌ {non_priority_3}

---

## Checklist

- [ ] Problem has customer quotes
- [ ] Vision is memorable
- [ ] Principles imply tradeoffs
- [ ] Goals are measurable
- [ ] Solution has 3-4 initiatives
- [ ] Non-Priorities are explicit

---

*FocusFlow Framework | PersonalOS*
"""


def generate_memo(title):
    """Generate memo skeleton."""
    print(
        MEMO_TEMPLATE.format(
            title=title,
            date=datetime.now().strftime("%Y-%m-%d"),
            problem_placeholder="[Describe the core customer pain point in 2-3 sentences]",
            customer_quote="[Add a real customer quote here]",
            vision_placeholder="[One memorable, aspirational sentence]",
            principle_1="[Principle 1]",
            tradeoff_1="[What you sacrifice]",
            principle_2="[Principle 2]",
            tradeoff_2="[What you sacrifice]",
            principle_3="[Principle 3]",
            tradeoff_3="[What you sacrifice]",
            output_placeholder="[One measurable result]",
            input_1="[Lever 1]",
            input_2="[Lever 2]",
            input_3="[Lever 3]",
            initiative_1="[Initiative name]",
            detail_1="[Key details]",
            initiative_2="[Initiative name]",
            detail_2="[Key details]",
            initiative_3="[Initiative name]",
            detail_3="[Key details]",
            non_priority_1="[What you're NOT doing]",
            non_priority_2="[What you're NOT doing]",
            non_priority_3="[What you're NOT doing]",
        )
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate-memo.py <title>")
        sys.exit(1)

    generate_memo(" ".join(sys.argv[1:]))
