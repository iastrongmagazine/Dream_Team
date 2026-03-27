#!/usr/bin/env python3
"""
55_Sync_Skills.py - Armor Layer Protected
Sync .agent/02_Skills/ → .cursor/02_Skills/

Unidirectional sync: .agent/ is the Source of Truth.
.cursor/ is a mirror that gets updated from .agent/.

Usage:
    python 55_Sync_Skills.py          # Dry run (show what would sync)
    python 55_Sync_Skills.py --apply  # Actually sync
"""

import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import PROJECT_ROOT, ARCHIVE_DIR

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

AGENT_SKILLS = PROJECT_ROOT / ".agent" / "02_Skills"
CURSOR_SKILLS = PROJECT_ROOT / ".cursor" / "02_Skills"

BACKUP_DIR = PROJECT_ROOT / "06_Archive" / "01_Backups" / "skills_sync"

EXCLUDE_FROM_SYNC = {
    ".cursor/00_Rules",
    ".cursor/06_History",
}

# ─────────────────────────────────────────────────────────────────────────────
# HELPERS
# ─────────────────────────────────────────────────────────────────────────────


def log(msg: str):
    print(f"[SYNC] {msg}")


def error(msg: str):
    print(f"[ERROR] {msg}", file=sys.stderr)


def success(msg: str):
    print(f"[OK] {msg}")


def get_all_items(base_path: Path) -> set:
    """Return all files/dirs relative to base_path."""
    if not base_path.exists():
        return set()

    items = set()
    for item in base_path.rglob("*"):
        rel = item.relative_to(base_path)
        items.add(str(rel))
    return items


def copy_tree(src: Path, dst: Path):
    """Copy entire directory tree."""
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def create_backup(cursor_skills: Path) -> Path | None:
    """Create timestamped backup of .cursor/02_Skills/."""
    if not cursor_skills.exists():
        return None

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = BACKUP_DIR / f"cursor_02_Skills_{timestamp}"

    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    log(f"Creating backup: {backup_path}")
    shutil.copytree(cursor_skills, backup_path)

    return backup_path


def sync_skills(dry_run: bool = True) -> dict:
    """Sync skills from .agent/ to .cursor/."""

    # ── Step 1: Check existence ──
    if not AGENT_SKILLS.exists():
        error(f"Source not found: {AGENT_SKILLS}")
        return {"status": "error", "changes": []}

    if not CURSOR_SKILLS.exists():
        log(f"Target not found, will create: {CURSOR_SKILLS}")
        if not dry_run:
            CURSOR_SKILLS.mkdir(parents=True, exist_ok=True)

    # ── Step 2: Detect changes ──
    agent_items = get_all_items(AGENT_SKILLS)
    cursor_items = get_all_items(CURSOR_SKILLS) if CURSOR_SKILLS.exists() else set()

    to_add = agent_items - cursor_items
    to_remove = cursor_items - agent_items
    unchanged = agent_items & cursor_items

    changes = {
        "add": sorted(to_add),
        "remove": sorted(to_remove),
        "unchanged": len(unchanged),
    }

    # ── Step 3: Report ──
    log(f"Source: {AGENT_SKILLS}")
    log(f"Target: {CURSOR_SKILLS}")
    log(f"Items in source: {len(agent_items)}")
    log(f"Items in target: {len(cursor_items)}")
    log(f"Changes to apply:")
    log(f"  - Add: {len(to_add)} items")
    log(f"  - Remove: {len(to_remove)} items")
    log(f"  - Unchanged: {len(unchanged)} items")

    if to_add:
        print("\n[+] Files to ADD:")
        for item in list(to_add)[:10]:
            print(f"   + {item}")
        if len(to_add) > 10:
            print(f"   ... and {len(to_add) - 10} more")

    if to_remove:
        print("\n[-] Files to REMOVE from .cursor/:")
        for item in list(to_remove)[:10]:
            print(f"   - {item}")
        if len(to_remove) > 10:
            print(f"   ... and {len(to_remove) - 10} more")

    # ── Step 4: Apply if not dry run ──
    if not dry_run:
        # Backup first
        backup = create_backup(CURSOR_SKILLS)

        # Remove items that shouldn't exist
        for item in to_remove:
            item_path = CURSOR_SKILLS / item
            if item_path.exists():
                if item_path.is_dir():
                    shutil.rmtree(item_path)
                else:
                    item_path.unlink()
                log(f"Removed: {item}")

        # Copy new/updated items
        for item in to_add:
            src = AGENT_SKILLS / item
            dst = CURSOR_SKILLS / item

            if src.is_dir():
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
            log(f"Added: {item}")

        success("Sync completed!")
        if backup:
            log(f"Backup created: {backup}")

        return {"status": "success", "changes": changes, "backup": str(backup)}

    else:
        log("Dry run complete. Use --confirm to actually sync.")
        return {"status": "dry_run", "changes": changes}


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    dry_run = True
    if len(sys.argv) > 1 and sys.argv[1] == "--apply":
        dry_run = False
        print("[!] Running with actual sync. Creating backup first.")
    else:
        print("[*] Running in DRY RUN mode. Use --apply to actually sync.")

    result = sync_skills(dry_run=dry_run)

    if dry_run and result["status"] != "error":
        print("\n[*] To apply changes, run:")
        print("   python sync_skills.py --apply")
