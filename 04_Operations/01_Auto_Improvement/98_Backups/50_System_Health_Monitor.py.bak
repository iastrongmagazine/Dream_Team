#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
System Health Monitor - PersonalOS v6.1
Monitorea la salud del sistema.
"""

import os
import sys
from pathlib import Path

# === SETUP PATHS ===
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# === IMPORTS ===
try:
    from config_paths import (
        ROOT_DIR,
        BRAIN_DIR,
        BRAIN_RULES_DIR,
        COMPOUND_ENGINE_DIR,
        ENGINE_DIR,
    )
except ImportError:
    ROOT_DIR = PROJECT_ROOT
    BRAIN_DIR = PROJECT_ROOT / "04_Operations"
    BRAIN_RULES_DIR = BRAIN_DIR / "04_Memory_Brain"
    COMPOUND_ENGINE_DIR = (
        PROJECT_ROOT / "01_Core" / "03_Skills" / "00_Compound_Engineering"
    )
    ENGINE_DIR = PROJECT_ROOT / "08_Scripts_Os"

# === COLOR SETUP ===
try:
    from colorama import Fore, Style, init

    init(autoreset=True)
except ImportError:

    class Fore:
        CYAN = GREEN = RED = YELLOW = MAGENTA = ""

    class Style:
        RESET_ALL = ""

    def init(**kw):
        pass


def check_directory_structure():
    print(f"{Fore.CYAN}--- Verificando Estructura de Directorios ---")
    required_dirs = [
        CORE_DIR,
        BRAIN_DIR,
        OPERATIONS_DIR,
        KNOWLEDGE_DIR,
        ENGINE_DIR,
        SYSTEM_DIR,
        ARCHIVE_DIR,
    ]
    all_good = True
    for d in required_dirs:
        if os.path.exists(d):
            print(f"{Fore.GREEN}[OK] {d}")
        else:
            print(f"{Fore.RED}[MISSING] {d}")
            all_good = False
    return all_good


def check_pollution():
    print(f"\n{Fore.CYAN}--- Verificando Contaminación ---")
    # Example check: look for common junk files in root
    junk_files = [".DS_Store", "Thumbs.db"]
    found_junk = False
    # Need to go up 2 levels from 08_Scripts_Os to root
    for junk in junk_files:
        if os.path.exists(os.path.join(os.path.dirname(__file__), "..", "..", junk)):
            print(f"{Fore.YELLOW}[WARN] Junk file found: {junk}")
            found_junk = True
    if not found_junk:
        print(f"{Fore.GREEN}[OK] No se detectó contaminación obvia.")
    return not found_junk


def verify_master_files():
    print(f"\n{Fore.CYAN}--- Verificando Archivos Maestros ---")
    master_files = ["CLAUDE.md", "README.md"]
    all_found = True
    # Need to go up 3 levels from Legacy_Backup/08_Scripts_Os/04_Engine to root
    for mf in master_files:
        if os.path.exists(
            os.path.join(os.path.dirname(__file__), "..", "..", "..", mf)
        ):
            print(f"{Fore.GREEN}[OK] {mf} encontrado.")
        else:
            print(f"{Fore.RED}[MISSING] {mf} no encontrado.")
            all_found = False
    return all_found


if __name__ == "__main__":
    print(f"{Fore.MAGENTA}=== Sistema de Monitoreo de Salud ===")
    s1 = check_directory_structure()
    s2 = check_pollution()
    s3 = verify_master_files()

    if s1 and s2 and s3:
        print(f"\n{Fore.GREEN}=== ESTATUS: SALUDABLE ===")
        sys.exit(0)
    else:
        print(f"\n{Fore.RED}=== ESTATUS: PROBLEMAS DETECTADOS ===")
        sys.exit(1)
