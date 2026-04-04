# Proposal: Update Video_Intel Skill (Change #19)

## Intent

Actualizar la skill Video_Intel para integrar persistencia con Engram, documentar explícitamente el workflow de 9 pasos, clarificar el propósito del registro de videos, y consolidar las advertencias (gotchas) conocidas. Esta actualización formaliza features ya implementadas que no estaban documentadas en SKILL.md.

## Scope

### In Scope
- Añadir referencia explícita a Engram con topic_key `unicorn/video-intel-skill`
- Documentar el workflow de 9 pasos en SKILL.md
- Clarificar propósito de `video_registry.py` en documentación
- Documentar migración automática a `02_Knowledge/05_Unicorn/`
- Documentar uso del registro global de videos
- Consolidar gotchas (12 items, vs 8 actuales)

### Out of Scope
- Modificar código de los scripts
- Cambiar estructura de archivos
- Añadir nueva funcionalidad

## Approach

Actualización documentación de SKILL.md únicamente. Los scripts ya implementan estas features; solo faltan documentarlas.

** Cambios específicos:**
1. Añadir sección "Engram Integration" con topic_key
2. Añadir sección "Workflow (9 pasos)" detallando cada fase
3. Añadir sección "Video Registry" explicando `video_registry.py`
4. Añadir sección "Knowledge Migration" documentando `02_Knowledge/05_Unicorn/`
5. Expandir sección "⚠️ Gotchas" de 8 a 12 items

## Affected Areas

| Area | Impact | Description |
|------|--------|-------------|
| `01_Core/03_Skills/19_Video_Intel/SKILL.md` | Modified | Actualización de documentación |
| `01_Core/03_Skills/19_Video_Intel/scripts/video_registry.py` | Documented | Aclarar propósito |
| `02_Knowledge/05_Unicorn/` | Referenced | Destino de migración |

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Documentación desincronizada con código | Low | Revisar contra código existente |
| Gotas faltantes | Low | Validar contra logs de producción |

## Rollback Plan

Revertir cambios en SKILL.md a la versión anterior. No hay cambios de código que afectar.

## Dependencies

- Ninguna dependencia externa
- Requiere acceso a Engram para verificar topic_key existe

## Success Criteria

- [ ] SKILL.md incluye topic_key `unicorn/video-intel-skill`
- [ ] Los 9 pasos del workflow están documentados
- [ ] `video_registry.py` tiene propósito documentado
- [ ] Migración a `02_Knowledge/05_Unicorn/` documentada
- [ ] Gotchas incluyen los 12 items identificados
- [ ] Archivo < 200 líneas (cumplimiento Skill_Auditor)
