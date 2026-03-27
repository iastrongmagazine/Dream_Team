#!/usr/bin/env python3
"""
Execute Plan Helper

Tracks execution progress and generates checkpoint reports.
"""

import sys
from pathlib import Path
from datetime import datetime


def parse_plan(plan_path):
    """Parse a plan file and extract tasks."""
    content = Path(plan_path).read_text(encoding="utf-8", errors="ignore")
    tasks = []

    lines = content.split("\n")
    for i, line in enumerate(lines):
        if line.strip().startswith("### Task"):
            tasks.append(
                {
                    "line": i,
                    "title": line.strip().replace("### ", ""),
                    "status": "pending",
                }
            )

    return tasks


def generate_checkpoint(batch_num, tasks, completed):
    """Generate a checkpoint report."""
    report = f"""## Checkpoint: Batch {batch_num} Complete

### Completed Tasks

"""
    for task in completed:
        report += f"- ✅ {task['title']}\n"

    report += f"""
### Completed: {len(completed)}/{len(tasks)}

### Ready for feedback.

Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}
"""
    return report


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python execute-plan.py <plan-path>")
        print("       python execute-plan.py <plan-path> --checkpoint <batch-num>")
        sys.exit(1)

    plan_path = sys.argv[1]
    tasks = parse_plan(plan_path)

    print(f"Found {len(tasks)} tasks in plan")
    for i, task in enumerate(tasks, 1):
        print(f"  {i}. {task['title']}")

    if "--checkpoint" in sys.argv:
        batch_idx = sys.argv.index("--checkpoint") + 1
        batch_num = int(sys.argv[batch_idx]) if batch_idx < len(sys.argv) else 1
        print(generate_checkpoint(batch_num, tasks, []))
