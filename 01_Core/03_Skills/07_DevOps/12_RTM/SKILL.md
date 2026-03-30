---
name: rtm-skill
description: > Triggers on: devops, deployment, infrastructure.
  Requirements Traceability Matrix management. Links requirements to tests, code, and documentation.
  Trigger: RTM, traceability matrix, requirements tracking, test coverage of requirements, compliance.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# RTM Skill — Requirements Traceability Matrix

## Esencia Original
> **Propósito:** Requirements Traceability Matrix — vincular requirements a tests y código
> **Flujo:** Mapear requirements → Link a tests → Validar cobertura → Generar reporte


## When to Use

- Creating traceability between requirements and tests
- Auditing code for requirement coverage
- Generating compliance documentation
- Tracking test coverage per requirement
- Managing requirement changes and impact

## Critical Patterns

### 1. RTM Structure

```
┌─────────────────────────────────────────────────────────────────┐
│                 REQUIREMENTS TRACEABILITY                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│    ┌──────────────┐                                            │
│    │  REQUIREMENT │ Req-001: User authentication                │
│    └──────┬───────┘                                            │
│           │                                                     │
│    ┌──────┴───────┐                                            │
│    │    DESIGN     │ Design-001: OAuth 2.0 implementation     │
│    └──────┬───────┘                                            │
│           │                                                     │
│    ┌──────┴───────┐                                            │
│    │     CODE     │ auth/oauth2.py, auth/jwt.py                │
│    └──────┬───────┘                                            │
│           │                                                     │
│    ┌──────┴───────┐                                            │
│    │     TEST     │ test_auth_login.py, test_auth_jwt.py      │
│    └──────┬───────┘                                            │
│           │                                                     │
│    ┌──────┴───────┐                                            │
│    │   DOCS      │ docs/authentication.md, API spec            │
│    └──────────────┘                                            │
│                                                                 │
│    BI-DIRECTIONAL TRACEABILITY: Each artifact links forward     │
│    and backward through the development lifecycle               │
└─────────────────────────────────────────────────────────────────┘
```

### 2. RTM Matrix Template

| Requirement ID | Description | Priority | Test Cases | Code Coverage | Status |
|----------------|-------------|----------|------------|---------------|--------|
| REQ-001 | User authentication via OAuth2 | P0 | TC-001, TC-002, TC-003 | 95% | ✅ Done |
| REQ-002 | Session management with JWT | P0 | TC-004, TC-005 | 100% | ✅ Done |
| REQ-003 | Password reset flow | P1 | TC-006, TC-007 | 80% | 🔄 WIP |
| REQ-004 | MFA support | P2 | TC-008 | 0% | 📋 Planned |

### 3. RTM Data Model

```python
from dataclasses import dataclass, field
from typing import Optional
from enum import Enum
from datetime import datetime

class RequirementStatus(Enum):
    DRAFT = "draft"
    APPROVED = "approved"
    IMPLEMENTED = "implemented"
    VERIFIED = "verified"
    DEPRECATED = "deprecated"

class TraceabilityType(Enum):
    PARENT = "parent"           # Parent requirement
    DESIGN = "design"           # Design document
    CODE = "code"              # Implementation files
    TEST = "test"              # Test cases
    DOCUMENTATION = "docs"     # Documentation

@dataclass
class Requirement:
    id: str                    # e.g., "REQ-001"
    title: str
    description: str
    priority: str              # P0, P1, P2, P3
    status: RequirementStatus

    # Traceability links
    parent_id: Optional[str] = None
    design_refs: list[str] = field(default_factory=list)
    code_refs: list[str] = field(default_factory=list)
    test_refs: list[str] = field(default_factory=list)
    doc_refs: list[str] = field(default_factory=list)

    # Metadata
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    owner: str = ""
    version: str = "1.0"

    def get_traceability_links(self) -> dict[TraceabilityType, list[str]]:
        return {
            TraceabilityType.PARENT: [self.parent_id] if self.parent_id else [],
            TraceabilityType.DESIGN: self.design_refs,
            TraceabilityType.CODE: self.code_refs,
            TraceabilityType.TEST: self.test_refs,
            TraceabilityType.DOCUMENTATION: self.doc_refs,
        }

    def get_coverage_percentage(self) -> float:
        """Calculate test coverage for this requirement."""
        if not self.code_refs:
            return 0.0

        # Calculate based on test_refs / code_refs ratio
        return min(len(self.test_refs) / max(len(self.code_refs), 1) * 100, 100.0)
```

## Code Examples

### RTM Generator

```python
import re
from pathlib import Path
from dataclasses import dataclass

@dataclass
class TraceabilityReport:
    requirements: list[Requirement]
    uncovered_requirements: list[Requirement]
    low_coverage_requirements: list[Requirement]
    total_coverage: float

class RTMGenerator:
    def __init__(self, project_root: Path):
        self.project_root = project_root

    def scan_project(self) -> TraceabilityReport:
        """Scan project and generate RTM."""
        requirements = self._find_requirements()
        test_files = self._find_test_files()
        code_files = self._find_code_files()

        # Link requirements to tests
        for req in requirements:
            req.test_refs = self._find_tests_for_requirement(req)
            req.code_refs = self._find_code_for_requirement(req)

        # Generate report
        uncovered = [r for r in requirements if not r.test_refs]
        low_coverage = [r for r in requirements if r.get_coverage_percentage() < 80]

        total_coverage = sum(
            r.get_coverage_percentage() for r in requirements
        ) / len(requirements) if requirements else 0

        return TraceabilityReport(
            requirements=requirements,
            uncovered_requirements=uncovered,
            low_coverage_requirements=low_coverage,
            total_coverage=total_coverage
        )

    def _find_tests_for_requirement(self, req: Requirement) -> list[str]:
        """Find test files that cover this requirement."""
        # Look for test files matching requirement ID
        pattern = f"**/test**{req.id}*.py"
        return [str(p) for p in self.project_root.glob(pattern)]

    def generate_markdown(self, report: TraceabilityReport) -> str:
        """Generate Markdown RTM report."""
        lines = [
            "# Requirements Traceability Matrix",
            "",
            f"**Total Requirements:** {len(report.requirements)}",
            f"**Total Coverage:** {report.total_coverage:.1f}%",
            f"**Uncovered:** {len(report.uncovered_requirements)}",
            "",
            "## Coverage by Requirement",
            "",
            "| ID | Description | Priority | Test Coverage | Status |",
            "|----|-------------|----------|---------------|--------|",
        ]

        for req in sorted(report.requirements, key=lambda r: r.priority):
            coverage = req.get_coverage_percentage()
            status_icon = {
                "verified": "✅",
                "implemented": "🔄",
                "approved": "📋",
                "draft": "📝",
            }.get(req.status.value, "❓")

            lines.append(
                f"| {req.id} | {req.title} | {req.priority} | "
                f"{coverage:.0f}% | {status_icon} |"
            )

        return "\n".join(lines)
```

### Requirement Testing Hook

```python
import pytest
from typing import TypeVar, Callable

T = TypeVar('T')

def traceable(func: Callable[T]) -> Callable[T]:
    """
    Decorator that automatically links tests to requirements.

    Usage:
        @traceable
        def test_req_001_user_login():
            '''Requirement: REQ-001 User authentication'''
            ...

    This will:
    1. Extract requirement ID from docstring
    2. Record test execution against requirement
    3. Update RTM with pass/fail status
    """
    import re

    def wrapper(*args, **kwargs):
        # Extract requirement ID from docstring
        req_match = re.search(r'Requirement:\s*(REQ-\d+)', func.__doc__ or "")
        req_id = req_match.group(1) if req_match else None

        # Track execution
        start = datetime.now()
        try:
            result = func(*args, **kwargs)
            status = "PASS"
            error = None
        except Exception as e:
            status = "FAIL"
            error = str(e)
            raise
        finally:
            if req_id:
                RTMTracker.record_execution(
                    requirement_id=req_id,
                    test_name=func.__name__,
                    status=status,
                    error=error,
                    duration_ms=(datetime.now() - start).total_seconds() * 1000
                )

        return result

    return wrapper

# Usage
RTMTracker = RTMExecutionTracker()

@traceable
def test_req_001_user_authentication():
    """Requirement: REQ-001 User authentication via OAuth2"""
    # Test implementation
    ...
```

### CI/CD RTM Integration

```yaml
# .github/workflows/rtm.yml
name: Requirements Traceability

on:
  push:
    branches: [main]
  pull_request:
    types: [opened, synchronize]

jobs:
  rtm-coverage:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Generate RTM Report
        run: |
          python -m rtm.generator \
            --format=markdown \
            --output=RTM_REPORT.md \
            --fail-under=80

      - name: Upload RTM Report
        uses: actions/upload-artifact@v4
        with:
          name: rtm-report
          path: RTM_REPORT.md

      - name: Comment on PR
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: '## Requirements Coverage\n' +
                    fs.readFileSync("RTM_REPORT.md", "utf8")
            })
```

## Commands

```bash
# Generate RTM from code
python -m rtm generate --project=. --output=RTM.md

# Update RTM with test results
python -m rtm update --test-results=results.json

# Check coverage threshold
python -m rtm check --fail-under=80

# Export to CSV
python -m rtm export --format=csv --output=rtm.csv

# Link requirement to test
python -m rtm link REQ-001 test/test_auth.py

# Generate compliance report
python -m rtm compliance --standard=ISO26262 --output=compliance.pdf
```

## Resources

- **RTM Templates**: https://requirements.com/requirements-template/
- **ISO 26262 RTM**: Automotive safety standard
- **DO-178C RTM**: Aviation software


## ⚠️ Gotchas

- **[ERROR]**: Error común
  - **Solución**: Cómo evitar

## 💾 State Persistence
Guardar en:
- `04_Operations/` — Estado activo
