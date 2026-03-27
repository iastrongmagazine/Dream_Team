"""
Auto Mode Security - Stage 1 Fast Filter
Filtro rápido single-token para clasificación de baja latencia.

Inspirado en: Claude Code auto mode article (Mar 25, 2026)
"""

from typing import Tuple
from dataclasses import dataclass
import re


@dataclass
class FastFilterResult:
    """Resultado del filtro rápido."""

    should_block: bool
    should_confirm: bool
    confidence: float
    reason: str


class Stage1FastFilter:
    """
    Filtro rápido single-token que decide en <10ms.
    Usa decisiones binarias basadas en reglas simples.
    """

    # Patterns que siempre deben bloquearse (single-token decision)
    ALWAYS_BLOCK = [
        r"rm\s+-rf\s+",
        r"rm\s+-R\s+",
        r"format\s+",
        r"mkfs",
        r"dd\s+if=.*of=/dev/",
        r":\(\)\s*:\s*\|",
    ]

    # Patterns que siempre requieren confirmación
    ALWAYS_CONFIRM = [
        r"^rm\s+",
        r"^del\s+",
        r"^remove\s+",
        r"^chmod\s+",
        r"^chown\s+",
        r"^kill\s+",
        r"^sudo",
        r".*\|\s*sh$",
        r".*\|\s*bash$",
    ]

    # Tools que son automáticamente safe
    AUTO_SAFE = [
        "read",
        "glob",
        "grep",
        "ls",
        "pwd",
        "find",
        "webfetch",
        "websearch",
        "codesearch",
    ]

    def __init__(self):
        self.block_patterns = [re.compile(p, re.IGNORECASE) for p in self.ALWAYS_BLOCK]
        self.confirm_patterns = [
            re.compile(p, re.IGNORECASE) for p in self.ALWAYS_CONFIRM
        ]

    def evaluate(self, tool_name: str, tool_command: str) -> FastFilterResult:
        """
        Evalúa una acción en <10ms.

        Args:
            tool_name: Nombre de la tool
            tool_command: El comando o input

        Returns:
            FastFilterResult con decisión binaria
        """
        # 1. Auto-safe tools
        if tool_name.lower() in self.AUTO_SAFE:
            return FastFilterResult(
                should_block=False,
                should_confirm=False,
                confidence=0.99,
                reason="Auto-safe tool",
            )

        # 2. Check for critical patterns
        command_str = str(tool_command)
        for pattern in self.block_patterns:
            if pattern.search(command_str):
                return FastFilterResult(
                    should_block=True,
                    should_confirm=False,
                    confidence=0.99,
                    reason="Critical pattern detected",
                )

        # 3. Check for confirmation patterns
        for pattern in self.confirm_patterns:
            if pattern.search(command_str):
                return FastFilterResult(
                    should_block=False,
                    should_confirm=True,
                    confidence=0.90,
                    reason="Confirmation required",
                )

        # 4. Default: approve with medium confidence
        return FastFilterResult(
            should_block=False,
            should_confirm=False,
            confidence=0.75,
            reason="Default approval",
        )

    def should_escalate(self, fast_result: FastFilterResult) -> bool:
        """
        Determina si debe escalar a Stage 2.

        Args:
            fast_result: Resultado del filtro rápido

        Returns:
            True si debe escalar a Stage 2
        """
        # Escalar solo cuando hay media confianza y no es bloque/crítico
        if fast_result.should_block:
            return False  # Ya bloqueado, no necesita Stage 2

        if fast_result.should_confirm:
            return True  # Confirmation, optional Stage 2

        if fast_result.confidence < 0.85:
            return True  # Baja confianza, necesita Stage 2

        return False


# Benchmark test
if __name__ == "__main__":
    import time

    filter = Stage1FastFilter()

    test_cases = [
        ("read", "filePath: /etc/passwd"),
        ("bash", "command: rm -rf /"),
        ("bash", "command: ls -la"),
        ("write", "filePath: /tmp/test.txt, content: hello"),
        ("rm", "path: /tmp/file.txt"),
    ]

    # Benchmark
    iterations = 10000
    start = time.perf_counter()

    for _ in range(iterations):
        for tool, cmd in test_cases:
            filter.evaluate(tool, cmd)

    elapsed = time.perf_counter() - start
    per_call = (elapsed / (iterations * len(test_cases))) * 1_000_000  # microseconds

    print(f"Evaluated {iterations * len(test_cases)} cases")
    print(f"Total time: {elapsed:.3f}s")
    print(f"Per call: {per_call:.2f}µs")
    print(f"Target: <10,000µs (10ms)")
    print(f"Status: {'✅ PASS' if per_call < 10000 else '❌ FAIL'}")
