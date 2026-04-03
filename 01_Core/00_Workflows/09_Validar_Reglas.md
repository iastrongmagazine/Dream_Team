---
name: validar
description: Valida el cumplimiento estricto de reglas y estándares del sistema.
argument-hint: "[opcional: regla o archivo específico a validar]"
---

# Workflow: Validación Estricta de Reglas

Este workflow asegura que el código y la estructura del proyecto PersonalOS cumplan con los estándares de **Armor Layer**, **Vitaminización** y **Naming Conventions**.

## Prerrequisitos

- Python instalado y en el PATH.
- Dependencias: `colorama` (opcional, incluida en entorno estándar).

## Pasos

1. **Ingesta de Contexto (CRÍTICO)**
   Antes de cualquier validación técnica, el agente debe:
   - **Leer todas las reglas** en `01_Core/01_Rules/`.
   - **Internalizar** los conceptos de _Armor Layer_, _Vitaminización_ y _Naming Conventions_.
   - Asegurar que cualquier código a validar cumple con la **intención** de la regla, no solo la sintaxis.

2. **Ejecutar Validador Maestro**
   El script `40_Validate_Rules.py` realiza un chequeo técnico exhaustivo y muestra el catálogo de reglas activas.

   ```bash
   python 08_Scripts_Os/05_Validator_Hub.py
   ```

3. **Revisión de Reporte**
   - Si el script termina en **VERDE** (Éxito), el sistema es compliant.
   - Si termina en **ROJO** (Error), revisar los logs para corregir:
     - Nombres de archivos en `08_Scripts_Os` (deben ser `NN_snake_case.py`).
     - Estructura de `.mdc` en `01_Core/01_Rules` (campos `description`, `globs`).

## Integración con Ritual de Cierre

Este proceso se ejecuta automáticamente como parte de `08_Scripts_Os/04_Ritual_Hub.py`.
