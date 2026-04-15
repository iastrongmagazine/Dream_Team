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
    class Fore: GREEN = RED = ""
    class Style: BRIGHT = ""

# Las dimensiones ya vienen de config_paths o se definen aquí
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


def audit():
    errors = 0
    print(f"{Style.BRIGHT}--- Structure Auditor ---")

    print(f"\n{Style.BRIGHT}Validating Dimensions:")
    for dim in DIMENSIONS:
        path = ROOT_DIR / dim
        if path.exists() and path.is_dir():
            print(f"{Fore.GREEN}[OK] {dim}")
        else:
            print(f"{Fore.RED}[ERROR] {dim} missing")
            errors += 1

    print(f"\n{Style.BRIGHT}Validating Engine Script Numbering:")
    scripts = list(ENGINE_DIR.glob("*.py"))
    for script in scripts:
        name = script.name
        if len(name) >= 3 and name[0:2].isdigit() and name[2] == "_":
            print(f"{Fore.GREEN}[OK] {name}")
        else:
            # Allow config_paths.py (helper, not script)
            if name != "config_paths.py":
                print(f"{Fore.RED}[ERROR] {name} does not follow NN_ pattern")
                errors += 1

    return errors == 0


if __name__ == "__main__":
    success = audit()
    sys.exit(0 if success else 1)
