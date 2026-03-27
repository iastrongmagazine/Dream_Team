# pyproject.toml
"""
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "mcp-advanced-scaffolder"
version = "2.0.0"
description = "MCP Skill para crear proyectos con arquitectura de tareas coordinadas"
readme = "01_README.md"
requires-python = ">=3.10"
dependencies = [
    "mcp>=0.9.0",
]

[project.scripts]
mcp-scaffold = "mcp_scaffolder.server:main"

[project.optional-dependencies]
dev = [
    "black>=23.0.0",
    "mypy>=1.0.0",
    "pytest>=7.0.0",
]
"""

# requirements.txt
"""
mcp>=0.9.0
"""

# setup.py (alternativa a pyproject.toml)
"""
from setuptools import setup, find_packages

setup(
    name="mcp-advanced-scaffolder",
    version="2.0.0",
    description="MCP Skill para crear proyectos con arquitectura de tareas coordinadas",
    author="Jesús Obando",
    packages=find_packages(),
    install_requires=[
        "mcp>=0.9.0",
    ],
    entry_points={
        'console_scripts': [
            'mcp-scaffold=mcp_scaffolder.server:main',
        ],
    },
    python_requires=">=3.10",
)
"""

# README.md para Python
"""
# Advanced Project Scaffolder MCP Skill (Python)

Skill MCP en Python que implementa las mejores prácticas de Claude Code Tasks.

## Instalación

### Opción 1: Instalación desde código fuente

```bash
# Clonar o crear el proyecto
mkdir mcp-advanced-scaffolder
cd mcp-advanced-scaffolder

# Crear estructura
mkdir mcp_scaffolder
touch mcp_scaffolder/__init__.py
touch mcp_scaffolder/server.py

# Copiar el código del servidor a mcp_scaffolder/server.py

# Crear pyproject.toml (ver contenido arriba)

# Instalar en modo desarrollo
pip install -e .
```

### Opción 2: Usando pip directamente

```bash
pip install mcp>=0.9.0
python server.py
```

## Configuración en Claude Desktop

**Windows:** `%APPDATA%\\Claude\\claude_desktop_config.json`

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "advanced-scaffolder": {
      "command": "python",
      "args": ["-m", "mcp_scaffolder.server"]
    }
  }
}
```

O si instalaste con pip:

```json
{
  "mcpServers": {
    "advanced-scaffolder": {
      "command": "mcp-scaffold"
    }
  }
}
```

## Estructura del Proyecto

```
mcp-advanced-scaffolder/
├── mcp_scaffolder/
│   ├── __init__.py
│   └── server.py          # Código principal
├── pyproject.toml         # Configuración del proyecto
├── requirements.txt       # Dependencias
└── README.md
```

## Uso

Una vez configurado en Claude Desktop:

```
Usuario: "Crea un proyecto llamado mi-app"
Claude: [usa la skill automáticamente]
```

```
Usuario: "Scaffold un proyecto e-commerce con auth y database"
Claude: [crea proyecto con features]
```

```
Usuario: "¿Cuál es el estado de las tareas en ./mi-app?"
Claude: [consulta el DAG de tareas]
```

## Desarrollo

```bash
# Instalar dependencias de desarrollo
pip install -e ".[dev]"

# Formatear código
black mcp_scaffolder/

# Type checking
mypy mcp_scaffolder/

# Tests
pytest
```

## Troubleshooting

### Error: No module named 'mcp'

```bash
pip install mcp>=0.9.0
```

### La skill no aparece en Claude

1. Verifica la ruta en claude_desktop_config.json
2. Asegúrate de que Python esté en el PATH
3. Reinicia Claude Desktop completamente
4. Revisa los logs de MCP

### Error de permisos en Windows

Ejecuta PowerShell como administrador:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Features Disponibles

- `auth`: Next-Auth configurado
- `database`: Prisma setup
- `testing`: Vitest configurado
- `i18n`: Internacionalización

Ejemplo:
```
Crea "mi-app" con auth, database y testing
```

## Ventajas de la Versión Python

- ✅ Más fácil de instalar para usuarios de Python
- ✅ Sin necesidad de Node.js
- ✅ Integración nativa con el ecosistema Python
- ✅ Mismo resultado que la versión TypeScript

## Comparación con TypeScript

| Característica | Python | TypeScript |
|---------------|--------|------------|
| Instalación | pip install | npm install |
| Dependencias | mcp | @modelcontextprotocol/sdk |
| Ejecución | python -m | node |
| Tipado | Type hints | TypeScript |
| Performance | Buena | Excelente |

Ambas versiones generan la misma estructura de proyecto y siguen las mismas prácticas.
"""
