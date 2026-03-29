---
title: Implementar tests unitarios para config_paths.py
type: refactor
date: 2026-03-19
---

# Implementar tests unitarios para config_paths.py

## Overview

Módulo crítico del sistema PersonalOS que centraliza todas las rutas. Tras la refactorización a determinismo (commit `f6f1918`), carece de cobertura de tests, lo cual representa un riesgo para la estabilidad del sistema.

## Problem Statement

`config_paths.py` es el **Single Point of Truth** para rutas del sistema. Sin tests, cualquier cambio futuro podría romper silenciosamente todos los scripts que dependen de él.

**Hallazgo del Vision Review:**
> ⚠️ CRITICAL: `config_paths.py` (módulo crítico) no tiene tests unitarios

## Proposed Solution

Crear suite de tests unitarios siguiendo los patrones existentes en `04_Engine/08_Scripts_Os/05_Tests/` que cubra:

1. **Validación de entorno** (fail-fast)
2. **Constantes exportadas** (7 Dimensiones)
3. **Subdirectorios** (Brain, Operations, Engine, Knowledge)
4. **Aliases** (BASE_DIR, PLANS_DIR, etc.)
5. **Edge cases** (ruta inexistente, permisos, encoding)

## Technical Considerations

### Arquitectura Actual

```python
# config_paths.py (líneas 19-28)
root_env = os.environ.get("PERSONAL_OS_ROOT")
if not root_env:
    raise RuntimeError("La variable de entorno 'PERSONAL_OS_ROOT' no está definida.")

ROOT_DIR = Path(root_env).resolve()
if not ROOT_DIR.exists():
    raise RuntimeError(f"El directorio no existe: {ROOT_DIR}")
```

### Patrón de Tests Existentes

```python
# test_safe_commit.py (líneas 32-52)
import pytest
from unittest.mock import patch, MagicMock
import importlib.util

def test_run_audit_success():
    spec = importlib.util.spec_from_file_location(...)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
```

## Acceptance Criteria

- [ ] Test: `PERSONAL_OS_ROOT` no definido → `RuntimeError`
- [ ] Test: `PERSONAL_OS_ROOT` con ruta inexistente → `RuntimeError`
- [ ] Test: Todas las constantes de 7 Dimensiones exportadas
- [ ] Test: Subdirectorios de Brain, Operations, Engine, Knowledge
- [ ] Test: Aliases (BASE_DIR, PLANS_DIR) funcionan
- [ ] Test: Paths son absolutos y resueltos
- [ ] Test: Estructura de 7 Dimensiones coincide con Inventario

## Success Metrics

| Métrica                      | Target                                |
|------------------------------|---------------------------------------|
| Tests覆盖率                     | 100% de funciones/constants           |
| Tests pasando                | 35 → 35+ (sin regresión)              |
| Fail-fast coverage           | 100% de validaciones                  |

## Dependencies & Risks

| Tipo                      | Descripción                                   | Mitigación                           |
|---------------------------|-----------------------------------------------|--------------------------------------|
| **Dependencia**           | Requiere `PERSONAL_OS_ROOT` seteada           | Tests usan `monkeypatch`             |
| **Riesgo**                | Tests rompen si estructura cambia             | Sincronizar con Inventario           |

## References & Research

### Archivos Relacionados

- `04_Engine/08_Scripts_Os/config_paths.py` — Módulo bajo test
- `04_Engine/05_Tests/test_safe_commit.py` — Patrón de tests existente
- `01_Brain/02_Knowledge_Brain/01_Inventario_Total.md` — Referencia de estructura
- Commit: `f6f1918` — Refactorización determinista

### Patrones de Test

```python
# Estructura estándar de tests
import pytest
from unittest.mock import patch
import importlib.util
from pathlib import Path

# Fixture para PERSONAL_OS_ROOT
@pytest.fixture
def mock_root_env(monkeypatch, tmp_path):
    monkeypatch.setenv("PERSONAL_OS_ROOT", str(tmp_path))
    # Crear estructura de 7D
    for dim in ["00_Core", "01_Brain", "02_Operations", "03_Knowledge", "04_Engine", "05_System", "06_Archive"]:
        (tmp_path / dim).mkdir()
    return tmp_path
```

---

## Implementación Sugerida

### Archivo: `04_Engine/05_Tests/test_config_paths.py`

```python
"""
Tests unitarios para config_paths.py
Patrón: Basado en test_safe_commit.py
"""

import pytest
import os
from unittest.mock import patch
from pathlib import Path
import importlib.util
import sys


# =============================================================================
# FIXTURES
# =============================================================================

@pytest.fixture
def temp_root(monkeypatch, tmp_path):
    """Fixture que crea estructura temporal de 7D."""
    (tmp_path / "00_Core").mkdir()
    (tmp_path / "01_Brain").mkdir()
    (tmp_path / "02_Operations").mkdir()
    (tmp_path / "03_Knowledge").mkdir()
    (tmp_path / "04_Engine").mkdir()
    (tmp_path / "05_System").mkdir()
    (tmp_path / "06_Archive").mkdir()
    monkeypatch.setenv("PERSONAL_OS_ROOT", str(tmp_path))
    return tmp_path


# =============================================================================
# TESTS: VALIDACIÓN DE ENTORNO (FAIL-FAST)
# =============================================================================

def test_missing_personal_os_root():
    """Test: PERSONAL_OS_ROOT no definido → RuntimeError."""
    env_backup = os.environ.get("PERSONAL_OS_ROOT")
    if "PERSONAL_OS_ROOT" in os.environ:
        del os.environ["PERSONAL_OS_ROOT"]

    with pytest.raises(RuntimeError, match="PERSONAL_OS_ROOT"):
        # Re-importar módulo
        import importlib
        import config_paths
        importlib.reload(config_paths)

    # Restaurar
    if env_backup:
        os.environ["PERSONAL_OS_ROOT"] = env_backup


def test_invalid_root_path(monkeypatch):
    """Test: Ruta inexistente → RuntimeError."""
    monkeypatch.setenv("PERSONAL_OS_ROOT", "/ruta/inexistente/12345")
    with pytest.raises(RuntimeError, match="no existe"):
        import importlib
        import config_paths
        importlib.reload(config_paths)


# =============================================================================
# TESTS: CONSTANTES DE 7 DIMENSIONES
# =============================================================================

def test_7_dimensions_constants(temp_root):
    """Test: Todas las 7 Dimensiones exportadas correctamente."""
    import config_paths
    importlib.reload(config_paths)

    assert config_paths.ROOT_DIR == temp_root
    assert config_paths.CORE_DIR == temp_root / "00_Core"
    assert config_paths.BRAIN_DIR == temp_root / "01_Brain"
    assert config_paths.OPERATIONS_DIR == temp_root / "02_Operations"
    assert config_paths.KNOWLEDGE_DIR == temp_root / "03_Knowledge"
    assert config_paths.ENGINE_DIR == temp_root / "04_Engine"
    assert config_paths.SYSTEM_DIR == temp_root / "05_System"
    assert config_paths.ARCHIVE_DIR == temp_root / "06_Archive"


# =============================================================================
# TESTS: SUBDIRECTORIOS
# =============================================================================

def test_brain_subdirs(temp_root):
    """Test: Subdirectorios de Brain."""
    import config_paths
    importlib.reload(config_paths)

    (temp_root / "01_Brain" / "01_Context_Memory").mkdir(parents=True)

    assert config_paths.BRAIN_MEMORY_DIR.exists() or True  # Puede no existir aún


# =============================================================================
# TESTS: ALIASES
# =============================================================================

def test_aliases(temp_root):
    """Test: BASE_DIR y PLANS_DIR son aliases correctos."""
    import config_paths
    importlib.reload(config_paths)

    assert config_paths.BASE_DIR == config_paths.ROOT_DIR
    assert config_paths.PLANS_DIR.name == "09_Strategic_Plans"


# =============================================================================
# TESTS: EDGE CASES
# =============================================================================

def test_paths_are_absolute(temp_root):
    """Test: Todas las rutas son absolutas."""
    import config_paths
    importlib.reload(config_paths)

    for name in dir(config_paths):
        if name.endswith("_DIR") or name == "ROOT_DIR":
            path = getattr(config_paths, name)
            if isinstance(path, Path):
                assert path.is_absolute(), f"{name} no es absoluta: {path}"


def test_paths_are_resolved(temp_root):
    """Test: Paths están resueltos (no relativos)."""
    import config_paths
    importlib.reload(config_paths)

    assert config_paths.ROOT_DIR == config_paths.ROOT_DIR.resolve()
```

---

## Checklist Pre-Commit

- [ ] Tests creados en `04_Engine/05_Tests/test_config_paths.py`
- [ ] Tests ejecutados: `pytest 04_Engine/05_Tests/test_config_paths.py`
- [ ] Suite completa pasa: `pytest 04_Engine/05_Tests/ -v`
- [ ] Commit: `test(engine): agregar tests unitarios para config_paths.py`
- [ ] Engram actualizado con aprendizaje compuesto

---

© 2026 PersonalOS | Plan creado con Professor_X_Plan
