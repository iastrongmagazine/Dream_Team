# 🦾 Skill 11_03: Resumen Extractor

## Esencia Original
> **Propósito:** Extraer contenido de documentos para crear resúmenes estructurados y bases de conocimiento
> **Flujo:** Escanear recursivamente → Extraer contenido → Generar resúmenes → Consolidar reporte


> **Sistema:** PersonalOS  
> **Categoría:** 11_Doc_Processing  
> **Skill:** 03/03  
> **Versión:** 2.0  
> **Última actualización:** 2026-03-23

## Overview

Extrae contenido de documentos específicos para crear resúmenes estructurados. Procesa directorios completos recursivamente y genera un reporte consolidado de conocimiento.

**Caso de uso:** Extracción de CVs, certificados, diplomas para crear bases de conocimiento.

## 🚀 Capacidades

- **Escaneo Recursivo:** Navega por subcarpetas automáticamente
- **Consolidación:** Genera un único reporte con todos los documentos
- **Soporte:** PDF, DOCX, XLSX, CSV, PPTX

## 🛠️ Uso

```bash
# Uso básico
python 08_Scripts_Os/85_Resumen_Extractor.py

# Directorio específico
python 08_Scripts_Os/85_Resumen_Extractor.py --source ./documentos

# Output específico
python 08_Scripts_Os/85_Resumen_Extractor.py -s ./docs -o mi_resumen.md
```

## 🤝 Integración con el Sistema

### Skills relacionadas:
- **Skill 83:** Universal Doc Reader (motor base)
- **Skill 84:** Batch Doc Processor (procesamiento masivo general)

### Flujo:
```
Documentos → 85_Resumen_Extractor.py → 83_Universal_Parser.py
                                           ↓
                                 Resumen_MD + Metadata.json
                                           ↓
                           03_Knowledge/
```

## 📦 Dependencias

```bash
# Requiere Skill 83
pip install PyPDF2 python-docx pandas python-pptx
```

## ✅ Checklist de Calidad

- [x] UTF-8 encoding
- [x] Timeout por archivo (120s)
- [x] Manejo de errores robusto
- [x] Log de progreso
- [x] Integración con config_paths.py

---
_Alineado con PersonalOS: "Del caos al conocimiento estructurado."_
