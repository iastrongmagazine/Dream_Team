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
{Fore.CYAN}    ###########################################################################
    #                                                                         #
    #      __        _______ _____ _   _ ______ _____                          #
    #      \ \      / / ____|_   _| \ | |  ____|  __ \                         #
    #       \ \ /\ / / |      | | |  \| | |__  | |__) |                        #
    #        \ V  V /| |      | | | . ` |  __| |  _  /                         #
    #         \_/\_/  |____| |_| |_|\_|_|_____|_| \_\                          #
    #                                                                         #
    #                      W O R K F L O W   H U B                            #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


def dynamic_speak(text):
    print(f"{Fore.MAGENTA}🔊 [VOICE]: {text}{Style.RESET_ALL}")


def run_script(script_name):
    script_path = Path(__file__).parent / "Legacy_Backup" / script_name
    if not script_path.exists():
        print(f"{Fore.RED}[ERROR] Script no encontrado: {script_path}{Style.RESET_ALL}")
        return

    print(f"{Fore.YELLOW}[RUNNING] Ejecutando: {script_name}...{Style.RESET_ALL}")
    subprocess.run([sys.executable, str(script_path)])


def main():
    print_banner()
    parser = argparse.ArgumentParser(
        description="Hub centralizador de Workflows y Procesos."
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos de Workflows")

    # Definir subcomandos
    subparsers.add_parser(
        "brainstorm",
        help="Generación de ideas Spider (reutiliza 01_Spider_Brainstorm.py)",
    )
    subparsers.add_parser(
        "plan", help="Planificación Profesor X (reutiliza 02_Professor_X_Plan.py)"
    )
    subparsers.add_parser(
        "lfg-lite", help="Ejecución AntMan (reutiliza 06_AntMan_Lfg_Lite.py)"
    )
    subparsers.add_parser(
        "lfg-full", help="Ejecución Doctor Strange (reutiliza 07_Doc_Strange_Lfg.py)"
    )
    subparsers.add_parser(
        "avengers",
        help="Workflow completo Avengers SOTA (reutiliza 73_Avengers_Workflow_v3.py)",
    )

    args = parser.parse_args()

    # Mapeo de comandos
    cmd_map = {
        "brainstorm": "01_Spider_Brainstorm.py",
        "plan": "02_Professor_X_Plan.py",
        "lfg-lite": "06_AntMan_Lfg_Lite.py",
        "lfg-full": "07_Doc_Strange_Lfg.py",
        "avengers": "73_Avengers_Workflow_v3.py",
    }

    if args.command in cmd_map:
        dynamic_speak(f"Ejecutando workflow: {args.command}")
        run_script(cmd_map[args.command])
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
