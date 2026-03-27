# 📄 11 — Doc Processing

> **Skills de extracción y procesamiento documental.**  
> **Última actualización:** 2026-03-23

---

## Skills en esta categoría

| # | Skill | Script | Propósito |
|---|-------|--------|-----------|
| 01 | [01_Universal_Doc_Reader](./01_Universal_Doc_Reader/) | `83_Universal_Parser.py` | Extracción individual de archivos |
| 02 | [02_Batch_Doc_Processor](./02_Batch_Doc_Processor/) | `84_Batch_Parser.py` | Procesamiento masivo de directorios |
| 03 | [03_Resumen_Extractor](./03_Resumen_Extractor/) | `85_Resumen_Extractor.py` | Extracción de CVs y resúmenes |

---

## Scripts asociados

| Script | Ubicación | Función |
|--------|-----------|---------|
| `83_Universal_Parser.py` | `08_Scripts_Os/` | Motor de extracción individual |
| `84_Batch_Parser.py` | `08_Scripts_Os/` | Orquestador batch |
| `85_Resumen_Extractor.py` | `08_Scripts_Os/` | Extracción de CVs/resúmenes |

---

## Formatos soportados

```
Documentos: PDF, DOCX, DOC
Tablas:     XLSX, XLS, CSV
Presentac.: PPTX
Diseño:     PSD, PSB
Imágenes:  TIFF, JPG, PNG, WEBP
Texto:      MD, TXT
```

---

## Uso rápido

```bash
# Extraer archivo individual
python 08_Scripts_Os/83_Universal_Parser.py <archivo>

# Batch - directorio completo
python 08_Scripts_Os/84_Batch_Parser.py <directorio> --recursive

# Extraer CVs/resúmenes
python 08_Scripts_Os/85_Resumen_Extractor.py --source <dir>
```

---

## Perfiles donde aplica

| Perfil | Uso |
|--------|-----|
| **05_Vibe_Coding** | Extracción de docs para proyectos |
| **04_Product_Design** | Documentación de specs |
| **03_Product_Manager** | Extracción de requirements |

---
_Categoría: 2026-03-23_
