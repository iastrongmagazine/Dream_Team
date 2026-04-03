---
name: returns-tracker
description: "Use when user wants to track return patterns, create auto-generated skills, or build workflows from observed behaviors. Trigger: user says 'create skill from', 'build from pattern', 'auto-skill', or 'track returns'."
---

# Returns Tracker — Auto-Skill Building

> "El sistema construye desde la observación." — Anti-system philosophy

## Overview

Detecta patrones recurrentes → genera skills automáticos. Ciclo: observar → detectar → generar → validar.

```
Observación → DETECTAR → PATRON → GENERAR → SKILL
```

---

## Inputs

| Source         | Data                | Weight   |
|----------------|---------------------|----------|
| Quick Capture  | Frecuencia de tags  | Alta     |
| Daily Notes    | Patrones temporales | Alta     |
| Recording Mode | Temas recurrentes   | Media    |
| Plan My Day    | Tareas repetitivas  | Alta     |

### Detectable Patterns

- Tag recurrence: >3 ocurrencias en 30 días
- Time patterns: misma tarea mismo horario
- Workflow chains: A → B → A repetidamente

---

## Proceso

### 1. Recolectar
```python
qc_tags = analyze_capture_frequency()
dn_patterns = analyze_time_patterns()
rm_topics = analyze_topic_frequency()
pm_tasks = analyze_task_repetition()
```

### 2. Detectar Patrones
```python
for tag, count in tags.items():
    if count > 3:
        patterns.append({'type': 'tag_recurrence', 'tag': tag, 'frequency': count})
```

### 3. Evaluar Viabilidad
```python
criteria = {
    'frequency': pattern['frequency'] >= 3,
    'consistency': pattern.get('consistency', 0) >= 0.5,
    'actionable': is_actionable(pattern),
    'unique': not_already_skill(pattern)
}
viability_score = sum(criteria.values()) / len(criteria)  # >= 0.7 = viable
```

### 4. Generar Skill
```markdown
---
name: auto-{pattern}
description: Auto-generated from pattern detection
---
# Auto-Generated Skill

> Confidence: {score}%

## Observed Behavior
- Frequency: {count} times
- Consistent: {pattern data}

## Structure
### Input → Process → Output

## Validation
- [ ] Test with real data
- [ ] Verify edge cases
```

---

## Output

1. **Skill Proposal**: Para cada patrón viable
2. **Pattern Report**: Frecuencia, confidence, acciones
3. **Generated Skills**: Pendientes de validación

---

## Gotchas & Edge Cases

### Observación
1. **Datos insuficientes** (<3): "Need more data"
2. **Datos inconsistentes**: "Pattern too variable"
3. **Noise**: Filter outliers
4. **Temporal**: Consider seasonality

### Detección
5. **False positives**: Similar tags, different context
6. **False negatives**: Real pattern not detected
7. **Confusión**: "reunión" can be standup/1:1/townhall
8. **Overlap**: Multiple patterns in same data

### Evaluación
9. **Viabilidad 0.6-0.7**: "Needs review"
10. **Skill existente**: "Already exists"
11. **Complejidad**: "Too complex for auto-gen"
12. **Utilidad**: "Low utility"

### Generación
13. **Template mal**: Manual review required
14. **Duplicado**: Dedupe
15. **Incompatibilidad**: Resolve conflict first

### Validación
16. **User rejects**: Feedback to pattern
17. **Partial success**: Iterate
18. **Edge cases**: Document

### Sistema
19. **Cycle loops**: Limit recursion
20. **Performance**: Background processing
21. **Storage**: Prune old/inactive

---

## File Structure

```
05_Returns_Tracker/
├── SKILL.md
├── patterns/detected/
├── patterns/validated/
├── generated_skills/
├── reports/
└── examples/pattern_report_example.md
```

---

## Implementation

| Scenario       | Behavior         |
|----------------|------------------|
| <3 occurrences | "Need more data" |
| Score 0.6-0.7  | "Needs review"   |
| Already exists | Skip             |
| User rejects   | Feedback + retry |

---

## Changelog

| Date       | Change       |
|------------|--------------|
| 2026-03-31 | Initial v1.0 |
