#!/usr/bin/env python3
"""
Analyze Weekly Progress

Compares Tasks/ with GOALS.md to provide objective progress data.
Runs as part of Weekly Review skill.
Supports multiple frontmatter formats:
- Standard YAML: ---key: value---
- PersonalOS: - --key: value-- (inline)
- Inline metadata: *Prioridad:** P0, *Status:** b
"""

import sys
import os
import re
from pathlib import Path
from datetime import datetime

# Fix Windows encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def find_project_root():
    """Find the project root by looking for marker files."""
    current = Path(__file__).resolve()

    for parent in [current] + list(current.parents):
        if (
            (parent / "00_Core").exists()
            or (parent / "GOALS.md").exists()
            or (parent / ".git").exists()
        ):
            return parent

    return Path.cwd()


def parse_task_file(filepath):
    """Parse a task markdown file and extract metadata."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return None

    yaml_part = None
    body = None

    # Format 1: Standard YAML ---key: value---
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            yaml_part = parts[1]
            body = parts[2]

    # Format 2: PersonalOS inline - --key: value--
    elif content.startswith("- --"):
        parts = content.split("- --", 2)
        if len(parts) >= 3:
            yaml_part = parts[1].strip()
            body = parts[2]

    # Format 3: No frontmatter - parse from body (*Prioridad:**, *Status:**)
    # This is the format: # Title\n\n* *Prioridad:** P0\n* *Status:** b
    else:
        # Extract title from first # heading
        title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filepath.stem

        # Extract priority from * *Prioridad:** or *Prioridad:**
        priority = "P3"  # default
        priority_match = re.search(
            r"\*?\*?Prioridad\*?\*?:\s*(\w+)", content, re.IGNORECASE
        )
        if priority_match:
            p_raw = priority_match.group(1).upper()
            if p_raw.startswith("P"):
                priority = p_raw[:2]
            elif "ALTA" in p_raw or "URGENTE" in p_raw:
                priority = "P0"
            elif "MEDIA" in p_raw:
                priority = "P1"
            elif "BAJA" in p_raw:
                priority = "P2"

        # Extract status from * *Status:** or *Status:**
        status = "n"  # default
        status_match = re.search(r"\*?\*?Status\*?\*?:\s*(\w+)", content, re.IGNORECASE)
        if status_match:
            s_raw = status_match.group(1).lower()
            status_map = {
                "active": "s",
                "in_progress": "s",
                "started": "s",
                "s": "s",
                "done": "d",
                "completed": "d",
                "finished": "d",
                "d": "d",
                "blocked": "b",
                "b": "b",
                "not_started": "n",
                "pending": "n",
                "n": "n",
            }
            status = status_map.get(s_raw, "n")

        return {
            "title": title,
            "status": status,
            "priority": priority,
            "filepath": str(filepath),
        }

    # Parse YAML formats
    if yaml_part and body:
        # Parse status
        status = "n"
        status_match = re.search(r"status:\s*(\w+)", yaml_part)
        if status_match:
            status_raw = status_match.group(1).lower()
            status_map = {
                "active": "s",
                "in_progress": "s",
                "started": "s",
                "done": "d",
                "completed": "d",
                "finished": "d",
                "blocked": "b",
                "not_started": "n",
                "pending": "n",
                "n": "n",
                "s": "s",
                "d": "d",
                "b": "b",
            }
            status = status_map.get(status_raw, "n")

        # Parse priority
        priority = "P3"
        priority_match = re.search(r"priority:\s*(\w+)", yaml_part)
        if priority_match:
            priority_raw = priority_match.group(1).upper()
            if priority_raw.startswith("P"):
                priority = priority_raw[:2]
            else:
                priority_map = {"HIGH": "P0", "MEDIUM": "P1", "LOW": "P2"}
                priority = priority_map.get(priority_raw, "P3")

        # Parse title
        title_match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filepath.stem

        return {
            "title": title,
            "status": status,
            "priority": priority,
            "filepath": str(filepath),
        }

    return None


def calculate_metrics(tasks):
    """Calculate completion metrics."""
    total = len(tasks)
    if total == 0:
        return {
            "total": 0,
            "completed": 0,
            "in_progress": 0,
            "not_started": 0,
            "blocked": 0,
            "completion_rate": 0,
        }

    completed = sum(1 for t in tasks if t["status"] == "d")
    in_progress = sum(1 for t in tasks if t["status"] == "s")
    blocked = sum(1 for t in tasks if t["status"] == "b")
    not_started = sum(1 for t in tasks if t["status"] == "n")

    return {
        "total": total,
        "completed": completed,
        "in_progress": in_progress,
        "blocked": blocked,
        "not_started": not_started,
        "completion_rate": (completed / total * 100) if total > 0 else 0,
    }


def main():
    print("=" * 50)
    print("🚀 WEEKLY PROGRESS ANALYSIS (ELITE v4.2)")
    print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 50)

    project_root = find_project_root()
    print(f"\n📁 Project Root: {project_root}")

    # Find tasks directory
    task_dir = project_root / "04_Operations" / "01_Active_Tasks"
    if not task_dir.exists():
        print(f"❌ Error: Directory {task_dir} not found.")
        alt_paths = [
            project_root / "Tasks",
            project_root / "04_Operations" / "Tasks",
        ]
        for alt in alt_paths:
            if alt.exists():
                task_dir = alt
                print(f"📁 Using alternative path: {task_dir}")
                break
        else:
            return

    tasks = []
    print(f"\n📂 Scanning: {task_dir}")
    for md_file in sorted(task_dir.glob("*.md")):
        task = parse_task_file(md_file)
        if task:
            tasks.append(task)
        else:
            print(f"  ⚠️ Could not parse: {md_file.name}")

    print(f"\n📊 Found {len(tasks)} tasks to analyze.\n")

    metrics = calculate_metrics(tasks)

    print("📈 METRICS:")
    print(f"  ✅ Completed:     {metrics['completed']}")
    print(f"  🔄 In Progress:  {metrics['in_progress']}")
    print(f"  ⛔ Blocked:      {metrics['blocked']}")
    print(f"  ⏳ Not Started:  {metrics['not_started']}")
    print(f"  📊 Completion:    {metrics['completion_rate']:.1f}%")

    # Group by priority
    priorities = {"P0": [], "P1": [], "P2": [], "P3": []}
    for task in tasks:
        p = task["priority"]
        if p in priorities:
            priorities[p].append(task)

    print("\n🎯 BY PRIORITY:")
    for p in ["P0", "P1", "P2", "P3"]:
        completed = sum(1 for t in priorities[p] if t["status"] == "d")
        total = len(priorities[p])
        if total > 0:
            print(
                f"  {p}: {completed}/{total} completed ({completed / total * 100:.0f}%)"
            )

    # Show completed
    print("\n✅ COMPLETED TASKS:")
    completed_tasks = [t for t in tasks if t["status"] == "d"]
    for t in completed_tasks[:5]:
        print(f"  - {t['title'][:60]}")
    if not completed_tasks:
        print("  (No completed tasks found)")

    # Show blocked
    blocked_tasks = [t for t in tasks if t["status"] == "b"]
    if blocked_tasks:
        print("\n⛔ BLOCKED:")
        for t in blocked_tasks:
            print(f"  - {t['title'][:60]}")

    # Show in progress
    in_progress_tasks = [t for t in tasks if t["status"] == "s"]
    if in_progress_tasks:
        print("\n🔄 IN PROGRESS:")
        for t in in_progress_tasks[:5]:
            print(f"  - {t['title'][:60]}")

    print("\n" + "=" * 50)
    print("💡 Ready for weekly review reflection!")
    print("=" * 50)


if __name__ == "__main__":
    main()
