# -*- coding: utf-8 -*-
"""
cleanup_tabs.py - Cierra pestañas abiertas en VS Code
"""

# Fix Windows console encoding
import sys

if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

import subprocess


def cleanup_vscode_tabs():
    """
    Intenta cerrar todas las pestañas abiertas en VS Code mediante comandos de sistema.
    """
    print("Iniciando limpieza de pestañas de VS Code...")

    # Comando de PowerShell para enviar teclas
    ps_command = """
    $wshell = New-Object -ComObject WScript.Shell;
    if ($wshell.AppActivate('Code')) {
        Start-Sleep -Milliseconds 500;
        $wshell.SendKeys('^k');
        Start-Sleep -Milliseconds 100;
        $wshell.SendKeys('^w');
        echo 'Comando enviado con exito.';
    } else {
        echo 'No se pudo activar VS Code.';
    }
    """

    try:
        result = subprocess.run(
            ["powershell", "-Command", ps_command],
            capture_output=True,
            text=True,
            check=False,
        )
        if result.stdout:
            print(result.stdout.strip())

        if "exito" in result.stdout:
            print("[OK] Pestañas cerradas")
        else:
            print("[FAIL] No se encontro VS Code abierto")
    except (subprocess.SubprocessError, OSError) as e:
        print(f"[ERROR] {e}")


if __name__ == "__main__":
    cleanup_vscode_tabs()
