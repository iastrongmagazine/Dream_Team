#!/usr/bin/env python3
"""
Skill Security Scanner v2.0

Escanea skills en busca de vulnerabilidades de seguridad.
Detecta: credenciales hardcodeadas, comandos peligrosos, paths sensibles.

Autor: Gentleman Programming
Versión: 2.0.0 (2026-03-30)
"""

import argparse
import io
import logging
import os
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Set

# Fix Unicode for Windows
if sys.platform == "win32":
    import codecs

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# Configuración de logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)


@dataclass
class SecurityFinding:
    """Representa un hallazgo de seguridad."""

    severity: str  # CRITICAL, HIGH, MEDIUM, LOW
    category: str
    file: str
    line: int
    message: str
    code_snippet: str = ""


@dataclass
class ScanResult:
    """Resultado del escaneo de una skill."""

    skill_path: str
    findings: List[SecurityFinding] = field(default_factory=list)

    @property
    def critical_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "CRITICAL")

    @property
    def high_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "HIGH")

    @property
    def medium_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "MEDIUM")

    @property
    def low_count(self) -> int:
        return sum(1 for f in self.findings if f.severity == "LOW")

    @property
    def is_clean(self) -> bool:
        return self.critical_count == 0 and self.high_count == 0


class SecurityScanner:
    """Escáner de seguridad para skills."""

    # Patrones de búsqueda de vulnerabilidades
    PATTERNS = {
        "CRITICAL": [
            # Credenciales hardcodeadas
            (
                r'password\s*=\s*["\'](?!{{|env|os\.getenv)[^"\']{8,}["\']',
                "Hardcoded password detected",
            ),
            (r'api[_-]?key\s*=\s*["\'][^"\']{16,}["\']', "Hardcoded API key detected"),
            (
                r'secret[_-]?key\s*=\s*["\'][^"\']{16,}["\']',
                "Hardcoded secret key detected",
            ),
            (r'token\s*=\s*["\'][^"\']{20,}["\']', "Hardcoded token detected"),
            # Ejecución remota
            (r"eval\s*\(", "Dangerous eval() usage"),
            (r"exec\s*\(", "Dangerous exec() usage"),
            (r"subprocess.*shell\s*=\s*True", "Shell=True is dangerous"),
        ],
        "HIGH": [
            # Paths sensibles
            (r"/etc/passwd", "Access to /etc/passwd"),
            (r"/etc/shadow", "Access to /etc/shadow"),
            (r"~/.ssh/", "Access to SSH directory"),
            # Comandos peligrosos
            (r"rm\s+-rf\s+/", "Recursive deletion detected"),
            (r"dd\s+if=", "Direct disk access"),
            # Inyección SQL simple
            (r'.*\+.*["\'].*%.*["\'].*', "Potential SQL injection"),
        ],
        "MEDIUM": [
            # Variables de entorno sin validación
            (r'os\.environ\.get\(["\'][^"\']+["\']', "Environment variable access"),
            # Archivos sin validación
            (r"open\s*\([^,]+,", "File operation without validation"),
            # Contraseñas débiles
            (r'password["\']\s*:\s*["\'][^"\']{0,7}["\']', "Weak password (too short)"),
        ],
        "LOW": [
            # Warnings informativos
            (r"print\s*\(.*password", "Password in print statement"),
            (r"logging\..*password", "Password in logging"),
            (r"# TODO.*password", "TODO about password in code"),
        ],
    }

    # Extensiones a escanear
    SCAN_EXTENSIONS = {".py", ".sh", ".js", ".ts", ".md", ".yaml", ".yml"}

    # Directorios a ignorar
    IGNORE_DIRS = {"__pycache__", ".git", "node_modules", ".venv", "venv"}

    def __init__(self, skill_path: str):
        self.skill_path = Path(skill_path)
        self.findings: List[SecurityFinding] = []

    def scan(self) -> ScanResult:
        """Ejecuta el escaneo completo."""
        logger.info(f"🔍 Scanning skill: {self.skill_path.name}")

        if not self.skill_path.exists():
            logger.error(f"❌ Path not found: {self.skill_path}")
            sys.exit(1)

        self._scan_recursive(self.skill_path)

        return ScanResult(skill_path=str(self.skill_path), findings=self.findings)

    def _scan_recursive(self, path: Path):
        """Escanea recursivamente."""
        if path.is_dir():
            if path.name in self.IGNORE_DIRS:
                return
            for item in path.iterdir():
                self._scan_recursive(item)
        elif path.is_file():
            if path.suffix.lower() in self.SCAN_EXTENSIONS:
                self._scan_file(path)

    def _scan_file(self, file_path: Path):
        """Escanea un archivo individual."""
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                lines = f.readlines()
        except Exception as e:
            logger.warning(f"⚠️  Cannot read {file_path}: {e}")
            return

        for line_num, line in enumerate(lines, 1):
            self._check_line(file_path, line_num, line)

    def _check_line(self, file_path: Path, line_num: int, line: str):
        """Verifica una línea contra los patrones."""
        for severity, patterns in self.PATTERNS.items():
            for pattern, message in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    finding = SecurityFinding(
                        severity=severity,
                        category="Pattern Match",
                        file=str(file_path.relative_to(self.skill_path)),
                        line=line_num,
                        message=message,
                        code_snippet=line.strip()[:80],
                    )
                    self.findings.append(finding)


def print_report(result: ScanResult):
    """Imprime el reporte de seguridad."""
    print("\n" + "=" * 60)
    print(f"🛡️  SECURITY SCAN REPORT: {result.skill_path}")
    print("=" * 60)

    if result.is_clean:
        print("\n✅ STATUS: CLEAN")
        print(f"   - 0 CRITICAL")
        print(f"   - 0 HIGH")
        print(f"   - {result.medium_count} MEDIUM (informational)")
        print(f"   - {result.low_count} LOW (informational)")
    else:
        print("\n❌ STATUS: ISSUES FOUND")
        print(f"   🔴 CRITICAL: {result.critical_count}")
        print(f"   🟠 HIGH: {result.high_count}")
        print(f"   🟡 MEDIUM: {result.medium_count}")
        print(f"   🟢 LOW: {result.low_count}")

    # Mostrar hallazgos
    if result.findings:
        print("\n" + "-" * 60)
        print("📋 FINDINGS:")
        print("-" * 60)

        # Ordenar por severidad
        severity_order = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3}
        sorted_findings = sorted(
            result.findings,
            key=lambda f: (severity_order.get(f.severity, 4), f.file, f.line),
        )

        for finding in sorted_findings:
            icon = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🟢"}.get(
                finding.severity, "⚪"
            )

            print(f"\n{icon} [{finding.severity}] {finding.file}:{finding.line}")
            print(f"   {finding.message}")
            if finding.code_snippet:
                print(f"   Code: {finding.code_snippet}")

    print("\n" + "=" * 60)

    # Recomendaciones
    if result.critical_count > 0 or result.high_count > 0:
        print("\n⚠️  RECOMMENDATIONS:")
        print("   1. Fix CRITICAL issues before integration")
        print("   2. Review HIGH issues manually")
        print("   3. Use environment variables for secrets")
        print("   4. Validate all user inputs")
        print("   5. Run this scan in CI/CD pipeline")

    print()


def main():
    """Función principal."""
    parser = argparse.ArgumentParser(
        description="🛡️  Skill Security Scanner v2.0",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python skill_security_scan.py --skill 01_Core/03_Skills/25_Mi_Skill
  python skill_security_scan.py --skill 01_Core/03_Skills/25_Mi_Skill --verbose
  python skill_security_scan.py --skill 01_Core/03_Skills/25_Mi_Skill --output report.txt
        """,
    )

    parser.add_argument(
        "--skill", "-s", type=str, required=True, help="Path a la skill a escanear"
    )

    parser.add_argument("--verbose", "-v", action="store_true", help="Output detallado")

    parser.add_argument("--output", "-o", type=str, help="Archivo de output (opcional)")

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Ejecutar escaneo
    scanner = SecurityScanner(args.skill)
    result = scanner.scan()

    # Generar reporte
    print_report(result)

    # Guardar a archivo si se especifica
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(f"Security Scan Report\n")
            f.write(f"Skill: {result.skill_path}\n")
            f.write(f"Critical: {result.critical_count}\n")
            f.write(f"High: {result.high_count}\n")
        logger.info(f"📄 Report saved to: {args.output}")

    # Exit code
    # CRITICAL=2, HIGH=1, CLEAN=0
    exit_code = 0 if result.is_clean else (2 if result.critical_count > 0 else 1)
    return exit_code


if __name__ == "__main__":
    main()
