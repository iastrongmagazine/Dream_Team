---
name: health-data-analyst
description: Workflow diseñado para Analista de Datos de Salud, aplicando principios DRY y KISS. Incluye limpieza, análisis poblacional y visualización. Triggers on: 13_Health_Data_Analyst, patterns, coding.
---

# Workflow Analista de Datos Salud

Para cumplir con los principios DRY (no te repitas) y KISS (mantenlo simple), este workflow modular en Python integra funciones reutilizables que se pueden invocar en orden.

## Fase 1: Limpieza y Estandarización (Aplicando DRY)

**Objetivo:** Crear una única "fuente de verdad" para la calidad de los datos.

En lugar de limpiar cada columna manualmente, creamos un "limpiador universal" para datos médicos.

```python
# scripts/clean_healthcare_data.py
import pandas as pd

def clean_healthcare_data(df):
    """
    Función única para estandarizar datasets de salud.
    """
    # 1. KISS: Formateo de fechas consistente
    date_cols = [col for col in df.columns if 'date' in col.lower()]
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    # 2. DRY: Manejo de nulos según tipo de dato
    for col in df.columns:
        if df[col].dtype == 'object' or pd.api.types.is_string_dtype(df[col]):
            df[col] = df[col].fillna('Unknown').astype(str).str.strip().str.title()
        elif col not in date_cols:
            df[col] = df[col].fillna(0)

    return df
```

## Fase 2: Análisis de Población (Aplicando KISS)

**Objetivo:** Obtener respuestas claras sobre la salud de la población.

Evita métricas complejas que nadie entiende. Enfócate en lo que los stakeholders necesitan.

```python
# scripts/calc_population_metrics.py
def get_population_insights(df):
    """
    Calcula KPIs clave de salud poblacional.
    """
    insights = {
        "total_pacientes": len(df),
        "promedio_edad": df['age'].mean(),
        "casos_por_region": df['region'].value_counts().to_dict(),
        "tasa_prioridad_alta": (df['priority'] == 'High').mean() * 100
    }
    return insights
```

## Fase 3: Visualización para Stakeholders (KISS)

**Objetivo:** Traducir datos complejos en decisiones.

La vacante pide "traducir datos complejos en insights accionables". Menos es más.

```python
# scripts/generate_health_dashboard.py
import matplotlib.pyplot as plt
import seaborn as sns

def plot_health_trends(df, target_col):
    """
    Genera un gráfico limpio y directo.
    """
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x=target_col, palette='viridis')
    plt.title(f'Distribución de {target_col.title()} en la Población')
    plt.ylabel('Cantidad de Pacientes')
    plt.xlabel(None)
    plt.tight_layout()
    plt.show()
```

## Orden de Ejecución Sugerido

1.  **Ingesta y Limpieza (clean_healthcare_data.py)**: Carga de datos y estandarización.
2.  **Análisis y KPIs (calc_population_metrics.py)**: Cálculo de métricas para validar calidad y obtener insights.
3.  **Visualización (generate_health_dashboard.py)**: Generación de gráficos para exportar a dashboards.

## Por qué este enfoque garantiza el éxito

- **Eficiencia (DRY):** Automatización de la limpieza para evitar errores y duplicidad.
- **Comunicación (KISS):** Métricas y gráficos simples y directos para stakeholders.
- **Foco en el Dominio:** Cuidado especial en la calidad y anotación de datos de salud.

## Esencia Original
> **Propósito:** Propósito del skill aquí
> **Flujo:** Pasos principales del flujo

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Error común
  - **Por qué**: Explicación
  - **Solución**: Cómo evitar

## 💾 State Persistence

Guardar en:
- `03_Knowledge/` — Documentación
- `02_Operations/` — Estado activo
