---
name: planificando-tareas-ai
description: GUÍA TÉCNICA: Crea planes de tareas estructurados y exhaustivos siguiendo el framework de ShipKit. ÚSALO CUANDO: El usuario pida planear una nueva funcionalidad, arreglar un bug complejo o estructurar un proyecto desde cero.
---

# Skill de Planificación de Tareas AI

Esta habilidad implementa el sistema de 5 pasos para el desarrollo impulsado por IA, enfocándose en la creación de documentos de tareas de alta fidelidad que sirven como contexto definitivo para los agentes ejecutores.

## Cuándo usar esta habilidad

- Cuando se inicia una nueva funcionalidad compleja.
- Antes de escribir cualquier código para un bug difícil de rastrear.
- Cuando el usuario dice "Planea esto", "Crea un plan para X" o "Usa la plantilla de planificación".
- **Trigger Especial:** "Ajuste de tareas" (Ver abajo).

## Flujo de Trabajo

1.  **Investigación Profunda**: Analiza el codebase actual, dependencias, esquemas de base de datos y patrones arquitectónicos. No asumas nada; verifica los archivos reales.
2.  **Análisis de Enfoques**: Considera al menos 2 o 3 formas de resolver el problema. Evalúa pros y contras.
3.  **Generación de la Recomendación**: Elige el mejor enfoque y justifica por qué es la solución técnica superior.
4.  **Redacción de la Tarea**: Crea un archivo en `03_Task/` usando la plantilla estándar. Asegúrate de incluir:
    - Criterios de éxito medibles.
    - Requisitos funcionales y no funcionales.
    - Análisis de impacto de segundo orden.
5.  **Revisión y Refinamiento**: Ajusta el plan según el feedback del usuario antes de proceder a la ejecución.

## Instrucciones para el Agente

- **Sé Exhaustivo**: Un plan vago produce código mediocre ("AI Slop"). El plan debe ser lo suficientemente detallado como para que un desarrollador junior pueda ejecutarlo sin preguntas.
- **Contexto Just-in-Time**: Carga solo los archivos relevantes para el problema específico para evitar saturar la ventana de contexto.
- **Detección de Consecuencias**: Identifica activamente qué partes del sistema podrían romperse con los cambios propuestos.

## Recursos

- **Plantilla**: [task_template.md](resources/task_template.md)
- **Script de Guía**: [03_AI_Task_Planner.py](../../08_Workflow/03_AI_Task_Planner.py)

---

## ⚡ Trigger: "Ajuste de tareas"

Este comando activa el **"AI Task Vitamin Injection"**.

### Protocolo de Ejecución (OBLIGATORIO)

Cuando el usuario invoque "Ajuste de tareas", el Agente debe seguir estrictamente estos pasos:

1.  **EJECUTAR SCRIPT**: Corre `python 08_Workflow/03_AI_Task_Planner.py`.
    - Esto escaneará `03_Task` y anexará el framework a las tareas que no lo tengan.
2.  **LEER** la salida del script para identificar qué archivos fueron actualizados.

3.  **BUCLE DE ANÁLISIS (Core Duty)**:
    - **Para CADA archivo actualizado:**
      - **LEE** el archivo completo.
      - **ANALIZA** el contexto del proyecto en relación a esa tarea.
      - **LLENA** la plantilla anexada al final.
      - **CRÍTICO:** No dejes secciones vacías. Si la tarea es "Integrar Stripe", el Agente debe llenar la sección de "Cambios en Datos" con los esquemas reales de Stripe, no con "TODO: ver docs".

> **Regla de Oro:** El script pone el esqueleto, el Agente pone el cerebro. Una plantilla vacía al final del archivo es un fallo de ejecución.

---

## Plantilla de Tarea (Estructura)

La tarea generada debe seguir estrictamente esta estructura:

1. **Visión General**: Título y Objetivo.
2. **Análisis del Proyecto**: Tecnología, Arquitectura y Estado Actual.
3. **Definición del Problema**: Pain points y Criterios de Éxito.
4. **Contexto de Desarrollo**: Prioridades, cambios disruptivos y manejo de datos.
5. **Requisitos Técnicos**: Funcionales, No Funcionales y Restricciones.
6. **Cambios en Datos**: Esquema, Modelos y Migración.
7. **Backend**: Patrones de acceso y Acciones del Servidor.
8. **Frontend**: Componentes, Páginas y Estado.
9. **Plan de Implementación**: Fases detalladas.
10. **Seguimiento**: Tracking de progreso en tiempo real.
11. **Estructura de Archivos**: Nuevos y Modificados.
12. **Instrucciones para Agentes**: Workflow de implementación y calidad.
13. **Análisis de Impacto**: Riesgos y performance.
