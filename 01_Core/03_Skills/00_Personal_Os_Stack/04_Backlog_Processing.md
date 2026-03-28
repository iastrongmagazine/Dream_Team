---
name: "backlog-processing"
description: "Procesar backlog y mantener el sistema PersonalOS - Flujo completo para limpiar, priorizar y crear tareas"
---

# Backlog Processing Skill

Esta skill guía el flujo completo para procesar el backlog del PersonalOS y mantener el sistema actualizado.

##触发 (Triggers)

- "clear my backlog"
- "process backlog"
- "actualizar backlog"
- "organizar tareas pendientes"

---

## Flujo Completo de Backlog Processing

### Paso 1: Leer Contexto Estratégico

Antes de procesar, siempre leer:

1. **GOALS.md** → Objetivos estratégicos actuales
   ```
   00_Winter_is_Coming/GOALS.md
   ```

2. **BACKLOG.md** → Tareas pendientes
   ```
   00_Winner_is_Coming/BACKLOG.md
   ```

3. **Engram** → Contexto de sesiones previas
   ```
   engram mem_context
   ```

### Paso 2: Extraer Ítems del Backlog

Leer `BACKLOG.md` y extraer cada ítem accionable.

**Reglas:**
- Ignorar líneas vacías o comentarios
- Cada ítem debe ser una acción clara
- Si falta contexto, PRIORIDAD o siguiente paso → PREGUNTAR al usuario antes de crear tarea

### Paso 3: Buscar Contexto

Para cada ítem:
- Buscar en `02_Knowledge/` por keywords relevantes
- Verificar si ya existe tarea similar (dedup)
- Vincular con objetivos en GOALS.md

### Paso 4: Crear Tareas en 03_Tasks/

**Template básico (usar según complejidad):**

```yaml
---
title: [Nombre de tarea]
category: [technical|outreach|research|writing|content|admin|personal|other]
priority: [P0|P1|P2|P3]
status: n  # n=not_started, s=started, b=blocked, d=done
created_date: [YYYY-MM-DD]
estimated_time: [minutos]
resource_refs:
  - 00_Winter_is_Coming/GOALS.md
---

# [Nombre de tarea]

## Context

Vinculado a: Meta "[nombre de meta]"

## Next Actions

- [ ] Acción 1
- [ ] Acción 2

## Progress Log

- YYYY-MM-DD: Notas, bloqueos, decisiones.
```

### Paso 5: Templates por Complejidad

| Complejidad | Template | Ubicación |
|-------------|---------|-----------|
| Alta (1-8 horas) | SOTA | `03_Tasks/00_Templates/03_Task_Template_SOTA.md` |
| Media (1-4 horas) | Medio | `03_Tasks/00_Templates/04_Task_Template_Medio.md` |
| Baja (30min-2h) | Corto | `03_Tasks/00_Templates/05_Task_Template_Corto.md` |

### Paso 6: Limpiar BACKLOG.md

Después de crear las tareas:
- Eliminar los ítems procesados de BACKLOG.md
- Agregar fecha de actualización
- Mantener solo nuevos items pendientes

### Paso 7: Guardar en Engram

Guardar el resultado del procesamiento:

```
engram mem_save: "Backlog Processing - [fecha]"
- Tareas creadas: [lista]
- Items pendientes: [cantidad]
- Meta vinculada: [nombre]
```

---

## Categorías de Tareas

| Categoría | Descripción |
|-----------|-------------|
| **technical** | build, fix, configure |
| **outreach** | communicate, meet |
| **research** | learn, analyze |
| **writing** | draft, document |
| **content** | blog posts, social media |
| **admin** | operations, finance, logistics |
| **personal** | health, routines |
| **other** | everything else |

---

## Reglas de Prioridad

| Priority | Significado | Límite |
|----------|------------|--------|
| **P0** | Esta semana, crítico | max 3 |
| **P1** | Este mes, importante | max 7 |
| **P2** | Programado | sin límite |
| **P3** | Algún día | sin límite |

---

## Deduplicación

Antes de crear tarea, verificar:
1. Buscar en `03_Tasks/` por título similar
2. Usar script de dedup si existe
3. Si existe相近 → actualizar en vez de crear nueva

---

## Ejemplo de Output

```
## Resumen de Backlog Processing

### Tareas Creadas:
- 11_P1_Actualizar_Documentacion_Sistema.md
- 12_P1_Actualizar_Estructura_Carpetas.md

### Pendientes (sin contexto suficiente):
- [ ] Item que requiere clarificación

### Vinculado a Goals:
- Meta: "Activate Think_Different PersonalOS in daily workflow"
```

---

## Errores Comunes a Evitar

1. ❌ Crear tarea sin vincular a GOALS
2. ❌ No preguntar cuando falta contexto
3. ❌ Olvidar actualizar BACKLOG.md
4. ❌ No guardar en Engram
5. ❌ Mezclar templates (usar el correcto según complejidad)

---

## Comandos Útiles

```bash
# Ver tareas activas
ls 03_Tasks/*.md

# Buscar tarea específica
grep -r "title:" 03_Tasks/

# Ver estado de prioridades
grep "priority:" 03_Tasks/*.md

# Contar tareas por estado
grep "status:" 03_Tasks/*.md | sort | uniq -c
```

---

## Integración con Skills

Esta skill funciona con:
- **personal-os**: Skill principal del sistema
- **sdd-workflow**: Para tareas que necesitan specs
- **system-guardian**: Para validar estructura después de cambios
