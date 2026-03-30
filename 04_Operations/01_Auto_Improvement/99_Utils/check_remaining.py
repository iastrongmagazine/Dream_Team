#!/usr/bin/env python3
"""Check what patterns remain in non-legacy files"""

import sys
import io
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).parent

NON_LEGACY = [
    "08_Scripts_Os\\11_Anthropic_Harness\\04_Playwright_QA.py",
    "08_Scripts_Os\\Ritual_Fixed\\50_System_Health_Monitor.py",
    "08_Scripts_Os\\Tool_Fixed\\60_Fast_Vision.py",
    "08_Scripts_Os\\Tool_Fixed\\61_MCP_Health_Check.py",
    "08_Scripts_Os\\Validator_Fixed\\33_Parallel_Audit_Pro.py",
    "08_Scripts_Os\\Validator_Fixed\\40_Validate_Rules.py",
]

patterns = ["04_Operations", "Legacy_Backup", "from 04_", "from 05_"]

for rel_path in NON_LEGACY:
    full_path = PROJECT_ROOT / rel_path
    if not full_path.exists():
        continue

    content = full_path.read_text(encoding="utf-8", errors="ignore")

    found = []
    for p in patterns:
        if p in content:
            # Count occurrences
            count = content.count(p)
            found.append(f"{p}({count})")

    if found:
        print(f"\n{rel_path}")
        print(f"   Patterns: {', '.join(found)}")
