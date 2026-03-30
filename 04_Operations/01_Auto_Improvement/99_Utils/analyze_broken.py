#!/usr/bin/env python3
"""Categorize broken imports by location"""

import sys
import io
from pathlib import Path

if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

PROJECT_ROOT = Path(__file__).parent

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
            rel = str(py_file.relative_to(PROJECT_ROOT))
            issues.append(
                {"file": rel, "pattern": pattern, "is_legacy": "Legacy_Backup" in rel}
            )

# Categorize
legacy = [i for i in issues if i["is_legacy"]]
non_legacy = [i for i in issues if not i["is_legacy"]]

print(f"\n=== ANALYSIS ===")
print(f"Total broken imports: {len(issues)}")
print(f"  - In Legacy_Backup: {len(legacy)} (will NOT fix)")
print(f"  - In ACTIVE scripts: {len(non_legacy)} (need review)")
print()

# Show non-legacy
print("=== NON-LEGACY FILES (need review) ===")
seen = set()
for i in non_legacy:
    f = i["file"]
    if f not in seen:
        seen.add(f)
        print(f"  - {f}")
