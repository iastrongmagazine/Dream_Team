#!/usr/bin/env python3
"""
Epic Generator

Generates Jira epic structure from feature description.
"""

import sys
from datetime import datetime


EPIC_TEMPLATE = """# [EPIC] {title}

**Figma:** {figma_url}

## Feature Overview

{overview}

## Requirements

### {area_1}
- Requirement 1
- Requirement 2

### {area_2}
- Requirement 1
- Requirement 2

## Technical Considerations

### Performance
- Large dataset handling
- Pagination

### Data Integration
- API endpoints
- Data sources

### UI Components
- Reusable components

## Implementation Checklist
- [ ] Task 1: {title} - API
- [ ] Task 2: {title} - UI
- [ ] Task 3: {title} - Tests

---

## Suggested Tasks

| # | Title | Component | Blocked By |
|---|-------|-----------|------------|
| 1 | [FEATURE] {title} API | API | - |
| 2 | [FEATURE] {title} UI | UI | Task 1 |
| 3 | [FEATURE] {title} Tests | QA | Task 2 |

Generated: {date}
"""


def generate_epic(title, overview="", area_1="API", area_2="UI"):
    """Generate epic structure."""
    print(
        EPIC_TEMPLATE.format(
            title=title,
            figma_url="[Figma link]",
            overview=overview or f"Feature to implement {title}",
            area_1=area_1,
            area_2=area_2,
            date=datetime.now().strftime("%Y-%m-%d"),
        )
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create-epic.py <feature-title>")
        sys.exit(1)

    title = " ".join(sys.argv[1:])
    generate_epic(title)
