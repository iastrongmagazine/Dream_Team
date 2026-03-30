#!/usr/bin/env python3
"""
Fix BROKEN_IMPORT issues - files with obsolete import patterns
Detects: "from Legacy_Backup", "import Legacy_Backup", "from 04_", "from 05_"
"""

import sys
import io
import re
import shutil
from pathlib import Path

# Fix encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).parent

# Patterns to detect broken imports
BROKEN_PATTERNS = [
    (r"from Legacy_Backup", "Legacy_Backup import"),
    (r"import Legacy_Backup", "Legacy_Backup import"),
    (r"from 04_", "04_ prefix import"),
    (r"from 05_", "05_ prefix import"),
    (r"from 06_", "06_ prefix import"),
    (r"from 07_", "07_ prefix import"),
    (r"from 08_", "08_ prefix import"),
]


def find_broken_import_files():
    """Find all files with broken import patterns"""
    scripts_dir = PROJECT_ROOT / "08_Scripts_Os"
    found = []

    for py_file in scripts_dir.glob("**/*.py"):
        if py_file.name.startswith("_"):
            continue

        try:
            content = py_file.read_text(errors="ignore")
        except:
            continue

        for pattern, desc in BROKEN_PATTERNS:
            if re.search(pattern, content):
                found.append(
                    {
                        "file": py_file,
                        "relative": str(py_file.relative_to(PROJECT_ROOT)),
                        "pattern": desc,
                        "content": content,
                    }
                )
                break

    return found


def fix_legacy_imports(file_path, content):
    """Fix Legacy_Backup imports"""
    original = content

    # Pattern: from Legacy_Backup.XXX import YYY
    # This usually refers to old scripts - we can try to find them

    # Count occurrences
    count = content.count("Legacy_Backup")

    # For now, comment them out with TODO
    content = re.sub(
        r"(from Legacy_Backup[^;]+\.)", r"# TODO: Fix legacy import - \1", content
    )
    content = re.sub(
        r"(import Legacy_Backup)", r"# TODO: Fix legacy import - \1", content
    )

    return (
        content,
        "Commented out Legacy_Backup imports" if content != original else "No changes",
    )


def fix_number_prefix_imports(content):
    """Fix imports starting with numbers (04_, 05_, etc)"""
    original = content

    # Replace: from 04_Something import X -> from Scripts_Os.04_Something import X
    # Or comment out if not resolvable

    # Simple approach: comment them
    content = re.sub(
        r"(from 0\d_\w+ import)", r"# TODO: Fix number prefix import - \1", content
    )

    return (
        content,
        "Commented out number prefix imports" if content != original else "No changes",
    )


def main():
    print("\n" + "=" * 60)
    print("🔧 FIXING BROKEN IMPORTS")
    print("=" * 60 + "\n")

    found = find_broken_import_files()
    print(f"Found {len(found)} files with broken imports\n")

    fixed = 0
    skipped = 0

    for i, item in enumerate(found):
        file_path = item["file"]
        content = item["content"]
        pattern = item["pattern"]

        print(f"\n[{i + 1}] {item['relative']}")
        print(f"    Pattern: {pattern}")

        # Create backup
        backup = file_path.with_suffix(".py.bak")
        shutil.copy2(file_path, backup)

        # Apply fixes
        new_content, action = fix_legacy_imports(file_path, content)
        new_content, action2 = fix_number_prefix_imports(new_content)

        if new_content != content:
            file_path.write_text(new_content, encoding="utf-8")
            print(f"    ✅ {action}")
            fixed += 1
        else:
            print(f"    ⏭️  No changes needed")
            skipped += 1

    print(f"\n{'=' * 60}")
    print(f"✅ Fixed: {fixed}")
    print(f"⏭️  Skipped: {skipped}")
    print(f"📁 Backups: *.py.bak")
    print("=" * 60)


if __name__ == "__main__":
    main()
