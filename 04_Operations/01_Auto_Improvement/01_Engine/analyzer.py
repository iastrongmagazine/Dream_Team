"""
📊 ANALYZER - Módulo de Análisis de Causa Raíz
=================================================
Analiza cada issue detectado y determina:
- Causa raíz (root cause)
- Impacto (high/medium/low)
- Solución recomendada
- Riesgo de la solución
- Si es auto-fixable
"""

from pathlib import Path
from typing import Dict, Any, List


class Analyzer:
    """Motor de análisis de causa raíz"""

    def __init__(self, project_root: Path):
        self.project_root = project_root

        # Known root causes patterns
        self.root_cause_patterns = {
            "broken_import": {
                "root_cause": "Rutas hardcodeadas o estructura legacy",
                "impact": "Alto",
                "risk": "Bajo",
                "tier": 1,
                "auto_fixable": True,
                "solution": "Actualizar a config_paths.py",
            },
            "orphan_file": {
                "root_cause": "Archivo no utilizado o muy pequeño",
                "impact": "Bajo",
                "risk": "Muy Bajo",
                "tier": 1,
                "auto_fixable": True,
                "solution": "Mover a archive o eliminar",
            },
            "naming_inconsistency": {
                "root_cause": "Convención de nombres no seguida",
                "impact": "Bajo",
                "risk": "Bajo",
                "tier": 2,
                "auto_fixable": False,
                "solution": "Renombrar manualmente",
            },
            "duplicate_script": {
                "root_cause": "Duplicación de código",
                "impact": "Medio",
                "risk": "Medio",
                "tier": 2,
                "auto_fixable": False,
                "solution": "Consolidar scripts",
            },
            "missing_docstring": {
                "root_cause": "Documentación faltante",
                "impact": "Bajo",
                "risk": "Muy Bajo",
                "tier": 1,
                "auto_fixable": True,
                "solution": "Agregar docstring básico",
            },
            "large_file": {
                "root_cause": "Archivo demasiado grande",
                "impact": "Medio",
                "risk": "Medio",
                "tier": 2,
                "auto_fixable": False,
                "solution": "Separar en módulos",
            },
        }

    def quick_analyze(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Análisis rápido - solo determina si es auto-fixable"""
        issue_type = issue.get("type", "unknown")

        # Get known pattern
        pattern = self.root_cause_patterns.get(issue_type, {})

        analysis = {
            **issue,
            "root_cause": pattern.get("root_cause", "Desconocido"),
            "impact": pattern.get("impact", "Desconocido"),
            "risk": pattern.get("risk", "Desconocido"),
            "tier": pattern.get("tier", 3),
            "auto_fixable": pattern.get("auto_fixable", False),
            "suggested_solution": pattern.get("solution", "Revisar manualmente"),
            "should_fix": pattern.get("tier", 3) <= 2,
        }

        return analysis

    def analyze(self, issue: Dict[str, Any]) -> Dict[str, Any]:
        """Análisis completo - determina toda la metadata"""
        # Start with quick analysis
        analysis = self.quick_analyze(issue)

        # Add additional analysis
        issue_type = issue.get("type", "unknown")

        # Custom analysis based on type
        if issue_type == "broken_import":
            analysis = self._analyze_broken_import(issue, analysis)
        elif issue_type == "naming_inconsistency":
            analysis = self._analyze_naming(issue, analysis)
        elif issue_type == "duplicate_script":
            analysis = self._analyze_duplicate(issue, analysis)

        # Calculate priority score
        analysis["priority_score"] = self._calculate_priority(analysis)

        return analysis

    def _analyze_broken_import(self, issue: Dict, analysis: Dict) -> Dict:
        """Análisis específico para imports rotos"""
        pattern = issue.get("pattern", "")

        if "Legacy_Backup" in pattern:
            analysis["specific_issue"] = "Legacy path reference"
            analysis["fix_action"] = "Reemplazar con ruta de _Fixed/"
        elif "04_Operations" in pattern:
            analysis["specific_issue"] = "Old structure reference"
            analysis["fix_action"] = "Usar config_paths.py"
        else:
            analysis["specific_issue"] = "Unknown broken import"
            analysis["fix_action"] = "Investigar y corregir"

        return analysis

    def _analyze_naming(self, issue: Dict, analysis: Dict) -> Dict:
        """Análisis específico para naming"""
        file_path = issue.get("file", "")
        file_name = file_path.split("/")[-1]

        # Determine expected pattern
        if file_path.endswith(".py"):
            analysis["expected_pattern"] = "XX_Nombre.py"
            analysis["suggestion"] = f"Cambiar {file_name} a XX_{file_name}"
        elif file_path.endswith(".md"):
            analysis["expected_pattern"] = "XX_Nombre.md"
            analysis["suggestion"] = f"Cambiar {file_name} a XX_{file_name}"
        else:
            analysis["expected_pattern"] = "XX_Nombre.ext"
            analysis["suggestion"] = "Revisar convención de nombres"

        return analysis

    def _analyze_duplicate(self, issue: Dict, analysis: Dict) -> Dict:
        """Análisis específico para duplicados"""
        files = issue.get("files", [])

        analysis["duplicate_count"] = len(files)
        analysis["merge_candidate"] = files[0] if files else None
        analysis["archive_candidates"] = files[1:] if len(files) > 1 else []

        return analysis

    def _calculate_priority(self, analysis: Dict) -> float:
        """Calcular score de prioridad (0-100)"""
        # Factors
        severity_scores = {"high": 30, "medium": 20, "low": 10}

        auto_fix_bonus = 20 if analysis.get("auto_fixable") else 0
        tier_penalty = (analysis.get("tier", 3) - 1) * 15

        base_score = severity_scores.get(analysis.get("impact", "low"), 10)
        score = base_score + auto_fix_bonus - tier_penalty

        return max(0, min(100, score))

    def batch_analyze(self, issues: List[Dict]) -> List[Dict]:
        """Analizar múltiples issues"""
        return [self.analyze(issue) for issue in issues]

    def get_fix_plan(self, analysis: Dict) -> Dict[str, Any]:
        """Generar plan de fix basado en análisis"""
        return {
            "issue": analysis.get("description"),
            "type": analysis.get("type"),
            "action": analysis.get("fix_action") or analysis.get("suggested_solution"),
            "tier": analysis.get("tier"),
            "auto_fixable": analysis.get("auto_fixable"),
            "risk": analysis.get("risk"),
            "priority": analysis.get("priority_score"),
        }
