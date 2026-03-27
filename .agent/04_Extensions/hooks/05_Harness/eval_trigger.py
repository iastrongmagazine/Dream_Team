#!/usr/bin/env python3
"""
05_Harness/eval_trigger.py — Evaluator Trigger Hook

Hook de PostToolUse para invocar el Evaluator después de builds grandes.
Sugiere o automáticament invoca el Evaluator cuando detecta trabajo completado.

VERSIÓN: 1.0
 fecha: 2026-03-26
 FILOSOFÍA: "No te traiciones, no te abandones" — Siempre lo correcto
"""

import os
import sys
import json
from pathlib import Path

# ========================
# CONFIGURATION
# ========================

# Threshold de archivos modificados para invocar evaluator
FILES_THRESHOLD = 10  # >10 archivos = probablemente un feature completo

# File types que trigger evaluation
CODE_EXTENSIONS = [
    ".py",
    ".js",
    ".ts",
    ".tsx",
    ".jsx",
    ".go",
    ".rs",
    ".java",
    ".rb",
    ".php",
    ".html",
    ".css",
    ".scss",
]

# Log file
LOG_FILE = ".claude/logs/eval_trigger.log"


def get_modified_files():
    """Get list of modified files in last commit/tool use"""

    # Check git diff
    try:
        import subprocess

        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            files = [f.strip() for f in result.stdout.split("\n") if f.strip()]
            return files
    except:
        pass

    return []


def analyze_changes(files):
    """Analyze changes to determine if evaluation is needed"""

    code_files = [f for f in files if any(f.endswith(ext) for ext in CODE_EXTENSIONS)]

    return {
        "total_files": len(files),
        "code_files": len(code_files),
        "should_eval": len(code_files) >= FILES_THRESHOLD,
    }


def trigger_evaluation():
    """Main evaluation trigger logic"""

    files = get_modified_files()
    analysis = analyze_changes(files)

    # Log
    log_entry = {"files": files, "analysis": analysis}

    print(f"\n🎯 EVAL TRIGGER CHECK:")
    print(f"   Total files: {analysis['total_files']}")
    print(f"   Code files: {analysis['code_files']}")
    print(f"   Should evaluate: {analysis['should_eval']}")

    if analysis["should_eval"]:
        print(f"\n   ⚠️  Recommendation: Run Evaluator!")
        print(
            f"   Command: python 04_Engine/08_Scripts_Os/11_Anthropic_Harness/02_Evaluator_Runner.py"
        )
    else:
        print(f"\n   ✅ No evaluation needed")

    print()

    # Save to log
    try:
        Path(LOG_FILE).parent.mkdir(parents=True, exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except:
        pass

    return analysis


def main():
    """Main entry point"""
    analysis = trigger_evaluation()

    # Exit
    sys.exit(0)


if __name__ == "__main__":
    main()
