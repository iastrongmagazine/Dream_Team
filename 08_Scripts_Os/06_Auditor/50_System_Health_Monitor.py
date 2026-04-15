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
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class Fore: CYAN = GREEN = RED = YELLOW = MAGENTA = ""
    class Style: RESET_ALL = ""
    def init(**kw): pass


def check_directory_structure():
    print(f"{Fore.CYAN}--- Verificando Estructura de Directorios ---")
    required_dirs = [
        MATRIX_DIR,
        CORE_DIR,
        BRAIN_DIR,
        OPERATIONS_DIR,
        KNOWLEDGE_DIR,
        ENGINE_DIR,
        SYSTEM_DIR,
        ARCHIVE_DIR,
        PROJECTS_DIR,
        PLAYGROUND_DIR,
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
    junk_files = [".DS_Store", "Thumbs.db"]
    found_junk = False
    for junk in junk_files:
        if (ROOT_DIR / junk).exists():
            print(f"{Fore.YELLOW}[WARN] Junk file found: {junk}")
            found_junk = True
    if not found_junk:
        print(f"{Fore.GREEN}[OK] No se detectó contaminación obvia.")
    return not found_junk


def verify_master_files():
    print(f"\n{Fore.CYAN}--- Verificando Archivos Maestros ---")
    master_files = ["CLAUDE.md", "README.md"]
    all_found = True
    for mf in master_files:
        if (ROOT_DIR / mf).exists():
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
