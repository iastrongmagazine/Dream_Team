import sys
import re
import os

# Assuming the file is in 04_Engine, we might need to adjust imports if
# we need to import config_paths directly if it's not in the same dir.
# It is in the same dir, so we can import it.
try:
    from config_paths import ROOT_DIR
except ImportError:
    # Fallback if running from a different context
    ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))


def validate_commit_message(message):
    """
    Validates the commit message against Conventional Commits.
    Pattern: <type>(<scope>): <subject>
    Types: feat, fix, docs, style, refactor, perf, test, chore, build, ci
    """
    pattern = (
        r"^(feat|fix|docs|style|refactor|perf|test|chore|build|ci)(?:\(.+\))?: .{1,50}$"
    )
    if re.match(pattern, message.strip()):
        return True
    return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python 51_Commit_Lint_Guard.py <commit-msg-file>")
        sys.exit(1)

    commit_msg_file = sys.argv[1]

    if not os.path.exists(commit_msg_file):
        print(f"Error: Commit message file {commit_msg_file} not found.")
        sys.exit(1)

    with open(commit_msg_file, "r", encoding="utf-8") as f:
        commit_message = f.read()

    if validate_commit_message(commit_message):
        print("Commit message is valid.")
        sys.exit(0)
    else:
        print("Error: Commit message does not follow Conventional Commits format.")
        print("Expected format: <type>(<scope>): <subject>")
        print(
            "Allowed types: feat, fix, docs, style, refactor, perf, test, chore, build, ci"
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
