#!/usr/bin/env python3
import os
from pathlib import Path


def generate_tree(root_dir: Path, level: int = 0) -> str:
    tree = ""
    # Filter ignored
    items = sorted(
        [
            item
            for item in root_dir.iterdir()
            if item.name
            not in ["__pycache__", ".git", ".ruff_cache", ".pytest_cache", "tree.txt"]
        ]
    )

    for item in items:
        prefix = "  " * level
        tree += f"{prefix}- {item.name}{'/' if item.is_dir() else ''}\n"
        if item.is_dir():
            tree += generate_tree(item, level + 1)
    return tree


root = Path(".")
# Update tree.txt files in subdirectories
for sub in [
    "00_Core",
    "01_Brain",
    "04_Operations",
    "03_Knowledge",
    "04_Operations",
    "05_System",
    "06_Archive",
    "07_Projects",
]:
    d = root / sub
    if d.exists():
        tree_content = generate_tree(d)
        (d / "tree.txt").write_text(tree_content)
        print(f"Updated {sub}/tree.txt")

# Update Architecture_Map.md
arch_map = "# PersonalOS System Map\n\n"
for sub in [
    "00_Core",
    "01_Brain",
    "04_Operations",
    "03_Knowledge",
    "04_Operations",
    "05_System",
    "06_Archive",
    "07_Projects",
]:
    arch_map += f"## {sub}\n\n```\n{generate_tree(root / sub)}\n```\n\n"

Path("Architecture_Map.md").write_text(arch_map)
Path("00_Core/Architecture_Map.md").write_text(arch_map)
print("Updated Architecture_Map.md")
