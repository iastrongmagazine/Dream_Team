# Advanced Project Scaffolder MCP Skill

Skill que implementa las mejores prácticas de Claude Code Tasks para crear proyectos con arquitectura de coordinación explícita.

## Principios Implementados

### 1. Coordinación Explícita (No Implícita)
- **DAG visible**: Todas las dependencias entre tareas están en `.claude/tasks.json`
- **Estados claros**: Cada tarea tiene un estado consultable (pending, in_progress, done, blocked, flaky)
- **Sin coordinación implícita**: No se asume orden en el chat, todo es explícito

### 2. Colaboración Nativa
- **Múltiples sesiones**: Cada tarea se ejecuta en contexto fresco
- **Progreso consultable**: Claude puede preguntar "¿qué está bloqueado?" en cualquier momento
- **Handoffs claros**: Una sesión termina una tarea, la siguiente toma la próxima

### 3. Tareas Pequeñas y Enfocadas
- **Tareas < 100 líneas**: Cada tarea es pequeña y manejable
- **Una responsabilidad**: Cada tarea hace una cosa bien
- **Contexto fresco**: Nueva ventana de contexto por tarea

### 4. Ejecución en Oleadas (Waves)
- **Wave 1**: Fundación (estructura, configs base)
- **Wave 2**: Configuración (Tailwind, componentes)
- **Wave 3**: Features (auth, testing, etc.)

## Instalación

### 1. Crear proyecto de la skill

```bash
mkdir mcp-advanced-scaffolder
cd mcp-advanced-scaffolder
```

### 2. Crear estructura

```
mcp-advanced-scaffolder/
├── src/
│   └── index.ts
├── package.json
└── tsconfig.json
```

### 3. Copiar archivos

**package.json:**
```json
{
  "name": "mcp-advanced-scaffolder",
  "version": "2.0.0",
  "type": "module",
  "main": "dist/index.js",
  "bin": {
    "mcp-scaffold": "./dist/index.js"
  },
  "scripts": {
    "build": "tsc",
    "dev": "tsc --watch"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^1.0.0"
  },
  "devDependencies": {
    "@types/node": "^20.11.0",
    "typescript": "^5.3.0"
  }
}
```

**tsconfig.json:**
```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true
  },
  "include": ["src/**/*"]
}
```

### 4. Compilar e instalar

```bash
npm install
npm run build
npm link
```

### 5. Configurar en Claude Desktop

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "advanced-scaffolder": {
      "command": "mcp-scaffold"
    }
  }
}
```

Reinicia Claude Desktop.

## Uso

### Crear un proyecto básico

```
Crea un proyecto llamado "mi-app"
```

### Crear con features específicos

```
Scaffold un proyecto "e-commerce" con auth y database
```

### Consultar estado de tareas

```
¿Cuál es el estado de las tareas en ./mi-app?
```

## Estructura Generada

```
mi-proyecto/
├── .claude/
│   ├── tasks.json         # DAG explícito de tareas
│   └── settings.json      # Configuración del proyecto
├── src/
│   ├── app/
│   │   ├── globals.css
│   │   ├── layout.tsx
│   │   └── page.tsx
│   ├── components/
│   │   └── ui/           # Componentes reutilizables
│   ├── lib/
│   │   └── utils.ts
│   └── utils/
├── public/
│   └── assets/
├── .gitignore
├── .mcp.json             # Config MCP
├── CLAUDE_TASKS.md       # Tracking visual de tareas
├── package.json
├── tsconfig.json
├── next.config.ts
├── tailwind.config.ts
└── README.md
```

## Workflow con Claude Code

### Fase 1: Scaffolding
```
Usuario: "Crea un proyecto llamado portfolio"
Claude: [usa la skill, genera estructura]
```

### Fase 2: Ejecución de Tareas
```
Usuario: "Ejecuta la siguiente tarea disponible"
Claude: [lee .claude/tasks.json]
Claude: "Voy a ejecutar Task 1: Crear estructura base"
Claude: [ejecuta en contexto fresco]
Claude: [actualiza CLAUDE_TASKS.md]
```

### Fase 3: Consulta de Estado
```
Usuario: "¿Qué tareas están bloqueadas?"
Claude: [lee .claude/tasks.json]
Claude: "Task C está bloqueada esperando Task B"
```

### Fase 4: Continuación
```
Usuario: "Continúa con la siguiente"
Claude: [identifica siguiente tarea disponible]
Claude: [ejecuta en contexto fresco]
```

## Archivos Clave

### `.claude/tasks.json` - DAG Explícito
```json
{
  "project": "mi-app",
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
      "name": "Setup Tailwind",
      "wave": 2,
      "dependencies": ["task-1", "task-2"]
    }
  ]
}
```

### `CLAUDE_TASKS.md` - Tracking Visual
```markdown
## Wave 1 - Fundación
- ✅ Task A: Crear estructura
- ✅ Task B: Config TypeScript

## Wave 2 - Configuración
- ⚙️ Task C: Setup Tailwind
- ⏳ Task D: Componentes base

## Estados
- ✅ Done
- ⚙️ In Progress
- ⏳ Pending
- ❌ Blocked
- ⚠️ Flaky
```

## Features Disponibles

La skill soporta estos features opcionales:

- **auth**: Next-Auth configurado
- **database**: Prisma setup
- **testing**: Vitest configurado
- **i18n**: Internacionalización

Ejemplo:
```
Crea "mi-app" con auth, database y testing
```

## Ventajas vs Script Tradicional

| Script Tradicional     | Advanced Skill            |
| ---------------------- | ------------------------- |
| Una ejecución grande   | Múltiples tareas pequeñas |
| Contexto único         | Contexto fresco por tarea |
| Sin tracking           | Estado consultable        |
| Coordinación implícita | DAG explícito             |
| Difícil parallelizar   | Waves naturales           |

## Comandos Útiles

```bash
# Ver logs de Claude Desktop (para debug)
# Windows
Get-Content "$env:APPDATA\Claude\logs\mcp*.log" -Wait

# Ver tareas del proyecto
cat .claude/tasks.json

# Ver tracking visual
cat CLAUDE_TASKS.md
```

## Troubleshooting

### La skill no aparece
1. Verifica instalación: `which mcp-scaffold` (Unix) o `where mcp-scaffold` (Windows)
2. Revisa config: `%APPDATA%\Claude\claude_desktop_config.json`
3. Reinicia Claude Desktop completamente
4. Revisa logs de MCP

### Error al crear proyecto
- Asegúrate que no existe el directorio
- Verifica permisos de escritura
- Comprueba que Node.js >= 18

### Tareas no se actualizan
- Verifica que `.claude/tasks.json` sea JSON válido
- Asegúrate de tener permisos de escritura
- Revisa que CLAUDE_TASKS.md no tenga conflictos

## Próximas Mejoras

- [ ] Sistema de rollback por tarea
- [ ] Métricas de tiempo por tarea
- [ ] Detección automática de tareas bloqueadas
- [ ] Sugerencias de paralelización
- [ ] Templates de tareas customizables
- [ ] Integración con Git (branch por tarea)

## Recursos

- [Claude Code Tasks](https://www.anthropic.com/engineering)
- [MCP Documentation](https://modelcontextprotocol.io)
- [Best Practices](https://docs.anthropic.com/claude/docs)
