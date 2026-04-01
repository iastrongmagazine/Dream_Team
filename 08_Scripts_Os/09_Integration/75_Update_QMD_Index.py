import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
#!/usr/bin/env python3
"""
QMD Index Update Script
Re-indexes QMD collections for PersonalOS.
Usage: python 56_Update_QMD_Index.py
"""

import subprocess
import sys
import os
from pathlib import Path

# Fix Windows encoding
os.system("chcp 65001 >nul 2>&1")

SCRIPT_DIR = Path(__file__).parent
QMD_BIN = Path(
    "C:/Users/sebas/AppData/Roaming/npm/node_modules/@tobilu/qmd/dist/cli/qmd.js"
)
BUN_BIN = "bun"


def run_cmd(cmd: list[str]) -> tuple[int, str, str]:
    """Run QMD command via bun."""
    try:
        result = subprocess.run(
            [BUN_BIN, str(QMD_BIN)] + cmd,
            cwd=str(SCRIPT_DIR.parent),
            capture_output=True,
            text=True,
            shell=False,
        )
        return result.returncode, result.stdout, result.stderr
    except Exception as e:
        return 1, "", str(e)


def main():
    print("=" * 50)
    print("QMD Index Update — PersonalOS")
    print("=" * 50)

    collections = ["personal-os", "core", "brain", "knowledge"]
    total_updated = 0
    total_removed = 0

    for col in collections:
        print(f"\n[*] Updating collection: {col}")

        # Update index
        code, out, err = run_cmd(["update", "--collection", col])
        if code == 0:
            # Parse output for counts
            for line in out.split("\n"):
                if "updated" in line.lower():
                    print(f"  {line.strip()}")
                if "removed" in line.lower():
                    print(f"  {line.strip()}")
        else:
            print(f"  [!] {err or out}")

    # Re-embed if needed
    print("\n[*] Checking embedding status...")
    code, out, err = run_cmd(["status"])
    if "Vectors:" in out:
        for line in out.split("\n"):
            if "Vectors:" in line or "Pending:" in line:
                print(f"  {line.strip()}")

    print("\n" + "=" * 50)
    print("[OK] QMD Update Complete")
    print("=" * 50)

    print("\nCommands:")
    print("  Search:      bun qmd.js search 'query'")
    print("  Query:       bun qmd.js query 'question'")
    print("  Status:      bun qmd.js status")
    print("  Collections: bun qmd.js collection list")
    print(f"\nQMD binary: {QMD_BIN}")


if __name__ == "__main__":
    main()
