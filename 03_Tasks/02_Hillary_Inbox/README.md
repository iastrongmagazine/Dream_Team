# 02_Hillary_Inbox — Quick Capture Inbox

> **Propósito:** Inbox de capturas del skill Quick Capture (Hillary Life OS)  
> **Skill fuente:** `01_Core/03_Skills/18_Personal_Life_OS/01_Quick_Capture/`  
> **Workflow:** `01_Core/00_Workflows/24_Hillary_Life_OS.md`

---

## Cómo usar

```
"captura: [tu idea o tarea] [tag opcional]"
→ Se genera automáticamente un archivo .md aquí con frontmatter
```

## Formato de archivos generados

```markdown
---
created: 2026-04-02T14:30:00Z
source: text
type: task
tags: [trabajo]
---

# Revisar propuesta de cliente
```

## Tags disponibles

| Tag | Uso |
|-----|-----|
| `[trabajo]` | Tareas laborales |
| `[personal]` | Cosas personales |
| `[salud]` | Salud y bienestar |
| `[ideas]` | Ideas e insights |

## Procesamiento

Las capturas en esta carpeta se procesan con:
- `02_Plan_My_Day` — genera schedule diario desde el inbox
- SDD o CE commands — para escalar una captura a feature/task formal
