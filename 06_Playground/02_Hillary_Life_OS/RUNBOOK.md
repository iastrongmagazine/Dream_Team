# Hillary Life OS — Runbook

> Guía de uso para los 5 skills del sistema.

## Quick Capture (FASE 1)

### Cómo Usar

```bash
# Captura rápida desde cualquier input
"reunión con cliente 3pm [trabajo]"
→ Genera: inbox/2026-03-31-1430-reunion.md
```

### Tags

| Tag          | Uso               |
|--------------|-------------------|
| `[trabajo]`  | Tareas laborales  |
| `[personal]` | Cosas personales  |
| `[salud]`    | Salud y bienestar |
| `[ideas]`    | Ideas y insights  |

### Output Esperado

```markdown
---
created: 2026-03-31T14:30:00Z
source: text
type: task
tags: ["trabajo", "reunion"]
---

# Reunión con cliente 3pm

reunión con cliente 3pm
```

---

## Plan My Day (FASE 2)

### Cómo Usar

1. **Ejecutar** con input: "Plan my day"
2. **Resultado**: Schedule generado en markdown

### Input Requerido

```
01_Quick_Capture/inbox/    ← Tareas capturadas
02_Plan_My_Day/templates/preferencias.md
02_Plan_My_Day/templates/calendario_hoy.md
```

### Output Esperado

```markdown
# Mi Día - 2026-03-31

## 🌅 Mañana (alta energía)
- [P0] Automatizar backup → 60min

## 🌞 Tarde (media energía)
- [P1] Preparar presentation → 30min

## 🌙 Noche (baja energía)
- Revisión diaria

---
## Análisis
- 3 tareas P0, 1 P1, 1 P2
```

---

## Daily Notes (FASE 3)

### Cómo Usar

1. **Iniciar**: "Start logging" / "Begin daily notes"
2. **Durante el día**: Registrar actividades
3. **Fin del día**: "Generate daily summary"

### Tipos de Logging

| Tipo     | Trigger          | Descripción        |
|----------|------------------|--------------------|
| Activity | "Working on X"   | Estado de tarea    |
| Energy   | "Energy is 4/5"  | Nivel de energía   |
| Switch   | "Switching to Y" | Cambio de contexto |

### Output Esperado

```markdown
# Daily Log - 2026-03-31

## Resumen
- Productivity: 85%
- Deep Work: 3.5h
- Tasks: 8 completados
```

---

## Recording Mode (FASE 4)

### Cómo Usar

1. **Grabar**: "Start recording" / "Record meeting"
2. **Procesar**: Auto-transcribe + anonymize
3. **Resultado**: Transcript seguro

### Configurar Privacidad

Editar `04_Recording_Mode/templates/privacidad.md`:

```markdown
## Niveles
- basic: email, teléfono
- standard: + nombre, SSN, tarjeta
- strict: + dirección, IP, password
```

### Output Esperado

```markdown
---
anonymized: true
privacy_level: strict
---

[00:00] [PERSONA] inicia
[00:05] Se discute [PROYECTO] con [EMAIL]
```

---

## Returns Tracker (FASE 5)

### Cómo Usar

1. **Activar**: "Generate skill from patterns" / "What patterns do you see?"
2. **Proceso**: Analiza datos de otros skills
3. **Resultado**: Propuestas de auto-skills

### Fuentes de Datos

- Quick Capture: Tags recurrentes
- Daily Notes: Patrones temporales
- Recording Mode: Temas recurrentes
- Plan My Day: Tareas repetitivas

### Output Esperado

```markdown
# Pattern Report

| Pattern       | Frecuencia   | Confidence   | Acción        |
|---------------|--------------|--------------|---------------|
| daily-standup | 30/30        | 92%          | Generar skill |
```

---

## Validación

Para verificar todos los skills:

```bash
python skill_validator.py 06_Playground/Hillary_Life_OS/
```

Expected: `Average Score: 100.0%`

---

## Changelog

| Fecha      | Cambio               |
|------------|----------------------|
| 2026-03-31 | Initial runbook v1.0 |
