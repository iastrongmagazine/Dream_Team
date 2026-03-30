---
name: sdd-archive
description: >
  Sincroniza specs delta a specs main y archiva el cambio completado.
  Úsalo cuando: (1) Verificación aprobada,
  (2) Se necesita consolidar el cambio,
  (3) Se prepara para cerrar el ciclo.
author: gentleman-programming
version: 1.0.0
category: 4
tags: [sdd, archive, consolidation]
---

# SDD Archive

Archiva el cambio completado sincronizando artifacts a specs main.

## Proceso

1. **Merge specs**: Copiar specs del change a specs main
2. **Merge design**: Actualizar architecture decision records
3. **Cleanup**: Limpiar artifacts temporales
4. **Generar reporte**: Resumen del cambio completado

## Estructura

```yaml
archive_report:
  change: nombre-del-cambio
  status: completed
  
  artifacts_merged:
    - specs/auth/spec.md
    - design/auth/adr.md
    
  summary:
    - features_added: 5
    - bugs_fixed: 0
    - breaking_changes: none
    
  lessons_learned:
    - [Lección 1]
    - [Lección 2]
    
  next_steps:
    - [Recomendación para futuro]
```

## Examples

Ver: [examples/](examples/)
