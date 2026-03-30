import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
import os
import re
import json
import subprocess
# Removed import engram_mem_save


def validate():
    # 1. Validate scripts in 04_Engine/
    engine_dir = "04_Engine"
    script_pattern = re.compile(r"^\d{2}_[a-zA-Z0-9_]+\.py$")
    all_ok = True

    print("[INFO] Validating scripts in 04_Engine/...")
    for filename in os.listdir(engine_dir):
        if filename == "60_Fast_Vision.py":
            continue
        # Excepciones: config_paths.py es backwards compatibility
        if filename == "config_paths.py":
            print(f"[OK] Script matches pattern: {filename} (backwards compatibility)")
            continue
        filepath = os.path.join(engine_dir, filename)
        if os.path.isfile(filepath) and filename.endswith(".py"):
            if not script_pattern.match(filename):
                print(f"[FAIL] Script does not match pattern: {filename}")
                all_ok = False
            else:
                print(f"[OK] Script matches pattern: {filename}")

    # 2. Verify 05_System/04_Env/Requirements.txt
    req_file = "05_System/04_Env/Requirements.txt"
    if os.path.exists(req_file):
        print(f"[OK] Requirements file exists: {req_file}")
    else:
        print(f"[FAIL] Requirements file missing: {req_file}")
        all_ok = False

    # 3. Scan mcp-config.json
    mcp_files = [
        "05_System/03_Integrations/granola/mcp-config.json",
        "05_System/03_Integrations/granola/mcp-config.json",
    ]

    for mcp_file in mcp_files:
        if os.path.exists(mcp_file):
            print(f"[INFO] Scanning {mcp_file}...")
            with open(mcp_file, "r") as f:
                try:
                    data = json.load(f)

                    # Simple scan for absolute paths starting with /
                    def check_paths(obj):
                        if isinstance(obj, str):
                            if obj.startswith("/"):
                                print(
                                    f"[WARN] Absolute path found in {mcp_file}: {obj}"
                                )
                        elif isinstance(obj, dict):
                            for v in obj.values():
                                check_paths(v)
                        elif isinstance(obj, list):
                            for v in obj:
                                check_paths(v)

                    check_paths(data)
                except Exception as e:
                    print(f"[FAIL] Error parsing {mcp_file}: {e}")
                    all_ok = False
        else:
            print(f"[FAIL] MCP config file not found: {mcp_file}")
            all_ok = False

    # 4. Invoke hook
    print("[INFO] Invoking Notify_System.py...")
    try:
        subprocess.run(
            ["python", "04_Engine/08_Scripts_Os/59_Notify_System.py"], check=True
        )
        print("[OK] Notify_System.py invoked successfully.")
    except Exception as e:
        print(f"[FAIL] Notify_System.py failed: {e}")
        all_ok = False

    if not all_ok:
        print("[FAIL] Issues detected. Check output.")
        exit(1)
    else:
        print("[OK] Fast Vision check passed.")
        exit(0)


if __name__ == "__main__":
    validate()
