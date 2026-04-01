#!/usr/bin/env python3
"""
87_Iron_Man_Gen.py — Genesis (Iron Man Boot) Workflow Automation
Carga contexto completo del sistema: reglas, memoria y notas de proceso.
Basado en: .agent/03_Workflows/01_Iron_Man_Gen.md
"""

import os
import sys
import io
import subprocess
from pathlib import Path
from datetime import datetime

try:
    from colorama import init, Fore, Style

    init()
except ImportError:
    # Fallback sin colorama
    class Fore:
        GREEN = YELLOW = RED = CYAN = MAGENTA = BLUE = ""

    class Style:
        RESET_ALL = ""


# =============================================================================
# ARMOR LAYER - PATH RESOLUTION (3-LEVEL)
# =============================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))

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
{Fore.GREEN}    ###########################################################################
    #                                                                         #
    #       _____ _      _______           __  __                             #
    #      |_   _| |    |__   __|/\       |  \/  |                            #
    #        | | | |__     | |  /  \   ___| \  / | ___ _ __  _ __   ___       #
    #        | | | '_ \    | | / /\ \ / __| |\/| |/ _ \ '_ \| '_ \ / _ \      #
    #       _| |_| |_) |  | |/ ____ \ (__| |  | |  __/ | | | | | |  __/      #
    #      |_____|_.__/   |_/_/    \_\___|_|  |_|\___|_| |_|_| |_|\___|      #
    #                                                                         #
    #                    🧬 GENESIS BOOT — PERSONAL OS                       #
    #                  Load Rules · Memory · Process Notes                    #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


# =============================================================================
# VALIDATION FUNCTIONS
# =============================================================================


def check_file_exists(path, description):
    """Verifica si un archivo existe y reporta."""
    full_path = os.path.join(PROJECT_ROOT, path) if not os.path.isabs(path) else path
    if os.path.exists(full_path):
        print(f"{Fore.GREEN}[OK] {description}: {path}{Style.RESET_ALL}")
        return True
    else:
        print(
            f"{Fore.YELLOW}[SKIP] {description}: no encontrado ({path}){Style.RESET_ALL}"
        )
        return False


def read_file_content(path, description, max_lines=50):
    """Lee contenido de un archivo y retorna las primeras líneas."""
    full_path = os.path.join(PROJECT_ROOT, path) if not os.path.isabs(path) else path
    if os.path.exists(full_path):
        try:
            with open(full_path, "r", encoding="utf-8", errors="replace") as f:
                lines = f.readlines()
            preview = "".join(lines[:max_lines])
            if len(lines) > max_lines:
                preview += f"\n... ({len(lines) - max_lines} líneas más)"
            return preview
        except Exception as e:
            return f"[ERROR] No se pudo leer: {e}"
    return "[NOT FOUND]"


def load_session_rules():
    """Paso 1: Cargar reglas de sesión."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("📜 PASO 1: REGLAS DE SESIÓN")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    rules_path = os.path.join(
        PROJECT_ROOT, ".cursor", "00_Rules", "01_Context_Protocol.mdc"
    )
    check_file_exists(".cursor/00_Rules/01_Context_Protocol.mdc", "Protocolo de Sesión")

    rules_dir = os.path.join(PROJECT_ROOT, ".cursor", "00_Rules")
    if os.path.isdir(rules_dir):
        always_apply = [
            f for f in os.listdir(rules_dir) if f.endswith(".mdc") or f.endswith(".md")
        ]
        print(f"  Archivos de reglas encontrados: {len(always_apply)}")
        for f in always_apply[:5]:
            print(f"    - {f}")


def load_long_term_memory():
    """Paso 2: Cargar memoria de largo plazo."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("🧠 PASO 2: MEMORIA DE LARGO PLAZO")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    memory_dir = os.path.join(PROJECT_ROOT, "01_Brain", "01_Context_Memory")
    if os.path.isdir(memory_dir):
        files = [
            f
            for f in os.listdir(memory_dir)
            if f.endswith(".md") or f.endswith(".json")
        ]
        files.sort(reverse=True)  # Más recientes primero
        print(f"  Archivos de memoria: {len(files)}")
        for f in files[:5]:
            print(f"    - {f}")

    # Mapa del sistema
    system_map = "01_Brain/07_Memory_Brain/00_MAPEOS/01_System_Map_2026-03-24.md"
    check_file_exists(system_map, "Mapa del Sistema")


def load_process_notes():
    """Paso 3: Revisar notas de proceso."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("📝 PASO 3: NOTAS DE PROCESO")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    notes_dir = os.path.join(PROJECT_ROOT, "01_Brain", "03_Process_Notes")
    if os.path.isdir(notes_dir):
        files = [f for f in os.listdir(notes_dir) if f.endswith(".md")]
        files.sort(reverse=True)
        print(f"  Notas de proceso: {len(files)}")
        for f in files[:5]:
            print(f"    - {f}")


def sync_task_status():
    """Paso 4: Sincronizar estado de tareas."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("📋 PASO 4: ESTADO DE TAREAS")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    tasks_dir = os.path.join(PROJECT_ROOT, "02_Operations", "01_Active_Tasks")
    if os.path.isdir(tasks_dir):
        files = [f for f in os.listdir(tasks_dir) if f.endswith(".md")]
        print(f"  Tareas activas: {len(files)}")
        for f in files[:3]:
            print(f"    - {f}")

    check_file_exists("00_Core/GOALS.md", "Metas (GOALS.md)")


def check_mcps():
    """Paso 5: Verificar MCPs disponibles."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("🔌 PASO 5: MCPs DISPONIBLES")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    mcp_config = os.path.join(PROJECT_ROOT, ".claude", "mcp.json")
    if os.path.exists(mcp_config):
        print(f"{Fore.GREEN}[OK] MCP config encontrado{Style.RESET_ALL}")
    else:
        print(f"{Fore.YELLOW}[SKIP] MCP config no encontrado{Style.RESET_ALL}")

    print(f"  Playwright MCP: disponible para navegación web")
    print(f"  Fireflies MCP: disponible si FIREFLIES_API_KEY configurada")


def get_git_status():
    """Obtiene estado actual de Git."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--pretty=format:%h - %s (%cr)"],
            capture_output=True,
            text=True,
            check=False,
            cwd=PROJECT_ROOT,
        )
        last_commit = (
            result.stdout.strip() if result.returncode == 0 else "No disponible"
        )

        result2 = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=False,
            cwd=PROJECT_ROOT,
        )
        changes = (
            len(result2.stdout.strip().split("\n")) if result2.stdout.strip() else 0
        )

        return last_commit, changes
    except:
        return "Git no disponible", 0


def generate_context_summary():
    """Paso 6: Generar resumen de contexto."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("📊 RESUMEN DE CONTEXTO")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    last_commit, changes = get_git_status()
    print(f"\n{Fore.GREEN}Git:{Style.RESET_ALL}")
    print(f"  Último commit: {last_commit}")
    print(f"  Cambios pendientes: {changes}")

    # Agentes disponibles
    agents_dir = os.path.join(PROJECT_ROOT, ".claude", "agents")
    if os.path.isdir(agents_dir):
        agents = [
            f
            for f in os.listdir(agents_dir)
            if f.endswith(".md") or f.endswith(".json")
        ]
        print(f"\n{Fore.GREEN}Agentes disponibles:{Style.RESET_ALL} {len(agents)}")

    # Skills
    skills_dir = os.path.join(PROJECT_ROOT, ".agent", "02_Skills")
    if os.path.isdir(skills_dir):
        categories = [
            d
            for d in os.listdir(skills_dir)
            if os.path.isdir(os.path.join(skills_dir, d))
        ]
        print(f"{Fore.GREEN}Categorías de skills:{Style.RESET_ALL} {len(categories)}")


def main():
    """Ejecuta el workflow Genesis (Iron Man Boot)."""
    print_banner()
    dynamic_speak("Iniciando Genesis — carga de contexto completo")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{Fore.MAGENTA}🕐 Sesión iniciada: {timestamp}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}📁 Proyecto: {PROJECT_ROOT}{Style.RESET_ALL}\n")

    # Ejecutar pasos del workflow
    load_session_rules()
    load_long_term_memory()
    load_process_notes()
    sync_task_status()
    check_mcps()
    generate_context_summary()

    print(f"\n{Fore.GREEN}{'=' * 60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}🧬 GENESIS COMPLETO — Contexto cargado{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'=' * 60}{Style.RESET_ALL}")

    dynamic_speak("Genesis completado — listo para trabajar")


if __name__ == "__main__":
    main()
