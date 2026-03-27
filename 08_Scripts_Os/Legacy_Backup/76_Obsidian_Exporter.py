#!/usr/bin/env python3
import datetime
import os
import json


def get_obsidian_path():
    """Obtiene la ruta del vault desde config.json"""
    # Buscar config.json en varias ubicaciones
    possible_paths = [
        os.path.join(os.path.dirname(__file__), "..", "07_Installer", "config.json"),
        os.path.join(
            os.path.dirname(__file__), "..", "..", "05_System", "04_Env", "config.json"
        ),
    ]

    for config_path in possible_paths:
        if os.path.exists(config_path):
            try:
                with open(config_path, "r") as f:
                    config = json.load(f)
                    vault_path = config.get("paths", {}).get("obsidian_vault", "")
                    if vault_path and os.path.exists(vault_path):
                        return vault_path
            except:
                pass

    return None


def export_to_obsidian(content):
    """Escribe el reporte directamente en el Vault de Obsidian."""
    vault_path = get_obsidian_path()

    if not vault_path:
        # Fallback a variable de entorno o valor por defecto
        vault_path = os.getenv("OBSIDIAN_VAULT", "")

    if not vault_path or not os.path.exists(vault_path):
        print(
            f"[WARN] Vault de Obsidian no configurado. Configura en 07_Installer/config.json"
        )
        return False
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    note_path = os.path.join(vault_path, f"Daily_Summary_{date_str}.md")

    try:
        # Si el archivo no existe, lo crea. Si existe, hace append.
        with open(note_path, "a", encoding="utf-8") as f:
            f.write(
                f"\n\n## Reporte de Cierre: {datetime.datetime.now().strftime('%H:%M:%S')}\n\n"
            )
            f.write(content)
        print(f"[OK] Sincronizado en Obsidian: {note_path}")
        return True
    except Exception as e:
        print(f"[ERR] Fallo al escribir en Obsidian: {e}")
        return False


if __name__ == "__main__":
    report_path = "02_Operations/03_Progress/2026-03-15_Resumen_Operativo.md"
    if os.path.exists(report_path):
        with open(report_path, "r", encoding="utf-8") as f:
            content = f.read()
        export_to_obsidian(content)
    else:
        print("[ERR] Reporte de hoy no encontrado.")
