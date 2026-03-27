#!/usr/bin/env python3
"""
SKILL 7: DIETER RAMS DESIGN VALIDATOR
Archivo: dieter_rams_design_validator.py
Descripción: Valida y optimiza diseños siguiendo los 10 Principios de Buen Diseño de Dieter Rams.

Los 10 Principios:
1. Innovador - Las posibilidades de innovación no están agotadas
2. Útil - Un producto debe satisfacer criterios funcionales, psicológicos y estéticos
3. Estético - La calidad estética es integral para la utilidad
4. Comprensible - Aclara la estructura del producto
5. Discreto - El diseño es neutral y contenido
6. Honesto - No exagera ni manipula al consumidor
7. Duradero - Evita tendencias pasajeras
8. Cuidadoso - Minucioso en cada detalle
9. Amigable - Contribuye a preservar el ambiente
10. Menos, pero mejor - Se concentra en lo esencial

Execution Mode: Hybrid (in-process analysis + isolated rendering)
"""

import sys
import json
import re
from pathlib import Path
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, asdict
from enum import Enum
from datetime import datetime

class DesignPrinciple(Enum):
    """Los 10 Principios de Dieter Rams"""
    INNOVATIVE = "innovador"
    USEFUL = "util"
    AESTHETIC = "estetico"
    UNDERSTANDABLE = "comprensible"
    UNOBTRUSIVE = "discreto"
    HONEST = "honesto"
    LONG_LASTING = "duradero"
    THOROUGH = "cuidadoso"
    ENVIRONMENTALLY_FRIENDLY = "amigable"
    AS_LITTLE_DESIGN_AS_POSSIBLE = "menos_pero_mejor"

@dataclass
class PrincipleScore:
    """Evaluación de un principio individual"""
    principle: str
    score: float  # 0-100
    compliance: str  # "excellent", "good", "needs_improvement", "poor"
    violations: List[str]
    recommendations: List[str]
    examples: List[str]

@dataclass
class DesignEvaluation:
    """Evaluación completa de diseño"""
    overall_score: float
    rams_compliance_level: str  # "Rams-certified", "Good", "Needs work", "Anti-Rams"
    principle_scores: List[PrincipleScore]
    strengths: List[str]
    weaknesses: List[str]
    actionable_recommendations: List[str]
    design_philosophy_summary: str

class DieterRamsDesignValidator:
    """
    Validador de diseño basado en principios de Dieter Rams.

    Analiza:
    - UI/UX designs
    - Product designs
    - Interior designs
    - Branding & identity
    - Web/App interfaces
    """

    def __init__(self):
        self.principle_weights = self._define_principle_weights()
        self.evaluation_criteria = self._define_evaluation_criteria()

    def _define_principle_weights(self) -> Dict[str, float]:
        """
        Pesos de importancia por principio (suman 1.0).
        En el espíritu de Rams, "Menos pero mejor" tiene peso extra.
        """
        return {
            "innovador": 0.10,
            "util": 0.15,
            "estetico": 0.12,
            "comprensible": 0.13,
            "discreto": 0.08,
            "honesto": 0.09,
            "duradero": 0.11,
            "cuidadoso": 0.07,
            "amigable": 0.06,
            "menos_pero_mejor": 0.09  # Principio filosófico central
        }

    def _define_evaluation_criteria(self) -> Dict[str, Dict]:
        """
        Criterios específicos para evaluar cada principio.
        """
        return {
            "innovador": {
                "description": "Las posibilidades de innovación no están agotadas. El desarrollo tecnológico ofrece nuevas oportunidades de diseño.",
                "check_for": [
                    "Uso de nuevas tecnologías de forma significativa",
                    "Soluciones creativas a problemas existentes",
                    "Evita copiar diseños existentes sin mejora",
                    "Aprovecha materiales o procesos innovadores"
                ],
                "red_flags": [
                    "Copia exacta de diseños populares",
                    "No aprovecha capacidades tecnológicas actuales",
                    "Diseño estancado en paradigmas antiguos"
                ]
            },
            "util": {
                "description": "Un producto debe satisfacer criterios funcionales, psicológicos y estéticos. Enfatiza la utilidad sobre todo.",
                "check_for": [
                    "Cumple su función principal de forma excelente",
                    "Considera necesidades psicológicas del usuario",
                    "Balance entre forma y función",
                    "Cada elemento tiene un propósito claro"
                ],
                "red_flags": [
                    "Elementos puramente decorativos sin función",
                    "Función comprometida por estética",
                    "No resuelve el problema del usuario",
                    "Características innecesarias que complican uso"
                ]
            },
            "estetico": {
                "description": "La calidad estética es integral para la utilidad porque los productos afectan el bienestar de las personas.",
                "check_for": [
                    "Estética limpia y atemporal",
                    "Armonía visual en proporciones",
                    "Paleta de colores restringida y deliberada",
                    "Tipografía legible y apropiada",
                    "Espacios en blanco utilizados estratégicamente"
                ],
                "red_flags": [
                    "Sobrecarga visual",
                    "Colores que no tienen justificación",
                    "Tipografía decorativa que reduce legibilidad",
                    "Texturas o efectos innecesarios"
                ]
            },
            "comprensible": {
                "description": "Aclara la estructura del producto. Es intuitivo y auto-revelador de su función.",
                "check_for": [
                    "Interfaz intuitiva sin necesidad de manual",
                    "Jerarquía visual clara",
                    "Affordances evidentes (botones parecen clicables)",
                    "Feedback inmediato a acciones del usuario",
                    "Estructura lógica y predecible"
                ],
                "red_flags": [
                    "Controles ocultos o no obvios",
                    "Iconografía ambigua",
                    "Flujo de usuario confuso",
                    "Falta de feedback visual",
                    "Requiere capacitación extensa"
                ]
            },
            "discreto": {
                "description": "El diseño es neutral y contenido, dejando espacio para la autoexpresión del usuario.",
                "check_for": [
                    "No impone personalidad del diseñador",
                    "Neutro pero no aburrido",
                    "Se integra en el ambiente",
                    "No busca llamar la atención innecesariamente"
                ],
                "red_flags": [
                    "Diseño egocéntrico (más sobre el diseñador que el usuario)",
                    "Elementos que gritan por atención",
                    "Personalización excesiva",
                    "Branding intrusivo"
                ]
            },
            "honesto": {
                "description": "No exagera ni manipula al consumidor. Presenta el producto tal como es sin falsas promesas.",
                "check_for": [
                    "Comunicación clara y veraz",
                    "No oculta limitaciones",
                    "Promete solo lo que puede cumplir",
                    "Materiales auténticos (no imita otros materiales)"
                ],
                "red_flags": [
                    "Dark patterns en UX",
                    "Exageraciones en capacidades",
                    "Materiales que imitan otros de mayor calidad",
                    "Información oculta o engañosa"
                ]
            },
            "duradero": {
                "description": "Evita tendencias pasajeras y permanece relevante durante muchos años.",
                "check_for": [
                    "Diseño atemporal",
                    "No sigue modas pasajeras",
                    "Calidad que resiste el paso del tiempo",
                    "Actualizable o adaptable"
                ],
                "red_flags": [
                    "Sigue trends actuales sin criterio",
                    "Diseño que se sentirá anticuado en 2 años",
                    "Obsolescencia programada",
                    "Materiales de baja durabilidad"
                ]
            },
            "cuidadoso": {
                "description": "Minucioso en cada detalle. Nada es arbitrario o al azar.",
                "check_for": [
                    "Atención al detalle en cada elemento",
                    "Consistencia en todo el diseño",
                    "Márgenes y espaciados precisos",
                    "Calidad en acabados y transiciones",
                    "Sistema de diseño coherente"
                ],
                "red_flags": [
                    "Inconsistencias visuales",
                    "Alineaciones descuidadas",
                    "Espaciados arbitrarios",
                    "Detalles sin pulir",
                    "Falta de sistema de diseño"
                ]
            },
            "amigable": {
                "description": "Contribuye a preservar el ambiente, conserva recursos y minimiza la contaminación.",
                "check_for": [
                    "Eficiencia energética",
                    "Materiales sostenibles o reciclables",
                    "Diseño modular para reparación",
                    "Minimiza desperdicio en producción",
                    "Performance optimizado (menor consumo de recursos digitales)"
                ],
                "red_flags": [
                    "Recursos digitales innecesarios (imágenes pesadas)",
                    "No optimizado para performance",
                    "Diseño que fomenta consumo excesivo",
                    "Materiales no sostenibles sin justificación"
                ]
            },
            "menos_pero_mejor": {
                "description": "Se concentra en lo esencial. La simplicidad es mejor que la complejidad innecesaria.",
                "check_for": [
                    "Solo lo esencial está presente",
                    "Cada elemento está justificado",
                    "Simplicidad sin ser simplista",
                    "Purity of form (pureza de forma)",
                    "Nada que quitar, nada que añadir"
                ],
                "red_flags": [
                    "Características innecesarias",
                    "Complejidad sin valor agregado",
                    "Múltiples formas de hacer lo mismo",
                    "Ornamentación gratuita",
                    "Feature creep"
                ]
            }
        }

    def evaluate_design(
        self,
        design_description: str,
        design_type: str = "ui",  # ui, product, interior, branding
        context: Optional[Dict[str, Any]] = None
    ) -> DesignEvaluation:
        """
        Evalúa un diseño contra los 10 principios de Rams.

        Args:
            design_description: Descripción detallada del diseño
            design_type: Tipo de diseño (afecta criterios de evaluación)
            context: Contexto adicional (target audience, constraints, etc.)

        Returns:
            DesignEvaluation completa
        """
        principle_scores = []

        # Evaluar cada principio
        for principle_key, criteria in self.evaluation_criteria.items():
            score = self._evaluate_principle(
                design_description,
                principle_key,
                criteria,
                design_type,
                context or {}
            )
            principle_scores.append(score)

        # Calcular score general ponderado
        overall_score = sum(
            score.score * self.principle_weights[score.principle]
            for score in principle_scores
        )

        # Determinar nivel de compliance
        compliance_level = self._determine_compliance_level(overall_score)

        # Identificar fortalezas y debilidades
        strengths = [
            f"{score.principle.capitalize()}: {score.score:.0f}/100"
            for score in principle_scores
            if score.score >= 80
        ]

        weaknesses = [
            f"{score.principle.capitalize()}: {score.score:.0f}/100 - {score.violations[0] if score.violations else 'Necesita mejora'}"
            for score in principle_scores
            if score.score < 60
        ]

        # Generar recomendaciones accionables
        recommendations = self._generate_actionable_recommendations(principle_scores)

        # Resumen filosófico
        philosophy_summary = self._generate_philosophy_summary(overall_score, principle_scores)

        return DesignEvaluation(
            overall_score=overall_score,
            rams_compliance_level=compliance_level,
            principle_scores=principle_scores,
            strengths=strengths,
            weaknesses=weaknesses,
            actionable_recommendations=recommendations,
            design_philosophy_summary=philosophy_summary
        )

    def _evaluate_principle(
        self,
        design_desc: str,
        principle_key: str,
        criteria: Dict,
        design_type: str,
        context: Dict
    ) -> PrincipleScore:
        """
        Evalúa un principio específico.
        En producción, usar LLM con criteria como prompt.
        """
        # Simplificado: análisis de keywords
        desc_lower = design_desc.lower()

        # Calcular score basado en keywords presentes
        positive_matches = sum(
            1 for keyword in criteria['check_for']
            if any(word in desc_lower for word in keyword.lower().split())
        )

        negative_matches = sum(
            1 for flag in criteria['red_flags']
            if any(word in desc_lower for word in flag.lower().split())
        )

        # Score = (positivos * 10) - (negativos * 15)
        raw_score = (positive_matches * 10) - (negative_matches * 15)
        score = max(0, min(100, 50 + raw_score))  # Normalizar a 0-100

        # Determinar compliance
        if score >= 90:
            compliance = "excellent"
        elif score >= 75:
            compliance = "good"
        elif score >= 60:
            compliance = "needs_improvement"
        else:
            compliance = "poor"

        # Identificar violaciones
        violations = [
            flag for flag in criteria['red_flags']
            if any(word in desc_lower for word in flag.lower().split())
        ]

        # Generar recomendaciones
        recommendations = self._generate_principle_recommendations(
            principle_key,
            score,
            violations
        )

        # Ejemplos de buen diseño para este principio
        examples = self._get_principle_examples(principle_key)

        return PrincipleScore(
            principle=principle_key,
            score=score,
            compliance=compliance,
            violations=violations[:3],  # Top 3
            recommendations=recommendations[:3],
            examples=examples[:2]
        )

    def _determine_compliance_level(self, score: float) -> str:
        """Determina nivel de compliance con filosofía Rams"""
        if score >= 85:
            return "Rams-certified ✅"
        elif score >= 70:
            return "Good Design ✓"
        elif score >= 50:
            return "Needs Work ⚠️"
        else:
            return "Anti-Rams ❌"

    def _generate_actionable_recommendations(
        self,
        principle_scores: List[PrincipleScore]
    ) -> List[str]:
        """
        Genera top 5 recomendaciones accionables priorizadas.
        """
        all_recommendations = []

        for score in principle_scores:
            for rec in score.recommendations:
                # Prioridad = (100 - score) para focalizarse en áreas débiles
                priority = 100 - score.score
                all_recommendations.append((priority, rec, score.principle))

        # Ordenar por prioridad
        all_recommendations.sort(reverse=True)

        # Top 5 con contexto
        top_5 = [
            f"[{principle.upper()}] {rec}"
            for _, rec, principle in all_recommendations[:5]
        ]

        return top_5

    def _generate_principle_recommendations(
        self,
        principle: str,
        score: float,
        violations: List[str]
    ) -> List[str]:
        """Genera recomendaciones específicas por principio"""
        recommendations_map = {
            "innovador": [
                "Explora nuevas interacciones o patrones que aporten valor real",
                "Usa tecnología emergente solo si mejora la experiencia",
                "Diferénciate con innovación funcional, no cosmética"
            ],
            "util": [
                "Elimina todo elemento que no sirva una función clara",
                "Prioriza la funcionalidad sobre la decoración",
                "Asegura que cada feature resuelva un problema real del usuario"
            ],
            "estetico": [
                "Reduce la paleta de colores a 2-3 principales",
                "Aumenta los espacios en blanco para dar respiro visual",
                "Usa tipografía sans-serif limpia y legible",
                "Elimina efectos visuales innecesarios (sombras, gradientes)"
            ],
            "comprensible": [
                "Mejora la jerarquía visual con tamaño y peso",
                "Agrupa elementos relacionados con proximidad",
                "Usa affordances claras (botones que parecen botones)",
                "Implementa feedback inmediato a acciones"
            ],
            "discreto": [
                "Reduce la saturación de colores",
                "Elimina animaciones llamativas sin propósito",
                "Deja que el contenido, no el diseño, sea protagonista"
            ],
            "honesto": [
                "Comunica claramente qué hace cada elemento",
                "No uses dark patterns para manipular usuarios",
                "Sé transparente sobre limitaciones"
            ],
            "duradero": [
                "Evita trends actuales sin valor a largo plazo",
                "Usa diseño atemporal que envejecerá bien",
                "Prioriza calidad sobre novedades efímeras"
            ],
            "cuidadoso": [
                "Revisa alineación y espaciado pixel-perfect",
                "Crea sistema de diseño consistente",
                "Pule todos los detalles, incluso los pequeños"
            ],
            "amigable": [
                "Optimiza imágenes y recursos",
                "Reduce código y dependencias innecesarias",
                "Diseña para accesibilidad (a11y)"
            ],
            "menos_pero_mejor": [
                "Pregunta: ¿Qué pasaría si eliminara este elemento?",
                "Simplifica hasta que no quede nada más que quitar",
                "Un botón claro es mejor que tres opciones confusas"
            ]
        }

        return recommendations_map.get(principle, ["Mejorar este aspecto"])

    def _get_principle_examples(self, principle: str) -> List[str]:
        """Ejemplos reales de buen diseño por principio"""
        examples_map = {
            "innovador": [
                "Apple iPhone (2007): Redefinió la interacción touch",
                "Braun T3 Radio (Rams): Nuevo paradigma en radio portátil"
            ],
            "util": [
                "Braun SK 4 (Rams): 'Snow White's Coffin' - función pura",
                "Google Search: Una caja, un botón, utilidad máxima"
            ],
            "estetico": [
                "Braun ET66 Calculator (Rams/Dietrich Lubs): Belleza funcional",
                "Apple Watch: Estética integrada con función"
            ],
            "comprensible": [
                "Nest Thermostat: Intuitivo sin manual",
                "Stripe Dashboard: Interfaz auto-explicativa"
            ],
            "discreto": [
                "Muji Products: Diseño neutral que se integra",
                "Nothing Phone: Diseño contenido y funcional"
            ],
            "honesto": [
                "Patagonia: Transparencia en materiales y procesos",
                "DuckDuckGo: Privacy sin exageraciones"
            ],
            "duradero": [
                "Vitsœ 606 Shelving: Diseñado en 1960, relevante hoy",
                "Leica M Cameras: Diseño atemporal desde 1954"
            ],
            "cuidadoso": [
                "Braun Products: Atención obsesiva al detalle",
                "Apple Hardware: Precisión en cada milímetro"
            ],
            "amigable": [
                "Fairphone: Diseño modular y reparable",
                "Ecosia: Search engine que planta árboles"
            ],
            "menos_pero_mejor": [
                "Braun T1000 Radio: Esencia destilada",
                "WhatsApp: Comunicación sin features innecesarias"
            ]
        }

        return examples_map.get(principle, ["Ver productos Braun diseñados por Rams"])

    def _generate_philosophy_summary(
        self,
        overall_score: float,
        principle_scores: List[PrincipleScore]
    ) -> str:
        """Genera resumen filosófico del diseño"""
        if overall_score >= 85:
            return """Este diseño encarna la filosofía de Rams: es funcional, bello en su simplicidad,
y respetuoso con el usuario. Se concentra en lo esencial y elimina todo lo superfluo.
Es el tipo de diseño que envejecerá bien."""

        elif overall_score >= 70:
            return """Este diseño muestra buen entendimiento de los principios de Rams.
Con algunas mejoras en simplicidad y atención al detalle, puede alcanzar la excelencia.
Está en el camino correcto hacia 'menos, pero mejor'."""

        elif overall_score >= 50:
            return """Este diseño tiene potencial pero se desvía de los principios de Rams en áreas clave.
Necesita enfocarse más en la utilidad, eliminar elementos innecesarios, y simplificar.
Menos features, más refinamiento."""

        else:
            return """Este diseño contradice la filosofía de Rams. Hay exceso donde debería haber restricción,
complejidad donde debería haber claridad, y decoración donde debería haber función.
Requiere repensar desde cero con foco en lo esencial."""

    def generate_design_report(
        self,
        evaluation: DesignEvaluation,
        output_format: str = "markdown"
    ) -> str:
        """
        Genera reporte detallado de evaluación.
        """
        if output_format == "markdown":
            return self._generate_markdown_report(evaluation)
        elif output_format == "html":
            return self._generate_html_report(evaluation)
        else:
            return json.dumps(asdict(evaluation), indent=2)

    def _generate_markdown_report(self, eval: DesignEvaluation) -> str:
        """Genera reporte en Markdown"""
        report = f"""# Evaluación de Diseño - Principios de Dieter Rams

**Score General**: {eval.overall_score:.1f}/100
**Nivel de Compliance**: {eval.rams_compliance_level}
**Fecha**: {datetime.now().strftime('%Y-%m-%d')}

---

## 📊 Resumen Ejecutivo

{eval.design_philosophy_summary}

### ✅ Fortalezas
{''.join(f"- {s}\n" for s in eval.strengths) if eval.strengths else "- Ninguna identificada"}

### ⚠️ Áreas de Mejora
{''.join(f"- {w}\n" for w in eval.weaknesses) if eval.weaknesses else "- Ninguna identificada"}

---

## 🎯 Top 5 Recomendaciones Accionables

{''.join(f"{i+1}. {rec}\n" for i, rec in enumerate(eval.actionable_recommendations))}

---

## 📋 Evaluación por Principio

"""
        # Agregar cada principio
        for score in eval.principle_scores:
            report += f"""### {score.principle.upper().replace('_', ' ')} - {score.score:.0f}/100
**Compliance**: {score.compliance}

"""
            if score.violations:
                report += f"**Violaciones detectadas**:\n"
                for v in score.violations:
                    report += f"- {v}\n"
                report += "\n"

            if score.recommendations:
                report += f"**Recomendaciones**:\n"
                for r in score.recommendations:
                    report += f"- {r}\n"
                report += "\n"

            if score.examples:
                report += f"**Ejemplos de referencia**:\n"
                for e in score.examples:
                    report += f"- {e}\n"
                report += "\n"

            report += "---\n\n"

        report += f"""
## 💡 Filosofía de Diseño

> "Menos, pero mejor" - Dieter Rams

El buen diseño no se trata de agregar hasta que no haya nada más que agregar.
Se trata de quitar hasta que no haya nada más que quitar.

**Score final: {eval.overall_score:.1f}/100**

---

*Generado por DieterRamsDesignValidator v1.0*
"""
        return report

    def _generate_html_report(self, eval: DesignEvaluation) -> str:
        """Genera reporte en HTML con estilos minimalistas (Rams-approved)"""
        # Simplificado - en producción usar templates
        return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Design Evaluation - Dieter Rams Principles</title>
    <style>
        body {{ font-family: 'Helvetica Neue', sans-serif; max-width: 800px; margin: 40px auto; }}
        h1 {{ font-weight: 300; border-bottom: 1px solid #000; }}
        .score {{ font-size: 3em; font-weight: 100; }}
    </style>
</head>
<body>
    <h1>Design Evaluation</h1>
    <div class="score">{eval.overall_score:.1f}/100</div>
    <p>{eval.rams_compliance_level}</p>
</body>
</html>"""

# ============================================================================
# ISOLATED AGENT MODE
# ============================================================================

def run_isolated_design_validation(params: Dict[str, Any]) -> Dict[str, Any]:
    """
    Ejecuta validación de diseño en modo aislado.
    """
    validator = DieterRamsDesignValidator()

    design_description = params.get('design_description', '')
    design_type = params.get('design_type', 'ui')
    context = params.get('context', {})
    output_format = params.get('output_format', 'markdown')

    # Evaluar diseño
    evaluation = validator.evaluate_design(
        design_description,
        design_type,
        context
    )

    # Generar reporte
    report = validator.generate_design_report(evaluation, output_format)

    return {
        "evaluation": asdict(evaluation),
        "report": report,
        "output_format": output_format
    }

def main():
    """Entry point for isolated execution"""
    if len(sys.argv) != 3:
        print("Usage: dieter_rams_design_validator.py <input.json> <output.json>", file=sys.stderr)
        sys.exit(1)

    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2])

    try:
        with open(input_file, 'r') as f:
            params = json.load(f)

        result = run_isolated_design_validation(params)

        with open(output_file, 'w') as f:
            json.dump({
                "status": "success",
                "result": result,
                "metadata": {
                    "agent": "dieter_rams_design_validator",
                    "version": "1.0",
                    "principles_evaluated": 10
                }
            }, f, indent=2)

    except Exception as e:
        with open(output_file, 'w') as f:
            json.dump({
                "status": "error",
                "result": None,
                "metadata": {
                    "error": str(e),
                    "agent": "dieter_rams_design_validator"
                }
            }, f, indent=2)
        sys.exit(1)

if __name__ == "__main__":
    main()
