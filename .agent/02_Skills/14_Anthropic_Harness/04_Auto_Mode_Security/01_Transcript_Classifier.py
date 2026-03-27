"""
Auto Mode Security - Transcript Classifier
Clasifica acciones del agente contra criterios de decisión.

Inspirado en: Claude Code auto mode article (Mar 25, 2026)
"""

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Any
import json


class RiskLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class Decision(Enum):
    APPROVE = "APPROVE"
    DENY = "DENY"
    CONFIRM = "CONFIRM"
    BLOCK = "BLOCK"


@dataclass
class ClassificationResult:
    risk_level: RiskLevel
    decision: Decision
    confidence: float
    reasons: List[str]
    suggestions: List[str]


class TranscriptClassifier:
    """
    Clasifica acciones del agente según nivel de riesgo.
    """

    # Tool definitions con risk levels
    TOOL_RISK_MAP: Dict[str, RiskLevel] = {
        # READ operations - LOW risk
        "read": RiskLevel.LOW,
        "glob": RiskLevel.LOW,
        "grep": RiskLevel.LOW,
        "ls": RiskLevel.LOW,
        "pwd": RiskLevel.LOW,
        "find": RiskLevel.LOW,
        # INFORMATION - LOW risk
        "webfetch": RiskLevel.LOW,
        "websearch": RiskLevel.LOW,
        "codesearch": RiskLevel.LOW,
        "context7_query-docs": RiskLevel.LOW,
        # EDIT/WRITE - MEDIUM risk
        "write": RiskLevel.MEDIUM,
        "edit": RiskLevel.MEDIUM,
        "create": RiskLevel.MEDIUM,
        "mkdir": RiskLevel.MEDIUM,
        # EXECUTION - varies
        "bash": RiskLevel.HIGH,  # HIGH by default
        "cmd": RiskLevel.HIGH,
        "powershell": RiskLevel.HIGH,
        "shell": RiskLevel.HIGH,
        # DANGEROUS - HIGH/CRITICAL
        "rm": RiskLevel.HIGH,
        "rmdir": RiskLevel.HIGH,
        "del": RiskLevel.HIGH,
        "delete": RiskLevel.HIGH,
        "remove": RiskLevel.HIGH,
    }

    # Critical patterns que siempre deben ser bloqueados
    CRITICAL_PATTERNS = [
        r"rm\s+-rf\s+/",
        r"rm\s+-rf\s+/var",
        r"rm\s+-rf\s+/etc",
        r"format\s+",
        r"mkfs",
        r"dd\s+if=.*of=/dev/",
        r"chmod\s+-R\s+777",
        r"chown\s+-R\s+",
        ":(){ :|:& };:",  # Fork bomb
        r"curl.*\|\s*sh",
        r"wget.*\|\s*sh",
        r"eval\s+.*rm",
    ]

    def __init__(self):
        self.custom_rules: Dict[str, RiskLevel] = {}

    def classify(
        self, tool_name: str, tool_input: Dict[str, Any], context: Optional[Dict] = None
    ) -> ClassificationResult:
        """
        Clasifica una acción del agente.

        Args:
            tool_name: Nombre de la tool
            tool_input: Input de la tool
            context: Contexto adicional

        Returns:
            ClassificationResult con la clasificación
        """
        reasons = []
        suggestions = []

        # Get base risk level from tool
        base_risk = self.TOOL_RISK_MAP.get(tool_name.lower(), RiskLevel.MEDIUM)

        # Check for critical patterns in arguments
        tool_input_str = json.dumps(tool_input).lower()

        import re

        for pattern in self.CRITICAL_PATTERNS:
            if re.search(pattern, tool_input_str):
                return ClassificationResult(
                    risk_level=RiskLevel.CRITICAL,
                    decision=Decision.BLOCK,
                    confidence=0.99,
                    reasons=[f"Critical pattern detected: {pattern}"],
                    suggestions=["This action is blocked for safety"],
                )

        # Adjust based on context
        if context:
            # Check if it's a test environment
            if context.get("is_test", False) and base_risk in [
                RiskLevel.HIGH,
                RiskLevel.CRITICAL,
            ]:
                base_risk = RiskLevel.MEDIUM
                reasons.append("Reduced risk for test environment")

            # Check if it's a known safe path
            safe_paths = context.get("safe_paths", [])
            for path in safe_paths:
                if (
                    isinstance(tool_input.get("path", ""), str)
                    and path in tool_input["path"]
                ):
                    base_risk = RiskLevel.LOW
                    reasons.append(f"Known safe path: {path}")
                    break

        # Determine decision based on risk level
        if base_risk == RiskLevel.LOW:
            decision = Decision.APPROVE
        elif base_risk == RiskLevel.MEDIUM:
            decision = Decision.APPROVE
        elif base_risk == RiskLevel.HIGH:
            decision = Decision.CONFIRM
        else:  # CRITICAL
            decision = Decision.BLOCK

        # Build result
        result = ClassificationResult(
            risk_level=base_risk,
            decision=decision,
            confidence=0.85,
            reasons=reasons if reasons else ["Standard classification"],
            suggestions=suggestions
            if suggestions
            else self._get_suggestions(base_risk),
        )

        return result

    def classify_batch(self, actions: List[Dict]) -> List[ClassificationResult]:
        """
        Clasifica múltiples acciones.
        """
        results = []
        for action in actions:
            result = self.classify(
                action.get("tool", ""), action.get("input", {}), action.get("context")
            )
            results.append(result)
        return results

    def _get_suggestions(self, risk_level: RiskLevel) -> List[str]:
        """Get suggestions based on risk level."""
        if risk_level == RiskLevel.LOW:
            return ["Action approved automatically"]
        elif risk_level == RiskLevel.MEDIUM:
            return ["Action approved with logging"]
        elif risk_level == RiskLevel.HIGH:
            return ["Confirmation required before execution"]
        else:
            return ["Action blocked - too dangerous"]

    def add_custom_rule(self, tool_name: str, risk_level: RiskLevel):
        """Add custom risk rule for a tool."""
        self.custom_rules[tool_name.lower()] = risk_level
        self.TOOL_RISK_MAP[tool_name.lower()] = risk_level


# Ejemplo de uso
if __name__ == "__main__":
    classifier = TranscriptClassifier()

    # Test cases
    test_actions = [
        {"tool": "read", "input": {"filePath": "/etc/passwd"}, "context": {}},
        {"tool": "bash", "input": {"command": "rm -rf /"}, "context": {}},
        {
            "tool": "write",
            "input": {"filePath": "/tmp/test.txt", "content": "hello"},
            "context": {},
        },
    ]

    for action in test_actions:
        result = classifier.classify(action["tool"], action["input"], action["context"])
        print(f"Tool: {action['tool']}")
        print(f"  Risk Level: {result.risk_level.value}")
        print(f"  Decision: {result.decision.value}")
        print(f"  Reasons: {result.reasons}")
        print()
