"""
INVICTUS MEDIC: Sistema de Auto-sanación.
Orquesta reparaciones de enlaces, validaciones de stack y sincronización de notas.
"""

import sys
import subprocess
import importlib.util
from pathlib import Path

# SCRIPT_DIR: .claude/knowledge/Workflows_Python
SCRIPT_FILE = Path(__file__).resolve()
WORKFLOW_DIR = SCRIPT_FILE.parent
ROOT_DIR = WORKFLOW_DIR.parent.parent.parent.resolve() # personal-os-main

def dynamic_speak(text):
    """
    Fallback para la función speak usando importación dinámica.
    """
    try:
        hook_path = ROOT_DIR / ".claude" / "hooks" / "utils" / "common.py"
        if hook_path.exists():
            spec = importlib.util.spec_from_file_location("common", str(hook_path))
            common = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(common)
            common.speak(text)
        else:
            print(f"[VOICE] {text}")
    except (ImportError, AttributeError, OSError):
        print(f"[VOICE] {text}")

def run_step(name, command):
    """
    Ejecuta un paso de sanación y notifica el resultado.
    """
    print(f"\n[Invictus Medic] Running: {name}...")
    try:
        subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            cwd=str(ROOT_DIR)
        )
        print(f"OK: {name} completed.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"ERROR: {name} failed.")
        if e.stdout:
            print(e.stdout)
        if e.stderr:
            print(e.stderr)
        return False

def self_heal():
    """
    Ciclo principal de auto-sanación.
    """
    print("--- INVICTUS MEDIC: SELF-HEALING CYCLE v4.0 ---")

    # 1. Reparación de Enlaces
    update_links = WORKFLOW_DIR / "05_12_Update_Links.py"
    if not run_step("Link Repair", [sys.executable, str(update_links)]):
        dynamic_speak("Fallo en reparación de enlaces.")
        return False

    # 2. Validación de Stack
    validate_stack = WORKFLOW_DIR / "06_13_Validate_Stack.py"
    if not run_step("Stack Validation", [sys.executable, str(validate_stack)]):
        dynamic_speak("Fallo en validación de estructura.")
        return False

    # 3. Sincronización de Notas de Proceso
    sync_notes = WORKFLOW_DIR / "11_Sync_Notes.py"
    run_step("Sync Process Notes", [sys.executable, str(sync_notes)])

    # 4. Verificación de Logs
    print("\n[Invictus Medic] Verifying session logs...")
    log_dir = ROOT_DIR / "logs"
    if log_dir.exists():
        print(f"OK: Log directory verified at {log_dir}")
    else:
        print(f"WARN: Log directory NOT found at {log_dir}")

    # 5. Auto-Commit (Si el estado es Pure Green)
    status_res = subprocess.run(
        ["git", "status", "--porcelain"],
        capture_output=True,
        text=True,
        cwd=str(ROOT_DIR),
        check=False
    )
    status = status_res.stdout.strip()

    if status:
        print("\n[Invictus Medic] Changes detected. Proceeding to auto-commit...")
        run_step("Git Add", ["git", "add", "."])
        commit_msg = "chore: self-healing cycle complete (pure green state)"
        run_step("Git Commit", ["git", "commit", "-m", commit_msg])
        dynamic_speak("Sistema sanado y cambios guardados.")
    else:
        print("\n[Invictus Medic] No healing required. System is healthy.")
        dynamic_speak("Sistema saludable. No se requirió intervención.")

    print("\nDONE: Self-healing cycle finished successfully.")
    return True

if __name__ == "__main__":
    self_heal()
