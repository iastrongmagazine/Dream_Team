"""
SKILL AUDITOR & FIXER
Audita la estructura de .agent/02_Skills y corrige la numeración.
"""

import os
import sys
import re

Skills_ROOT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".agent", "02_Skills"
)
CATEGORIES = ["01_Core", "02_High_Value", "03_Utilities"]


def sanitize_name(name):
    # Eliminar prefijos numéricos existentes y guiones bajos extra
    name = re.sub(r"^\d+[_\-]", "", name)
    name = name.replace("-", "_").replace(" ", "_")
    # Convertir a Title Case (excepto siglas conocidas si se desea, pero Title es estándar)
    return "".join(x.capitalize() for x in name.split("_"))


def audit_category(category_name):
    cat_path = os.path.join(Skills_ROOT, category_name)
    if not os.path.exists(cat_path):
        print(f"❌ Categoría no encontrada: {category_name}")
        return

    print(f"\n📂 Analizando Categoría: {category_name}")

    # Listar directorios
    items = [
        d for d in os.listdir(cat_path) if os.path.isdir(os.path.join(cat_path, d))
    ]

    # Ordenar por nombre actual para mantener cierta lógica, o intentar detectar número
    # Estrategia: Detectar si ya tiene número, usarlo para ordenar. Si no, al final.
    def sort_key(d_name):
        match = re.match(r"^(\d+)", d_name)
        if match:
            return int(match.group(1))
        return 9999 + len(d_name)  # Al final

    items.sort(key=sort_key)

    expected_num = 1
    changes = []

    for item_name in items:
        original_name = item_name

        # Extraer nombre base limpio
        # Caso especial: Si es "01_Fork_Terminal", base es "Fork_Terminal"
        # Si es "20_browser-use", base es "BrowserUse"

        # Regex para separar numero del resto
        match = re.match(r"^(\d+)[_\-](.+)$", original_name)
        if match:
            current_num = int(match.group(1))
            raw_name = match.group(2)
        else:
            current_num = None
            raw_name = original_name

        # Normalizar nombre (TitleCase, sin guiones)
        # Excepciones manuales si es necesario, pero TitleCase es seguro
        # browser-use -> BrowserUse
        # remotion-best-practices -> RemotionBestPractices

        clean_name = raw_name.replace("-", "_").replace(" ", "_")
        clean_name = "_".join(word.capitalize() for word in clean_name.split("_"))

        # Construir nuevo nombre ideal
        new_name = f"{expected_num:02d}_{clean_name}"

        if original_name != new_name:
            # Check if destination exists (collision)
            if (
                os.path.exists(os.path.join(cat_path, new_name))
                and new_name != item_name
            ):
                print(
                    f"   ⚠️ Conflicto: {new_name} ya existe. Saltando renombre de {original_name}"
                )
            else:
                changes.append(
                    (
                        os.path.join(cat_path, item_name),
                        os.path.join(cat_path, new_name),
                    )
                )
                print(f"   🔧 {original_name} -> {new_name}")
        else:
            print(f"   ✅ {original_name}")

        expected_num += 1

    return changes


def apply_changes(changes):
    if not changes:
        return

    print("\n⚡ Aplicando cambios...")
    for src, dst in changes:
        try:
            os.rename(src, dst)
            print(f"   Renombrado: {os.path.basename(src)} -> {os.path.basename(dst)}")
        except Exception as e:
            print(f"   ❌ Error renombrando {os.path.basename(src)}: {e}")


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    if not os.path.exists(Skills_ROOT):
        print(f"Error: No se encuentra {Skills_ROOT}")
        return

    all_changes = []
    for cat in CATEGORIES:
        changes = audit_category(cat)
        if changes:
            all_changes.extend(changes)

    if all_changes:
        # Prompt user? No, subagent script should just do it or report it.
        # Given "cuida la numeracion", we should fix it.
        # But allow a "dry run" arg ideally. For now, let's just apply to fix errors.
        apply_changes(all_changes)
        print("\n✨ Auditoría y corrección de numeración completada.")
    else:
        print("\n✨ Toda la numeración está perfecta.")


if __name__ == "__main__":
    main()
