---
name: sdd-init
description: >
  Inicializa el contexto Spec-Driven Development (SDD) en cualquier proyecto.
  Úsalo cuando: (1) El usuario dice "sdd init" o "iniciar sdd",
  (2) Se detecta un proyecto nuevo que necesita estructura SDD,
  (3) Se requiere bootstrapping del persistence backend.
  NO usar cuando: Ya existe contexto SDD activo (ver sdd-continue).
author: gentleman-programming
version: 1.0.0
category: 5
tags: [sdd, initialization, workflow]
---

# SDD Init

Inicializa el contexto SDD detectando stack, convenciones y bootstrapping el backend de persistencia.

## Proceso

1. **Detectar Stack**: Analizar package.json, requirements.txt, go.mod, etc.
2. **Identificar Convenciones**: Git flow, naming conventions, estructura de archivos
3. **Seleccionar Backend**: Engram (default) u OpenSpec
4. **Crear Estructura**: Generar directorios para artifacts

## Comandos

```bash
# Inicialización básica
sdd-init --project <nombre>

# Con backend específico
sdd-init --project <nombre> --backend engram|openspec|hybrid
```

## Examples

Ver: [examples/](examples/)

---

**Nota:** Esta skill es el punto de entrada al workflow SDD.
