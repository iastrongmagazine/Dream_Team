---
name: sdd-apply
description: >
  Implementa tareas escribiendo código real siguiendo specs y design.
  Úsalo cuando: (1) Las tasks están definidas,
  (2) Se va a escribir código,
  (3) Se necesita mantener trazabilidad.
author: gentleman-programming
version: 1.0.0
category: 5
tags: [sdd, implementation, code]
---

# SDD Apply

Ejecuta las tareas de implementación siguiendo specs y design.

## Proceso

1. **Seleccionar tarea**: Tomar tarea pending
2. **Verificar contexto**: Leer spec y design relevantes
3. **Implementar**: Escribir código
4. **Verificar**: 确保 matching con spec
5. **Actualizar estado**: Marcar tarea completada

## Reglas

- **NUNCA** implementar features fuera de scope
- **SIEMPRE** referenciar spec/design en commits
- **MANTENER** trazabilidad en apply-progress

## Examples

Ver: [examples/](examples/)
