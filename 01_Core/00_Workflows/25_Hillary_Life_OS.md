# 24_Hillary_Life_OS — Workflow Orquestador

> **Trigger:** `/hillary`, "life os", "personal productivity"  
> **Versión:** 1.0.0 — 2026-04-02  
> **Skills:** `18_Personal_Life_OS` (5 skills)

---

## Overview

Orquesta los 5 skills de Hillary Life OS según el contexto del usuario. No reemplaza ningún workflow existente — complementa el sistema de productividad personal.

```
Usuario → Detectar intención → Skill correcto → Ejecutar → Capturar resultado
```

---

## Routing de Intenciones

| Trigger del usuario | Skill invocado | Acción |
|--------------------|----------------|--------|
| "capture", "captura", "quick add", "anota", "guarda idea" | `01_Quick_Capture` | Crear archivo en `03_Tasks/02_Hillary_Inbox/` |
| "plan my day", "plan día", "qué hago hoy", "organizar día" | `02_Plan_My_Day` | Leer inbox → generar schedule |
| "daily notes", "log this", "registro", "anotar actividad" | `03_Daily_Notes` | Agregar a log diario en `04_Operations/` |
| "record", "transcribe", "grabar reunión", "recording mode" | `04_Recording_Mode` | Transcribir + anonimizar PII |
| "create skill from", "auto-skill", "build pattern", "track returns" | `05_Returns_Tracker` | Detectar patrón → generar skill |

---

## Flujo Principal

```
1. DETECTAR intención (tabla arriba)
2. CARGAR skill: 01_Core/03_Skills/18_Personal_Life_OS/{skill}/SKILL.md
3. EJECUTAR según instrucciones del skill
4. GUARDAR resultado en destino apropiado
5. NOTIFICAR via notification.py si corresponde
```

---

## Destinos por Skill

| Skill | Destino del output |
|-------|--------------------|
| Quick Capture | `03_Tasks/02_Hillary_Inbox/` |
| Plan My Day | respuesta inline + opcionalmente `04_Operations/` |
| Daily Notes | `04_Operations/03_Process_Notes/` (si existe) |
| Recording Mode | `02_Knowledge/` (transcripciones) |
| Returns Tracker | `01_Core/03_Skills/` (auto-generated skills) |

---

## Integración con el Sistema

- **Engram:** Guardar capturas importantes con `mem_save`
- **SDD:** Compatible con `/sdd:new` si la captura escala a feature
- **CE:** Compatible con `/ce:work` para ejecutar tasks del inbox
- **GOALS.md:** Quick Capture → tareas alineadas con objetivos Q2 2026
- **Notificaciones:** `python 01_Core/07_Hooks/04_Sound/notification.py --task-complete`

---

## Ejemplo de Uso

```
Usuario: "captura: revisar propuesta de cliente [trabajo]"
→ Skill: Quick Capture
→ Output: 03_Tasks/02_Hillary_Inbox/2026-04-02-revisar-propuesta.md
→ Engram: mem_save("Quick capture: revisar propuesta cliente")

Usuario: "plan my day"
→ Skill: Plan My Day
→ Lee: 03_Tasks/02_Hillary_Inbox/ + GOALS.md
→ Output: Schedule por bloques de energía inline
```

---

## RUNBOOK

Ver `02_Knowledge/04_Docs/Hillary_Life_OS_RUNBOOK.md` para guía detallada.

---

*Think Different PersonalOS v6.1 — Workflow 24 — Hillary Life OS*
