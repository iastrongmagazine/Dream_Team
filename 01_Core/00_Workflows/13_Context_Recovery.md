---
name: recover
description: Protocolo de recuperación de contexto degradado o corrupto. Usar cuando el AI pierde el hilo o produce respuestas inconsistentes.
argument-hint: "[opcional: describir qué está confuso o qué tarea estaba activa]"
---

# 🔄 Workflow: Context Recovery (Reset de Contexto)

Usar cuando el contexto de la sesión está degradado: respuestas incoherentes, referencias a archivos incorrectos, confusión sobre la estructura del sistema, o bucles de errores repetidos.

## Síntomas que indican necesidad de reset

- El AI referencia rutas o nombres de carpetas que no existen
- Repite los mismos errores tras múltiples intentos
- Confunde la estructura del proyecto (menciona carpetas viejas como `06_ENGINE`, `08_ARCHIVE`)
- Propone soluciones que contradicen decisiones previas de la sesión
- El contexto de la conversación supera el 80% de la ventana

## Pasos de Recuperación

### Opción A — Reset Suave (recomendado primero)

1. Ejecutar el script de reset:

   ```bash
   python 08_Scripts_Os/04_Ritual_Hub.py --reset
   ```

2. Iniciar nueva sesión ejecutando `01_Iron_Man_Gen` (Workflow Génesis)
3. Cargar solo los archivos estrictamente necesarios para la tarea actual
4. Consultar Engram: `mem_search()` + `mem_context()`

### Opción B — Reset Manual (si el script falla)

1. Abrir nueva conversación en Claude/OpenCode
2. Ejecutar el Workflow Génesis (`01_Iron_Man_Gen.md`) completo:
   - `01_Core/01_Rules/`
   - `04_Operations/00_Context_Memory/` (último archivo)
   - `04_Operations/03_Process_Notes/` (último archivo)
   - `01_Core/01_Inventario_Total.md`
   - **Engram**: `mem_search()` + `mem_context()`
3. Leer `AGENTS.md` — constitución del sistema
4. Reportar contexto cargado antes de continuar

### Opción C — Reset Completo del Sistema

Solo si A y B fallan:

1. Guardar manualmente notas de lo que estabas haciendo
2. Cerrar Claude Code completamente
3. Reabrir y ejecutar Génesis desde cero

## Prevención

- Usar subagentes (`.agent/01_Agents/`) para tareas largas → protegen la ventana de contexto principal
- Guardar `Process_Notes` al final de cada sesión con `11_Ritual_Cierre_Protocol`
- Hacer commits frecuentes → el estado del repo siempre refleja el avance real
- Si una tarea requiere leer más de 10 archivos → delegar a un subagente

## Referencia rápida de estructura actual v6.1

```
Think_Different/
├── 00_Winter_is_Coming/  # GOALS, BACKLOG, AGENTS
├── 01_Core/              # Inventario, Rules, Config
├── 02_Knowledge/         # Examples, Resources
├── 03_Tasks/             # Tareas activas
├── 04_Operations/        # Context_Memory, Process_Notes, Memory_Brain, Plans, Solutions
├── 05_Archive/           # Legacy
├── 08_Scripts_Os/        # HUBs y scripts Python
└── .agent/              # Skills, Workflows, Extensions
```

---

© 2026 PersonalOS | Cuando te pierdes, vuelve al origen.
