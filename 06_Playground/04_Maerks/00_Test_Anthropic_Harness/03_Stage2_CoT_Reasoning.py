"""
Auto Mode Security - Stage 2 CoT Reasoning
Chain-of-thought reasoning para decisiones complejas.

Inspirado en: Claude Code auto mode article (Mar 25, 2026)
"""

from dataclasses import dataclass
from typing import List, Dict, Any, Optional
import json


@dataclass
class CoTResult:
    """Resultado del reasoning chain-of-thought."""

    decision: str  # "approve", "deny", "confirm"
    reasoning: List[str]
    confidence: float
    risk_score: float  # 0-1


class Stage2CoTReasoning:
    """
    Stage 2: Chain-of-thought reasoning para decisiones complejas.
    Solo se activa si Stage 1 flaggea.
    Latencia objetivo: <50ms
    """

    # Factores de riesgo
    RISK_FACTORS = {
        "destructive": 0.8,
        "network": 0.3,
        "file_modification": 0.5,
        "system_access": 0.7,
        "reversible": -0.3,
        "test_environment": -0.5,
    }

    # Safe patterns
    SAFE_PATTERNS = [
        "/tmp/",
        "/var/tmp/",
        "~/",
        "$HOME/",
    ]

    # Dangerous patterns
    DANGEROUS_PATTERNS = [
        "/etc/",
        "/var/",
        "/usr/",
        "/bin/",
        "/sbin/",
        "/root/",
        ".env",
        ".pem",
        ".key",
        "id_rsa",
    ]

    def __init__(self):
        self.decision_history: List[CoTResult] = []

    def reason(
        self, tool_name: str, tool_input: Dict[str, Any], context: Optional[Dict] = None
    ) -> CoTResult:
        """
        Realiza chain-of-thought reasoning.

        Args:
            tool_name: Nombre de la tool
            tool_input: Input de la tool
            context: Contexto adicional

        Returns:
            CoTResult con la decisión
        """
        reasoning = []
        risk_score = 0.0

        # Step 1: Analyze the action
        action = f"{tool_name}: {json.dumps(tool_input)[:100]}"
        reasoning.append(f"1. Analyzing action: {action}")

        # Step 2: Check for destructive patterns
        input_str = json.dumps(tool_input).lower()

        has_destructive = any(p in input_str for p in ["rm", "del", "remove", "delete"])
        if has_destructive:
            risk_score += self.RISK_FACTORS["destructive"]
            reasoning.append("2. Detected destructive operation (+0.8 risk)")
        else:
            reasoning.append("2. No destructive patterns detected")

        # Step 3: Check path safety
        path = tool_input.get("path", tool_input.get("filePath", ""))
        if path:
            is_safe_path = any(path.startswith(sp) for sp in self.SAFE_PATTERNS)
            is_dangerous_path = any(p in path for p in self.DANGEROUS_PATTERNS)

            if is_safe_path:
                risk_score += self.RISK_FACTORS["reversible"]
                reasoning.append(f"3. Safe path detected: {path} (-0.3 risk)")
            elif is_dangerous_path:
                risk_score += self.RISK_FACTORS["system_access"]
                reasoning.append(f"3. Dangerous path detected: {path} (+0.7 risk)")
            else:
                reasoning.append(f"3. Unknown path: {path}")

        # Step 4: Check context
        if context:
            if context.get("is_test"):
                risk_score += self.RISK_FACTORS["test_environment"]
                reasoning.append("4. Test environment detected (-0.5 risk)")

            if context.get("requires_approval"):
                risk_score += 0.3
                reasoning.append("4. Approval required by context (+0.3 risk)")

        # Step 5: Calculate final decision
        # Normalize risk_score to 0-1
        normalized_risk = max(0.0, min(1.0, risk_score))

        # Determine decision
        if normalized_risk >= 0.7:
            decision = "deny"
            confidence = 0.95
        elif normalized_risk >= 0.4:
            decision = "confirm"
            confidence = 0.85
        elif normalized_risk >= 0.2:
            decision = "approve"
            confidence = 0.80
        else:
            decision = "approve"
            confidence = 0.95

        reasoning.append(f"5. Final risk score: {normalized_risk:.2f}")
        reasoning.append(f"6. Decision: {decision} (confidence: {confidence})")

        result = CoTResult(
            decision=decision,
            reasoning=reasoning,
            confidence=confidence,
            risk_score=normalized_risk,
        )

        # Store in history
        self.decision_history.append(result)

        return result

    def get_statistics(self) -> Dict[str, Any]:
        """Get statistics from decision history."""
        if not self.decision_history:
            return {"total_decisions": 0}

        total = len(self.decision_history)
        denied = sum(1 for r in self.decision_history if r.decision == "deny")
        confirmed = sum(1 for r in self.decision_history if r.decision == "confirm")
        approved = sum(1 for r in self.decision_history if r.decision == "approve")

        avg_confidence = sum(r.confidence for r in self.decision_history) / total
        avg_risk = sum(r.risk_score for r in self.decision_history) / total

        return {
            "total_decisions": total,
            "denied": denied,
            "confirmed": confirmed,
            "approved": approved,
            "deny_rate": denied / total,
            "avg_confidence": avg_confidence,
            "avg_risk_score": avg_risk,
        }


# Ejemplo de uso
if __name__ == "__main__":
    stage2 = Stage2CoTReasoning()

    test_cases = [
        {
            "tool": "bash",
            "input": {"command": "rm -rf /tmp/test"},
            "context": {"is_test": True},
        },
        {
            "tool": "write",
            "input": {"filePath": "/etc/config.conf", "content": "test"},
            "context": {},
        },
        {"tool": "read", "input": {"filePath": "/tmp/data.txt"}, "context": {}},
    ]

    for case in test_cases:
        result = stage2.reason(case["tool"], case["input"], case.get("context"))
        print(f"Tool: {case['tool']}")
        print(f"  Decision: {result.decision}")
        print(f"  Confidence: {result.confidence}")
        print(f"  Risk Score: {result.risk_score:.2f}")
        for step in result.reasoning:
            print(f"    {step}")
        print()

    print("Statistics:")
    print(json.dumps(stage2.get_statistics(), indent=2))
