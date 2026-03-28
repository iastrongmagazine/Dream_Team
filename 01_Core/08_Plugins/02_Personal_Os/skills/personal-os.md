---
name: "personal-os"
description: "Activar el modo Think Different PersonalOS - Sistema completo de productividad con goals, backlog, tareas y workflows"
---

# Think Different PersonalOS

Este es el sistema de productividad personal Think Different. Cuando actives esta skill, operás con la metodología del PersonalOS.

## Estructura del Sistema

El PersonalOS tiene la siguiente estructura:

```
├── 00_Winter_is_Coming/    # Goals, Backlog, Agentes
├── 01_Core/               # Skills, Agents, Evals, MCP, Server
├── 02_Knowledge/          # Base de conocimiento
├── 03_Tasks/              # Tareas activas (YAML frontmatter)
├── 04_Operations/         # Memoria, Brain, Notas
├── 05_Archive/           # Archive: Repos, legacy
├── 07_Projects/          # Proyectos
└── 08_Scripts_Os/        # HUBs: Auditor, Git, AIPM, Ritual
```

## Comandos Principales

### Gestión de Tareas

- **"Clear my backlog"** → Procesa el backlog y crea tareas
- **"What should I work on today?"** → Muestra prioridades del día
- **"Show tasks supporting goal [nombre]"** → Lista tareas de una meta

### Workflows SDD

- `/sdd:init` → Inicializar contexto SDD
- `/sdd:new [nombre]` → Crear nueva propuesta
- `/sdd:apply` → Implementar tareas

### Compound Engineering

- `/ce:ideate` → Descubrir mejoras
- `/ce:brainstorm` → Explorar requisitos
- `/ce:plan` → Planes detallados
- `/ce:work` → Ejecutar con worktrees

### System Guardian

- `gr` → Validación dry-run
- `gr --apply` → Aplicar fixes automáticos

## Categorías de Tareas

- **technical**: build, fix, configure
- **outreach**: communicate, meet
- **research**: learn, analyze
- **writing**: draft, document
- **content**: blog posts, social media
- **admin**: operations, finance
- **personal**: health, routines

## Protocolo de Sesión

Al iniciar una nueva sesión:

1. Leer `00_Winter_is_Coming/GOALS.md` → Objetivos
2. Leer `00_Winter_is_Coming/BACKLOG.md` → Tareas pendientes
3. Usar `engram mem_context` → Recuperar contexto previo
4. Reportar resumen antes de actuar

##记忆 (Memoria)

- **engram** → Persistencia entre sesiones
- Guardar decisiones importantes con `engram mem_save`
- Buscar contexto con `engram mem_search`

## metallic (Reglas)

1. NO actuar sin plan aprobado
2. Enumeración correcta de archivos (XX_Nombre.ext)
3. Corrección de errores - documentar antes de actuar
