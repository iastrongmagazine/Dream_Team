---
name: edge-case-skill
description: > Triggers on: testing, QA, quality, validation.
  Edge case identification, documentation, and testing. Includes boundary analysis, error handling, and failure modes.
  Trigger: edge cases, boundary testing, error handling, failure modes, exceptional cases, fuzzing, negative testing.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# Edge Case Skill — Systematic Edge Case Discovery

## When to Use

- Identifying edge cases before implementation
- Testing boundary conditions
- Documenting error handling requirements
- Writing defensive code
- Fuzzing and negative testing
- Failure mode analysis

## Critical Patterns

### 1. Edge Case Categories

```
┌─────────────────────────────────────────────────────────────────┐
│                    EDGE CASE TAXONOMY                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │    BOUNDARY     │  │     EMPTY       │  │     INVALID     │  │
│  │  ────────────   │  │  ────────────   │  │  ────────────   │  │
│  │ • Min/Max values│  │ • Null/None     │  │ • Type errors   │  │
│  │ • First/Last    │  │ • Empty string  │  │ • Malformed     │  │
│  │ • Overflow      │  │ • Empty array   │  │ • Out of range  │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │    TEMPORAL     │  │     SYSTEM      │  │     DATA        │  │
│  │  ────────────   │  │  ────────────   │  │  ────────────   │  │
│  │ • Timezones    │  │ • Disk full     │  │ • Duplicate    │  │
│  │ • Leap year    │  │ • No network    │  │ • Race condition│  │
│  │ • DST change   │  │ • Memory limit  │  │ • Concurrent   │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Decision Table for Common Edge Cases

| Input Type | Boundary Min | Valid Range | Boundary Max | Invalid |
|------------|--------------|-------------|--------------|---------|
| String | "" | 1 char | 10,000 chars | >10,000 |
| Integer | MIN_INT | - | MAX_INT | Overflow |
| Float | 0.0 | >0.0 | 1.797e308 | Inf, NaN |
| Array | [] | 1 element | 1000 elements | >1000 |
| Date | 1970-01-01 | - | 2099-12-31 | Future >10y |

### 3. Edge Case Discovery Framework

```python
from dataclasses import dataclass
from typing import Any, Callable, TypeVar
import fuzzing

@dataclass
class EdgeCase:
    name: str
    description: str
    input_value: Any
    expected_behavior: str
    severity: str  # "critical", "high", "medium", "low"

class EdgeCaseAnalyzer:
    def analyze_function(self, func: Callable) -> list[EdgeCase]:
        cases = []
        
        # Introspection
        sig = inspect.signature(func)
        
        for param_name, param in sig.parameters.items():
            cases.extend(self._analyze_parameter(param_name, param))
        
        # Add common temporal edge cases
        cases.extend(self._temporal_edge_cases())
        
        # Add system edge cases
        cases.extend(self._system_edge_cases())
        
        return cases
    
    def _analyze_parameter(self, name: str, param) -> list[EdgeCase]:
        cases = []
        param_type = param.annotation
        
        if param_type == int:
            cases.extend([
                EdgeCase(f"{name}_zero", f"{name} = 0", 0, "handle gracefully", "medium"),
                EdgeCase(f"{name}_negative", f"{name} < 0", -1, "validate or reject", "high"),
                EdgeCase(f"{name}_max_int", f"{name} = MAX_INT", 2**31-1, "no overflow", "critical"),
            ])
        elif param_type == str:
            cases.extend([
                EdgeCase(f"{name}_empty", f"{name} = ''", "", "handle gracefully", "high"),
                EdgeCase(f"{name}_whitespace", f"{name} = '   '", "   ", "trim or reject", "medium"),
                EdgeCase(f"{name}_unicode", f"{name} = '日本語'", "日本語", "encoding safe", "high"),
                EdgeCase(f"{name}_sql_injection", f"{name} = \"'; DROP TABLE\"", "'; DROP TABLE", "sanitize", "critical"),
            ])
        
        return cases
```

## Code Examples

### Property-Based Testing (Fuzzing)

```python
from hypothesis import given, strategies as st, settings

@given(
    text=st.text(min_size=0, max_size=10000),
    max_length=st.integers(min_value=1, max_value=1000)
)
@settings(max_examples=1000)
def test_truncate_edge_cases(text: str, max_length: int):
    """Hypothesis finds unexpected edge cases."""
    result = truncate(text, max_length)
    
    # Properties
    assert len(result) <= max_length
    assert result.endswith("...") == (len(text) > max_length)
    assert isinstance(result, str)

@given(
    email=st.emails() | st.just("user@@domain.com") | st.just("@domain.com")
)
def test_email_validation(email: str):
    """Fuzz email validation with valid and invalid formats."""
    is_valid = validate_email(email)
    
    # Known invalid patterns should fail
    if "@@" in email or not "@" in email:
        assert not is_valid, f"Should reject: {email}"
```

### Defensive Programming

```python
def safe_divide(a: float, b: float) -> float:
    """
    Divide with comprehensive edge case handling.
    
    Edge cases:
    - Division by zero → return infinity or raise
    - Both zero → undefined behavior
    - Very small b → potential underflow
    - Very large a → potential overflow
    """
    # Guard against division by zero
    if b == 0:
        if a == 0:
            raise ValueError("0/0 is undefined")
        raise ZeroDivisionError("Division by zero")
    
    # Check for overflow/underflow
    try:
        result = a / b
        if not math.isfinite(result):
            raise OverflowError(f"Result not finite: {result}")
        return result
    except FloatingPointError:
        raise

# Example of input validation
def process_user_input(data: dict) -> User:
    """
    Process user input with full edge case handling.
    """
    # Validate required fields
    required = ["email", "name"]
    missing = [f for f in required if f not in data]
    if missing:
        raise ValidationError(f"Missing fields: {missing}")
    
    # Validate email format
    email = data["email"].strip().lower()
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        raise ValidationError(f"Invalid email: {email}")
    
    # Validate name
    name = data["name"].strip()
    if len(name) < 1:
        raise ValidationError("Name cannot be empty")
    if len(name) > 255:
        raise ValidationError("Name too long (max 255 chars)")
    
    # Sanitize inputs
    return User(
        email=sanitize(email),
        name=sanitize(name)
    )
```

### Error Handling Matrix

```python
ERROR_HANDLING_MATRIX = {
    # (Error Type, Context) -> Response
    ("NetworkError", "User facing"): "Retry with exponential backoff, then show error UI",
    ("NetworkError", "Background job"): "Queue for retry with dead letter on max retries",
    ("ValidationError", "User input"): "Return field-specific error messages",
    ("ValidationError", "Internal"): "Log and return generic error",
    ("AuthError", "Expired token"): "Redirect to login",
    ("AuthError", "Invalid token"): "Clear session, redirect to login",
    ("RateLimitError", "Any"): "Implement backoff, notify user",
    ("TimeoutError", "Read operation"): "Retry once, then timeout message",
    ("TimeoutError", "Write operation"): "Check state, retry with idempotency key",
}

def handle_error(error: Exception, context: str) -> Response:
    """Centralized error handling."""
    error_type = type(error).__name__
    response = ERROR_HANDLING_MATRIX.get(
        (error_type, context),
        ERROR_HANDLING_MATRIX.get((error_type, "Any"), "Internal error")
    )
    
    if "Retry" in response:
        return retry_with_backoff(error)
    elif "Redirect" in response:
        return redirect_to_login()
    elif "error message" in response:
        return show_error(response)
    else:
        return handle_internal_error(error)
```

## Commands

```bash
# Hypothesis fuzzing
pytest tests/ --hypothesis-show-statistics

# AFL++ fuzzing
afl-fuzz -i input/ -o output/ -- ./target_program

# Quick check property testing
python -m hypothesis write hpytest_examples

# Edge case documentation
python -m edgecase.generate --template=markdown

# Run with edge cases enabled
pytest tests/ --edge-cases --verbose
```

## Resources

- **Hypothesis**: https://hypothesis.readthedocs.io/
- **AFL++**: https://github.com/AFLplusplus/AFLplusplus
- **beartype**: https://github.com/beartype/beartype
- **pydantic**: https://docs.pydantic.dev/

## Esencia Original
> **Propósito:** 12_Edge_Case - propósito del skill
> **Flujo:** Pasos principales del flujo de trabajo

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Error común
  - **Por qué**: Explicación
  - **Solución**: Cómo evitar

## 📁 Progressive Disclosure

> Para información detallada:
- [references/guide.md](references/guide.md) — Guía completa

## 🛠️ Scripts

- [scripts/run.py](scripts/run.py) — Script principal

## 💾 State Persistence

Guardar en:
-  — Evaluaciones
-  — Documentación

