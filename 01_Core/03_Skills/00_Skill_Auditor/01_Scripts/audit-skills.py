#!/usr/bin/env python3
"""
Skill Auditor - SOTA v5.1

Analyzes skills against Anthropic SOTA standards and PersonalOS v5.1 requirements.
Includes checks for: YAML frontmatter, Gotchas, Progressive Disclosure,
Esencia Original, State Persistence, and v2.0 features (evals).
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


def count_lines(content: str) -> int:
    """Count non-empty lines."""
    return len([l for l in content.split("\n") if l.strip()])


def audit_skill(skill_dir: Path) -> dict:
    """Audit a single skill against SOTA v5.1 standards."""
    results = {
        "name": skill_dir.name,
        "path": str(skill_dir),
        "checks": {},
        "passed": 0,
        "failed": 0,
        "warnings": [],
        "missing": [],
        "score": 0,
    }

    skill_md = skill_dir / "SKILL.md"

    # =========================================================================
    # CHECK 1: SKILL.md exists
    # =========================================================================
    if not skill_md.exists():
        results["checks"]["SKILL.md exists"] = False
        results["failed"] += 1
        results["missing"].append("SKILL.md not found")
        results["score"] = 0
        return results

    results["checks"]["SKILL.md exists"] = True
    results["passed"] += 1

    content = skill_md.read_text(encoding="utf-8", errors="ignore")
    line_count = count_lines(content)

    # =========================================================================
    # CHECK 2: YAML Frontmatter
    # =========================================================================
    has_yaml = content.startswith("---")
    results["checks"]["YAML frontmatter"] = has_yaml
    if has_yaml:
        results["passed"] += 1

        # Extract YAML
        yaml_match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
        if yaml_match:
            yaml_content = yaml_match.group(1)

            # Check name field
            name_match = re.search(r"^name:\s*(.+)$", yaml_content, re.MULTILINE)
            if name_match:
                name_value = name_match.group(1).strip()
                # Check lowercase
                is_lowercase = name_value == name_value.lower()
                # Check no spaces
                no_spaces = " " not in name_value
                # Check gerund (optional heuristic)
                is_gerund = name_value.endswith("-") or any(
                    name_value.endswith(f"-{suffix}")
                    for suffix in ["ing", "tion", "s", "ed"]
                )
                # Check prohibited words
                prohibited = any(
                    word in name_value.lower() for word in ["claude", "anthropic"]
                )

                results["checks"]["name: lowercase"] = is_lowercase
                results["checks"]["name: no spaces"] = no_spaces
                results["checks"]["name: no prohibited words"] = not prohibited

                if is_lowercase:
                    results["passed"] += 1
                else:
                    results["failed"] += 1
                    results["missing"].append("name must be lowercase")

                if no_spaces:
                    results["passed"] += 1
                else:
                    results["failed"] += 1
                    results["missing"].append("name must not contain spaces")

                if not prohibited:
                    results["passed"] += 1
                else:
                    results["failed"] += 1
                    results["missing"].append(
                        "name cannot contain 'claude' or 'anthropic'"
                    )
            else:
                results["failed"] += 1
                results["missing"].append("Missing 'name' field in YAML")

            # Check description field - handle both single-line and multi-line YAML
            # First try single-line, then try multi-line with ">" or "|"
            desc_match = re.search(r"^description:\s*(.+)$", yaml_content, re.MULTILINE)
            if not desc_match:
                # Try to match multi-line description (with > or |)
                desc_match = re.search(
                    r"^description:\s*[>|]\s*\n(.+?)\n---", yaml_content, re.DOTALL
                )

            if desc_match:
                desc_value = desc_match.group(1).strip()
                # Also check the full YAML section for triggers
                full_desc_check = yaml_content

                # Check triggers - accept "triggers on:", "triggers:", "trigger:", "TRIGGERS:"
                has_triggers = (
                    "triggers" in desc_value.lower()
                    or "trigger" in desc_value.lower()
                    or "triggers" in full_desc_check.lower()
                )
                results["checks"]["description: has triggers"] = has_triggers

                if has_triggers:
                    results["passed"] += 1
                else:
                    results["failed"] += 1
                    results["missing"].append("description must include 'triggers'")

                # Check length
                is_valid_length = len(desc_value) <= 1024
                results["checks"]["description: valid length"] = is_valid_length
                if is_valid_length:
                    results["passed"] += 1
                else:
                    results["failed"] += 1
            else:
                results["failed"] += 1
                results["missing"].append("Missing 'description' field in YAML")
    else:
        results["failed"] += 1
        results["missing"].append("SKILL.md must start with YAML frontmatter (---)")

    # =========================================================================
    # CHECK 3: Progressive Disclosure
    # =========================================================================
    # Line count - solo fail si pasa de 700
    is_under_limit = line_count < 200
    is_under_max = line_count < 700
    results["checks"]["SKILL.md: < 200 lines"] = is_under_limit

    if is_under_limit:
        results["passed"] += 1
    elif is_under_max:
        results["warnings"].append(f"SKILL.md has {line_count} lines (ideal: < 200)")
        results["passed"] += 1  # Pass but warn if under 700
    else:
        results["failed"] += 1
        results["missing"].append(f"SKILL.md has {line_count} lines (max: 500)")

    # References folder
    has_references = (skill_dir / "references").exists()
    results["checks"]["references/ folder"] = has_references
    if has_references:
        results["passed"] += 1
    elif line_count > 200:
        results["failed"] += 1
        results["missing"].append("references/ folder needed (SKILL.md > 200 lines)")
    else:
        results["warnings"].append("references/ folder recommended")

    # Scripts folder (optional)
    has_scripts = (skill_dir / "scripts").exists()
    results["checks"]["scripts/ folder"] = has_scripts
    if has_scripts:
        results["passed"] += 1
        # Check if scripts exist
        scripts = list((skill_dir / "scripts").glob("*.py"))
        if scripts:
            results["checks"]["scripts: exist"] = True
            results["passed"] += 1
    else:
        results["warnings"].append("scripts/ folder recommended")

    # =========================================================================
    # CHECK 4: Gotchas Section
    # =========================================================================
    has_gotchas = (
        "## ⚠️ Gotchas" in content
        or "## Gotchas" in content
        or "## Gotchas (Common Mistakes)" in content
    )
    results["checks"]["Gotchas section"] = has_gotchas

    if has_gotchas:
        results["passed"] += 1

        # Count gotchas (look for "**Don't**:" or "- **ERROR**:" or "- Don't:")
        gotcha_patterns = [
            r"\*\*Don\'t\*\*:",  # **Don't**:
            r"\*\*ERROR\*\*:",  # **ERROR**:
            r"\*\*\[ERROR\]\*\*:",  # **[ERROR]**:
            r"### ERROR",  # ### ERROR 1: (markdown header)
            r"^- Don\'t:",  # - Don't:
            r"^- \[ERROR\]:",  # - [ERROR]:
            r"^- \*\*\[ERROR\]\*\*:",  # - **[ERROR]**:
        ]
        gotcha_count = 0
        for pattern in gotcha_patterns:
            gotcha_count += len(re.findall(pattern, content, re.IGNORECASE))

        has_minimum_gotchas = gotcha_count >= 3
        results["checks"]["Gotchas: minimum 3"] = has_minimum_gotchas

        if has_minimum_gotchas:
            results["passed"] += 1
        else:
            results["failed"] += 1
            results["missing"].append(f"Need minimum 3 gotchas (found: {gotcha_count})")

        # Check for "Por qué" and "Solución"
        has_por_que = "Por qué" in content or "por qué" in content
        has_solucion = "Solución" in content or "Solucion" in content
        results["checks"]["Gotchas: has Por qué"] = has_por_que
        results["checks"]["Gotchas: has Solución"] = has_solucion

        if has_por_que:
            results["passed"] += 1
        else:
            results["warnings"].append("Gotchas should include 'Por qué'")

        if has_solucion:
            results["passed"] += 1
        else:
            results["warnings"].append("Gotchas should include 'Solución'")
    else:
        results["failed"] += 1
        results["missing"].append("Missing Gotchas section")

    # =========================================================================
    # CHECK 5: Esencia Original
    # =========================================================================
    has_esencia = "## Esencia Original" in content or "## Esencia" in content
    results["checks"]["Esencia Original section"] = has_esencia
    if has_esencia:
        results["passed"] += 1
    else:
        results["failed"] += 1
        results["missing"].append("Missing Esencia Original section")

    # =========================================================================
    # CHECK 6: State Persistence
    # =========================================================================
    has_state = "State Persistence" in content or "state persistence" in content.lower()
    results["checks"]["State Persistence"] = has_state
    if has_state:
        results["passed"] += 1
    else:
        results["warnings"].append("State Persistence not mentioned (recommended)")

    # =========================================================================
    # CHECK 7: v2.0 Features (OPTIONAL)
    # =========================================================================
    # evals.json
    has_evals = (skill_dir / "evals.json").exists()
    results["checks"]["evals.json (v2.0)"] = has_evals
    if has_evals:
        results["passed"] += 1
    else:
        results["warnings"].append("evals.json not found (v2.0 recommendation)")

    # agents/ folder
    has_agents = (skill_dir / "agents").exists()
    results["checks"]["agents/ folder"] = has_agents
    if has_agents:
        results["passed"] += 1

    # Calculate score
    total_checks = results["passed"] + results["failed"]
    results["score"] = round(
        (results["passed"] / total_checks * 100) if total_checks > 0 else 0, 1
    )
    results["line_count"] = line_count

    return results


def main():
    print("=" * 70)
    print("🔍 SKILL AUDITOR - SOTA v5.1")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("=" * 70)

    project_root = find_project_root()

    # Default to 01_Core/03_Skills
    skills_dir = project_root / "01_Core" / "03_Skills"

    if not skills_dir.exists():
        # Try alternative path
        skills_dir = project_root / ".agent" / "02_Skills"

    if not skills_dir.exists():
        print(f"❌ Skills directory not found: {skills_dir}")
        print("Usage: python audit-skills.py [path_to_skills_dir]")
        return

    # Allow custom path argument
    if len(sys.argv) > 1:
        skills_dir = Path(sys.argv[1])
        if not skills_dir.exists():
            print(f"❌ Directory not found: {skills_dir}")
            return

    # Find all skill directories
    skills = [
        d for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()
    ]

    print(f"\n📂 Found {len(skills)} skills to audit\n")

    all_results = []
    total_passed = 0
    total_failed = 0
    total_warnings = 0

    for skill_dir in sorted(skills):
        results = audit_skill(skill_dir)
        all_results.append(results)
        total_passed += results["passed"]
        total_failed += results["failed"]
        total_warnings += len(results["warnings"])

        # Score emoji
        if results["score"] >= 90:
            status = "✅"
        elif results["score"] >= 70:
            status = "👍"
        elif results["score"] >= 50:
            status = "⚠️"
        else:
            status = "❌"

        print(
            f"{status} {results['name']}: {results['score']}% ({results['passed']}/{results['passed'] + results['failed']} checks)"
        )

        if results["warnings"]:
            for w in results["warnings"]:
                print(f"   💡 {w}")

        if results["missing"]:
            for m in results["missing"]:
                print(f"   ⚠️  {m}")

    # Summary
    total_checks = total_passed + total_failed
    overall_score = round(
        (total_passed / total_checks * 100) if total_checks > 0 else 0, 1
    )

    print("\n" + "=" * 70)
    print("📊 SUMMARY")
    print("=" * 70)
    print(f"Total skills: {len(skills)}")
    print(f"Total checks: {total_checks}")
    print(f"Passed: {total_passed}")
    print(f"Failed: {total_failed}")
    print(f"Warnings: {total_warnings}")
    print(f"Overall score: {overall_score}%")

    if overall_score >= 90:
        print("\n🎉 EXCELLENT! Skills meet SOTA v5.1 standards")
    elif overall_score >= 70:
        print("\n👍 GOOD! Minor improvements needed")
    elif overall_score >= 50:
        print("\n⚠️  NEEDS WORK! Significant fixes required")
    else:
        print("\n❌ FAILED! Do not integrate until fixed")

    print("=" * 70)

    # List skills that need attention
    needs_attention = [r for r in all_results if r["score"] < 70]
    if needs_attention:
        print("\n🔧 Skills needing attention (< 70%):")
        for r in needs_attention:
            print(f"   - {r['name']}: {r['score']}%")

    return overall_score


if __name__ == "__main__":
    main()
