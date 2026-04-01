#!/usr/bin/env python3
"""
14_Morning_Standup.py - PersonalOS Morning Standup v3.0
======================================================
Basado en: examples/workflows/morning-standup.md

A quick check-in to set your focus for the day.

Usage:
    python 14_Morning_Standup.py           # Run standup
    python 14_Morning_Standup.py --tasks   # Show tasks only
    python 14_Morning_Standup.py --goals   # Show goals only
"""

import sys
import os
import io
import glob
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Optional

# Fix Windows encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# Path resolution
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent

# Add Legacy_Backup for config_paths
sys.path.insert(0, str(PROJECT_ROOT / "08_Scripts_Os" / "Legacy_Backup"))
from config_paths import ROOT_DIR, OPERATIONS_DIR, KNOWLEDGE_DIR


# ============================================================================
# CONFIGURATION
# ============================================================================

CONTEXT_MEMORY_DIR = PROJECT_ROOT / "04_Operations" / "00_Context_Memory"
PROCESS_NOTES_DIR = PROJECT_ROOT / "04_Operations" / "03_Process_Notes"
TASKS_DIR = PROJECT_ROOT / "03_Tasks"
GOALS_FILE = PROJECT_ROOT / "00_Winter_is_Coming" / "GOALS.md"
BACKLOG_FILE = PROJECT_ROOT / "00_Winter_is_Coming" / "BACKLOG.md"


# ============================================================================
# FUNCTIONS
# ============================================================================


def get_latest_file(directory: Path, pattern: str = "*.md") -> Optional[Path]:
    """Get most recent file matching pattern."""
    if not directory.exists():
        return None
    files = list(directory.glob(pattern))
    if not files:
        return None
    return max(files, key=lambda p: p.stat().st_mtime)


def read_file_lines(path: Path, lines: int = 10) -> List[str]:
    """Read first N lines of a file."""
    if not path or not path.exists():
        return []
    try:
        return [
            line.strip()
            for line in path.read_text(encoding="utf-8").split("\n")[:lines]
        ]
    except Exception:
        return []


def get_tasks(priority: str = None) -> List[Dict]:
    """Get active tasks, optionally filtered by priority."""
    tasks = []

    if not TASKS_DIR.exists():
        return tasks

    for f in TASKS_DIR.glob("*.md"):
        try:
            content = f.read_text(encoding="utf-8")

            # Check status (n = not started)
            if (
                "status: n" not in content.lower()
                and "status: s" not in content.lower()
            ):
                continue

            # Filter by priority if specified
            if priority:
                if f"P{priority}" not in f.stem.upper():
                    continue

            # Extract title
            title = f.stem
            if "_" in title:
                # Remove priority prefix
                parts = title.split("_", 1)
                if parts[0].startswith("P"):
                    title = parts[1]

            tasks.append(
                {
                    "name": title.replace("-", " ")[:60],
                    "file": f.name,
                    "priority": "P0"
                    if "P0" in f.stem
                    else ("P1" if "P1" in f.stem else "P2"),
                }
            )
        except Exception:
            continue

    return tasks


def get_blocked_tasks() -> List[Dict]:
    """Get blocked tasks."""
    blocked = []

    if not TASKS_DIR.exists():
        return blocked

    for f in TASKS_DIR.glob("*.md"):
        try:
            content = f.read_text(encoding="utf-8")
            if "status: b" in content.lower():
                title = f.stem.split("_", 1)[-1] if "_" in f.stem else f.stem
                blocked.append(
                    {
                        "name": title.replace("-", " "),
                        "file": f.name,
                    }
                )
        except Exception:
            continue

    return blocked


def read_goals() -> List[str]:
    """Read goals from GOALS.md."""
    if not GOALS_FILE.exists():
        return []

    content = GOALS_FILE.read_text(encoding="utf-8")
    goals = []

    in_goals_section = False
    for line in content.split("\n"):
        if "##" in line and ("goal" in line.lower() or "objetivo" in line.lower()):
            in_goals_section = True
            continue

        if in_goals_section and line.strip().startswith("-"):
            goals.append(line.strip())
        elif in_goals_section and line.strip().startswith("##"):
            break

    return goals[:5]  # Top 5 goals


def print_banner():
    """Print standup banner."""
    print("""
╔══════════════════════════════════════════════════════════════════════╗
║                                                                      ║
║          ☀️  M O R N I N G   S T A N D U P                         ║
║              Think Different PersonalOS v3.0                          ║
║                                                                      ║
╚══════════════════════════════════════════════════════════════════════╝
""")
    print(f"📅 {datetime.now().strftime('%A, %d de %B de %Y')}\n")


def run_standup(show_tasks: bool = True, show_goals: bool = True):
    """Run the morning standup."""
    print_banner()

    print("=" * 70)
    print("📋 RESUMEN DEL SISTEMA")
    print("=" * 70)

    # Latest Context
    latest_ctx = get_latest_file(CONTEXT_MEMORY_DIR, "CTX_*.md")
    if latest_ctx:
        print(f"🧠 Último CTX: {latest_ctx.name}")
    else:
        print("🧠 CTX: No hay contexto previo")

    # Latest Note
    latest_note = get_latest_file(PROCESS_NOTES_DIR, "*.md")
    if latest_note:
        print(f"📝 Última nota: {latest_note.name}")
    else:
        print("📝 Notas: No hay notas previas")

    # Tasks count
    p0_tasks = get_tasks("0")
    p1_tasks = get_tasks("1")
    p2_tasks = get_tasks("2")
    blocked = get_blocked_tasks()

    print(f"\n📊 TAREAS ACTIVAS:")
    print(f"   🔴 P0 (Urgente): {len(p0_tasks)}")
    print(f"   🟡 P1 (Importante): {len(p1_tasks)}")
    print(f"   🟢 P2 (Normal): {len(p2_tasks)}")

    if blocked:
        print(f"\n⚠️  BLOQUEADAS: {len(blocked)}")
        for t in blocked[:3]:
            print(f"   - {t['name'][:50]}")

    print()

    # Top Priorities
    if show_tasks:
        print("=" * 70)
        print("🎯 TOP 3 PRIORIDADES PARA HOY")
        print("=" * 70)

        all_tasks = p0_tasks + p1_tasks

        if all_tasks:
            for i, task in enumerate(all_tasks[:3], 1):
                emoji = "🔴" if task["priority"] == "P0" else "🟡"
                print(f"   {i}. {emoji} [{task['priority']}] {task['name']}")
        else:
            print("   ✅ No hay tareas pendientes!")

    # Goals
    if show_goals:
        print("\n" + "=" * 70)
        print("🎯 OBJECTIVOS (GOALS)")
        print("=" * 70)

        goals = read_goals()
        if goals:
            for goal in goals[:3]:
                print(f"   • {goal[:65]}")
        else:
            print("   📌 Revisar GOALS.md")

    # Backlog
    if BACKLOG_FILE.exists():
        backlog_lines = BACKLOG_FILE.read_text(encoding="utf-8").split("\n")
        backlog_items = [l for l in backlog_lines if l.strip().startswith("- ")]
        print(f"\n📬 BACKLOG: {len(backlog_items)} items pendientes")

    print("\n" + "=" * 70)
    print("💬 ¿EN QUÉ TRABAJAREMOS HOY?")
    print("=" * 70 + "\n")


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Morning Standup v3.0")
    parser.add_argument("--tasks", action="store_true", help="Show only tasks")
    parser.add_argument("--goals", action="store_true", help="Show only goals")

    args = parser.parse_args()

    show_tasks = not args.goals
    show_goals = not args.tasks

    run_standup(show_tasks=show_tasks, show_goals=show_goals)
