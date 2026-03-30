#!/usr/bin/env python3
"""Fix broken imports in ACTIVE scripts (non-Legacy_Backup)"""

import sys
import io
import re
import shutil
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).parent

ACTIVE_FILES = [
    "08_Scripts_Os\\11_Anthropic_Harness\\04_Playwright_QA.py",
    "08_Scripts_Os\\Ritual_Fixed\\12_Update_Links.py",
    "08_Scripts_Os\\Ritual_Fixed\\50_System_Health_Monitor.py",
    "08_Scripts_Os\\Tool_Fixed\\39_Repair_Corruption.py",
    "08_Scripts_Os\\Tool_Fixed\\60_Fast_Vision.py",
    "08_Scripts_Os\\Tool_Fixed\\61_MCP_Health_Check.py",
    "08_Scripts_Os\\Validator_Fixed\\33_Parallel_Audit_Pro.py",
    "08_Scripts_Os\\Validator_Fixed\\40_Validate_Rules.py",
    "08_Scripts_Os\\Workflow_Fixed\\73_Avengers_Workflow_v3.py",
]


def fix_04_engine_refs(content, file_path):
    """Replace 04_Operations references with correct path"""
    original = content

    # Replace "04_Operations" in string paths (not comments)
    # Pattern: "04_Operations/..." -> "../../08_Scripts_Os/..." or similar

    # Common replacements
    replacements = [
        # Path references
        (r'"04_Operations"', r'"../.."'),  # From 08_Scripts_Os subfolder
        (r"'04_Operations'", r"'../..'"),
        # Comments about 04_Operations - leave as-is or update
    ]

    for old, new in replacements:
        content = re.sub(old, new, content)

    return content


print("\n" + "=" * 60)
print("🔧 FIXING ACTIVE SCRIPTS")
print("=" * 60 + "\n")

fixed = 0
for rel_path in ACTIVE_FILES:
    full_path = PROJECT_ROOT / rel_path

    if not full_path.exists():
        print(f"❌ NOT FOUND: {rel_path}")
        continue

    # Read
    content = full_path.read_text(encoding="utf-8", errors="ignore")
    original = content

    # Fix 04_Operations references
    content = fix_04_engine_refs(content, rel_path)

    if content != original:
        # Backup
        backup = full_path.with_suffix(".py.bak")
        shutil.copy2(full_path, backup)

        # Write fixed
        full_path.write_text(content, encoding="utf-8")
        print(f"✅ Fixed: {rel_path}")
        fixed += 1
    else:
        print(f"⏭️  Skipped: {rel_path} (no changes)")

print(f"\n{'=' * 60}")
print(f"✅ Fixed: {fixed} files")
print(f"📁 Backups: *.py.bak")
print("=" * 60)
