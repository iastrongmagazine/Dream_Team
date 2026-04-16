"""
09_Data_Hub.py — Data Processing & Analytics Hub
==================================================
PersonalOS v6.1 | Think Different

Procesa y analiza datos del OS: métricas de sesiones, consumo de tokens,
performance de skills, reportes de auditoría y visualización de tendencias.
Genera outputs en `04_Operations/10_Reports/` para revisión manual o automatizada.

Uso:
    python 09_Data_Hub.py --help
    python 09_Data_Hub.py analyze
    python 09_Data_Hub.py report --period week
    python 09_Data_Hub.py export --format csv
"""
import argparse
import subprocess
import sys
from pathlib import Path

# === PROTOCOLO DE RUTA DINÁMICA (v6.1) ===
_current = Path(__file__).resolve()
_root = next((p for p in _current.parents if (p / "01_Core").exists()), None)
if _root:
    sys.path.insert(0, str(_root / "08_Scripts_Os"))
from config_paths import *

# === COLOR SETUP ===
try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Fore: GREEN = YELLOW = RED = CYAN = MAGENTA = BLUE = ""
    class Style: RESET_ALL = ""

# Fix Windows console encoding
if sys.platform == "win32":
    import io
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
    print(f"{Fore.MAGENTA}[VOICE]: {text}{Style.RESET_ALL}")


def run_script(script_name):
    # Los scripts de Datos están en 07_Data
    script_path = ENGINE_DIR / "07_Data" / script_name
    if not script_path.exists():
        # Fallback a 01_Ritual para Generate_Progress si no está en 07_Data
        script_path = ENGINE_DIR / "01_Ritual" / script_name
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
