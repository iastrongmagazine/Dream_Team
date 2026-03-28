#!/usr/bin/env python3
"""
Generate accurate directory tree for .agent/02_Skills/ with skill counts.
"""

from pathlib import Path

SKILLS_DIR = Path(".agent/02_Skills")


def count_skills(dir_path, depth=0):
    """Count SKILL.md files in directory (recursively to depth 2)."""
    count = 0
    has_subdirs = False

    for item in dir_path.iterdir():
        if item.is_dir() and item.name != "__pycache__":
            if (item / "SKILL.md").exists() or (item / "skill.md").exists():
                count += 1
            if depth < 2:
                sub_count, _ = count_skills(item, depth + 1)
                if sub_count > 0:
                    count += sub_count
                    has_subdirs = True

    return count, has_subdirs


def generate_tree(dir_path, prefix="", max_depth=3, current_depth=0):
    """Generate tree string with skill counts."""
    lines = []
    items = sorted(
        [d for d in dir_path.iterdir() if d.is_dir() and d.name != "__pycache__"]
    )

    for i, item in enumerate(items):
        is_last = i == len(items) - 1
        connector = "└── " if is_last else "├── "

        # Count skills in this directory
        skill_count, has_subdirs = count_skills(item, 0)

        # Format name with count
        if skill_count > 0:
            name = f"{item.name}/ ({skill_count} skills)"
        else:
            name = f"{item.name}/"

        lines.append(f"{prefix}{connector}{name}")

        # Recurse if depth allows
        if current_depth < max_depth:
            extension = "    " if is_last else "│   "
            sub_lines = generate_tree(
                item, prefix + extension, max_depth, current_depth + 1
            )
            lines.extend(sub_lines)

    return lines


def main():
    print("=== DIRECTORY TREE: .agent/02_Skills/ ===\n")
    print(".agent/02_Skills/")

    tree_lines = generate_tree(SKILLS_DIR, max_depth=3)
    for line in tree_lines:
        print(line)

    # Count totals
    print("\n=== SKILL COUNTS BY CATEGORY ===\n")

    total = 0
    for category_dir in sorted(SKILLS_DIR.iterdir()):
        if category_dir.is_dir() and category_dir.name not in [
            "__pycache__",
            "README.md",
        ]:
            count, _ = count_skills(category_dir, 0)
            if count > 0:
                print(f"{category_dir.name}: {count} skills")
                total += count

    print(f"\n[TOTAL] {total} skills across all categories")


if __name__ == "__main__":
    main()
