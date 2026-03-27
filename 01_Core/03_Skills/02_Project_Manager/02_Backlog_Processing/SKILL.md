---
name: backlog-processing
description: Organizes notes into tasks. Triggers on: process backlog, triage notes, clear my backlog, organize notes, backlog cleanup.
---

# Backlog Processing Skill

> Turns messy notes into actionable, prioritized tasks.

## Esencia Original
> Based on PersonalOS workflow: "Process my backlog" → Creates prioritized tasks based on GOALS.md

## When to Use

- When `BACKLOG.md` grows too large or messy.
- When the user says "Process my backlog" or "Triage my notes."
- After a long capture session of "frictionless" ideas.
- Weekly during Sunday Ritual.

## Workflow (Original)

1. **Read Backlog**: Scan `00_Winter_is_Coming/BACKLOG.md` for new entries.
2. **Categorize**: Assign items to categories (P0, P1, P2 or Archive).
3. **Deduplicate**: Check for existing tasks in `03_Tasks/` to avoid redundancy.
4. **Draft Tasks**: For P0 and P1 items, create task files in `03_Tasks/`.
5. **Clean Up**: Clear the processed items from `00_Winter_is_Coming/BACKLOG.md`.

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: No usar deduplicación
  - **Por qué**: Crear tasks duplicados pierde tiempo
  - **Solución**: Always check existing tasks before creating new ones

- **[ERROR]**: No asignar priority clara
  - **Por qué**: Tasks sin priority se pierden
  - **Solución**: Always assign P0/P1/P2/P3

- **[ERROR]**: No asignar owner
  - **Por qué**: Tasks sin owner no avanzan
  - **Solución**: Every task needs an owner

- **[ERROR]**: Dejar tareas en Backlog más de 1 semana
  - **Por qué**: El backlog crece sin control
  - **Solución**: Weekly triage obligatorio

- **[ERROR]**: Crear tasks sin validar con usuario
  - **Por qué**: Malinterpretar items del backlog
  - **Solución**: Siempre confirmar antes de crear tareas

---

## 📁 Progressive Disclosure

> Para información detallada, ver:
- [references/dedup-guide.md](references/dedup-guide.md) — Guía de deduplicación
- [references/priority-matrix.md](references/priority-matrix.md) — Matriz de prioridades

---

## 🛠️ Scripts

- [scripts/backlog-triage.py](scripts/backlog-triage.py) — Analiza y sugiere cómo procesar el backlog

---

## 📋 Task Template (Original)

```yaml
---
title: [Actionable task name]
category: [technical|outreach|research|writing|content|admin|personal|other]
priority: [P0|P1|P2|P3]
status: n  # n=not_started (s=started, b=blocked, d=done)
created_date: [YYYY-MM-DD]
due_date: [YYYY-MM-DD]  # optional
estimated_time: [minutes]  # optional
resource_refs:
  - 03_Knowledge/example.md
---

# [Task name]

## Context

Tie to goals and reference material.

## Next Actions

- [ ] Step one
- [ ] Step two

## Progress Log

- YYYY-MM-DD: Notes, blockers, decisions.
```

---

## 💾 State Persistence

Esta skill puede guardar un log deitems procesados para historial.
