#!/usr/bin/env python3
"""
93_AIPM_Hub.py — Hub centralizador de AIPM (AI Project Management)
Reutiliza scripts AIPM: 22, 23, 24, 28, 30
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
    #              ___    _____ _____  __  __                                 #
    #             /   \  |_   _|  __ \|  \/  |                                #
    #            / /_\ \   | | | |__) | \  / |                                #
    #           / ___ \ \  | | |  ___/| |\/| |                                #
    #          /_/   \_\_| |_| |_|    |_|  |_|                                #
    #                                                                         #
    #                      A I P M   H U B                                    #
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


def run_script(script_name, args=None):
    # Usamos AIPM_Fixed para los scripts corregidos
    script_path = Path(__file__).parent / "AIPM_Fixed" / script_name
    if not script_path.exists():
        print(
            f"{Fore.RED}[ERROR] Script corregido no encontrado: {script_path}{Style.RESET_ALL}"
        )
        return

    cmd = [sys.executable, str(script_path)]
    if args:
        cmd.extend(args)

    print(
        f"{Fore.YELLOW}[RUNNING] Ejecutando versión corregida: {script_name} {' '.join(args) if args else ''}...{Style.RESET_ALL}"
    )
    subprocess.run(cmd)


def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Hub centralizador de AIPM.")
    subparsers = parser.add_subparsers(dest="command", help="Comandos AIPM")

    # Definir subcomandos
    subparsers.add_parser(
        "logger", help="Logger AIPM (reutiliza 22_AIPM_Trace_Logger.py)"
    )
    subparsers.add_parser(
        "evaluator", help="Evaluador AIPM (reutiliza 23_AIPM_Evaluator.py)"
    )
    subparsers.add_parser(
        "interview", help="Entrevistador AIPM (reutiliza 24_AIPM_Interview_Sim.py)"
    )
    subparsers.add_parser(
        "control", help="Control Center AIPM (reutiliza 28_AIPM_Control_Center.py)"
    )
    subparsers.add_parser(
        "report", help="Reporte AIPM (reutiliza 30_AIPM_Consolidated_Report.py)"
    )

    args = parser.parse_args()

    # Mapeo de comandos
    cmd_map = {
        "logger": "22_AIPM_Trace_Logger.py",
        "evaluator": "23_AIPM_Evaluator.py",
        "interview": "24_AIPM_Interview_Sim.py",
        "control": "28_AIPM_Control_Center.py",
        "report": "30_AIPM_Consolidated_Report.py",
    }

    if args.command in cmd_map:
        dynamic_speak(f"Ejecutando comando AIPM: {args.command}")
        run_script(cmd_map[args.command])
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
