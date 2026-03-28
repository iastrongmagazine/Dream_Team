#!/usr/bin/env python3
"""
Fix Missing Components

Auto-fixes common issues found during skill audits:
- Adds missing YAML frontmatter
- Adds missing Gotchas section
- Adds missing references folder
- Adds missing scripts folder
- Adds missing Esencia Original section
"""

import sys
from pathlib import Path
from datetime import datetime

# Fix Windows encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


# Templates for missing components
YAML_TEMPLATE = """---
name: {skill_name}
description: {skill_description}
---

"""

ESCENCIA_TEMPLATE = """
## Esencia Original

> Original purpose of this skill. This section preserves WHY this skill exists.

"""

GOTCHAS_TEMPLATE = """

## ⚠️ Gotchas (Errores Comunes a Evitar)

> Common mistakes and edge cases to watch for when using this skill.

- **[ERROR]**: No verificar triggers semánticos en la descripción
  - **Por qué**: Sin triggers, la skill no se activa cuando el usuario la necesita
  - **Solución**: Incluir "triggers on:" con keywords que el usuario usa realmente

- **[ERROR]**: No verificar Gotchas al crear una skill
  - **Por qué**: Sin gotchas documentadas, los errores se repiten
  - **Solución**: Agregar mínimo 3 errores comunes con "Por qué" y "Solución"

- **[ERROR]**: SKILL.md excede 200 líneas
  - **Por qué**: Satura el context window y empeora el rendimiento
  - **Solución**: Mover contenido a references/ para progressive disclosure

- **[ERROR]**: No verificar esencia original
  - **Por qué**: La skill puede perder su propósito con el tiempo
  - **Solución**: Documentar "## Esencia Original" al inicio

"""

REFERENCES_README_TEMPLATE = """# {skill_name} - References

Additional documentation and resources for this skill.

## Files

- [](./) - Add reference files here

"""


def find_project_root():
    """Find the project root."""
    current = Path(__file__).resolve()
    for parent in [current] + list(current.parents):
        if (parent / ".agent").exists() or (parent / "01_Core").exists():
            return parent
    return Path.cwd()


def add_yaml_frontmatter(skill_md, skill_name):
    """Add YAML frontmatter if missing."""
    content = skill_md.read_text(encoding="utf-8", errors="ignore")

    if content.startswith("---"):
        return False, "YAML frontmatter already exists"

    # Extract description from first paragraph
    lines = content.split("\n")
    description = ""
    for line in lines:
        line = line.strip()
        if line and not line.startswith("#"):
            description = line[:100]
            break

    if not description:
        description = f"Skill: {skill_name}"

    new_content = (
        YAML_TEMPLATE.format(
            skill_name=skill_name.lower().replace("_", "-"),
            skill_description=description,
        )
        + content
    )

    skill_md.write_text(new_content, encoding="utf-8")
    return True, "Added YAML frontmatter"


def add_esencia_original(skill_md):
    """Add Esencia Original section if missing."""
    content = skill_md.read_text(encoding="utf-8", errors="ignore")

    if "Esencia Original" in content:
        return False, "Esencia Original already exists"

    # Find a good place to insert - after the first heading
    lines = content.split("\n")
    insert_idx = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("# ") and i > 0:
            insert_idx = i + 1
            break

    lines.insert(insert_idx, ESCENCIA_TEMPLATE)
    new_content = "\n".join(lines)

    skill_md.write_text(new_content, encoding="utf-8")
    return True, "Added Esencia Original section"


def add_gotchas(skill_md):
    """Add Gotchas section if missing."""
    content = skill_md.read_text(encoding="utf-8", errors="ignore")

    if "## Gotchas" in content or "## ⚠️ Gotchas" in content:
        return False, "Gotchas section already exists"

    # Add before Progressive Disclosure or at end
    if "## Progressive Disclosure" in content:
        content = content.replace(
            "## Progressive Disclosure",
            GOTCHAS_TEMPLATE + "\n## Progressive Disclosure",
        )
    elif "## 📁 Progressive Disclosure" in content:
        content = content.replace(
            "## 📁 Progressive Disclosure",
            GOTCHAS_TEMPLATE + "\n## 📁 Progressive Disclosure",
        )
    else:
        content += GOTCHAS_TEMPLATE

    skill_md.write_text(content, encoding="utf-8")
    return True, "Added Gotchas section"


def add_references_folder(skill_dir, skill_name):
    """Create references folder with README if missing."""
    refs_dir = skill_dir / "references"

    if refs_dir.exists() and any(refs_dir.iterdir()):
        return False, "references folder already exists with content"

    refs_dir.mkdir(exist_ok=True)
    readme = refs_dir / "README.md"
    readme.write_text(
        REFERENCES_README_TEMPLATE.format(skill_name=skill_name), encoding="utf-8"
    )
    return True, "Created references/ folder with README"


def add_scripts_folder(skill_dir):
    """Create scripts folder with placeholder if missing."""
    scripts_dir = skill_dir / "scripts"

    if scripts_dir.exists() and any(scripts_dir.iterdir()):
        return False, "scripts folder already exists with content"

    scripts_dir.mkdir(exist_ok=True)
    placeholder = scripts_dir / "README.md"
    placeholder.write_text(
        """# Scripts

Add Python scripts here to automate tasks.

## Usage

```bash
python scripts/your-script.py
```

""",
        encoding="utf-8",
    )
    return True, "Created scripts/ folder"


def fix_skill(skill_dir, dry_run=False):
    """Apply all fixes to a skill."""
    skill_name = skill_dir.name
    skill_md = skill_dir / "SKILL.md"

    fixes_applied = []

    if not skill_md.exists():
        return [f"SKILL.md not found - cannot fix"]

    # Fix 1: YAML frontmatter
    success, msg = add_yaml_frontmatter(skill_md, skill_name)
    if success:
        fixes_applied.append(msg)

    # Fix 2: Esencia Original
    success, msg = add_esencia_original(skill_md)
    if success:
        fixes_applied.append(msg)

    # Fix 3: Gotchas section
    success, msg = add_gotchas(skill_md)
    if success:
        fixes_applied.append(msg)

    # Fix 4: References folder
    success, msg = add_references_folder(skill_dir, skill_name)
    if success:
        fixes_applied.append(msg)

    # Fix 5: Scripts folder
    success, msg = add_scripts_folder(skill_dir)
    if success:
        fixes_applied.append(msg)

    return fixes_applied


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Fix missing skill components")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be fixed without making changes",
    )
    parser.add_argument(
        "--skill",
        type=str,
        help="Fix specific skill only (e.g., 16_Silicon_Valley_Data_Analyst)",
    )
    parser.add_argument(
        "path", nargs="?", type=str, default=None, help="Path to skills directory"
    )
    args = parser.parse_args()

    print("=" * 60)
    print("🔧 SKILL FIXER - SOTA v5.1")
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    if args.dry_run:
        print("🔍 DRY RUN MODE - No changes will be made")
    print("=" * 60)

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
        print(f"Usage: python fix-missing.py [--skill NAME] [path/to/skills]")
        return

    # Find skills to fix
    if args.skill:
        skill_path = skills_dir / args.skill
        if not skill_path.exists():
            # Try case-insensitive search
            for d in skills_dir.iterdir():
                if d.is_dir() and d.name.lower() == args.skill.lower():
                    skill_path = d
                    break

        if skill_path.exists() and skill_path.is_dir():
            skills = [skill_path]
        else:
            print(f"❌ Skill not found: {args.skill}")
            return
    else:
        skills = [
            d for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists()
        ]

    print(f"\n🔍 Checking {len(skills)} skills...\n")

    total_fixes = 0
    for skill_dir in sorted(skills):
        fixes = fix_skill(skill_dir, dry_run=args.dry_run)

        if fixes:
            print(f"📌 {skill_dir.name}:")
            for fix in fixes:
                print(f"   ✅ {fix}")
                total_fixes += 1
        else:
            print(f"✅ {skill_dir.name}: No fixes needed")

    print("\n" + "=" * 60)
    print(f"📊 SUMMARY: {total_fixes} fixes applied")
    if args.dry_run:
        print("🔍 This was a dry run - no changes made")
    print("=" * 60)


if __name__ == "__main__":
    main()
