import re
import json
from pathlib import Path
import sys

# Configuración
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
BACKUP_DIR = PROJECT_ROOT / "04_Operations" / "09_Backups" / "repair_backup_2026-03-21"
REPAIR_MAP_PATH = PROJECT_ROOT / "04_Operations" / "00_Config" / "repair_map.json"


def load_repair_map():
    if not REPAIR_MAP_PATH.exists():
        return {}
    with open(REPAIR_MAP_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def run_apply():
    print("--- MODO APPLY: Aplicando reparación robusta ---")

    # Cargar el mapa corregido del Agente-2
    # El mapa ahora es un objeto con path_normalization y malformed_links
    repair_map = {
        "path_normalization": "C:\\Users\\sebas\\Downloads\\01 Revisar\\11_Personal_Os\\Think_Different_AI-main\\Think_Different_AI-main\\",
        "malformed_links": {
            "/invalid": "",
            "/missing}": "",
            "/broken-hook-change": "/hooks/pre_tool_use.py",
            "/estilo]": "/estilo",
        },
    }

    path_norm = repair_map["path_normalization"]
    malformed = repair_map["malformed_links"]

    # Recorrer archivos .md
    for md_file in PROJECT_ROOT.rglob("*.md"):
        if any(
            excluded in str(md_file)
            for excluded in [".git", ".agent", ".cursor", "06_Archive"]
        ):
            continue

        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = content

        # 1. Normalizar rutas absolutas a relativas
        new_content = new_content.replace(path_norm, "./")

        # 2. Reparar links malformados
        for broken, fixed in malformed.items():
            if broken in new_content:
                print(
                    f"Reparado: {md_file.name} -> Reemplazar '{broken}' por '{fixed}'"
                )
                new_content = new_content.replace(broken, fixed)

        if new_content != content:
            with open(md_file, "w", encoding="utf-8") as f:
                f.write(new_content)
                print(f"✅ Archivo actualizado: {md_file.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    run_apply()


if __name__ == "__main__":
    run_apply()
