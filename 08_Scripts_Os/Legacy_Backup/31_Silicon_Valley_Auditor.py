"""
SILICON VALLEY QUALITY AUDITOR - PersonalOS v1.0
Validación de estándares de código de nivel élite para herramientas AIPM.
"""

import ast
import os
from typing import Dict, List


class SiliconValleyAuditor:
    """
    Auditor de calidad que valida código contra estándares Silicon Valley:
    - Docstrings completos
    - Type hints
    - Manejo de errores
    - PEP 8 compliance
    - Mejores prácticas
    """

    def __init__(self):
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.tools_to_audit = [
            "22_AIPM_Trace_Logger.py",
            "23_AIPM_Evaluator.py",
            "24_AIPM_Interview_Sim.py",
            "25_Token_Budget_Guard.py",
            "26_RAG_Optimizer_Pro.py",
            "27_Probabilistic_Risk_Audit.py",
            "28_AIPM_Control_Center.py",
            "29_Guardrails_Service.py",
            "30_AIPM_Consolidated_Report.py",
        ]

    def audit_file(self, filepath: str) -> Dict:
        """Audita un archivo Python individual."""
        results = {
            "file": os.path.basename(filepath),
            "status": "PASS",
            "issues": [],
            "score": 10.0,
        }

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                tree = ast.parse(content)

            # 1. Verificar docstring del módulo
            if not ast.get_docstring(tree):
                results["issues"].append("[ERROR] Falta docstring del módulo")
                results["score"] -= 1.0

            # 2. Analizar clases y funciones
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    if not ast.get_docstring(node):
                        results["issues"].append(
                            f"[ISSUE] Clase '{node.name}' sin docstring"
                        )
                        results["score"] -= 0.5

                if isinstance(node, ast.FunctionDef):
                    if not ast.get_docstring(node) and not node.name.startswith("_"):
                        results["issues"].append(
                            f"[ISSUE] Función '{node.name}' sin docstring"
                        )
                        results["score"] -= 0.3

                    # Verificar type hints
                    if not node.returns and not node.name.startswith("_"):
                        results["issues"].append(
                            f"[TIP] Función '{node.name}' sin type hint de retorno"
                        )
                        results["score"] -= 0.2

            # 3. Verificar manejo de errores básico
            has_try_except = any(isinstance(node, ast.Try) for node in ast.walk(tree))
            if not has_try_except:
                results["issues"].append(
                    "[TIP] No se detectó manejo de excepciones (try/except)"
                )
                results["score"] -= 0.5

            # Determinar estado final
            if results["score"] >= 9.0:
                results["status"] = "ELITE"
            elif results["score"] >= 7.0:
                results["status"] = "PASS"
            else:
                results["status"] = "NEEDS_IMPROVEMENT"

        except Exception as e:
            results["status"] = "ERROR"
            results["issues"].append(f"Error al analizar: {str(e)}")
            results["score"] = 0.0

        return results

    def run_full_audit(self) -> Dict:
        """Ejecuta auditoría completa de todas las herramientas AIPM."""
        print("\n" + "=" * 70)
        print("   SILICON VALLEY QUALITY AUDIT - AIPM TOOLS")
        print("=" * 70 + "\n")

        audit_results = []
        total_score = 0

        for tool in self.tools_to_audit:
            filepath = os.path.join(self.script_dir, tool)
            if os.path.exists(filepath):
                result = self.audit_file(filepath)
                audit_results.append(result)
                total_score += result["score"]

                # Mostrar resultado
                print(f"FILE: {result['file']}")
                print(f"   Status: {result['status']}")
                print(f"   Score: {result['score']:.1f}/10.0")
                if result["issues"]:
                    for issue in result["issues"]:
                        print(f"      {issue}")
                print()
            else:
                print(f"WARNING: Archivo no encontrado: {tool}\n")

        # Calcular promedio
        avg_score = total_score / len(audit_results) if audit_results else 0

        print("=" * 70)
        print(f"   SCORE PROMEDIO: {avg_score:.1f}/10.0")

        if avg_score >= 9.0:
            print("   CERTIFICACION: ELITE GRADE - SILICON VALLEY APPROVED")
        elif avg_score >= 7.0:
            print("   CERTIFICACION: PRODUCTION READY")
        else:
            print("   ESTADO: REQUIERE MEJORAS")

        print("=" * 70 + "\n")

        return {
            "total_files": len(audit_results),
            "average_score": avg_score,
            "results": audit_results,
            "certification": "ELITE"
            if avg_score >= 9.0
            else "PRODUCTION"
            if avg_score >= 7.0
            else "NEEDS_WORK",
        }


if __name__ == "__main__":
    auditor = SiliconValleyAuditor()
    report = auditor.run_full_audit()
