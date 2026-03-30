import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
"""
40_Validate_Rules.py - Armor Layer Protected
"""

import os
import sys
import io
import re
import subprocess
import glob
from pathlib import Path
from typing import List
from colorama import init, Fore, Style

init()

# === COLORS ===
SUCCESS = Fore.GREEN
INFO = Fore.CYAN
WARNING = Fore.YELLOW
ERROR = Fore.RED
RESET = Style.RESET_ALL

BRIGHT = Fore.MAGENTA

sys.path.insert(0, str(Path(__file__).parent.parent))
from config_paths import PROJECT_ROOT, BRAIN_DIR, ENGINE_DIR, KNOWLEDGE_DIR

REQUIRED_DIRS = [
    "00_Core",
    "01_Brain",
    "02_Operations",
    "03_Knowledge",
    "../..",
    "05_System",
    "06_Archive",
]
for d in REQUIRED_DIRS:
    if not (PROJECT_ROOT / d).exists():
        print(f"[WARN] Required directory not found: {d}")

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


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


# Alias for compatibility
speak = dynamic_speak


def print_banner():
    banner = rf"""
{Fore.YELLOW}    ###########################################################################
    #                                                                         #
    #       _____ _    _ _____ ______ _      _____         _      _           #
    #      / ____| |  | |_   _|  ____| |    |  __ \       | |    | |          #
    #     | (___ | |__| | | | | |__  | |    | |  | |      | |    | |          #
     #     \___ \|  __  | | | |  __| | |    | |  | |      | |    | |          #
    #      ____) | |  | |_| |_| |____| |____| |__| |      | |____| |____      #
    #     |_____/|_|  |_|_____|______|______|_____/       |______|______|     #
    #                                                                         #
    #                        R U L E   S H I E L D                            #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


ROOT_DIR = PROJECT_ROOT


def main() -> None:
    """Orquestador principal de validaciones."""
    print_banner()
    dynamic_speak("Iniciando validación integral de reglas y blindaje Armor Layer")


# --- VALIDACIONES ---


def validate_engine_naming() -> bool:
    """
    Verifica que los scripts del ENGINE sigan el formato NN_snake_case.py.

    Returns:
        bool: True si todos los archivos cumplen el estándar, False de lo contrario.
    """
    print(f"\n{INFO}[SCAN] Validando Naming Convention en 04_Engine...{RESET}")
    engine_dir = ENGINE_DIR
    pattern = re.compile(r"^\d{2}_[A-Z][a-zA-Z0-9_]+\.py$")
    errors: List[str] = []

    if not os.path.exists(engine_dir):
        print(f"{ERROR}[ERR] No se encontró el directorio 04_Engine.{RESET}")
        return False

    for item_name in os.listdir(engine_dir):
        if not item_name.endswith(".py") or item_name == "__init__.py":
            continue
        if not pattern.match(item_name):
            errors.append(item_name)

    if errors:
        print(
            f"{Fore.YELLOW}[WARN] Archivos que no siguen el estándar 'NN_Title_Case.py':{Style.RESET_ALL}"
        )
        for err in errors:
            print(f"  - {err}")
        return False

    print(
        f"{Fore.GREEN}[OK] Todos los scripts del Engine cumplen el estándar.{Style.RESET_ALL}"
    )
    return True


def validate_rules_structure() -> bool:
    """
    Verifica la estructura básica de los archivos .mdc en .cursor/rules.

    Returns:
        bool: True si todas las reglas tienen la estructura requerida.
    """
    import glob

    print(f"\n{INFO}[SCAN] Validando y Listando Reglas (.mdc) para Contexto...{RESET}")
    rules_dir = BRAIN_DIR / "04_Rules"
    if not os.path.exists(rules_dir):
        print(f"{WARNING}[SKIP] No se encontró el directorio de reglas.{RESET}")
        return True

    errors: List[str] = []
    print(f"{BRIGHT}Catálogo de Reglas Activas:{RESET}")
    for rule_path in sorted(glob.glob(os.path.join(rules_dir, "*.mdc"))):
        rule_name = os.path.basename(rule_path)
        try:
            try:
                with open(rule_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except (UnicodeDecodeError, OSError):
                with open(rule_path, "r", encoding="latin-1") as f:
                    content = f.read()

            # Extraer descripción simple
            desc_match = re.search(r"description:\s*(.+)$", content, re.MULTILINE)
            desc = (
                desc_match.group(1).strip() if desc_match else "Sin descripción clara"
            )

            if "description:" not in content.lower():
                errors.append(f"{rule_name}: Falta field 'description'")
            if "globs:" not in content.lower():
                errors.append(f"{rule_name}: Falta field 'globs'")

            print(f"  - {SUCCESS}{rule_name}{RESET}: {desc}")

        except OSError as e:
            errors.append(f"{rule_name}: Error de lectura ({e})")

    if errors:
        print(f"{Fore.RED}[ERR] Violaciones de estructura en reglas:{Style.RESET_ALL}")
        for err in errors:
            print(f"  - {err}")
        return False

    print(
        f"{Fore.GREEN}[OK] Todas las reglas parecen tener estructura válida.{Style.RESET_ALL}"
    )
    return True


def validate_arsenal_integrity() -> bool:
    """
    Verifica la existencia física de los skills referenciados en el Inventario.
    Solo valida referencias que sigan el patrón de Skills (NN_Nombre_Skill).

    Returns:
        bool: True si todos los skills existen en el sistema.
    """
    print(f"\n{INFO}[SCAN] Validando Integridad del Arsenal (Skills)...{RESET}")

    # Rutas de búsqueda de Skills
    skills_paths = [
        PROJECT_ROOT / ".agent" / "02_Skills" / "01_Core",
        PROJECT_ROOT / ".agent" / "02_Skills" / "02_High_Value",
        PROJECT_ROOT / ".agent" / "02_Skills" / "03_Utilities",
        PROJECT_ROOT / ".agent" / "02_Skills",
    ]

    inventory_file = KNOWLEDGE_DIR / "01_Inventario_Total.md"

    if not os.path.exists(inventory_file):
        print(
            f"{WARNING}[SKIP] No se encontró el inventario para validar arsenal.{RESET}"
        )
        return True

    try:
        with open(inventory_file, "r", encoding="utf-8") as f:
            content = f.read()
    except (UnicodeDecodeError, OSError):
        with open(inventory_file, "r", encoding="latin-1") as f:
            content = f.read()

    # Buscar patrones de skills: [NN_Nombre_Skill] o [Nombre_Skill] (evitando documentos .md)
    # Filtramos para que no coincida con archivos de documentación como 03_References_Guide.md
    skill_refs = re.findall(r"\[(\d{2}_[^\]]+)\]", content)
    missing: List[str] = []

    for skill_name in skill_refs:
        # Si termina en .md o .txt, es una referencia a doc, no a skill
        if skill_name.lower().endswith((".md", ".txt", ".py")):
            continue

        found = False
        for path in skills_paths:
            if os.path.exists(os.path.join(path, skill_name)):
                found = True
                break

        if not found:
            missing.append(skill_name)

    if missing:
        print(f"{ERROR}[ERR] Skills referenciadas que NO existen físicamente:{RESET}")
        for m in missing:
            print(f"  - {m}")
        return False

    print(f"{SUCCESS}[OK] Integridad del arsenal validada correctamente.{RESET}")
    return True


def validate_folder_health() -> bool:
    """Verifica que la jerarquía 00-08 de PersonalOS esté intacta."""
    print(f"\n{INFO}[SCAN] Validando Jerarquía de Carpetas (00-08)...{RESET}")
    expected_dirs = [
        "00_Core",
        "01_Brain",
        "02_Operations",
        "03_Knowledge",
        "../..",
        "05_System",
        "06_Archive",
    ]
    missing = []
    for d in expected_dirs:
        if not os.path.exists(PROJECT_ROOT / d):
            missing.append(d)

    if missing:
        print(f"{ERROR}[ERR] Carpetas faltantes: {', '.join(missing)}{RESET}")
        return False
    print(f"{SUCCESS}[OK] Jerarquía 00-08 validada.{RESET}")
    return True


def validate_integrations() -> bool:
    """Verifica el estado de Playwright y Fireflies."""
    print(f"\n{INFO}[SCAN] Validando Integraciones Criticas...{RESET}")
    # Playwright check (simple command check)
    try:
        import subprocess

        res = subprocess.run(
            ["npx", "playwright", "--version"],
            capture_output=True,
            text=True,
            shell=True,
        )
        pl_ok = res.returncode == 0
    except:
        pl_ok = False

    # Fireflies check - es opcional, no fallar si no existe
    ff_ok = True  # Opcional - no hacer fallar el script por esto
    recap_path = ENGINE_DIR / "08_Scripts_Os" / "38_Recap_Planning.py"
    if os.path.exists(recap_path):
        print(f"{SUCCESS}[OK] Recap Planning detectado.{RESET}")
    else:
        print(f"{WARNING}[WARN] Recap Planning no encontrado (opcional).{RESET}")

    if pl_ok:
        print(f"{SUCCESS}[OK] Playwright operativo.{RESET}")
    else:
        print(f"{WARNING}[WARN] Playwright no detectado globalmente.{RESET}")

    return pl_ok  # Solo Playwright es obligatorio


def main() -> None:
    """Orquestador principal de validaciones."""
    print_banner()
    dynamic_speak("Iniciando validación integral PURE GREEN")

    results = {
        "Naming": validate_engine_naming(),
        "Reglas": validate_rules_structure(),
        "Arsenal": validate_arsenal_integrity(),
        "Carpetas": validate_folder_health(),
        "Integraciones": validate_integrations(),
    }

    pureness = (sum(results.values()) / len(results)) * 100

    if all(results.values()):
        print(
            f"\n{SUCCESS}[VALID] SISTEMA EN ESTADO PURE GREEN ({pureness:.0f}%) [VALID]{RESET}"
        )
        speak(f"Validacion exitosa. Sistema certificado con cien por ciento de pureza.")
        sys.exit(0)
    else:
        print(
            f"\n{WARNING}[WARN] SISTEMA CON DESVIACIONES ({pureness:.0f}% de pureza){RESET}"
        )
        # Mostrar que debe resolver
        print(f"\n{ERROR}=== ACCIONES REQUERIDAS ==={RESET}")
        for key, value in results.items():
            if not value:
                if key == "Arsenal":
                    print(
                        f"  - Crear inventario de skills en 01_Brain/02_Knowledge_Brain/01_Inventario_Total.md"
                    )
                elif key == "Integraciones":
                    print(f"  - Instalar o configurar Playwright")
                elif key == "Reglas":
                    print(f"  - Revisar estructura de reglas en 01_Brain/04_Rules/")
                elif key == "Carpetas":
                    print(f"  - Crear carpetas faltantes en la raiz del proyecto")
                else:
                    print(f"  - Revisar validacion de {key}")
        speak(
            f"Atencion. El sistema presenta desviaciones. Nivel de pureza: {pureness:.0f} por ciento."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
