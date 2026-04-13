"""
07_Integration_Hub.py — MCP & External Integrations Hub
=========================================================
PersonalOS v6.1 | Think Different

Administra las integraciones con servicios externos y servidores MCP.
Permite verificar estado de conexión, recargar configuraciones y diagnosticar
problemas de conectividad con Context7, EXA, Notion, OpenRouter, Engram, etc.

Uso:
    python 07_Integration_Hub.py --help
    python 07_Integration_Hub.py status
    python 07_Integration_Hub.py check <mcp-name>
    python 07_Integration_Hub.py reload
"""
import argparse
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
{Fore.MAGENTA}    ###########################################################################
    #                                                                         #
    #      _____ ___ _    _        _    _                                       #
    #     |_   _/ _ \ |  | |      | |  | |                                      #
    #       | || | | | |__| |      | |  | |                                      #
    #       | || | | |  __  |      | |  | |                                      #
    #       | || |_| | |  | |      | |__| |                                      #
    #       |_| \___/|_|  |_|       \____/                                       #
    #                                                                         #
    #                    I N T E G R A T I O N   H U B                         #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


def dynamic_speak(text):
    print(f"{Fore.MAGENTA}🔊 [VOICE]: {text}{Style.RESET_ALL}")


def run_script(script_name):
    script_path = Path(__file__).parent / "Integration_Fixed" / script_name
    if not script_path.exists():
        print(f"{Fore.RED}[ERROR] Script no encontrado: {script_path}{Style.RESET_ALL}")
        return

    print(f"{Fore.YELLOW}[RUNNING] Ejecutando: {script_name}...{Style.RESET_ALL}")
    subprocess.run([sys.executable, str(script_path)])


def main():
    print_banner()
    parser = argparse.ArgumentParser(description="Hub centralizador de Integraciones.")
    subparsers = parser.add_subparsers(dest="command", help="Comandos de Integración")

    # Definir subcomandos
    subparsers.add_parser(
        "qmd", help="Actualización del índice QMD (reutiliza 75_Update_QMD_Index.py)"
    )
    subparsers.add_parser(
        "obsidian", help="Exportador para Obsidian (reutiliza 76_Obsidian_Exporter.py)"
    )
    subparsers.add_parser(
        "mcp-sync",
        help="Sincronización con OpenCode MCP (reutiliza 46_Sync_MCP_OpenCode.py)",
    )

    args = parser.parse_args()

    # Mapeo de comandos
    cmd_map = {
        "qmd": "75_Update_QMD_Index.py",
        "obsidian": "76_Obsidian_Exporter.py",
        "mcp-sync": "46_Sync_MCP_OpenCode.py",
    }

    if args.command in cmd_map:
        dynamic_speak(f"Ejecutando integración: {args.command}")
        run_script(cmd_map[args.command])
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
