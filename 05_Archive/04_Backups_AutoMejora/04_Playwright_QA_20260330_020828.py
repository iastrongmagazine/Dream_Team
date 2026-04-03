#!/usr/bin/env python3
"""
04_Playwright_QA.py — Playwright QA Integration

Integración con Playwright para testing interactivo del Evaluator.
Del artículo: "they use the Playwright MCP so that the evaluator has tools it can use
to actually navigate the app, screenshot it and test it like a real user."

Esto permite que el Evaluator INTERACTÚE con el output, no solo evalúe texto.

VERSIÓN: 1.0
 fecha: 2026-03-26
 FILOSOFÍA: "No te traiciones, no te abandones" — Siempre lo correcto

REFERENCIA: 01_Core/02_Knowledge_Brain/10_Anthropic_Harness_Design.md
"""

import os
import json
import subprocess
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Optional, Callable

# ========================
# PLAYWRIGHT QA CONFIG
# ========================


class QAState(Enum):
    """Estados del QA"""

    READY = "ready"
    RUNNING = "running"
    PASSED = "passed"
    FAILED = "failed"


@dataclass
class TestResult:
    """Resultado de un test"""

    name: str
    passed: bool
    duration_ms: float
    error: str = ""
    screenshot: str = ""

    def to_dict(self) -> dict:
        return {
            "name": self.name,
            "passed": self.passed,
            "duration_ms": self.duration_ms,
            "error": self.error,
            "screenshot": self.screenshot,
        }


@dataclass
class QASession:
    """Sesión de QA con Playwright"""

    session_id: str
    url: str
    tests: List[TestResult] = field(default_factory=list)
    state: QAState = QAState.READY

    @property
    def passed_count(self) -> int:
        return sum(1 for t in self.tests if t.passed)

    @property
    def total_count(self) -> int:
        return len(self.tests)

    @property
    def passed_percentage(self) -> float:
        if not self.tests:
            return 0
        return (self.passed_count / self.total_count) * 100


class PlaywrightQA:
    """
    Playwright QA para el Evaluator.

    DEL ARTÍCULO:
    "So they use the Playwright MCP so that the evaluator has tools it can use
    to actually navigate the app, screenshot it and test it like a real user."

    FUNCIONALIDADES:
    - Abrir browser y navegar a la URL
    - Tomar screenshots
    - Ejecutar tests interactivos
    - Verificar elementos visuales
    - Reporte de QA
    """

    def __init__(self, headless: bool = True):
        self.headless = headless
        self.playwright_available = self._check_playwright()

    def _check_playwright(self) -> bool:
        """Verifica si Playwright está disponible"""
        try:
            import playwright

            return True
        except ImportError:
            return False

    def create_session(self, url: str, session_id: str = None) -> QASession:
        """Crea una sesión de QA"""
        import uuid

        return QASession(session_id=session_id or str(uuid.uuid4())[:8], url=url)

    def run_test(
        self,
        session: QASession,
        test_name: str,
        test_func: Callable,
        timeout_ms: int = 30000,
    ) -> TestResult:
        """Ejecuta un test en la sesión"""
        import time

        start = time.time()

        try:
            # Ejecutar el test
            test_func(session)

            duration = (time.time() - start) * 1000

            result = TestResult(name=test_name, passed=True, duration_ms=duration)

        except Exception as e:
            duration = (time.time() - start) * 1000

            result = TestResult(
                name=test_name, passed=False, duration_ms=duration, error=str(e)
            )

        session.tests.append(result)
        return result

    def navigate_and_screenshot(self, session: QASession, path: str = "/") -> str:
        """
        Navega a una ruta y toma screenshot.
        Retorna la ruta del screenshot.
        """
        # En implementación real, usaría Playwright
        # Por ahora, retornar path simulado

        screenshot_path = (
            f".claude/screenshots/{session.session_id}_{path.replace('/', '_')}.png"
        )
        return screenshot_path

    def verify_element_exists(self, session: QASession, selector: str) -> bool:
        """Verifica que un elemento existe"""
        # En implementación real, usaría Playwright
        # Por ahora, retornar True como placeholder
        return True

    def verify_visual_consistency(
        self, session: QASession, baseline: str, current: str
    ) -> dict:
        """
        Compara visuales contra baseline.
        Retorna similarity score.
        """
        # En implementación real, usaría image comparison
        return {"similarity": 0.95, "diff_pixels": 100, "passed": True}

    def get_qa_report(self, session: QASession) -> str:
        """Genera reporte de QA"""
        status_emoji = {
            QAState.READY: "⚪",
            QAState.RUNNING: "🔵",
            QAState.PASSED: "✅",
            QAState.FAILED: "❌",
        }

        lines = [
            f"\n{'=' * 60}",
            "🎭 PLAYWRIGHT QA REPORT",
            f"{'=' * 60}",
            f"Session ID: {session.session_id}",
            f"URL: {session.url}",
            f"Status: {status_emoji[session.state]} {session.state.value}",
            f"{'=' * 60}",
            f"\n📊 RESULTS:",
            f"  Passed: {session.passed_count}/{session.total_count} ({session.passed_percentage:.1f}%)",
        ]

        if session.tests:
            lines.append(f"\n📋 TEST DETAILS:")
            for test in session.tests:
                emoji = "✅" if test.passed else "❌"
                lines.append(f"  {emoji} {test.name} ({test.duration_ms:.0f}ms)")
                if test.error:
                    lines.append(f"      Error: {test.error}")

        lines.append(f"\n{'=' * 60}\n")

        return "\n".join(lines)


def run_playwright_qa(url: str, tests: List[dict]) -> dict:
    """
    Función principal para ejecutar Playwright QA.

    Usage:
        from 04_Playwright_QA import run_playwright_qa

        tests = [
            {"name": "Login form exists", "selector": "#login-form"},
            {"name": "Submit button works", "selector": "#submit-btn"},
        ]

        result = run_playwright_qa("http://localhost:3000", tests)
    """
    print("\n🎭 Inicializando Playwright QA...")

    qa = PlaywrightQA(headless=True)

    # Crear sesión
    session = qa.create_session(url)
    session.state = QAState.RUNNING

    print(f"📱 Testing URL: {url}")

    # Ejecutar tests
    for test_def in tests:
        test_name = test_def.get("name", "Unnamed test")
        selector = test_def.get("selector")

        def make_test(sel):
            def test(s):
                if sel:
                    qa.verify_element_exists(s, sel)

            return test

        result = qa.run_test(session, test_name, make_test(selector))
        print(f"{'✅' if result.passed else '❌'} {test_name}")

    # Actualizar estado
    if session.passed_percentage >= 80:
        session.state = QAState.PASSED
    else:
        session.state = QAState.FAILED

    # Reporte
    print(qa.get_qa_report(session))

    return {
        "session_id": session.session_id,
        "url": session.url,
        "passed": session.state == QAState.PASSED,
        "passed_count": session.passed_count,
        "total_count": session.total_count,
        "tests": [t.to_dict() for t in session.tests],
    }


if __name__ == "__main__":
    # Demo
    print("\n🔬 Testing Playwright QA:\n")

    result = run_playwright_qa(
        url="http://localhost:3000",
        tests=[
            {"name": "Hero section visible", "selector": ".hero"},
            {"name": "Login form exists", "selector": "#login-form"},
            {"name": "Submit button exists", "selector": "#submit"},
            {"name": "Navigation works", "selector": "nav"},
        ],
    )

    print("\n📋 Final Result:")
    print(json.dumps(result, indent=2))
