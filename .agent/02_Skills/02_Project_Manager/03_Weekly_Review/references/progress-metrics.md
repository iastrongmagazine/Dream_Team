# Progress Metrics Guide

## Cómo Medir el Éxito de la Semana

### Métricas Cuantitativas

| Métrica | Cómo Calcular | Meta Sugerida |
|---------|--------------|---------------|
| **Completion Rate** | Tareas completadas / Tareas totales | > 70% |
| **Goal Alignment** | Tareas P0 completadas / Total P0 | > 80% |
| **Blocker Resolution** | Bloqueos resueltos / Bloqueos identificados | > 50% |
| **Time Investment** | Horas de deep work registradas | 15-20 hrs/semana |

### Categorías de Tiempo

```
Deep Work:     [████████░░░░░░░░] 65% - Trabajo enfocado sin interrupciones
Meetings:      [████░░░░░░░░░░░░] 25% - Reuniones obligatorias
Buffer:        [██░░░░░░░░░░░░░░] 10% - Espacio para imprevistos
```

### Indicadores de Alerta

| Señal | Qué Significa | Acción |
|-------|---------------|--------|
| 🔴 < 50% completion | Sobrecarga o bloqueos | Revisar prioridades |
| 🔴 Bloqueos > 3 sin resolver | Falta de seguimiento | Escalar o pedir ayuda |
| 🟡 Deep work < 10 hrs | Demasiadas interrupciones | Proteger tiempo fokus |
| 🟢Completion > 80% | Semana productiva | Celebrar y mantener |

### Cómo Usar estos Datos

1. **Ejecutar `analyze-progress.py`** - Obtiene lista de tareas
2. **Calcular completion rate** - Tareas con `status: d` / total
3. **Revisar blockers** - Identificar bloqueos > 3 días
4. **Ajustar presupuesto de tiempo** - Para la próxima semana
