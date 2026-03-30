#!/usr/bin/env python3
"""
95_Validator_Hub.py — Hub centralizador de Validaciones del sistema
Reutiliza scripts de validación: 13, 40, 37, 80
"""

import argparse
import os
import sys
import io
import subprocess
from pathlib import Path

try:
    from colorama import init, Fore, Style

    init()
except ImportError:

    class Fore:
        GREEN = YELLOW = RED = CYAN = MAGENTA = BLUE = ""

    class Style:
        RESET_ALL = ""


# =============================================================================
# ARMOR LAYER - PATH RESOLUTION (2-LEVEL: Scripts -> Root)
# =============================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


def print_banner():
    banner = rf"""
{Fore.GREEN}    ###########################################################################
    #                                                                         #
    #      __      __   _     _ _      _   _ _____  ____  _____               #
    #      \ \    / /  | |   | | |    | \ | |_   _|/ __ \|  __ \              #
    #       \ \  / /_ _| |   | | |    |  \| | | | | |  | | |__) |             #
    #        \ \/ / _` | |   | | |    | . ` | | | | |  | |  _  /              #
    #         \  / (_| | |___| | |____| |\  |_| |_| |__| | | \ \              #
    #          \/ \__,_|_____|_|______|_| \_|_____|\____/|_|  \_\             #
    #                                                                         #
    #                      V A L I D A T O R   H U B                          #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


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


def run_script(script_name):
    script_path = Path(__file__).parent / "Validator_Fixed" / script_name
    if not script_path.exists():
        print(f"{Fore.RED}[ERROR] Script no encontrado: {script_path}{Style.RESET_ALL}")
        return

    print(f"{Fore.YELLOW}[RUNNING] Ejecutando: {script_name}...{Style.RESET_ALL}")
    subprocess.run([sys.executable, str(script_path)])


def main():
    print_banner()
    parser = argparse.ArgumentParser(
        description="Hub centralizador de Validaciones del sistema."
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos de Validación")

    # Definir subcomandos
    subparsers.add_parser(
        "stack", help="Validación de stack (reutiliza 13_Validate_Stack.py)"
    )
    subparsers.add_parser(
        "rules", help="Validación de reglas (reutiliza 40_Validate_Rules.py)"
    )
    subparsers.add_parser(
        "linter", help="Linter y autofix (reutiliza 37_Linter_Autofix.py)"
    )
    subparsers.add_parser(
        "edge", help="Validador de edge-cases (reutiliza 80_Edge_Case_Validator.py)"
    )
    subparsers.add_parser(
        "skills", help="Validación de skills SOTA (reutiliza skill_validator.py)"
    )
    subparsers.add_parser(
        "security", help="Security scan de skills (reutiliza skill_security_scan.py)"
    )

    args = parser.parse_args()

    # Mapeo de comandos
    cmd_map = {
        "stack": "13_Validate_Stack.py",
        "rules": "40_Validate_Rules.py",
        "linter": "37_Linter_Autofix.py",
        "edge": "80_Edge_Case_Validator.py",
        "skills": "skill_validator.py",
        "security": "skill_security_scan.py",
    }

    if args.command in cmd_map:
        dynamic_speak(f"Ejecutando validación: {args.command}")
        run_script(cmd_map[args.command])
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
