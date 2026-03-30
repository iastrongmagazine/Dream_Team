---
name: skill-registry
description: >
  Mantiene el registro de skills del proyecto.
  Úsalo cuando: (1) Se crea una nueva skill,
  (2) Se actualiza una skill existente,
  (3) Se necesita buscar skills disponibles.
author: gentleman-programming
version: 1.0.0
category: 9
tags: [skills, registry, catalog]
---

# Skill Registry

Gestiona el registro centralizado de skills del proyecto.

## Proceso

1. **Indexar skills**: Escanear directorio de skills
2. **Extraer metadata**: Parsear frontmatter
3. **Generar registry**: Crear archivo indexado
4. **Mantener actualizado**: Sincronizar cambios

## Estructura del Registry

```yaml
registry:
  version: 2.0
  updated: 2026-03-30
  
  skills:
    - name: sdd-init
      path: skills/sdd-init
      category: 5
      tags: [sdd, workflow]
      description: Inicializa contexto SDD
      
    - name: sdd-explore
      path: skills/sdd-explore
      category: 1
      tags: [sdd, research]
      description: Explora ideas
```

## Comandos

```bash
# Actualizar registry
python scripts/update_registry.py

# Buscar skill
grep -r "skill-name" 01_Core/03_Skills/
```

## Examples

Ver: [examples/](examples/)
