"""
54_Commit_Guard.py - Compound Workflow: Structure Audit + Engineering Audit + Commit
====================================================================================
Ejecuta validación completa ANTES de permitir commit.

Flujo:
  1. Structure Audit (53) → Si falla, ABORT
  2. Engineering Audit (42) → Si falla, ABORT
  3. Git Commit (si todo OK)

Este script es EL GUARDIÁN del sistema Pure Green.
Nunca permite un commit que rompa la estructura o las reglas de ingeniería.

Uso:
  python 04_Engine/08_Scripts_Os/54_Commit_Guard.py -m "feat: description"
  python 04_Engine/08_Scripts_Os/54_Commit_Guard.py -m "fix: description" archivo.py
"""

import sys
import subprocess
import os
from config_paths import ROOT_DIR


def run_script(path, desc):
    print(f"\n{'=' * 60}")
    print(f"STEP: {desc}")
    print(f"{'=' * 60}")
    result = subprocess.run([sys.executable, path])
    return result.returncode == 0


def main():
    # Verificar que hay argumentos para commit
    if len(sys.argv) < 2:
        print("Uso: python 54_Commit_Guard.py -m 'mensaje' [archivos]")
        print("\nEjemplo: python 54_Commit_Guard.py -m 'feat: nuevo feature'")
        sys.exit(1)

    # 1. Structure Audit
    if not run_script(
        os.path.join(ROOT_DIR, "04_Engine", "08_Scripts_Os", "53_Structure_Auditor.py"),
        "STRUCTURE AUDIT",
    ):
        print("\n[ABORT] Estructura del proyecto falló")
        sys.exit(1)

    # 2. Engineering Audit (Pure Green)
    if not run_script(
        os.path.join(ROOT_DIR, "04_Engine", "08_Scripts_Os", "42_Audit_Engineering.py"),
        "ENGINEERING AUDIT",
    ):
        print("\n[ABORT] Pure Green no aprobado")
        sys.exit(1)

    # 3. Git Commit
    print(f"\n{'=' * 60}")
    print("STEP: GIT COMMIT")
    print(f"{'=' * 60}")

    git_args = ["git", "commit"] + sys.argv[1:]
    print(f"Ejecutando: {' '.join(git_args)}\n")

    try:
        subprocess.run(git_args, check=True)
        print("\n[SUCCESS] Commit realizado con éxito")
    except subprocess.CalledProcessError as e:
        print(f"\n[ABORT] Git commit falló: {e}")
        sys.exit(e.returncode)


if __name__ == "__main__":
    main()
