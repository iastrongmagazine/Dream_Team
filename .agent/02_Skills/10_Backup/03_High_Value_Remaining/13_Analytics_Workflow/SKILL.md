---
name: analytics-workflow
description: QUÉ HACE: Orquestador maestro para análisis de datos avanzado (limpieza, cohortes, visualización). CUÁNDO SE EJECUTA: Ante tareas complejas de datos CSV/Excel que requieran descubrimientos profundos o predicciones.
---

# Enhanced Analytics Workflow (Hub & Spoke)

Este skill es el "cerebro" para cualquier tarea compleja de datos. Utiliza una arquitectura de Hub & Spoke para delegar tareas pesadas a agentes especializados mientras mantiene un contexto limpio.

## Capacidades

- **Data Profiling**: Resumen estadístico automático.
- **Cohort Analysis**: Segmentación profunda de usuarios/entidades.
- **Data Enrichment**: Aumenta datasets con datos externos (Startups, Funding, etc.).
- **Visualización**: Genera diagramas de flujo y visualizaciones de datos.
- **Notebook Generation**: Produce un archivo `.ipynb` con todo el análisis documentado.

## Cuándo usarlo

- Cuando el usuario proporcione un CSV/Excel y pida un análisis profundo.
- Para predecir comportamientos (Churn, Conversión) basado en datos históricos.
- Para limpiar y enriquecer bases de datos fragmentadas.

## Instrucciones

### Paso 1: Identificar el objetivo

Pregunta al usuario: "¿Qué quieres descubrir en estos datos?" (ej. "Predecir éxito de startups", "Segmentar clientes por valor").

### Paso 2: Ejecutar el orquestador

Usa el script maestro para coordinar el trabajo:

```bash
python 02_Core/skills/enhanced_workflow_orchestrator.py <dataset.csv> --goal "<objetivo>" --context "<nombre_proyecto>"
```

### Paso 3: Entregar resultados

El script generará un Notebook y artifacts visuales. Proporciona al usuario el enlace al Notebook generado.

## Gobernanza de Datos

- **Notebook Obligatorio**: Todo análisis debe terminar en un `.ipynb`.
- **Explicabilidad**: Cada paso debe ser visualizado.
- **Aislamiento**: Las tareas pesadas se ejecutan en subprocesos para no saturar el contexto del agente principal.
