# -*- coding: utf-8 -*-
"""
Stop Hook - System Guardian Integration
Al cerrar sesión, detecta cambios y ejecuta System Guardian.
"""

import os
import sys
import argparse
import subprocess
from pathlib import Path

# Forzar encoding UTF-8 para consola Windows
if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# Importar utilities con fallback
_ext_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(_ext_root))

_speak = None
_visual_alert = None
_log_to_json = None

try:
    # Usar importlib para evitar syntax error con nombre numerico
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


def log_to_json(event, data):
    if _log_to_json:
        _log_to_json(event, data)


def run_guardian_if_needed():
    """Check for changes and run System Guardian if needed."""

    # Detectar si hay cambios unstaged
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"], capture_output=True, text=True, timeout=10
        )
        has_changes = bool(result.stdout.strip())
    except Exception:
        has_changes = False

    if has_changes:
        print("\n" + "=" * 50)
        print("  SYSTEM GUARDIAN - Post-Session Check")
        print("=" * 50)
        print("Cambios detectados - Ejecutando validacion...\n")

        # Buscar script guardian
        project_root = _ext_root.parent.parent
        guardian_path = (
            project_root / "04_Engine" / "08_Scripts_Os" / "79_System_Guardian.py"
        )
        if guardian_path.exists():
            try:
                # Correr guardian y capturar output
                result_check = subprocess.run(
                    [sys.executable, str(guardian_path)],
                    capture_output=True,
                    text=True,
                    timeout=120,
                )
                print(result_check.stdout)

                if result_check.stderr:
                    print(result_check.stderr, file=sys.stderr)

                # Verificar si hay issues
                output = result_check.stdout + result_check.stderr

                if "FAIL" in output or "WARN" in output:
                    print("\n[GUARDIAN] Issues detectados!")
                    visual_alert("issues_detectados")
                    try:
                        import winsound

                        winsound.Beep(1000, 500)
                    except Exception:
                        pass  # Linux/macOS
                    print(
                        "\nRevisa el reporte: 04_Engine/12_Validation/04_Config_Audit/guardian_latest.md"
                    )
                else:
                    print("\n[GUARDIAN] Todo OK - Sin issues")

            except subprocess.TimeoutExpired:
                print("[GUARDIAN] Timeout - Skip")
            except Exception as e:
                print(f"[GUARDIAN] Error: {e}")
        else:
            print("[GUARDIAN] Script no encontrado: 79_System_Guardian.py")

        print("=" * 50 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Claude Code Stop Hook")
    parser.add_argument("--chat", action="store_true", help="Stop chat hook")
    parser.add_argument(
        "--guardian", action="store_true", help="Run System Guardian check"
    )
    parser.add_argument(
        "--quiet", action="store_true", help="Run quietly (no voice output)"
    )
    args = parser.parse_args()

    print("--- STOP HOOK ---")

    msg = "Sesion finalizada. Todos los procesos se han detenido correctamente."
    print(msg)

    # Notificacion de voz al finalizar (skip if quiet mode)
    if not args.quiet:
        speak(msg, priority="high")

    # Log to JSON
    log_to_json("stop", {"event": "stop", "chat": args.chat})

    # Run guardian solo si se pide explicitamente (no por defecto para evitar bloqueos)
    if args.guardian:
        run_guardian_if_needed()


if __name__ == "__main__":
    main()
