---
name: plan-my-day
description: "Use when user wants to plan their day, organize tasks, or create a schedule. Trigger: user says 'plan my day', 'what should I do', 'organize my day', or 'create schedule'."
---

# Plan My Day — Agent de Planificación Diaria

> "El sistema aprende de vos, no al revés." — Anti-system philosophy

## Overview

Transforma inbox de tareas en schedule organizado. Lee inbox, prefs y calendario → genera plan por bloques de energía.

```
INBOX ──► ANALYZE ──► PRIORITIZE ──► SCHEDULE
```

| Component   | Responsibility               |
|-------------|------------------------------|
| Collector   | Read inbox, prefs, calendar  |
| Analyzer    | Extract tags, energy, impact |
| Prioritizer | Apply Eisenhower + 10x rules |
| Scheduler   | Map to time blocks           |

---

## Inputs

### 1. Inbox (Fase 1)
`01_Quick_Capture/inbox/*.md` → extrae `created`, `type`, `tags`, body

### 2. Preferencias
`templates/preferencias.md`: energía por horario, constraints, observaciones

```markdown
## Energía
- Mañana (9-12): alta, trabajo profundo
- Tarde (14-17): media, reuniones
- Noche (19-22): baja, tareas simples

## Constraints
- No trabajo >8pm (familia)
- 30min exercise diario
- Máximo 3 P0 por día
```

### 3. Calendario
`templates/calendario_hoy.md`: bloques ocupados del día

---

## Proceso

### 1. Recolectar
```python
inbox = read_folder("01_Quick_Capture/inbox/")
prefs = read("templates/preferencias.md")
calendar = read("templates/calendario_hoy.md")
```

### 2. Analizar
- **Tags**: del frontmatter
- **Energy**: alta (deep work), media (revisiones), baja (simples)
- **Impact**: 10x test — ¿esto elimina otras tareas?

### 3. Prioritizar

| Rule          | Priority   |
|---------------|------------|
| Deadline hoy  | P0         |
| 10x impacto   | P1         |
| Bloquea otras | P2         |
| Default       | P3         |

### 4. Schedule

```markdown
# Mi Día - 2026-03-31

## 🌅 Mañana (alta)
- [P0] Automatizar backup → 60min

## 🌞 Tarde (media)
- [P1] Preparar presentation → 30min

## 🌙 Noche (baja)
- Revisión diaria
```

---

## Output

1. Schedule por bloques de energía
2. Recomendaciones (qué empezar, delegar)
3. Resumen: P0/P1/P2 count, deep work total

---

## Gotchas & Edge Cases

### Input
1. **Inbox vacío** → "Add items to inbox first"
2. **Solo insights** → listar separately, no schedule
3. **Prefs no existen** → defaults (mañana=alta)
4. **Calendario no existe** → asumir día libre

### Prioritization
5. **>5 P0** → warn "reducir a 3"
6. **Deadline conflict** → 10x test
7. **Sin deadline** → "someday" default
8. **Tarea >2hr** → sugerir dividir

### Scheduling
9. **Sin bloques** → warning
10. **Conflictos** → respetar constraints
11. **Exercise missing** → warn
12. **Fin de semana** → energía flexible
13. **Meeting >4hr** → warn

### Energy
14. **Alta en bloque bajo** → mover o warn
15. **Deep work >4hr** → dividir

### Constraints
16. **>8pm** → warn
17. **Familia time** → respetar

### Data
18. **Sin tags** → "sin-categorizar"
19. **Tag no reconocido** → warning
20. **Frontmatter inválido** → skip + log
21. **Archivo corrupto** → skip

### System
22. **Carpeta no existe** → crear o error
23. **Permission denied** → error claro

---

## File Structure

```
02_Plan_My_Day/
├── SKILL.md
├── templates/
│   ├── preferencias.md
│   └── calendario_hoy.md
├── examples/
│   └── plan_ejemplo.md
└── output/
    └── .gitkeep
```

---

## Implementation

| Scenario        | Behavior                  |
|-----------------|---------------------------|
| Inbox vacío     | "No tasks to plan"        |
| >5 P0           | "Reduce to 3 recommended" |
| Energy mismatch | Warn but schedule         |
| No prefs        | Use defaults              |

---

## Changelog

| Date       | Change       |
|------------|--------------|
| 2026-03-31 | Initial v1.0 |
