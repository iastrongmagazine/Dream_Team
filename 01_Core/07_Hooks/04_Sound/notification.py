import os
import sys
import argparse

# Forzar encoding UTF-8 para consola Windows
if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from pathlib import Path
import sys

_ext_root = Path(__file__).parent.parent.parent

_speak = None
_visual_alert = None
_log_to_json = None

try:
    import importlib.util

    _common_path = _ext_root / "02_Utils" / "common.py"
    if _common_path.exists():
        _spec = importlib.util.spec_from_file_location("_common", _common_path)
        _common = importlib.util.module_from_spec(_spec)
        _spec.loader.exec_module(_common)
        _speak = _common.speak
        _visual_alert = _common.visual_alert
        _log_to_json = _common.log_to_json
except Exception:
    pass


def speak(msg, priority="normal"):
    if _speak:
        _speak(msg, priority)
    else:
        print(msg)


def visual_alert(msg):
    if _visual_alert:
        _visual_alert(msg)
    else:
        print(f"[ALERT] {msg}")


def log_to_json(event, data):
    if _log_to_json:
        _log_to_json(event, data)
    else:
        print(f"[LOG] {event}: {data}")


def main():
    parser = argparse.ArgumentParser(description="Claude Code Notification Hook")
    parser.add_argument(
        "--notify", action="store_true", help="Send general notification"
    )
    args = parser.parse_args()

    message = os.environ.get("CLAUDE_NOTIFICATION", "Claude requiere tu atención")

    if args.notify:
        print(f"Enviando notificación: {message}")
        visual_alert(message)
        speak(message, priority="high")  # Explicit notifications are high priority

        # Log to JSON
        log_to_json("notification", {"message": message, "status": "sent"})


if __name__ == "__main__":
    main()
