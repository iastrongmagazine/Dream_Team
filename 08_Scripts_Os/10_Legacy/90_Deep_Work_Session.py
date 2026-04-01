#!/usr/bin/env python3
"""
90_Deep_Work_Session.py — Deep Work Session Workflow Automation
Sesión de trabajo profundo con checkpoints de energía y foco total.
Basado en: .agent/03_Workflows/15_Deep_Work_Session.md
"""

import os
import sys
import io
import subprocess
import time
from pathlib import Path
from datetime import datetime, timedelta

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
    #       _______           _                                                #
    #      |__   __|         | |                                               #
    #         | |  ___  _ __ | |_  _   _  _ __  ___                           #
    #         | | / _ \| '_ \| __|| | | || '__|/ _ \                          #
    #         | ||  __/| | | | |_ | |_| || |  |  __/                          #
    #         |_| \___||_| |_|\__| \__,_||_|   \___|                          #
    #                                                                         #
    #     ________                 ____                                        #
    #    |  ____  |               / __ \                                        #
    #    | |    | | ___  _   _   | |  | | ___  _ __ ___   ___  _ __           #
    #    | |    | || __|| | | |  | |  | |/ _ \| '_ ` _ \ / _ \| '_ \          #
    #    | |____| || |_ | |_| |  | |__| |  __/| | | | | |  __/| | | |         #
    #    |________| \__| \__,_|   \____/ \___||_| |_| |_|\___||_| |_|         #
    #                                                                         #
    #           🎯 DEEP WORK — Foco Total · Sin Interrupciones                #
    #                   Pomodoro · Flow State · Checkpoints                   #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


# =============================================================================
# CONFIGURATION
# =============================================================================

WORK_TYPES = {
    "writing": {
        "name": "Escritura / Documentación",
        "duration": 45,  # minutos
        "break_duration": 5,
        "break_type": "caminar, agua, sin pantalla",
    },
    "design": {
        "name": "Diseño UX/UI",
        "duration": 60,
        "break_duration": 10,
        "break_type": "estirar, mirar a distancia",
    },
    "coding": {
        "name": "Programación / Scripts",
        "duration": 90,
        "break_duration": 10,
        "break_type": "caminar, agua, estirar",
    },
    "learning": {
        "name": "Aprendizaje (Python/English)",
        "duration": 45,
        "break_duration": 5,
        "break_type": "repasar notas, agua",
    },
    "review": {
        "name": "Review + Revisión",
        "duration": 30,
        "break_duration": 5,
        "break_type": "reset visual, agua",
    },
}

ENERGY_LEVELS = {
    "green": {"emoji": "🟢", "label": "Verde", "action": "Flujo alto — seguir"},
    "yellow": {
        "emoji": "🟡",
        "label": "Amarillo",
        "action": "Algo de fricción — ajustar approach",
    },
    "red": {
        "emoji": "🔴",
        "label": "Rojo",
        "action": "Energía baja — pausa larga o cambiar",
    },
}


# =============================================================================
# FUNCTIONS
# =============================================================================


def print_duration_table():
    """Muestra tabla de duraciones recomendadas."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("⏱️ DURACIONES RECOMENDADAS")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    print(f"\n  {'Tipo de trabajo':<30} {'Duración':<15} {'Pausa'}")
    print(f"  {'-' * 60}")
    for key, value in WORK_TYPES.items():
        print(
            f"  {value['name']:<30} {value['duration']} min{' ':>10} {value['break_duration']} min"
        )


def print_session_protocol():
    """Muestra el protocolo de sesión (antes de empezar)."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("📋 PROTOCOLO PRE-SESIÓN (2 min)")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    print(f"""
  {Fore.GREEN}1. Definir la sesión{Style.RESET_ALL}
     Responder estas 3 preguntas:

     • {Fore.MAGENTA}¿Cuál es el único output de esta sesión?{Style.RESET_ALL}
       → Específico, no vago

     • {Fore.MAGENTA}¿Cómo sabré que terminé?{Style.RESET_ALL}
       → Criterio de done claro

     • {Fore.MAGENTA}¿Qué necesito tener abierto?{Style.RESET_ALL}
       → Solo lo necesario

  {Fore.GREEN}2. Preparar el contexto{Style.RESET_ALL}
     python 04_Engine/14_Morning_Standup.py   # Ver prioridades
     git status                                # Estado limpio

  {Fore.GREEN}3. Cerrar lo que distrae{Style.RESET_ALL}
     • Silenciar notificaciones
     • Cerrar tabs irrelevantes
     • Música instrumental si ayuda
""")


def print_workflow_blocks(work_type_key):
    """Muestra el flujo de bloques de trabajo."""
    work_type = WORK_TYPES.get(work_type_key, WORK_TYPES["coding"])

    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print(f"⏳ BLOQUES DE TRABAJO — {work_type['name']}")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    print(f"""
  Configuración:
    • Trabajo: {work_type["duration"]} min
    • Pausa: {work_type["break_duration"]} min ({work_type["break_type"]})
    • Repetir hasta completar

  Flujo:
    ┌─────────────────────────────────────┐
    │  [{work_type["duration"]:>2} min] Trabajo profundo              │
    │       ↓                             │
    │  [{work_type["break_duration"]:>2} min] Pausa activa                   │
    │       ↓                             │
    │  [Repetir]                          │
    └─────────────────────────────────────┘
""")


def print_energy_checkpoint():
    """Muestra el checkpoint de energía."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("⚡ CHECKPOINT DE ENERGÍA (al finalizar cada bloque)")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    for level, info in ENERGY_LEVELS.items():
        color = {"green": Fore.GREEN, "yellow": Fore.YELLOW, "red": Fore.RED}[level]
        print(
            f"  {color}{info['emoji']} {info['label']}{Style.RESET_ALL}: {info['action']}"
        )


def print_distraction_capture():
    """Muestra protocolo de captura de distracciones."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("🎯 REGLA DE CAPTURA DE DISTRACCIONES")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    print(f"""
  Si surge una idea o tarea nueva:

    1. {Fore.MAGENTA}NO proceses{Style.RESET_ALL} — solo captura
    2. Escribe en BACKLOG.md (workflow 14: Captura Rápida)
    3. {Fore.GREEN}Sigue trabajando{Style.RESET_ALL}

  Regla: Captura sin interrumpir el flujo.
""")


def print_closing_protocol():
    """Muestra el protocolo de cierre."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("🏁 CIERRE DE SESIÓN (5 min)")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    print(f"""
  1. {Fore.GREEN}Documentar{Style.RESET_ALL}
     → ¿Qué logré? ¿Qué quedó pendiente?
     → Guardar en 01_Brain/03_Process_Notes/

  2. {Fore.GREEN}Commit{Style.RESET_ALL}
     → Si hay código → commit atómico descriptivo

  3. {Fore.GREEN}Actualizar tarea{Style.RESET_ALL}
     → Cambiar status en 02_Operations/01_Active_Tasks/

  4. {Fore.GREEN}Captura de aprendizajes{Style.RESET_ALL}
     → ¿Qué aprendí hoy que vale la pena guardar?

  5. {Fore.MAGENTA}Cierre ritual{Style.RESET_ALL}
     → python 04_Engine/08_Ritual_Cierre.py (si es fin de día)
""")


def print_learning_sprints():
    """Muestra sprints específicos para aprendizaje."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("📚 SPRINTS DE APRENDIZAJE")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    print(f"""
  {Fore.GREEN}Python Sprint (45 min){Style.RESET_ALL}
    [0-5 min]   Revisar qué quiero aprender/construir hoy
    [5-35 min]  Escribir código, experimentar, romper cosas
    [35-45 min] Documentar en 03_Knowledge/02_Notes_Brain/

  {Fore.GREEN}English Session (45 min){Style.RESET_ALL}
    [0-10 min]  Input: Leer/escuchar contenido en inglés
    [10-30 min] Output: Escribir párrafo, resumir, documentar
    [30-45 min] Revisión: Mejorar con Claude como tutor
""")


def run_session_timer(duration_minutes):
    """Ejecuta un timer de sesión (simulado)."""
    print(f"\n{Fore.GREEN}{'=' * 60}{Style.RESET_ALL}")
    print(f"⏱️ INICIANDO SESIÓN — {duration_minutes} minutos")
    print(f"{Fore.GREEN}{'=' * 60}{Style.RESET_ALL}")

    print(f"\n  {Fore.YELLOW}Para detener: Ctrl+C{Style.RESET_ALL}")
    print(f"  Sesión iniciada: {datetime.now().strftime('%H:%M:%S')}")
    print(
        f"  Sesión termina:  {(datetime.now() + timedelta(minutes=duration_minutes)).strftime('%H:%M:%S')}"
    )

    dynamic_speak(f"Iniciando sesión de {duration_minutes} minutos. Enfócate.")

    print(
        f"\n  {Fore.GREEN}[TIP] Trabaja en tu editor. Este timer muestra el horario de fin.{Style.RESET_ALL}"
    )
    print(
        f"  {Fore.MAGENTA}[CHECKPOINT] Cada {min(45, duration_minutes // 2)} min, evalúa tu energía: verde, amarillo o rojo.{Style.RESET_ALL}"
    )


def main():
    """Ejecuta el workflow Deep Work Session."""
    print_banner()
    dynamic_speak("Iniciando Deep Work Session")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{Fore.MAGENTA}🕐 Sesión iniciada: {timestamp}{Style.RESET_ALL}")

    # Mostrar duraciones
    print_duration_table()

    # Protocolo pre-sesión
    print_session_protocol()

    # Bloques de trabajo (coding por default)
    print_workflow_blocks("coding")

    # Checkpoint de energía
    print_energy_checkpoint()

    # Captura de distracciones
    print_distraction_capture()

    # Protocolo de cierre
    print_closing_protocol()

    # Sprints de aprendizaje
    print_learning_sprints()

    # Iniciar timer (45 min por default)
    run_session_timer(45)

    print(f"\n{Fore.GREEN}{'=' * 60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}🎯 DEEP WORK — Listo para enfocarte{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'=' * 60}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()
