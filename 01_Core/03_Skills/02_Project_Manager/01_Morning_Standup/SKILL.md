---
name: morning-standup
description: Daily focus session. Triggers on: morning routine, daily priorities, what should I work on, start my day, daily standup, morning planning.
---

# Morning Standup Skill

> Quick 2-minute daily focus session to start the workday.

## Esencia Original
> Based on PersonalOS workflow: "Show me today's priorities" → Pick 1-3 tasks

## When to Use

- First thing in the morning when starting the workday.
- When the user asks "What should I work on today?"
- When feeling overwhelmed and needing to prioritize tasks.

## Workflow (Original)

1. **Read Context**: Read `GOALS.md`, `BACKLOG.md`, and active tasks in `03_Tasks/`.
2. **Analyze Priorities**: Identify top 3 priorities based on deadlines and alignment with goals.
3. **Propose Schedule**: Suggest a realistic plan for the day, highlighting deep work vs. quick wins.
4. **Check Blockers**: Identify any blocked tasks and propose next steps to unblock.

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Proponer más de 3 prioridades
  - **Por qué**: Diluye el foco, defeats the purpose of standup
  - **Solución**: Solo P0 y P1, el resto para después

- **[ERROR]**: Tareas sin owner asignado
  - **Por qué**: Sin responsabilidad, las tareas se estancan
  - **Solución**: Toda tarea debe tener un responsable

- **[ERROR]**: Incluir tareas P3 en el standup
  - **Por qué**: P3 = Nice to have, no es foco diario
  - **Solución**: Solo P0 (crítico) e P1 (importante)

- **[ERROR]**: No verificar tareas bloqueadas
  - **Por qué**: Las tareas bloqueadas pierden momentum
  - **Solución**: Siempre revisar `status: b` antes de proponer nuevo trabajo

- **[ERROR]**: Discusiones largas (>2 min)
  - **Por qué**: El standup debe ser rápido, no una reunión
  - **Solución**: Defer discussions to after standup

---

## 📁 Progressive Disclosure

> Para información detallada, ver:
- [references/priority-guide.md](references/priority-guide.md) — Guía de prioridades P0/P1/P2/P3
- [references/goals-alignment.md](references/goals-alignment.md) — Cómo alinear con GOALS.md
- [references/workflow-examples.md](references/workflow-examples.md) — Ejemplos de standup

---

## 🛠️ Scripts

- [scripts/format-standup.py](scripts/format-standup.py) — Formatea el output del standup
- [scripts/check-blockers.py](scripts/check-blockers.py) — Revisa tareas bloqueadas

---

## 📋 Output Format

```
🎯 THE BIG 3 (Today)

1. [P0] Task Name (est: X min)
   - Why: alineado a GOALS.md

2. [P1] Task Name (est: X min)
   - Why: deadline próximo

3. [P1] Task Name (est: X min)
   - Why: alta impacto

⛔ BLOCKERS: Task X blocked by Y
```

---

## 💾 State Persistence

Esta skill puede guardar un log de sesiones anteriores para comparar días.
