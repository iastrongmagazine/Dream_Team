---
name: sdd-propose
description: >
  Crea una propuesta de cambio con intent, scope y approach.
  Úsalo cuando: (1) Se necesita documentar un cambio planned,
  (2) El usuario quiere formalizar una idea,
  (3) Se requiere aprobación antes de proceder.
author: gentleman-programming
version: 1.0.0
category: 4
tags: [sdd, proposal, planning]
---

# SDD Propose

Crea el documento de propuesta formal para un cambio.

## Proceso

1. **Intent**: Por qué hacemos este cambio
2. **Scope**: Qué incluye y qué NO incluye
3. **Approach**: Cómo lo vamos a lograr
4. **Risks**: Riesgos identificados y mitigaciones

## Estructura del Proposal

```yaml
change: nombre-del-cambio
intent: >
  [Descripción del problema o oportunidad]
scope:
  in:
    - [Feature 1]
    - [Feature 2]
  out:
    - [Feature NO incluida]
approach:
  - Paso 1
  - Paso 2
risks:
  - [Riesgo 1]: [Mitigación]
```

## Examples

Ver: [examples/](examples/)
