#!/usr/bin/env python3
"""
89_Redaccion_de_Docs.py — Strategy Memo Workflow Automation
Genera memos estratégicos siguiendo el template FocusFlow.
Basado en: .agent/03_Workflows/09_Redaccion_de_Docs.md
"""

import os
import sys
import io
import subprocess
from pathlib import Path
from datetime import datetime

try:
    from colorama import init, Fore, Style

    init()
except ImportError:

    class Fore:
        GREEN = YELLOW = RED = CYAN = MAGENTA = BLUE = ""

    class Style:
        RESET_ALL = ""


# =============================================================================
# ARMOR LAYER - PATH RESOLUTION (3-LEVEL)
# =============================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


def dynamic_speak(text):
    """Interfaz de Voz SOTA v2.2"""
    print(f"{Fore.MAGENTA}🔊 [VOICE]: {text}{Style.RESET_ALL}")
    if sys.platform == "win32":
        try:
            cmd = f"PowerShell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}')\""
            subprocess.Popen(
                cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
        except:
            pass


def print_banner():
    banner = rf"""
{Fore.GREEN}    ###########################################################################
    #                                                                         #
    #      _____       _         ____              _                           #
    #     |  __ \     | |       |  _ \            | |                          #
    #     | |__) |_ _ | |_   _  | |_) | ___  _ __ | |__   __ _ _ __           #
    #     |  _  / _` || | | | | |  _ < / _ \| '_ \| '_ \ / _` | '_ \          #
    #     | | \ \ (_| || | |_| | | |_) | (_) | | | | |_) | (_| | | | |         #
    #     |_|  \_\__,_|_|\__, | |____/ \___/|_| |_|_.__/ \__,_|_| |_|         #
    #                      __/ |                                               #
    #                     |___/          STRATEGY MEMO GENERATOR                #
    #                                                                         #
    #               Problem · Vision · Principles · Goals · Solution           #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


# =============================================================================
# MEMO TEMPLATE STRUCTURE
# =============================================================================

MEMO_TEMPLATE = {
    "problem": {
        "title": "### Problema",
        "description": "Máximo 2-3 frases. Define el punto de dolor principal del cliente.",
        "instructions": [
            "Incluye 1-2 citas directas de clientes/usuarios",
            "Evita listar demasiados problemas",
            "Elige el más crítico",
        ],
        "example": "Los profesionales sufren de 'fatiga por lista de tareas', donde tener 50 ítems pendientes genera ansiedad en lugar de productividad.",
    },
    "vision": {
        "title": "### Visión",
        "description": "1 frase. Declaración clara y aspiracional del éxito.",
        "instructions": [
            "Debe ser memorable",
            "Debe ser diferenciada",
            "Inspira acción",
        ],
        "example": "Ser el sistema operativo que ayuda a las personas a terminar su jornada con una sensación de logro real.",
    },
    "principles": {
        "title": "### Principios",
        "description": "Máximo 3 puntos. Creencias no negociables que guían decisiones.",
        "instructions": [
            "Cada uno debe implicar qué estás dispuesto a sacrificar",
            "Son las reglas del juego",
            "Guían los trade-offs",
        ],
        "example": [
            "Menos es más: Preferimos que el usuario complete 3 tareas críticas a que marque 10 irrelevantes.",
            "Contexto sobre volumen: Priorizamos qué hacer ahora, sacrificando la vista general abrumadora.",
        ],
    },
    "goals": {
        "title": "### Objetivos",
        "description": "Una métrica de resultado + 2-4 métricas de entrada.",
        "instructions": [
            "Output: El resultado final que te importa",
            "Inputs: Las palancas que puedes influenciar directamente",
            "Mantente enfocado — no más de 5 métricas total",
        ],
        "output_example": "Tasa de finalización de tareas marcadas como 'Prioridad del Día' (Aumento del 40%)",
        "input_examples": [
            "Número de sesiones de Deep Work iniciadas por semana",
            "Promedio de tareas añadidas vs. completadas (ratio de balance)",
            "Tiempo promedio en lista de 'Hoy'",
        ],
    },
    "solution": {
        "title": "### Solución",
        "description": "Máximo 3-4 iniciativas clave.",
        "instructions": [
            "Cada iniciativa aborda directamente el problema",
            "Se alinea con los principios",
            "Incluye suficiente detalle para ser concreto",
            "No tanto como para ser un spec técnico",
        ],
        "examples": [
            "Motor de Priorización Sugerida (IA)",
            "Modo Deep Work Integrado",
            "Reflexión de Cierre de Jornada",
        ],
    },
    "not_prioritizing": {
        "title": "### Qué NO estamos priorizando",
        "description": "2-4 puntos. Evita scope creep y demuestra claridad estratégica.",
        "instructions": [
            "Sé explícito sobre lo que queda fuera",
            "Esta sección revela más tu estrategia que la solución",
            "Previene expectativas falsas",
        ],
        "examples": [
            "Colaboración compleja de equipos — enfocamos en ejecución individual",
            "Integraciones masivas — solo calendario y correo",
            "Gamificación excesiva — sin puntos ni rachas de presión",
        ],
    },
}


# =============================================================================
# FUNCTIONS
# =============================================================================


def print_template_overview():
    """Muestra overview del template de memo."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("📋 PLANTILLA DE MEMO ESTRATÉGICO")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    print(f"""
  {Fore.GREEN}Estructura FocusFlow:{Style.RESET_ALL}

    1. {Fore.MAGENTA}Problema{Style.RESET_ALL}        → Máx 2-3 frases + citas reales
    2. {Fore.MAGENTA}Visión{Style.RESET_ALL}          → 1 frase memorable
    3. {Fore.MAGENTA}Principios{Style.RESET_ALL}      → Máx 3 no negociables
    4. {Fore.MAGENTA}Objetivos{Style.RESET_ALL}       → 1 output + 2-4 inputs
    5. {Fore.MAGENTA}Solución{Style.RESET_ALL}        → 3-4 iniciativas clave
    6. {Fore.MAGENTA}No Priorizado{Style.RESET_ALL}   → 2-4 bullets de alcance
""")


def print_section_guide(section_key):
    """Imprime guía detallada para una sección."""
    section = MEMO_TEMPLATE.get(section_key)
    if not section:
        print(f"{Fore.RED}[ERR] Sección no encontrada: {section_key}{Style.RESET_ALL}")
        return

    print(f"\n{Fore.GREEN}{section['title']}{Style.RESET_ALL}")
    print(f"  {section['description']}")
    print(f"\n  {Fore.YELLOW}Instrucciones:{Style.RESET_ALL}")
    for instr in section["instructions"]:
        print(f"    • {instr}")

    if "example" in section:
        if isinstance(section["example"], list):
            print(f"\n  {Fore.CYAN}Ejemplos:{Style.RESET_ALL}")
            for ex in section["example"]:
                print(f"    - {ex}")
        else:
            print(f"\n  {Fore.CYAN}Ejemplo:{Style.RESET_ALL}")
            print(f'    "{section["example"]}"')

    if "output_example" in section:
        print(f"\n  {Fore.CYAN}Output Example:{Style.RESET_ALL}")
        print(f"    {section['output_example']}")
    if "input_examples" in section:
        print(f"\n  {Fore.CYAN}Input Examples:{Style.RESET_ALL}")
        for ex in section["input_examples"]:
            print(f"    • {ex}")


def generate_memo_template():
    """Genera el template completo listo para llenar."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("📝 TEMPLATE GENERADO (copiar y llenar)")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    template = f"""
# Memo Estratégico

**Fecha:** {datetime.now().strftime("%Y-%m-%d")}
**Autor:** [Tu nombre]
**Tema:** [Tema del memo]

---

## Problema
[2-3 frases sobre el punto de dolor principal]

> "[Cita directa del cliente/usuario]"

## Visión
[1 frase memorable y aspiracional]

## Principios
1. **[Principio 1]:** [Qué implica / qué sacrificas]
2. **[Principio 2]:** [Qué implica / qué sacrificas]
3. **[Principio 3]:** [Qué implica / qué sacrificas]

## Objetivos
* **Output:** [Métrica de éxito principal]
* **Inputs:**
  * [Indicador 1]
  * [Indicador 2]
  * [Indicador 3]

## Solución

### [Iniciativa 1]
[Descripción — suficiente detalle para ser concreto]

### [Iniciativa 2]
[Descripción]

### [Iniciativa 3]
[Descripción]

## Qué NO estamos priorizando
* [Item 1 — y por qué]
* [Item 2 — y por qué]
* [Item 3 — y por qué]

---
"""
    print(template)
    return template


def print_writing_tips():
    """Imprime tips de redacción estratégica."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("💡 TIPS DE REDACCIÓN")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    tips = [
        "Problema: Usa citas reales — fundamentan en la realidad",
        "Visión: Debe caber en un tweet — si es muy larga, simplifica",
        "Principios: Piensa 'qué sacrifico?' — si no implica trade-off, no es principio",
        "Objetivos: Métricas que puedas medir mañana — evita vanity metrics",
        "Solución: Máximo 4 — si necesitas más, estás en spec, no en strategy",
        "No priorizado: La parte más difícil y la más reveladora de tu estrategia",
    ]

    for i, tip in enumerate(tips, 1):
        print(f"  {i}. {tip}")


def check_existing_memos():
    """Busca memos existentes en el proyecto."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("🔍 MEMOS EXISTENTES")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    search_dirs = [
        os.path.join(PROJECT_ROOT, "03_Knowledge", "06_Writing_Content"),
        os.path.join(PROJECT_ROOT, "03_Knowledge", "13_Strategic_Plans"),
        os.path.join(PROJECT_ROOT, "01_Brain", "03_Process_Notes"),
    ]

    found = 0
    for dir_path in search_dirs:
        if os.path.isdir(dir_path):
            files = [
                f
                for f in os.listdir(dir_path)
                if f.endswith(".md")
                and ("memo" in f.lower() or "strategy" in f.lower())
            ]
            if files:
                found += len(files)
                print(f"  {Fore.GREEN}{os.path.basename(dir_path)}:{Style.RESET_ALL}")
                for f in files[:3]:
                    print(f"    - {f}")

    if found == 0:
        print(f"  {Fore.YELLOW}No se encontraron memos existentes{Style.RESET_ALL}")


def main():
    """Ejecuta el workflow de Redacción de Docs (Strategy Memo)."""
    print_banner()
    dynamic_speak("Iniciando generador de Memos Estratégicos")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{Fore.MAGENTA}🕐 Workflow iniciado: {timestamp}{Style.RESET_ALL}")

    # Mostrar overview del template
    print_template_overview()

    # Mostrar guía de cada sección
    for section_key in MEMO_TEMPLATE.keys():
        print_section_guide(section_key)

    # Generar template listo
    generate_memo_template()

    # Tips de redacción
    print_writing_tips()

    # Buscar memos existentes
    check_existing_memos()

    print(f"\n{Fore.GREEN}{'=' * 60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}📝 STRATEGY MEMO — Template listo{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'=' * 60}{Style.RESET_ALL}")

    dynamic_speak("Memo template generado — listo para escribir")


if __name__ == "__main__":
    main()
