---
name: captura
description: Captura sin fricción — idea, insight o aprendizaje → BACKLOG en menos de 60 segundos. El workflow más corto del sistema.
argument-hint: "[idea o aprendizaje a capturar]"
---

# ⚡ Workflow: Captura Rápida

El enemigo del sistema no es la falta de ideas — es la fricción para capturarlas.
Este workflow elimina esa fricción. Una sola pregunta, un destino claro.

## Regla de oro

> Si capturar tarda más de 60 segundos, el sistema está fallando.

## Cuándo usar

- Tienes una idea y no quieres perderla
- Lees algo importante que quieres guardar
- Aprendes algo que debe quedar documentado
- Surge una tarea nueva en medio de otra
- Quieres anotar un bloqueante sin interrumpir el flujo actual

## El flujo (60 segundos)

### Paso 1 — ¿Qué tipo de captura es?

| Tipo | Destino | Ejemplo |
|------|---------|---------|
| **Idea / Tarea** | `00_Core/BACKLOG.md` | "Crear workflow de English practice" |
| **Aprendizaje** | `01_Brain/Process_Notes/` | "Descubrí que ctx.resume() es necesario en iOS" |
| **Referencia** | `03_Knowledge/Notes/` | Link, paper, concepto a profundizar |
| **Insight de diseño** | `03_Knowledge/Writing/` | Reflexión sobre UX, AI, producto |
| **Bug / Problema** | `00_Core/BACKLOG.md` con tag `[BUG]` | "El script 13 falla con archivos vacíos" |

### Paso 2 — Escribir en crudo

No estructures ahora. Solo escribe:

```
[fecha] [tipo] — descripción breve
```

Ejemplo en `BACKLOG.md`:

```
- [2026-03-02] [IDEA] Crear workflow de Deep Work con timer Pomodoro
- [2026-03-02] [REF] Ver cómo Raycast maneja el command palette — aplicar a mi OS
- [2026-03-02] [BUG] Script 07_Morning_Standup no lee Context_Memory correctamente
```

### Paso 3 — Soltar y seguir

No proceses ahora. El triage lo hace `09_Backlog_Triage.py` cuando toque.

## Procesamiento diferido

Cuando el backlog tenga 10+ items o al final del día:

```bash
python 04_Engine/09_Backlog_Triage.py
```

Convierte entradas brutas en tareas estructuradas con prioridad, categoría y vínculo a GOALS.

## Capturas especiales

### Captura de reunión (con Fireflies MCP)

Si tienes una reunión grabada y quieres extraer aprendizajes:

```
"Busca en mis reuniones de [fecha] los puntos de acción"
→ Fireflies MCP: search_meetings / get_transcript
→ Resultado → 00_Core/BACKLOG.md o 01_Brain/Process_Notes/
```

### Captura de pantalla / UI insight

```
→ Playwright MCP: screenshot de la referencia
→ Guardar en 03_Knowledge/Resources/ con descripción
```

---

© 2026 PersonalOS | Captura todo, procesa después, ejecuta con foco.
