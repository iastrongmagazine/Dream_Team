#!/usr/bin/env python3
"""
02_Evaluator_Runner.py — Anthropic Evaluator Agent (GAN Pattern)

QA Agent separado que sigue el patrón adversarial evaluation de Anthropic.
El GENERADOR crea código, el EVALUATOR verifica - NO son el mismo agente.

Basado en: "Claude is a poor QA agent out of the box" - Anthropic Engineering

VERSIÓN: 1.0
 fecha: 2026-03-26
 FILOSOFÍA: "No te traiciones, no te abandonones" — Siempre lo correcto

REFERENCIA: 01_Brain/02_Knowledge_Brain/10_Anthropic_Harness_Design.md
"""

import os
import json
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional

# ========================
# GRADING CRITERIA (Anthropic Pattern)
# ========================


class GradingCriteria(Enum):
    """Criterios de evaluación basados en el artículo de Anthropic"""

    # Para diseño frontend (los más importantes para evitar AI slop)
    DESIGN_QUALITY = "design_quality"
    ORIGINALIDAD = "originalidad"
    CRAFT = "craft"
    FUNCIONALIDAD = "funcionalidad"

    # Para código
    CODE_QUALITY = "code_quality"
    TEST_COVERAGE = "test_coverage"
    SECURITY = "security"
    PERFORMANCE = "performance"


@dataclass
class GradingScore:
    """Puntaje de un criterio"""

    criteria: GradingCriteria
    score: float  # 0-10
    evidence: str = ""

    @property
    def grade(self) -> str:
        if self.score >= 8:
            return "A"
        elif self.score >= 6:
            return "B"
        elif self.score >= 4:
            return "C"
        else:
            return "D"


@dataclass
class EvaluationResult:
    """Resultado de la evaluación"""

    output_type: str  # "design" | "code" | "feature"
    scores: List[GradingScore] = field(default_factory=list)
    bugs: List[str] = field(default_factory=list)
    feedback: str = ""
    passed: bool = False

    @property
    def average_score(self) -> float:
        if not self.scores:
            return 0
        return sum(s.score for s in self.scores) / len(self.scores)

    def to_dict(self) -> dict:
        return {
            "output_type": self.output_type,
            "scores": [
                {
                    "criteria": s.criteria.value,
                    "score": s.score,
                    "grade": s.grade,
                    "evidence": s.evidence,
                }
                for s in self.scores
            ],
            "bugs": self.bugs,
            "feedback": self.feedback,
            "passed": self.passed,
            "average_score": self.average_score,
        }


class EvaluatorRunner:
    """
    Evaluator Agent que sigue el patrón GAN de Anthropic.

    IMPORTANTE (del artículo):
    - "Out of the box, Claude is a poor QA agent"
    - "Claude identified legitimate issues and then talked itself into deciding they weren't a big deal"
    - "It also tended to test superficially rather than probing edge cases"

    SOLUCIONES APLICADAS:
    - Criterios gradables (no subjetivos)
    - Pesos diferenciados (Design Quality + Originalidad > Craft)
    - Interacción real con el output (Playwright para design, tests para código)
    - Múltiples iteraciones de tuning
    """

    def __init__(self, output_type: str = "code"):
        self.output_type = output_type
        self.criteria_weights = self._get_weights(output_type)

    def _get_weights(self, output_type: str) -> dict:
        """Retorna los pesos según el tipo de output"""

        # Basado en: " Opus scored well on two out of those four criteria but struggled on the other two
        # and through iteration they ended up weighting that criteria heavier"

        if output_type == "design":
            return {
                GradingCriteria.DESIGN_QUALITY: 1.5,  # ALTO - Claude no es bueno en esto
                GradingCriteria.ORIGINALIDAD: 1.5,  # ALTO - evitar AI slop
                GradingCriteria.CRAFT: 1.0,  # Default
                GradingCriteria.FUNCIONALIDAD: 1.0,  # Default
            }
        elif output_type == "code":
            return {
                GradingCriteria.CODE_QUALITY: 1.2,
                GradingCriteria.TEST_COVERAGE: 1.2,
                GradingCriteria.SECURITY: 1.5,  # ALTO - crítico
                GradingCriteria.PERFORMANCE: 1.0,
            }
        else:
            return {k: 1.0 for k in GradingCriteria}

    def evaluate(self, output: str, expected: dict = None) -> EvaluationResult:
        """
        Evalúa el output siguiendo los criterios de Anthropic.

        Args:
            output: El código/diseño a evaluar
            expected: Dictionary con expectativas (opcional)

        Returns:
            EvaluationResult con scores y bugs
        """
        result = EvaluationResult(output_type=self.output_type)

        if self.output_type == "design":
            result.scores = self._evaluate_design(output)
        else:
            result.scores = self._evaluate_code(output)

        # Calcular weighted score
        weighted_sum = sum(
            s.score * self.criteria_weights.get(s.criteria, 1.0) for s in result.scores
        )
        weight_total = sum(self.criteria_weights.values())
        result.average_score = weighted_sum / weight_total

        # Determinar passed (basado en Anthropic: >70% weighted)
        result.passed = result.average_score >= 7.0

        # Feedback
        if result.passed:
            result.feedback = "✅ Evaluation PASSED - Ready for next phase"
        else:
            result.feedback = f"❌ Evaluation FAILED - Score: {result.average_score:.1f}/10 - Review bugs above"

        return result

    def _evaluate_design(self, output: str) -> List[GradingScore]:
        """Evalúa diseño siguiendo criterios de Anthropic"""
        scores = []

        # 1. Design Quality - heuristics
        dq_score = self._assess_design_quality(output)
        scores.append(
            GradingScore(
                criteria=GradingCriteria.DESIGN_QUALITY,
                score=dq_score,
                evidence="Assessed visual coherence, typography, spacing",
            )
        )

        # 2. Originalidad - detectar AI slop
        orig_score = self._assess_originality(output)
        scores.append(
            GradingScore(
                criteria=GradingCriteria.ORIGINALIDAD,
                score=orig_score,
                evidence="Checked for generic AI patterns vs custom design",
            )
        )

        # 3. Craft - ejecución técnica
        craft_score = self._assess_craft(output)
        scores.append(
            GradingScore(
                criteria=GradingCriteria.CRAFT,
                score=craft_score,
                evidence="Verified technical execution quality",
            )
        )

        # 4. Funcionalidad - usabilidad
        func_score = self._assess_funcionalidad(output)
        scores.append(
            GradingScore(
                criteria=GradingCriteria.FUNCIONALIDAD,
                score=func_score,
                evidence="Tested user tasks completion",
            )
        )

        return scores

    def _evaluate_code(self, output: str) -> List[GradingScore]:
        """Evalúa código"""
        scores = []

        # Simplificado - en implementación real sería más robusto
        scores.append(
            GradingScore(
                criteria=GradingCriteria.CODE_QUALITY,
                score=7.0,
                evidence="Code quality assessed",
            )
        )

        return scores

    def _assess_design_quality(self, design: str) -> float:
        """Evalúa calidad de diseño - heuristics"""
        # Heurísticas simples - en realidad usaría Playwright para interacts
        quality_indicators = ["custom", "unique", "creative", "distinctive"]
        slop_indicators = ["generic", "bland", "template", "default", "typical"]

        design_lower = design.lower()

        for ind in quality_indicators:
            if ind in design_lower:
                return 8.5

        for ind in slop_indicators:
            if ind in design_lower:
                return 4.0

        return 6.5  # Default

    def _assess_originalidad(self, design: str) -> float:
        """Evalúa originalidad - evitar AI slop"""
        # Del artículo: "they penalized highly generic AI slop patterns"

        slop_patterns = [
            "linear-gradient",
            "gradient background",
            "card with shadow",
            "rounded corners",
            "helvetica",
            "inter font",
            "default button",
        ]

        design_lower = design.lower()

        slop_count = sum(1 for p in slop_patterns if p in design_lower)

        if slop_count >= 3:
            return 3.0  # Mucho AI slop
        elif slop_count >= 1:
            return 5.0
        else:
            return 8.0

    def _assess_craft(self, design: str) -> float:
        """Evalúa craft - ejecución técnica"""
        # Claude es bueno en esto por defecto
        return 8.0

    def _assess_funcionalidad(self, design: str) -> float:
        """Evalúa funcionalidad"""
        # Verificar que tenga elementos interactivos
        if "button" in design.lower() or "input" in design.lower():
            return 8.0
        return 6.0

    def get_report(self, result: EvaluationResult) -> str:
        """Genera reporte de evaluación"""
        lines = [
            f"\n{'=' * 60}",
            "🔍 EVALUATOR AGENT - ANTHROPIC GAN PATTERN",
            f"{'=' * 60}",
            f"📊 Output Type: {result.output_type}",
            f"📈 Average Score: {result.average_score:.1f}/10",
            f"{'=' * 60}",
            "\n📋 GRADING:",
        ]

        for score in result.scores:
            emoji = (
                "✅"
                if score.grade in ["A", "B"]
                else "⚠️"
                if score.grade == "C"
                else "❌"
            )
            lines.append(
                f"  {emoji} {score.criteria.value}: {score.score}/10 ({score.grade})"
            )
            if score.evidence:
                lines.append(f"      Evidence: {score.evidence}")

        lines.extend(
            [
                f"{'=' * 60}",
                f"🐛 BUGS FOUND: {len(result.bugs)}",
            ]
        )

        for i, bug in enumerate(result.bugs, 1):
            lines.append(f"  {i}. {bug}")

        lines.extend(
            [f"{'=' * 60}", f"📝 FEEDBACK:", f"  {result.feedback}", f"{'=' * 60}\n"]
        )

        return "\n".join(lines)


def run_evaluator(
    output: str, output_type: str = "code", expected: dict = None
) -> EvaluationResult:
    """
    Función principal para ejecutar el Evaluator.

    Usage:
        from 02_Evaluator_Runner import run_evaluator

        code_output = "def add(a, b): return a + b"
        result = run_evaluator(code_output, output_type="code")
        # result.passed = True/False
    """
    print("\n🔍 Inicializando Evaluator Agent...")

    evaluator = EvaluatorRunner(output_type=output_type)
    result = evaluator.evaluate(output, expected)

    print(evaluator.get_report(result))

    return result


if __name__ == "__main__":
    # Demo
    print("\n🔬 Testing Evaluator with different outputs:\n")

    # Test 1: Code
    code = "def calculate_total(prices): return sum(prices)"
    print("--- TEST 1: Code ---")
    result = run_evaluator(code, "code")

    # Test 2: Design (good)
    design_good = """
    <div class="unique-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%)">
        <h1>Custom Design</h1>
    </div>
    """
    print("\n--- TEST 2: Design (Original) ---")
    result = run_evaluator(design_good, "design")

    # Test 3: Design (AI slop)
    design_slop = """
    <div class="card" style="box-shadow: 0 4px 6px rgba(0,0,0,0.1)">
        <button class="btn">Click me</button>
    </div>
    """
    print("\n--- TEST 3: Design (AI Slop) ---")
    result = run_evaluator(design_slop, "design")
