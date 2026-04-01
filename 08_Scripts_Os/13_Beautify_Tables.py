#!/usr/bin/env python3
"""
Beautify Tables - Alinea y embellece todas las tablas markdown del proyecto.
Versión para PersonalOS v6.1
"""

import sys
import os
import re
import glob
import io

# Fix encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def align_table(table_block):
    """Alinea las columnas de una tabla markdown."""
    lines = table_block.strip().split("\n")
    if len(lines) < 2:
        return table_block

    # Parse rows
    rows = []
    for line in lines:
        if not line.strip().startswith("|"):
            return table_block

        cells = [c.strip() for c in line.split("|")]
        if cells and cells[0] == "":
            cells.pop(0)
        if cells and cells[-1] == "":
            cells.pop(-1)
        rows.append(cells)

    if not rows:
        return table_block

    # Calcular ancho de cada columna
    col_widths = {}
    for row in rows:
        for i, cell in enumerate(row):
            col_widths[i] = max(col_widths.get(i, 0), len(cell))
            if set(cell) == {"-"}:
                col_widths[i] = max(col_widths.get(i, 0), 3)

    # Reconstruir
    new_lines = []
    for row in rows:
        new_row = "|"
        for i, cell in enumerate(row):
            width = col_widths.get(i, 0)
            if set(cell) == {"-"} or (
                set(cell).issubset({"-", ":", " "}) and len(cell) > 1
            ):
                content = "-" * (width + 2)
            else:
                content = f" {cell.ljust(width)} "
            new_row += content + "|"
        new_lines.append(new_row)

    return "\n".join(new_lines)


def process_file(file_path):
    """Procesa un archivo y beautifica sus tablas."""
    try:
        if not os.path.exists(file_path):
            return False, f"[SKIP] No existe: {os.path.basename(file_path)}"

        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        original = content

        # State machine para tablas
        new_lines = []
        current_table = []
        in_table = False

        for line in content.splitlines():
            is_table_row = line.strip().startswith("|") and "|" in line

            if is_table_row:
                current_table.append(line)
                in_table = True
            else:
                if in_table:
                    table_block = "\n".join(current_table)
                    if len(current_table) >= 2 and any(
                        "---" in l for l in current_table
                    ):
                        new_lines.append(align_table(table_block))
                    else:
                        new_lines.extend(current_table)
                    current_table = []
                    in_table = False
                new_lines.append(line)

        # Fin del archivo con tabla
        if in_table and current_table:
            table_block = "\n".join(current_table)
            if len(current_table) >= 2 and any("---" in l for l in current_table):
                new_lines.append(align_table(table_block))
            else:
                new_lines.extend(current_table)

        new_content = "\n".join(new_lines) + "\n"

        if new_content != original:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            return True, f"[BEAUTY] {os.path.basename(file_path)}"

        return True, f"[OK] {os.path.basename(file_path)}"

    except Exception as e:
        return False, f"[ERROR] {os.path.basename(file_path)}: {e}"


def main():
    print("=" * 50)
    print("   BEAUTIFY TABLES - PersonalOS v2.0")
    print("=" * 50)

    # Buscar todos los .md
    all_md = glob.glob(os.path.join(PROJECT_ROOT, "**/*.md"), recursive=True)

    # Excluir paths
    exclude = [
        "node_modules",
        ".git",
        "dist",
        "build",
        "__pycache__",
        "Legacy",
        "legacy",
    ]
    files = [f for f in all_md if not any(p in f for p in exclude)]

    print(f"📊 Archivos a procesar: {len(files)}")

    success = 0
    errors = 0

    for f in files:
        ok, msg = process_file(f)
        print(msg)
        if ok:
            success += 1
        else:
            errors += 1

    print("=" * 50)
    print(f"✅ Procesados: {success}")
    print(f"❌ Errores: {errors}")
    print("=" * 50)


if __name__ == "__main__":
    main()
