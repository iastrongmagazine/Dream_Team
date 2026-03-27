#!/usr/bin/env python3
"""
MCP Skill: Advanced Project Scaffolder (Python)
Implementa las mejores prácticas de Claude Code Tasks
"""

import asyncio
import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent


class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    DONE = "done"
    BLOCKED = "blocked"
    FLAKY = "flaky"


@dataclass
class Task:
    id: str
    name: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
    dependencies: List[str] = field(default_factory=list)
    wave: int = 1


class TaskCoordinator:
    """Coordina la ejecución de tareas con DAG explícito"""

    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self.completed_tasks: set = set()

    def add_task(self, task: Task):
        self.tasks[task.id] = task

    def get_next_task(self) -> Optional[Task]:
        """Obtiene la siguiente tarea disponible"""
        for task in self.tasks.values():
            if (task.status == TaskStatus.PENDING and
                all(dep in self.completed_tasks for dep in task.dependencies)):
                task.status = TaskStatus.IN_PROGRESS
                return task
        return None

    def complete_task(self, task_id: str):
        if task_id in self.tasks:
            self.tasks[task_id].status = TaskStatus.DONE
            self.completed_tasks.add(task_id)

    def get_tasks_by_wave(self, wave: int) -> List[Task]:
        return [t for t in self.tasks.values() if t.wave == wave]

    def get_status(self) -> Dict[str, int]:
        stats = {status.value: 0 for status in TaskStatus}
        for task in self.tasks.values():
            stats[task.status.value] += 1
        return stats


class Templates:
    """Templates para archivos del proyecto"""

    @staticmethod
    def gitignore() -> str:
        return """# Dependencies
/node_modules
/.pnp
.pnp.js

# Next.js
/.next/
/out/

# Production
/build
/dist

# Environment
.env*.local
.env

# IDE
.vscode
.idea

# OS
.DS_Store
Thumbs.db

# TypeScript
*.tsbuildinfo
next-env.d.ts
"""

    @staticmethod
    def package_json(name: str, features: List[str]) -> str:
        deps = {
            "next": "^15.1.0",
            "react": "^19.0.0",
            "react-dom": "^19.0.0",
            "clsx": "^2.1.0",
            "tailwind-merge": "^2.2.0",
        }

        if "auth" in features:
            deps["next-auth"] = "^5.0.0"
        if "database" in features:
            deps["@prisma/client"] = "^5.0.0"

        return json.dumps({
            "name": name,
            "version": "0.1.0",
            "private": True,
            "scripts": {
                "dev": "next dev",
                "build": "next build",
                "start": "next start",
                "lint": "next lint"
            },
            "dependencies": deps,
            "devDependencies": {
                "@types/node": "^20.11.0",
                "@types/react": "^19.0.0",
                "@types/react-dom": "^19.0.0",
                "typescript": "^5.3.0",
                "tailwindcss": "^4.0.0",
                "postcss": "^8.4.0",
                "autoprefixer": "^10.4.0",
                "eslint": "^8.56.0",
                "eslint-config-next": "^15.1.0"
            }
        }, indent=2)

    @staticmethod
    def readme(name: str) -> str:
        return f"""# {name}

Proyecto creado con Advanced Project Scaffolder siguiendo las mejores prácticas de Claude Code.

## Arquitectura de Tareas

Este proyecto implementa un sistema de coordinación explícita:
- Tareas pequeñas y enfocadas
- Contexto fresco por tarea
- DAG explícito de dependencias
- Ejecución en oleadas (waves)

## Estructura

```
{name}/
├── .claude/
│   ├── tasks.json          # DAG de tareas
│   └── settings.json       # Configuración del proyecto
├── src/
│   ├── app/               # Next.js App Router
│   ├── components/        # Componentes React
│   ├── lib/              # Lógica de negocio
│   └── utils/            # Utilidades
├── public/
├── CLAUDE_TASKS.md        # Tracking de tareas
└── README.md
```

## Inicio Rápido

```bash
npm install
npm run dev
```

## Workflow con Claude Code

1. Claude lee `.claude/tasks.json`
2. Identifica la siguiente tarea disponible
3. Ejecuta la tarea en contexto fresco
4. Actualiza el estado en CLAUDE_TASKS.md
5. Pasa a la siguiente tarea

Cada tarea es pequeña, enfocada y consultable.
"""

    @staticmethod
    def tasks_json(name: str) -> str:
        return json.dumps({
            "project": name,
            "tasks": [
                {
                    "id": "task-1",
                    "name": "Crear estructura base",
                    "wave": 1,
                    "dependencies": []
                },
                {
                    "id": "task-2",
                    "name": "Configurar TypeScript",
                    "wave": 1,
                    "dependencies": []
                },
                {
                    "id": "task-3",
                    "name": "Configurar Tailwind",
                    "wave": 2,
                    "dependencies": ["task-1", "task-2"]
                },
                {
                    "id": "task-4",
                    "name": "Crear componentes base",
                    "wave": 2,
                    "dependencies": ["task-3"]
                },
                {
                    "id": "task-5",
                    "name": "Setup testing",
                    "wave": 3,
                    "dependencies": ["task-4"]
                }
            ]
        }, indent=2)

    @staticmethod
    def claude_tasks_md() -> str:
        return """# Claude Code Tasks

## Coordinación Explícita

Este proyecto usa un DAG (Directed Acyclic Graph) para coordinar tareas:

### Wave 1 - Fundación
- ✅ Task A: Crear estructura de carpetas
- ✅ Task B: Configurar TypeScript

### Wave 2 - Configuración
- ⚙️ Task C: Setup Tailwind (depende de A, B)
- ⚙️ Task D: Crear componentes base (depende de C)

### Wave 3 - Features
- ⏳ Task E: Implementar autenticación (depende de D)
- ⏳ Task F: Setup testing (depende de D)

## Estados
- ✅ Done
- ⚙️ In Progress
- ⏳ Pending
- ❌ Blocked
- ⚠️ Flaky

## Reglas
1. Cada tarea se ejecuta en una ventana de contexto fresco
2. Las dependencias son explícitas, no implícitas
3. El progreso es consultable en cualquier momento
4. Las tareas son pequeñas y enfocadas (< 100 líneas)
"""

    @staticmethod
    def tsconfig() -> str:
        return json.dumps({
            "compilerOptions": {
                "target": "ES2020",
                "lib": ["ES2020", "DOM", "DOM.Iterable"],
                "module": "ESNext",
                "skipLibCheck": True,
                "moduleResolution": "bundler",
                "allowImportingTsExtensions": True,
                "resolveJsonModule": True,
                "isolatedModules": True,
                "noEmit": True,
                "jsx": "preserve",
                "strict": True,
                "noUnusedLocals": True,
                "noUnusedParameters": True,
                "noFallthroughCasesInSwitch": True,
                "incremental": True,
                "esModuleInterop": True,
                "paths": {
                    "@/*": ["./src/*"]
                },
                "plugins": [{"name": "next"}]
            },
            "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
            "exclude": ["node_modules"]
        }, indent=2)

    @staticmethod
    def next_config() -> str:
        return """import type { NextConfig } from 'next';

const config: NextConfig = {
  reactStrictMode: true,
  images: {
    domains: [],
  },
  experimental: {
    serverActions: {
      bodySizeLimit: '2mb',
    },
  },
};

export default config;
"""

    @staticmethod
    def tailwind_config() -> str:
        return """import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
      },
    },
  },
  plugins: [],
};

export default config;
"""

    @staticmethod
    def env_example() -> str:
        return """# API Keys
# NEXT_PUBLIC_API_URL=

# Database
# DATABASE_URL=

# Auth (Next-Auth)
# NEXTAUTH_URL=http://localhost:3000
# NEXTAUTH_SECRET=

# Claude Code
# CLAUDE_API_KEY=
"""

    @staticmethod
    def utils_ts() -> str:
        return """import { type ClassValue, clsx } from "clsx";
import { twMerge } from "tailwind-merge";

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

export function formatDate(date: Date): string {
  return new Intl.DateTimeFormat('es-VE', {
    dateStyle: 'long'
  }).format(date);
}

export function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms));
}
"""

    @staticmethod
    def layout_tsx(name: str) -> str:
        return f"""import type {{ Metadata }} from "next";
import "./globals.css";

export const metadata: Metadata = {{
  title: "{name}",
  description: "Proyecto con arquitectura de tareas explícita",
}};

export default function RootLayout({{
  children,
}}: {{
  children: React.ReactNode;
}}) {{
  return (
    <html lang="es">
      <body>{{children}}</body>
    </html>
  );
}}
"""

    @staticmethod
    def page_tsx(name: str) -> str:
        return f"""export default function Home() {{
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="max-w-2xl text-center">
        <h1 className="text-4xl font-bold mb-4">
          {name}
        </h1>
        <p className="text-xl text-gray-600 mb-8">
          Proyecto con arquitectura de tareas coordinadas
        </p>
        <div className="flex gap-4 justify-center">
          <a
            href="/docs"
            className="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            Ver Documentación
          </a>
          <a
            href="/tasks"
            className="px-6 py-3 border border-gray-300 rounded-lg hover:bg-gray-50"
          >
            Ver Tareas
          </a>
        </div>
      </div>
    </main>
  );
}}
"""

    @staticmethod
    def globals_css() -> str:
        return """@tailwind base;
@tailwind components;
@tailwind utilities;

:root {
  --background: #ffffff;
  --foreground: #171717;
}

@media (prefers-color-scheme: dark) {
  :root {
    --background: #0a0a0a;
    --foreground: #ededed;
  }
}

body {
  color: var(--foreground);
  background: var(--foreground);
  font-family: system-ui, -apple-system, sans-serif;
}

@layer utilities {
  .text-balance {
    text-wrap: balance;
  }
}
"""

    @staticmethod
    def mcp_json() -> str:
        return json.dumps({
            "mcpServers": {
                "filesystem": {
                    "command": "npx",
                    "args": ["-y", "@modelcontextprotocol/server-filesystem", "./src"]
                }
            }
        }, indent=2)

    @staticmethod
    def claude_settings(name: str, features: List[str]) -> str:
        return json.dumps({
            "project": name,
            "framework": "next",
            "language": "typescript",
            "styling": "tailwind",
            "features": features,
            "taskCoordination": "explicit",
            "contextStrategy": "fresh-per-task"
        }, indent=2)


async def create_directory(path: Path):
    """Crea un directorio de forma recursiva"""
    path.mkdir(parents=True, exist_ok=True)


async def write_file(path: Path, content: str):
    """Escribe contenido a un archivo"""
    path.write_text(content, encoding="utf-8")


async def scaffold_project(
    project_name: str,
    framework: str = "next",
    styling: str = "tailwind",
    features: Optional[List[str]] = None,
    base_path: Optional[str] = None
) -> str:
    """Crea la estructura completa del proyecto"""

    if features is None:
        features = []

    if base_path is None:
        base_path = os.getcwd()

    project_path = Path(base_path) / project_name

    # Verificar si existe
    if project_path.exists():
        raise FileExistsError(f"El proyecto {project_name} ya existe en {project_path}")

    # Crear estructura de directorios
    directories = [
        project_path,
        project_path / ".claude",
        project_path / "src",
        project_path / "src" / "app",
        project_path / "src" / "app" / "api",
        project_path / "src" / "components",
        project_path / "src" / "components" / "ui",
        project_path / "src" / "lib",
        project_path / "src" / "utils",
        project_path / "public",
        project_path / "public" / "assets",
    ]

    for directory in directories:
        await create_directory(directory)

    # Crear archivos
    files = {
        ".gitignore": Templates.gitignore(),
        "package.json": Templates.package_json(project_name, features),
        "01_README.md": Templates.readme(project_name),
        ".env.local.example": Templates.env_example(),
        "tsconfig.json": Templates.tsconfig(),
        "next.config.ts": Templates.next_config(),
        "tailwind.config.ts": Templates.tailwind_config(),
        ".mcp.json": Templates.mcp_json(),
        "CLAUDE_TASKS.md": Templates.claude_tasks_md(),
        "src/lib/utils.ts": Templates.utils_ts(),
        "src/app/layout.tsx": Templates.layout_tsx(project_name),
        "src/app/page.tsx": Templates.page_tsx(project_name),
        "src/app/globals.css": Templates.globals_css(),
        ".claude/tasks.json": Templates.tasks_json(project_name),
        ".claude/settings.json": Templates.claude_settings(project_name, features),
    }

    for file_name, content in files.items():
        file_path = project_path / file_name
        await write_file(file_path, content)

    features_str = ", ".join(features) if features else "base"

    return f"""✅ Proyecto {project_name} creado con arquitectura de tareas

📊 Estructura creada:
- Sistema de coordinación explícita (DAG)
- Tareas organizadas en oleadas (waves)
- Contexto fresco por tarea
- Tracking en CLAUDE_TASKS.md

🎯 Features: {features_str}

📋 Próximos pasos:
1. cd {project_name}
2. npm install
3. Leer CLAUDE_TASKS.md para ver el DAG de tareas
4. Pedirle a Claude: "Ejecuta la siguiente tarea disponible"

🔄 Cada tarea se ejecuta en una ventana de contexto fresco
📈 El progreso es consultable en cualquier momento
"""


async def get_task_status(project_path: str) -> str:
    """Obtiene el estado actual de las tareas del proyecto"""
    try:
        tasks_file = Path(project_path) / ".claude" / "tasks.json"
        content = tasks_file.read_text(encoding="utf-8")
        tasks = json.loads(content)

        return f"📊 Estado del proyecto:\n\n{json.dumps(tasks, indent=2)}"
    except Exception as e:
        raise Exception(f"Error leyendo estado de tareas: {e}")


# Crear servidor MCP
app = Server("advanced-scaffolder")


@app.list_tools()
async def list_tools() -> list[Tool]:
    """Lista las herramientas disponibles"""
    return [
        Tool(
            name="scaffold_project",
            description="Crea proyecto Next.js con arquitectura de tareas coordinadas (DAG explícito, contexto fresco, ejecución en oleadas)",
            inputSchema={
                "type": "object",
                "properties": {
                    "projectName": {
                        "type": "string",
                        "description": "Nombre del proyecto"
                    },
                    "framework": {
                        "type": "string",
                        "enum": ["next", "react", "astro"],
                        "default": "next"
                    },
                    "styling": {
                        "type": "string",
                        "enum": ["tailwind", "css"],
                        "default": "tailwind"
                    },
                    "features": {
                        "type": "array",
                        "items": {
                            "type": "string",
                            "enum": ["auth", "database", "testing", "i18n"]
                        },
                        "description": "Features opcionales a incluir"
                    },
                    "basePath": {
                        "type": "string",
                        "description": "Ruta base (default: directorio actual)"
                    }
                },
                "required": ["projectName"]
            }
        ),
        Tool(
            name="get_task_status",
            description="Consulta el estado actual de las tareas del proyecto",
            inputSchema={
                "type": "object",
                "properties": {
                    "projectPath": {
                        "type": "string",
                        "description": "Ruta del proyecto"
                    }
                },
                "required": ["projectPath"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Maneja las llamadas a las herramientas"""

    if name == "scaffold_project":
        try:
            result = await scaffold_project(
                project_name=arguments.get("projectName"),
                framework=arguments.get("framework", "next"),
                styling=arguments.get("styling", "tailwind"),
                features=arguments.get("features", []),
                base_path=arguments.get("basePath")
            )
            return [TextContent(type="text", text=result)]
        except Exception as e:
            return [TextContent(type="text", text=f"❌ Error: {str(e)}")]

    elif name == "get_task_status":
        try:
            result = await get_task_status(arguments.get("projectPath"))
            return [TextContent(type="text", text=result)]
        except Exception as e:
            return [TextContent(type="text", text=f"❌ Error: {str(e)}")]

    else:
        raise ValueError(f"Tool desconocido: {name}")


async def main():
    """Punto de entrada principal"""
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
