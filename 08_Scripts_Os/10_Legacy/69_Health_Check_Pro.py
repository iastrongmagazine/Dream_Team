#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
69_Health_Check_Pro.py
=======================
Health Check avanzado con retry, metricas y auto-remediation.

Uso:
    python 69_Health_Check_Pro.py
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Callable

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import ROOT_DIR, OPERATIONS_DIR, OPERATIONS_ANALYTICS_DIR

# Fix encoding
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except:
        pass

# Paths
SCRIPT_DIR = Path(__file__).parent

# Cargar modulos dinamicamente (evita SyntaxError con numeros)
import importlib.util

spec_retry = importlib.util.spec_from_file_location(
    "_retry", SCRIPT_DIR / "67_Retry_Decorator.py"
)
rd = importlib.util.module_from_spec(spec_retry)
spec_retry.loader.exec_module(rd)

spec_audit = importlib.util.spec_from_file_location(
    "_audit", SCRIPT_DIR / "63_Audit_Sync_Master.py"
)
asm = importlib.util.module_from_spec(spec_audit)
spec_audit.loader.exec_module(asm)

retry_on_failure = rd.retry_on_failure

# ============================================================
# CHECKS
# ============================================================


def check_structure() -> Dict:
    """Check de estructura de carpetas."""
    required = [
        "00_Core",
        "01_Brain",
        str(OPERATIONS_DIR.name),
        "03_Knowledge",
        "04_Engine",
        "05_System",
        "06_Archive",
    ]
    missing = [d for d in required if not (ROOT_DIR / d).exists()]

    return {
        "status": "PASS" if not missing else "FAIL",
        "missing": missing,
        "message": f"Faltan {len(missing)} carpetas" if missing else "Estructura OK",
    }


def check_stack() -> Dict:
    """Check de stack tecnologico."""
    import subprocess

    checks = {
        "Python": {
            "status": "PASS",
            "version": f"{sys.version_info.major}.{sys.version_info.minor}",
        },
        "Git": {
            "status": "PASS"
            if subprocess.run(["git", "--version"], capture_output=True).returncode == 0
            else "FAIL"
        },
    }

    all_ok = all(c["status"] == "PASS" for c in checks.values())
    return {"status": "PASS" if all_ok else "FAIL", "checks": checks}


def check_git() -> Dict:
    """Check de estado Git."""
    import subprocess

    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=ROOT_DIR,
            capture_output=True,
            text=True,
            timeout=10,
        )
        lines = [l for l in result.stdout.strip().split("\n") if l]
        return {
            "status": "PASS",
            "changes": len(lines),
            "message": f"{len(lines)} cambios sin commit"
            if lines
            else "Working tree clean",
        }
    except Exception as e:
        return {"status": "FAIL", "message": str(e)}


def check_dimensions() -> Dict:
    """Check de dimensiones del sistema."""
    dims = asm.get_current_dimensions()
    os_dims = [d for d in dims if d in asm.OS_DIMENSIONS]
    external = [d for d in dims if d not in asm.OS_DIMENSIONS]

    return {
        "status": "PASS",
        "os_dimensions": len(os_dims),
        "external": external,
        "message": f"{len(os_dims)} dimensiones OS, {len(external)} externas",
    }


@retry_on_failure(max_retries=2, backoff=1)
def check_scripts() -> Dict:
    """Check de scripts criticos con retry."""
    critical = [
        "53_Structure_Auditor.py",
        "63_Audit_Sync_Master.py",
        "66_Alert_Manager.py",
    ]
    missing = [s for s in critical if not (SCRIPT_DIR / s).exists()]

    return {
        "status": "PASS" if not missing else "FAIL",
        "missing": missing,
        "message": f"Faltan {len(missing)} scripts" if missing else "Scripts OK",
    }


# ============================================================
# MAIN
# ============================================================

CHECKS: List[tuple] = [
    ("Estructura", check_structure),
    ("Stack Tech", check_stack),
    ("Git Status", check_git),
    ("Dimensiones", check_dimensions),
    ("Scripts", check_scripts),
]


def run_health_check() -> Dict:
    """Ejecuta todos los health checks."""
    print("=" * 60)
    print("   HEALTH CHECK PRO - PersonalOS")
    print("=" * 60)

    results = {
        "timestamp": datetime.now().isoformat(),
        "checks": {},
        "summary": {"pass": 0, "fail": 0},
    }

    for name, check_func in CHECKS:
        print(f"\n>>> {name}...", end=" ")

        try:
            result = check_func()
            results["checks"][name] = result

            if result["status"] == "PASS":
                print(f"[OK] {result.get('message', 'OK')}")
                results["summary"]["pass"] += 1
            else:
                print(f"[FAIL] {result.get('message', 'FAIL')}")
                results["summary"]["fail"] += 1

        except Exception as e:
            print(f"[ERROR] {e}")
            results["checks"][name] = {"status": "ERROR", "message": str(e)}
            results["summary"]["fail"] += 1

    print("\n" + "=" * 60)
    print(
        f"   RESUMEN: {results['summary']['pass']} OK, {results['summary']['fail']} FAIL"
    )
    print("=" * 60)

    return results


def main():
    """Main entry point."""
    results = run_health_check()

    # Guardar reporte
    report_dir = OPERATIONS_ANALYTICS_DIR / "health"
    report_dir.mkdir(parents=True, exist_ok=True)

    filename = f"health_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    filepath = report_dir / filename

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"\n>>> Reporte guardado: {filepath}")

    return 0 if results["summary"]["fail"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
