"""
Módulo de limpieza de pestañas para VS Code.
Proporciona automatización para cerrar editores y limpiar la interfaz.
"""

import subprocess


def cleanup_vscode_tabs():
    """
    Intenta cerrar todas las pestañas abiertas en VS Code mediante comandos de sistema.
    """
    print("🚀 Iniciando limpieza de pestañas de VS Code (Python Edition)...")

    # Comando de PowerShell para enviar teclas
    ps_command = """
    $wshell = New-Object -ComObject WScript.Shell;
    if ($wshell.AppActivate('Code')) {
        Start-Sleep -Milliseconds 500;
        $wshell.SendKeys('^k');
        Start-Sleep -Milliseconds 100;
        $wshell.SendKeys('^w');
        echo 'Comando enviado con éxito.';
    } else {
        echo 'No se pudo activar VS Code.';
    }
    """

    try:
        result = subprocess.run(
            ["powershell", "-Command", ps_command],
            capture_output=True,
            text=True,
            check=False
        )
        if result.stdout:
            print(result.stdout.strip())

        if "éxito" in result.stdout:
            print("✅ Pestañas cerradas. Los archivos fantasma deberían desaparecer.")
        else:
            print("❌ No se encontró VS Code abierto o no se pudo activar.")
    except (subprocess.SubprocessError, OSError) as e:
        print(f"⚠️ Error al ejecutar el script de limpieza: {e}")


if __name__ == "__main__":
    cleanup_vscode_tabs()
