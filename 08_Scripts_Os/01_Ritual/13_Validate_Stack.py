#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Validate Stack - PersonalOS v6.1
Valida el stack tecnológico.
"""

import subprocess
import sys
import os
import io
from pathlib import Path

# === SETUP PATHS ===
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = (
    SCRIPT_DIR.parent.parent
)  # Ritual_Fixed → 08_Scripts_Os → Think_Different
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
    #      _____ _______       _____ _  __  __      __      _      _____ _____  #
    #     / ____|__   __|/\   / ____| |/ /  \ \    / /     | |    |_   _|  __ \ #
    #    | (___    | |  /  \ | |    | ' /    \ \  / /      | |      | | | |  | |#
    #     \___ \   | | / /\ \| |    |  <      \ \/ /       | |      | | | |  | |#
    #     ____) |  | |/ ____ \ |____| . \      \  /        | |____ _| |_| |__| |#
    #    |_____/   |_/_/    \_\_____|_|\_\      \/         |______|_____|_____/ #
    #                                                                         #
    #                        S T A C K   V A L I D A T O R                    #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


ROOT_DIR = PROJECT_ROOT


def check_uv():
    """Verifica que uv esté instalado."""
    try:
        result = subprocess.run(
            ["uv", "--version"], capture_output=True, text=True, check=False
        )
        if result.returncode == 0:
            print(f"[OK] uv: {result.stdout.strip()}")
            return True
        print("[ERR] uv: No encontrado")
        return False
    except FileNotFoundError:
        print("[ERR] uv: No instalado")
        return False


def check_python():
    """Verifica la versión de Python."""
    version = sys.version.split()[0]
    print(f"[OK] Python: {version}")
    return True


def check_git():
    """Verifica que git esté disponible."""
    try:
        result = subprocess.run(
            ["git", "--version"],
            capture_output=True,
            text=True,
            check=False,
            cwd=ROOT_DIR,
        )
        if result.returncode == 0:
            print(f"[OK] Git: {result.stdout.strip()}")
            return True
        print("[ERR] Git: No encontrado")
        return False
    except FileNotFoundError:
        print("[ERR] Git: No instalado")
        return False


def check_core_structure():
    """Verifica la existencia de los archivos críticos actualizados."""
    critical_files = {
        "Raíz: README.md": os.path.join(ROOT_DIR, "README.md"),
        "Raíz: CLAUDE.md": os.path.join(ROOT_DIR, "CLAUDE.md"),
        "Config: settings.local.json": os.path.join(
            ROOT_DIR, ".claude", "settings.local.json"
        ),
        "Core: Server.py": os.path.join(
            ROOT_DIR, "05_System", "01_Core", "mcp", "Server.py"
        ),
    }

    all_ok = True
    print("-" * 30)
    print("Chequeo de Estructura Personal OS")
    for name, path in critical_files.items():
        if os.path.exists(path):
            print(f"[OK] {name}")
        else:
            print(f"[ERR] {name} (No encontrado en {path})")
            all_ok = False
    print("-" * 30)
    return all_ok


def main():
    """Ejecuta todas las validaciones del stack."""
    print_banner()
    dynamic_speak("Iniciando validación del stack tecnológico")

    print(f"{Fore.CYAN}{'=' * 75}{Style.RESET_ALL}")
    print("VALIDACIÓN DEL STACK TECNOLÓGICO PersonalOS")
    print(f"{Fore.CYAN}{'=' * 75}{Style.RESET_ALL}")
    checks = [check_python(), check_uv(), check_git(), check_core_structure()]
    if all(checks):
        print(
            f"\n{Fore.GREEN}[OK] Todas las validaciones pasaron correctamente{Style.RESET_ALL}"
        )
        dynamic_speak("Validación del stack exitosa")
        sys.exit(0)
    else:
        print(f"\n{Fore.RED}[ERR] Algunas validaciones fallaron{Style.RESET_ALL}")
        dynamic_speak("Error en la validación del stack")
        sys.exit(1)


if __name__ == "__main__":
    main()
