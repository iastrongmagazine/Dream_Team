# OpenSpec Locations

> **Fecha:** 2026-04-03  
> **Estado:** Actualizado

---

## Ubicaciones de OpenSpec

### Activos (Usar estos)

| Ubicación | Contenido | Uso |
|-----------|-----------|-----|
| `.atl/.atl/openspec/` | SDD activo - configs, changes, specs | **PRINCIPAL** - Cambios actuales |
| `.atl/.atl/openspec/config.yaml` | Configuración SDD del proyecto | Referencia central |
| `.atl/.atl/openspec/changes/` | Cambios SDD en progreso | Cambios activos |
| `.atl/.atl/openspec/specs/` | Specs principales | Specs merged |

### Archivados

| Ubicación | Contenido | Uso |
|-----------|-----------|-----|
| `05_Archive/09_OpenSpec_Archive/.atl/openspec/` | Históricos | Solo lectura, referencia histórica |

---

## Cómo Referenciar

### ✅ Correcto (activos)
```markdown
- Config: `.atl/.atl/openspec/config.yaml`
- Changes: `.atl/.atl/openspec/changes/{change-name}/`
- Specs: `.atl/.atl/openspec/specs/{domain}/spec.md`
```

### ❌ Incorrecto (旧)
```markdown
- .atl/openspec/config.yaml (sin el prefijo .atl/)
- .atl/openspec/changes/...
```

---

## Notas

- **2026-04-03**: `.atl/openspec/` movido de raíz a `.atl/.atl/openspec/` + `05_Archive/09_OpenSpec_Archive/`
- Las referencias antiguas (`.atl/openspec/`) en documentación de externos (Gentleman, repos archived) se mantienen como están - son documentación de esos proyectos
- Solo las referencias DENTRO del proyecto Think_Different deben usar `.atl/.atl/openspec/`

---

*Think Different PersonalOS v6.1*