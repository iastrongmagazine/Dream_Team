#!/usr/bin/env python3
"""
Audit Loop — Runs until 100% SOTA v5.1 Compliance

This script:
1. Runs audit-skills.py
2. If any skill < 100%, runs fix-missing.py
3. Repeats until all skills = 100%

Usage:
    python audit-loop.py
    python audit-loop.py --max-iterations 10
"""

import sys
import subprocess
import re
from pathlib import Path
from datetime import datetime

# Fix Windows encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def find_project_root():
    """Find the project root."""
    current = Path(__file__).resolve()
    for parent in [current] + list(current.parents):
        if (parent / ".agent").exists() or (parent / "01_Core").exists():
            return parent
    return Path.cwd()


def parse_audit_results(output: str) -> dict:
    """Parse audit-skills.py output to get scores."""
    results = {}

    # Match patterns like: ✅ 00_Skill_Auditor: 94.1% (16/17 checks)
    # or: ⚠️ 17_SEO_SOTA_Master: 63.6% (7/11 checks)
    pattern = r"([✅⚠️❌])\s+(\S+):\s+(\d+\.?\d*)%"

    for match in re.finditer(pattern, output):
        emoji = match.group(1)
        name = match.group(2)
        score = float(match.group(3))
        results[name] = score

    return results


def run_audit(skills_dir: Path) -> tuple[dict, int]:
    """Run audit-skills.py and return results."""
    script_path = Path(__file__).parent / "audit-skills.py"

    cmd = [sys.executable, str(script_path), str(skills_dir)]

    result = subprocess.run(
        cmd, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )

    output = result.stdout
    scores = parse_audit_results(output)

    # Get overall score
    overall_match = re.search(r"Overall score:\s+(\d+\.?\d*)%", output)
    overall = float(overall_match.group(1)) if overall_match else 0

    return scores, overall


def run_fix(skill_name: str, skills_dir: Path) -> bool:
    """Run fix-missing.py for a specific skill."""
    script_path = Path(__file__).parent / "fix-missing.py"

    cmd = [sys.executable, str(script_path), "--skill", skill_name, str(skills_dir)]

    result = subprocess.run(
        cmd, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )

    return result.returncode == 0


def run_validate_essence(skills_dir: Path) -> dict:
    """Run validate-essence.py and return results."""
    script_path = Path(__file__).parent / "validate-essence.py"

    cmd = [sys.executable, str(script_path), str(skills_dir)]

    result = subprocess.run(
        cmd, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )

    # Parse essence validation results
    output = result.stdout
    scores = {}

    # Match: ✅ 00_Skill_Auditor: 100.0%
    pattern = r"([✅⚠️❌])\s+(\S+):\s+(\d+\.?\d*)%"

    for match in re.finditer(pattern, output):
        emoji = match.group(1)
        name = match.group(2)
        score = float(match.group(3))
        scores[name] = score

    return scores


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Audit loop until 100%")
    parser.add_argument(
        "--max-iterations",
        type=int,
        default=10,
        help="Maximum iterations before giving up",
    )
    parser.add_argument(
        "path", nargs="?", type=str, default=None, help="Path to skills directory"
    )
    args = parser.parse_args()

    print("=" * 70)
    print("🔄 AUDIT LOOP — HASTA 100%")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)

    project_root = find_project_root()

    # Determine skills directory
    if args.path:
        skills_dir = Path(args.path)
    else:
        skills_dir = project_root / "01_Core" / "03_Skills"
        if not skills_dir.exists():
            skills_dir = project_root / ".agent" / "02_Skills"

    if not skills_dir.exists():
        print(f"❌ Skills directory not found: {skills_dir}")
        return

    print(f"\n📂 Skills directory: {skills_dir}\n")

    iteration = 0
    all_100 = False

    while iteration < args.max_iterations and not all_100:
        iteration += 1
        print(f"\n{'=' * 70}")
        print(f"🔄 ITERACIÓN {iteration}/{args.max_iterations}")
        print(f"{'=' * 70}")

        # Run audit
        print("\n📊 Ejecutando auditoría...")
        scores, overall = run_audit(skills_dir)

        # Run essence validation
        print("🎭 Validando esencia...")
        essence_scores = run_validate_essence(skills_dir)

        # Check for skills below 100%
        below_100 = [(name, score) for name, score in scores.items() if score < 100]

        if not below_100:
            all_100 = True
            print("\n" + "=" * 70)
            print("🎉 ¡ÉXITO! Todas las skills = 100%")
            print("=" * 70)
            break

        # Show current status
        print(f"\n📈 Estado actual:")
        for name, score in sorted(scores.items()):
            emoji = "✅" if score == 100 else "⚠️"
            print(f"   {emoji} {name}: {score}%")

        print(f"\n📊 Overall: {overall}%")

        # Fix skills below 100%
        print(f"\n🔧 Corrigiendo {len(below_100)} skills...")
        for name, score in below_100:
            print(f"   🔧 Fixing {name}...")
            success = run_fix(name, skills_dir)
            if success:
                print(f"      ✅ Applied fixes to {name}")
            else:
                print(f"      ⚠️ Could not fix {name}")

        # Brief pause
        print("\n⏳ Preparando siguiente iteración...")

    # Final audit
    print("\n" + "=" * 70)
    print("📋 AUDITORÍA FINAL")
    print("=" * 70)

    scores, overall = run_audit(skills_dir)

    for name, score in sorted(scores.items()):
        emoji = "✅" if score == 100 else "⚠️" if score >= 70 else "❌"
        print(f"   {emoji} {name}: {score}%")

    print(f"\n📊 Overall: {overall}%")

    if all_100:
        print("\n🎉 ¡TODAS LAS SKILLS 100%!")
    else:
        print(f"\n⚠️  No se alcanzó 100% en {args.max_iterations} iteraciones")
        print("   Ejecuta audit-loop.py nuevamente o revisa manualmente")

    print("=" * 70)

    return 0 if all_100 else 1


if __name__ == "__main__":
    sys.exit(main())
