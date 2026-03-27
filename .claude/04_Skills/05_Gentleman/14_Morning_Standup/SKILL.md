---
name: morning-standup
description: Guides the user through a quick 2-minute daily focus session. Triggered when the user mentions morning routine or daily priorities.
---

# Morning Standup Skill

## When to use this skill

- First thing in the morning when starting the workday.
- When the user asks "What should I work on today?"
- When feeling overwhelmed and needing to prioritize tasks.

## Workflow

1.  **Retrieve Context**: Read `GOALS.md`, `BACKLOG.md`, and active tasks in `02_Operations/01_Active_Tasks/`.
2.  **Analyze Priorities**: Identify top 3 priorities based on deadlines and alignment with goals.
3.  **Propose Schedule**: Suggest a realistic plan for the day, highlighting deep work vs. quick wins.
4.  **Check Blockers**: Identify any blocked tasks and propose next steps to unblock.

## Instructions

- Keep the interaction under 2 minutes.
- Provide clear, actionable advice.
- Use the following format for priorities:
  - **1. [Priority Level] Task Name** (est: Time)
  - Brief rationale.

## Resources

- [Workflow Example](../../05_Examples/workflows/morning-standup.md)
- [Morning Script](../../08_Workflow/07_07_Morning_Standup.py)

<!--
# Habilidad de Standup Matutino

## Cuándo usar esta habilidad

- A primera hora de la mañana al comenzar la jornada laboral.
- Cuando el usuario pregunta "¿En qué debería trabajar hoy?"
- Cuando te sientas abrumado y necesites priorizar tareas.

## Flujo de trabajo

1.  **Recuperar Contexto**: Leer `GOALS.md`, `BACKLOG.md` y tareas activas en `02_Operations/01_Active_Tasks/`.
2.  **Analizar Prioridades**: Identificar las 3 prioridades principales basándose en plazos y alineación con los objetivos.
3.  **Proponer Horario**: Sugerir un plan realista para el día, destacando el trabajo profundo frente a las victorias rápidas.
4.  **Verificar Bloqueadores**: Identificar cualquier tarea bloqueada y proponer pasos a seguir para desbloquearla.

## Instrucciones

- Mantener la interacción en menos de 2 minutos.
- Proporcionar consejos claros y accionables.
- Utilizar el siguiente formato para las prioridades:
    - **1. [Nivel de Prioridad] Nombre de la Tarea** (est: Tiempo)
    - Breve justificación.
-->
