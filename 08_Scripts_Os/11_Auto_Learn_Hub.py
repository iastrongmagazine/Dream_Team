#!/usr/bin/env python3
"""
🔄 AUTO LEARN HUB - Motor Principal de Automejora Recursiva
================================================================
Orquesta todos los componentes de automejora del PersonalOS v6.1

Usage:
    python 11_Auto_Learn_Hub.py --scan        # Scan rápido (daily)
    python 11_Auto_Learn_Hub.py --weekly      # Scan profundo (weekly)
    python 11_Auto_Learn_Hub.py --monthly    # Auto-evolución (monthly)
    python 11_Auto_Learn_Hub.py --apply      # Aplicar fixes
"""

import argparse
import sys
from pathlib import Path

# === PROTOCOLO DE RUTA DINÁMICA (v6.1) ===
_current = Path(__file__).resolve()
_root = next((p for p in _current.parents if (p / "01_Core").exists()), None)
if _root:
    sys.path.insert(0, str(_root / "08_Scripts_Os"))
from config_paths import *

# Add engine to path (usando constants de config_paths)
sys.path.insert(0, str(AUTO_IMPROVEMENT_DIR / "01_Engine"))

try:
    from recursive_improvement_engine import RecursiveImprovementEngine
except ImportError:
    print("ERROR: No se pudo importar el motor de automejora")
    print("Asegurate de que existe: 04_Operations/01_Auto_Improvement/01_Engine/")
    sys.exit(1)


BANNER = """
╔══════════════════════════════════════════════════════════════════════╗
║           🔄 AUTO LEARN HUB - PersonalOS v6.1                      ║
║              Motor de Automejora Recursiva                          ║
╠══════════════════════════════════════════════════════════════════════╣
"""


def run_scan(dry_run=True):
    """Ejecutar scan rápido (daily)"""
    print(f"{BANNER}")
    print("║  Mode: DAILY SCAN                                                ║")
    print("╚══════════════════════════════════════════════════════════════════════╝\n")

    engine = RecursiveImprovementEngine(dry_run=dry_run)
    report = engine.run_quick_scan()

    print_report(report)
    return report


def run_weekly(dry_run=True):
    """Ejecutar scan profundo (weekly)"""
    print(f"{BANNER}")
    print("║  Mode: WEEKLY DEEP SCAN                                          ║")
    print("╚══════════════════════════════════════════════════════════════════════╝\n")

    engine = RecursiveImprovementEngine(dry_run=dry_run)
    report = engine.run_full_cycle()

    print_report(report)
    return report


def run_monthly():
    """Ejecutar auto-evolución (monthly)"""
    print(f"{BANNER}")
    print("║  Mode: MONTHLY EVOLUTION                                          ║")
    print("╚══════════════════════════════════════════════════════════════════════╝\n")

    engine = RecursiveImprovementEngine(dry_run=False)
    report = engine.run_full_cycle()

    print_report(report)
    return report


def run_learn_only():
    """Solo aprender del historial"""
    print(f"{BANNER}")
    print("║  Mode: LEARN FROM HISTORY                                        ║")
    print("╚══════════════════════════════════════════════════════════════════════╝\n")

    engine = RecursiveImprovementEngine(dry_run=True)
    result = engine.run_learn_only()

    print(f"\n📚 Aprendizajes cargados: {len(result.get('learnings', []))}")
    print(f"💡 Sugerencias: {len(result.get('suggestions', []))}")

    return result


def print_report(report):
    """Imprimir reporte formateado"""
    print("\n" + "=" * 60)
    print("📋 RESUMEN DEL CICLO")
    print("=" * 60)
    print(f"Timestamp: {report.get('timestamp', 'N/A')}")
    print(f"Mode: {report.get('mode', 'N/A')}")
    print(f"Issues detectados: {report.get('issues_detected', 0)}")
    print(f"Issues analizados: {report.get('issues_analyzed', 0)}")
    print(f"Fixes aplicados: {report.get('fixes_applied', 0)}")
    print(f"Aprendizajes: {report.get('learnings', 0)}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Auto Learn Hub - Recursive Self-Improvement Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python 11_Auto_Learn_Hub.py --scan           # Scan diario (dry-run)
  python 11_Auto_Learn_Hub.py --weekly         # Scan semanal (dry-run)
  python 11_Auto_Learn_Hub.py --monthly        # Evolución mensual
  python 11_Auto_Learn_Hub.py --scan --apply  # Scan con auto-fix
  python 11_Auto_Learn_Hub.py --learn         # Solo aprender del historial
        """,
    )

    parser.add_argument("--scan", action="store_true", help="Quick scan (daily mode)")
    parser.add_argument("--weekly", action="store_true", help="Deep scan (weekly mode)")
    parser.add_argument(
        "--monthly", action="store_true", help="Monthly evolution (apply fixes)"
    )
    parser.add_argument("--learn", action="store_true", help="Learn from history only")
    parser.add_argument(
        "--apply", action="store_true", help="Apply fixes (default is dry-run)"
    )

    args = parser.parse_args()

    # Default to scan if no args
    if not any([args.scan, args.weekly, args.monthly, args.learn]):
        args.scan = True

    dry_run = not args.apply

    try:
        if args.scan:
            run_scan(dry_run=dry_run)
        elif args.weekly:
            run_weekly(dry_run=dry_run)
        elif args.monthly:
            run_monthly()
        elif args.learn:
            run_learn_only()

        print("\n✅ Auto Learn Hub completado exitosamente")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
