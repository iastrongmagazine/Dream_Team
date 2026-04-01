"""
65_CTX_Generator.py - Armor Layer Protected
CTX GENERATOR - PersonalOS v1.0
Genera reporte de contexto de sesión para Mi bienestar (Gentleman)
Guarda en 01_Brain/01_Context_Memory/CTX_XXX_fecha.md
"""

import os
import sys
import glob
import json
import io
from pathlib import Path
from datetime import datetime

if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import (
    PROJECT_ROOT,
    BRAIN_DIR,
    OPERATIONS_DIR,
    ENGINE_DIR,
    BRAIN_MEMORY_DIR,
    BRAIN_NOTES_DIR,
)

REQUIRED_DIRS = [
    "00_Core",
    "01_Brain",
    "02_Operations",
    "03_Knowledge",
    "04_Engine",
    "05_System",
    "06_Archive",
]
for d in REQUIRED_DIRS:
    if not (PROJECT_ROOT / d).exists():
        print(f"[WARN] Required directory not found: {d}")

BASE_DIR = PROJECT_ROOT
CONTEXT_MEMORY_DIR = BRAIN_MEMORY_DIR
PROCESS_NOTES_DIR = BRAIN_NOTES_DIR
ANALYTICS_DIR = ENGINE_DIR / "Analytics_Output"


def format_date():
    """Retorna fecha en formato dd/mm/aaaa HH:MM:SS"""
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")


def get_next_ctx_number():
    """Obtiene el siguiente número de CTX."""
    if not os.path.exists(CONTEXT_MEMORY_DIR):
        os.makedirs(CONTEXT_MEMORY_DIR, exist_ok=True)

    files = glob.glob(os.path.join(CONTEXT_MEMORY_DIR, "CTX_*.md"))
    if not files:
        return 1

    numbers = []
    for f in files:
        try:
            basename = os.path.basename(f)
            # Extraer número: CTX_001_...
            num_str = basename.split("_")[1]
            numbers.append(int(num_str))
        except:
            pass

    return max(numbers) + 1 if numbers else 1


def get_latest_file(directory, pattern="*.md"):
    """Obtiene el archivo más reciente."""
    if not os.path.exists(directory):
        return None
    files = glob.glob(os.path.join(directory, pattern))
    if not files:
        return None
    return max(files, key=os.path.getmtime)


def read_task_summary():
    """Lee resumen de tareas activas."""
    tasks_dir = os.path.join(OPERATIONS_DIR, "01_Active_Tasks")
    if not os.path.exists(tasks_dir):
        return "Sin tareas"

    count = len([f for f in os.listdir(tasks_dir) if f.endswith(".md")])
    return f"{count} tareas activas"


def get_aipm_metrics():
    """Obtiene métricas AIPM si existen."""
    metrics = {
        "traces": "No hay trazas",
        "evaluation": "No hay evaluación",
        "budget": "Sin datos",
    }

    # Buscar traces
    traces = glob.glob(os.path.join(ANALYTICS_DIR, "trace_*.json"))
    if traces:
        metrics["traces"] = f"{len(traces)} trazas"

    # Buscar evaluación
    eval_file = os.path.join(ANALYTICS_DIR, "evaluation_report.json")
    if os.path.exists(eval_file):
        try:
            with open(eval_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                metrics["evaluation"] = f"Score: {data.get('score', 'N/A')}"
        except:
            pass

    return metrics


def generate_ctx():
    """Genera el reporte CTX de la sesión."""
    print("\n" + "=" * 60)
    print("🧠 GENERANDO MI CONTEXTO (CTX)")
    print("=" * 60)

    # [10%] Obtener número
    ctx_num = get_next_ctx_number()
    print(f"\n[10%] CTX número: {ctx_num}")

    # [30%] Recolectar información
    print("[30%] Recolectando información...")

    fecha = format_date()
    ctx_filename = f"CTX_{ctx_num:03d}_{datetime.now().strftime('%Y-%m-%d')}.md"
    ctx_path = os.path.join(CONTEXT_MEMORY_DIR, ctx_filename)

    # Último CTX anterior
    latest_ctx = get_latest_file(CONTEXT_MEMORY_DIR, "CTX_*.md")
    last_ctx_name = os.path.basename(latest_ctx) if latest_ctx else "Sin CTX previo"

    # Última Process Note
    latest_note = get_latest_file(PROCESS_NOTES_DIR, "*.md")
    last_note_name = os.path.basename(latest_note) if latest_note else "Sin notas"

    # Métricas AIPM
    aipm = get_aipm_metrics()

    # Tareas
    tasks_summary = read_task_summary()

    # [50%] Generar contenido
    print("[50%] Generando contenido...")

    content = f"""# CTX_{ctx_num:03d} — Reporte de Contexto de Sesión

**Fecha:** {fecha}
**Número CTX:** {ctx_num}
**Session ID:** ctx-{datetime.now().strftime("%Y%m%d")}-{ctx_num:03d}

---

## 📊 Estado del Sistema

| Métrica | Valor |
|---------|-------|
| Tareas Activas | {tasks_summary} |
| Trazas AIPM | {aipm["traces"]} |
| Evaluación | {aipm["evaluation"]} |
| Presupuesto | {aipm["budget"]} |

---

## 🔗 Contexto Anterior

- **Último CTX:** {last_ctx_name}
- **Última Nota:** {last_note_name}

---

## 📝 Resumen de la Sesión

*(Completar manualmente o desde el chat)*

### Objetivos Completados
- [ ]

### Problemas Detectados
- [ ]

### Próximos Pasos
- [ ]

---

## 🧠 Decisiones Clave

*(Decisiones importantes tomadas durante la sesión)*

1.

---

## 💡 Aprendizajes

*(Lo que debó recordar para futuras sesiones)*

-

---

## 📚 Archivos Importantes Tocados

*(Rutas de archivos modificados)*

-

---

*Generado automáticamente por CTX Generator - {fecha}*
*Para recuperación: leer completo, especialmente "Decisiones Clave" y "Aprendizajes"*
"""

    # [70%] Escribir archivo
    print("[70%] Escribiendo archivo...")

    try:
        with open(ctx_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"   ✅ Guardado: {ctx_filename}")
    except Exception as e:
        print(f"   ❌ Error: {e}")
        return False

    # [100%] Completado
    print(f"\n[100%] ✅ CTX generado: {ctx_filename}")
    print("=" * 60)

    return True


if __name__ == "__main__":
    generate_ctx()
