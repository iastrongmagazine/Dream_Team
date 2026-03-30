---
name: sdd-verify
description: >
  Valida que la implementación coincide con specs, design y tareas.
  Úsalo cuando: (1) La implementación está completa,
  (2) Se necesita verificar calidad,
  (3) Se requiere preparar para merge.
author: gentleman-programming
version: 1.0.0
category: 2
tags: [sdd, verification, testing]
---

# SDD Verify

Verifica que la implementación cumple con specs, design y tareas.

## Proceso

1. **Verificar specs**: Cada requirement tiene implementación
2. **Verificar design**: Arquitectura seguida
3. **Verificar tasks**: Todas completadas
4. **Verificar código**: Quality, security, tests
5. **Generar reporte**: Resultados de verificación

## Estructura del Reporte

```yaml
verify_report:
  change: nombre-del-cambio
  
  specs_verification:
    - spec_id: REQ-001
      status: passed|failed
      evidence: [Link a código/tests]
      
  design_verification:
    - decision_id: ADR-001
      status: passed|failed
      
  tasks_verification:
    - total: 6
    - completed: 6
    - pending: 0
    
  code_quality:
    - tests: 15 passed
    - coverage: 85%
    - security: passed
    
  final_status: approved|rejected
```

## Examples

Ver: [examples/](examples/)
