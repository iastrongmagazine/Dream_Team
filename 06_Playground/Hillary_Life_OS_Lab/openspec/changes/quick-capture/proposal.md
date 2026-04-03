# Proposal: Quick Capture Skill (Fase 1)

## Intent

Crear una skill de captura de tareas sin fricción que funcione como primer paso del sistema de Hillary. El objetivo es permitir capturar cualquier tarea, idea o recordatorio de forma inmediata, sin setup complejo, guardando en inbox como markdown con YAML frontmatter.

## Scope

### In Scope
- Skill `01_Quick_Capture/SKILL.md` con workflow input → process → save
- Carpeta `01_Quick_Capture/inbox/` para almacenar capturas
- Formato Markdown con frontmatter (timestamp, source, tags)
- Ejemplo de uso documentado

### Out of Scope
- APIs externas o integraciones
- Categorización automática de tareas
- Sistema de prioridades o fechas
- Interfaz GUI (solo CLI/skill)

## Approach

Usar estructura simple de skill:
1. **Input**: Recibir texto libre de tarea
2. **Process**: Agregar metadata (timestamp ISO 8601, source: manual, tags[])
3. **Save**: Escribir archivo `.md` en `inbox/` con nombre basado en timestamp

Formato de archivo:
```markdown
---
created: 2026-03-31T12:00:00Z
source: manual
tags: []
---

# Tarea: [título]

[contenido original]
```

## Affected Areas

| Area                                                          | Impact   | Description                       |
|---------------------------------------------------------------|----------|-----------------------------------|
| `06_Playground/Hillary_Life_OS_Lab/01_Quick_Capture/SKILL.md` | New      | Skill principal de captura        |
| `06_Playground/Hillary_Life_OS_Lab/01_Quick_Capture/inbox/`   | New      | Directorio para tareas capturadas |
| `.atl/openspec/changes/quick-capture/proposal.md`                  | New      | Este documento                    |

## Risks

| Risk                        | Likelihood   | Mitigation                                |
|-----------------------------|--------------|-------------------------------------------|
| Nombre de archivo duplicado | Low          | Usar timestamp único en nombre de archivo |
| YAML inválido               | Low          | Validar frontmatter antes de escribir     |

## Rollback Plan

1. Eliminar carpeta `01_Quick_Capture/`
2. Eliminar `.atl/openspec/changes/quick-capture/`
3. No hay impacto en sistema existente (skill nueva)

## Dependencies

- Ninguna dependencia externa
- Solo requiere sistema de archivos local

## Success Criteria

- [ ] Skill `01_Quick_Capture/SKILL.md` existe y es ejecutable
- [ ] Carpeta `inbox/` creada
- [ ] Captura de tarea genera archivo `.md` válido
- [ ] Frontmatter contiene timestamp, source, tags
- [ ] Ejemplo de uso documentado
