# Workflow: Classify Task

## Trigger
User wants to classify a task or needs template recommendation.

## Questions

1. **¿Cuál es la tarea?**
   → Capture description

2. **¿Cuánto tiempo estimás?**
   - [ ] <2 horas → CORTO
   - [ ] 2-8 horas → MEDIO
   - [ ] 8+ horas → SOTA

3. **¿Cuántos archivos?**
   - [ ] 1-2 → CORTO
   - [ ] 3-10 → MEDIO
   - [ ] 10+ → SOTA

## Output

```
## Clasificacion

| Criterio | Valor | Template |
|----------|-------|----------|
| Esfuerzo | Xh | - |
| Archivos | Y | - |
| Complejidad | Z | - |

**Template Recomendado:** [SOTA/MEDIO/CORTO]
**Archivo:** [ruta]
```

## Next Step
User confirms → Apply template.
