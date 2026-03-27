#!/usr/bin/env python3
"""
Skill Auditor

Analyzes skills against Anthropic standards and reports quality metrics.
"""

import sys
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
        if (parent / ".agent").exists():
            return parent
    return Path.cwd()


def audit_skill(skill_dir):
    """Audit a single skill."""
    results = {
        "name": skill_dir.name,
        "checks": {},
        "passed": 0,
        "failed": 0,
        "missing": [],
    }

    skill_md = skill_dir / "SKILL.md"

    # Check 1: SKILL.md exists
    if skill_md.exists():
        results["checks"]["SKILL.md exists"] = True
        results["passed"] += 1
        content = skill_md.read_text(encoding="utf-8", errors="ignore")

        # Check 2: YAML frontmatter
        has_yaml = content.startswith("---")
        results["checks"]["YAML frontmatter"] = has_yaml
        if has_yaml:
            results["passed"] += 1
        else:
            results["failed"] += 1

        # Check 3: Semantic triggers in description
        has_triggers = (
            "triggers on:" in content.lower() or "triggered when:" in content.lower()
        )
        results["checks"]["Semantic triggers"] = has_triggers
        if has_triggers:
            results["passed"] += 1
        else:
            results["failed"] += 1
            results["missing"].append("Description should have 'triggers on:' keywords")

        # Check 4: Gotchas section
        has_gotchas = "## ⚠️ Gotchas" in content or "## Gotchas" in content
        results["checks"]["Gotchas section"] = has_gotchas
        if has_gotchas:
            results["passed"] += 1
        else:
            results["failed"] += 1
            results["missing"].append("Missing Gotchas section")

        # Check 5: Progressive Disclosure (references/)
        has_references = (skill_dir / "references").exists()
        results["checks"]["References folder"] = has_references
        if has_references:
            results["passed"] += 1
        else:
            results["failed"] += 1
            results["missing"].append("Missing references/ folder")

        # Check 6: Scripts folder
        has_scripts = (skill_dir / "scripts").exists()
        results["checks"]["Scripts folder"] = has_scripts
        if has_scripts:
            results["passed"] += 1
            # Check if scripts work
            scripts = list((skill_dir / "scripts").glob("*.py"))
            if scripts:
                results["checks"]["Scripts exist"] = True
                results["passed"] += 1
            else:
                results["checks"]["Scripts exist"] = False
                results["failed"] += 1
        else:
            results["failed"] += 1
            results["missing"].append("Missing scripts/ folder")

        # Check 7: Esencia Original
        has_esencia = "Esencia Original" in content or "Original" in content
        results["checks"]["Esencia Original"] = has_esencia
        if has_esencia:
            results["passed"] += 1
        else:
            results["failed"] += 1
            results["missing"].append("Missing Esencia Original section")

        # Check 8: State Persistence
        has_state = "State Persistence" in content or "state" in content.lower()
        results["checks"]["State persistence"] = has_state
        if has_state:
            results["passed"] += 1
        else:
            results["failed"] += 1
            results["missing"].append("Missing State Persistence mention")

    else:
        results["checks"]["SKILL.md exists"] = False
        results["failed"] += 1
        results["missing"].append("SKILL.md not found")

    return results


def main():
    print("=" * 60)
    print("🔍 SKILL AUDITOR")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 60)

    project_root = find_project_root()
    skills_dir = project_root / ".agent" / "02_Skills" / "02_Project_Manager"

    if not skills_dir.exists():
        print(f"❌ Skills directory not found: {skills_dir}")
        return

    # Find all skill directories
    skills = [
        d for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()
    ]

    print(f"\n📂 Found {len(skills)} skills to audit\n")

    all_results = []
    total_passed = 0
    total_failed = 0

    for skill_dir in sorted(skills):
        results = audit_skill(skill_dir)
        all_results.append(results)
        total_passed += results["passed"]
        total_failed += results["failed"]

        score = (
            (results["passed"] / (results["passed"] + results["failed"]) * 100)
            if (results["passed"] + results["failed"]) > 0
            else 0
        )

        status = "✅" if score >= 70 else "❌"
        print(
            f"{status} {results['name']}: {results['passed']}/{results['passed'] + results['failed']} ({score:.0f}%)"
        )

        if results["missing"]:
            for m in results["missing"]:
                print(f"   ⚠️  {m}")

    # Summary
    total_checks = total_passed + total_failed
    overall_score = (total_passed / total_checks * 100) if total_checks > 0 else 0

    print("\n" + "=" * 60)
    print("📊 SUMMARY")
    print("=" * 60)
    print(f"Total skills: {len(skills)}")
    print(f"Total checks: {total_checks}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")
    print(f"Overall score: {overall_score:.1f}%")

    if overall_score >= 90:
        print("\n🎉 Excellent! Skills meet Anthropic standards")
    elif overall_score >= 70:
        print("\n👍 Good! Minor improvements needed")
    else:
        print("\n⚠️  Needs work! Run fix-missing.py to correct")

    print("=" * 60)


if __name__ == "__main__":
    main()
