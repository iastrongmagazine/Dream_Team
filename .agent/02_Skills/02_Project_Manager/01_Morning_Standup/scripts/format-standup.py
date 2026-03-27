#!/usr/bin/env python3
"""
Morning Standup Formatter

Reads Tasks/ folder and formats priorities for daily standup.
Works with PersonalOS task structure (YAML frontmatter).

Usage:
    python format-standup.py                    # Show today's priorities
    python format-standup.py --limit 3           # Limit to top 3
    python format-standup.py --include-p2         # Include P2 tasks
"""

import argparse
import os
import re
import sys

# Fix Windows encoding for emojis
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional


def get_tasks_dir() -> Path:
    """Get Tasks directory - works in PersonalOS structure"""
    candidates = [
        "Tasks",
        "../Tasks",
        "../../02_Operations/01_Active_Tasks",
        "02_Operations/01_Active_Tasks",
    ]

    for candidate in candidates:
        if Path(candidate).exists():
            return Path(candidate)

    raise FileNotFoundError("Tasks directory not found")


def parse_task_file(filepath: Path) -> Optional[dict]:
    """Parse a task file - supports YAML frontmatter or inline format"""
    try:
        content = filepath.read_text(encoding="utf-8")
        task = {"title": filepath.stem, "file": str(filepath)}

        # Try YAML frontmatter first (--- or - --)
        if content.startswith("---") or content.startswith("- --"):
            parts = content.replace("- --", "---", 1).split("---", 2)
            if len(parts) >= 2:
                yaml_section = parts[1]
                for line in yaml_section.split("\n"):
                    if ":" in line:
                        key, value = line.split(":", 1)
                        task[key.strip()] = value.strip()
                # DONE - use YAML title, don't parse body
                return task

        # Fallback: inline format (e.g., "# 🔴 P0 — Task Name")
        # Priority in first heading
        priority_match = re.search(
            r"^[#🔴🟡🟢⚪]+\s*\[?P([0-3])\]?\s*[—\-]\s*(.+)$", content, re.MULTILINE
        )
        if priority_match:
            task["priority"] = f"P{priority_match.group(1)}"
            task["title"] = priority_match.group(2).strip()

        # Category in filename or default
        # Priority from filename as fallback (e.g., "07_P0_Task_Name.md")
        if "priority" not in task:
            filename_priority = re.search(r"_P([0-3])_", filepath.stem)
            if filename_priority:
                task["priority"] = f"P{filename_priority.group(1)}"

        task["category"] = "other"

        # Status: look for "status: n/s/b/d/y" or "* *Status:** b"
        status_match = re.search(
            r"(?:status|Status)[:\s*]+([nsbdy])", content, re.IGNORECASE
        )
        if status_match:
            task["status"] = status_match.group(1)

        return task

    except Exception as e:
        print(f"Error parsing {filepath}: {e}", file=sys.stderr)
        return None


def filter_p0_p1(task: dict) -> bool:
    """Check if task is P0 or P1"""
    priority = task.get("priority", "P3")
    return priority in ["P0", "P1"]


def filter_today_or_overdue(task: dict) -> bool:
    """Check if task is due today or overdue"""
    due_date = task.get("due_date")
    if not due_date:
        return True  # No due date = anytime

    try:
        due = datetime.strptime(due_date, "%Y-%m-%d")
        today = datetime.now()

        # Due today or overdue
        return due <= today + timedelta(days=1)
    except ValueError:
        return True


def get_priority_order(priority: str) -> int:
    """Return sort order for priorities"""
    order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    return order.get(priority, 99)


def format_task_line(task: dict, index: int) -> str:
    """Format a single task for standup output"""
    priority = task.get("priority", "P1")
    title = task.get("title", "Untitled")
    est_time = task.get("estimated_time", "?")
    category = task.get("category", "other")

    emoji = {"P0": "🔴", "P1": "🟡", "P2": "🟢", "P3": "⚪"}.get(priority, "⚪")

    # ELITE FLAG for blocked tasks
    blocked_flag = " [BLOCKED]" if task.get("status") == "b" else ""

    due = task.get("due_date", "")
    if due:
        try:
            due_date = datetime.strptime(due, "%Y-%m-%d")
            days_until = (due_date - datetime.now()).days
            if days_until < 0:
                due_str = f" (OVERDUE {abs(days_until)} days)"
            elif days_until == 0:
                due_str = " (due today)"
            elif days_until == 1:
                due_str = " (due tomorrow)"
            else:
                due_str = f" (due {due_date.strftime('%b %d')})"
        except ValueError:
            due_str = f" (due: {due})"
    else:
        due_str = ""

    return f"{index}. {emoji} [{priority}]{blocked_flag} {title} (est: {est_time}min) — {category}{due_str}"


def main():
    parser = argparse.ArgumentParser(description="Format morning standup output")
    parser.add_argument("--limit", type=int, default=5, help="Max tasks to show")
    parser.add_argument("--include-p2", action="store_true", help="Include P2 tasks")
    parser.add_argument("--category", type=str, help="Filter by category")
    parser.add_argument(
        "--show-blockers", action="store_true", help="Show blocked tasks"
    )

    args = parser.parse_args()

    try:
        tasks_dir = get_tasks_dir()
    except FileNotFoundError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    # Parse all tasks
    tasks = []
    for filepath in tasks_dir.glob("*.md"):
        task = parse_task_file(filepath)
        if task:
            tasks.append(task)

    # Filter by priority
    if args.include_p2:
        priority_filter = lambda t: t.get("priority", "P3") in ["P0", "P1", "P2"]
    else:
        priority_filter = filter_p0_p1

    # Revert: Include blocked tasks, but flag them in format
    tasks = [t for t in tasks if priority_filter(t)]

    # Filter by due date (P0/P1 should show if due today/overdue)
    tasks = [t for t in tasks if filter_today_or_overdue(t)]

    # Filter by category if specified
    if args.category:
        tasks = [t for t in tasks if t.get("category") == args.category]

    # Sort by priority
    tasks.sort(key=lambda t: get_priority_order(t.get("priority", "P3")))

    # Limit results
    tasks = tasks[: args.limit] if args.limit > 0 else tasks

    # Output
    today = datetime.now().strftime("%A, %B %d")

    print("=" * 60)
    print(f"🌅 MORNING STANDUP - {today}")
    print("=" * 60)
    print()

    if not tasks:
        print("No P0/P1 tasks due. You're free to focus on P2 or explore!")
        print()
        print("Tip: Run 'python check-blockers.py' to see blocked tasks")
    else:
        print("📋 TODAY'S PRIORITIES")
        print("-" * 40)
        for i, task in enumerate(tasks, 1):
            print(format_task_line(task, i))
        print()

    # Show blockers if requested
    if args.show_blockers:
        print("🚧 BLOCKED TASKS")
        print("-" * 40)
        blocked = [t for t in tasks if t.get("status") == "b"]
        if blocked:
            for task in blocked:
                print(f"  • {task['title']}")
                blocker = task.get("blocker", "Unknown blocker")
                print(f"    Blocked by: {blocker}")
        else:
            print("  No blocked tasks! 🎉")
        print()

    print("=" * 60)
    print("💡 Remember: Focus on P0 first, then P1")
    print("=" * 60)


if __name__ == "__main__":
    main()
