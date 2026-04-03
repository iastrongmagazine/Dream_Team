---
name: daily-notes
description: "Use when user wants to record daily observations, log activities, or create daily summaries. Trigger: user says 'daily notes', 'log this', 'what did I do today', or 'record activity'."
---

# Daily Notes — Observación Activa

> "El sistema observa y aprende, no al revés." — Anti-system philosophy

## Overview

El skill de Daily Notes implementa el concepto "Yapper's API" — un agent que observa y registra actividades del usuario mientras trabaja, aprende patrones over time.

### Concepto: Yapper's API

- El usuario trabaja normalmente
- El agent observa y registra lo que hace (con consentimiento)
- Aprende patrones: qué días son productivos, qué tareas take más tiempo
- Sin打扰 (sin interrupciones)

### Data Flow

```
User Activity → OBSERVE → LOG → LEARN → INSIGHT
                    │         │       │
              (passive)   (markdown) (patterns)
```

---

## Inputs

### 1. Quick Capture (Input pasivo)
- Notas rápidas capturadas durante el día
- Tags: `[observación]`, `[patrón]`, `[insight]`

### 2. Plan My Day (Referencia)
- Schedule del día para comparar planeado vs real

### 3. Preferencias de Observación
`templates/observacion.md`:

```markdown
# Preferencias de Observación

## ¿Qué registrar?
- Tiempo en tareas (start/end)
- Context switches
- Estado de energía (1-5)
- Interruptions

## Frecuencia
- Logging activo cada 30min
- Check-in manual al inicio/fin del día
- Auto-capture de métricas si está disponible

## Privacidad
- Solo lo que el usuario permita
- Anonimizar detalles sensibles
- No recording de calls/reuniones
```

---

## Proceso

### Paso 1: Captura de Actividad

**Manual**:
- "Start working on X" → registra inicio
- "Done with X" → registra fin + duración
- "Switch to Y" → registra context switch

**Pasiva** (si está disponible):
- Window title changes
- Active app tracking
- Idle detection

### Paso 2: Log

```markdown
---
created: 2026-03-31T09:15:00Z
type: activity
task: Automatizar backup
duration: 45min
energy: 4
tags: [trabajo, deep-work]
---

# Automatizar backup

Start: 09:15
End: 10:00
Duration: 45min
Energy: 4/5
Notes: Terminando script de bash
```

### Paso 3: Análisis

- Comparar planeado (Plan My Day) vs real
- Calcular productivity score
- Detectar patrones:
  - Días más productivos
  - Tasks que toman más tiempo
  - Context switches excessivos

### Paso 4: Insights

```markdown
## Insights del Día

- Productivity: 85% (vs 70% avg)
- Deep work: 3h (vs 2h target)
- Context switches: 12 (high)
- Energy trend: decreció después de lunch
```

---

## Output

1. **Daily Log**: Markdown con todas las actividades
2. **Resumen Diario**: Métricas clave
3. **Patrones**: Comparación vs días anteriores
4. **Weekly Insight**: Tendencies de la semana

---

## Gotchas & Edge Cases

### Captura
1. **No hay input**: Si usuario no registra nada → mostrar prompt suave
2. **Logging irregular**: Si gaps >2hr → marcar como "unknown time"
3. **Multitarea**: Si registra dos cosas a la vez → clarify o crear entrada separate

### Privacidad
4. **Sensitive data**: No registrar passwords, financial info, personal conversations
5. **Anonimización**: Si usuario menciona datos sensibles → sugerir `[sensitive]` tag
6. **Opt-out**: Si usuario dice "no me grabes" → respetarlo, solo logging manual

### Análisis
7. **No comparison data**: Si no hay Plan My Day → solo show raw metrics
8. **Patterns inconclusive**: Si <5 días de data → "Aún no hay suficientes datos"
9. **Inconsistent tracking**: Si usuario solo tracking algunos días → warn

### Sistema
10. **Archivo grande**: Si daily log >5000 líneas →archivar comprimido
11. **Corrupt data**: Si entrada malformed → skip, no romper parsing
12. **Timezone mix**: Si usuario trabaja en zonas múltiples → normalize to local

---

## File Structure

```
03_Daily_Notes/
├── SKILL.md
├── templates/
│   └── observacion.md
├── logs/
│   ├── 2026-03-31.md
│   └── 2026-04-01.md
└── insights/
    └── weekly-2026-13.md
```

---

## Implementation

| Scenario          | Behavior                               |
|-------------------|----------------------------------------|
| Sin input         | Prompt: "Sin actividad registrada hoy" |
| Privacy sensitive | Tag `[sensitive]`, no análisis         |
| <5 días data      | "Aún no hay suficientes datos"         |
| Log >5000 líneas  | Archivar comprimido                    |

---

## Changelog

| Date       | Change         |
|------------|----------------|
| 2026-03-31 | Initial design |
