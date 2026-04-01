#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sync Notes - PersonalOS v6.1
Sincroniza notas del Brain.
"""

import os
import sys
import subprocess
import glob
from datetime import datetime
from pathlib import Path

# === SETUP PATHS ===
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# === IMPORTS ===
try:
    from config_paths import (
        ROOT_DIR,
        BRAIN_DIR,
        BRAIN_RULES_DIR,
        COMPOUND_ENGINE_DIR,
        ENGINE_DIR,
        BRAIN_NOTES_DIR,
    )
except ImportError:
    ROOT_DIR = PROJECT_ROOT
    BRAIN_DIR = PROJECT_ROOT / "04_Operations"
    BRAIN_NOTES_DIR = BRAIN_DIR / "03_Process_Notes"
    BRAIN_RULES_DIR = BRAIN_DIR / "04_Memory_Brain"
    COMPOUND_ENGINE_DIR = (
        PROJECT_ROOT / "01_Core" / "03_Skills" / "00_Compound_Engineering"
    )
    ENGINE_DIR = PROJECT_ROOT / "08_Scripts_Os"

SESSIONS_DIR = BRAIN_NOTES_DIR

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
    import io

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
{Fore.CYAN}    ###########################################################################
    #                                                                         #
    #       _____ ______  _____ _____ _____ ____  _   _    _______     __ _   #
    #      / ____|  ____|/ ____/ ____|_   _/ __ \| \ | |  / ____\ \   / /| \  #
    #     | (___ | |__  | (___| (___   | || |  | |  \| | | (___  \ \_/ / |  | #
    #      \___ \|  __|  \___ \\___ \  | || |  | | . ` |  \___ \  \   /  | |  #
    #      ____) | |____ ____) |___) |_| || |__| | |\  |  ____) |  | |   | |  #
    #     |_____/|______|_____/|_____/|_____\____/|_| \_| |_____/   |_|   |_|  #
    #                                                                         #
    #                        S E S S I O N   S Y N C                          #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


def get_activity_summary():
    """Obtiene un sumario de actividad desde Git para el día actual."""
    try:
        # Obtener logs de hoy
        result = subprocess.run(
            ["git", "log", "--since", "midnight", "--pretty=format:- %s"],
            capture_output=True,
            text=True,
            cwd=PROJECT_ROOT,
        )
        if result.returncode == 0 and result.stdout:
            return result.stdout.strip()
        return "- No se detectaron commits recientes en Git."
    except Exception as e:
        return f"- Error extrayendo actividad: {e}"


def sync_session_notes():
    """Actualiza o crea la nota de sesión del día con sumario premium."""
    print_banner()
    dynamic_speak("Sincronizando notas de sesión")

    print(f"\n{Fore.CYAN}{'=' * 75}")
    print(f"🔄  SESSION SYNC - {datetime.now().strftime('%d/%m/%Y')}")
    print(f"{'=' * 75}{Style.RESET_ALL}")

    if not os.path.exists(SESSIONS_DIR):
        print(f"{Fore.RED}Error: No se encuentra {SESSIONS_DIR}{Style.RESET_ALL}")
        return False

    today = datetime.now().strftime("%Y-%m-%d")
    # Buscar nota de hoy (formato XX_Nombre_YYYY-MM-DD.md o similar)
    current_session_file = None
    # Prioridad 1: Buscar archivo que contenga "Session_Note" y la fecha de hoy
    for f in glob.glob(os.path.join(SESSIONS_DIR, "*Session_Note*.md")):
        if today in os.path.basename(f):
            current_session_file = f
            break

    # Prioridad 2: Buscar cualquier archivo con la fecha de hoy (fallback)
    if not current_session_file:
        for f in glob.glob(os.path.join(SESSIONS_DIR, "*.md")):
            if today in os.path.basename(f):
                current_session_file = f
                break

    if not current_session_file:
        print(
            f"{Fore.CYAN}Creando nueva nota de sesión para {today}...{Style.RESET_ALL}"
        )
        # Encontrar el siguiente índice
        existing_notes = glob.glob(os.path.join(SESSIONS_DIR, "[0-9][0-9]_*.md"))
        next_idx = len(existing_notes) + 1
        filename = f"{next_idx:02d}_Session_Note_{today}.md"
        current_session_file = os.path.join(SESSIONS_DIR, filename)

        with open(current_session_file, "w", encoding="utf-8") as sf:
            sf.write(
                f"# 📝 Sesión de Trabajo: {today}\n\n## 🎯 Objetivos del Día\n- \n\n## 📝 Sumario de Actividad\n\n## 🛡️ Estado del Sistema\n- [ ] Pure Green Check\n"
            )

    # Leer contenido actual
    try:
        with open(current_session_file, "r", encoding="utf-8") as f:
            content = f.read()

        activity = get_activity_summary()
        timestamp = datetime.now().strftime("%H:%M:%S")

        # Inyectar o actualizar el sumario
        summary_header = "## 📝 Sumario de Actividad"
        if summary_header in content:
            # Reemplazar hasta la siguiente sección o final
            parts = content.split(summary_header)
            after_part = parts[1].split("##")[1] if "##" in parts[1] else ""
            new_content = parts[0] + summary_header + "\n\n" + activity + "\n\n"
            if after_part:
                new_content += "##" + after_part
        else:
            new_content = content + f"\n\n{summary_header}\n\n" + activity

        # Pie de página de sincronización
        sync_stamp = f"\n\n---\n_Sincronizado automáticamente por PersonalOS Engine a las {timestamp}_"
        if "Sincronizado automáticamente" in new_content:
            new_content = new_content.split("---\n_Sincronizado")[0]

        with open(current_session_file, "w", encoding="utf-8") as f:
            f.write(new_content.strip() + sync_stamp)

        print(
            f"{Fore.GREEN}[OK] Nota de sesión sincronizada: {os.path.basename(current_session_file)}{Style.RESET_ALL}"
        )
        dynamic_speak("Sincronización de notas completada.")
        return True

    except Exception as e:
        print(f"{Fore.RED}[ERR] Fallo en la sincronización: {e}{Style.RESET_ALL}")
        dynamic_speak("Error en la sincronización")
        return False


if __name__ == "__main__":
    success = sync_session_notes()
    sys.exit(0 if success else 1)
