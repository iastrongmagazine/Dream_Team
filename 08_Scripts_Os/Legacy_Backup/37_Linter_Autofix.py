import subprocess
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import PROJECT_ROOT

# Configuración de Colores
GREEN = "\033[92m"
CYANT = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

ROOT_DIR = PROJECT_ROOT
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


def run_linter_fix(directory, name):
    print(f"{CYANT}>>> Ejecutando Auto-Fix Linter en: {name}...{RESET}")
    package_json = os.path.join(directory, "package.json")

    if not os.path.exists(package_json):
        print(f"{YELLOW}[SKIP] No se encontró package.json en {name}.{RESET}")
        return True

    try:
        # Intentamos ejecutar 'npm run lint -- --fix' o similar
        # Muchos proyectos usan 'eslint --fix' via script o directamente
        result = subprocess.run(
            ["npm", "run", "lint", "--", "--fix"],
            cwd=directory,
            shell=True,
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            print(f"{GREEN}[OK] Linter fix completado en {name}.{RESET}")
            return True
        else:
            print(
                f"{YELLOW}[AVISO] Linter encontró problemas no auto-corregibles.{RESET}"
            )
            # print(result.stdout)
            return True  # No bloqueamos el ritual
    except Exception as e:
        print(f"{RED}[ERR] Error ejecutando linter en {name}: {e}{RESET}")
        return True


def main():
    print(f"{CYANT}=== AUTO-FIX LINTER SERVICE ==={RESET}")

    # 1. Drilling Calculator
    drilling_dir = os.path.join(ROOT_DIR, "Side Project", "Oil", "drilling-calculator")
    run_linter_fix(drilling_dir, "Drilling Calculator")

    # 2. Main Project (si tiene linter en el futuro)
    # run_linter_fix(ROOT_DIR, "PersonalOS Root")


if __name__ == "__main__":
    main()
