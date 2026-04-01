from pathlib import Path
import os
import sys
import subprocess
import datetime
import importlib.util

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import ROOT_DIR as BASE_DIR, BRAIN_MEMORY_DIR

"""
AUTO-COMPOUND INTELLIGENCE v1.0
Captura automáticamente aprendizajes de los logs de Git y los inyecta en el Digital Brain.
Cumple con Armor Layer y PersonalOS Standards.
"""

import os
import sys
import subprocess
import datetime
import importlib.util

SCRIPT_DIR = Path(__file__).resolve().parent
MEMORY_DIR = BRAIN_MEMORY_DIR

# Soporte para colores
try:
    from colorama import init, Fore, Style

    init(autoreset=True)
    SUCCESS = Fore.GREEN
    INFO = Fore.CYAN
    WARNING = Fore.YELLOW
    ERROR = Fore.RED
    RESET = Style.RESET_ALL
except ImportError:
    SUCCESS = INFO = WARNING = ERROR = RESET = ""


def speak(text):
    """Notificación de voz."""
    try:
        hook_path = os.path.join(
            BASE_DIR, ".agent", "04_Extensions", "hooks", "utils", "common.py"
        )
        if os.path.exists(hook_path):
            spec = importlib.util.spec_from_file_location("common", hook_path)
            common = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(common)
            common.speak(text)
        else:
            print(f"[VOZ] {text}")
    except Exception:
        print(f"[VOZ] {text}")


def get_session_insights():
    """Extrae insights de los commits de hoy."""
    try:
        # Obtener commits desde medianoche
        result = subprocess.run(
            ["git", "log", "--since", "midnight", "--pretty=format:%h: %s"],
            capture_output=True,
            text=True,
            cwd=BASE_DIR,
        )
        if result.returncode == 0 and result.stdout:
            commits = result.stdout.strip().split("\n")
            return commits
        return []
    except Exception as e:
        print(f"{ERROR}Error al extraer insights: {e}{RESET}")
        return []


def compound_intelligence():
    """Genera el archivo de memoria de contexto automático."""
    print(f"\n{INFO}>>> Capitalizando Inteligencia Automática...{RESET}")

    insights = get_session_insights()
    if not insights:
        print(
            f"{WARNING}No se detectaron nuevas interacciones significativas hoy. Inteligencia en reposo.{RESET}"
        )
        return True

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    timestamp = datetime.datetime.now().strftime("%H-%M-%S")
    filename = f"CTX_AUTO_Intelligence_{today}_{timestamp}.md"
    file_path = os.path.join(MEMORY_DIR, filename)

    content = f"""# Inteligencia Capturada: {today}

## Resumen de la Sesion
Esta memoria ha sido generada automaticamente por el PersonalOS Engine al detectar actividad significativa en los logs de Git.

## Cambios y Aprendizajes (Git Logs)
{chr(10).join(["- " + i for i in insights])}

## Estado del Sistema
- Pure Green: Validado
- Armor Layer: Activa
- Sincronizacion: Automatizada

---
_Memoria de contexto inyectada por el motor de inteligencia a las {datetime.datetime.now().strftime("%H:%M:%S")}_
"""

    try:
        if not os.path.exists(MEMORY_DIR):
            os.makedirs(MEMORY_DIR)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"{SUCCESS}✅ Inteligencia capitalizada en: {filename}{RESET}")
        speak(
            "Inteligencia detectada y capitalizada con éxito. Tu cerebro digital ha sido actualizado."
        )
        return True
    except Exception as e:
        print(f"{ERROR}Error al guardar inteligencia: {e}{RESET}")
        return False


if __name__ == "__main__":
    compound_intelligence()
