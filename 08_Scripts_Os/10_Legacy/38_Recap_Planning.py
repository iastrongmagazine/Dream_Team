import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import ROOT_DIR as BASE_DIR, OPERATIONS_TASKS_DIR

"""
MORNING PLANNING: Sistema Avanzado de Planificación Matutina.
Integra Fireflies, MCP para Tareas y Alineación Estratégica.
"""
import os
import json
import io
from datetime import datetime

TASKS_DIR = OPERATIONS_TASKS_DIR


def get_latest_sync_time():
    # Simulado: En producción leería de un archivo de estado
    return "2026-02-20T09:00:00Z"


def find_fireflies_meetings(last_sync):
    """
    Simula la llamada al MCP de Fireflies para encontrar reuniones.
    En ejecución real, esto sería una llamada a tool.
    """
    print(f"[FIREFLIES] Buscando reuniones desde {last_sync}...")
    # Mock data
    return [
        {
            "title": "Ariza AI and Experimentation Workflow",
            "date": "2026-02-26",
            "summary": "Discusión sobre flujos de agentes autónomos.",
        },
        {
            "title": "System Architecture Review",
            "date": "2026-02-25",
            "summary": "Revisión de la Base 2 de PersonalOS.",
        },
    ]


def list_mcp_tasks():
    """
    Enumera tareas reales de 02_Operations/01_Active_Tasks/.
    """
    print("[MCP] Enumerando tareas reales de 02_Operations/01_Active_Tasks/...")
    tasks = []
    if os.path.exists(TASKS_DIR):
        import glob

        for i, task_path in enumerate(
            sorted(glob.glob(os.path.join(TASKS_DIR, "*.md")))
        ):
            task_file_name = os.path.basename(task_path)
            if task_file_name == "README.md":
                continue
            with open(task_path, "r", encoding="utf-8") as f:
                content = f.read()
                # Extraer título y prioridad del YAML
                priority = "P2"
                if "priority: P0" in content:
                    priority = "P0"
                elif "priority: P1" in content:
                    priority = "P1"

                title = os.path.splitext(task_file_name)[0]
                if "title: " in content:
                    title = content.split("title: ")[1].split("\n")[0].strip()

                tasks.append({"id": i + 1, "task": title, "priority": priority})

    if not tasks:
        # Fallback to mock
        return [{"id": 1, "task": "Configurar Personal OS", "priority": "P0"}]
    return tasks


def generate_morning_plan():
    print("=" * 60)
    print("        SISTEMA DE PLANIFICACIÓN MATUTINA (MORNING PLANNING)")
    print("=" * 60)

    # 1. Fireflies Integration
    last_sync = get_latest_sync_time()
    meetings = find_fireflies_meetings(last_sync)

    print("\n--- [1] RESUMEN DE REUNIONES (FIREFLIES) ---")
    for m in meetings:
        print(f"• {m['title']} ({m['date']})")
        print(f"  Resumen: {m['summary']}")
        # Validación lógica (simulada)
        print(f"  [SYNC] Relevante para metas actuales: SÍ")

    # 2. MCP Task Enumeration
    tasks = list_mcp_tasks()
    # Ordenar por prioridad: P0 primero, luego P1, luego P2
    priority_map = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    tasks.sort(key=lambda x: priority_map.get(x["priority"], 99))

    print("\n--- [2] ENFOQUE PARA EL DÍA ---")
    print(
        "Hoy el enfoque es: Consolidación de la Estructura Base 2 y Mejora de Comunicación."
    )

    print("\n--- [3] TOP 3 DE TAREAS (P0/P1) ---")
    for t in tasks[:3]:
        print(f"{t['id']}. [{t['priority']}] {t['task']}")

    print("\n--- [4] VICTORIAS RÁPIDAS (QUICK WINS) ---")
    print("• Ejecutar script de limpieza (16_Clean_System.py)")
    print("• Actualizar el archivo de estructura completa.")

    print("\n--- [5] HOUSEKEEPING NOTES ---")
    print("• Revisar carpeta 06_Archive para purga mensual.")
    print("• Validar integridad de reglas de Cursor.")

    print("\n" + "-" * 60)
    print("  ¿EN QUÉ DEBERÍA TRABAJAR PRIMERO?")
    print(f"  >>> {tasks[0]['task']} <<<")
    print("-" * 60)

    print("\n[TIP] Usa el comando /morning-planning para refrescar este plan.")


if __name__ == "__main__":
    generate_morning_plan()
