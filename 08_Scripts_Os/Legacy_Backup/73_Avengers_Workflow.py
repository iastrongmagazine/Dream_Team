#!/usr/bin/env python3
"""
73_Avengers_Workflow.py - Avengers Compound Flow
Ejecuta: Vision_Review -> Hulk_Compound (en loop)
"""

import subprocess
import os
import sys
import io

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# ARMOR LAYER - PATH RESOLUTION
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# Navegar desde Legacy_Backup -> 08_Scripts_Os -> 04_Engine -> ROOT
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(SCRIPT_DIR)))
LEGACY_BACKUP_DIR = SCRIPT_DIR

# Agregar al path para imports
sys.path.insert(0, os.path.join(PROJECT_ROOT, "04_Engine", "08_Scripts_Os"))
os.environ["PERSONAL_OS_ROOT"] = PROJECT_ROOT


def run_workflow(script_name, description, args=None):
    """Ejecuta un script del workflow desde Legacy_Backup."""
    script_path = os.path.join(LEGACY_BACKUP_DIR, script_name)

    if not os.path.exists(script_path):
        print(f"[ERROR] Script no encontrado: {script_path}")
        return False

    print(f"\n--- Ejecutando: {description} ({script_name}) ---")
    try:
        # Armar comando con argumentos
        cmd = [sys.executable, script_path]
        if args:
            cmd.extend(args)

        result = subprocess.run(
            cmd,
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            env={**os.environ, "PERSONAL_OS_ROOT": PROJECT_ROOT},
        )
        if result.returncode == 0:
            print(f"[OK] {description} completado.")
            return True
        else:
            print(f"[ERR] {description} falló.")
            # Mostrar output relevante
            output = result.stdout + result.stderr
            if output:
                print(output[:800])
            return False
    except Exception as e:
        print(f"[ERR] Error ejecutando {script_name}: {e}")
        return False


def main():
    print("=" * 60)
    print("AVENGERS COMPOUND FLOW - PersonalOS")
    print("=" * 60)
    print("[AVENGERS] Iniciando Avengers Compound Flow...")
    print()

    # ============================================================
    # STEP 1: Thor_Work (Vision Review)
    # ============================================================
    print("[1/2] Vision Review - Analisis exhaustivo del codigo")
    # Vision Review requiere un argumento (target)
    if not run_workflow("04_Vision_Review.py", "Vision Review", args=["main"]):
        print("[ABORT] Vision Review falló. Deteniendo workflow.")
        sys.exit(1)

    # ============================================================
    # STEP 2: Hulk_Compound (Compound Intelligence)
    # ============================================================
    print("\n[2/2] Hulk Compound - Capitalizacion de inteligencia")
    if not run_workflow("05_Hulk_Compound.py", "Hulk Compound"):
        print("[ABORT] Hulk Compound falló. Deteniendo workflow.")
        sys.exit(1)

    # ============================================================
    # COMPLETE
    # ============================================================
    print()
    print("=" * 60)
    print("[AVENGERS] Ciclo Avengers completado: Review -> Compound")
    print("=" * 60)


if __name__ == "__main__":
    main()
