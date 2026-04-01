"""
80_Edge_Case_Validator.py - Armor Layer Protected
Detecta boundary conditions y valida inputs extremos.
Basado en: 01_Core/03_Skills/05_Gentleman/05_Utilities/11_Edge_Case/SKILL.md
"""

import ast
import sys

sys.stdout.reconfigure(encoding="utf-8")
import inspect
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, TypeVar
from enum import Enum

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import PROJECT_ROOT, ENGINE_DIR

REQUIRED_DIRS = [
    "00_Core",
    "01_Brain",
    "02_Operations",
    "03_Knowledge",
    "04_Engine",
    "05_System",
    "06_Archive",
]
for d in REQUIRED_DIRS:
    if not (PROJECT_ROOT / d).exists():
        print(f"[WARN] Required directory not found: {d}")

BASE_DIR = PROJECT_ROOT
SCRIPTS_DIR = ENGINE_DIR / "08_Scripts_Os"


class Severity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


@dataclass
class EdgeCase:
    name: str
    description: str
    input_value: Any
    expected_behavior: str
    severity: Severity
    file_path: str = ""
    line_number: int = 0


@dataclass
class EdgeCaseReport:
    total_analyzed: int = 0
    edge_cases_found: int = 0
    boundary_cases: list[EdgeCase] = field(default_factory=list)
    empty_cases: list[EdgeCase] = field(default_factory=list)
    invalid_cases: list[EdgeCase] = field(default_factory=list)
    temporal_cases: list[EdgeCase] = field(default_factory=list)
    system_cases: list[EdgeCase] = field(default_factory=list)


class EdgeCaseAnalyzer:
    BOUNDARY_VALUES = {
        "str": {
            "empty": "",
            "whitespace": "   ",
            "unicode": "日本語",
            "very_long": "x" * 10000,
        },
        "int": {"zero": 0, "negative": -1, "max_int": 2**31 - 1, "min_int": -(2**31)},
        "float": {
            "zero": 0.0,
            "negative": -1.0,
            "max_float": 1.797e308,
            "inf": float("inf"),
            "nan": float("nan"),
        },
        "list": {"empty": [], "single": [1], "very_long": list(range(1001))},
        "dict": {"empty": {}, "nested": {"a": {"b": {}}}},
        "none": {"null": None},
    }

    def __init__(self, scripts_dir: Path):
        self.scripts_dir = scripts_dir

    def analyze_all(self) -> EdgeCaseReport:
        report = EdgeCaseReport()
        python_files = list(self.scripts_dir.glob("*.py"))
        report.total_analyzed = len(python_files)

        for py_file in python_files:
            cases = self.analyze_file(py_file)
            for case in cases:
                report.edge_cases_found += 1
                self._categorize_case(report, case)

        return report

    def analyze_file(self, file_path: Path) -> list[EdgeCase]:
        cases = []
        try:
            content = file_path.read_text(encoding="utf-8")
            tree = ast.parse(content)
            cases.extend(self._analyze_ast(tree, file_path))
            cases.extend(self._analyze_content(content, file_path))
        except Exception as e:
            print(f"⚠️  Error analizando {file_path}: {e}")
        return cases

    def _analyze_ast(self, tree: ast.AST, file_path: Path) -> list[EdgeCase]:
        cases = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                cases.extend(self._analyze_function(node, file_path))
            elif isinstance(node, ast.FunctionDef) and node.name in (
                "validate",
                "check",
                "process",
            ):
                cases.extend(self._analyze_validation_function(node, file_path))
        return cases

    def _analyze_function(
        self, func: ast.FunctionDef, file_path: Path
    ) -> list[EdgeCase]:
        cases = []
        for arg in func.args.args:
            cases.extend(self._analyze_parameter(arg.arg, file_path, func.lineno))
        return cases

    def _analyze_parameter(
        self, name: str, file_path: Path, line: int
    ) -> list[EdgeCase]:
        cases = []
        cases.append(
            EdgeCase(
                name=f"{name}_empty",
                description=f"Parameter '{name}' vacio",
                input_value="",
                expected_behavior="Handle gracefully",
                severity=Severity.HIGH,
                file_path=str(file_path),
                line_number=line,
            )
        )
        cases.append(
            EdgeCase(
                name=f"{name}_null",
                description=f"Parameter '{name}' es None",
                input_value=None,
                expected_behavior="Validate or reject",
                severity=Severity.HIGH,
                file_path=str(file_path),
                line_number=line,
            )
        )
        return cases

    def _analyze_validation_function(
        self, func: ast.FunctionDef, file_path: Path
    ) -> list[EdgeCase]:
        cases = []
        for node in ast.walk(func):
            if isinstance(node, ast.Compare):
                cases.append(
                    EdgeCase(
                        name="potential_division_by_zero",
                        description="Posible división por cero",
                        input_value=0,
                        expected_behavior="Validate before divide",
                        severity=Severity.CRITICAL,
                        file_path=str(file_path),
                        line_number=func.lineno,
                    )
                )
        return cases

    def _analyze_content(self, content: str, file_path: Path) -> list[EdgeCase]:
        cases = []
        if re.search(r"\/\s*0", content):
            cases.append(
                EdgeCase(
                    name="explicit_division_by_zero",
                    description="División por cero explícita",
                    input_value=0,
                    expected_behavior="Avoid division by zero",
                    severity=Severity.CRITICAL,
                    file_path=str(file_path),
                    line_number=0,
                )
            )
        if "eval(" in content or "exec(" in content:
            cases.append(
                EdgeCase(
                    name="code_injection_risk",
                    description="Riesgo de inyección de código (eval/exec)",
                    input_value="'; DROP TABLE",
                    expected_behavior="Sanitize input or avoid eval/exec",
                    severity=Severity.CRITICAL,
                    file_path=str(file_path),
                    line_number=0,
                )
            )
        if re.search(r'password\s*=\s*["\'][^"\']+["\']', content, re.IGNORECASE):
            cases.append(
                EdgeCase(
                    name="hardcoded_password",
                    description="Contraseña hardcodeada",
                    input_value="***",
                    expected_behavior="Use environment variables",
                    severity=Severity.HIGH,
                    file_path=str(file_path),
                    line_number=0,
                )
            )
        return cases

    def _categorize_case(self, report: EdgeCaseReport, case: EdgeCase):
        name_lower = case.name.lower()
        if any(kw in name_lower for kw in ["boundary", "max", "min", "overflow"]):
            report.boundary_cases.append(case)
        elif any(kw in name_lower for kw in ["empty", "null", "none", "undefined"]):
            report.empty_cases.append(case)
        elif any(kw in name_lower for kw in ["invalid", "malformed", "type"]):
            report.invalid_cases.append(case)
        elif any(
            kw in name_lower for kw in ["timezone", "leap", "dst", "date", "time"]
        ):
            report.temporal_cases.append(case)
        elif any(kw in name_lower for kw in ["disk", "network", "memory", "system"]):
            report.system_cases.append(case)
        else:
            report.boundary_cases.append(case)


def generate_report(report: EdgeCaseReport) -> str:
    lines = [
        "# 🔍 Edge Case Validator Report",
        "",
        f"**Archivos analizados:** {report.total_analyzed}",
        f"**Edge cases encontrados:** {report.edge_cases_found}",
        "",
        "---",
        "",
        "## Por Categoría",
        "",
        f"| Categoría | Cantidad |",
        f"|-----------|----------|",
        f"| Boundary | {len(report.boundary_cases)} |",
        f"| Empty/Null | {len(report.empty_cases)} |",
        f"| Invalid | {len(report.invalid_cases)} |",
        f"| Temporal | {len(report.temporal_cases)} |",
        f"| System | {len(report.system_cases)} |",
        "",
    ]

    if report.edge_cases_found > 0:
        lines.extend(
            [
                "## Detalle de Casos Críticos",
                "",
                "| Caso | Severidad | Archivo |",
                "|------|-----------|---------|",
            ]
        )
        critical_cases = [
            c
            for c in report.boundary_cases + report.empty_cases + report.invalid_cases
            if c.severity in (Severity.CRITICAL, Severity.HIGH)
        ]
        for case in critical_cases[:20]:
            icon = "🔴" if case.severity == Severity.CRITICAL else "🟡"
            lines.append(
                f"| {case.name} | {icon} {case.severity.value} | {Path(case.file_path).name} |"
            )

    return "\n".join(lines)


def main():
    print("🔍 Edge Case Validator")
    print("=" * 50)

    analyzer = EdgeCaseAnalyzer(SCRIPTS_DIR)
    report = analyzer.analyze_all()

    print(f"\n📊 Resumen:")
    print(f"   Archivos analizados: {report.total_analyzed}")
    print(f"   Edge cases encontrados: {report.edge_cases_found}")
    print(f"   - Boundary: {len(report.boundary_cases)}")
    print(f"   - Empty/Null: {len(report.empty_cases)}")
    print(f"   - Invalid: {len(report.invalid_cases)}")
    print(f"   - Temporal: {len(report.temporal_cases)}")
    print(f"   - System: {len(report.system_cases)}")

    report_md = generate_report(report)
    report_file = BASE_DIR / "04_Engine" / "06_Reports" / "edge_case_report.md"
    report_file.parent.mkdir(parents=True, exist_ok=True)
    report_file.write_text(report_md, encoding="utf-8")
    print(f"\n📄 Reporte guardado: {report_file}")

    return 0 if report.edge_cases_found == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
