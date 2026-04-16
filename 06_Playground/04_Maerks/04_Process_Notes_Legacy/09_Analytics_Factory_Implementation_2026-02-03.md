# Nota de Proceso: Implementación Universal Analytics Factory

* *Fecha**: 2026-02-03
* *ID**: 09

## Resumen de la Sesión

Se transformó el módulo de análisis de salud en una **Universal Data Analytics Factory** capaz de procesar cualquier rubro (Salud, Ventas, Marketing) mediante detección dinámica de dominios y generación de scripts a partir de plantillas.

- **Estándar v4.2 (Domain-Aware Intelligence)**: Evolución del motor para adaptar visualizaciones y ratios según el rubro detectado (Salud, Ventas, Marketing).

## Hitos Alcanzados

1.  **Detección Dinámica**: Implementación de `13_Master_Analytics_Factory.py` con meta-análisis de cabeceras CSV.
2.  **Plantillas DRY v4.2**: Refactorización de `base_template.py.tmpl` para inyectar `primary_intensity` y ratios contextuales (CPA vs Margin).
3.  **Reglas "Pure Green"**:
    - `00_plan_first_es.mdc`: Obliga planificación en español.
    - `01_report_progress_es.mdc`: Obliga reporte cada 10%.
4.  **Power Dash v4.2**: Visualizaciones inteligentes que cambian su eje principal (e.g., 'age' en salud, 'revenue' en ventas) automáticamente.
5.  **Organización Tiered**: Clasificación de ejemplos por niveles (01_Salud, 02_Ventas, 03_Marketing) dentro de `06_ENGINE/analytics_output/`.

## Lecciones Aprendidas

- **El Contexto es el multiplicador de valor**: Un gráfico sin una métrica de intensidad adecuada al dominio (ej: edad en salud) pierde el 80% de su utilidad de negocio.
- **Resiliencia de Rutas**: Los motores de análisis deben usar rutas de salida relativas al proyecto para ser portables, evitando rutas absolutas o de carpetas externas no garantizadas.
- **Estandarización de Gráficos**: El uso de un `primary_intensity` universal permite que 10 gráficos diferentes se mantengan coherentes entre sí sin intervención manual.

## Reporte Final de Ejecución (Pure Green)

- **Validación Salud**: Exitosa (v4.2) - Detectado como 'Salud', Intensidad: `age`.
- **Validación Ventas**: Exitosa (v4.2) - Detectado como 'Ventas', Intensidad: `revenue`, Ratios: `Margin`, `Avg_Ticket`.
- **Validación Marketing**: Exitosa (v4.2) - Detectado como 'Marketing', Intensidad: `conversions`, Ratios: `CPA`, `CTR`.
- **Orquestación**: Uso de `AnalyticsFactory` para centralizar la lógica de negocio y delegar la ejecución a scripts especializados.

## Reglas Aprendidas (Cursor Rules Proposal)

- **Standard of Domain Intelligence**: Todo motor de análisis debe definir una heurística de detección de dominio y una métrica de intensidad primaria.
- **Data Transparency**: Obligatorio el uso de `Rug Plots` y `Boxplot+Stripplot` para revelar la distribución real de los datos detrás de los promedios.
- **Contextual Ratio Engineering**: No calcular ratios genéricos; inyectar lógica de negocio (CPA para Marketing, Margen para Ventas).

## Próximos Pasos (Backlog)

- [x] Implementar v4.2 con Inteligencia Multi-Dominio.
- [ ] Expandir templates para visualizaciones complejas (seaborn/plotly).
- [ ] Implementar análisis predictivo básico en la Factory.
- [ ] Integrar con Skill de Notificaciones para enviar reportes automáticos.
