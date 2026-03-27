#!/usr/bin/env python3
"""
Validate Esencia Original - SOTA v5.1

Verifies that skills maintain their original purpose and essence.
This prevents scope creep and drift from original intent.

Supports PersonalOS structure: 01_Core/03_Skills/
"""

import sys
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


def validate_essence(skill_dir: Path) -> dict:
    """Validate that a skill maintains its original essence."""
    results = {
        "name": skill_dir.name,
        "path": str(skill_dir),
        "has_essence": False,
        "essence_content": "",
        "checks": {},
        "passed": 0,
        "failed": 0,
        "issues": [],
    }

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        results["checks"]["SKILL.md exists"] = False
        results["failed"] += 1
        results["issues"].append("SKILL.md not found")
        return results

    results["checks"]["SKILL.md exists"] = True
    results["passed"] += 1

    content = skill_md.read_text(encoding="utf-8", errors="ignore")

    # =========================================================================
    # CHECK 1: Esencia Original Section
    # =========================================================================
    esencia_patterns = [
        r"##\s*Esencia\s+Original",
        r"##\s*Esencia",
        r"##\s*Original\s+Purpose",
        r"##\s*Purpose",
    ]

    esencia_match = None
    for pattern in esencia_patterns:
        match = re.search(pattern, content, re.IGNORECASE)
        if match:
            esencia_match = match
            break

    if esencia_match:
        results["has_essence"] = True
        results["passed"] += 1

        # Extract essence content (next 500 chars after header)
        start = esencia_match.end()
        essence_text = content[start : start + 500].strip()
        results["essence_content"] = essence_text[:200]

        # Check essence is not empty
        if len(essence_text.strip()) > 20:
            results["checks"]["Essence content valid"] = True
            results["passed"] += 1
        else:
            results["checks"]["Essence content valid"] = False
            results["failed"] += 1
            results["issues"].append("Esencia Original section is empty or too short")

        # Check it defines a purpose
        has_purpose_keywords = any(
            kw in essence_text.lower()
            for kw in [
                "purpose",
                "objetivo",
                "meta",
                "goal",
                "mission",
                "qué hace",
                "what it does",
                "problem",
                "solves",
                "metaskill",
            ]
        )
        results["checks"]["Defines purpose"] = has_purpose_keywords
        if has_purpose_keywords:
            results["passed"] += 1
        else:
            results["failed"] += 1
            results["issues"].append("Esencia Original doesn't define clear purpose")
    else:
        results["checks"]["Esencia Original section"] = False
        results["failed"] += 1
        results["issues"].append("Missing '## Esencia Original' section")

    # =========================================================================
    # CHECK 2: Metaskill Defined
    # =========================================================================
    metaskill_patterns = [
        r"metaskill",
        r"meta[- ]skill",
        r">\s*\*\*[Mm]etaskill",
    ]

    has_metaskill = any(re.search(p, content) for p in metaskill_patterns)
    results["checks"]["Metaskill documented"] = has_metaskill

    if has_metaskill:
        results["passed"] += 1

    # =========================================================================
    # CHECK 3: Hasn't drifted (no excessive new sections)
    # =========================================================================
    section_count = len(re.findall(r"^##\s+", content, re.MULTILINE))
    results["checks"]["Section count reasonable"] = section_count < 15

    if section_count < 15:
        results["passed"] += 1
    else:
        results["failed"] += 1
        results["issues"].append(
            f"Too many sections ({section_count}) - possible scope drift"
        )

    # =========================================================================
    # CHECK 4: Has semantic triggers (for invocation)
    # =========================================================================
    has_triggers = (
        "triggers on:" in content.lower() or "triggered when:" in content.lower()
    )
    results["checks"]["Semantic triggers"] = has_triggers

    if has_triggers:
        results["passed"] += 1
    else:
        results["failed"] += 1
        results["issues"].append("Missing semantic triggers in YAML description")

    # =========================================================================
    # CHECK 5: Has Gotchas (knowledge preservation)
    # =========================================================================
    has_gotchas = "## Gotchas" in content or "## ⚠️ Gotchas" in content
    results["checks"]["Has Gotchas"] = has_gotchas

    if has_gotchas:
        results["passed"] += 1
    else:
        results["failed"] += 1
        results["issues"].append("Missing Gotchas section")

    return results


def main():
    print("=" * 70)
    print("🎭 VALIDATE ESSENCIA ORIGINAL - SOTA v5.1")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)

    project_root = find_project_root()
    skills_dir = project_root / "01_Core" / "03_Skills"

    # Allow custom path argument
    if len(sys.argv) > 1:
        skills_dir = Path(sys.argv[1])

    if not skills_dir.exists():
        # Try alternative paths
        skills_dir = project_root / ".agent" / "02_Skills"

    if not skills_dir.exists():
        print(f"❌ Skills directory not found")
        print("Usage: python validate-essence.py [path_to_skills_dir]")
        return

    skills = [
        d for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()
    ]

    print(f"\n📂 Validating essence for {len(skills)} skills\n")

    all_results = []
    total_passed = 0
    total_failed = 0

    for skill_dir in sorted(skills):
        results = validate_essence(skill_dir)
        all_results.append(results)
        total_passed += results["passed"]
        total_failed += results["failed"]

        score = round(
            (results["passed"] / (results["passed"] + results["failed"]) * 100)
            if (results["passed"] + results["failed"]) > 0
            else 0,
            1,
        )

        status = "✅" if score >= 70 else "❌"
        print(f"{status} {results['name']}: {score}%")

        if results.get("essence_content"):
            preview = results["essence_content"][:80].replace("\n", " ")
            print(f"   📝 {preview}...")

        if results.get("issues"):
            for issue in results["issues"]:
                print(f"   ⚠️  {issue}")

    # Summary
    total_checks = total_passed + total_failed
    overall_score = round(
        (total_passed / total_checks * 100) if total_checks > 0 else 0, 1
    )

    print("\n" + "=" * 70)
    print("📊 ESSENCE VALIDATION SUMMARY")
    print("=" * 70)
    print(f"Total skills: {len(skills)}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")
    print(f"Overall score: {overall_score}%")

    if overall_score >= 90:
        print("\n🎉 EXCELLENT! All skills maintain their essence")
    elif overall_score >= 70:
        print("\n👍 GOOD! Most essence preserved")
    else:
        print("\n⚠️  NEEDS WORK! Some skills may have lost their essence")

    # Skills needing attention
    needs_attention = [r for r in all_results if r["passed"] < r["failed"]]
    if needs_attention:
        print("\n🔧 Skills needing essence review:")
        for r in needs_attention:
            print(f"   - {r['name']}")

    print("=" * 70)


if __name__ == "__main__":
    main()
