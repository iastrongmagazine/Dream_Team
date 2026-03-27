import os
import re
from pathlib import Path
from datetime import datetime


def extract_name_from_skills_md(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"^---\nname:\s*(.+?)\n", content, re.MULTILINE)
    return match.group(1).strip() if match else None


def get_file_mtime(filepath):
    t = os.path.getmtime(filepath)
    return datetime.fromtimestamp(t)


def format_date(dt):
    return dt.strftime("%Y-%m-%d %H:%M")


def scan_skill_folder(base_path):
    skills = {}
    pattern = os.path.join(base_path, "**", "SKILL.md")
    for filepath in Path(".").glob(pattern):
        relative_path = str(filepath)
        name = extract_name_from_skills_md(filepath)
        if name:
            mtime = get_file_mtime(filepath)
            skills[name] = {"path": relative_path, "mtime": mtime}
    return skills


def main():
    root = Path(".")
    gentleman_path = root / ".agent" / "02_Skills" / "05_Gentleman"
    every_path = root / ".agent" / "02_Skills" / "07_Every"

    os.chdir(root)

    gentleman_skills = {}
    if gentleman_path.exists():
        for filepath in gentleman_path.rglob("SKILL.md"):
            name = extract_name_from_skills_md(filepath)
            if name:
                gentleman_skills[name] = {
                    "path": str(filepath),
                    "mtime": get_file_mtime(filepath),
                }

    every_skills = {}
    if every_path.exists():
        for filepath in every_path.rglob("SKILL.md"):
            name = extract_name_from_skills_md(filepath)
            if name:
                every_skills[name] = {
                    "path": str(filepath),
                    "mtime": get_file_mtime(filepath),
                }

    all_names = set(gentleman_skills.keys()) | set(every_skills.keys())
    duplicates = []

    for name in sorted(all_names):
        in_gentleman = name in gentleman_skills
        in_every = name in every_skills

        if in_gentleman and in_every:
            gm = gentleman_skills[name]["mtime"]
            em = every_skills[name]["mtime"]

            if em > gm:
                winner = "07_Every"
            else:
                winner = "05_Gentleman"

            duplicates.append(
                {
                    "name": name,
                    "gentleman_date": format_date(gm),
                    "every_date": format_date(em),
                    "winner": winner,
                }
            )

    print("=== DUPLICATE SKILLS REPORT ===")
    print()
    print("| Name | 05_Gentleman | 07_Every | Winner |")
    print("|------|--------------|----------|--------|")
    for d in duplicates:
        print(
            f"| {d['name']} | {d['gentleman_date']} | {d['every_date']} | {d['winner']} |"
        )
    print()
    print("=== DUPLICATES COUNT ===")
    print(f"Total: {len(duplicates)}")


if __name__ == "__main__":
    main()
