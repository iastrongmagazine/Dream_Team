#!/usr/bin/env python3
"""
Fix sys.path for subdirectory scripts so they can find config_paths
"""

import sys
import io
import re
import shutil
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).parent
SCRIPTS_OS = PROJECT_ROOT / "08_Scripts_Os"

# Files with broken imports
TARGET_FILES = [
    SCRIPTS_OS / "Validator_Fixed" / "40_Validate_Rules.py",
    SCRIPTS_OS / "Validator_Fixed" / "33_Parallel_Audit_Pro.py",
    SCRIPTS_OS / "Ritual_Fixed" / "50_System_Health_Monitor.py",
    SCRIPTS_OS / "Tool_Fixed" / "60_Fast_Vision.py",
    SCRIPTS_OS / "Tool_Fixed" / "61_MCP_Health_Check.py",
]


def fix_syspath(content, file_path):
    """Add proper sys.path.insert for config_paths"""
    original = content

    # Check if already has proper path to SCRIPTS_OS
    if "08_Scripts_Os" in content or "SCRIPTS_OS" in content:
        return content, "already has SCRIPTS_OS reference"

    # Find where PROJECT_ROOT is defined
    # Pattern: PROJECT_ROOT = Path(...).parent.parent (etc)

    # Add sys.path.insert for SCRIPTS_OS after the existing sys.path.insert calls
    # Find the last sys.path.insert and add after it

    lines = content.split("\n")
    new_lines = []
    added = False

    for line in lines:
        new_lines.append(line)

        # After PROJECT_ROOT definition and sys.path.insert, add SCRIPTS_OS path
        if "sys.path.insert" in line and "PROJECT_ROOT" in line and not added:
            # Add the new line after this
            indent = len(line) - len(line.lstrip())
            space = " " * indent
            new_lines.append(
                f"{space}sys.path.insert(0, str(PROJECT_ROOT / '08_Scripts_Os'))"
            )
            added = True

    content = "\n".join(new_lines)

    if added:
        return content, "added SCRIPTS_OS path"
    else:
        return original, "no changes needed"


print("\n" + "=" * 60)
print("🔧 FIXING SYS.PATH FOR CONFIG_PATHS")
print("=" * 60 + "\n")

fixed = 0
for file_path in TARGET_FILES:
    if not file_path.exists():
        print(f"❌ NOT FOUND: {file_path.name}")
        continue

    content = file_path.read_text(encoding="utf-8", errors="ignore")
    original = content

    content, action = fix_syspath(content, file_path)

    if content != original:
        # Backup
        backup = file_path.with_suffix(".py.bak2")
        shutil.copy2(file_path, backup)

        # Write fixed
        file_path.write_text(content, encoding="utf-8")
        print(f"✅ {file_path.name}: {action}")
        fixed += 1
    else:
        print(f"⏭️  {file_path.name}: {action}")

print(f"\n{'=' * 60}")
print(f"✅ Fixed: {fixed} files")
print(f"📁 Backups: *.py.bak2")
print("=" * 60)
