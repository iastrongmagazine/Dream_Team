#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Clean System - PersonalOS v6.1
Limpia el sistema de archivos temporales.
"""

import os
import sys
import io
import subprocess
import glob
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
{Fore.GREEN}    ###########################################################################
    #                                                                         #
    #       _____ _      ______          _   _    _____                      #
    #      / ____| |    |  ____|   /\   | \ | |  / ____|     /\              #
    #     | |    | |    | |__     /  \  |  \| | | (___      /  \             #
    #     | |    | |    |  __|   / /\ \ | . ` |  \___ \    / /\ \            #
    #     | |____| |____| |____ / ____ \| |\  |  ____) |  / ____ \           #
    #      \_____|______|______/_/    \_\_| \_| |_____/  /_/    \_\          #
    #                                                                         #
    #                        C L E A N   S Y S T E M                          #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


ROOT_DIR = PROJECT_ROOT


def clean_file(path):
    """Limpia un archivo específico eliminando espacios y saltos de línea extra."""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    # Remove trailing whitespace and ensure single newline at end
    new_lines = [line.rstrip() for line in lines]
    content = "\n".join(new_lines).strip() + "\n"

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Cleaned: {path}")


def main():
    """Función principal para iterar y limpiar archivos del sistema."""
    print_banner()
    dynamic_speak("Iniciando limpieza profunda del sistema")

    target_dir = ROOT_DIR
    for ext in ["*.py", "*.md", "*.sh", "*.json", "*.xml"]:
        # Búsqueda recursiva usando glob
        pattern = os.path.join(target_dir, "**", ext)
        for p in glob.glob(pattern, recursive=True):
            if any(
                x in p
                for x in ("__pycache__", ".venv", ".git", "node_modules", ".cursor")
            ):
                continue
            clean_file(p)


if __name__ == "__main__":
    main()
