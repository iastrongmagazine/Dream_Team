#!/usr/bin/env python3
"""
Backlog Triage Script

Reads BACKLOG.md and suggests how to process each item.
Works with PersonalOS structure.

Usage:
    python backlog-triage.py                 # Analyze backlog
    python backlog-triage.py --create-tasks  # Create task files
    python backlog-triage.py --dedup         # Check for duplicates
"""

import argparse
import re
import sys
from pathlib import Path
from datetime import datetime

# Fix Windows encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def get_backlog_path() -> Path:
    """Find BACKLOG.md"""
    candidates = [
        "BACKLOG.md",
        "../BACKLOG.md",
        "../../BACKLOG.md",
        "00_Core/BACKLOG.md",
        "../00_Core/BACKLOG.md",
    ]
    for c in candidates:
        if Path(c).exists():
            return Path(c)
    raise FileNotFoundError("BACKLOG.md not found")


def get_tasks_dir() -> Path:
    """Find Tasks directory"""
    candidates = [
        "Tasks",
        "04_Operations/01_Active_Tasks",
        "../04_Operations/01_Active_Tasks",
    ]
    for c in candidates:
        if Path(c).exists():
            return Path(c)
    raise FileNotFoundError("Tasks directory not found")


def parse_backlog_items(content: str) -> list[dict]:
    """Parse backlog items from markdown"""
    items = []
    lines = content.split("\n")

    current_item = None
    for line in lines:
        line = line.strip()

        # Skip empty lines and headers
        if not line or line.startswith("#"):
            continue

        # List item
        if line.startswith("- "):
            text = line[2:].strip()
            if text:
                # Detect type
                item_type = "general"
                priority_hint = None

                lower = text.lower()
                if any(w in lower for w in ["bug", "error", "fix", "broken"]):
                    item_type = "bug"
                elif any(w in lower for w in ["idea", "maybe", "someday"]):
                    item_type = "idea"
                elif any(w in lower for w in ["meeting", "1:1", "call"]):
                    item_type = "meeting"

                current_item = {
                    "text": text,
                    "type": item_type,
                    "priority_hint": priority_hint,
                }
                items.append(current_item)

    return items


def suggest_priority(item: dict) -> str:
    """Suggest priority based on content"""
    text = item["text"].lower()
    item_type = item["type"]

    # Bugs are usually P0
    if item_type == "bug":
        return "P0"

    # Meetings with dates
    if "tomorrow" in text or "today" in text:
        return "P1"

    # Keywords
    if any(w in text for w in ["urgent", "asap", "critical"]):
        return "P0"
    if any(w in text for w in ["important", "priority"]):
        return "P1"

    return "P2"


def suggest_category(item: dict) -> str:
    """Suggest category based on content"""
    text = item["text"].lower()

    if any(w in text for w in ["bug", "fix", "error", "code"]):
        return "technical"
    if any(w in text for w in ["email", "message", "follow", "call", "meet"]):
        return "outreach"
    if any(w in text for w in ["write", "blog", "doc", "content"]):
        return "writing"
    if any(w in text for w in ["research", "analyze", "explore"]):
        return "research"
    if any(w in text for w in ["plan", "roadmap", "strategy"]):
        return "strategy"

    return "other"


def check_dedup(item_text: str, tasks_dir: Path) -> list[str]:
    """Check for duplicate tasks"""
    duplicates = []
    text_lower = item_text.lower()

    # Keywords to check
    keywords = [w for w in text_lower.split() if len(w) > 4]

    for task_file in tasks_dir.glob("*.md"):
        task_name = task_file.stem.lower()

        # Check if any keyword matches existing task
        for kw in keywords:
            if kw in task_name:
                duplicates.append(task_file.stem)
                break

    return duplicates


def format_suggestion(item: dict, index: int, duplicates: list[str] = None) -> str:
    """Format a single backlog item suggestion"""
    priority = suggest_priority(item)
    category = suggest_category(item)

    emoji = {"P0": "🔴", "P1": "🟡", "P2": "🟢", "P3": "⚪"}.get(priority, "⚪")

    output = f"{index}. {emoji} [{priority}] [{category}] {item['text']}"

    if duplicates:
        output += f"\n   ⚠️ Possible duplicate: {duplicates}"

    return output


def main():
    parser = argparse.ArgumentParser(description="Backlog Triage Helper")
    parser.add_argument("--create-tasks", action="store_true", help="Create task files")
    parser.add_argument("--dedup", action="store_true", help="Check for duplicates")
    parser.add_argument("--limit", type=int, default=20, help="Max items to process")

    args = parser.parse_args()

    try:
        backlog_path = get_backlog_path()
        tasks_dir = get_tasks_dir()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Read backlog
    content = backlog_path.read_text(encoding="utf-8")
    items = parse_backlog_items(content)

    if not items:
        print("No items found in BACKLOG.md")
        sys.exit(0)

    # Process items
    items = items[: args.limit]

    print("=" * 60)
    print("📋 BACKLOG TRIAGE REPORT")
    print("=" * 60)
    print(f"\nFound {len(items)} items to process:\n")

    # Count priorities
    priorities = {"P0": 0, "P1": 0, "P2": 0, "P3": 0}
    categories = {}

    for i, item in enumerate(items, 1):
        priority = suggest_priority(item)
        category = suggest_category(item)

        priorities[priority] = priorities.get(priority, 0) + 1
        categories[category] = categories.get(category, 0) + 1

        # Check duplicates if requested
        duplicates = []
        if args.dedup:
            duplicates = check_dedup(item["text"], tasks_dir)

        print(format_suggestion(item, i, duplicates))

    # Summary
    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    print(f"\nBy Priority:")
    for p, count in priorities.items():
        emoji = {"P0": "🔴", "P1": "🟡", "P2": "🟢", "P3": "⚪"}.get(p, "⚪")
        if count > 0:
            print(f"  {emoji} {p}: {count}")

    print(f"\nBy Category:")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  • {cat}: {count}")

    print("\n" + "=" * 60)
    print("💡 Next Steps:")
    print("  1. Review each item above")
    print("  2. Confirm/adjust priorities")
    print("  3. Create tasks with --create-tasks")
    print("  4. Clear processed items from BACKLOG.md")
    print("=" * 60)


if __name__ == "__main__":
    main()
