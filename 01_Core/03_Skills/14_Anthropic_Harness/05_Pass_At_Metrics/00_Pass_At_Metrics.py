"""
Pass@k Metrics - Calculate pass@k and pass^k for agent evaluations.

Inspirado en: "Demystifying Evals for AI Agents" article (Jan 09, 2026)
"""

from typing import List, Optional, Dict, Any
from dataclasses import dataclass
import math


@dataclass
class PassAtKResult:
    """Resultado de cálculo pass@k."""

    k: int
    pass_at_k: float
    total_trials: int
    successes: int

    def __str__(self):
        return f"pass@{self.k}: {self.pass_at_k:.2%} ({self.successes}/{self.total_trials})"


def calculate_pass_at_k(results: List[bool], k: int) -> float:
    """
    Calcula pass@k: probabilidad de al menos 1 éxito en k intentos.

    pass@k = 1 - (1 - p)^k
    donde p = success rate

    Args:
        results: Lista de booleanos (True = success, False = fail)
        k: Número de intentos

    Returns:
        Probabilidad de al menos 1 éxito en k intentos
    """
    if not results:
        return 0.0

    if k <= 0:
        return 0.0

    n = len(results)
    successes = sum(1 for r in results if r)

    if successes == 0:
        return 0.0

    p = successes / n  # per-trial success rate

    # pass@k = 1 - (1 - p)^k
    return 1 - math.pow(1 - p, k)


def calculate_pass_all_k(results: List[bool], k: int) -> float:
    """
    Calcula pass^k: probabilidad de que TODOS k intentos succeedan.

    pass^k = p^k

    Args:
        results: Lista de booleanos (True = success, False = fail)
        k: Número de intentos

    Returns:
        Probabilidad de que todos k intentos sean exitosos
    """
    if not results:
        return 0.0

    if k <= 0:
        return 0.0

    n = len(results)
    successes = sum(1 for r in results if r)

    if successes == 0:
        return 0.0

    p = successes / n  # per-trial success rate

    # pass^k = p^k
    return math.pow(p, k)


def calculate_pass_at_k_from_raw(trials: List[Dict[str, Any]], k: int) -> float:
    """
    Calcula pass@k desde trials crudos (no solo booleanos).

    Args:
        trials: Lista de dicts con 'passed' key
        k: Número de intentos

    Returns:
        Probabilidad de al menos 1 éxito
    """
    results = [trial.get("passed", False) for trial in trials]
    return calculate_pass_at_k(results, k)


class EvaluationMetrics:
    """
    Clase para manejar métricas de evaluación de agentes.
    """

    def __init__(self, name: str):
        self.name = name
        self.results: List[bool] = []
        self.trials: List[Dict[str, Any]] = []

    def add_trial(self, passed: bool, metadata: Optional[Dict] = None):
        """Agrega un trial."""
        self.results.append(passed)
        self.trials.append({"passed": passed, "metadata": metadata or {}})

    def get_summary(self) -> Dict[str, Any]:
        """Obtiene resumen de métricas."""
        if not self.results:
            return {"total_trials": 0, "successes": 0, "pass_rate": 0.0}

        successes = sum(1 for r in self.results if r)
        total = len(self.results)
        p = successes / total

        return {
            "name": self.name,
            "total_trials": total,
            "successes": successes,
            "failures": total - successes,
            "pass_rate": p,
            "pass@1": calculate_pass_at_k(self.results, 1),
            "pass@3": calculate_pass_at_k(self.results, 3),
            "pass@5": calculate_pass_at_k(self.results, 5),
            "pass@10": calculate_pass_at_k(self.results, 10),
            "pass^1": calculate_pass_all_k(self.results, 1),
            "pass^3": calculate_pass_all_k(self.results, 3),
            "pass^5": calculate_pass_all_k(self.results, 5),
        }

    def print_report(self):
        """Imprime reporte de métricas."""
        summary = self.get_summary()

        print("=" * 60)
        print(f"Evaluation Report: {summary['name']}")
        print("=" * 60)
        print(f"Total Trials: {summary['total_trials']}")
        print(f"Successes: {summary['successes']}")
        print(f"Pass Rate: {summary['pass_rate']:.2%}")
        print()
        print("Pass@k Metrics:")
        print(f"  pass@1:  {summary['pass@1']:.2%}")
        print(f"  pass@3:  {summary['pass@3']:.2%}")
        print(f"  pass@5:  {summary['pass@5']:.2%}")
        print(f"  pass@10: {summary['pass@10']:.2%}")
        print()
        print("Pass^k Metrics (consistency):")
        print(f"  pass^1:  {summary['pass^1']:.2%}")
        print(f"  pass^3:  {summary['pass^3']:.2%}")
        print(f"  pass^5:  {summary['pass^5']:.2%}")
        print("=" * 60)


# ==================== EJEMPLO DE USO ====================

if __name__ == "__main__":
    # Simular resultados de evaluación
    # Easy task: 10/10 success
    easy = EvaluationMetrics("Easy Task")
    for _ in range(10):
        easy.add_trial(True)

    # Medium task: 7/10 success
    medium = EvaluationMetrics("Medium Task")
    results_medium = [True, False, True, True, False, True, True, False, True, True]
    for r in results_medium:
        medium.add_trial(r)

    # Hard task: 2/10 success
    hard = EvaluationMetrics("Hard Task")
    results_hard = [False, False, False, True, False, False, False, False, False, False]
    for r in results_hard:
        hard.add_trial(r)

    # Print reports
    easy.print_report()
    print()
    medium.print_report()
    print()
    hard.print_report()
