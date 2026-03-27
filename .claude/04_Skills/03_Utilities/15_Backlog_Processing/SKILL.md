---
name: backlog-processing
description: Organizes messy notes into actionable tasks. Triggered when the user wants to process their backlog or triage notes.
---

# Backlog Processing Skill

## When to use this skill

- When `BACKLOG.md` grows too large or messy.
- When the user says "Process my backlog" or "Triage my notes."
- After a long capture session of "frictionless" ideas.

## Workflow

1.  **Read Backlog**: Scan `BACKLOG.md` for new entries.
2.  **Categorize**: Assign items to categories (P0, P1, P2 or Archive).
3.  **Deduplicate**: Check for existing tasks in `03_Task/` to avoid redundancy.
4.  **Draft Tasks**: For P0 and P1 items, create task files in `03_Task/` using the standard template.
5.  **Clean Up**: Clear the processed items from `BACKLOG.md`.

## Instructions

- Be aggressive with archiving low-priority ideas to keep the focus sharp.
- Ensure all new tasks have clear success criteria and next steps.
- Use the `process_backlog_with_dedup` MCP tool if available.

## Resources

- [Workflow Example](../../05_Examples/workflows/backlog-processing.md)
- [Triage Script](../../08_Workflow/09_Backlog_Triage.py)

<!--
# Habilidad de Procesamiento del Backlog

## Cuándo usar esta habilidad

- Cuando el `BACKLOG.md` se vuelve demasiado grande o desorganizado.
- Después de una sesión de "Captura Sin Fricción".
- Durante el Ritual Dominical para preparar la semana.

## Flujo de trabajo

1.  **Escanear el Backlog**: Leer todas las entradas en `BACKLOG.md`.
2.  **Categorizar**: Agrupar los elementos por proyecto o tipo de tarea.
3.  **Estimar**: Proporcionar una estimación rápida de tiempo/esfuerzo para cada elemento.
4.  **Triage**: Mover los elementos de alta prioridad a archivos de tareas individuales en `03_Task/`.
5.  **Limpiar**: Eliminar duplicados y refinar las descripciones de las tareas.

## Instrucciones

- Ser implacable con el triage; no todas las ideas necesitan convertirse en una tarea inmediata.
- Utilizar etiquetas para categorizar (ej., #personal, #trabajo, #estudio).
- Sugerir el "archivado" para ideas interesantes que no son accionables actualmente.
-->
