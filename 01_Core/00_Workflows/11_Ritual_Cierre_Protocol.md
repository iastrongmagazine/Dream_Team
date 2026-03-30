---
name: cierre
description: Protocolo de cierre de sesión — backup, validación, sync y commit. Dejar el sistema en estado Pure Green.
argument-hint: "[opcional: notas o aprendizajes del día a documentar]"
---

# 🔒 Workflow: Ritual de Cierre

Ejecutar al finalizar cada sesión de trabajo. Garantiza que el sistema quede en estado **Pure Green**: sin cambios sin commit, sin referencias rotas, sin inventario desactualizado.

## Cuándo usar

- Al terminar una sesión de trabajo
- Antes de cerrar Claude Code
- Tras completar cualquier tarea P0/P1
- Cuando el script `08_Ritual_Cierre.py` lo solicite

## Pasos

### 1. Validar Estado del Sistema

1. `git status` — confirmar qué archivos cambiaron
2. Verificar que no hay referencias rotas: `grep -r "04_Operations\|01_Core\|04_Operations\|docs/" --include="*.py" --include="*.md"`
3. Si hay errores → resolverlos antes de continuar

### 2. Actualizar Inventario (si aplica)

1. ¿Se crearon scripts nuevos en `08_Scripts_Os/`? → Registrar en `01_Core/01_Inventario_Total.md`
2. ¿Se crearon Skills o Workflows nuevos? → Registrar en `01_Core/01_Inventario_Total.md` + actualizar `README.md` del directorio

### 3. Guardar Notas de Proceso

1. Crear o actualizar archivo en `04_Operations/03_Process_Notes/` con resumen de la sesión + ejecutar `mem_save()` en Engram:
   - Qué se hizo
   - Decisiones tomadas
   - Pendientes para la próxima sesión
2. Formato de nombre: `YYYY-MM-DD_<tema>.md`

### 4. Ejecutar Ritual Automatizado

```bash
python 08_Scripts_Os/04_Ritual_Hub.py
```

El script ejecuta: backup + validación de reglas + sync de contexto.

### 5. Commit Final

1. `git add` — solo archivos relevantes (nunca `.env`, credenciales)
2. Commit con mensaje descriptivo usando Conventional Commits:
   - `feat:` nueva funcionalidad
   - `fix:` corrección de bug
   - `chore:` mantenimiento, docs, reorganización
3. Verificar `git log --oneline -3` — confirmar que el commit quedó registrado

### 6. Confirmación Pure Green

Reportar en chat:

```
✅ PURE GREEN
- Commits: [N archivos]
- Validación: OK
- Inventario: actualizado
- Process Notes: guardadas
```

## Automatización

Para ejecutar el ritual completo con un solo comando:

```bash
python 08_Scripts_Os/04_Ritual_Hub.py
```

---

© 2026 PersonalOS | Cierra bien, abre mejor.
