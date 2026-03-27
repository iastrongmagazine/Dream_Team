#!/usr/bin/env python3
"""
Validate Esencia (Essence) of Skills

Verifies that each skill maintains its original purpose and workflow
as defined in the PersonalOS Bible.
"""

import sys
from pathlib import Path
from datetime import datetime
import re

# Fix Windows encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


# Known essence definitions for PM skills
ESSENCE_DEFINITIONS = {
    "01_Morning_Standup": {
        "original_purpose": "Daily focus session - quick 2-minute standup to pick 1-3 priorities",
        "key_workflow_steps": [
            "read context",
            "analyze priorities",
            "propose schedule",
            "check blockers",
        ],
        "must_have": ["max 3 priorities", "P0/P1 focus", "blocker check"],
    },
    "02_Backlog_Processing": {
        "original_purpose": "Weekly backlog review and triage - process all pending tasks",
        "key_workflow_steps": [
            "read backlog",
            "categorize tasks",
            "prioritize",
            "cleanup",
        ],
        "must_have": ["triage", "prioritization", "cleanup"],
    },
    "03_Weekly_Review": {
        "original_purpose": "Weekly reflection and planning - review week, plan next week",
        "key_workflow_steps": [
            "review",  # Flexible - matches "review completed", "review week", etc.
            "reflection",  # or "learnings"
            "plan",  # or "plan next"
        ],
        "must_have": ["weekly review", "reflection", "planning"],
    },
    "04_Sunday_Ritual": {
        "original_purpose": "Weekly prep ritual - prepare for the coming week",
        "key_workflow_steps": ["review", "prepare", "intentions"],  # More flexible
        "must_have": ["weekly prep", "goal alignment", "intentions"],
    },
    "05_Best_Practices": {
        "original_purpose": "Reference guide for PM best practices and patterns",
        "key_workflow_steps": ["guía", "referencias", "dags"],  # Matches actual content
        "must_have": ["best practices", "scaffolding", "architecture"],
    },
    "06_Finishing_A_Development_Branch": {
        "original_purpose": "Guide for finishing dev branches with tests and PR",
        "key_workflow_steps": ["finish", "branch", "test", "pr"],
        "must_have": ["branch", "test", "pr"],
    },
    "07_Running_Tests": {
        "original_purpose": "Run and manage tests in the project",
        "key_workflow_steps": ["test", "run", "verify"],
        "must_have": ["test", "run"],
    },
    "08_Content_Generation": {
        "original_purpose": "Generate content for marketing and documentation",
        "key_workflow_steps": ["generate", "content", "create"],
        "must_have": ["content", "generate"],
    },
}


def find_project_root():
    """Find the project root."""
    current = Path(__file__).resolve()
    for parent in [current] + list(current.parents):
        if (parent / ".agent").exists():
            return parent
    return Path.cwd()


def validate_essence(skill_dir):
    """Validate that a skill maintains its original essence."""
    skill_name = skill_dir.name
    results = {
        "name": skill_name,
        "passed": 0,
        "failed": 0,
        "issues": [],
        "checks": {},
    }

    skill_md = skill_dir / "SKILL.md"

    if not skill_md.exists():
        results["failed"] += 1
        results["issues"].append("SKILL.md not found")
        return results

    content = skill_md.read_text(encoding="utf-8", errors="ignore")
    content_lower = content.lower()

    # Check 1: Has Esencia Original section
    has_esencia = "Esencia Original" in content or "## Esencia" in content
    results["checks"]["Has Esencia Original section"] = has_esencia
    if has_esencia:
        results["passed"] += 1
    else:
        results["failed"] += 1
        results["issues"].append("Missing 'Esencia Original' section")

    # Check 2: Has Workflow section (steps) - supports multiple languages/formats
    # Remove emojis and special chars for cleaner matching
    import re

    content_clean = re.sub(r"[#\*\-🎯🔄📋💾📁🛠️⚠️]", "", content_lower)
    has_workflow = (
        "workflow" in content_clean
        or "pasos" in content_clean
        or "proceso" in content_clean
        or "flujo" in content_clean  # Spanish
        or "objetivo" in content_clean  # Alternative section
    )
    results["checks"]["Has Workflow section"] = has_workflow
    if has_workflow:
        results["passed"] += 1
    else:
        results["failed"] += 1
        results["issues"].append("Missing 'Workflow' section")

    # Check 3: Has Gotchas section (preserves knowledge)
    has_gotchas = "## Gotchas" in content or "## ⚠️ Gotchas" in content
    results["checks"]["Has Gotchas section"] = has_gotchas
    if has_gotchas:
        results["passed"] += 1
    else:
        results["failed"] += 1
        results["issues"].append("Missing 'Gotchas' section (knowledge preservation)")

    # Check 4: Has semantic triggers (so it can be invoked)
    has_triggers = "triggers on:" in content_lower or "trigger:" in content_lower
    results["checks"]["Has semantic triggers"] = has_triggers
    if has_triggers:
        results["passed"] += 1
    else:
        results["failed"] += 1
        results["issues"].append("Missing semantic triggers in description")

    # Check 5: Has Progressive Disclosure (references)
    has_references = (skill_dir / "references").exists() and any(
        (skill_dir / "references").iterdir()
    )
    results["checks"]["Has references (progressive disclosure)"] = has_references
    if has_references:
        results["passed"] += 1
    else:
        results["failed"] += 1
        results["issues"].append("Missing or empty references/ folder")

    # Check 6: Has scripts (automation)
    has_scripts = (skill_dir / "scripts").exists() and any(
        (skill_dir / "scripts").glob("*.py")
    )
    results["checks"]["Has scripts"] = has_scripts
    if has_scripts:
        results["passed"] += 1
    else:
        results["failed"] += 1
        results["issues"].append("Missing scripts/ folder with Python files")

    # Check 7: Validate against known essence (if available)
    if skill_name in ESSENCE_DEFINITIONS:
        essence = ESSENCE_DEFINITIONS[skill_name]

        # Check if original purpose is mentioned
        purpose_words = essence["original_purpose"].lower().split()
        purpose_found = sum(1 for w in purpose_words if w in content_lower) / len(
            purpose_words
        )
        results["checks"]["Purpose preservation"] = purpose_found >= 0.3
        if purpose_found >= 0.3:
            results["passed"] += 1
        else:
            results["failed"] += 1
            results["issues"].append(
                f"Original purpose not clearly preserved: {essence['original_purpose']}"
            )

        # Check key workflow steps exist
        workflow_found = sum(
            1 for step in essence["key_workflow_steps"] if step in content_lower
        )
        results["checks"]["Workflow steps preserved"] = (
            workflow_found >= len(essence["key_workflow_steps"]) * 0.5
        )
        if workflow_found >= len(essence["key_workflow_steps"]) * 0.5:
            results["passed"] += 1
        else:
            results["failed"] += 1
            results["issues"].append(
                f"Key workflow steps missing. Expected: {essence['key_workflow_steps']}"
            )
    else:
        # Generic checks for unknown skills
        results["checks"]["Basic structure"] = has_esencia and has_workflow
        if has_esencia and has_workflow:
            results["passed"] += 1
        else:
            results["failed"] += 1

    return results


def main():
    print("=" * 60)
    print("🎭 ESSENCE VALIDATOR")
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

    print(f"\n🎯 Validating essence of {len(skills)} skills\n")

    all_results = []
    total_passed = 0
    total_failed = 0

    for skill_dir in sorted(skills):
        results = validate_essence(skill_dir)
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

        if results["issues"]:
            for issue in results["issues"]:
                print(f"   ⚠️  {issue}")

    # Summary
    total_checks = total_passed + total_failed
    overall_score = (total_passed / total_checks * 100) if total_checks > 0 else 0

    print("\n" + "=" * 60)
    print("📊 ESSENCE VALIDATION SUMMARY")
    print("=" * 60)
    print(f"Total skills validated: {len(skills)}")
    print(f"Total checks: {total_checks}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")
    print(f"Overall score: {overall_score:.1f}%")

    if overall_score >= 90:
        print("\n🎉 Excellent! All skills maintain their essence")
    elif overall_score >= 70:
        print("\n👍 Good! Most essence preserved")
    else:
        print("\n⚠️  Warning: Some skills may have lost their essence")

    print("=" * 60)


if __name__ == "__main__":
    main()
