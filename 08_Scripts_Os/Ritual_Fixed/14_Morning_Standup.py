import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
"""
14_Morning_Standup.py - Armor Layer Protected
"""

import os
import sys
import glob
import io
import subprocess
from pathlib import Path
from datetime import datetime
from colorama import Fore, Style, init

init()

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import (ROOT_DIR, BRAIN_DIR, BRAIN_RULES_DIR, COMPOUND_ENGINE_DIR, ENGINE_DIR)
    PROJECT_ROOT,
    BRAIN_DIR as BRAIN_DIR_IMPORTED,
    CORE_DIR as CORE_DIR_IMPORTED,
    OPERATIONS_DIR as OPERATIONS_DIR_IMPORTED,
    BRAIN_MEMORY_DIR,
    BRAIN_NOTES_DIR,
    KNOWLEDGE_DIR,
)

REQUIRED_DIRS = [
    "00_Core",
    "01_Brain",
    "02_Operations",
    "03_Knowledge",
    "04_Engine",
    "05_System",
    "06_Archive",
]
for d in REQUIRED_DIRS:
    if not (PROJECT_ROOT / d).exists():
        print(f"[WARN] Required directory not found: {d}")

BRAIN_DIR = BRAIN_DIR_IMPORTED
CORE_DIR = CORE_DIR_IMPORTED
OPERATIONS_DIR = OPERATIONS_DIR_IMPORTED
CONTEXT_MEMORY_DIR = BRAIN_MEMORY_DIR
PROCESS_NOTES_DIR = BRAIN_NOTES_DIR

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


def print_banner():
    banner = rf"""
{Fore.YELLOW}    ###########################################################################
    #                                                                         #
    #      __  __  ____  _____  _   _ _____ _   _  _____   _____ _____        #
    #     |  \/  |/ __ \|  __ \| \ | |_   _| \ | |/ ____| / ____|  __ \       #
    #     | \  / | |  | | |__) |  \| | | | |  \| | |  __ | (___ | |__) |      #
    #     | |\/| | |  | |  _  /| . ` | | | | . ` | | |_ | \___ \|  ___/       #
    #     | |  | | |__| | | \ \| |\  |_| |_| |\  | |__| | ____) | |           #
    #     |_|  |_|\____/|_|  \_\_| \_|_____|_| \_|\_____||_____/|_|           #
    #                                                                         #
    #                    M O R N I N G   S T A N D U P                        #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


# Rutas utilizando constantes centralizadas
CONTEXT_MEMORY_DIR = os.path.join(BRAIN_DIR, "01_Context_Memory")
PROCESS_NOTES_DIR = os.path.join(BRAIN_DIR, "03_Process_Notes")
GOALS_FILE = os.path.join(CORE_DIR, "GOALS.md")
BACKLOG_FILE = os.path.join(CORE_DIR, "BACKLOG.md")
OPERATIONS_DIR = OPERATIONS_DIR  # Usando la constante importada directamente


def get_latest_file(directory, pattern="*.md"):
    """Obtiene el archivo más reciente."""
    if not os.path.exists(directory):
        return None
    files = glob.glob(os.path.join(directory, pattern))
    if not files:
        return None
    return max(files, key=os.path.getmtime)


def read_file_summary(path, lines=15):
    """Lee el encabezado de un archivo."""
    if not path or not os.path.exists(path):
        return "No disponible."
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = [next(f).strip() for _ in range(lines) if f]
        return "\n".join(content[:lines])
    except Exception:
        return "Error al leer el archivo."


def count_active_tasks():
    """Cuenta tareas activas P0/P1."""
    tasks_dir = os.path.join(OPERATIONS_DIR, "01_Active_Tasks")
    if not os.path.exists(tasks_dir):
        return 0, 0

    p0_count = 0
    p1_count = 0

    for f in os.listdir(tasks_dir):
        if f.endswith(".md"):
            try:
                with open(os.path.join(tasks_dir, f), "r", encoding="utf-8") as file:
                    content = file.read().lower()
                    if "priority: p0" in content:
                        p0_count += 1
                    if "priority: p1" in content:
                        p1_count += 1
            except:
                pass

    return p0_count, p1_count


def format_date():
    """Retorna fecha en formato dd/mm/aaaa."""
    return datetime.now().strftime("%d/%m/%Y")


def morning_standup():
    """Ejecuta el standup matutino."""
    print_banner()
    dynamic_speak("Iniciando Standup Matutino")

    print(f"{Fore.CYAN}{'=' * 75}{Style.RESET_ALL}")
    print(f"☀️  MORNING STANDUP - {format_date()}")
    print(f"{Fore.CYAN}{'=' * 75}{Style.RESET_ALL}")

    # [10%] Iniciando
    print("\n[10%] 🔍 Analizando contexto del sistema...")

    # 1. Leer Inventario Total
    print("\n📖 LEYENDO INVENTARIO VIVO...")
    inventario = KNOWLEDGE_DIR / "01_Inventario_Total.md"
    if os.path.exists(inventario):
        print(f"   ✅ Inventario: {os.path.basename(inventario)}")
    else:
        print("   ⚠️ Inventario no encontrado")

    # [30%] Contexto CTX
    print("\n[30%] 🧠 Recuperando mi contexto (CTX)...")
    latest_ctx = get_latest_file(CONTEXT_MEMORY_DIR, "CTX_*.md")
    if latest_ctx:
        ctx_name = os.path.basename(latest_ctx)
        print(f"   ✅ Último CTX: {ctx_name}")
        # Mostrar encabezado del CTX
        ctx_summary = read_file_summary(latest_ctx, 8)
        print("\n   📋 Resumen del CTX:")
        for line in ctx_summary.split("\n")[:5]:
            if line.strip():
                print(f"      {line[:60]}...")
    else:
        print("   ℹ️  No hay CTX previo - primera sesión")

    # [50%] Process Notes
    print("\n[50%] 📝 Recuperando notas del usuario...")
    latest_note = get_latest_file(PROCESS_NOTES_DIR, "*.md")
    if latest_note:
        note_name = os.path.basename(latest_note)
        print(f"   ✅ Última nota: {note_name}")
    else:
        print("   ℹ️  No hay notas de proceso")

    # [70%] Goals y Backlog
    print("\n[70%] 🎯 Analizando prioridades...")

    p0_count, p1_count = count_active_tasks()
    print(f"   📊 Tareas activas: P0: {p0_count} | P1: {p1_count}")

    if os.path.exists(GOALS_FILE):
        print("   ✅ GOALS.md cargado")
    if os.path.exists(BACKLOG_FILE):
        print("   ✅ BACKLOG.md cargado")

    # [90%] Plan del día
    print("\n[90%] 📋 Preparando plan del día...")

    # [100%] Completado
    print("\n[100%] ✅ Análisis completo - Listo para trabajar")

    print("\n" + "=" * 75)
    print(f"{Fore.GREEN}☀️  PROTOCOLO DE CONCIENCIA ACTIVADO{Style.RESET_ALL}")
    print("=" * 75)

    print(f"\n{Fore.YELLOW}📌 THE BIG 3 (Prioridades del día):{Style.RESET_ALL}")
    print("   1. Completar tarea P0 más antigua")
    print("   2. Avanzar en objetivo principal de GOALS.md")
    print("   3. Documentar aprendizajes al cerrar")

    print(
        f"\n{Fore.CYAN}💡 Recordatorio: Usar 10% reporting en cada tarea multi-paso{Style.RESET_ALL}"
    )

    dynamic_speak("Protocolo de conciencia activado. ¿En qué trabajaremos hoy?")

    print("\n" + "=" * 75)
    print("🎯 ¿En qué deberíamos trabajar hoy?")
    print("=" * 75 + "\n")

    return {
        "fecha": format_date(),
        "ctx": os.path.basename(latest_ctx) if latest_ctx else "Sin CTX previo",
        "nota": os.path.basename(latest_note) if latest_note else "Sin notas",
        "p0": p0_count,
        "p1": p1_count,
        "estado": "✅ Listo",
    }


if __name__ == "__main__":
    result = morning_standup()
    print(f"\n📊 Resumen: {result}")
