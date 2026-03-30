#!/usr/bin/env python3
"""
Fix all 5 outdated paths in PersonalOS v6.1
"""

import re
from pathlib import Path

PROJECT_ROOT = Path(
    "C:/Users/sebas/Downloads/01 Revisar/09 Versiones/00 Respaldo PC Sebas/01 Github/personal-os/Think_Different"
)

# All replacements to make
REPLACEMENTS = [
    # (pattern, replacement, description)
    ("04_Operations", "04_Operations", "Old engine folder"),
    ("01_Core/03_Skills", "01_Core/03_Skills", "Claude skills old path"),
    ("04_Operations", "04_Operations", "Old operations folder"),
    ("03_Tasks/", "03_Tasks/", "Old todos directory"),
    (".agent/01_Agents", ".agent/01_Agents", "Claude agents old path"),
]


def get_all_files():
    """Get all text files to check"""
    extensions = {".md", ".py", ".yaml", ".yml", ".json", ".txt", ".sh"}
    files = []
    for ext in extensions:
        files.extend(PROJECT_ROOT.glob(f"**/*{ext}"))
    return [f for f in files if ".git" not in str(f) and "node_modules" not in str(f)]


def should_skip(filepath):
    """Skip certain directories"""
    skip_patterns = [
        "Legacy_Backup",
        "_Fixed",
        "Archive",
        "05_Archive",
        "node_modules",
        ".git",
    ]
    path_str = str(filepath)
    return any(p in path_str for p in skip_patterns)


def fix_file(filepath, verbose=True):
    """Fix paths in a single file"""
    try:
        content = filepath.read_text(encoding="utf-8", errors="ignore")
    except:
        return 0

    original = content
    changes = 0

    for old, new, desc in REPLACEMENTS:
        if old in content:
            count = content.count(old)
            content = content.replace(old, new)
            changes += count
            if verbose:
                print(f"  {desc}: {count} replacements")

    if content != original:
        filepath.write_text(content, encoding="utf-8")
        return changes
    return 0


def main():
    print("=" * 60)
    print("FIXING ALL 5 OUTDATED PATHS")
    print("=" * 60)

    files = get_all_files()
    print(f"\nScanning {len(files)} files...")

    total_changes = 0
    files_changed = 0

    for i, filepath in enumerate(files):
        if should_skip(filepath):
            continue

        changes = fix_file(filepath, verbose=False)
        if changes > 0:
            total_changes += changes
            files_changed += 1
            print(
                f"[{i + 1}/{len(files)}] {filepath.relative_to(PROJECT_ROOT)}: {changes} changes"
            )

    print(f"\n{'=' * 60}")
    print(f"SUMMARY:")
    print(f"  Files changed: {files_changed}")
    print(f"  Total replacements: {total_changes}")
    print("=" * 60)


if __name__ == "__main__":
    main()
