#!/usr/bin/env python3
"""
91_Auditor_Hub.py — Hub centralizador de auditorías del sistema
Reutiliza scripts de auditoría existentes: 53, 57, 34, 50, 33
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


# === PROTOCOLO DE RUTA DINÁMICA (v6.1) ===
_current = Path(__file__).resolve()
_root = next((p for p in _current.parents if (p / "01_Core").exists()), None)
if _root:
    sys.path.insert(0, str(_root / "08_Scripts_Os"))
from config_paths import *

# PROJECT_ROOT ya viene de config_paths como ROOT_DIR
PROJECT_ROOT = ROOT_DIR

DIMENSIONS = [
    "00_Winter_is_Coming",
    "01_Core",
    "02_Knowledge",
    "03_Tasks",
    "04_Operations",
    "05_Archive",
    "06_Playground",
    "07_Projects",
    "08_Scripts_Os",
]


def audit_dimensions():
    """Valida las 7+ dimensiones del proyecto."""
    print(f"\n{Style.BRIGHT}Validating Dimensions:")
    errors = 0
    # Usar constante DIMENSIONS de config_paths si existiera, o manual dinámica
    dims = [
        "00_Winter_is_Coming",
        "01_Core",
        "02_Knowledge",
        "03_Tasks",
        "04_Operations",
        "05_Archive",
        "06_Playground",
        "07_Projects",
        "08_Scripts_Os",
    ]
    for dim in dims:
        path = PROJECT_ROOT / dim
        if path.exists() and path.is_dir():
            print(f"{Fore.GREEN}[OK] {dim}")
        else:
            print(f"{Fore.RED}[ERROR] {dim} missing")
            errors += 1
    return errors


def audit_script_numbering():
    """Valida que scripts sigan el patrón NN_ o NNN_."""
    print(f"\n{Style.BRIGHT}Validating Engine Script Numbering:")
    engine_dir = ENGINE_DIR
    errors = 0
    scripts = list(engine_dir.glob("*.py"))
    for script in scripts:
        name = script.name
        # Aceptar NN_ (2 dígitos) o NNN_ (3 dígitos como 100)
        is_valid = (len(name) >= 3 and name[0:2].isdigit() and name[2] == "_") or (
            len(name) >= 4 and name[0:3].isdigit() and name[3] == "_"
        )
        if is_valid:
            print(f"{Fore.GREEN}[OK] {name}")
        else:
            if name != "config_paths.py":
                print(f"{Fore.RED}[ERROR] {name} does not follow NN_ or NNN_ pattern")
                errors += 1
    return errors


# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


def print_banner():
    banner = rf"""
{Fore.CYAN}    ###########################################################################
    #                                                                         #
    #      _____  _    _ _____  _____   ____  _    _ _____  _    _ _____      #
    #     |  __ \| |  | |  __ \|  __ \ / __ \| |  | |  __ \| |  | |  __ \     #
    #     | |__) | |  | | |__) | |  | | |  | | |  | | |__) | |__| | |  | |    #
    #     |  _  /| |  | |  _  /| |  | | |  | | |  | |  _  /|  __  | |  | |    #
    #     | | \ \| |__| | | \ \| |__| | |__| | |__| | | \ \| |  | | |__| |    #
    #     |_|  \_\____/|_|  \_\_____/ \____/ \____/|_|  \_\_|  |_|_____/     #
    #                                                                         #
    #                          A U D I T O R   H U B                          #
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
    # Usamos AUDITOR_DIR definido en config_paths o relativo dinámico
    script_path = AUDITOR_DIR / script_name
    if not script_path.exists():
        print(f"{Fore.RED}[ERROR] Script no encontrado: {script_path}{Style.RESET_ALL}")
        return
    print(f"{Fore.YELLOW}[RUNNING] Ejecutando: {script_name}...{Style.RESET_ALL}")
    subprocess.run([sys.executable, str(script_path)])


def main():
    print_banner()
    parser = argparse.ArgumentParser(
        description="Hub centralizador de auditorías del sistema."
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos disponibles")

    subparsers.add_parser(
        "estructura", help="Auditoría de estructura (reutiliza 53_Structure_Auditor.py)"
    )
    subparsers.add_parser(
        "links", help="Auditoría de links (reutiliza 57_Repo_Sync_Auditor.py)"
    )
    subparsers.add_parser(
        "skills", help="Auditoría de skills (reutiliza 34_Skill_Auditor.py)"
    )
    subparsers.add_parser(
        "health", help="Monitoreo de salud (reutiliza 50_System_Health_Monitor.py)"
    )
    subparsers.add_parser(
        "profundo", help="Auditoría profunda (reutiliza 33_Parallel_Audit_Pro.py)"
    )

    args = parser.parse_args()

    if args.command == "estructura":
        dynamic_speak("Iniciando auditoría de estructura")
        print(f"{Style.BRIGHT}--- Structure Auditor ---")
        errors_dim = audit_dimensions()
        errors_num = audit_script_numbering()
        total_errors = errors_dim + errors_num
        if total_errors == 0:
            print(f"\n{Fore.GREEN}{Style.BRIGHT}✓ Estructura válida{Style.RESET_ALL}")
        else:
            print(
                f"\n{Fore.RED}{Style.BRIGHT}✗ Se encontraron {total_errors} errores{Style.RESET_ALL}"
            )
    elif args.command == "links":
        dynamic_speak("Iniciando auditoría de enlaces")
        run_script("57_Repo_Sync_Auditor.py")
    elif args.command == "skills":
        dynamic_speak("Iniciando auditoría de skills")
        run_script("34_Skill_Auditor.py")
    elif args.command == "health":
        dynamic_speak("Iniciando monitoreo de salud")
        run_script("50_System_Health_Monitor.py")
    elif args.command == "profundo":
        dynamic_speak("Iniciando auditoría profunda paralela")
        run_script("33_Parallel_Audit_Pro.py")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
