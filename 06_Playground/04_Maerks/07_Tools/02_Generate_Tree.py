# -*- coding: utf-8 -*-
"""
generate_tree.py - Genera tree.txt para cada carpeta del proyecto
"""

# Fix Windows console encoding
import sys

if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import os
from pathlib import Path


def generate_tree(path, prefix="", max_depth=3, current_depth=0):
    """Genera estructura de árbol recursivamente"""
    if current_depth >= max_depth:
        return []

    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        return []

    # Filtrar archivos/carpetas a ignorar
    exclude = {
        ".git",
        "__pycache__",
        ".pytest_cache",
        "node_modules",
        "tree.txt",
        ".mcp.json",
        ".claude",
    }
    items = [item for item in items if item not in exclude and not item.startswith(".")]

    lines = []
    for i, item in enumerate(items):
        full_path = os.path.join(path, item)
        is_last = i == len(items) - 1
        connector = "+-- " if is_last else "|-- "
        lines.append(f"{prefix}{connector}{item}")

        if os.path.isdir(full_path):
            extension = "    " if is_last else "|   "
            sub_lines = generate_tree(
                full_path, prefix + extension, max_depth, current_depth + 1
            )
            lines.extend(sub_lines)

    return lines


def main():
    """Genera tree.txt para las carpetas principales"""
    from pathlib import Path

    script_dir = Path(__file__).resolve().parent
    project_root = script_dir.parent.parent

    dirs = [
        "00_Core",
        "01_Brain",
        "04_Operations",
        "03_Knowledge",
        "04_Operations",
        "05_System",
        "06_Archive",
        "07_Projects",
    ]

    print("Generando trees...")

    for d in dirs:
        dir_path = project_root / d
        tree_file = dir_path / "tree.txt"

        if dir_path.exists():
            lines = [f"{d}/"]
            lines.extend(generate_tree(str(dir_path), max_depth=2))

            content = "\n".join(lines)
            tree_file.write_text(content, encoding="utf-8")
            print(f"  [OK] {d}/tree.txt")
        else:
            print(f"  [SKIP] {d}/ no existe")

    print("Done!")


if __name__ == "__main__":
    main()
