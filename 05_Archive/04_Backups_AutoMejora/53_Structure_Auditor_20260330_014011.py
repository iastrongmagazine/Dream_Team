import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
ENGINE_DIR = ROOT_DIR / "04_Operations" / "08_Scripts_Os"

DIMENSIONS = [
    "00_Core",
    "01_Brain",
    "04_Operations",
    "03_Knowledge",
    "04_Operations",
    "05_System",
    "06_Archive",
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
