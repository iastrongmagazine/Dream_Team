# 🦾 Skill 11_02: Batch Doc Processor Elite

## Esencia Original
> **Propósito:** Realizar extracciones masivas de información de directorios enteros con consolidación automática
> **Flujo:** Escanear directorio → Parsear archivos → Consolidar resultados → Generar reporte único


> **Sistema:** PersonalOS  
> **Categoría:** 11_Doc_Processing  
> **Skill:** 02/03  
> **Versión:** 2.0  
> **Última actualización:** 2026-03-23

## Overview

Esta Skill permite realizar extracciones masivas de información de directorios enteros. Utiliza el motor `84_Batch_Parser.py` para iterar sobre archivos compatibles y generar un reporte consolidado en Markdown.

## 🚀 Capacidades

- **Escaneo Recursivo:** Navega por subcarpetas automáticamente
- **Consolidación:** Agrupa salida de múltiples archivos en un solo documento
- **Soporte Universal:** Compatible con todos los formatos de Skill 83

## 🛠️ Uso

```bash
# Uso básico - directorio actual
python 08_Scripts_Os/84_Batch_Parser.py <directorio>

# Con recursividad
python 08_Scripts_Os/84_Batch_Parser.py <directorio> --recursive

# Con output específico
python 08_Scripts_Os/84_Batch_Parser.py <directorio> -o reporte.md

# Ejemplo completo
python 08_Scripts_Os/84_Batch_Parser.py ./docs --recursive -o mi_reporte.md
```

## 🤝 Integración con el Sistema

### Skills relacionadas:
- **Skill 83:** Universal Doc Reader (análisis individual)
- **Skill 85:** Resumen Extractor (extracción de CVs)

### Flujo:
```
Directorio → 84_Batch_Parser.py → 83_Universal_Parser.py (por archivo)
                                                    ↓
                                          Reporte Markdown consolidado
                                                    ↓
                                    03_Knowledge/
```

## 📦 Dependencias

```bash
# Requiere Skill 83
pip install PyPDF2 python-docx pandas python-pptx psd-tools Pillow
```

## ✅ Checklist de Calidad

- [x] UTF-8 encoding
- [x] Escaneo recursivo
- [x] Manejo de errores por archivo
- [x] Metadata JSON del batch
- [x] Integración con config_paths.py

---
_Alineado con PersonalOS: "Del archivo individual al conocimiento sistémico."_
