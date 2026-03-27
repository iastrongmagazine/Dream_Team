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
   python 04_Engine/00_Context_Reset.py
   ```

2. Iniciar nueva sesión ejecutando `01_Iron_Man_Gen` (Workflow Génesis)
3. Cargar solo los archivos estrictamente necesarios para la tarea actual

### Opción B — Reset Manual (si el script falla)

1. Abrir nueva conversación en Claude Code
2. Ejecutar el Workflow Génesis (`01_Iron_Man_Gen.md`) completo:
   - `.cursor/00_Rules/01_Context_Protocol.mdc`
   - `01_Brain/Context_Memory/` (último archivo)
   - `01_Brain/Process_Notes/` (último archivo)
   - `01_Brain/Knowledge_Brain/01_Inventario_Total.md`
3. Leer `CLAUDE.md` — constitución del sistema
4. Reportar contexto cargado antes de continuar

### Opción C — Reset Completo del Sistema

Solo si A y B fallan:

1. Guardar manualmente notas de lo que estabas haciendo
2. Cerrar Claude Code completamente
3. Reabrir y ejecutar Génesis desde cero

## Prevención

- Usar subagentes (`.claude/agents/`) para tareas largas → protegen la ventana de contexto principal
- Guardar `Process_Notes` al final de cada sesión con `11_Ritual_Cierre_Protocol`
- Hacer commits frecuentes → el estado del repo siempre refleja el avance real
- Si una tarea requiere leer más de 10 archivos → delegar a un subagente

## Referencia rápida de estructura actual

```
Think_Different/
├── 00_Core/          # GOALS, BACKLOG, AGENTS
├── 01_Brain/         # Context_Memory, Process_Notes, Knowledge_Brain
├── 02_Operations/    # Tasks/
├── 03_Knowledge/     # Examples/, Resources/, Docs/, Notes/
├── 04_Engine/        # 38 scripts Python
├── 05_System/        # MCP, requirements.txt
└── 06_Archive/       # Legacy
```

---

© 2026 PersonalOS | Cuando te pierdes, vuelve al origen.
