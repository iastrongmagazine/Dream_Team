---
name: test-coverage-skill
description: >
  Test coverage analysis and improvement. Includes coverage metrics, gap analysis, and coverage optimization.
  Trigger: test coverage, coverage analysis, coverage gaps, code coverage, testing strategy, coverage optimization.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# Test Coverage Skill — Coverage Analysis & Improvement

## When to Use

- Analyzing test coverage reports
- Identifying coverage gaps
- Improving test coverage
- Setting coverage thresholds
- Writing coverage-focused tests

## Critical Patterns

### 1. Coverage Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                    COVERAGE PYRAMID                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│                         LINE 90%                                 │
│                        ╱╲╱╲╱╲                                  │
│                       LINE 80%                                   │
│                      ╱    ╲╱    ╲                               │
│                     BRANCH 70%                                  │
│                    ╱   ╲╱╱   ╲                                  │
│                   FUNCTION 80%                                  │
│                  ╱      ╲╱      ╲                               │
│                 STATEMENT 85%                                   │
│                ╱════════════════════╲                          │
│                                                                 │
│  Remember: 100% coverage ≠ 100% tested quality!                │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Coverage Metrics

| Metric | Definition | Target | Tool |
|--------|------------|--------|------|
| **Line Coverage** | Executed lines / total lines | 80%+ | Coverage.py |
| **Branch Coverage** | Executed branches / total branches | 70%+ | Coverage.py |
| **Function Coverage** | Functions called / total functions | 100% | Coverage.py |
| **Statement Coverage** | Statements executed / total statements | 85%+ | Istanbul |

### 3. Coverage Ignorance Patterns

```python
# Never test these - ignore in coverage reports
if __debug__:  # pragma: no cover
    # Debug only code
    
if TYPE_CHECKING:  # pragma: no cover
    # Type hints only

# Runtime platform checks - mark untestable branches
if sys.platform == "win32":  # pragma: no cover
    windows_only()

# Version-specific code
if sys.version_info >= (3, 11):  # pragma: no cover
    python_311_feature()
```

## Code Examples

### Coverage Analysis Script

```python
import coverage
from pathlib import Path
from dataclasses import dataclass

@dataclass
class CoverageAnalysis:
    total_statements: int
    covered_statements: int
    missed_statements: list[str]
    coverage_percent: float

def analyze_coverage(coverage_file: str) -> CoverageAnalysis:
    cov = coverage.Coverage()
    cov.load(coverage_file)
    
    analysis = cov.analysis2()
    covered = set(analysis[1])
    missed = set(analysis[2])
    
    total = covered | missed
    coverage_pct = len(covered) / len(total) * 100 if total else 0
    
    return CoverageAnalysis(
        total_statements=len(total),
        covered_statements=len(covered),
        missed_statements=[str(Path(f)) for f in missed],
        coverage_percent=coverage_pct
    )

def find_coverage_gaps(
    analysis: CoverageAnalysis,
    source_dir: str
) -> dict[str, list[str]]:
    """Identify files and functions with low coverage."""
    gaps = {}
    
    for file_path in analysis.missed_statements:
        rel_path = Path(file_path).relative_to(source_dir)
        if rel_path not in gaps:
            gaps[str(rel_path)] = []
        gaps[str(rel_path)].append(file_path)
    
    return gaps
```

### Coverage-Optimized Testing

```python
import pytest
from hypothesis import given, strategies as st

# Property-based testing for better coverage
@given(
    user_input=st.text(min_size=1, max_size=1000)
)
def test_process_user_input_coverage(user_input: str):
    """Tests many code paths through property-based inputs."""
    result = process_input(user_input)
    assert isinstance(result, (str, int, list))

# Parametrized testing for branch coverage
@pytest.mark.parametrize("edge_value,expected_type", [
    ("", str),           # Empty string
    ("a" * 10000, str), # Very long string
    ("\x00\x01", bytes), # Binary data
    ("null", type(None)),# Null-like string
])
def test_edge_cases_coverage(edge_value, expected_type):
    """Parametrized tests cover all edge branches."""
    result = process_input(edge_value)
    assert isinstance(result, expected_type)
```

### Coverage Reports

```bash
# Generate HTML coverage report
coverage html -d htmlcov

# Generate XML for CI/CD
coverage xml -o coverage.xml

# Minimum threshold enforcement
coverage report --fail-under=80

# Combine coverage from multiple runs
coverage combine

# Show only files with coverage below threshold
coverage report --skip-covered --fail-under=70
```

## Commands

```bash
# Run with coverage
pytest tests/ --cov=src --cov-report=html --cov-report=term

# Minimum coverage threshold
pytest tests/ --cov=src --cov-fail-under=80

# Coverage with branch analysis
coverage run -m pytest tests/ --branch
coverage report --show-missing

# Generate annotated HTML
coverage html
open htmlcov/index.html

# CI/CD integration
coverage report --format=markdown > coverage_summary.md
```

## Resources

- **Coverage.py**: https://coverage.readthedocs.io/
- **pytest-cov**: https://pytest-cov.readthedocs.io/
- **Istanbul**: https://istanbul.js.org/
- **Codecov**: https://docs.codecov.io/
