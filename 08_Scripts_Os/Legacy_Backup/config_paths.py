"""
config_paths.py - Rutas Centralizadas para PersonalOS
====================================================
Este módulo proporciona rutas absolutas a todos los directorios del sistema.
Úsalo en lugar de hardcodear paths relativos.

Uso:
    from config_paths import ROOT_DIR, TASKS_DIR, SERVER_DIR
"""

from pathlib import Path
import os


# =============================================================================
# AUTO-DETECCIÓN DE RAÍZ (estructura real)
# =============================================================================


def find_project_root():
    """Detecta automáticamente la raíz buscando 01_Core (directorio real)"""
    current = Path(__file__).resolve().parent
    # Navegar desde Legacy_Backup -> 08_Scripts_Os -> raíz
    project_root = current.parent.parent
    if (project_root / "01_Core").exists():
        return project_root
    return None


# Intentar con env var primero
root_env = os.environ.get("PERSONAL_OS_ROOT")
if root_env:
    ROOT_DIR = Path(root_env).resolve()
else:
    # Auto-detectar
    ROOT_DIR = find_project_root()

if not ROOT_DIR or not ROOT_DIR.exists():
    raise RuntimeError(
        "No se pudo detectar la raíz del proyecto. "
        "Define la variable 'PERSONAL_OS_ROOT' o asegúrate de que existe 01_Core."
    )

# =============================================================================
# ESTRUCTURA REAL DEL SISTEMA
# =============================================================================

# Matrix: Goals, Backlog, Agentes (ubicación central)
MATRIX_DIR = ROOT_DIR / "00_Winter_is_Coming"

# Core del sistema
CORE_DIR = ROOT_DIR / "01_Core"

# Knowledge
KNOWLEDGE_DIR = ROOT_DIR / "02_Knowledge"

# Tareas activas (directorio real)
TASKS_DIR = ROOT_DIR / "03_Tasks"

# Operations (Memory, Brain, Notes)
OPERATIONS_DIR = ROOT_DIR / "04_Operations"

# Archive
ARCHIVE_DIR = ROOT_DIR / "05_Archive"

# Projects
PROJECTS_DIR = ROOT_DIR / "07_Projects"

# Engine (legacy - ahora es 08_Scripts_Os)
ENGINE_DIR = ROOT_DIR / "08_Scripts_Os"

# System (ahora en 01_Core)
SYSTEM_DIR = ROOT_DIR / "01_Core"

# Scripts
SCRIPTS_DIR = ROOT_DIR / "08_Scripts_Os"

# =============================================================================
# SUBDIRECTORIOS CORE
# =============================================================================

CORE_AGENTS_DIR = CORE_DIR / "03_Agents"
CORE_SKILLS_DIR = CORE_DIR / "03_Skills"
CORE_EVALS_DIR = CORE_DIR / "02_Evals"
CORE_MCP_DIR = CORE_DIR / "05_Mcp"
CORE_SERVER_DIR = CORE_DIR / "09_Server"

# =============================================================================
# SUBDIRECTORIOS OPERATIONS
# =============================================================================

OPERATIONS_MEMORY_DIR = OPERATIONS_DIR / "01_Context_Memory"
OPERATIONS_BRAIN_DIR = OPERATIONS_DIR / "02_Knowledge_Brain"
OPERATIONS_NOTES_DIR = OPERATIONS_DIR / "03_Process_Notes"
OPERATIONS_MEMORY_MAP_DIR = OPERATIONS_DIR / "04_Memory_Brain"

# Alias legacy
OPERATIONS_TASKS_DIR = TASKS_DIR  # Compatibilidad
OPERATIONS_EVALS_DIR = CORE_EVALS_DIR  # Compatibilidad

# =============================================================================
# ALIAS PARA COMPATIBILIDAD (scripts legacy)
# =============================================================================

BASE_DIR = ROOT_DIR  # Alias para scripts que usan BASE_DIR
PROJECT_ROOT = ROOT_DIR  # Alias para scripts que usan PROJECT_ROOT
BRAIN_DIR = OPERATIONS_DIR  # Alias legacy (Operations ahora es el Brain)

# =============================================================================
# VERIFICACIÓN (para debugging)
# =============================================================================

if __name__ == "__main__":
    print("=== PersonalOS - Rutas Configuradas (Legacy) ===")
    print(f"Validando entorno: PERSONAL_OS_ROOT={os.environ.get('PERSONAL_OS_ROOT')}")
    print(f"ROOT_DIR: {ROOT_DIR}")
    print()
    print("Rutas del Sistema:")
    print(f"  TASKS_DIR: {TASKS_DIR}")
    print(f"  CORE_DIR: {CORE_DIR}")
    print(f"  OPERATIONS_DIR: {OPERATIONS_DIR}")
    print(f"  MATRIX_DIR: {MATRIX_DIR}")
    print()
    print("Verificando existencia de directorios...")
    for name, path in [
        ("ROOT", ROOT_DIR),
        ("TASKS", TASKS_DIR),
        ("CORE", CORE_DIR),
        ("OPERATIONS", OPERATIONS_DIR),
        ("MATRIX", MATRIX_DIR),
    ]:
        status = "[OK]" if path.exists() else "[FAIL]"
        print(f"  [{status}] {name}: {path}")
