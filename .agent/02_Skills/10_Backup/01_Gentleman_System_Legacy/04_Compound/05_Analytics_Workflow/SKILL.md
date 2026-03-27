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

---

## Remotion Best Practices (Merged: 2026-03-18)

### Cuándo usar

Utiliza este skill cuando trabajes con código Remotion para obtener conocimiento específico del dominio.

### Subtítulos/Captions

Cuando trabajes con subtítulos, carga el archivo [./rules/subtitles.md](./rules/subtitles.md) para más información.

### Usando FFmpeg

Para algunas operaciones de video como trimming o detección de silencio, usa FFmpeg. Carga el archivo [./rules/ffmpeg.md](./rules/ffmpeg.md) para más información.

### Visualización de Audio

Cuando necesites visualizar audio (barras de espectro, waveforms, efectos reactivos al bass), carga el archivo [./rules/audio-visualization.md](./rules/audio-visualization.md).

### Cómo usar

Lee los archivos individuales de reglas para explicaciones detalladas y ejemplos de código:

- [rules/3d.md](rules/3d.md) - Contenido 3D en Remotion usando Three.js y React Three Fiber
- [rules/animations.md](rules/animations.md) - Habilidades fundamentales de animación para Remotion
- [rules/assets.md](rules/assets.md) - Importando imágenes, videos, audio y fuentes en Remotion
- [rules/audio.md](rules/audio.md) - Usando audio y sonido en Remotion
- [rules/calculate-metadata.md](rules/calculate-metadata.md) - Establecer dinámicamente duración, dimensiones y props de composición
- [rules/can-decode.md](rules/can-decode.md) - Verificar si un video puede ser decodificado por el navegador
- [rules/charts.md](rules/charts.md) - Patrones de gráficos y visualización de datos para Remotion
- [rules/compositions.md](rules/compositions.md) - Definiendo composiciones, stills, carpetas
- [rules/extract-frames.md](rules/extract-frames.md) - Extraer frames de videos
- [rules/fonts.md](rules/fonts.md) - Cargar Google Fonts y fuentes locales
- [rules/get-audio-duration.md](rules/get-audio-duration.md) - Obtener duración de audio
- [rules/get-video-dimensions.md](rules/get-video-dimensions.md) - Obtener dimensiones de video
- [rules/get-video-duration.md](rules/get-video-duration.md) - Obtener duración de video
- [rules/gifs.md](rules/gifs.md) - Mostrar GIFs sincronizados con la línea de tiempo
- [rules/images.md](rules/images.md) - Insertar imágenes en Remotion
- [rules/light-leaks.md](rules/light-leaks.md) - Efectos de light leak overlay
- [rules/lottie.md](rules/lottie.md) - Insertar animaciones Lottie
- [rules/measuring-dom-nodes.md](rules/measuring-dom-nodes.md) - Medir dimensiones de elementos DOM
- [rules/measuring-text.md](rules/measuring-text.md) - Medir dimensiones de texto
- [rules/sequencing.md](rules/sequencing.md) - Patrones de secuenciación
- [rules/tailwind.md](rules/tailwind.md) - Usando TailwindCSS en Remotion
- [rules/text-animations.md](rules/text-animations.md) - Patrones de animación de texto
- [rules/timing.md](rules/timing.md) - Curvas de interpolación
- [rules/transitions.md](rules/transitions.md) - Patrones de transición de escenas
- [rules/transparent-videos.md](rules/transparent-videos.md) - Renderizar videos con transparencia
- [rules/trimming.md](rules/trimming.md) - Patrones de trimming
- [rules/videos.md](rules/videos.md) - Insertar videos en Remotion
- [rules/parameters.md](rules/parameters.md) - Hacer un video parametrizable con Zod
- [rules/maps.md](rules/maps.md) - Agregar un mapa usando Mapbox