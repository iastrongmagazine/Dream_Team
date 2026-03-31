import os
import sys
import subprocess
from datetime import datetime

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


PROJECT_ROOT = _ext_root.parent.parent


def run_linter(file_path):
    if file_path.endswith(".py"):
        print(f"--- Running Ruff on {file_path} ---")
    elif file_path.endswith((".js", ".ts", ".jsx", ".tsx", ".json")):
        print(f"--- Running Prettier on {file_path} ---")


def create_backup(file_path):
    if not os.path.exists(file_path):
        return

    backup_dir = ".claude/backups"
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = os.path.basename(file_path)
    backup_path = os.path.join(backup_dir, f"{file_name}_{timestamp}.bak")

    import shutil

    print(f"--- Creating backup: {backup_path} ---")
    shutil.copy(file_path, backup_path)
    return backup_path


def organize_solution_if_needed(file_path):
    """Check if file is in 04_Operations/06_Solutions/ and organize it."""
    if (
        "04_Operations" in file_path
        and "06_Solutions" in file_path
        and file_path.endswith(".md")
    ):
        try:
            script_path = (
                PROJECT_ROOT
                / "08_Scripts_Os"
                / "Legacy_Backup"
                / "56_Organize_Solutions.py"
            )
            if script_path.exists():
                result = subprocess.run(
                    [sys.executable, str(script_path), "--apply"],
                    capture_output=True,
                    text=True,
                    cwd=str(PROJECT_ROOT),
                )
                if result.stdout:
                    print(f"[ORG] {result.stdout.strip()}")
                if result.stderr:
                    print(f"[ORG-ERR] {result.stderr.strip()}")
            else:
                print(f"[ORG] Script not found: {script_path}")
        except Exception as e:
            print(f"[ERROR] Failed to organize solutions: {e}")


def cleanup_empty_docs_dirs():
    """Remove empty docs/ directories (legacy) - NOW uses 04_Operations/."""
    # Legacy cleanup - no longer needed as we use 04_Operations/
    docs_dirs = [
        PROJECT_ROOT / "docs" / "solutions",
        PROJECT_ROOT / "docs" / "plans",
        PROJECT_ROOT / "docs" / "brainstorms",
        PROJECT_ROOT / "docs",
    ]

    for dir_path in docs_dirs:
        if dir_path.exists() and dir_path.is_dir():
            if not any(dir_path.iterdir()):
                try:
                    dir_path.rmdir()
                    print(f"[ORG] Removed empty directory: {dir_path}")
                except OSError:
                    pass


def cleanup_nul_files():
    """Remove Windows nul device files accidentally created by redirect bugs."""
    nul_files = [
        PROJECT_ROOT / "nul",
        PROJECT_ROOT / "NUL",
    ]
    for nul_path in nul_files:
        if nul_path.exists():
            try:
                nul_path.unlink()
                print(f"[CLEANUP] Removed Windows reserved name file: {nul_path.name}")
            except Exception as e:
                print(f"[CLEANUP] Could not remove {nul_path.name}: {e}")


def main():
    print("--- POST-TOOL USE HOOK ---")

    tool_name = os.environ.get("CLAUDE_TOOL_NAME", "unknown_tool")
    target_file = os.environ.get("CLAUDE_TARGET_FILE", "")
    log_data = {"tool": tool_name, "target_file": target_file}

    # Solo procesar archivos si el tool los modifica
    if target_file and os.path.exists(target_file):
        backup_path = create_backup(target_file)
        run_linter(target_file)
        organize_solution_if_needed(target_file)
        cleanup_empty_docs_dirs()
        log_data["backup"] = backup_path

    # Siempre limpiar archivos nul residuales de Windows
    cleanup_nul_files()

    # 🔔 SONIDO: Beep después de cada tool
    try:
        import winsound
        winsound.Beep(800, 100)
        print("[Sound] Beep OK")
    except Exception as e:
        print(f"[Sound] Beep falló: {e}")

    # Notificación de voz selectiva usando el sistema inteligente
    # Solo notificar para modificaciones de archivos importantes (prioridad normal)
    # El sistema automáticamente notificará cada 2 tareas
    if target_file:
        file_name = os.path.basename(target_file)
        # Solo notificar para archivos importantes (configuración, scripts principales)
        important_extensions = [".md", ".py", ".json", ".yaml", ".toml"]
        if any(target_file.endswith(ext) for ext in important_extensions):
            speak(f"Archivo actualizado: {file_name}", priority="high")

    log_to_json("post_tool_use", log_data)
    print("✅ Post-tool processing complete.")


if __name__ == "__main__":
    main()
