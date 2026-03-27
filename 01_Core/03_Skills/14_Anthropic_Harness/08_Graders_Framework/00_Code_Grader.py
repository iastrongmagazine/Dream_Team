"""
Graders Framework - Code-based Grader

Inspirado en: "Demystifying Evals for AI Agents" article (Jan 09, 2026)
"""

from typing import Dict, Any, List, Optional, Callable
from dataclasses import dataclass, field
from enum import Enum
import re
import subprocess


class TestResult(Enum):
    PASS = "pass"
    FAIL = "fail"
    ERROR = "error"
    SKIP = "skip"


@dataclass
class GraderResult:
    """Resultado de evaluación de un grader."""

    passed: bool
    score: float  # 0.0 - 1.0
    details: Dict[str, Any] = field(default_factory=dict)
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


class CodeGrader:
    """
    Grader basado en código para verificaciones objetivas.
    """

    def __init__(self):
        self.checks: List[Callable] = []

    def add_check(
        self, name: str, check_func: Callable[[Any], bool], weight: float = 1.0
    ):
        """Agrega un check al grader."""
        self.checks.append({"name": name, "func": check_func, "weight": weight})

    def evaluate(self, task: Dict[str, Any]) -> GraderResult:
        """
        Evalúa una tarea usando checks de código.

        Args:
            task: Diccionario con 'input' y 'expected'

        Returns:
            GraderResult con la evaluación
        """
        passed_checks = 0
        total_weight = 0
        errors = []
        warnings = []

        for check in self.checks:
            try:
                result = check["func"](task)
                if result:
                    passed_checks += check["weight"]
                total_weight += check["weight"]
            except Exception as e:
                errors.append(f"{check['name']}: {str(e)}")

        score = passed_checks / total_weight if total_weight > 0 else 0.0
        passed = score >= 0.8  # 80% threshold

        return GraderResult(
            passed=passed,
            score=score,
            details={
                "passed_checks": passed_checks,
                "total_weight": total_weight,
                "checks_run": len(self.checks),
            },
            errors=errors,
            warnings=warnings,
        )


# Common check functions
def check_output_equals(output: str, expected: str) -> bool:
    """Check if output equals expected."""
    return output.strip() == expected.strip()


def check_output_contains(output: str, substring: str) -> bool:
    """Check if output contains substring."""
    return substring in output


def check_output_matches_regex(output: str, pattern: str) -> bool:
    """Check if output matches regex pattern."""
    return re.search(pattern, output) is not None


def check_status_code(status_code: int, expected: int) -> bool:
    """Check if HTTP status code matches."""
    return status_code == expected


def check_file_exists(filepath: str) -> bool:
    """Check if file exists."""
    import os

    return os.path.exists(filepath)


def check_file_contains(filepath: str, substring: str) -> bool:
    """Check if file contains substring."""
    try:
        with open(filepath, "r") as f:
            return substring in f.read()
    except:
        return False


# Example: Create a grader for a task
def create_basic_grader() -> CodeGrader:
    """Creates a basic code grader with common checks."""
    grader = CodeGrader()

    # Add common checks
    grader.add_check(
        "output_contains_result",
        lambda t: check_output_contains(t.get("output", ""), t.get("expected", "")),
        weight=1.0,
    )

    grader.add_check(
        "no_errors", lambda t: "error" not in t.get("output", "").lower(), weight=1.0
    )

    return grader


# Binary test helpers
class BinaryTest:
    """Helper para tests binarios (fail-to-pass, pass-to-pass)."""

    @staticmethod
    def fail_to_pass(before: Any, after: Any, test_func: Callable) -> bool:
        """Verifica que el test pase después de un fix."""
        # Before: should fail
        # After: should pass
        return test_func(after)

    @staticmethod
    def pass_to_pass(before: Any, after: Any, test_func: Callable) -> bool:
        """Verifica que el test siga pasando después de un cambio."""
        # Both should pass
        return test_func(before) and test_func(after)


# Static analysis helpers
class StaticAnalysis:
    """Helpers para static analysis."""

    @staticmethod
    def run_linter(filepath: str, linter: str = "ruff") -> Dict[str, Any]:
        """Run linter on file."""
        try:
            result = subprocess.run(
                [linter, filepath], capture_output=True, text=True, timeout=30
            )
            return {
                "passed": result.returncode == 0,
                "output": result.stdout + result.stderr,
            }
        except Exception as e:
            return {"passed": False, "error": str(e)}

    @staticmethod
    def run_type_check(filepath: str, checker: str = "mypy") -> Dict[str, Any]:
        """Run type checker on file."""
        try:
            result = subprocess.run(
                [checker, filepath], capture_output=True, text=True, timeout=60
            )
            return {
                "passed": result.returncode == 0,
                "output": result.stdout + result.stderr,
            }
        except Exception as e:
            return {"passed": False, "error": str(e)}


# ==================== EJEMPLO ====================

if __name__ == "__main__":
    # Crear grader
    grader = create_basic_grader()

    # Evaluar tarea
    task = {"output": "Hello, World!", "expected": "Hello"}

    result = grader.evaluate(task)
    print(f"Passed: {result.passed}")
    print(f"Score: {result.score}")
    print(f"Details: {result.details}")
