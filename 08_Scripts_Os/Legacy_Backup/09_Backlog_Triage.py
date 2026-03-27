import os
import sys
import io
import re
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import ROOT_DIR as BASE_DIR, CORE_DIR

if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

BACKLOG_FILE = CORE_DIR / "BACKLOG.md"


def get_categories(text):
    """Extrae todas las etiquetas #categoria del texto."""
    matches = re.findall(r"#(\w+)", text)
    return sorted(list(set(m.upper() for m in matches))) if matches else ["GENERAL"]


def process_backlog():
    """Analiza y organiza el archivo BACKLOG.md por categorías."""
    print("--- 🧹 PersonalOS BACKLOG TRIAGE v2.1 (Multi-Category Support) ---")

    if not os.path.exists(BACKLOG_FILE):
        print(f"[ERROR] No se encontró {BACKLOG_FILE}")
        return

    with open(BACKLOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    tasks_section = False
    captured_tasks = []

    for line in lines:
        if "## 🚀 Tareas del Sistema" in line:
            tasks_section = True
            new_lines.append(line)
            continue

        if tasks_section and line.startswith("---"):
            # Procesar tareas antes de cerrar la sección
            if captured_tasks:
                # Mapa de categorías: cada tarea puede estar en varias
                categories_map = {}
                seen_tasks = set()
                for task in captured_tasks:
                    task_clean = task.strip()
                    if task_clean in seen_tasks:
                        continue
                    seen_tasks.add(task_clean)

                    cats = get_categories(task)
                    for cat in cats:
                        if cat not in categories_map:
                            categories_map[cat] = []
                        categories_map[cat].append(task)

                # Siempre poner GENERAL al final si existe
                sorted_cats = sorted([c for c in categories_map if c != "GENERAL"])
                if "GENERAL" in categories_map:
                    sorted_cats.append("GENERAL")

                for cat in sorted_cats:
                    new_lines.append(f"\n### 🏷️ {cat}\n")
                    for t in categories_map[cat]:
                        new_lines.append(t)

                captured_tasks = []

            tasks_section = False
            new_lines.append("\n" + line)  # Asegurar espacio antes del separador
            continue

        if tasks_section:
            clean_line = line.strip()
            if clean_line and (
                clean_line.startswith("- [") or re.match(r"^\d+\.", clean_line)
            ):
                captured_tasks.append(line)
            elif clean_line.startswith("###"):
                # Ignorar encabezados viejos dinámicos
                continue
            elif not clean_line and captured_tasks:
                # Ignorar líneas vacías dentro del bloque de tareas para reconstrucción limpia
                continue
            else:
                # Conservar texto que no sean tareas (comentarios, etc.)
                if clean_line or not captured_tasks:
                    new_lines.append(line)
        else:
            new_lines.append(line)

    # Escribir cambios de vuelta
    with open(BACKLOG_FILE, "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print("\n[INFO] Análisis de categorías completado:")
    print("- Soporte multi-categoría activado.")
    print("- Las tareas se han duplicado en sus respectivas secciones de etiquetas.")
    print("\n[OK] Backlog organizado por dimensión estratégica.")


if __name__ == "__main__":
    process_backlog()
