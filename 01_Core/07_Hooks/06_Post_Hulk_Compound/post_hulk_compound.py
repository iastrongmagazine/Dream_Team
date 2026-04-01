import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path

if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

_ext_root = Path(__file__).parent.parent.parent

_speak = None
_log_to_json = None

try:
    import importlib.util

    _common_path = _ext_root / "02_Utils" / "common.py"
    if _common_path.exists():
        _spec = importlib.util.spec_from_file_location("_common", _common_path)
        if _spec and _spec.loader:
            _common = importlib.util.module_from_spec(_spec)
            _spec.loader.exec_module(_common)
            _speak = _common.speak
            _log_to_json = _common.log_to_json
except Exception:
    pass


def speak(msg, priority="normal"):
    if _speak:
        _speak(msg, priority)
    else:
        print(msg)


def log_to_json(event, data):
    if _log_to_json:
        _log_to_json(event, data)
    else:
        print(f"[LOG] {event}: {data}")


def main():
    print("--- POST-HULK-COMPOUND HOOK ---")

    project_root = _ext_root.parent.parent
    script_dir = project_root / "04_Operations" / "08_Scripts_Os"
    organize_script = script_dir / "56_Organize_Solutions.py"

    if not organize_script.exists():
        print("[!] 56_Organize_Solutions.py not found. Skipping.")
        return

    print("[*] Running solution organizer...")

    try:
        result = subprocess.run(
            [sys.executable, str(organize_script), "--apply"],
            cwd=str(project_root),
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )

        if result.returncode == 0:
            print("[+] Solution organization completed successfully.")
            speak("Solutions organizados correctamente", priority="low")
        else:
            print(f"[!] Organizer returned code: {result.returncode}")
            if result.stderr:
                print(f"    stderr: {result.stderr[:200]}")

    except Exception as e:
        print(f"[ERROR] Failed to run organizer: {e}")

    log_to_json("post_hulk_compound", {"status": "completed"})
    print("--- POST-HULK-COMPOUND DONE ---")


if __name__ == "__main__":
    main()
