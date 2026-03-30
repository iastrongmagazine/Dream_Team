#!/usr/bin/env python3
"""
Fix sys.path for subdirectory scripts - correct parent path
"""

import sys
import io
import shutil
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).parent
SCRIPTS_OS = PROJECT_ROOT / "08_Scripts_Os"

# Files to fix
TARGETS = [
    ("Validator_Fixed/40_Validate_Rules.py", 30),
    ("Validator_Fixed/33_Parallel_Audit_Pro.py", None),
    ("Ritual_Fixed/50_System_Health_Monitor.py", None),
    ("Tool_Fixed/60_Fast_Vision.py", None),
    ("Tool_Fixed/61_MCP_Health_Check.py", None),
]

print("\n" + "=" * 60)
print("🔧 FIXING CONFIG_PATHS IMPORTS")
print("=" * 60 + "\n")

for rel_path, line_num in TARGETS:
    file_path = SCRIPTS_OS / rel_path

    if not file_path.exists():
        print(f"❌ NOT FOUND: {rel_path}")
        continue

    content = file_path.read_text(encoding="utf-8", errors="ignore")
    original = content

    # Fix: sys.path.insert(0, str(Path(__file__).parent))
    # To: sys.path.insert(0, str(Path(__file__).parent.parent))
    # Because config_paths.py is in 08_Scripts_Os/, not in Validator_Fixed/

    content = content.replace(
        "sys.path.insert(0, str(Path(__file__).parent))",
        "sys.path.insert(0, str(Path(__file__).parent.parent))",
    )

    if content != original:
        backup = file_path.with_suffix(".py.bak3")
        shutil.copy2(file_path, backup)
        file_path.write_text(content, encoding="utf-8")
        print(f"✅ Fixed: {rel_path}")
    else:
        print(f"⏭️  Skipped: {rel_path} (no change)")

print("\n" + "=" * 60)
