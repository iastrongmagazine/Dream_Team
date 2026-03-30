#!/usr/bin/env python3
"""
Weekly Metrics Generator

Generates a weekly progress report for the Sunday Ritual.
"""

import sys
from pathlib import Path
from datetime import datetime, timedelta

# Fix Windows encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def find_project_root():
    """Find the project root."""
    current = Path(__file__).resolve()
    for parent in [current] + list(current.parents):
        if (parent / "00_Core").exists() or (parent / "GOALS.md").exists():
            return parent
    return Path.cwd()


def main():
    print("=" * 50)
    print("📊 WEEKLY METRICS REPORT")
    print(f"📅 Week of {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 50)

    project_root = find_project_root()
    task_dir = project_root / "04_Operations" / "01_Active_Tasks"

    if not task_dir.exists():
        print(f"❌ Tasks directory not found: {task_dir}")
        return

    tasks = list(task_dir.glob("*.md"))

    # Count by status
    done = sum(
        1
        for t in tasks
        if "status: d" in t.read_text(encoding="utf-8", errors="ignore").lower()
    )
    in_progress = sum(
        1
        for t in tasks
        if "status: s" in t.read_text(encoding="utf-8", errors="ignore").lower()
    )
    blocked = sum(
        1
        for t in tasks
        if "status: b" in t.read_text(encoding="utf-8", errors="ignore").lower()
    )
    not_started = len(tasks) - done - in_progress - blocked

    total = len(tasks)
    completion_rate = (done / total * 100) if total > 0 else 0

    print(f"\n📈 COMPLETION:")
    print(f"  ✅ Completed:  {done}")
    print(f"  🔄 In Progress: {in_progress}")
    print(f"  ⛔ Blocked:    {blocked}")
    print(f"  ⏳ Not Started: {not_started}")
    print(f"  📊 Rate:       {completion_rate:.1f}%")

    print(f"\n📋 TASKS: {total} total")
    print(f"\n💡 TIPS:")
    if completion_rate < 50:
        print("  - Focus on completing existing tasks before adding new ones")
    elif completion_rate > 80:
        print("  - Great week! Consider taking on more P0 tasks")

    if blocked > 2:
        print("  - High blocked count - prioritize unblocking")

    print("\n" + "=" * 50)
    print("💾 Use this data to plan next week's P0 tasks")
    print("=" * 50)


if __name__ == "__main__":
    main()
