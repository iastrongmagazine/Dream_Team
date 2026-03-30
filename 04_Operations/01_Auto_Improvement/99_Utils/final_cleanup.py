#!/usr/bin/env python3
"""
Fix ALL remaining outdated paths - FINAL CLEANUP
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(
    "C:/Users/sebas/Downloads/01 Revisar/09 Versiones/00 Respaldo PC Sebas/01 Github/personal-os/Think_Different"
)

# More aggressive replacements for remaining items
REPLACEMENTS = [
    # These need careful handling - replace with correct context
    ("01_Core/", "01_Core/"),
    ("01_Core\\", "01_Core\\"),
    ("04_Operations/", "04_Operations/"),
    ("04_Operations\\", "04_Operations\\"),
]


def get_all_files():
    extensions = {".md", ".py", ".yaml", ".yml", ".json", ".txt", ".sh"}
    files = []
    for ext in extensions:
        files.extend(PROJECT_ROOT.glob(f"**/*{ext}"))
    return [f for f in files if ".git" not in str(f)]


def should_skip(filepath):
    # Only skip truly legacy backup folders
    skip = ["Legacy_Backup", "_Fixed", "05_Archive", "Maerks/06_Reports"]
    path_str = str(filepath)
    return any(s in path_str for s in skip)


def fix_file(filepath):
    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
    except:
        return 0

    original = content

    # More careful replacements
    for old, new in REPLACEMENTS:
        content = content.replace(old, new)

    if content != original:
        filepath.write_text(content, encoding="utf-8")
        return original.count(old)
    return 0


def main():
    print("=" * 60)
    print("FINAL CLEANUP - ALL REMAINING PATHS")
    print("=" * 60)

    files = get_all_files()
    total = 0

    for i, f in enumerate(files):
        if should_skip(f):
            continue
        changes = fix_file(f)
        if changes:
            print(f"[{i}] {f.relative_to(PROJECT_ROOT)}: {changes}")
            total += changes

    print(f"\nTotal: {total} replacements")


if __name__ == "__main__":
    main()
