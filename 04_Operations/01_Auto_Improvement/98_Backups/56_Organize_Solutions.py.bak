"""
56_Organize_Solutions.py - Armor Layer Protected
Organize Hulk Compound solutions to Knowledge structure.

Moves files from 04_Operations/06_Solutions/ to 02_Knowledge/ (archived solutions).
Renames files to format: NNN_Descripcion_DD_MM_YYYY.md

Usage:
    python 56_Organize_Solutions.py          # Dry run (show what would move)
    python 56_Organize_Solutions.py --apply  # Actually move files
"""

import os
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import PROJECT_ROOT, KNOWLEDGE_DIR, ARCHIVE_DIR

REQUIRED_DIRS = [
    "00_Core",
    "01_Brain",
    "02_Operations",
    "03_Knowledge",
    "04_Engine",
    "05_System",
    "06_Archive",
]
for d in REQUIRED_DIRS:
    if not (PROJECT_ROOT / d).exists():
        print(f"[WARN] Required directory not found: {d}")

SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = PROJECT_ROOT

SOURCE_DIR = PROJECT_ROOT / "docs" / "solutions"
DEST_BASE = PROJECT_ROOT / "03_Knowledge" / "01_Research_Knowledge" / "solutions"
BACKUP_DIR = PROJECT_ROOT / "06_Archive" / "01_Backups" / "solutions_organize"

CATEGORIES = [
    "logic-errors",
    "performance-issues",
    "security-issues",
    "database-issues",
    "ui-bugs",
    "build-errors",
    "test-failures",
    "runtime-errors",
    "integration-issues",
    "other",
]


def log(msg: str):
    print(f"[ORG] {msg}")


def error(msg: str):
    print(f"[ERROR] {msg}", file=sys.stderr)


def success(msg: str):
    print(f"[OK] {msg}")


def get_category_from_frontmatter(content: str, folder_name: str) -> str:
    """Extract category from frontmatter or use folder name."""
    category_match = re.search(r"category:\s*(\S+)", content)
    if category_match:
        return category_match.group(1)

    problem_type_match = re.search(r"problem_type:\s*(\S+)", content)
    if problem_type_match:
        pt = problem_type_match.group(1).lower()
        if "logic" in pt:
            return "logic-errors"
        if "performance" in pt:
            return "performance-issues"
        if "security" in pt:
            return "security-issues"
        if "database" in pt or "db" in pt:
            return "database-issues"
        if "ui" in pt or "interface" in pt:
            return "ui-bugs"
        if "build" in pt or "compile" in pt:
            return "build-errors"
        if "test" in pt:
            return "test-failures"
        if "runtime" in pt:
            return "runtime-errors"
        if "integration" in pt:
            return "integration-issues"

    if folder_name in CATEGORIES[:-1]:
        return folder_name

    return "other"


def get_title_from_frontmatter(content: str) -> str:
    """Extract title from frontmatter. Returns None if empty/null."""
    title_match = re.search(r"title:\s*[\"\']?([^\n\"\'\[]+)[\"\']?", content)
    if title_match:
        title = title_match.group(1).strip()
        if title and title.lower() not in ("null", "none", ""):
            return title
    return None  # Return None instead of "Untitled"


def get_date_from_frontmatter(content: str) -> str:
    """Extract date from frontmatter or return current date."""
    date_match = re.search(r"date:\s*(\d{4}-\d{2}-\d{2})", content)
    if date_match:
        date_str = date_match.group(1)
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d")
            return dt.strftime("%d_%m_%Y")
        except ValueError:
            pass
    return datetime.now().strftime("%d_%m_%Y")


def slugify(text: str) -> str:
    """Convert text to a safe filename description."""
    text = text.strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "_", text)
    text = text[:50]
    text = text.strip("_")
    return text if text else "Untitled"


def get_next_sequence_number(category: str) -> int:
    """Get next sequence number for a category."""
    dest_folder = DEST_BASE / category
    if not dest_folder.exists():
        return 1

    max_num = 0
    for f in dest_folder.glob("*.md"):
        match = re.match(r"(\d+)_", f.name)
        if match:
            num = int(match.group(1))
            if num > max_num:
                max_num = num
    return max_num + 1


def generate_new_filename(content: str, category: str) -> str | None:
    """Generate new filename in format: NNN_Descripcion_DD_MM_YYYY.md
    Returns None if title is empty/null (file should be deleted)."""
    title = get_title_from_frontmatter(content)
    date_str = get_date_from_frontmatter(content)
    seq_num = get_next_sequence_number(category)

    if title is None:
        return None  # Signal to delete this file

    description = slugify(title)
    new_name = f"{seq_num:03d}_{description}_{date_str}.md"
    return new_name


def update_internal_links(content: str, old_base: str, new_base: str) -> str:
    """Update relative links pointing to old location."""
    content = re.sub(
        rf"{re.escape(old_base)}/([^)\s\]]+)",
        f"{new_base}/\\1",
        content,
    )
    return content


def create_backup(source_dir: Path) -> Path | None:
    """Create timestamped backup of source directory."""
    if not source_dir.exists():
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = BACKUP_DIR / f"docs_solutions_{timestamp}"

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    log(f"Creating backup: {backup_path}")
    shutil.copytree(source_dir, backup_path)

    return backup_path


def cleanup_untitled_files() -> list:
    """Remove existing files with 'Untitled' in the name from destination."""
    if not DEST_BASE.exists():
        return []

    deleted = []
    for cat_folder in DEST_BASE.iterdir():
        if cat_folder.is_dir():
            for md_file in cat_folder.glob("*Untitled*.md"):
                try:
                    md_file.unlink()
                    log(
                        f"[DEL] Removed Untitled file: {md_file.relative_to(DEST_BASE)}"
                    )
                    deleted.append(str(md_file))
                except Exception as e:
                    error(f"Failed to delete {md_file}: {e}")
    return deleted


def organize_solutions(dry_run: bool = True) -> dict:
    """Organize solutions from 04_Operations/06_Solutions/ to Knowledge structure."""

    if not SOURCE_DIR.exists():
        error(f"Source directory not found: {SOURCE_DIR}")
        return {"status": "error", "moved": [], "skipped": []}

    dest_base = DEST_BASE
    dest_base.mkdir(parents=True, exist_ok=True)

    for cat in CATEGORIES:
        (dest_base / cat).mkdir(parents=True, exist_ok=True)

    files_to_move = []
    source_folders = []

    for folder in SOURCE_DIR.iterdir():
        if folder.is_dir():
            source_folders.append(folder.name)
            for md_file in folder.glob("*.md"):
                files_to_move.append((folder.name, md_file))

    if not files_to_move:
        log("No solution files found to organize.")
        return {"status": "success", "moved": [], "skipped": []}

    log(
        f"Found {len(files_to_move)} solution file(s) in {len(source_folders)} folder(s)"
    )

    moved = []
    skipped = []

    for folder_name, src_file in files_to_move:
        try:
            content = src_file.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                content = src_file.read_text(encoding="latin-1")
            except Exception as e:
                error(f"Cannot read {src_file}: {e}")
                skipped.append(str(src_file))
                continue

        category = get_category_from_frontmatter(content, folder_name)
        new_filename = generate_new_filename(content, category)

        # Handle null/empty title files - delete them
        if new_filename is None:
            if dry_run:
                log(f"  [DRY] Would DELETE: {src_file.name} (null/empty title)")
            else:
                src_file.unlink()
                log(f"  [DEL] Deleted: {src_file.name} (null/empty title)")
                moved.append(
                    {
                        "original": src_file.name,
                        "action": "deleted_null_title",
                        "reason": "title was empty or null",
                    }
                )
            continue

        dest_folder = dest_base / category
        dest_file = dest_folder / new_filename

        counter = 1
        while dest_file.exists():
            base = dest_file.stem.rsplit("_", 1)[0]
            dest_file = dest_folder / f"{base}_{counter}.md"
            counter += 1

        if dry_run:
            log(f"  [DRY] Would move: {src_file.name}")
            log(f"         From: 04_Operations/06_Solutions/{folder_name}/")
            log(f"         To:   03_Knowledge/.../solutions/{category}/{new_filename}")
        else:
            new_content = update_internal_links(
                content,
                old_base=f"04_Operations/06_Solutions/{folder_name}",
                new_base=f"03_Knowledge/01_Research_Knowledge/solutions/{category}",
            )

            dest_file.write_text(new_content, encoding="utf-8")
            log(f"  Moved: {src_file.name} -> solutions/{category}/{new_filename}")
            moved.append(
                {
                    "original": src_file.name,
                    "file": new_filename,
                    "from": f"04_Operations/06_Solutions/{folder_name}/",
                    "to": f"solutions/{category}/",
                }
            )

    if dry_run:
        log("Dry run complete. Use --apply to actually move files.")
        return {"status": "dry_run", "moved": moved, "skipped": skipped}
    else:
        backup = create_backup(SOURCE_DIR)

        # Eliminar archivos .md de subcarpetas originales después de mover
        if SOURCE_DIR.exists():
            for subfolder in SOURCE_DIR.iterdir():
                if subfolder.is_dir():
                    # Eliminar archivos .md de esta subcarpeta
                    for md_file in subfolder.glob("*.md"):
                        md_file.unlink()
                        log(f"Removed original file: {md_file.name}")

                    # Eliminar subcarpeta si está vacía
                    if not any(subfolder.iterdir()):
                        shutil.rmtree(subfolder)
                        log(f"Removed empty subfolder: {subfolder.name}")

            # Eliminar SOURCE_DIR si está vacío
            if SOURCE_DIR.exists() and not any(SOURCE_DIR.iterdir()):
                shutil.rmtree(SOURCE_DIR)
                log(f"Removed empty directory: 04_Operations/06_Solutions/")

        # Eliminar docs/ si está vacío
        docs_dir = PROJECT_ROOT / "docs"
        if docs_dir.exists() and not any(docs_dir.iterdir()):
            shutil.rmtree(docs_dir)
            log(f"Removed empty directory: docs/")

        if backup:
            log(f"Backup created: {backup}")

        success(f"Organized {len(moved)} file(s). {len(skipped)} skipped.")
        return {
            "status": "success",
            "moved": moved,
            "skipped": skipped,
            "backup": str(backup),
        }


if __name__ == "__main__":
    dry_run = True
    cleanup_only = False

    if len(sys.argv) > 1 and sys.argv[1] == "--apply":
        dry_run = False
        print("[!] Running with actual file move. Creating backup first.")
    elif len(sys.argv) > 1 and sys.argv[1] == "--cleanup-untitled":
        cleanup_only = True
        print("[*] Cleaning up Untitled files from destination...")

    if cleanup_only:
        deleted = cleanup_untitled_files()
        if deleted:
            print(f"\n[OK] Cleaned up {len(deleted)} Untitled file(s).")
        else:
            print("[*] No Untitled files found.")
    else:
        result = organize_solutions(dry_run=dry_run)

        # Also cleanup existing Untitled files after moving (only in apply mode)
        if not dry_run and result.get("status") == "success":
            print("\n[*] Cleaning up existing Untitled files...")
            deleted = cleanup_untitled_files()
            if deleted:
                print(f"[OK] Removed {len(deleted)} existing Untitled file(s).")

        if dry_run and result["status"] != "error":
            print("\n[*] To apply changes, run:")
            print("   python 56_Organize_Solutions.py --apply")
