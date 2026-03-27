---
name: best-practices
description: Project scaffolding and architecture patterns. Triggers on: best practices, project setup, scaffolding, architecture, DAG, atomic tasks, project structure, coordination patterns.
---

# Best Practices & Advanced Scaffolding 🏆

> Implement explicit coordination architectures and task-based scaffolding using DAGs.

## Esencia Original
> Advanced skill for complex project coordination using atomic tasks and wave-based execution.

## 🎯 Objetivo

Eliminate implicit coordination and context errors through **DAG-based** project structures, atomic tasks, and wave execution.

## When to Use

- Setting up new complex projects
- Coordinating multi-phase implementations
- When you need explicit task tracking
- Building scalable architectures

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: No tracking of task dependencies
  - **Por qué**: Sin DAG, las tareas se ejecutan sin orden
  - **Solución**: Usar `tasks.json` con dependencias explícitas

- **[ERROR]**: Tareas demasiado grandes
  - **Por qué**: Tasks > 100 líneas acumulan deuda técnica
  - **Solución**: Dividir en tareas atómicas

- **[ERROR]**: No validation hooks
  - **Por qué**: Errors pasan desapercibidos
  - **Solución**: Usar hooks de stop/post-tool

- **[ERROR]**: Contexto acumulado (context drift)
  - **Por qué**: Sesiones largas = alucinaciones
  - **Solución**: Tratar cada tarea como sesión independiente

- **[ERROR]**: No auto-healing
  - **Por qué**: Errores de config no se detectan
  - **Solución**: Implementar self-healing checks

---

## 📁 Progressive Disclosure

> Para información detallada:
- [references/dag-guide.md](references/dag-guide.md) — Guía de DAGs
- [references/wave-execution.md](references/wave-execution.md) — Ejecución por olas
- [references/atomic-tasks.md](references/atomic-tasks.md) — Tareas atómicas

---

## 🛠️ Scripts

- [scripts/python_mcp_skill1.py](scripts/python_mcp_skill1.py) — MCP server para scaffolding
- [scripts/python_setup_files1.py](scripts/python_setup_files1.py) — Configuración de entornos

---

## 🔄 Workflow (Original)

### Wave 1: Fundación
- Definir estructura de carpetas mínima
- Configurar `tasks.json` con el DAG
- Establecer reglas de blindaje

### Wave 2: Configuración
- Inyectar dependencias core
- Establecer hooks de validación

### Wave 3: Ejecución
- Procesar tareas de forma atómica (< 100 líneas por cambio)
- Validar en cada paso

---

## 💾 State Persistence

Guardar estado del proyecto en:
- `${CLAUDE_PLUGIN_DATA}/best-practices/projects/`
- O en `projects/` local
