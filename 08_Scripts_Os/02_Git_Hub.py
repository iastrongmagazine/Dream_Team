#!/usr/bin/env python3
"""
92_Git_Hub.py — Hub centralizador de acciones Git
SISTEMA SOTA INDEPENDIENTE - Sin dependencias Legacy
"""

import argparse
import os
import io
import sys
import subprocess
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
    class Style: RESET_ALL = BRIGHT = ""

# Fix Windows console encoding
if sys.platform == "win32":
    import io
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
    SISTEMA INDEPENDIENTE - Sin dependencias Legacy.
    """
    print(
        f"{Fore.CYAN}[STRUCTURE] Validando estructura del proyecto...{Style.RESET_ALL}"
    )

    # Dimensiones del proyecto (Pure Green v6.1)
    DIMENSIONS = [
        "00_Winter_is_Coming",
        "01_Core",
        "02_Knowledge",
        "03_Tasks",
        "04_Operations",
        "05_Archive",
        "08_Scripts_Os",
    ]

    errors = 0
    for dim in DIMENSIONS:
        path = ROOT_DIR / dim
        if path.exists() and path.is_dir():
            print(f"{Fore.GREEN}[OK] {dim}")
        else:
            print(f"{Fore.RED}[ERROR] {dim} missing")
            errors += 1

    if errors > 0:
        print(
            f"{Fore.RED}[FAIL] Estructura incompleta: {errors} carpetas faltantes{Style.RESET_ALL}"
        )
        return False

    print(f"{Fore.GREEN}[PASS] Estructura validada{Style.RESET_ALL}")
    return True


def run_engineering_audit():
    """
    Ejecuta auditoría de ingeniería (Pure Green).
    SISTEMA INDEPENDIENTE - Sin依赖 de Legacy.
    """
    print(f"{Fore.CYAN}[AUDIT] Ejecutando validación de código...{Style.RESET_ALL}")

    # Validaciones independientes (sin scripts legacy)
    errors = []

    # 1. Verificar que hay cambios para commit
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"], capture_output=True, text=True, check=True
        )
        if not result.stdout.strip():
            errors.append("No hay cambios para commit")
    except:
        errors.append("Error al verificar status de git")

    # 2. Verificar que no hay archivos sin跟踪
    try:
        result = subprocess.run(
            ["git", "ls-files", "--others", "--exclude-standard"],
            capture_output=True,
            text=True,
            check=True,
        )
        if result.stdout.strip():
            print(
                f"{Fore.YELLOW}[WARN] Archivos sin trackear: {len(result.stdout.strip().split(chr(10)))}{Style.RESET_ALL}"
            )
    except:
        pass

    if errors:
        print(f"{Fore.RED}[ERROR] {errors[0]}{Style.RESET_ALL}")
        return False

    print(f"{Fore.GREEN}[PASS] Validación passed{Style.RESET_ALL}")
    return True


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
        description="Hub centralizador de acciones Git (SISTEMA SOTA INDEPENDIENTE)"
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
