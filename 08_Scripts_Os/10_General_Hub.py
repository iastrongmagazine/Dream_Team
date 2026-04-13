"""
10_General_Hub.py — General Utilities Hub
==========================================
PersonalOS v6.1 | Think Different

Colección de utilidades generales del OS: limpieza de temporales, verificación
de dependencias, reset de estado, helpers de debugging y operaciones
de mantenimiento que no encajan en hubs especializados.

Uso:
    python 10_General_Hub.py --help
    python 10_General_Hub.py clean
    python 10_General_Hub.py deps-check
    python 10_General_Hub.py reset-state
"""
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

import argparse
import subprocess


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
    # Los scripts Generales están en 08_General
    script_path = ENGINE_DIR / "08_General" / script_name
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
