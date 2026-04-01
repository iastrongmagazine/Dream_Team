#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ritual Dominical - PersonalOS v6.1
Ritual de fin de semana.
"""

import os
import sys
import subprocess
import io
from pathlib import Path

# === SETUP PATHS ===
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# === COLOR SETUP ===
try:
    from colorama import init, Fore, Style

    init(autoreset=True)
except ImportError:

    class Fore:
        CYAN = GREEN = RED = YELLOW = MAGENTA = ""

    class Style:
        RESET_ALL = ""


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
{Fore.MAGENTA}    ###########################################################################
    #                                                                         #
    #       _____ _   _ _   _ _____           __     _______                  #
    #      / ____| | | | \ | |  __ \   /\     \ \   / / ____|     /\          #
    #     | (___ | | | |  \| | |  | | /  \     \ \_/ / |__       /  \         #
    #      \___ \| | | | . ` | |  | |/ /\ \     \   /|___ \     / /\ \        #
    #      ____) | |_| | |\  | |__| / ____ \     | |  ____) |   / ____ \       #
    #     |_____/ \___/|_| \_|_____/_/    \_\    |_| |_____/   /_/    \_\      #
    #                                                                         #
    #                        S U N D A Y   R I T U A L                        #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


ROOT_DIR = PROJECT_ROOT
WORKFLOW_DIR = SCRIPT_DIR


def run_step(name, script_name):
    """Ejecuta un paso individual del ritual."""
    print(f"\n[PersonalOS Sunday] Ejecutando: {name}...")
    script_path = os.path.join(WORKFLOW_DIR, script_name)
    if not os.path.exists(script_path):
        print(f"WARN: Script {script_name} no encontrado.")
        return

    try:
        subprocess.run([sys.executable, str(script_path)], check=True)
    except subprocess.CalledProcessError:
        print(f"ERROR: Falló {name}.")


def sunday_ritual():
    """Ejecuta la secuencia completa del ritual dominical."""
    print_banner()
    dynamic_speak("Iniciando Ritual Dominical de PersonalOS")

    print(f"\n{Fore.MAGENTA}{'=' * 75}{Style.RESET_ALL}")
    print("🌅  SUNDAY RITUAL - SESIÓN DE ALTA FRECUENCIA")
    print(f"{Fore.MAGENTA}{'=' * 75}{Style.RESET_ALL}")

    # 1. Triage de Backlog
    run_step("Triage de Backlog", "09_Backlog_Triage.py")

    # 2. Sincronización de Notas
    run_step("Sincronización de Notas", "11_Sync_Notes.py")

    # 3. Auto-sanación
    run_step("Auto-sanación de Links", "self_heal.py")

    # 4. Archivados
    run_step("Archivado de Tareas", "archive_tasks.py")

    print("\n[INFO] Ritual técnico completado.")
    print("[TIP] Di 'Haz mi ritual dominical' para el análisis estratégico con Claude.")
    print("\n--- Sistema listo para la nueva semana. ---")


if __name__ == "__main__":
    sunday_ritual()
