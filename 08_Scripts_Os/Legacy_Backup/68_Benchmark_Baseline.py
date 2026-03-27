#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
68_Benchmark_Baseline.py
=======================
Crea un baseline de rendimiento para los scripts críticos del sistema.

Ejecuta los scripts principales y mide:
- Tiempo de ejecución
- Uso de memoria
- Exit codes

Uso:
    python 68_Benchmark_Baseline.py
"""

import os
import sys
import time
import json
import subprocess
import psutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import ROOT_DIR, OPERATIONS_ANALYTICS_DIR

# Fix encoding
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except:
        pass

# ============================================================
# CONFIGURACIÓN
# ============================================================

SCRIPT_DIR = Path(__file__).parent.parent  # 04_Engine/08_Scripts_Os/
BENCHMARK_DIR = OPERATIONS_ANALYTICS_DIR / "benchmarks"

# Scripts a benchmarkear (buscar en la carpeta correcta)
CRITICAL_SCRIPTS = [
    ("01_Auditor_Hub.py", "Structure Auditor"),  # Buscar en 08_Scripts_Os/
    ("01_Auditor_Hub.py", "Validate Stack"),  # TODO: crear script real
    ("10_General_Hub.py", "Audit Sync Master"),  # Buscar en 08_Scripts_Os/
    ("01_Auditor_Hub.py", "System Health"),  # TODO: crear script real
]

# ============================================================
# BENCHMARKING
# ============================================================


def get_memory_usage() -> float:
    """Obtiene uso actual de memoria en MB."""
    process = psutil.Process()
    return process.memory_info().rss / 1024 / 1024


def benchmark_script(script_name: str, script_desc: str) -> Dict:
    """Ejecuta un script y mide su rendimiento."""
    script_path = SCRIPT_DIR / script_name

    if not script_path.exists():
        return {
            "script": script_name,
            "desc": script_desc,
            "status": "NOT_FOUND",
            "error": "Script no encontrado",
        }

    start_time = time.time()
    start_memory = get_memory_usage()

    try:
        result = subprocess.run(
            [sys.executable, str(script_path)],
            capture_output=True,
            text=True,
            timeout=60,  # 60 segundos max
        )

        end_time = time.time()
        end_memory = get_memory_usage()

        return {
            "script": script_name,
            "desc": script_desc,
            "status": "PASS" if result.returncode == 0 else "FAIL",
            "exit_code": result.returncode,
            "duration_ms": round((end_time - start_time) * 1000, 2),
            "memory_delta_mb": round(end_memory - start_memory, 2),
            "timestamp": datetime.now().isoformat(),
        }

    except subprocess.TimeoutExpired:
        return {
            "script": script_name,
            "desc": script_desc,
            "status": "TIMEOUT",
            "error": "Excedió 60 segundos",
        }
    except Exception as e:
        return {
            "script": script_name,
            "desc": script_desc,
            "status": "ERROR",
            "error": str(e),
        }


def run_benchmark() -> Dict:
    """Ejecuta todos los benchmarks."""
    print("=" * 60)
    print("   BENCHMARK BASELINE - PersonalOS")
    print("=" * 60)

    results = {"timestamp": datetime.now().isoformat(), "scripts": [], "summary": {}}

    total_duration = 0
    pass_count = 0
    fail_count = 0

    for script_name, script_desc in CRITICAL_SCRIPTS:
        print(f"\n>>> Benchmarking: {script_desc}...")

        result = benchmark_script(script_name, script_desc)
        results["scripts"].append(result)

        if result["status"] == "PASS":
            print(
                f"    [OK] {result['duration_ms']}ms | Mem: {result['memory_delta_mb']}MB"
            )
            pass_count += 1
            total_duration += result["duration_ms"]
        elif result["status"] == "FAIL":
            print(f"    [FAIL] Exit code: {result['exit_code']}")
            fail_count += 1
        else:
            print(f"    [{result['status']}] {result.get('error', '')}")
            fail_count += 1

    # Resumen
    results["summary"] = {
        "total_scripts": len(CRITICAL_SCRIPTS),
        "passed": pass_count,
        "failed": fail_count,
        "avg_duration_ms": round(total_duration / pass_count, 2)
        if pass_count > 0
        else 0,
        "pass_rate": f"{(pass_count / len(CRITICAL_SCRIPTS) * 100):.1f}%",
    }

    print("\n" + "=" * 60)
    print("   RESUMEN")
    print("=" * 60)
    print(f" Scripts probados: {results['summary']['total_scripts']}")
    print(f" Pasados: {results['summary']['passed']}")
    print(f" Fallidos: {results['summary']['failed']}")
    print(f" Promedio duración: {results['summary']['avg_duration_ms']}ms")
    print(f" Tasa de éxito: {results['summary']['pass_rate']}")
    print("=" * 60)

    return results


def save_benchmark(results: Dict) -> str:
    """Guarda el benchmark en archivo."""
    BENCHMARK_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"benchmark_{timestamp}.json"
    filepath = BENCHMARK_DIR / filename

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    return str(filepath)


def load_previous_benchmark() -> Dict:
    """Carga el último benchmark para comparar."""
    if not BENCHMARK_DIR.exists():
        return None

    benchmarks = sorted(BENCHMARK_DIR.glob("benchmark_*.json"), reverse=True)

    if not benchmarks:
        return None

    with open(benchmarks[0], "r") as f:
        return json.load(f)


def compare_benchmarks(current: Dict, previous: Dict) -> Dict:
    """Compara benchmarks actuales con anteriores."""
    if not previous:
        return {"message": "Sin benchmark anterior para comparar"}

    comparison = {"timestamp": datetime.now().isoformat(), "changes": []}

    for curr_script in current["scripts"]:
        script_name = curr_script["script"]

        for prev_script in previous["scripts"]:
            if prev_script["script"] == script_name:
                if curr_script["status"] == "PASS" and prev_script["status"] == "PASS":
                    delta = curr_script["duration_ms"] - prev_script["duration_ms"]
                    comparison["changes"].append(
                        {
                            "script": script_name,
                            "previous_ms": prev_script["duration_ms"],
                            "current_ms": curr_script["duration_ms"],
                            "delta_ms": delta,
                            "trend": "SLOWER" if delta > 0 else "FASTER",
                        }
                    )
                break

    return comparison


# ============================================================
# MAIN
# ============================================================


def main():
    """Ejecuta el benchmark completo."""
    # Cargar benchmark anterior
    previous = load_previous_benchmark()
    if previous:
        print(f">>> Último benchmark: {previous['timestamp']}")

    # Ejecutar benchmarks
    current = run_benchmark()

    # Guardar
    filepath = save_benchmark(current)
    print(f"\n>>> Benchmark guardado: {filepath}")

    # Comparar con anterior
    if previous:
        comparison = compare_benchmarks(current, previous)
        print("\n>>> COMPARACIÓN CON ANTERIOR:")
        for change in comparison.get("changes", []):
            emoji = "🐌" if change["trend"] == "SLOWER" else "⚡"
            print(
                f"  {emoji} {change['script']}: {change['previous_ms']}ms -> {change['current_ms']}ms ({int(change['delta_ms']):+d}ms)"
            )


if __name__ == "__main__":
    main()
