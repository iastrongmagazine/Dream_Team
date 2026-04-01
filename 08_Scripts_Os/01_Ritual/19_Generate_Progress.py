#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PersonalOS PROGRESS DASHBOARD v6.1
Genera una vista consolidada del estado de todas las tareas.
"""

import os
import sys
import io
import re
import glob
from pathlib import Path

# === SETUP PATHS ===
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import importlib.util
from datetime import datetime
from typing import Dict, List, Tuple, Optional

# --- CONFIGURACIÓN ARMOR LAYER ---
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# === IMPORTS ===
try:
    from config_paths import (
        ROOT_DIR,
        BRAIN_DIR,
        BRAIN_RULES_DIR,
        COMPOUND_ENGINE_DIR,
        ENGINE_DIR,
        TASKS_DIR,
        BASE_DIR,
    )
except ImportError:
    ROOT_DIR = PROJECT_ROOT
    BASE_DIR = PROJECT_ROOT
    BRAIN_DIR = PROJECT_ROOT / "04_Operations"
    BRAIN_RULES_DIR = BRAIN_DIR / "04_Memory_Brain"
    COMPOUND_ENGINE_DIR = (
        PROJECT_ROOT / "01_Core" / "03_Skills" / "00_Compound_Engineering"
    )
    ENGINE_DIR = PROJECT_ROOT / "08_Scripts_Os"
    TASKS_DIR = PROJECT_ROOT / "03_Tasks"

# Importar sistema de progreso
templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
sys.path.insert(0, templates_dir)
try:
    from multi_step_script_template import report_progress
except ImportError:

    def report_progress(step, total, desc, speak_func=None):
        """Fallback para reportar progreso si el template no está disponible."""
        progress = (step / total) * 100
        print(f"\n{INFO}[{progress:.1f}%] Paso {step}/{total}: {desc}{RESET}")
        if speak_func and progress in [25.0, 50.0, 75.0, 100.0]:
            speak_func(f"Progreso: {progress:.0f} por ciento completado.")


# --- COLORES ---
try:
    from colorama import init, Fore, Style

    init(autoreset=True)
    SUCCESS = Fore.GREEN
    INFO = Fore.CYAN
    WARNING = Fore.YELLOW
    ERROR = Fore.RED
    BRIGHT = Style.BRIGHT
    RESET = Style.RESET_ALL
except ImportError:
    SUCCESS = INFO = WARNING = ERROR = BRIGHT = RESET = ""

# --- CONSTANTES ---
# Usar las rutas de config_paths o fallback
if isinstance(TASKS_DIR, str):
    TASKS_DIR = Path(TASKS_DIR)
if isinstance(BASE_DIR, str):
    BASE_DIR = Path(BASE_DIR)

TASK_END_DIR = TASKS_DIR / "Task_End"
PROGRESS_FILE = ROOT_DIR / "00_Winter_is_Coming" / "PROGRESS.md"

# Orden de prioridad
PRIORITY_ORDER = [
    "P0",
    "P1",
    "P2",
    "P3",
    "H1",
    "H2",
    "H3",
    "H4",
    "T1",
    "T2",
    "T3",
    "T4",
]


def speak(text):
    """Interfaz de voz integrada."""
    try:
        common_path = (
            BASE_DIR / ".agent" / "04_Extensions" / "hooks" / "utils" / "common.py"
        )
        if os.path.exists(common_path):
            spec = importlib.util.spec_from_file_location("common", str(common_path))
            common = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(common)
            common.speak(text)
        else:
            print(f"{INFO}[VOZ]{RESET} {text}")
    except Exception:
        print(f"{INFO}[VOZ]{RESET} {text}")


def print_branding():
    """Imprime la cabecera premium de PersonalOS."""
    print(f"\n{BRIGHT}{INFO}==============================================")
    print(f"{BRIGHT}{INFO}   [DASHBOARD] PERSONAL OS : PROGRESS v2.0")
    print(f"{BRIGHT}{INFO}      SUPER UNIFIED EDITION")
    print(f"{BRIGHT}{INFO}=============================================={RESET}")


# =============================================================================
# LÓGICA DE 70_Progress_Update (FUSIONADA)
# =============================================================================


def extract_frontmatter(filepath: Path) -> Dict:
    """Extrae el frontmatter YAML de un archivo markdown."""
    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception:
        return {}

    frontmatter = {}

    # Buscar frontmatter ---
    if content.startswith("---"):
        end = content.find("---", 3)
        if end != -1:
            fm_text = content[3:end].strip()
            for line in fm_text.split("\n"):
                if ":" in line:
                    key, value = line.split(":", 1)
                    frontmatter[key.strip()] = value.strip()

    return frontmatter


def get_priority_from_filename(filename: str) -> str:
    """Extrae la prioridad del nombre del archivo."""
    for p in PRIORITY_ORDER:
        if p in filename:
            return p
    return "P9"  # Menor prioridad


def get_task_status_from_frontmatter(filepath: Path) -> str:
    """Determina el estado de una task desde frontmatter."""
    fm = extract_frontmatter(filepath)
    status = fm.get("status", "").lower()

    # Si está en Task_End, está completada
    if "Task_End" in str(filepath):
        return "done"

    # Parsear status
    if status in ["y", "yes", "done", "completed", "complete", "c"]:
        return "done"
    elif status in ["p", "progress", "in_progress", "i"]:
        return "in_progress"
    elif status in ["n", "no", "pending", "todo", "-"]:
        return "pending"

    return "pending"


def get_task_title(filepath: Path) -> str:
    """Obtiene el título de la task."""
    fm = extract_frontmatter(filepath)
    if fm.get("title"):
        return fm["title"]

    # Del nombre del archivo
    filename = filepath.stem
    # Remover prefijo de prioridad
    filename = re.sub(r"^\d+_?[PHTH]\d+_?", "", filename)
    return filename.replace("_", " ")


def get_priority_index(priority: str) -> int:
    """Obtiene el índice de prioridad para ordenamiento."""
    if priority in PRIORITY_ORDER:
        return PRIORITY_ORDER.index(priority)
    return 999


# =============================================================================
# LÓGICA DE 19_Generate_Progress (MEJORADA)
# =============================================================================


def scan_tasks() -> List[Dict]:
    """Escanea todas las tareas con soporte para Task_End y YAML."""
    if not os.path.exists(TASKS_DIR):
        print(f"{ERROR}Error: No se encuentra el directorio de tareas{RESET}")
        return []

    tasks = []

    # Archivos en directorio principal
    task_files = glob.glob(os.path.join(TASKS_DIR, "*.md"))

    # Archivos en Task_End (recursivo)
    if os.path.exists(TASK_END_DIR):
        task_files.extend(
            glob.glob(os.path.join(TASK_END_DIR, "**", "*.md"), recursive=True)
        )

    # Excluir README y TODO_Work
    task_files = [f for f in task_files if "README" not in f and "TODO_Work" not in f]

    for task_path in task_files:
        try:
            task_file_name = os.path.basename(task_path)
            filepath = Path(task_path)

            with open(task_path, "r", encoding="utf-8") as f:
                content = f.read()

            # === Detectar si está en Task_End ===
            in_task_end = "Task_End" in task_path

            # === Estado desde frontmatter (nuevo de 70) ===
            yaml_status = get_task_status_from_frontmatter(filepath)

            # === Prioridad desde filename (nuevo de 70) ===
            priority = get_priority_from_filename(task_file_name)

            # === Título (mejorado) ===
            fm = extract_frontmatter(filepath)
            if fm.get("title"):
                title = fm["title"]
            else:
                title_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
                title = (
                    title_match.group(1).strip()
                    if title_match
                    else get_task_title(filepath)
                )

            # === Tags (de 19) ===
            tags = re.findall(r"#(\w+)", content)
            tags_unique = sorted(list(set([t.upper() for t in tags])))
            tags_str = (
                ", ".join([f"`#{t}`" for t in tags_unique[:5]])  # Max 5 tags
                if tags_unique
                else "_Sin etiquetas_"
            )

            # === Métricas de avance (checkbox style de 19) ===
            total_items = content.count("- [")
            completed_items = content.count("- [x]")

            # Si está en Task_End, считать como 100%
            if in_task_end or yaml_status == "done":
                progress = 100.0
                completed_items = total_items if total_items > 0 else 1
            else:
                progress = (
                    (completed_items / total_items * 100) if total_items > 0 else 0
                )

            # === Estado Semántico (mejorado) ===
            if yaml_status == "done" or in_task_end:
                status = "✅ Hecho"
                completed_items = total_items if total_items > 0 else 1
                progress = 100.0
            elif yaml_status == "in_progress":
                status = "🔄 En curso"
            elif progress > 0:
                status = f"🔄 En curso ({progress:.0f}%)"
            else:
                status = "⏸️ Pendiente"

            tasks.append(
                {
                    "file": task_file_name,
                    "title": title,
                    "status": status,
                    "progress": progress,
                    "completed": completed_items,
                    "total": max(total_items, 1),
                    "tags": tags_str,
                    "priority": priority,
                    "priority_index": get_priority_index(priority),
                    "has_active_work": yaml_status == "in_progress"
                    or "- [/" in content,
                    "is_done": yaml_status == "done" or in_task_end,
                }
            )
        except (IOError, OSError) as e:
            print(f"{WARNING}Aviso: No se pudo procesar {task_path}: {e}{RESET}")

    # Ordenar: primero por prioridad, luego por progreso (completadas al inicio)
    return sorted(
        tasks, key=lambda x: (not x["is_done"], x["priority_index"], -x["progress"])
    )


def calculate_stats(tasks: List[Dict]) -> Dict:
    """Calcula estadísticas consolidadas."""
    total = len(tasks)
    done = len([t for t in tasks if t["is_done"]])
    working = len([t for t in tasks if t["has_active_work"] and not t["is_done"]])
    pending = total - done - working
    global_avg = sum(t["progress"] for t in tasks) / total if total > 0 else 0

    # Stats por prioridad
    priority_stats = {}
    for p in PRIORITY_ORDER:
        p_tasks = [t for t in tasks if t["priority"] == p]
        if p_tasks:
            priority_stats[p] = {
                "done": len([t for t in p_tasks if t["is_done"]]),
                "total": len(p_tasks),
                "pct": len([t for t in p_tasks if t["is_done"]]) / len(p_tasks) * 100
                if p_tasks
                else 0,
            }

    return {
        "total": total,
        "done": done,
        "working": working,
        "pending": pending,
        "global_avg": global_avg,
        "priority_stats": priority_stats,
    }


def generate_dashboard():
    """Genera el reporte visual PROGRESS.md unificado."""
    total_steps = 6

    # Paso 1: Branding
    report_progress(1, total_steps, "Inicializando Dashboard", speak_func=speak)
    print_branding()
    print(f"{INFO}Buscando tareas en 02_Operations/01_Active_Tasks...{RESET}")

    # Paso 2: Escaneo
    report_progress(2, total_steps, "Escaneando Tareas + Task_End", speak_func=speak)
    tasks = scan_tasks()
    if not tasks:
        print(f"{ERROR}Zero tareas encontradas. Abortando.{RESET}")
        return

    # Paso 3: Stats
    report_progress(3, total_steps, "Calculando Estadisticas", speak_func=speak)
    stats = calculate_stats(tasks)

    # Determinar foco
    active_tasks = [t for t in tasks if t["has_active_work"] and not t["is_done"]]
    focus_task = active_tasks[0]["title"] if active_tasks else "Ninguno"

    # Paso 4: Generar contenido principal
    report_progress(4, total_steps, "Generando Contenido", speak_func=speak)

    content = f"""# Dashboard de Progreso: PersonalOS

> **Estado:** `{"SALUDABLE" if stats["global_avg"] > 50 else "EN DESARROLLO"}`
> **Ultima actualizacion:** `{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}`
> **Foco actual:** `{focus_task}`

---

## Resumen General

| Metrica | Valor |
|---------|-------|
| Completadas | {stats["done"]} |
| En Progreso | {stats["working"]} |
| Pendientes | {stats["pending"]} |
| Total | {stats["total"]} |
| Progreso | {stats["global_avg"]:.1f}% |

---

## Progreso por Prioridad

| Prioridad | Done | Total | Progreso |
|-----------|------|-------|----------|
"""

    # Agregar stats por prioridad
    for p in PRIORITY_ORDER:
        if p in stats["priority_stats"]:
            s = stats["priority_stats"][p]
            content += f"| {p} | {s['done']} | {s['total']} | {s['pct']:.0f}% |\n"

    content += """
---

## Registro de Tareas

| Prioridad | Tarea | Estado | Progreso |
|-----------|-------|--------|----------|
"""

    # Tareas completadas primero
    for task in tasks:
        bar_len = 10
        filled = int((task["progress"] / 100) * bar_len)
        visual_bar = "█" * filled + "░" * (bar_len - filled)
        content += f"| {task['priority']} | {task['title'][:50]} | {task['status']} | `{visual_bar}` {task['progress']:.0f}% |\n"

    # Paso 5: Tareas pendientes detalladas
    report_progress(5, total_steps, "Listando tareas pendientes", speak_func=speak)

    content += """
---

## Detalle de Tareas Pendientes

"""

    pending_by_priority = {}
    for task in tasks:
        if not task["is_done"]:
            p = task["priority"]
            if p not in pending_by_priority:
                pending_by_priority[p] = []
            pending_by_priority[p].append(task["title"])

    for p in PRIORITY_ORDER:
        if p in pending_by_priority:
            content += f"### {p}\n\n"
            for title in pending_by_priority[p]:
                content += f"- [ ] {title}\n"
            content += "\n"

    # Paso 6: Guardar
    report_progress(6, total_steps, "Guardando PROGRESS.md", speak_func=speak)
    try:
        with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"{SUCCESS}[OK] PROGRESS.md actualizado{RESET}")

        speak(
            f"Dashboard actualizado. {stats['done']} tareas completadas de {stats['total']}. "
            f"Progreso global {stats['global_avg']:.0f} por ciento."
        )

    except (IOError, OSError) as e:
        print(f"{ERROR}[ERR] No se pudo escribir: {e}{RESET}")


if __name__ == "__main__":
    generate_dashboard()
