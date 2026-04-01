#!/usr/bin/env python3
"""
09_Backlog_Triage.py - PersonalOS Backlog Triage v3.0
======================================================
Procesa el BACKLOG, crea tareas en 03_Tasks/ y limpia el backlog.

Flujo:
1. Lee 00_Winter_is_Coming/BACKLOG.md
2. Extrae tareas accionables
3. Crea archivos de tarea en 03_Tasks/
4. Limpia el BACKLOG.md

Usage:
    python 09_Backlog_Triage.py           # Solo mostrar preview
    python 09_Backlog_Triage.py --execute  # Crear tareas y limpiar
"""

import sys
import os
import io
import re
import argparse
from pathlib import Path
from datetime import datetime

# Fix Windows encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# Path resolution
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent

# Add Legacy_Backup to path for config_paths
LEGACY_DIR = PROJECT_ROOT / "08_Scripts_Os" / "Legacy_Backup"
sys.path.insert(0, str(LEGACY_DIR))

from config_paths import ROOT_DIR, TASKS_DIR


# ============================================================================
# CONFIGURATION
# ============================================================================

BACKLOG_FILE = PROJECT_ROOT / "00_Winter_is_Coming" / "BACKLOG.md"
TASKS_DIR = PROJECT_ROOT / "03_Tasks"

# Template de tarea
TASK_TEMPLATE = """---
title: {title}
category: {category}
priority: {priority}
status: n
created_date: {date}
resource_refs:
  - 00_Winter_is_Coming/BACKLOG.md
---

# {title}

## Context
Creado desde backlog procesado el {date}.

## Next Actions
- [ ] {next_action}

## Progress Log
- {date}: Tarea creada desde backlog
"""

# Categorías válidas
CATEGORIES = {
    "technical": "P0-P1",
    "outreach": "P1-P2",
    "research": "P2",
    "writing": "P2",
    "content": "P2",
    "admin": "P1",
    "personal": "P2",
    "other": "P3",
}


# ============================================================================
# FUNCTIONS
# ============================================================================


def parse_backlog_items(content: str) -> list[dict]:
    """Parsea tareas del contenido del backlog."""
    items = []
    lines = content.split("\n")

    for line in lines:
        line = line.strip()

        # Skip headers and empty lines
        if not line or line.startswith("#"):
            continue

        # Parsear items de lista (- [ ] o - item)
        if line.startswith("- "):
            text = line[2:].strip()
            if text and not text.startswith("["):
                # Detectar prioridad
                priority = infer_priority(text)
                category = infer_category(text)

                items.append(
                    {
                        "text": text,
                        "priority": priority,
                        "category": category,
                    }
                )

    return items


def infer_priority(text: str) -> str:
    """Infiere prioridad basada en palabras clave."""
    text_lower = text.lower()

    if any(w in text_lower for w in ["urgent", "p0", "crítico", "ahora", "hoy"]):
        return "P0"
    elif any(w in text_lower for w in ["important", "p1", "importante", "semana"]):
        return "P1"
    elif any(w in text_lower for w in ["someday", "maybe", "idea", "algún día"]):
        return "P3"
    else:
        return "P2"


def infer_category(text: str) -> str:
    """Infiere categoría basada en palabras clave."""
    text_lower = text.lower()

    if any(w in text_lower for w in ["bug", "error", "fix", "broken", "error"]):
        return "technical"
    elif any(
        w in text_lower for w in ["meeting", "call", "contact", "llamar", "hablar"]
    ):
        return "outreach"
    elif any(
        w in text_lower for w in ["research", "investigar", "analyze", "analizar"]
    ):
        return "research"
    elif any(
        w in text_lower for w in ["write", "blog", "post", "escribir", "redactar"]
    ):
        return "writing"
    elif any(w in text_lower for w in ["content", "video", "social"]):
        return "content"
    elif any(w in text_lower for w in ["admin", "report", "expense", "reporte"]):
        return "admin"
    elif any(w in text_lower for w in ["personal", "health", "health"]):
        return "personal"
    else:
        return "other"


def sanitize_filename(text: str) -> str:
    """Convierte texto a nombre de archivo válido."""
    # Reemplazar caracteres no válidos
    filename = re.sub(r"[^\w\s-]", "", text)
    filename = re.sub(r"[-\s]+", "-", filename)
    return filename[:50].strip("-")


def create_task_file(item: dict) -> Path:
    """Crea archivo de tarea en 03_Tasks/."""
    date = datetime.now().strftime("%Y-%m-%d")

    # Generar nombre de archivo
    base_name = sanitize_filename(item["text"])
    filename = f"{item['priority']}_{base_name}.md"

    task_path = TASKS_DIR / filename

    # Evitar duplicados
    counter = 1
    while task_path.exists():
        filename = f"{item['priority']}_{base_name}_{counter}.md"
        task_path = TASKS_DIR / filename
        counter += 1

    # Crear contenido
    content = TASK_TEMPLATE.format(
        title=item["text"][:100],
        category=item["category"],
        priority=item["priority"],
        date=date,
        next_action=item["text"][:80],
    )

    task_path.write_text(content, encoding="utf-8")
    return task_path


def clear_backlog():
    """Limpia el BACKLOG.md dejando solo estructura."""
    if not BACKLOG_FILE.exists():
        print(f"[ERROR] No se encontró {BACKLOG_FILE}")
        return

    # Leer contenido actual
    content = BACKLOG_FILE.read_text(encoding="utf-8")

    # Mantener solo headers y estructura, borrar tareas
    lines = content.split("\n")
    new_lines = []

    for line in lines:
        # Mantener headers y líneas vacías
        if line.startswith("#") or not line.strip():
            new_lines.append(line)
        # Eliminar items de tarea
        elif line.strip().startswith("- "):
            continue
        else:
            new_lines.append(line)

    # Escribir archivo limpio
    BACKLOG_FILE.write_text("\n".join(new_lines), encoding="utf-8")
    print(f"[OK] BACKLOG.md limpiado")


def process_backlog(dry_run: bool = True):
    """Procesa el backlog y opcionalmente crea tareas."""
    print("=" * 60)
    print("📋 PERSONALOS BACKLOG TRIAGE v3.0")
    print("=" * 60)

    # Verificar BACKLOG existe
    if not BACKLOG_FILE.exists():
        print(f"[ERROR] No se encontró: {BACKLOG_FILE}")
        print(f"  Creando BACKLOG.md vacío...")
        BACKLOG_FILE.parent.mkdir(parents=True, exist_ok=True)
        BACKLOG_FILE.write_text("# Backlog\n\n## Pendientes\n\n", encoding="utf-8")
        return

    # Verificar TASKS_DIR existe
    TASKS_DIR.mkdir(parents=True, exist_ok=True)

    # Leer backlog
    content = BACKLOG_FILE.read_text(encoding="utf-8")

    # Parsear items
    items = parse_backlog_items(content)

    if not items:
        print("\n[INFO] No se encontraron tareas en el backlog.")
        return

    print(f"\n📝 Se encontraron {len(items)} tareas:\n")

    created_tasks = []

    for i, item in enumerate(items, 1):
        emoji = {"P0": "🔴", "P1": "🟡", "P2": "🟢", "P3": "⚪"}.get(
            item["priority"], "⚪"
        )
        print(
            f"  {i}. {emoji} [{item['priority']}] [{item['category']}] {item['text'][:60]}"
        )

        if not dry_run:
            task_path = create_task_file(item)
            created_tasks.append(task_path)
            print(f"      ✅ Creado: {task_path.name}")

    print("\n" + "=" * 60)

    if dry_run:
        print("📌 MODO PREVIEW - Usa --execute para crear tareas")
        print("=" * 60)
    else:
        # Limpiar backlog
        clear_backlog()

        print(f"\n✅ RESUMEN:")
        print(f"  - Tareas creadas: {len(created_tasks)}")
        print(f"  - BACKLOG.md limpiado")
        print("=" * 60)


# ============================================================================
# MAIN
# ============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Backlog Triage v3.0")
    parser.add_argument(
        "--execute",
        action="store_true",
        help="Ejecutar (crear tareas y limpiar backlog)",
    )

    args = parser.parse_args()

    # Default: dry-run
    dry_run = not args.execute

    process_backlog(dry_run=dry_run)
