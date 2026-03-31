#!/usr/bin/env python3
"""
Context Usage Progress Bar - OpenCode Integration
=================================================
Muestra uso de contexto con barra de progreso bloque de 10 caracteres.
Escala: 80% real = 100% (threshold de compaction de Claude)

Colores:
  - Verde: <50%
  - Amarillo: 50-65%
  - Naranja: 65-95%
  - Rojo parpadeante + 💀: >=95%

Formato: model_name | folder_name | ██████░░░ | 100%
"""

import sys
import os
import math

# ============================================================
# CONFIGURACIÓN
# ============================================================

COMPACT_THRESHOLD = 0.80  # Claude compacta al 80%
BAR_WIDTH = 10


# Colores ANSI
class Colors:
    DIM = "\033[90m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    ORANGE = "\033[38;5;208m"
    RED = "\033[91m"
    BLINK = "\033[5m"
    RESET = "\033[0m"


# ============================================================
# FUNCIONES
# ============================================================


def scale_percentage(real_percentage: float) -> float:
    """
    Escala: 80% real -> 100% mostrado
    """
    if real_percentage >= COMPACT_THRESHOLD:
        return 100.0
    return (real_percentage / COMPACT_THRESHOLD) * 100


def get_color(real_percentage: float) -> str:
    """Retorna color basado en porcentaje real"""
    if real_percentage < 0.50:
        return Colors.GREEN
    elif real_percentage < 0.65:
        return Colors.YELLOW
    elif real_percentage < 0.95:
        return Colors.ORANGE
    else:
        return Colors.RED


def get_bar_filled_blocks(percentage: float) -> int:
    """Retorna número de bloques llenos (0-10)"""
    return min(BAR_WIDTH, int((percentage / 100) * BAR_WIDTH + 0.5))


def create_progress_bar(real_percentage: float) -> str:
    """Crea barra de progreso de 10 caracteres"""
    scaled = scale_percentage(real_percentage)
    filled = get_bar_filled_blocks(scaled)
    empty = BAR_WIDTH - filled

    color = get_color(real_percentage)

    # Usar caracteres ASCII que funcionan en todos los sistemas
    bar = "#" * filled + "-" * empty

    # Si >= 95%, agregar blink + skull
    if real_percentage >= 0.95:
        bar += f" {Colors.BLINK}{Colors.RED}CRITICAL{Colors.RESET}"

    return f"{color}{bar}{Colors.RESET}"


def format_context_usage(
    model_name: str, folder_name: str, real_percentage: float
) -> str:
    """
    Formato: model_name | folder_name | ██████░░░ | 100%
    """
    scaled = scale_percentage(real_percentage)
    bar = create_progress_bar(real_percentage)

    # Dim model y folder
    display = (
        f"{Colors.DIM}{model_name:<20}{Colors.RESET} | "
        f"{Colors.DIM}{folder_name:<20}{Colors.RESET} | "
        f"{bar} | "
        f"{scaled:.0f}%"
    )

    return display


def parse_context_from_args(args: list) -> tuple:
    """
    Parsea argumentos: python context_bar.py [model] [folder] [percentage]
    """
    if len(args) < 3:
        # Demo mode
        return [
            ("opus", "hillary_life_os", 0.35),
            ("sonnet", "sdd_workflow", 0.55),
            ("haiku", "skill_audit", 0.78),
            ("opus", "deep_research", 0.96),
        ]

    model = args[0]
    folder = args[1]
    pct = float(args[2]) / 100

    return [(model, folder, pct)]


# ============================================================
# EJEMPLOS DE USO
# ============================================================


def run_demo():
    """Demo con ejemplos de diferentes niveles de uso"""

    examples = [
        ("claude-opus-3-5", "hillary_life_os", 0.35),  # 35% real = 44% scaled -> verde
        ("claude-sonnet", "sdd_apply", 0.58),  # 58% real = 73% scaled -> amarillo
        ("claude-sonnet", "skill_audit", 0.72),  # 72% real = 90% scaled -> naranja
        (
            "claude-opus",
            "research_agent",
            0.97,
        ),  # 97% real = 100% scaled -> rojo blink + 💀
    ]

    print("=" * 70)
    print(
        f"{Colors.DIM}Context Usage Progress Bar | OpenCode Integration{Colors.RESET}"
    )
    print("=" * 70)
    print(f"{Colors.DIM}Threshold compaction: 80% real = 100% shown{Colors.RESET}")
    print("-" * 70)
    print()

    for model, folder, real_pct in examples:
        print(format_context_usage(model, folder, real_pct))

    print()
    print("-" * 70)
    print(f"{Colors.DIM}Leyenda:{Colors.RESET}")
    print(
        f"  {Colors.GREEN}█{Colors.RESET} <50% | {Colors.YELLOW}█{Colors.RESET} 50-65% | {Colors.ORANGE}█{Colors.RESET} 65-95% | {Colors.RED}█ + 💀{Colors.RESET} >=95%"
    )


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--demo":
        run_demo()
    else:
        # Demo por defecto
        run_demo()
