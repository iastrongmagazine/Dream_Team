---
name: auto-template-selector
description: Auto-detecta y recomienda template según complejidad de tarea
---

# Auto Template Selector

Use this skill to automatically detect which template to use for a task.

## Detection Logic

Read task description and analyze:

| Criterio | SOTA | MEDIO | CORTO |
|----------|------|-------|-------|
| Esfuerzo | 8h+ | 2-8h | <2h |
| Archivos | 10+ | 3-10 | 1-2 |
| Scope | Multi-modulo | Modulo | Archivo |

## Keywords

**SOTA:** sistema, arquitectura, restructurar, migracion, breaking, multi
**MEDIO:** feature, nuevo, endpoint, componente, refactorizar
**CORTO:** fix, bug, typo, docs, quick, simple

## Output

After analysis, output:

```
## Template Recomendado: [SOTA/MEDIO/CORTO]

Razon: [explicación breve]
Archivo: [01_Brain/05_Templates/XX_Task_Template_XXX.md]

¿Confirmás este template?
```

## Integration

Run script for more detailed analysis:
```bash
python 08_Scripts_Os/59_Task_Classifier.py "descripcion"
```
