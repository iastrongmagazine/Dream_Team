#!/usr/bin/env python3
"""
Blocker Checker for Morning Standup

Scans Tasks/ folder for blocked tasks (status: b) and suggests unblocking actions.
Works with PersonalOS task structure.

Usage:
    python check-blockers.py              # Show all blocked tasks
    python check-blockers.py --urgent    # Show only P0/P1 blocked
    python check-blockers.py --action     # Suggest unblocking actions
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
    """Get Tasks directory"""
    candidates = [
        "Tasks",
        "../Tasks",
        "../../04_Operations/01_Active_Tasks",
        "04_Operations/01_Active_Tasks",
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
                body = parts[2] if len(parts) > 2 else ""

                for line in yaml_section.split("\n"):
                    if ":" in line:
                        key, value = line.split(":", 1)
                        task[key.strip()] = value.strip()

                # Extract blocker from body if present
                if "blocked" in body.lower() or "bloqueado" in body.lower():
                    blocker_match = re.search(
                        r"(?:blocked?|bloqueado)[:\s*]+([^\n\*]+)", body, re.IGNORECASE
                    )
                    if blocker_match:
                        task["blocker_reason"] = blocker_match.group(1).strip()

                # DONE - use YAML title, don't parse body
                return task

        # Fallback: inline format (e.g., "# 🔴 P0 — Task Name")
        priority_match = re.search(
            r"^[#🔴🟡🟢⚪]+\s*\[?P([0-3])\]?\s*[—\-]\s*(.+)$", content, re.MULTILINE
        )
        if priority_match:
            task["priority"] = f"P{priority_match.group(1)}"
            task["title"] = priority_match.group(2).strip()

        # Priority from filename as fallback
        if "priority" not in task:
            filename_priority = re.search(r"_P([0-3])_", filepath.stem)
            if filename_priority:
                task["priority"] = f"P{filename_priority.group(1)}"

        task["category"] = "other"

        # Status
        status_match = re.search(
            r"(?:status|Status)[:\s*]+([nsbdy])", content, re.IGNORECASE
        )
        if status_match:
            task["status"] = status_match.group(1)

        # Blocker info for inline format
        if "blocked" in content.lower() or "bloqueado" in content.lower():
            # Match: "* *Status:** b (bloqueado hasta...)"
            blocker_match = re.search(
                r"(?:Status)[:\s*]+\w+\s*\(?([^\)]+)\)?", content, re.IGNORECASE
            )
            if blocker_match:
                task["blocker_reason"] = blocker_match.group(1).strip()
            else:
                # Fallback: just say blocked
                task["blocker_reason"] = "Blocked (reason in file)"

        return task

    except Exception:
        return None


def suggest_actions(task: dict) -> list[str]:
    """Suggest actions to unblock a task"""
    suggestions = []
    title = task.get("title", "").lower()

    # Generic suggestions based on common blockers
    if "waiting" in title or "esperando" in title:
        suggestions.append("Send a follow-up message")
        suggestions.append("Schedule a reminder to check back")

    if "api" in title or "spec" in title:
        suggestions.append("Reach out directly to get estimate")
        suggestions.append("Start with a simpler version")

    if "review" in title or "feedback" in title:
        suggestions.append("Send a gentle ping")
        suggestions.append("Offer to help unblock them first")

    if "waiting on" in title:
        blocker = task.get("blocker_reason", "")
        if "james" in blocker.lower():
            suggestions.append("James might need context - add more details")
        if "sarah" in blocker.lower():
            suggestions.append("Check if there's someone else who can help")

    # Default suggestions
    if not suggestions:
        suggestions.append("Send a quick follow-up message")
        suggestions.append("Check if there's a workaround")
        suggestions.append("Escalate if blocked > 3 days")

    return suggestions


def format_blocker(task: dict, index: int, verbose: bool = False) -> str:
    """Format a blocked task"""
    priority = task.get("priority", "P2")
    title = task.get("title", "Untitled")
    due = task.get("due_date", "")

    emoji = {"P0": "🔴", "P1": "🟡", "P2": "🟢", "P3": "⚪"}.get(priority, "⚪")

    output = f"{index}. {emoji} [{priority}] {title}"

    if due:
        output += f" (due: {due})"

    if verbose:
        blocker = task.get("blocker_reason", "Unknown")
        output += f"\n   Blocked by: {blocker}"

        suggestions = suggest_actions(task)
        output += "\n   Suggestions:"
        for s in suggestions[:3]:
            output += f"\n     → {s}"

    return output


def main():
    parser = argparse.ArgumentParser(description="Check blocked tasks")
    parser.add_argument("--urgent", action="store_true", help="Show only P0/P1 blocked")
    parser.add_argument(
        "--action", action="store_true", help="Suggest unblocking actions"
    )
    parser.add_argument(
        "--days", type=int, default=3, help="Flag as urgent if blocked > N days"
    )

    args = parser.parse_args()

    try:
        tasks_dir = get_tasks_dir()
    except FileNotFoundError:
        print("Tasks directory not found")
        sys.exit(1)

    # Parse all tasks
    all_tasks = []
    for filepath in tasks_dir.glob("*.md"):
        task = parse_task_file(filepath)
        if task:
            all_tasks.append(task)

    # Filter blocked tasks
    blocked = [t for t in all_tasks if t.get("status") == "b"]

    # Filter by priority if urgent
    if args.urgent:
        blocked = [t for t in blocked if t.get("priority") in ["P0", "P1"]]

    # Sort by priority
    priority_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    blocked.sort(key=lambda t: priority_order.get(t.get("priority", "P2"), 99))

    # Output
    print("=" * 60)
    print("🚧 BLOCKED TASKS REPORT")
    print("=" * 60)
    print()

    if not blocked:
        print("✅ No blocked tasks! Great job keeping things moving.")
    else:
        print(f"Found {len(blocked)} blocked task(s):\n")

        for i, task in enumerate(blocked, 1):
            print(format_blocker(task, i, verbose=args.action))
            print()

    # Summary
    p0_blocked = len([t for t in blocked if t.get("priority") == "P0"])
    p1_blocked = len([t for t in blocked if t.get("priority") == "P1"])

    if p0_blocked > 0:
        print(f"⚠️  {p0_blocked} P0 task(s) blocked - HIGH PRIORITY to unblock!")

    print()
    print("=" * 60)
    if blocked:
        print("💡 Tip: Don't let blockers sit > 3 days. Follow up or find workaround.")
    else:
        print("🎉 All clear! Focus on your priorities.")
    print("=" * 60)


if __name__ == "__main__":
    main()
