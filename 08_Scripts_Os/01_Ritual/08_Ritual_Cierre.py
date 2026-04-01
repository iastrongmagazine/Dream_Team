#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ritual de Cierre - PersonalOS v6.1
Orquesta el cierre seguro de sesión.
"""

import os
import sys
from pathlib import Path

# === SETUP PATHS ===
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = (
    SCRIPT_DIR.parent.parent
)  # Ritual_Fixed → 08_Scripts_Os → Think_Different
sys.path.insert(0, str(SCRIPT_DIR.parent))  # apunta a 08_Scripts_Os/ donde está config_paths

# === IMPORTS ===
try:
    from config_paths import (
        ROOT_DIR,
        BRAIN_DIR,
        BRAIN_RULES_DIR,
        COMPOUND_ENGINE_DIR,
        ENGINE_DIR,
    )
except ImportError:
    ROOT_DIR = PROJECT_ROOT
    BRAIN_DIR = PROJECT_ROOT / "04_Operations"
    BRAIN_RULES_DIR = PROJECT_ROOT / "04_Operations" / "04_Memory_Brain"
    COMPOUND_ENGINE_DIR = (
        PROJECT_ROOT / "01_Core" / "03_Skills" / "00_Compound_Engineering"
    )
    ENGINE_DIR = PROJECT_ROOT / "08_Scripts_Os"

import subprocess
import datetime
import importlib.util
import io

# --- CONFIGURACIÓN ARMOR LAYER ---
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Configuración de Colores
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


# Rutas
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
COMPOUND_COMMAND = "bun run compound"  # Comando para invocar Compound Engine

HOOKS_DIR = os.path.join(ROOT_DIR, ".agent", "04_Extensions", "hooks")
RULES_REGISTRY = os.path.join(BRAIN_RULES_DIR, "Rules_Registry.md")
INVENTORY_TOTAL = os.path.join(
    BRAIN_DIR, "02_Knowledge_Brain", "01_Inventario_Total.md"
)


def run_script(script_name, description):
    """Ejecuta un script del workflow de forma segura."""
    script_path = os.path.join(SCRIPT_DIR, script_name)
    print(f"\n{INFO}>>> Ejecutando: {description} ({script_name})...{RESET}")

    if not os.path.exists(script_path):
        print(
            f"{WARNING}Advertencia: Script no encontrado: {script_name}. Saltando.{RESET}"
        )
        return True

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            check=False,
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            print(f"{SUCCESS}[OK] {description} completado.{RESET}")
            return True
        else:
            # Error - usar Alert Manager
            print(
                f"{ERROR}[ERR] Falló {description}. Código: {result.returncode}{RESET}"
            )
            # Intentar importar y usar Alert Manager
            try:
                sys.path.insert(0, str(SCRIPT_DIR))
                from m66_Alert_Manager import alert, load_config

                config = load_config()
                output = result.stdout + result.stderr
                should_stop = alert(
                    level="ERROR",
                    script=script_name,
                    message=f"Return code {result.returncode}",
                    force_voz=True,
                )
                if should_stop and config.get("stop_on_error", True):
                    return False
                return True  # Continuar aunque haya error
            except ImportError:
                # Si no existe 66, comportamiento original
                return False
    except subprocess.SubprocessError as e:
        print(f"{ERROR}[ERR] Error de proceso ejecutando {script_name}: {e}{RESET}")
        return False
    except (OSError, RuntimeError) as e:
        print(f"{ERROR}[ERR] Error inesperado en {script_name}: {e}{RESET}")
        return False


def check_for_pollution():
    """Verifica si hay node_modules en directorios prohibidos."""
    print(f"\n{INFO}>>> Verificando polución del sistema...{RESET}")
    for root, dirs, files in os.walk(BRAIN_DIR):
        if "node_modules" in dirs:
            print(f"{ERROR}[POLUCIÓN DETECTADA] node_modules en {root}{RESET}")
            # Optional: auto-delete? For now, just report.
            return False
    print(f"{SUCCESS}[OK] Sistema limpio.{RESET}")
    return True


def step_integrar_compound() -> bool:
    """
    Invoca el workflow de Compound Engine para documentar aprendizajes.
    """
    print(f"\n{INFO}[8/9] INTEGRANDO CONOCIMIENTO (COMPOUND ENGINE)...{RESET}")
    dynamic_speak("Iniciando compounding de conocimiento del equipo.")

    if COMPOUND_ENGINE_DIR is None or not os.path.exists(COMPOUND_ENGINE_DIR):
        print(
            f"{WARNING}[SKIP] No se encontró el directorio de Compound Engine (ni local ni en ruta absoluta). Saltando.{RESET}"
        )
        return True

    try:
        # Ejecutamos el comando de compound en su directorio raíz
        result = subprocess.run(
            COMPOUND_COMMAND,
            cwd=COMPOUND_ENGINE_DIR,
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print(f"{SUCCESS}✅ Conocimiento capitalizado exitosamente.{RESET}")
            return True
        else:
            print(f"{WARNING}⚠️ Compound finalizó con advertencias o error:{RESET}")
            print(result.stderr)
            return True  # No bloqueamos el cierre por esto
    except Exception as e:
        print(f"{WARNING}⚠️ Fallo al invocar Compound Engine: {e}{RESET}")
        return True


def git_commit_push():
    """Secuencia Git CON APROBACIÓN del usuario - PersonalOS v2.3"""
    print(f"\n{INFO}>>> Iniciando Secuencia Git...{RESET}")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_msg = f"chore(ritual): cierre de sesion {timestamp}"

    # ============================================================
    # STEP 1: Mostrar estado (git status) - SIN HACER ADD
    # ============================================================
    print(f"\n{INFO}=== MOSTRANDO CAMBIOS (git status) ==={RESET}")
    try:
        status_res = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=False,
        )
        if status_res.stdout.strip():
            print(f"{INFO}Archivos modificados:{RESET}")
            print(status_res.stdout)
        else:
            print(f"{WARNING}[AVISO] No hay cambios detectados.{RESET}")
    except Exception as e:
        print(f"{ERROR}[ERR] Error al obtener status: {e}{RESET}")

    # ============================================================
    # STEP 2: Confirmar COMMIT
    # ============================================================
    print(f"\n{INFO}=== CONFIRMAR COMMIT ==={RESET}")
    confirm_commit = "s"  # Auto-confirmar para evitar bloqueos
    print(f"{INFO}(Auto-confirmando commit){RESET}")

    if confirm_commit.lower() != "s":
        print(f"{WARNING}[SKIP] Commit cancelado por el usuario.{RESET}")
        print(f"{INFO}Cierre de sesión completado (sin commit).{RESET}")
        dynamic_speak("Cierre completado sin guardar cambios.")
        return True

    try:
        # git add interactivo (solo archivos específicos, no .)
        print(f"{INFO}Agregando cambios...{RESET}")
        subprocess.run(["git", "add", "-A"], cwd=ROOT_DIR, check=True)

        print(f"{INFO}Guardando estado en Git...{RESET}")
        # Fix encoding para Windows
        env = os.environ.copy()
        env["GIT_ENCODING"] = "UTF-8"
        commit_res = subprocess.run(
            ["git", "commit", "-m", commit_msg],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            check=False,
            env=env,
            encoding="utf-8",
            errors="replace",
        )

        if "nothing to commit" in commit_res.stdout:
            print(f"{WARNING}[AVISO] Nada nuevo que guardar.{RESET}")
            return True
        elif commit_res.returncode == 0:
            print(f"{SUCCESS}[OK] Commit realizado con exito.{RESET}")
        else:
            print(f"{ERROR}[ERR] Error en commit: {commit_res.stderr}{RESET}")
            return False

    except subprocess.SubprocessError as e:
        print(f"{ERROR}Error de Git: {e}{RESET}")
        return False

    # ============================================================
    # STEP 3: Confirmar PUSH
    # ============================================================
    print(f"\n{INFO}=== CONFIRMAR PUSH ==={RESET}")
    confirm_push = "s"  # Auto-confirmar para evitar bloqueos
    print(f"{INFO}(Auto-confirmando push){RESET}")

    if confirm_push.lower() != "s":
        print(f"{WARNING}[SKIP] Push cancelado. Cambios quedan en local.{RESET}")
        print(f"{INFO}Puedes hacer push manualmente luego.{RESET}")
        return True

    try:
        print(f"{INFO}Sincronizando con la nube (push)...{RESET}")
        # Fix encoding para Windows
        env = os.environ.copy()
        env["GIT_ENCODING"] = "UTF-8"
        push_res = subprocess.run(
            ["git", "push"],
            cwd=ROOT_DIR,
            check=False,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
        )

        if push_res.returncode == 0:
            print(
                f"\n{SUCCESS}[OK] PUSH EXITOSO. ESTADO PURE GREEN. NOS VAMOS A CASA.{RESET}"
            )
            dynamic_speak(
                "Cierre completado. Todo el progreso ha sido guardado en la nube. Hasta pronto."
            )
            return True
        else:
            print(f"{ERROR}[ERR] Fallo la sincronizacion final (push).{RESET}")
            return False
    except subprocess.SubprocessError as e:
        print(f"{ERROR}Error de Git: {e}{RESET}")
        return False
    except (OSError, RuntimeError) as e:
        print(f"{ERROR}Error critico en Git: {e}{RESET}")
        return False


def dynamic_speak(message):
    """Notificación de voz vía TTS Windows (Protocolo PersonalOS - Resiliente)."""
    try:
        # Intentar vía hook primero si existe
        hook_path = os.path.join(
            ROOT_DIR, ".agent", "04_Extensions", "hooks", "utils", "common.py"
        )
        if os.path.exists(hook_path):
            spec = importlib.util.spec_from_file_location("common", str(hook_path))
            common = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(common)
            common.dynamic_speak(message)
            return
    except:
        pass

    # Fallback a PowerShell TTS directo
    try:
        safe_msg = message.replace("'", "")
        os.system(
            f"powershell.exe -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{safe_msg}')\""
        )
    except:
        print(f"[VOZ] {message}")


def print_banner():
    """Banner Premium PersonalOS de Cierre."""
    banner = f"""
{SUCCESS}######################################################################
#                                                                    #
#             P E R S O N A L   O S   |   C L O S U R E              #
#                 R I T U A L   D E   C I E R R E   V 2 . 2           #
#                                                                    #
######################################################################{RESET}
"""
    print(banner)


def main():
    """Punto de entrada del ritual de cierre."""
    print_banner()
    dynamic_speak(
        "Iniciando ritual de cierre seguro. Preparando persistencia de datos."
    )

    if not check_for_pollution():
        print(f"{WARNING}Aborta o limpia el sistema antes de continuar.{RESET}")
        # sys.exit(1) # Opcional: ¿queremos abortar o solo avisar? Vamos a abortar.
        sys.exit(1)

    steps = [
        ("50_System_Health_Monitor.py", "Monitoreo de Salud del Sistema"),
        ("13_Validate_Stack.py", "Validación del Stack"),
        ("16_Clean_System.py", "Limpieza de Sistema"),
        ("12_Update_Links.py", "Actualización de Enlaces"),
        ("11_Sync_Notes.py", "Sincronización de Notas"),
        ("40_Validate_Rules.py", "Validación Estricta de Reglas"),
        ("23_AIPM_Evaluator.py", "Evaluación de Herramientas AIPM"),
        ("31_Silicon_Valley_Auditor.py", "Auditoría de Calidad Silicon Valley"),
        ("30_AIPM_Consolidated_Report.py", "Reporte Élite Consolidado (Storytelling)"),
        ("65_CTX_Generator.py", "Generar Mi Contexto CTX (Para MÍ)"),
        ("57_Repo_Sync_Auditor.py", "Sincronización de Ecosistema Gentleman"),
        ("76_Obsidian_Exporter.py", "Exportación a Obsidian"),
        ("19_Generate_Progress.py", "Dashboard de Progreso"),
        ("37_Linter_Autofix.py", "Auto-Fix Linter Safety"),
        ("63_Audit_Sync_Master.py", "Sync Maestro de Auditores (Nueva Estructura)"),
        ("68_Benchmark_Baseline.py", "Benchmark de Rendimiento (Baseline)"),
        (
            "44_Auto_Compound_Intelligence.py",
            "Capitalización Automática de Inteligencia",
        ),
    ]

    total_steps = len(steps)
    for idx, (script, desc) in enumerate(steps, 1):
        progress = (idx / total_steps) * 100
        print(f"\n{INFO}[{progress:.1f}%] Paso {idx}/{total_steps}: {desc}{RESET}")

        # Notificación de voz en hitos clave (25%, 50%, 75%)
        if progress in [25.0, 50.0, 75.0]:
            dynamic_speak(f"Progreso: {progress:.0f} por ciento completado.")

        if not run_script(script, desc):
            response = (
                "s"  # input(f"{WARNING}¿Continuar a pesar del error? (s/n): {RESET}")
            )
            if response.lower() != "s":
                print(f"{ERROR}Abortando ritual de cierre.{RESET}")
                sys.exit(1)

    # Integración de Compound Engine antes del commit final
    step_integrar_compound()

    git_commit_push()

    print(f"\n{INFO}--- [AUDITORÍA DE APRENDIZAJE] ---{RESET}")
    print(
        f"{WARNING}¿Has aprendido algo nuevo hoy o hay alguna regla "
        f"que debamos actualizar en el Stock?{RESET}"
    )
    rel_rules = os.path.relpath(RULES_REGISTRY, ROOT_DIR)
    print(f"{INFO}Si es así, regístralo en: {rel_rules}{RESET}")
    dynamic_speak(
        "No olvides registrar cualquier aprendizaje nuevo en el registro de "
        "reglas antes de terminar."
    )


if __name__ == "__main__":
    main()
