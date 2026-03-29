# Migración de Rutas Think Different v6.1

**Fecha:** 2026-03-27
**Estado:** En Progreso

## Resumen

Se está actualizando todas las referencias a carpetas obsoletas en el PersonalOS para adoptar la estructura v6.1.

## ✅ Completado

### Commits realizados:
1. **fix: update routes to Think Different v6.1 structure** - 35 files
2. **fix: update routes in 01_Core/00_Workflows to v6.1** - 14 files
3. **fix: remaining routes in 00_Workflows** - 5 files

### Carpetas corregidas:
- `00_Winter_is_Coming/`
- `.agent/03_Workflows/`
- `01_Core/00_Workflows/`
- Scripts en `08_Scripts_Os/Legacy_Backup/`
- Hooks en `.agent/` y `01_Core/`

## 🔲 Pendiente

| Carpeta | Estado | Rutas |
|---------|--------|-------|
| `01_Core/03_Agents/` | Parcial | ~30 |
| `01_Core/03_Skills/` | Pendiente | ~600 |
| `01_Core/05_Mcp/` | Pendiente | ~10 |
| `01_Core/01_Inventario_Total.md` | Pendiente | ~20 |

## Mapa de Reemplazos

| Vieja | Nueva |
|-------|-------|
| `.cursor/00_Rules/` | `01_Core/01_Rules/` |
| `01_Brain/Context_Memory/` | `04_Operations/00_Context_Memory/` + Engram |
| `01_Brain/Process_Notes/` | `04_Operations/03_Process_Notes/` + Engram |
| `01_Brain/07_Memory_Brain/` | `04_Operations/04_Memory_Brain/` + Engram |
| `02_Operations/Tasks/` | `03_Tasks/` |
| `00_Core/GOALS.md` | `00_Winter_is_Coming/GOALS.md` |
| `04_Engine/` | `08_Scripts_Os/` |
| `docs/brainstorms/` | `04_Operations/07_Brain_Storming/` |
| `docs/plans/` | `04_Operations/05_Plans/` |
| `docs/solutions/` | `04_Operations/06_Solutions/` |

## Estructura v6.1

```
Think_Different/
├── 00_Winter_is_Coming/  # GOALS, BACKLOG
├── 01_Core/              # Fuente de la verdad
├── 02_Knowledge/
├── 03_Tasks/
├── 04_Operations/        # Context, Notes, Plans, Solutions
├── 05_Archive/
├── 08_Scripts_Os/
└── .agent/
```

## Notas Importantes

- **Fuente de la verdad:** `01_Core/` SOLO
- **.agent/** es espejo de `01_Core/`
- **Memoria:** Engram (`mem_search`, `mem_save`)
