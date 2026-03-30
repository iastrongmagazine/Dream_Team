---
name: Elite Agent Auditor
description: Sistema de auditoría continua de nivel industrial para garantizar la calidad, seguridad y cumplimiento de estándares en agentes y scripts.
---

# 🕵️ Elite Agent Auditor

Esta Skill formaliza la inspección de calidad de los agentes del sistema, utilizando motores de análisis estático y dinámico para asegurar que cada línea de código cumpla con los estándares de **PersonalOS** y **Silicon Valley**.

## 🚀 Triggers

- "Audita esta nueva Skill que acabo de crear."
- "Revisa la calidad del script X en Engine."
- "¿Cumplen mis agentes con el estándar de Silicon Valley?"
- "Realiza una revisión de visión sobre este componente."

## 🛠️ Workflow: The Auditor Way

### 1. Análisis de Capas (Armor Layer Scan)
El auditor verifica la robustez técnica:
- **Rutas Absolutas**: Validación dinámica de directorios.
- **Manejo de Errores**: Verificación de bloques `try-except` y logging.
- **Type Hinting**: Asegurar tipado fuerte en Python.

### 2. Auditoría de Estándares (Valley Standards)
Integración directa con los motores de `04_Operations`:
- **Silicon Valley Auditor (`31_Silicon_Valley_Auditor.py`)**: Valida docstrings, PEP 8 y complejidad ciclomática.
- **AIPM Evaluator (`23_AIPM_Evaluator.py`)**: Mide la salud y cobertura del ecosistema AIPM.
- **Vision Review (`04_Vision_Review.py`)**: Simula múltiples perspectivas de revisión (Dev, Ops, Sec, Biz).

### 3. Emisión de Certificado (Grade Elite)
No es solo un log; es un veredicto:
- Genera un archivo `.md` con el score y los "Critical Fixes".
- Clasifica como **ELITE**, **PASS** o **FAIL**.

## 📋 Instrucciones de Ejecución

1. **Identificar**: Determinar el objetivo (Directorio, Archivo o Skill).
2. **Ejecutar Motores**: Correr los scripts de auditoría en paralelo si es posible.
3. **Sintetizar**: Crear un reporte consolidado (Dashboard) fácil de leer.
4. **Notificar**: Informar al usuario sobre los riesgos detectados y el camino a la perfección.

> [!IMPORTANT]
> Un score menor a 8/10 requiere corrección inmediata para mantener el sistema en **PURE GREEN**.

---
*Alineado con el Motor PersonalOS: "Indestructible por diseño, superior por estética."*
