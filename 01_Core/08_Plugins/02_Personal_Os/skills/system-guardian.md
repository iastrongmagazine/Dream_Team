---
name: "system-guardian"
description: "System Guardian - Validación automática de estructura, nombres, links y más"
---

# System Guardian

El System Guardian valida automáticamente la integridad del proyecto.

## Comandos

```bash
gr              # Dry-run - solo mostrar issues
gr --apply      # Aplicar fixes automáticos
gr --agents     # Ejecutar 3 agents de validación
```

## Qué Valida

### 1. Estructura de Carpetas
- Verifica que existan carpetas 00-08
- Nombres con formato: XX_Nombre/

### 2. Convenciones de Nombres
- Archivos: XX_Nombre.ext
- Sin espacios, sin caracteres especiales

### 3. Links Rotos
- Busca referencias a archivos que no existen
- Markdown links rotos

### 4. Archivos Huérfanos
- Archivos sin referencias en README

## Integración

El System Guardian se ejecuta:
- Al iniciar sesión (opcional)
- Antes de commit (via GGA)
- Manual cuando se requiera

## Personalización

Para agregar más validaciones, editar:
`08_Scripts_Os/01_Auditor_Hub.py`
