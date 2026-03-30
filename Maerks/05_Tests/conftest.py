"""
Fixtures de testing para scripts Python de 04_Operations.

ARMOR LAYER: Los scripts del sistema viven en Legacy_Backup/.
Todos los tests deben importar desde LEGACY_SCRIPTS_DIR.
"""

import pytest
import tempfile
import os
import json
import sys
from pathlib import Path

# ============================================================
# ARMOR LAYER — Ruta centralizada a los scripts del sistema
# ============================================================
# CORREGIDO: ruta correcta desde raíz del proyecto
PROJECT_ROOT = Path(__file__).parent.parent.parent
LEGACY_SCRIPTS_DIR = PROJECT_ROOT / "08_Scripts_Os" / "Legacy_Backup"
sys.path.insert(0, str(LEGACY_SCRIPTS_DIR))
sys.path.insert(0, str(PROJECT_ROOT / "08_Scripts_Os"))


@pytest.fixture
def script_dir():
    """Fixture que expone la ruta a Legacy_Backup para los tests."""
    return LEGACY_SCRIPTS_DIR


@pytest.fixture
def temp_dir():
    """Directorio temporal para tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)


@pytest.fixture
def mock_config(temp_dir):
    """Configuración mock para tests."""
    config = {
        "project": "test-project",
        "active": True,
        "settings": {"debug": False, "verbose": True},
    }
    config_file = temp_dir / "config.json"
    with open(config_file, "w") as f:
        json.dump(config, f)
    return config_file


@pytest.fixture
def mock_environment(monkeypatch, temp_dir):
    """Simula entorno de testing."""
    monkeypatch.setenv("TEST_MODE", "true")
    monkeypatch.setenv("PYTHONUNBUFFERED", "1")
    return temp_dir


@pytest.fixture
def sample_script_content():
    """Contenido de ejemplo para scripts."""
    return """
#!/usr/bin/env python3
import sys

def main():
    print("Script ejecutado correctamente")
    return 0

if __name__ == "__main__":
    sys.exit(main())
"""


def create_mock_script(temp_dir, script_name, content):
    """Helper para crear scripts mock."""
    script_path = temp_dir / script_name
    script_path.write_text(content)
    script_path.chmod(0o755)
    return script_path
