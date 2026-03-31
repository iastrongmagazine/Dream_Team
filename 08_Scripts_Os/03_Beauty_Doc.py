#!/usr/bin/env python3
"""
Beauty Doc - Aplica formato premium a todos los documentos markdown del proyecto.
Versión actualizada para PersonalOS v6.1
"""

import os
import re
import glob
import hashlib

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_content_hash(text: str) -> str:
    """Hash del contenido sin espacios."""
    pure = "".join(text.split())
    return hashlib.sha256(pure.encode("utf-8")).hexdigest()


def beautify_markdown(content: str) -> str:
    """Reglas de estética premium."""
    # Normalizar saltos entre títulos y párrafos
    content = re.sub(r"(#+ .*?)\n+", r"\1\n\n", content)
    # Espacio después de títulos
    content = re.sub(r"(#+ .*?)\n(?!\n)", r"\1\n\n", content)
    # Listas con un espacio
    content = re.sub(r"^(\s*[\-\*])\s*", r"\1 ", content, flags=re.MULTILINE)
    # Máximo 2 saltos
    content = re.sub(r"\n{3,}", r"\n\n", content)
    # Un salto al final
    content = content.strip() + "\n"
    return content


def process_file(file_path: str) -> tuple:
    """Procesa archivo individual. Returns (success, message)"""
    try:
        if not os.path.exists(file_path):
            return False, f"[SKIP] No existe: {os.path.basename(file_path)}"

        with open(file_path, "r", encoding="utf-8") as f:
            original = f.read()
        original_hash = get_content_hash(original)

        beautified = beautify_markdown(original)
        beautified_hash = get_content_hash(beautified)

        # Validar integridad
        if original_hash != beautified_hash:
            return (
                False,
                f"[ERROR] Integridad comprometida: {os.path.basename(file_path)}",
            )

        if original != beautified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(beautified)
            return True, f"[BEAUTY] Optimizado: {os.path.basename(file_path)}"

        return True, f"[OK] Ya bello: {os.path.basename(file_path)}"

    except (OSError, UnicodeDecodeError) as e:
        return False, f"[EXCEPTION] {os.path.basename(file_path)}: {e}"


def main():
    print("=" * 50)
    print("   PERSONAL OS : BEAUTY DOC v2.0")
    print("=" * 50)

    # Buscar TODOS los .md en el proyecto
    all_md_files = glob.glob(os.path.join(BASE_DIR, "**/*.md"), recursive=True)

    # Excluir ciertos paths
    exclude_patterns = [
        "node_modules",
        ".git",
        "dist",
        "build",
        "__pycache__",
        "Legacy",
        "legacy",
        "backup",
        ".claude",
    ]

    files_to_process = []
    for f in all_md_files:
        if not any(pattern in f for pattern in exclude_patterns):
            files_to_process.append(f)

    print(f"📄 Encontrados: {len(files_to_process)} archivos .md")

    success_count = 0
    error_count = 0

    for file_path in files_to_process:
        success, msg = process_file(file_path)
        print(msg)
        if success:
            success_count += 1
        else:
            error_count += 1

    print("=" * 50)
    print(f"✅ Procesados: {success_count}")
    print(f"❌ Errores: {error_count}")
    print("=" * 50)


if __name__ == "__main__":
    main()
