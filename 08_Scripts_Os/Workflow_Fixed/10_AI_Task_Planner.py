import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
"""
INVITUS TASK PLANNER (BATCH MODE): Script para "vitaminar" tareas existentes.
Escanea todas las tareas activas y les anexa el AI Task Planning Framework si aún no lo tienen.
"""

import sys
import os
import glob
import io
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import PROJECT_ROOT, OPERATIONS_TASKS_DIR, BRAIN_TEMPLATE_DIR

# Asegurar encoding UTF-8 en STDOUT para Windows (Evita errores de caracteres especiales)
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Intentar importar colorama, si no está, usar prints simples
try:
    from colorama import init, Fore, Style

    init(autoreset=True)
    SUCCESS = Fore.GREEN
    INFO = Fore.CYAN
    WARNING = Fore.YELLOW
    ERROR = Fore.RED
    RESET = Style.RESET_ALL
except ImportError:
    SUCCESS = ""
    INFO = ""
    WARNING = ""
    ERROR = ""
    RESET = ""

TASK_DIR = OPERATIONS_TASKS_DIR
TEMPLATE_PATH = BRAIN_TEMPLATE_DIR / "01_ai_task_template.md"

# Marcador para detectar si ya tiene el framework
MARKER = "# 🧠 AI Task Planning Framework"
SEPARATOR = f"\n\n---\n{MARKER} (Ajuste de Tareas)\n---\n"


def speak(message):
    """Notificación de voz vía TTS Windows (Protocolo PersonalOS)."""
    try:
        # Escapar comillas simples para PowerShell
        safe_msg = message.replace("'", "")
        os.system(
            f"powershell.exe -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{safe_msg}')\""
        )
    except:
        pass


def print_banner():
    """Banner Premium PersonalOS."""
    banner = f"""
{SUCCESS}######################################################################
#                                                                    #
#             P E R S O N A L   O S   |   W O R K   T H O R          #
#                A I   T A S K   P L A N N E R   V 2 . 2             #
#                                                                    #
######################################################################{RESET}
"""
    print(banner)


def main():
    """Función principal para ejecutar el escaneo y actualización de tareas."""
    print_banner()
    speak("Iniciando inyección de vitaminas técnicas en tareas activas.")

    print(f"{INFO}--- [AI TASK PLANNER: BATCH INJECTION] ---{RESET}\n")

    if not os.path.exists(TASK_DIR):
        print(
            f"{ERROR}Error: No se encontró el directorio de tareas: {TASK_DIR}{RESET}"
        )
        sys.exit(1)

    if not os.path.exists(TEMPLATE_PATH):
        print(f"{ERROR}Error: No se encontró el template: {TEMPLATE_PATH}{RESET}")
        sys.exit(1)

    # Leer el template
    try:
        with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
            template_content = f.read()
    except (OSError, UnicodeError) as e:
        print(f"{ERROR}Error leyendo el template: {e}{RESET}")
        sys.exit(1)

    # Escanear archivos
    tasks_updated = 0
    files = glob.glob(os.path.join(TASK_DIR, "*.md"))
    files.sort()

    print(
        f"{INFO}Analizando {len(files)} archivos en {os.path.basename(TASK_DIR)}...{RESET}"
    )

    for file_path in files:
        # Ignorar README y archivos ocultos/sistema
        fname = os.path.basename(file_path)
        if fname.lower() == "readme.md" or fname.startswith("."):
            continue

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Verificar si ya tiene el framework
            if MARKER in content:
                continue

            # Anexar template al final
            new_content = content + SEPARATOR + template_content
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)

            print(f"{SUCCESS}✔ ACTUALIZADO: {fname}{RESET}")
            tasks_updated += 1

        except (OSError, UnicodeError) as e:
            print(f"{ERROR}Error procesando {fname}: {e}{RESET}")

    print(f"\n{INFO}--- RESUMEN ---{RESET}")
    if tasks_updated > 0:
        msg_success = f"Se han vitaminado {tasks_updated} tareas con el framework."
        print(f"{SUCCESS}{msg_success}{RESET}")
        speak(msg_success)
        print(f"{WARNING}IMPORTANTE PARA EL AGENTE:{RESET}")
        print("1. Revisa los archivos actualizados.")
        print("2. LLENA las secciones de la plantilla anexada con análisis real.")
    else:
        print(
            f"{SUCCESS}Todas las tareas ya están al día. No se requieren acciones.{RESET}"
        )
        speak("Todas las tareas están al día.")


if __name__ == "__main__":
    main()
