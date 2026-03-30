#!/usr/bin/env python3
"""
01_Context_Manager.py — Anthropic Context Manager

Gestiona la decisión entre Context Reset vs Context Compaction según el modelo.
Basado en el artículo de Anthropic sobre harness design para agentes de larga duración.

VERSIÓN: 1.0
 fecha: 2026-03-26
 FILOSOFÍA: "No te traiciones, no te abandones" — Siempre lo correcto

REFERENCIA: 01_Core/02_Knowledge_Brain/10_Anthropic_Harness_Design.md
"""

import os
import json
from enum import Enum
from dataclasses import dataclass
from typing import Optional

# ========================
# MODEL CONFIGURATION
# ========================


class ModelType(Enum):
    """Tipos de modelo Claude"""

    OPUS_46 = "opus-4-6"
    OPUS_45 = "opus-4-5"
    SONNET_45 = "sonnet-4-5"
    SONNET = "sonnet"
    HAICU = "haiku"

    @property
    def needs_context_reset(self) -> bool:
        """¿El modelo necesita context reset?"""
        return self in [ModelType.SONNET_45, ModelType.SONNET]

    @property
    def context_window(self) -> int:
        """Ventana de contexto en tokens"""
        windows = {
            ModelType.OPUS_46: 1000000,  # 1M tokens
            ModelType.OPUS_45: 200000,  # 200K tokens
            ModelType.SONNET_45: 200000,
            ModelType.SONNET: 200000,
            ModelType.HAICU: 200000,
        }
        return windows.get(self, 200000)

    @property
    def has_context_anxiety(self) -> bool:
        """¿El modelo muestra context anxiety?"""
        return self.needs_context_reset


@dataclass
class ContextState:
    """Estado del contexto"""

    current_tokens: int
    threshold_percentage: float = 0.80  # 80% de la ventana

    @property
    def usage_percentage(self) -> float:
        return self.current_tokens / 200000  # Asumiendo 200K base

    @property
    def should_reset(self) -> bool:
        return self.usage_percentage >= self.threshold_percentage

    @property
    def should_compact(self) -> bool:
        return 0.50 <= self.usage_percentage < self.threshold_percentage


class ContextManager:
    """Gestor de contexto basado en Anthropic patterns"""

    def __init__(self, model: ModelType = None):
        self.model = model or self._detect_model()
        self.state: Optional[ContextState] = None

    def _detect_model(self) -> ModelType:
        """Detecta el modelo actual desde el entorno"""
        model_env = os.getenv("CLAUDE_MODEL", "").lower()

        if "opus-4-6" in model_env or "opus 4.6" in model_env:
            return ModelType.OPUS_46
        elif "opus-4-5" in model_env or "opus 4.5" in model_env:
            return ModelType.OPUS_45
        elif "sonnet-4-5" in model_env or "sonnet 4.5" in model_env:
            return ModelType.SONNET_45
        elif "sonnet" in model_env:
            return ModelType.SONNET
        elif "haiku" in model_env:
            return ModelType.HAICU
        else:
            # Default: assume latest Opus (best performance)
            return ModelType.OPUS_46

    def update_tokens(self, token_count: int):
        """Actualiza el conteo de tokens"""
        self.state = ContextState(current_tokens=token_count)

    def analyze(self) -> dict:
        """
        Analiza el contexto y retorna recomendación.

        Returns:
            dict con:
                - action: "reset" | "compact" | "continue"
                - reason: explicación
                - model: modelo detectado
                - anxiety_level: nivel de ansiedad
        """
        if self.state is None:
            return {
                "action": "continue",
                "reason": "No context data available",
                "model": self.model.value,
                "anxiety_level": "unknown",
            }

        # Análisis basado en Anthropic article
        usage = self.state.usage_percentage

        if self.model.has_context_anxiety:
            # Sonnet 4.5: context anxiety presente
            if self.state.should_reset:
                return {
                    "action": "reset",
                    "reason": f"Sonnet 4.5 shows context anxiety at {usage:.0%} usage. "
                    "Reset required to prevent premature completion.",
                    "model": self.model.value,
                    "anxiety_level": "HIGH",
                }
            elif self.state.should_compact:
                return {
                    "action": "compact",
                    "reason": f"Sonnet 4.5 approaching threshold. Compaction recommended.",
                    "model": self.model.value,
                    "anxiety_level": "MEDIUM",
                }
        else:
            # Opus 4.5/4.6: sin context anxiety
            if self.state.should_reset:
                return {
                    "action": "compact",  # Opus puede compactar, no reset
                    "reason": f"Opus 4.6 at {usage:.0%} - can use compaction instead of reset.",
                    "model": self.model.value,
                    "anxiety_level": "NONE",
                }

        return {
            "action": "continue",
            "reason": f"Context at {usage:.0%} - healthy range for {self.model.value}",
            "model": self.model.value,
            "anxiety_level": "NONE" if not self.model.has_context_anxiety else "LOW",
        }

    def get_recommendation(self) -> str:
        """Retorna recomendación en formato legible"""
        analysis = self.analyze()

        lines = [
            f"\n{'=' * 60}",
            "🦾 CONTEXT MANAGER - ANTHROPIC PATTERN",
            f"{'=' * 60}",
            f"📊 Model: {analysis['model']}",
            f"⚡ Action: {analysis['action'].upper()}",
            f"📈 Anxiety Level: {analysis['anxiety_level']}",
            f"💡 Reason: {analysis['reason']}",
            f"{'=' * 60}\n",
        ]

        return "\n".join(lines)

    def should_invoke_evaluator(self) -> bool:
        """
        Basado en el artículo, decide si debe invocarse el Evaluator.
        Anthropic encontró que:
        - Para tareas difíciles: Necesitás evaluator
        - Para tareas easy: No necesitás evaluator

        Esto es una heurística inicial - ajustar según experiencia.
        """
        if self.state is None:
            return False

        # Si el contexto está muy usado, el modelo puede intentar terminar temprano
        # En ese caso, un evaluator externo ayuda
        return self.state.usage_percentage >= 0.60


def run_context_manager(token_count: int = None) -> dict:
    """
    Función principal para ejecutar el Context Manager.

    Usage:
        from 01_Context_Manager import run_context_manager

        result = run_context_manager(token_count=80000)
        # result = {'action': 'compact', 'reason': '...', 'model': 'opus-4-6', 'anxiety_level': 'NONE'}
    """
    print("\n🧠 Inicializando Context Manager...")

    # Obtener token count si no se provee
    if token_count is None:
        # Intentar detectar desde el entorno
        env_tokens = os.getenv("CONTEXT_TOKEN_COUNT")
        token_count = int(env_tokens) if env_tokens else 0

    # Inicializar manager
    manager = ContextManager()

    # Actualizar estado
    if token_count > 0:
        manager.update_tokens(token_count)

    # Análisis
    print(manager.get_recommendation())

    # Retornar análisis
    return manager.analyze()


if __name__ == "__main__":
    # Demo
    print("\n🔬 Testing Context Manager with different scenarios:\n")

    scenarios = [
        ("Opus 4.6 - 50%", 100000),
        ("Opus 4.6 - 85%", 170000),
        ("Sonnet 4.5 - 50%", 100000),
        ("Sonnet 4.5 - 85%", 170000),
    ]

    for name, tokens in scenarios:
        print(f"\n--- {name} ---")
        # Simular cambio de modelo
        os.environ["CLAUDE_MODEL"] = "opus-4-6" if "Opus" in name else "sonnet-4-5"
        result = run_context_manager(token_count=tokens)
        print(f"→ Action: {result['action']}")
