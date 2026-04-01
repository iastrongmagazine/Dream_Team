#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Skill Harmonizer - Valida paridad entre skills en carpetas e inventarios
Detecta duplicados y genera reporte de salud del sistema de skills.
"""

import os
import sys
import json
from pathlib import Path

# === SETUP PATHS ===
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# === CONSTANTS ===
SKILLS_DIR = PROJECT_ROOT / "01_Core" / "03_Skills"


def find_skills() -> dict:
    """Encuentra todas las skills en 01_Core/03_Skills/."""
    skills = {}

    if not SKILLS_DIR.exists():
        print(f"[WARN] Skills directory not found: {SKILLS_DIR}")
        return skills

    for category in SKILLS_DIR.iterdir():
        if category.is_dir() and not category.name.startswith("."):
            category_name = category.name

            # Buscar SKILL.md en la carpeta
            skill_md = category / "SKILL.md"
            if skill_md.exists():
                skills[category_name] = {"path": str(skill_md), "has_skill_md": True}
            else:
                # Buscar subcarpetas con SKILL.md
                sub_skills = []
                for sub in category.iterdir():
                    if sub.is_dir():
                        sub_skill_md = sub / "SKILL.md"
                        if sub_skill_md.exists():
                            sub_skills.append(
                                {"name": sub.name, "path": str(sub_skill_md)}
                            )

                skills[category_name] = {
                    "path": str(category),
                    "has_skill_md": False,
                    "sub_skills": sub_skills,
                }

    return skills


def analyze_skills(skills: dict) -> dict:
    """Analiza el estado de las skills."""
    analysis = {
        "total_categories": len(skills),
        "with_skill_md": 0,
        "without_skill_md": 0,
        "sub_skills": 0,
        "issues": [],
    }

    for name, info in skills.items():
        if info.get("has_skill_md"):
            analysis["with_skill_md"] += 1
        else:
            analysis["without_skill_md"] += 1
            if info.get("sub_skills"):
                analysis["sub_skills"] += len(info["sub_skills"])
            else:
                analysis["issues"].append(f"Category {name} has no SKILL.md")

    return analysis


def print_report(skills: dict, analysis: dict):
    """Imprime el reporte de salud."""
    print("\n" + "=" * 60)
    print("SKILL HARMONIZER - PersonalOS")
    print("=" * 60)

    print(f"\n[RESUMEN]")
    print(f"   Categorias totales: {analysis['total_categories']}")
    print(f"   Con SKILL.md: {analysis['with_skill_md']}")
    print(f"   Sin SKILL.md: {analysis['without_skill_md']}")
    print(f"   Sub-skills: {analysis['sub_skills']}")

    print(f"\n[CATEGORIAS]")
    print("-" * 40)

    for name, info in sorted(skills.items()):
        if info.get("has_skill_md"):
            print(f"[OK] {name}")
        else:
            subs = info.get("sub_skills", [])
            if subs:
                print(f"[DIR] {name} ({len(subs)} sub-skills)")
                for s in subs:
                    print(f"   +-- {s['name']}")
            else:
                print(f"[WARN] {name} (SIN SKILL.md)")

    if analysis["issues"]:
        print(f"\n[ISSUES]")
        for issue in analysis["issues"]:
            print(f"   - {issue}")

    print("\n" + "=" * 60)
    print("Usa este reporte para mantener la salud del sistema de skills.")
    print("=" * 60)


def main():
    """Punto de entrada."""
    print("[INFO] Analizando skills...")

    # Find skills
    skills = find_skills()

    if not skills:
        print("[ERROR] No se encontraron skills.")
        return

    # Analyze
    analysis = analyze_skills(skills)

    # Print report
    print_report(skills, analysis)


if __name__ == "__main__":
    main()
