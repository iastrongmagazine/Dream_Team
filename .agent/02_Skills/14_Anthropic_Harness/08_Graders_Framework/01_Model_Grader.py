"""
Graders Framework - Model-based Grader (LLM-as-judge)

Inspirado en: "Demystifying Evals for AI Agents" article (Jan 09, 2026)
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field
from enum import Enum


class GradingMode(Enum):
    RUBRIC = "rubric"  # Scoring against rubric
    ASSERTION = "assertion"  # Natural language assertions
    PAIRWISE = "pairwise"  # Compare two outputs
    REFERENCE = "reference"  # Compare to reference solution


@dataclass
class RubricItem:
    """Un ítem de la rúbrica de evaluación."""

    name: str
    description: str
    max_score: float
    criteria: List[str]


class ModelGrader:
    """
    Grader basado en LLM para evaluaciones subjetivas.
    """

    def __init__(self, model=None):
        """
        Args:
            model: LLM a usar para grading (si es None, usa mock)
        """
        self.model = model

    def evaluate_with_rubric(
        self, output: str, rubric: List[RubricItem], context: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Evalúa output usando una rúbrica.

        Args:
            output: Output a evaluar
            rubric: Lista de RubricItems
            context: Contexto adicional

        Returns:
            Dict con scores por criterion y score total
        """
        if self.model is None:
            # Mock evaluation for testing
            return self._mock_rubric_evaluation(output, rubric)

        # Build prompt con la rúbrica
        rubric_text = "\n".join(
            [
                f"- {item.name} ({item.max_score} pts): {item.description}"
                for item in rubric
            ]
        )

        prompt = f"""Evaluate the following output against this rubric:

Rubric:
{rubric_text}

Output to evaluate:
{output}

{context or ""}

Provide scores for each criterion and a brief justification."""

        # Call LLM
        response = self.model.complete(prompt)

        # Parse response (simplified)
        return self._parse_llm_response(response, rubric)

    def evaluate_with_assertions(
        self, output: str, assertions: List[str], context: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Evalúa output usando natural language assertions.

        Args:
            output: Output a evaluar
            assertions: Lista de assertions en lenguaje natural
            context: Contexto adicional

        Returns:
            Dict con resultados de cada assertion
        """
        if self.model is None:
            return self._mock_assertion_evaluation(output, assertions)

        assertions_text = "\n".join([f"- {a}" for a in assertions])

        prompt = f"""Evaluate each assertion against the output.

Assertions:
{assertions_text}

Output:
{output}

For each assertion, respond with:
- PASS: if the assertion is true
- FAIL: if the assertion is false
- UNCERTAIN: if you cannot determine

Provide a brief justification for each."""

        response = self.model.complete(prompt)

        return self._parse_assertions_response(response, assertions)

    def pairwise_compare(
        self, output_a: str, output_b: str, criteria: List[str]
    ) -> Dict[str, Any]:
        """
        Compara dos outputs usando criteria dados.

        Returns:
            Dict con winner y scores por criterion
        """
        if self.model is None:
            return self._mock_pairwise_comparison(criteria)

        criteria_text = "\n".join([f"- {c}" for c in criteria])

        prompt = f"""Compare these two outputs based on the criteria.

Criteria:
{criteria_text}

Output A:
{output_a}

Output B:
{output_b}

Determine which output is better for each criterion, and overall.
Explain your reasoning."""

        response = self.model.complete(prompt)

        return self._parse_pairwise_response(response, criteria)

    def _mock_rubric_evaluation(
        self, output: str, rubric: List[RubricItem]
    ) -> Dict[str, Any]:
        """Mock evaluation for testing."""
        # Simple heuristic: length and basic checks
        results = {}
        total_score = 0.0

        for item in rubric:
            # Mock: dar score basado en si output tiene contenido
            has_content = len(output.strip()) > 0
            score = item.max_score * (0.8 if has_content else 0.3)

            results[item.name] = {
                "score": score,
                "max_score": item.max_score,
                "justification": "Mock evaluation",
            }
            total_score += score

        max_total = sum(item.max_score for item in rubric)

        return {
            "scores": results,
            "total_score": total_score,
            "max_total": max_total,
            "percentage": (total_score / max_total * 100) if max_total > 0 else 0,
        }

    def _mock_assertion_evaluation(
        self, output: str, assertions: List[str]
    ) -> Dict[str, Any]:
        """Mock assertion evaluation."""
        results = {}

        for assertion in assertions:
            # Simple keyword check para mock
            lower_output = output.lower()
            # Mock: todas pasan si hay contenido
            passed = len(output.strip()) > 0

            results[assertion] = {
                "result": "PASS" if passed else "FAIL",
                "justification": "Mock evaluation",
            }

        total = len(assertions)
        passed_count = sum(1 for r in results.values() if r["result"] == "PASS")

        return {
            "assertions": results,
            "passed": passed_count,
            "total": total,
            "percentage": (passed_count / total * 100) if total > 0 else 0,
        }

    def _mock_pairwise_comparison(self, criteria: List[str]) -> Dict[str, Any]:
        """Mock pairwise comparison."""
        return {
            "winner": "A",  # Default
            "scores": {c: {"A": 0.6, "B": 0.4} for c in criteria},
            "explanation": "Mock comparison",
        }

    def _parse_llm_response(
        self, response: str, rubric: List[RubricItem]
    ) -> Dict[str, Any]:
        """Parse LLM response to rubric format."""
        # Simplified: would need proper parsing in production
        return self._mock_rubric_evaluation(response, rubric)

    def _parse_assertions_response(
        self, response: str, assertions: List[str]
    ) -> Dict[str, Any]:
        """Parse LLM response to assertions format."""
        return self._mock_assertion_evaluation(response, assertions)

    def _parse_pairwise_response(
        self, response: str, criteria: List[str]
    ) -> Dict[str, Any]:
        """Parse LLM response to pairwise format."""
        return self._mock_pairwise_comparison(criteria)


# ==================== EJEMPLO ====================

if __name__ == "__main__":
    grader = ModelGrader()  # Sin modelo real

    # Ejemplo con rúbrica
    rubric = [
        RubricItem(
            name="Code Quality",
            description="Code is clean and well-organized",
            max_score=10.0,
        ),
        RubricItem(
            name="Functionality",
            description="Code performs the required function",
            max_score=10.0,
        ),
        RubricItem(
            name="Readability", description="Code is easy to understand", max_score=5.0
        ),
    ]

    output = "def hello():\n    print('Hello, World!')"

    result = grader.evaluate_with_rubric(output, rubric)
    print("Rubric Evaluation:")
    print(f"  Total: {result['total_score']}/{result['max_total']}")
    print(f"  Percentage: {result['percentage']:.1f}%")

    # Ejemplo con assertions
    assertions = [
        "Code defines a function",
        "Code prints Hello World",
        "Code has no syntax errors",
    ]

    result2 = grader.evaluate_with_assertions(output, assertions)
    print("\nAssertion Evaluation:")
    print(f"  Passed: {result2['passed']}/{result2['total']}")
    print(f"  Percentage: {result2['percentage']:.1f}%")
