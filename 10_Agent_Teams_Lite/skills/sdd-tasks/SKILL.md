---
name: sdd-tasks
description: >
  Desglosa el cambio en checklist de tareas implementables.
  Úsalo cuando: (1) El design está aprobado,
  (2) Se necesita planificar la implementación,
  (3) Se requiere tracking de progreso.
author: gentleman-programming
version: 1.0.0
category: 4
tags: [sdd, tasks, planning]
---

# SDD Tasks

Crea el desglose de tareas para implementar el cambio.

## Proceso

1. **Identificar tareas**: Basado en specs y design
2. **Ordenar dependencias**: Tareas que dependen de otras
3. **Estimación**: Complejidad de cada tarea
4. **Asignación**: Quién hace cada tarea

## Estructura

```yaml
tasks:
  - id: TASK-001
    description: >
      [Descripción de la tarea]
    spec_ref: REQ-001
    design_ref: ADR-001
    dependencies: []
    status: pending|progress|completed

  - id: TASK-002
    description: >
      [Descripción]
    dependencies: [TASK-001]
    status: pending
```

## Examples

Ver: [examples/](examples/)
