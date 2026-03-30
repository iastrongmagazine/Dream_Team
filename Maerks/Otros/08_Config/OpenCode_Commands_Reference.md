# 📋 Referencia de Comandos y Herramientas de OpenCode

## 🎯 Agentes Disponibles

### Agentes Principales (opencode.json)
| Agente                                | Modo                  | Descripción                                                                        |
|---------------------------------------|-----------------------|------------------------------------------------------------------------------------|
| **gentleman**                         | Primary               | Senior Architect mentor - helpful first, challenging when it matters               |
| **dangerous-gentleman**               | All                   | Full permissions - no restrictions, no questions asked                             |
| **sdd-orchestrator**                  | All                   | Gentleman personality + SDD delegate-only orchestrator                             |

### Agentes del Sistema (Think Different)
- **Orchestrator** (00): Enrutamiento de alto nivel
- **Scope & Rule Architect** (01): Definición de límites técnicos
- **TDD Test First** (02): Ciclos Red-Green-Refactor
- **LFG Autonomous Engine** (12): Ejecución autónoma
- **AIPM Judge** (11): Evaluación de calidad
- **Y más...** (ver 01_Inventario_Total.md)

---

## 🔌 MCPs Disponibles (22 servidores)

### Local ( ejecutados en tu máquina )
| Servidor                     | Comando                                                 | Uso                                           |
|------------------------------|---------------------------------------------------------|-----------------------------------------------|
| **Engram**                   | `engram.exe mcp`                                        | Memoria persistente del sistema               |
| **Playwright**               | `@playwright/mcp@latest`                                | Navegación y testing UI                       |
| **Filesystem**               | `@modelcontextprotocol/server-filesystem`               | Gestión de archivos                           |
| **Exa**                      | `exa-mcp-server`                                        | Búsqueda web en tiempo real                   |
| **Notion**                   | `@notionhq/notion-mcp-server`                           | Base de datos y notas                         |
| **Fireflies**                | `mcp-remote`                                            | Transcripción de reuniones                    |
| **GitHub**                   | (remote)                                                | Integración con GitHub API                    |

### Remotos (acceso via URL)
| Servidor                    | URL                                           |
|-----------------------------|-----------------------------------------------|
| **Context7**                | `https://mcp.context7.com/mcp`                |
| **Eagle-MCP**               | `http://localhost:41596/mcp`                  |
| **Supabase**                | `https://mcp.supabase.com/mcp`                |
| **Linear**                  | `https://mcp.linear.app/mcp`                  |
| **Amplitude**               | `https://mcp.amplitude.com/mcp`               |

---

## ⚙️ Comandos SDD (Spec-Driven Development)

Los comandos SDD se activan con prefijo `/sdd:`

| Comando                             | Skill                          | Función                                       |
|-------------------------------------|--------------------------------|-----------------------------------------------|
| `/sdd:init`                         | `01_Sdd_Init`                  | Inicializar contexto SDD                      |
| `/sdd:explore <tema>`               | `02_Sdd_Explore`               | Explorar código y restricciones               |
| `/sdd:new <nombre>`                 | `03_Sdd_Propose`               | Crear propuesta de cambio                     |
| `/sdd:spec`                         | `04_Sdd_Spec`                  | Escribir especificaciones                     |
| `/sdd:design`                       | `05_Sdd_Design`                | Diseño técnico y arquitectura                 |
| `/sdd:tasks`                        | `06_Sdd_Tasks`                 | Descomponer en tareas                         |
| `/sdd:apply`                        | `07_Sdd_Apply`                 | Implementar tareas                            |
| `/sdd:verify`                       | `08_Sdd_Verify`                | Verificar contra specs                        |
| `/sdd:archive`                      | `09_Sdd_Archive`               | Archivar y cerrar cambio                      |

---

## 🛠️ Skills Disponibles en OpenCode

### Desarrollo Web
- **react-19**: React 19 patterns, hooks, components
- **nextjs-15**: Next.js 15, App Router, Server Components
- **tailwind-4**: Tailwind CSS v4 patterns
- **typescript**: TypeScript patterns, types, generics
- **ai-sdk-5**: Vercel AI SDK 5

### Backend & Data
- **django-drf**: Django REST Framework
- **zod-4**: Zod validation schemas
- **zustand-5**: Zustand state management

### Testing & QA
- **playwright**: Playwright E2E testing
- **pytest**: Python pytest patterns
- **pr-review**: Code review patterns

### SDD & Workflows
- **sdd-init**: Initialize SDD project context
- **sdd-explore**: Explore codebase and approaches
- **sdd-propose**: Create change proposal
- **sdd-spec**: Write delta specifications
- **sdd-design**: Technical design and architecture
- **sdd-tasks**: Break work into implementation tasks
- **sdd-apply**: Implement assigned task batches
- **sdd-verify**: Verify implementation against specs
- **sdd-archive**: Close a change and archive final artifacts

### Utilidades
- **skill-creator**: Create new AI agent skills
- **jira-epic**: Jira epic management
- **jira-task**: Jira task management

---

## 📋 Comandos de Sistema

### Gestión de Tareas
- `/todo-write` - Crear y gestionar lista de tareas
- `/task` - Lanzar sub-agentes para tareas complejas

### Búsqueda y Exploración
- `/websearch` - Buscar en la web con Exa AI
- `/webfetch` - Obtener contenido de URLs
- `/codesearch` - Buscar código y documentación
- `/glob` - Buscar archivos por patrón
- `/grep` - Buscar contenido en archivos

### Archivos
- `/read` - Leer archivos o directorios
- `/write` - Escribir archivos
- `/edit` - Editar contenido existente

### Bash
- `/bash` - Ejecutar comandos bash

### Agentes Especializados
- `/lfg-lite` - Ejecución autónoma ligera
- `/lfg-pro` - Ejecución autónoma avanzada
- `/aipm-judge` - Evaluación de calidad

---

## 🔒 Permisos Configurados

### Bash (restrictivo)
- ✅ Permitido: `*` (todos los comandos)
- ❌ Preguntar: `git commit *`, `git push *`, `git rebase *`, `git reset --hard *`

### Lectura (permitido)
- ✅ Permitido: `*` (todos los archivos)
- ❌ Denegado: `*.env`, `*.env.*`, `**/.env`, `**/.env.*`, `**/secrets/**`, `**/credentials.json`

### Escritura
- ✅ Agentes con herramientas: `write`, `edit`, `bash`

---

## 🎨 Temas y Apariencia

**Tema Gentleman** configurado con:
- Colores: Azul claro (#7FB4CA), Amarillo acento (#E0C15A)
- Fondo: Oscuro (#06080f)
- Sintaxis: Colores diferenciados para código

---

## 📚 Documentación Adicional

- **OpenCode Integration**: `03_Knowledge/OpenCode_Integration.md`
- **Claude Best Practices**: `01_Core/02_Knowledge_Brain/01_Claude_Best_Practices.md`
- **Inventario Total**: `01_Core/02_Knowledge_Brain/01_Inventario_Total.md`

---

## 🚀 Cómo Usar

### Para usar un agente específico:
```
[Agente]: <tu mensaje>
```
Ejemplo: `[Gentleman]: ¿Cómo estructuro este proyecto?`

### Para usar un comando SDD:
```
/sdd:init proyecto-nuevo
```

### Para conectar a un MCP:
```
Usa Exa para buscar información sobre [tema]
```

### Para ver MCPs disponibles:
```
/mcp-list
```

---

**Última actualización**: 2026-03-10
**Sistema**: Think Different AI - OpenCode Integration
