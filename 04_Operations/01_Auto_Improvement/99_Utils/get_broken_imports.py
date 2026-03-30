#!/usr/bin/env python3
"""Get detailed broken imports"""

import sys
import io
import ast
import traceback
from pathlib import Path

# Fix encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

sys.path.insert(
    0,
    str(Path(__file__).parent / "04_Operations" / "01_Auto_Improvement" / "01_Engine"),
)

from detector import Detector

d = Detector(Path(__file__).parent)
issues = d.scan_critical()

# Filter only BROKEN_IMPORT
broken_imports = [i for i in issues if i.get("type") == "BROKEN_IMPORT"]

print(f"\n=== BROKEN IMPORTS: {len(broken_imports)} ===\n")

for i, issue in enumerate(broken_imports):
    file_path = issue.get("file", "unknown")
    details = issue.get("details", "")

    print(f"{i + 1}. 📁 {file_path}")
    print(f"   Error: {str(details)[:100]}")
    print()
