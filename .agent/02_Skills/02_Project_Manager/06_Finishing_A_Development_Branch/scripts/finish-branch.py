#!/usr/bin/env python3
"""
Finish Branch Helper

Checks git status and suggests next steps for finishing a development branch.
"""

import subprocess
import sys


def run_git(cmd):
    """Run a git command and return output."""
    try:
        result = subprocess.run(
            ["git"] + cmd, capture_output=True, text=True, check=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr}"


def check_branch_status():
    """Check current branch status."""
    print("=" * 50)
    print("🌿 FINISH BRANCH HELPER")
    print("=" * 50)

    # Current branch
    branch = run_git(["branch", "--show-current"])
    print(f"\n📍 Current branch: {branch}")

    # Uncommitted changes
    status = run_git(["status", "--porcelain"])
    if status:
        print("\n⚠️  Uncommitted changes:")
        print(status)
    else:
        print("\n✅ Working tree clean")

    # Unpushed commits
    unpushed = run_git(
        [
            "log",
            "--oneline",
            f"origin/{branch}..HEAD" if branch != "master" else "HEAD",
            "-5",
        ]
    )
    if unpushed:
        print(f"\n📤 Unpushed commits:\n{unpushed}")

    # Suggest next steps
    print("\n" + "=" * 50)
    print("📋 NEXT STEPS")
    print("=" * 50)
    print("1. Run tests: pytest or npm test")
    print("2. Commit changes: git add . && git commit -m 'feat: ...'")
    print("3. Push branch: git push -u origin " + branch)
    print("4. Create PR or merge to master")


if __name__ == "__main__":
    check_branch_status()
