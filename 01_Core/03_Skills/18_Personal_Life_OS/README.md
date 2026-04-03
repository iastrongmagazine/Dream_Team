# 18_Personal_Life_OS

> **Categoría:** Personal Life OS — Hillary Integration  
> **Versión:** 1.0.0 — 2026-04-02  
> **Origen:** `06_Playground/Hillary_Life_OS/` (integrado a producción)

---

## 5 Skills del Sistema

| # | Skill | Trigger | Propósito |
|---|-------|---------|-----------|
| 01 | **Quick Capture** | "capture", "quick add", "captura" | Capturar ideas/tareas a markdown con frontmatter automático |
| 02 | **Plan My Day** | "plan my day", "plan día", "organizar día" | Transformar inbox en schedule por bloques de energía |
| 03 | **Daily Notes** | "daily notes", "log this", "registro diario" | Observación activa — Yapper's API pattern |
| 04 | **Recording Mode** | "record", "transcribe", "recording mode" | Transcripción + anonimización PII automática |
| 05 | **Returns Tracker** | "create skill from", "auto-skill", "track returns" | Detecta patrones → genera skills automáticos |

---

## Flujo de Integración

```
Quick Capture → 03_Tasks/02_Hillary_Inbox/   (inbox de capturas)
Plan My Day   → schedule diario desde inbox
Daily Notes   → 04_Operations/ (observaciones)
Recording Mode → transcripciones anonimizadas
Returns Tracker → 01_Core/03_Skills/ (auto-generated skills)
```

---

## Invocar el Orquestador

```
/hillary          # Activa workflow 24_Hillary_Life_OS.md
"life os"         # Alias del orquestador
"personal productivity"
```

---

## RUNBOOK

Ver `02_Knowledge/04_Docs/Hillary_Life_OS_RUNBOOK.md` para guía completa de uso.
