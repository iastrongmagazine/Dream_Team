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
{Fore.WHITE}    ###########################################################################
    #                                                                         #
    #       _____ _   _ _______ _______ _____ _______ _____  _____             #
    #      / ____| \ | |__   __|__   __|_   _|__   __|  __ \ / ____|            #
    #     | |    |  \| | | |     | |    | |    | |  | |__) | |  __              #
    #     | |    | . ` | | |     | |    | |    | |  |  _  /| | |_ |             #
    #     | |____| |\  | | |     | |    | |    | |  | | \ \| |__| |             #
    #      \_____|_| \_| |_|     |_|    |_|    |_|  |_|  \_\\_____|             #
    #                                                                         #
    #                      G E N E R A L   H U B                              #
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
        description="Hub centralizador de utilidades Generales."
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos Generales")

    # Definir subcomandos
    subparsers.add_parser(
        "reset", help="Reseteo de contexto (reutiliza 00_Context_Reset.py)"
    )
    subparsers.add_parser(
        "notify", help="Sistema de notificaciones (reutiliza 77_Notify_System.py)"
    )
    subparsers.add_parser(
        "alert", help="Gestor de alertas (reutiliza 66_Alert_Manager.py)"
    )
    subparsers.add_parser(
        "campanilla", help="Campanilla de tareas (reutiliza 64_Campanilla.py)"
    )
    subparsers.add_parser(
        "sync-notes", help="Sincronización de notas (reutiliza 11_Sync_Notes.py)"
    )

    args = parser.parse_args()

    # Mapeo de comandos
    cmd_map = {
        "reset": "00_Context_Reset.py",
        "notify": "77_Notify_System.py",
        "alert": "66_Alert_Manager.py",
        "campanilla": "64_Campanilla.py",
        "sync-notes": "11_Sync_Notes.py",
    }

    if args.command in cmd_map:
        dynamic_speak(f"Ejecutando utilidad general: {args.command}")
        run_script(cmd_map[args.command])
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
