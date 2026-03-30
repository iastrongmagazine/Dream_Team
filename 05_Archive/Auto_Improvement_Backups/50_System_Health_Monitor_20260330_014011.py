import os
import sys

try:
    from colorama import Fore, Style, init
except ImportError:

    class Fore:
        CYAN = GREEN = RED = YELLOW = MAGENTA = ""

    class Style:
        RESET_ALL = ""

    def init(**kw):
        pass


# Add ROOT_DIR to path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from config_paths import (
    CORE_DIR,
    BRAIN_DIR,
    OPERATIONS_DIR,
    KNOWLEDGE_DIR,
    ENGINE_DIR,
    SYSTEM_DIR,
    ARCHIVE_DIR,
)

init(autoreset=True)


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
    # Need to go up 3 levels from _Fixed/08_Scripts_Os/04_Operations to root
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
