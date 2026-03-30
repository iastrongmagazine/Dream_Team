---
name: sdd-spec
description: >
  Especifica requisitos con scenarios (delta specs para cambios).
  Úsalo cuando: (1) La proposal está aprobada,
  (2) Se necesitan requisitos detallados,
  (3) Se requieren scenarios de testing.
author: gentleman-programming
version: 1.0.0
category: 5
tags: [sdd, specification, requirements]
---

# SDD Spec

Escribe las especificaciones detalladas del cambio.

## Proceso

1. **Requisitos funcionales**: Qué hace el sistema
2. **Requisitos no funcionales**: Performance, security, etc.
3. **Scenarios**: Casos de uso con Gherkin
4. **Criterios de aceptación**: Definition of Done

## Estructura

```yaml
specs:
  - id: REQ-001
    description: >
      [Requisito funcional]
    acceptance:
      - [Criterio 1]
      - [Criterio 2]

scenarios:
  - id: SCN-001
    description: >
      [Scenario]
    given: [Contexto]
    when: [Acción]
    then: [Resultado]
```

## Examples

Ver: [examples/](examples/)
