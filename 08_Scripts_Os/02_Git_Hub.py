#!/usr/bin/env python3
"""
92_Git_Hub.py — Hub centralizador de acciones Git
INTEGRADO: 52_Safe_Commit + 54_Commit_Guard (sin dependencia de Legacy_Backup)
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


from config_paths import ROOT_DIR


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
{Fore.RED}    ###########################################################################
    #                                                                         #
    #      _____ _____ _______   _    _ _    _ ____  _____                    #
    #     / ____|_   _|__   __| | |  | | |  | |  _ \|  __ \                   #
    #    | |  __  | |    | |    | |__| | |  | | |_) | |__) |                  #
    #    | | |_ | | |    | |    |  __  | |  | |  _ <|  _  /                   #
    #    | |__| |_| |_   | |    | |  | | |__| | |_) | | \ \                   #
    #     \_____|_____|  |_|    |_|  |_|\____/|____/|_|  \_\                  #
    #                                                                         #
    #                          G I T   H U B                                  #
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


def run_script(script_path, desc):
    """Ejecuta un script y retorna True si tuvo éxito."""
    print(f"\n{'=' * 60}")
    print(f"STEP: {desc}")
    print(f"{'=' * 60}")
    try:
        result = subprocess.run([sys.executable, str(script_path)], check=False)
        return result.returncode == 0
    except Exception as e:
        print(f"{Fore.RED}[ERROR] Falló {desc}: {e}{Style.RESET_ALL}")
        return False


def run_structure_audit():
    """
    Ejecuta validación de estructura del proyecto.
    Wrapper para 53_Structure_Auditor.py.
    """
    script_path = (
        ROOT_DIR / "08_Scripts_Os" / "Legacy_Backup" / "53_Structure_Auditor.py"
    )
    if not script_path.exists():
        print(
            f"{Fore.RED}[ERROR] Structure Auditor no encontrado: {script_path}{Style.RESET_ALL}"
        )
        return False
    return run_script(script_path, "STRUCTURE AUDIT")


def run_engineering_audit():
    """
    Ejecuta auditoría de ingeniería (Pure Green).
    Wrapper para 42_Audit_Engineering.py.
    """
    script_path = (
        ROOT_DIR / "08_Scripts_Os" / "Legacy_Backup" / "42_Audit_Engineering.py"
    )
    if not script_path.exists():
        print(
            f"{Fore.RED}[ERROR] Engineering Audit no encontrado: {script_path}{Style.RESET_ALL}"
        )
        return False
    return run_script(script_path, "ENGINEERING AUDIT")


def run_git_commit(git_args):
    """Ejecuta git commit con los argumentos dados."""
    if not git_args:
        print(f"{Fore.RED}[ERROR] No hay argumentos para git commit{Style.RESET_ALL}")
        return False

    cmd = ["git", "commit"] + git_args
    print(f"\n{'=' * 60}")
    print(f"STEP: GIT COMMIT")
    print(f"{'=' * 60}")
    print(f"Ejecutando: {' '.join(cmd)}\n")

    try:
        subprocess.run(cmd, check=True)
        print(f"{Fore.GREEN}[SUCCESS] Commit realizado con éxito{Style.RESET_ALL}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"{Fore.RED}[ABORT] Git commit falló: {e}{Style.RESET_ALL}")
        return False


def safe_commit(git_args):
    """
    Commit seguro: Engineering Audit + Git Commit.
    Integra lógica de 52_Safe_Commit.py.
    """
    print(
        f"{Fore.CYAN}[SAFE-COMMIT] Iniciando auditoría de ingeniería...{Style.RESET_ALL}"
    )

    if not run_engineering_audit():
        print(
            f"\n{Fore.RED}[ABORT] Pure Green no aprobado — COMMIT DENEGADO{Style.RESET_ALL}"
        )
        dynamic_speak("Commit abortado por auditoría de ingeniería")
        return False

    dynamic_speak("Auditoría aprobada, ejecutando commit")
    return run_git_commit(git_args)


def guard_commit(git_args):
    """
    Commit con guardrail: Structure Audit + Engineering Audit + Git Commit.
    Integra lógica de 54_Commit_Guard.py.
    """
    print(
        f"{Fore.CYAN}[GUARD-COMMIT] Iniciando validación completa...{Style.RESET_ALL}"
    )

    # 1. Structure Audit
    if not run_structure_audit():
        print(
            f"\n{Fore.RED}[ABORT] Estructura del proyecto falló — COMMIT DENEGADO{Style.RESET_ALL}"
        )
        dynamic_speak("Commit abortado por auditoría de estructura")
        return False

    # 2. Engineering Audit
    if not run_engineering_audit():
        print(
            f"\n{Fore.RED}[ABORT] Pure Green no aprobado — COMMIT DENEGADO{Style.RESET_ALL}"
        )
        dynamic_speak("Commit abortado por auditoría de ingeniería")
        return False

    # 3. Git Commit
    dynamic_speak("Validación completa aprobada, ejecutando commit")
    return run_git_commit(git_args)


def main():
    print_banner()
    parser = argparse.ArgumentParser(
        description="Hub centralizador de acciones Git (INTEGRADO - sin Legacy_Backup)"
    )
    subparsers = parser.add_subparsers(dest="command", help="Comandos de Git")

    # Safe Commit
    parser_safe = subparsers.add_parser(
        "safe-commit",
        help="Git commit seguro (Engineering Audit → Git Commit)",
        description="Ejecuta auditoría de ingeniería antes de permitir commit. Si falla, aborta.",
    )
    parser_safe.add_argument(
        "git_args",
        nargs=argparse.REMAINDER,
        help="Argumentos para git commit (ej: -m 'feat: description')",
    )

    # Commit Guard
    parser_guard = subparsers.add_parser(
        "guard-commit",
        help="Commit con guardrail (Structure + Engineering → Git Commit)",
        description="Ejecuta auditoría de estructura Y ingeniería antes de permitir commit. Si alguna falla, aborta.",
    )
    parser_guard.add_argument(
        "git_args",
        nargs=argparse.REMAINDER,
        help="Argumentos para git commit (ej: -m 'feat: description')",
    )

    args = parser.parse_args()

    if args.command == "safe-commit":
        dynamic_speak("Iniciando commit seguro")
        success = safe_commit(args.git_args)
        sys.exit(0 if success else 1)

    elif args.command == "guard-commit":
        dynamic_speak("Iniciando guardrail de commit")
        success = guard_commit(args.git_args)
        sys.exit(0 if success else 1)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
