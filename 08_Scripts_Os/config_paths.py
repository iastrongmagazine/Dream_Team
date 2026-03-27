"""
config_paths.py - Rutas Centralizadas para PersonalOS
====================================================
Este módulo proporciona rutas absolutas a todos los directorios del sistema.
Úsalo en lugar de hardcodear paths relativos.

Uso:
    from config_paths import ROOT_DIR, BRAIN_DIR, ENGINE_DIR
"""

from pathlib import Path
import os


# =============================================================================
# AUTO-DETECCIÓN DE RAÍZ (7 Dimensiones)
# =============================================================================


def find_project_root():
    """Detecta automáticamente la raíz buscando 01_Core (directorio real)"""
    current = Path(__file__).resolve().parent
    # Navegar desde 08_Scripts_Os -> raíz
    project_root = current.parent
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

# 7 Dimensiones del OS
CORE_DIR = ROOT_DIR / "00_Core"
BRAIN_DIR = ROOT_DIR / "01_Brain"
OPERATIONS_DIR = ROOT_DIR / "02_Operations"
KNOWLEDGE_DIR = ROOT_DIR / "03_Knowledge"
ENGINE_DIR = ROOT_DIR / "04_Engine"
SYSTEM_DIR = ROOT_DIR / "05_System"
ARCHIVE_DIR = ROOT_DIR / "06_Archive"
PROJECTS_DIR = ROOT_DIR / "07_Projects"

# =============================================================================
# SUBDIRECTORIOS BRAIN
# =============================================================================

BRAIN_MEMORY_DIR = BRAIN_DIR / "01_Context_Memory"
BRAIN_KNOWLEDGE_DIR = BRAIN_DIR / "02_Knowledge_Brain"
BRAIN_NOTES_DIR = BRAIN_DIR / "03_Process_Notes"
BRAIN_RULES_DIR = BRAIN_DIR / "04_Rules"
BRAIN_TEMPLATE_DIR = BRAIN_DIR / "05_Templates"

# =============================================================================
# SUBDIRECTORIOS OPERATIONS
# =============================================================================

OPERATIONS_TASKS_DIR = OPERATIONS_DIR / "01_Active_Tasks"
OPERATIONS_EVALS_DIR = OPERATIONS_DIR / "02_Evals"
OPERATIONS_ANALYTICS_DIR = OPERATIONS_DIR / "03_Analytics"

# =============================================================================
# SUBDIRECTORIOS ENGINE
# =============================================================================

ENGINE_SCRIPTS_DIR = ENGINE_DIR / "08_Scripts_Os"
ENGINE_TESTS_DIR = ENGINE_DIR / "06_Tests"
ENGINE_COMPOUND_DIR = ENGINE_DIR / "03_Compound_Engine"

# =============================================================================
# SUBDIRECTORIOS KNOWLEDGE
# =============================================================================

KNOWLEDGE_RESEARCH_DIR = KNOWLEDGE_DIR / "01_Research_Knowledge"
KNOWLEDGE_NOTES_DIR = KNOWLEDGE_DIR / "02_Notes_Brain"
KNOWLEDGE_RESOURCES_DIR = KNOWLEDGE_DIR / "03_Resources_External"
KNOWLEDGE_EXAMPLES_DIR = KNOWLEDGE_DIR / "04_Examples_Guide"
KNOWLEDGE_PLANS_DIR = KNOWLEDGE_DIR / "09_Strategic_Plans"

# Alias para scripts que usan PLANS_DIR
PLANS_DIR = KNOWLEDGE_PLANS_DIR

# =============================================================================
# DIRECTORIOS ADICIONALES (usados por scripts específicos)
# =============================================================================

# Brainstorms (deprecated - ahora en 02_Knowledge_Brain si existe)
BRAINSTORMS_DIR = BRAIN_DIR / "02_Knowledge_Brain"

# Compound Engine - ubicacion principal en Every_Sync_Zone
COMPOUND_ENGINE_DIR = (
    PROJECTS_DIR
    / "01_Projects_Lab"
    / "Every_Sync_Zone"
    / "plugins"
    / "compound-engineering"
)

# Ubicacion alternativa en home (skills gentleman)
COMPOUND_ENGINE_HOME_DIR = (
    Path.home() / ".config" / "opencode" / "skills" / "gentleman" / "04_Compound"
)

# =============================================================================
# ALIAS PARA COMPATIBILIDAD (scripts legacy)
# =============================================================================

BASE_DIR = ROOT_DIR  # Alias para scripts que usan BASE_DIR
PROJECT_ROOT = ROOT_DIR  # Alias para scripts que usan PROJECT_ROOT

# =============================================================================
# RUTAS REALES DEL SISTEMA (estructura actual)
# =============================================================================

# Matrix: Goals, Backlog, Agentes (ubicación central)
MATRIX_DIR = ROOT_DIR / "00_Winter_is_Coming"

# Tareas activas (directorio real)
TASKS_DIR = ROOT_DIR / "03_Tasks"

# Evaluaciones (directorio real)
EVALS_DIR = ROOT_DIR / "01_Core" / "02_Evals"

# Server MCP
SERVER_DIR = ROOT_DIR / "01_Core" / "09_Server"

# Alias para compatibilidad con Server.py legacy
MANAGER_AI_BASE_DIR = ROOT_DIR  # Compatibilidad con Server.py

# =============================================================================
# VERIFICACIÓN (para debugging)
# =============================================================================

if __name__ == "__main__":
    print("=== PersonalOS - Rutas Configuradas ===")
    print(f"Validando entorno: PERSONAL_OS_ROOT={os.environ.get('PERSONAL_OS_ROOT')}")
    print(f"ROOT_DIR: {ROOT_DIR}")
    print()
    print("Rutas del Sistema:")
    print(f"  TASKS_DIR: {TASKS_DIR}")
    print(f"  EVALS_DIR: {EVALS_DIR}")
    print(f"  SERVER_DIR: {SERVER_DIR}")
    print(f"  MATRIX_DIR: {MATRIX_DIR}")
    print()
    print("Verificando existencia de directorios...")
    for name, path in [
        ("ROOT", ROOT_DIR),
        ("TASKS", TASKS_DIR),
        ("EVALS", EVALS_DIR),
        ("SERVER", SERVER_DIR),
        ("MATRIX", MATRIX_DIR),
    ]:
        status = "[OK]" if path.exists() else "[FAIL]"
        print(f"  [{status}] {name}: {path}")
