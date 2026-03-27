---
name: audit
description: Auditoría completa del sistema — valida estructura, scripts, referencias y estado general. Usar antes de cada entrega importante.
argument-hint: "[opcional: componente específico a auditar — ej: 04_Engine, workflows, rules]"
---

# 🏥 Workflow: System Health Audit

Auditoría proactiva del PersonalOS. Verificar que todo está en orden: scripts funcionales, referencias válidas, inventario actualizado, estructura correcta.

## Cuándo usar

- Antes de una sesión importante (P0/P1)
- Tras una reestructura mayor de carpetas
- Semanalmente como parte del `00_Weekly_Review`
- Cuando el sistema se siente "desordenado"

## Pasos

### 1. Auditoría Automatizada

```bash
python 04_Engine/42_Audit_Engineering.py
```

Revisa: estructura de carpetas, scripts Python, referencias en `.md`, reglas `.mdc`.

### 2. Validar Referencias (grep global)

```bash
grep -r "04_Engine\|05_System\|06_Archive\|03_Knowledge/Examples\|03_Knowledge/Resources" \
  --include="*.py" --include="*.md" --include="*.mdc" \
  | grep -v "(ex " | grep -v "fueron consolidados"
```

Resultado esperado: **0 líneas**. Cualquier resultado es una referencia rota.

### 3. Verificar Estructura de Carpetas

Confirmar que las 7 dimensiones existen:

```
00_Core / 01_Brain / 02_Operations / 03_Knowledge /
04_Engine / 05_System / 06_Archive
```

### 4. Validar Scripts de 04_Engine

```bash
python 04_Engine/13_Validate_Stack.py
```

Verifica dependencias y que los 43 scripts están presentes.

### 5. Validar Reglas de Cursor

```bash
python 04_Engine/40_Validate_Rules.py
```

Confirma que todos los `.mdc` en `.cursor/00_Rules/` tienen estructura válida.

### 6. Revisar Inventario

- Abrir `01_Brain/02_Knowledge_Brain/01_Inventario_Total.md`
- Confirmar que el número de scripts en `04_Engine/` coincide con el inventario
- Confirmar que nuevas Skills/Workflows están registradas

### 7. Estado Git

```bash
git status
git log --oneline -5
```

- Sin cambios sin commit → Pure Green
- Si hay cambios → ejecutar `11_Ritual_Cierre_Protocol`

## Criterios de Pure Green

| Check | Estado esperado |
|-------|----------------|
| Referencias rotas | 0 |
| Scripts en inventario | 38 (o actualizado) |
| Carpetas 00-06 | Todas presentes |
| Reglas `.mdc` válidas | 100% |
| Git status | Clean |
| Dependencias Python | OK |

## Frecuencia recomendada

- **Diaria**: Solo `git status` + grep rápido
- **Semanal**: Auditoría completa (este workflow)
- **Post-reestructura**: Auditoría completa inmediata

---

© 2026 PersonalOS | Un sistema sano es un sistema productivo.
