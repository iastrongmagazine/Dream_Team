import csv
import sys
import os

# Forzar encoding UTF-8 para consola Windows
if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


def find_latest_csv(root_dir):
    latest_file = None
    latest_time = 0
    for root, _, files in os.walk(root_dir):
        if ".git" in root or ".agent" in root or "Knowledge" in root:
            continue
        for file in files:
            if file.endswith(".csv"):
                path = os.path.join(root, file)
                mtime = os.path.getmtime(path)
                if mtime > latest_time:
                    latest_time = mtime
                    latest_file = path
    return latest_file


def validate_csv(file_path):
    if not file_path or not os.path.exists(file_path):
        print(f"Error: Target CSV not found or invalid: {file_path}")
        sys.exit(1)

    try:
        with open(file_path, mode="r", encoding="utf-8") as f:
            sample = f.read(2048)
            f.seek(0)

            if not sample.strip():
                print(f"⚠️ Warning: File {file_path} is empty.")
                return

            try:
                dialect = csv.Sniffer().sniff(sample)
                f.seek(0)
                reader = csv.reader(f, dialect)
            except:
                f.seek(0)
                reader = csv.reader(f)  # Fallback to standard comma

            rows = list(reader)
            if not rows:
                return

            col_count = len(rows[0])
            for i, row in enumerate(rows):
                # Only check rows that aren't completely empty
                if any(field.strip() for field in row):
                    if len(row) != col_count:
                        print(
                            f"❌ CSV Error in {file_path} (Line {i + 1}): Expected {col_count} columns, found {len(row)}"
                        )
                        sys.exit(1)

        print(f"✅ CSV Hook: Structure validated for {file_path}")
    except Exception as e:
        print(f"❌ CSV Hook Error: Failed to validate {file_path}\n{e}")
        sys.exit(1)


if __name__ == "__main__":
    # Get target file from CLAUDE_TARGET_FILE environment (hook context)
    # or from command line argument
    target = os.environ.get("CLAUDE_TARGET_FILE", "")

    # Only validate if it's a CSV file
    if target and target.endswith(".csv"):
        validate_csv(target)
    elif not target:
        # Fallback: find latest CSV in project
        latest = find_latest_csv(".")
        if latest:
            validate_csv(latest)
        else:
            print("CSV Validator: No CSV files found to validate.")
    else:
        # Target exists but not a CSV - skip silently
        pass
