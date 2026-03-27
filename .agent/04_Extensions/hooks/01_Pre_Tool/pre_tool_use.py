import os
import sys
import subprocess

# Forzar encoding UTF-8 para consola Windows
if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

from pathlib import Path

_ext_root = Path(__file__).parent.parent.parent

_speak = None
_log_to_json = None

try:
    import importlib.util

    _common_path = _ext_root / "02_Utils" / "common.py"
    if _common_path.exists():
        _spec = importlib.util.spec_from_file_location("_common", _common_path)
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


def check_battery():
    try:
        ps_command = "Get-WmiObject -Class Win32_Battery | Select-Object -ExpandProperty EstimatedChargeRemaining"
        result = subprocess.run(
            ["powershell.exe", "-Command", ps_command], capture_output=True, text=True
        )
        if result.stdout.strip():
            battery_level = int(result.stdout.strip())
            if battery_level < 15:
                print(f"⚠️ Batería baja: {battery_level}%")
                return False, battery_level
    except:
        pass
    return True, 100


def main():
    print("--- PRE-TOOL USE HOOK ---")

    # Check battery
    if os.environ.get("BYPASS_BATTERY_CHECK") != "1":
        bat_ok, level = check_battery()
        if not bat_ok:
            error_msg = f"Operacion cancelada por bateria baja: {level}%."
            print(f"[ERR] {error_msg}")
            # Importación local para evitar dependencias circulares pesadas
            speak(error_msg)
            log_to_json(
                "pre_tool_use",
                {"action": "cancel", "reason": "low_battery", "level": level},
            )
            sys.exit(1)

    # Get tool input from environment
    tool_input = os.environ.get("CLAUDE_TOOL_INPUT", "").lower()

    # 1. Block destructive commands
    if "rm -rf" in tool_input:
        error_msg = "Comando destructivo 'rm -rf' bloqueado."
        print(f"❌ ERROR: {error_msg}")
        log_to_json(
            "pre_tool_use",
            {"action": "block", "command": tool_input, "reason": "destructive"},
        )
        sys.exit(1)

    # 2. Protect .env files
    if ".env" in tool_input and "cat" in tool_input:
        error_msg = "Acceso a archivos .env bloqueado."
        print(f"❌ ERROR: {error_msg}")
        log_to_json(
            "pre_tool_use",
            {"action": "block", "command": tool_input, "reason": "security_file"},
        )
        sys.exit(1)

    log_to_json("pre_tool_use", {"action": "allow", "command": tool_input})
    print("✅ Pre-tool check exitoso.")


if __name__ == "__main__":
    main()
