#!/usr/bin/env python3
"""
15_Weekly_Review.py - PersonalOS Weekly Review v3.0
====================================================
Basado en: examples/workflows/weekly-review.md

A 15-30 minute session to reflect on progress and plan ahead.

Usage:
    python 15_Weekly_Review.py           # Full review
    python 15_Weekly_Review.py --quick   # Quick 5-min version
    python 15_Weekly_Review.py --step N  # Run specific step only
"""

import sys
import os
import io
import glob
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Optional

# Fix Windows encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# Path resolution
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "08_Scripts_Os" / "Legacy_Backup"))
from config_paths import ROOT_DIR, OPERATIONS_DIR, KNOWLEDGE_DIR


# ============================================================================
# CONFIGURATION
# ============================================================================

TASKS_DIR = PROJECT_ROOT / "03_Tasks"
CONTEXT_MEMORY_DIR = PROJECT_ROOT / "04_Operations" / "00_Context_Memory"
GOALS_FILE = PROJECT_ROOT / "00_Winter_is_Coming" / "GOALS.md"
PROCESS_NOTES_DIR = PROJECT_ROOT / "04_Operations" / "03_Process_Notes"


# ============================================================================
# FUNCTIONS
# ============================================================================


def get_week_range() -> tuple:
    """Get the date range for this week."""
    today = datetime.now()
    start = today - timedelta(days=today.weekday())
    end = start + timedelta(days=6)
    return start, end


def get_tasks_by_status() -> Dict[str, List[Dict]]:
    """Get tasks grouped by status."""
    tasks = {"done": [], "active": [], "blocked": [], "all": []}

    if not TASKS_DIR.exists():
        return tasks

    for f in TASKS_DIR.glob("*.md"):
        try:
            content = f.read_text(encoding="utf-8")

            title = f.stem
            if "_" in title and title[1].isdigit():
                title = "_".join(title.split("_")[1:])

            task_info = {
                "name": title.replace("-", " ")[:60],
                "file": f.name,
                "priority": "P0"
                if "P0" in f.stem
                else ("P1" if "P1" in f.stem else "P2"),
                "modified": datetime.fromtimestamp(f.stat().st_mtime),
            }

            tasks["all"].append(task_info)

            if "status: d" in content.lower():
                tasks["done"].append(task_info)
            elif "status: b" in content.lower():
                tasks["blocked"].append(task_info)
            elif "status: n" in content.lower() or "status: s" in content.lower():
                tasks["active"].append(task_info)
        except Exception:
            continue

    return tasks


def get_completed_this_week() -> List[Dict]:
    """Get tasks completed this week."""
    tasks = get_tasks_by_status()
    start, end = get_week_range()

    completed = []
    for task in tasks["done"]:
        if start <= task["modified"] <= end:
            completed.append(task)

    return completed


def get_blocked_tasks() -> List[Dict]:
    """Get blocked tasks."""
    tasks = get_tasks_by_status()
    return tasks["blocked"]


def get_active_tasks() -> List[Dict]:
    """Get active (not started or in progress) tasks."""
    tasks = get_tasks_by_status()
    return tasks["active"]


def read_goals() -> List[str]:
    """Read goals from GOALS.md."""
    if not GOALS_FILE.exists():
        return []

    content = GOALS_FILE.read_text(encoding="utf-8")
    goals = []

    in_goals = False
    for line in content.split("\n"):
        if "##" in line and "goal" in line.lower():
            in_goals = True
            continue
        if in_goals and line.strip().startswith("-"):
            goals.append(line.strip())
        elif in_goals and line.strip().startswith("##") and len(goals) > 0:
            break

    return goals


def print_banner():
    """Print weekly review banner."""
    start, end = get_week_range()
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║          📊 W E E K L Y   R E V I E W                              ║
║              Think Different PersonalOS v3.0                          ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""")
    print(f"📅 Semana: {start.strftime('%d/%m')} - {end.strftime('%d/%m/%Y')}")
    print(f"📆 Fecha: {datetime.now().strftime('%A, %d de %B de %Y')}\n")


def step1_review_completed():
    """Step 1: Review completed work."""
    print("=" * 70)
    print("✅ STEP 1: ¿Qué completamos esta semana?")
    print("=" * 70)

    completed = get_completed_this_week()

    if completed:
        print(f"\n📋 Se completaron {len(completed)} tareas:\n")

        # Group by priority
        p0 = [t for t in completed if t["priority"] == "P0"]
        p1 = [t for t in completed if t["priority"] == "P1"]
        p2 = [t for t in completed if t["priority"] == "P2"]

        if p0:
            print("🔴 P0 (Urgente):")
            for t in p0:
                print(f"   ✓ {t['name']}")

        if p1:
            print("\n🟡 P1 (Importante):")
            for t in p1:
                print(f"   ✓ {t['name']}")

        if p2:
            print("\n🟢 P2 (Normal):")
            for t in p2:
                print(f"   ✓ {t['name']}")
    else:
        print("\n📭 No hay tareas completadas esta semana")

    print()


def step2_check_goals():
    """Step 2: Check goal progress."""
    print("=" * 70)
    print("🎯 STEP 2: ¿Cómo vamos con los objetivos?")
    print("=" * 70)

    goals = read_goals()

    if goals:
        print(f"\n📌 Objetivos definidos ({len(goals)}):\n")
        for goal in goals:
            print(f"   • {goal[:65]}")
    else:
        print("\n📭 No hay objetivos definidos en GOALS.md")

    print()


def step3_blockers():
    """Step 3: Identify blockers."""
    print("=" * 70)
    print("⚠️ STEP 3: ¿Qué está bloqueado o estancado?")
    print("=" * 70)

    blocked = get_blocked_tasks()
    active = get_active_tasks()

    if blocked:
        print(f"\n🚫 Tareas bloqueadas ({len(blocked)}):\n")
        for t in blocked:
            print(f"   • {t['name']} [{t['priority']}]")
    else:
        print("\n✅ No hay tareas bloqueadas")

    # Find stalled (started but no progress)
    week_ago = datetime.now() - timedelta(days=7)
    stalled = [t for t in active if t["modified"] < week_ago]

    if stalled:
        print(f"\n⏸️ Tareas estancadas ({len(stalled)} - sin progreso en 7 días):\n")
        for t in stalled[:5]:
            print(f"   • {t['name']}")

    print()


def step4_plan_next():
    """Step 4: Plan next week."""
    print("=" * 70)
    print("📅 STEP 4: Plan para la próxima semana")
    print("=" * 70)

    active = get_active_tasks()

    # Sort by priority
    p0 = [t for t in active if t["priority"] == "P0"]
    p1 = [t for t in active if t["priority"] == "P1"]
    p2 = [t for t in active if t["priority"] == "P2"]

    print(f"\n🎯 PRIORIDADES SUGERIDAS PARA LA PRÓXIMA SEMANA:\n")

    print("MUST DO (P0/P1):")
    for t in (p0 + p1)[:5]:
        emoji = "🔴" if t["priority"] == "P0" else "🟡"
        print(f"   {emoji} {t['name']}")

    if len(p0 + p1) > 5:
        print(f"\n   ... y {len(p0 + p1) - 5} más")

    print("\nSHOULD DO (P2):")
    for t in p2[:3]:
        print(f"   🟢 {t['name']}")

    print()


def run_full_review():
    """Run complete weekly review."""
    print_banner()
    step1_review_completed()
    step2_check_goals()
    step3_blockers()
    step4_plan_next()

    print("=" * 70)
    print("💬 Resumen generado. ¿Querés ajustar algo?")
    print("=" * 70 + "\n")


def run_quick_review():
    """Run quick 5-minute version."""
    print_banner()

    completed = get_completed_this_week()
    blocked = get_blocked_tasks()
    active = get_active_tasks()

    print("=" * 70)
    print("⚡ QUICK WEEKLY REVIEW")
    print("=" * 70)

    print(f"\n✅ Completadas: {len(completed)}")
    print(f"🔄 Activas: {len(active)}")
    print(f"⚠️ Bloqueadas: {len(blocked)}")

    print("\n🎯 Próximas prioridades:")
    for t in (get_active_tasks())[:3]:
        print(f"   • {t['name']}")

    print()


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Weekly Review v3.0")
    parser.add_argument("--quick", action="store_true", help="Quick 5-min version")
    parser.add_argument(
        "--step", type=int, choices=[1, 2, 3, 4], help="Run specific step only"
    )

    args = parser.parse_args()

    if args.step:
        if args.step == 1:
            step1_review_completed()
        elif args.step == 2:
            step2_check_goals()
        elif args.step == 3:
            step3_blockers()
        elif args.step == 4:
            step4_plan_next()
    elif args.quick:
        run_quick_review()
    else:
        run_full_review()
