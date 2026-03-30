#!/usr/bin/env python3
"""Detailed detector check"""

import sys
import io
import re
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).parent

# Patterns from detector
BROKEN_PATTERNS = [
    "from Legacy_Backup",
    "import Legacy_Backup",
    "04_Operations",
    "from 04_",
    "from 05_",
]

scripts_dir = PROJECT_ROOT / "08_Scripts_Os"
issues = []

for py_file in scripts_dir.glob("**/*.py"):
    if py_file.name.startswith("_"):
        continue
    try:
        content = py_file.read_text(errors="ignore")
    except:
        continue

    for pattern in BROKEN_PATTERNS:
        if pattern in content:
            issues.append(
                {"file": str(py_file.relative_to(PROJECT_ROOT)), "pattern": pattern}
            )

print(f"\n=== BROKEN IMPORTS: {len(issues)} ===\n")

# Group by pattern
by_pattern = {}
for i in issues:
    p = i["pattern"]
    if p not in by_pattern:
        by_pattern[p] = []
    by_pattern[p].append(i["file"])

for p, files in sorted(by_pattern.items(), key=lambda x: -len(x[1])):
    print(f"\n## {p}: {len(files)} files")
    for f in files[:5]:
        print(f"  - {f}")
    if len(files) > 5:
        print(f"  ... and {len(files) - 5} more")
