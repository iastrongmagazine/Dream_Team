"""
06_Tool_Hub.py — Tool Integration & Management Hub
====================================================
PersonalOS v6.1 | Think Different

Gestiona la integración y el ciclo de vida de herramientas externas dentro del OS.
Proporciona comandos para instalar, verificar, actualizar y auditar las herramientas
del ecosistema (CLI tools, binaries, MCP servers, etc.).

Uso:
    python 06_Tool_Hub.py --help
    python 06_Tool_Hub.py list
    python 06_Tool_Hub.py check <tool>
    python 06_Tool_Hub.py audit
"""
import argparse
import os
import io
import subprocess


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
{Fore.CYAN}    ###########################################################################
    #                                                                         #
    #       _____ _____  _____  _____                                          #
    #      / ____|  __ \|  __ \|  __ \                                        #
    #     | |    | |  | | |__) | |__) |                                        #
    #     | |    | |  | |  _  /|  _  /                                         #
    #     | |____| |__| | | \ \| | \ \                                         #
    #      \_____|_____/|_|  \_\_|  \_\                                        #
    #                                                                         #
    #                           T O O L   H U B                               #
    #                        P E R S O N A L   O S                            #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


def dynamic_speak(text):
    print(f"{Fore.MAGENTA}🔊 [VOICE]: {text}{Style.RESET_ALL}")


def report_progress(percent, message):
    bar_length = 40
    filled = int(bar_length * percent / 100)
    bar = "█" * filled + "░" * (bar_length - filled)
    print(f"{Fore.GREEN}[{bar}] {percent}% - {message}{Style.RESET_ALL}")


def run_script(script_name):
    # Los scripts de Herramientas están en 02_Tool
    script_path = ENGINE_DIR / "02_Tool" / script_name
    if not script_path.exists():
        print(f"{Fore.RED}[ERROR] Script no encontrado: {script_path}{Style.RESET_ALL}")
        return False

    report_progress(10, "Iniciando ejecución...")
    dynamic_speak(f"Ejecutando: {script_name}")

    report_progress(30, "Preparando entorno...")
    result = subprocess.run([sys.executable, str(script_path)])

    report_progress(60, "Procesando resultados...")
    report_progress(90, "Finalizando...")

    if result.returncode == 0:
        report_progress(100, "Completado exitosamente")
        print(
            f"{Fore.GREEN}[OK] {script_name} ejecutado correctamente{Style.RESET_ALL}"
        )
    else:
        report_progress(100, f"Finalizado con código {result.returncode}")
        print(
            f"{Fore.YELLOW}[WARN] {script_name} finalizó con código {result.returncode}{Style.RESET_ALL}"
        )

    return result.returncode == 0


def main():
    print_banner()
    parser = argparse.ArgumentParser(
        description="Hub de herramientas del sistema PersonalOS."
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    # Definir subcomandos
    subparsers.add_parser(
        "cleanup", help="Limpieza de tabs (reutiliza 01_Cleanup_Tabs.py)"
    )
    subparsers.add_parser(
        "tree",
        help="Generación de árbol de directorios (reutiliza 02_Generate_Tree.py)",
    )
    subparsers.add_parser(
        "repair", help="Reparación de corrupción (reutiliza 39_Repair_Corruption.py)"
    )

    args = parser.parse_args()

    # Mapeo de comandos
    cmd_map = {
        "cleanup": "01_Cleanup_Tabs.py",
        "tree": "02_Generate_Tree.py",
        "repair": "39_Repair_Corruption.py",
    }

    if args.command in cmd_map:
        dynamic_speak(f"Tool Hub - Ejecutando: {args.command}")
        run_script(cmd_map[args.command])
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
