#!/usr/bin/env python3
"""
Archive Completed Tasks

Moves completed tasks to the archive folder.
"""

import sys
import shutil
from pathlib import Path
from datetime import datetime

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
    print("📦 ARCHIVE COMPLETED TASKS")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d')}")
    print("=" * 50)

    project_root = find_project_root()
    task_dir = project_root / "04_Operations" / "01_Active_Tasks"
    archive_dir = project_root / "06_Archive" / "01_Tasks_Archive"

    if not task_dir.exists():
        print(f"❌ Tasks directory not found: {task_dir}")
        return

    # Create archive dir if not exists
    archive_dir.mkdir(parents=True, exist_ok=True)

    # Find completed tasks
    completed = []
    for task_file in task_dir.glob("*.md"):
        try:
            content = task_file.read_text(encoding="utf-8", errors="ignore")
            if "status: d" in content.lower() or "status: done" in content.lower():
                completed.append(task_file)
        except Exception:
            continue

    print(f"\n📋 Found {len(completed)} completed task(s)")

    if not completed:
        print("✅ No tasks to archive")
        return

    # Move to archive
    archived = 0
    for task_file in completed:
        dest = archive_dir / task_file.name
        # Handle duplicates
        if dest.exists():
            dest = (
                archive_dir
                / f"{task_file.stem}_archived{datetime.now().strftime('%Y%m%d')}{task_file.suffix}"
            )

        shutil.move(str(task_file), str(dest))
        print(f"  ✓ Archived: {task_file.name}")
        archived += 1

    print(f"\n✅ Archived {archived} task(s) to {archive_dir}")
    print("=" * 50)


if __name__ == "__main__":
    main()
