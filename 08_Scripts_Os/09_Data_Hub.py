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
{Fore.BLUE}    ###########################################################################
    #                                                                         #
    #      _____  _____ _____  ______ _    _                                    #
    #     |  __ \|  __ \_   _| |  __ \ |  | |                                   #
    #     | |  | | |  | | |   | |  | | |__| |                                   #
    #     | |  | | |  | | |   | |  | |  __  |                                   #
    #     | |__| | |__| |_|   | |__| | |  | |                                   #
    #     |_____/|_____/|_|   |_____/|_|  |_|                                   #
    #                                                                         #
    #                        D A T A   H U B                                  #
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
        description="Hub centralizador de Datos y Reportes."
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos de Datos")

    # Definir subcomandos
    subparsers.add_parser(
        "progress",
        help="Generación de reportes de progreso (reutiliza 19_Generate_Progress.py)",
    )
    subparsers.add_parser(
        "analytics",
        help="Fábrica de analítica maestra (reutiliza 20_Master_Analytics_Factory.py)",
    )
    subparsers.add_parser(
        "parser", help="Parser universal (reutiliza 86_Universal_Parser.py)"
    )
    subparsers.add_parser(
        "extract", help="Extractor de resúmenes (reutiliza 85_Resumen_Extractor.py)"
    )
    subparsers.add_parser(
        "batch", help="Parser por lotes (reutiliza 84_Batch_Parser.py)"
    )

    args = parser.parse_args()

    # Mapeo de comandos
    cmd_map = {
        "progress": "19_Generate_Progress.py",
        "analytics": "20_Master_Analytics_Factory.py",
        "parser": "86_Universal_Parser.py",
        "extract": "85_Resumen_Extractor.py",
        "batch": "84_Batch_Parser.py",
    }

    if args.command in cmd_map:
        dynamic_speak(f"Ejecutando comando de datos: {args.command}")
        run_script(cmd_map[args.command])
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
