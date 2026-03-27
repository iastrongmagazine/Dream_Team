#!/usr/bin/env python3
"""
00_Safety_Wrapper.py — Anthropic Harness Safety System

Safety Wrapper para validar no-regresión antes de ejecutar scripts de Anthropic.
Similar a pre_tool_use.py pero específico para el sistema de harness.

VERSIÓN: 1.0
 fecha: 2026-03-26
 FILOSOFÍA: "No te traiciones, no te abandones" — Siempre lo correcto
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

# ========================
# CONFIGURATION
# ========================


class SafetyConfig:
    """Configuración del Safety Wrapper"""

    # Thresholds
    MAX_TOKEN_BUDGET = 150000  # Tokens antes de warning
    MAX_FILES_AFFECTED = 50  # Files antes de warning
    MAX_CONTEXT_LENGTH = 100000  # Chars antes de context anxiety

    # Paths protegidos (no modificar nunca)
    PROTECTED_PATHS = [
        ".agent/01_Agents/00_Orchestrator.md",
        ".agent/01_Agents/01_Scope_Rule_Architect.md",
        ".agent/01_Agents/02_TDD_Test_First.md",
        ".agent/01_Agents/03_React_Test_Implementer.md",
        ".agent/01_Agents/04_React_Mentor.md",
        ".agent/01_Agents/05_Security_Auditor.md",
        ".agent/01_Agents/06_Git_Workflow_Manager.md",
        ".agent/01_Agents/07_Accessibility_Auditor.md",
        ".agent/01_Agents/08_PRD_Dashboard_Template.md",
        ".agent/01_Agents/09_Design_SOP_Document.md",
        ".agent/01_Agents/10_Workflow_Orchestrator.md",
        ".agent/01_Agents/11_AIPM_Judge.md",
        ".agent/01_Agents/12_LFG_Autonomous_Engine.md",
    ]

    # Extensiones críticas (no tocar sin confirmación)
    CRITICAL_EXTENSIONS = [".env", ".credentials", ".key", ".pem", ".cert"]

    # Modo strict (True = bloquea todo risky)
    STRICT_MODE = True

    # Log file
    LOG_FILE = ".claude/logs/harness_safety.log"


class SafetyResult:
    """Resultado de la validación de seguridad"""

    def __init__(self):
        self.passed = True
        self.warnings = []
        self.errors = []
        self.checks = {}
        self.timestamp = datetime.now().isoformat()

    def add_warning(self, check: str, message: str):
        self.warnings.append(f"[{check}] {message}")
        self.checks[check] = "WARNING"

    def add_error(self, check: str, message: str):
        self.errors.append(f"[{check}] {message}")
        self.checks[check] = "ERROR"
        self.passed = False

    def add_pass(self, check: str, message: str = "OK"):
        self.checks[check] = "PASS"

    def to_dict(self) -> dict:
        return {
            "passed": self.passed,
            "warnings": self.warnings,
            "errors": self.errors,
            "checks": self.checks,
            "timestamp": self.timestamp,
        }

    def summary(self) -> str:
        status = "✅ PASS" if self.passed else "❌ FAIL"
        lines = [f"\n{'=' * 60}"]
        lines.append(f" SAFETY WRAPPER RESULT: {status}")
        lines.append(f"{'=' * 60}")

        for check, result in self.checks.items():
            emoji = "✅" if result == "PASS" else "⚠️" if result == "WARNING" else "❌"
            lines.append(f" {emoji} {check}: {result}")

        if self.warnings:
            lines.append(f"\n⚠️  WARNINGS ({len(self.warnings)}):")
            for w in self.warnings:
                lines.append(f"    {w}")

        if self.errors:
            lines.append(f"\n❌  ERRORS ({len(self.errors)}):")
            for e in self.errors:
                lines.append(f"    {e}")

        lines.append(f"\n{'=' * 60}")
        return "\n".join(lines)


class SafetyWrapper:
    """Safety Wrapper principal"""

    def __init__(self, strict_mode: bool = None):
        self.config = SafetyConfig()
        if strict_mode is not None:
            self.config.STRICT_MODE = strict_mode

    def validate_all(self, context: dict = None) -> SafetyResult:
        """
        Ejecuta todas las validaciones de seguridad.

        Args:
            context: Diccionario con información del contexto actual

        Returns:
            SafetyResult con el resultado de la validación
        """
        result = SafetyResult()

        # Check 1: Dependencies
        self._check_dependencies(result)

        # Check 2: Protected paths
        self._check_protected_paths(result)

        # Check 3: Token budget
        self._check_token_budget(result, context)

        # Check 4: Context length
        self._check_context_length(result, context)

        # Check 5: Git status
        self._check_git_status(result)

        # Check 6: Critical files
        self._check_critical_files(result)

        # Log result
        self._log_result(result)

        return result

    def _check_dependencies(self, result: SafetyResult):
        """Verifica que las dependencias estén disponibles"""
        try:
            import anthropic

            result.add_pass("DEPENDENCIES", "Anthropic SDK available")
        except ImportError:
            result.add_error(
                "DEPENDENCIES",
                "Anthropic SDK not found - install with: pip install anthropic",
            )

        try:
            import playwright

            result.add_pass("DEPENDENCIES", "Playwright available")
        except ImportError:
            result.add_warning(
                "DEPENDENCIES", "Playwright not found - install for full QA testing"
            )

    def _check_protected_paths(self, result: SafetyResult):
        """Verifica que no se intenten modificar paths protegidos"""
        protected_found = False

        for path in self.config.PROTECTED_PATHS:
            if Path(path).exists():
                protected_found = True
                result.add_warning("PROTECTED_PATHS", f"Protected path exists: {path}")

        if not protected_found:
            result.add_pass("PROTECTED_PATHS", "No protected paths in current scope")

    def _check_token_budget(self, result: SafetyResult, context: dict = None):
        """Verifica el presupuesto de tokens"""
        if context is None:
            context = {}

        token_count = context.get("token_count", 0)

        if token_count > self.config.MAX_TOKEN_BUDGET:
            if self.config.STRICT_MODE:
                result.add_error(
                    "TOKEN_BUDGET",
                    f"Token count {token_count} exceeds max {self.config.MAX_TOKEN_BUDGET}",
                )
            else:
                result.add_warning(
                    "TOKEN_BUDGET",
                    f"Token count {token_count} exceeds max - consider context compaction",
                )
        else:
            result.add_pass("TOKEN_BUDGET", f"Tokens {token_count} within budget")

    def _check_context_length(self, result: SafetyResult, context: dict = None):
        """Detecta context anxiety"""
        if context is None:
            context = {}

        context_length = context.get("context_length", 0)

        if context_length > self.config.MAX_CONTEXT_LENGTH:
            result.add_warning(
                "CONTEXT_ANXIETY",
                f"Context length {context_length} exceeds max - model may try to finish early. "
                f"Consider using Context_Manager with Opus 4.6 or reset with Sonnet 4.5",
            )
            result.add_pass("CONTEXT_ANXIETY", "Detected - Context Manager will handle")
        else:
            result.add_pass("CONTEXT_ANXIETY", "Context healthy")

    def _check_git_status(self, result: SafetyResult):
        """Verifica el estado de git antes de ejecutar"""
        try:
            import subprocess

            result_check = subprocess.run(
                ["git", "status", "--porcelain"],
                capture_output=True,
                text=True,
                timeout=5,
            )

            if result_check.returncode == 0:
                changes = result_check.stdout.strip()
                if changes:
                    file_count = len(changes.split("\n"))
                    if file_count > self.config.MAX_FILES_AFFECTED:
                        result.add_warning(
                            "GIT_STATUS",
                            f"{file_count} uncommitted changes - review before proceeding",
                        )
                    else:
                        result.add_pass("GIT_STATUS", f"{file_count} changes pending")
                else:
                    result.add_pass("GIT_STATUS", "Working tree clean")
            else:
                result.add_warning(
                    "GIT_STATUS", "Not a git repository - running outside git"
                )
        except Exception as e:
            result.add_warning("GIT_STATUS", f"Could not check git status: {e}")

    def _check_critical_files(self, result: SafetyResult):
        """Verifica que no haya archivos críticos expuestos"""
        critical_found = False

        for ext in self.config.CRITICAL_EXTENSIONS:
            critical_files = list(Path(".").rglob(f"*{ext}"))
            if critical_files:
                critical_found = True
                result.add_warning(
                    "CRITICAL_FILES",
                    f"Found {len(critical_files)} files with {ext} extension",
                )

        if not critical_found:
            result.add_pass("CRITICAL_FILES", "No critical files exposed")

    def _log_result(self, result: SafetyResult):
        """Guarda el resultado en el log"""
        try:
            log_path = Path(self.config.LOG_FILE)
            log_path.parent.mkdir(parents=True, exist_ok=True)

            with open(log_path, "a") as f:
                f.write(json.dumps(result.to_dict()) + "\n")
        except Exception:
            pass  # Fail silently

    def validate_and_proceed(
        self, context: dict = None, auto_continue: bool = False
    ) -> bool:
        """
        Valida y decide si continuar.

        Args:
            context: Contexto actual
            auto_continue: Si True, continúa aunque haya warnings (pero no errors)

        Returns:
            True si puede proceder, False si debe detenerse
        """
        result = self.validate_all(context)

        print(result.summary())

        if not result.passed:
            print("\n❌ SAFETY CHECK FAILED - ABORTING")
            print("Fix the errors above before proceeding.")
            return False

        if result.warnings and not auto_continue:
            response = input("\n⚠️  Warnings detected. Continue? (y/n): ")
            if response.lower() != "y":
                print("Aborted by user.")
                return False

        print("\n✅ SAFETY CHECK PASSED - PROCEEDING")
        return True


def run_safety_check(script_name: str = None, context: dict = None) -> bool:
    """
    Función principal para ejecutar el safety check.

    Usage:
        from 00_Safety_Wrapper import run_safety_check

        if run_safety_check("01_Context_Manager", {"token_count": 50000}):
            # Execute your script
            pass
    """
    print(f"\n{'=' * 60}")
    print(f"🦾 ANTHROPIC HARNESS SAFETY WRAPPER")
    print(f"   Script: {script_name or 'Unknown'}")
    print(f"   Philosophy: 'No te traiciones, no te abandones'")
    print(f"{'=' * 60}")

    wrapper = SafetyWrapper()
    return wrapper.validate_and_proceed(context, auto_continue=False)


if __name__ == "__main__":
    # Si se ejecuta directamente, hacer check completo
    run_safety_check("manual_check")
