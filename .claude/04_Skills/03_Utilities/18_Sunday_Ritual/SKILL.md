---
name: sunday-ritual
description: Executes the Sunday ritual for personal and system maintenance. Triggered when the user mentions Sunday ritual or end-of-week cleanup.
---

# Sunday Ritual Skill

## When to use this skill

- Sunday evenings for a "Weekly Reset."
- When the user wants to align their Digital Brain with long-term goals.

## Workflow

1.  **Reflective Harvest**: Analyze progress against metrics in `GOALS.md`.
2.  **Capture Sweep**: Run `backlog-processing` focusing on the past week's captures.
3.  **Architecture**: Plan next week's top 3 P0 tasks.
4.  **System Maintenance**:
    - Archive completed tasks.
    - Sync process notes using `11_Sync_Notes.py`.
    - Run `self_heal.py` to fix broken links.

## Instructions

- Ensure all P0/P1 tasks align with the "North Star" in `GOALS.md`.
- Focus on "Simplicity over Complexity."

## Resources

- [Workflow Example](../../05_Examples/workflows/sunday-ritual.md)
- [Ritual Script](../../08_Workflow/17_Ritual_Dominical.py)

<!--
# Habilidad de Ritual Dominical

## Cuándo usar esta habilidad

- Los domingos para un reinicio completo del sistema.
- Para alinear el cerebro digital con los objetivos de vida.

## Flujo de trabajo

1.  **Mantenimiento Técnico**: Ejecutar auto-sanación, limpieza de caché y archivado de tareas.
2.  **Alineación Estratégica**: Revisar `GOALS.md` y ajustar las prioridades para el mes/trimestre.
3.  **Reinicio Mental**: Vaciar el backlog y organizar las ideas capturadas durante la semana.

## Instrucciones

- Enfocarse en la claridad y la preparación para la semana siguiente.
- Asegurarse de que el sistema esté en un estado "verde puro" (sin errores).
-->
