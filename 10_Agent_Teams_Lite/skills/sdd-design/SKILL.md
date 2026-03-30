---
name: sdd-design
description: >
  Crea diseño técnico con decisiones de arquitectura.
  Úsalo cuando: (1) Las specs están definidas,
  (2) Se necesita detallar la implementación técnica,
  (3) Se requieren decisiones de arquitectura.
author: gentleman-programming
version: 1.0.0
category: 5
tags: [sdd, design, architecture]
---

# SDD Design

Documenta las decisiones técnicas y arquitectura del cambio.

## Proceso

1. **Arquitectura**: Componentes y relaciones
2. **Data Model**: Esquemas de DB, tipos
3. **API Design**: Endpoints, contratos
4. **Tech Decisions**: Librerías, patrones

## Estructura

```yaml
architecture:
  components:
    - name: [Componente]
      responsibility: [Responsabilidad]
      dependencies: [Dependencias]

data_model:
  - entity: [Entidad]
    fields:
      - name: [Campo]
        type: [Tipo]

api:
  - endpoint: /api/endpoint
    method: GET|POST|PUT|DELETE
    request: [Schema]
    response: [Schema]

decisions:
  - id: ADR-001
    title: "[Título]"
    decision: "[Decisión]"
    rationale: "[Por qué]"
```

## Examples

Ver: [examples/](examples/)
