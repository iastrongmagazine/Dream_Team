#!/usr/bin/env python3
"""
AUDITORÍA DE RUTAS DE SKILLS - DRY RUN
=====================================
Refactorizar: .agent/02_Skills/ -> 01_Core/03_Skills/

Objetivo: Identificar TODAS las referencias que romperían al migrar.
NO modifica archivos - solo lista lo que cambiaría.

Usage: python audit_skills_routes.py [--execute]
"""

import os
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(
    r"C:\Users\sebas\Downloads\01 Revisar\09 Versiones\00 Respaldo PC Sebas\01 Github\personal-os\Think_Different"
)

OLD_PATH = ".agent/02_Skills/"
NEW_PATH = "01_Core/03_Skills/"

EXTENSIONS = {".md", ".py", ".yaml", ".yml", ".json", ".txt", ".sh", ".bash", ".zsh"}


def find_references():
    """Encuentra todas las referencias a .agent/02_Skills/"""
    refs = defaultdict(list)

    for ext in EXTENSIONS:
        for f in ROOT.rglob(f"*{ext}"):
            if ".git" in str(f) or "node_modules" in str(f):
                continue
            if OLD_PATH in str(f):
                continue

            try:
                content = f.read_text(encoding="utf-8", errors="ignore")
                lines = content.split("\n")
                for i, line in enumerate(lines, 1):
                    if OLD_PATH in line and ".agent/02_Skills/" not in line.replace(
                        OLD_PATH, ""
                    ):
                        continue
                    if OLD_PATH in line:
                        refs[str(f.relative_to(ROOT))].append((i, line.strip()[:100]))
            except Exception:
                pass

    return refs


def analyze_impact():
    """Analiza el impacto de la migración"""
    refs = find_references()

    print("=" * 80)
    print("AUDITORÍA DE RUTAS DE SKILLS - DRY RUN")
    print("=" * 80)
    print(f"\nRuta Antigua: {OLD_PATH}")
    print(f"Ruta Nueva:   {NEW_PATH}")
    print(f"\nTotal archivos con referencias: {len(refs)}")

    by_category = defaultdict(int)
    for file in refs:
        ext = Path(file).suffix
        by_category[ext] += 1

    print("\n--- Referencias por tipo de archivo ---")
    for ext, count in sorted(by_category.items(), key=lambda x: -x[1]):
        print(f"  {ext}: {count}")

    print("\n--- Archivos afectados (primeros 30) ---")
    for i, (file, lines) in enumerate(list(refs.items())[:30]):
        print(f"\n{i + 1}. {file}")
        for line_num, line in lines[:2]:
            print(f"   L{line_num}: {line[:70]}...")

    if len(refs) > 30:
        print(f"\n... y {len(refs) - 30} archivos más")

    print("\n" + "=" * 80)
    print("RESUMEN DE IMPACTO")
    print("=" * 80)
    print(f"Archivos a modificar: {len(refs)}")
    print(f"Reemplazos totales: {sum(len(v) for v in refs.values())}")
    print("\nPrecaución: Muchos archivos son文档ación que referencia")
    print("la estructura, no código que llama las skills.")

    return refs


def generate_script(refs):
    """Genera script de migración (sed para Unix/Mac, ps1 para Windows)"""

    script_path = ROOT / "08_Scripts_Os" / "12_Audits" / "migrate_skills_routes.ps1"

    script = f"""# Script de Migración de Rutas de Skills
# Generated: Auto-refactor .agent/02_Skills/ -> 01_Core/03_Skills/
# DRY RUN - NOmodifica archivos

$OLD_PATH = ".agent/02_Skills/"
$NEW_PATH = "01_Core/03_Skills/"

$files = @(
"""

    for file in sorted(refs.keys()):
        script += f'    "{file}",\n'

    script += """)

Write-Host "DRY RUN - Archivos que serían modificados:" -ForegroundColor Yellow
$files | ForEach-Object {{ Write-Host "  $_" }}

$count = $files.Count
Write-Host "`nTotal: $count archivos" -ForegroundColor Cyan

Write-Host "`nPara ejecutar la migración, cambia '$false' a '$true' en la línea siguiente:" -ForegroundColor Yellow
$migrate = $false

if ($migrate) {{
    foreach ($file in $files) {{
        $fullPath = Join-Path $PSScriptRoot "..\\..\\$file"
        if (Test-Path $fullPath) {{
            (Get-Content $fullPath -Raw) -replace [regex]::Escape($OLD_PATH), $NEW_PATH | 
                Set-Content $fullPath -NoNewline
            Write-Host "Updated: $file" -ForegroundColor Green
        }}
    }}
    Write-Host "`nMigración completada!" -ForegroundColor Green
}} else {{
    Write-Host "`nDRY RUN completado. No se modificó ningún archivo." -ForegroundColor Yellow
}}
"""

    script_path.write_text(script, encoding="utf-8")
    print(f"\nScript generado: {script_path}")
    return script_path


if __name__ == "__main__":
    refs = analyze_impact()
    script_path = generate_script(refs)
    print("\n✅ Auditoría completada. Ejecutar script para ver preview.")
