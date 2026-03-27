---
name: Invoice Intelligence (OCR)
description: Sistema profesional de procesamiento paralelo de facturas con OCR. Extrae datos clave (montos, fechas, items, proveedores) de PDFs y los organiza automáticamente. Diseñado para alta fidelidad y rendimiento usando Tesseract y procesamiento paralelo. Triggers on: 12_Invoice_Intelligence, patterns, coding.
---

# 📑 Skill 49: Invoice Intelligence (OCR)

Sistema de grado industrial para la extracción y organización de datos financieros desde documentos PDF.

## 🎯 Capacidades Clave

- **Procesamiento Paralelo**: Despliegue de 1 worker por factura para velocidad máxima.
- **OCR Robusto**: Motor Tesseract configurado para Español e Inglés.
- **Extracción Estructurada**: Captura de Vendor, Cliente, Fecha, Montos (Base, Tax, Total) e Items line-by-line.
- **Auto-Organización**: Clasificación automática de archivos financieros en carpetas `YYYY-MM`.
- **Exportación Multi-formato**: Resultados en CSV, Excel formateado y JSON detallado.

## 🛠️ Herramientas Incluidas

- `invoice_processor.py`: Motor principal de procesamiento.
- `dashboard.py`: Visualización HTML de estadísticas de facturación.
- `advanced_examples.py`: Integración mejorada con LLMs para precisión quirúrgica.
- `test_invoice_system.py`: Generador de facturas sintéticas para pruebas.

## 🚀 Uso Rápido

### Procesamiento de Lote

```bash
python scripts/invoice_processor.py [ruta_directorio_facturas]
```

### Generación de Dashboard

```bash
python scripts/dashboard.py
```

## ⚖️ Leyes de la Skill

1. **Armor Layer**: Siempre usar rutas absolutas para directorios de entrada/salida.
2. **Signal-to-Noise**: Solo reportar confianza de OCR si es inferior al 85% o si hay errores críticos.
3. **Pure Green**: El script debe validar la existencia de `tesseract` antes de iniciar el procesamiento masivo.

## 📁 Estructura

- `scripts/`: Motores de ejecución vitaminizados.
- `LEGACY_README.md`: Documentación original del sistema.
- `QUICKSTART.txt`: Guía visual rápida.

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
