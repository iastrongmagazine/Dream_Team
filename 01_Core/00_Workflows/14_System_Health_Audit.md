---
name: audit
description: Auditoría completa del sistema — valida estructura, scripts, referencias y estado general. Usar antes de cada entrega importante.
argument-hint: "[opcional: componente específico a auditar — ej: 04_Operations, workflows, rules]"
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
python 08_Scripts_Os/01_Auditor_Hub.py
```

Revisa: estructura de carpetas, scripts Python, referencias en `.md`, reglas `.mdc`.

### 2. Validar Referencias (grep global)

```bash
grep -r "04_Operations\|01_Core\|04_Operations\|docs/" \
  --include="*.py" --include="*.md" --include="*.mdc" \
  | grep -v "(ex " | grep -v "fueron consolidados" | grep -v "Legacy_Backup"
```

Resultado esperado: **0 líneas**. Cualquier resultado es una referencia rota.

### 3. Verificar Estructura de Carpetas

Confirmar que las carpetas v6.1 existen:

```
00_Winter_is_Coming / 01_Core / 02_Knowledge / 03_Tasks /
04_Operations / 05_Archive / 08_Scripts_Os / .agent
```

### 4. Validar Scripts de 08_Scripts_Os

```bash
python 08_Scripts_Os/05_Validator_Hub.py
```

Verifica dependencias y que los scripts están presentes.

### 5. Validar Reglas de Agent

```bash
python 08_Scripts_Os/05_Validator_Hub.py --rules
```

Confirma que todos los `.mdc` en `01_Core/01_Rules/` tienen estructura válida.

### 6. Revisar Inventario

- Abrir `01_Core/01_Inventario_Total.md`
- Confirmar que el número de scripts en `08_Scripts_Os/` coincide con el inventario
- Confirmar que nuevas Skills/Workflows están registradas

### 7. Estado Git

```bash
git status
git log --oneline -5
```

- Sin cambios sin commit → Pure Green
- Si hay cambios → ejecutar `11_Ritual_Cierre_Protocol`

## Criterios de Pure Green

| Check                 | Estado esperado    |
|-----------------------|--------------------|
| Referencias rotas     | 0                  |
| Scripts en inventario | 38 (o actualizado) |
| Carpetas 00-06        | Todas presentes    |
| Reglas `.mdc` válidas | 100%               |
| Git status            | Clean              |
| Dependencias Python   | OK                 |

## Frecuencia recomendada

- **Diaria**: Solo `git status` + grep rápido
- **Semanal**: Auditoría completa (este workflow)
- **Post-reestructura**: Auditoría completa inmediata

---

© 2026 PersonalOS | Un sistema sano es un sistema productivo.
