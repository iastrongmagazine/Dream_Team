#!/usr/bin/env python3
"""Get issues from detector"""

import sys
import io
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

print(f"\n=== TOTAL ISSUES: {len(issues)} ===\n")

# Group by type
by_type = {}
for issue in issues:
    t = issue.get("type", "unknown")
    if t not in by_type:
        by_type[t] = []
    by_type[t].append(issue)

for t, items in sorted(by_type.items(), key=lambda x: -len(x[1])):
    print(f"\n## {t.upper()} ({len(items)} issues)")
    for i, issue in enumerate(items[:5]):
        print(
            f"  {i + 1}. [{issue.get('severity', '?')}] {issue.get('file', '?')[:70]}"
        )
        if "details" in issue and issue["details"]:
            print(f"      -> {str(issue['details'])[:60]}")
    if len(items) > 5:
        print(f"  ... and {len(items) - 5} more")
