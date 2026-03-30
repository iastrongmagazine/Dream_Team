# Plan: Fusión Completa + Reenumeración Hubs 01-10

> **Sobre este Plan:** Transformar los Hubs 91-100 en Hubs autónomos 01-10, eliminando dependencia de Legacy_Backup y reorganizando la estructura del Engine.

---

## 1. Visión General de la Tarea

### Título de la Tarea

**Fusión Completa + Reenumeración Hubs O4 Engine (01-10)**

### Declaración del Objetivo

## **Objetivo:** Transformar los 10 Hubs del O4 Engine (actualmente 91-100) en Scripts autónomos (01-10) que no dependan de carpetas Legacy, fusionando el código de los scripts individuales dentro de cada Hub y archivando los scripts redundantes.

---

## 2. Análisis del Proyecto y Estado Actual

### Tecnología y Arquitectura

- **Sistema Operativo:** PersonalOS (Think Different AI)
- **Lenguaje:** Python 3.14+
- **Estructura Actual:**
  - `08_Scripts_Os/` - Scripts principales + Hubs 91-100
  - `Legacy_Backup/` - ~80 scripts individuales (backward compatibility)
  - `AIPM_Fixed/` - 5 scripts AIPM corregidos
- **Patrón Arquitectónico:** Compound Hubs + Legacy Backup

### Estado Actual

| Componente | Estado |
|------------|--------|
| 91_Auditor_Hub | ✅ FUSIONADO (funciones internas) |
| 92_Git_Hub | ✅ FUSIONADO (funciones internas) |
| 93_AIPM_Hub | ⚠️ Wrapper →依赖 Legacy/AIPM_Fixed |
| 94_Ritual_Hub | ⚠️ Wrapper →依赖 Legacy_Backup |
| 95_Validator_Hub | ⚠️ Wrapper →依赖 Legacy_Backup |
| 96_Tool_Hub | ⚠️ Wrapper →依赖 Legacy_Backup |
| 97_Integration_Hub | ⚠️ Wrapper →依赖 Legacy_Backup |
| 98_Workflow_Hub | ⚠️ Wrapper →依赖 Legacy_Backup |
| 99_Data_Hub | ⚠️ Wrapper →依赖 Legacy_Backup |
| 100_General_Hub | ⚠️ Sin función clara |

---

## 3. Contexto y Definición del Problema

### Definición del Problema

**Pain Points:**
1. Los Hubs 93-99 dependen de scripts en `Legacy_Backup/` - si se archivan, los Hubs se rompen
2. Hay duplicación: mismos scripts en raíz + en Legacy_Backup
3. Numeración inconsistente: 91-100 vs 00-90

### Criterios de Éxito

- [ ] Los 10 Hubs (01-10) funcionan SIN依赖 de Legacy_Backup/
- [ ] Todos los scripts individuales están archivados o eliminados
- [ ] Validación `91_Auditor_Hub.py estructura` pasa con 0 errores
- [ ] README.md actualizado con nuevos comandos
- [ ] tree.txt actualizado con nueva estructura

---

## 4. Contexto del Modo de Desarrollo

- **🚨 Etapa del Proyecto:** Refactorización de sistema existente
- **Cambios Disruptivos:** SI - reorganización completa de estructura
- **Manejo de Datos:** No aplica (solo scripts)
- **Base de Usuarios:** Sistema interno PersonalOS
- **Prioridad:** Estabilidad > Velocidad

---

## 5. Requisitos Técnicos

### Requisitos Funcionales

1. **Fusión de Hubs 93-99:**
   - 93_AIPM_Hub: Integrar funciones de AIPM (logger, evaluator, control, report)
   - 94_Ritual_Hub: Integrar funciones de rituales (cierre, standup, weekly)
   - 95_Validator_Hub: Integrar funciones de validación (stack, rules, linter)
   - 96_Tool_Hub: Integrar funciones de herramientas
   - 97_Integration_Hub: Integrar funciones de integración
   - 98_Workflow_Hub: Integrar funciones de workflows
   - 99_Data_Hub: Integrar funciones de datos

2. **Reenumeración:**
   - Renombrar 91→01_Auditor_Hub.py
   - Renombrar 92→02_Git_Hub.py
   - ...hasta 100→10_General_Hub.py

3. **Gestión de Scripts Individuales:**
   - Mover scripts 00-09 a Legacy_Backup/ (si no están ya)
   - Eliminar duplicados raíz vs Legacy
   - Opcional: Archivar en 06_Archive/

### Requisitos No Funcionales

- **Rendimiento:** Scripts deben ejecutarse < 5 segundos
- **Seguridad:** No exponer paths internos
- **Usabilidad:** Comandos intuitivos y bien documentados

---

## 6. Plan de Implementación

### Fase 1: Fusión de Hubs 93-99

| Orden | Hub | Scripts a Fusionar | Complejidad |
|-------|-----|-------------------|-------------|
| 1 | 93_AIPM_Hub | 22, 23, 24, 28, 30 | Alta |
| 2 | 94_Ritual_Hub | 08, 09, 14, 15, 17 | Media |
| 3 | 95_Validator_Hub | 13, 37, 40, 80 | Baja |
| 4 | 96_Tool_Hub | 01, 02, 39 | Baja |
| 5 | 97_Integration_Hub | 46, 75, 76 | Media |
| 6 | 98_Workflow_Hub | 01, 02, 06, 07, 73 | Alta |
| 7 | 99_Data_Hub | 19, 20, 84, 85, 86 | Media |

### Fase 2: Reenumeración

| Original | Nuevo |
|----------|-------|
| 91_Auditor_Hub.py | 01_Auditor_Hub.py |
| 92_Git_Hub.py | 02_Git_Hub.py |
| 93_AIPM_Hub.py | 03_AIPM_Hub.py |
| 94_Ritual_Hub.py | 04_Ritual_Hub.py |
| 95_Validator_Hub.py | 05_Validator_Hub.py |
| 96_Tool_Hub.py | 06_Tool_Hub.py |
| 97_Integration_Hub.py | 07_Integration_Hub.py |
| 98_Workflow_Hub.py | 08_Workflow_Hub.py |
| 99_Data_Hub.py | 09_Data_Hub.py |
| 100_General_Hub.py | 10_General_Hub.py |

### Fase 3: Limpieza

- Mover scripts 00-09 a Legacy_Backup/
- Eliminar duplicados
- Actualizar referencias en código

---

## 7. Estructura de Archivos

### Archivos a Modificar

| Archivo | Acción |
|---------|--------|
| 91_Auditor_Hub.py | Renombrar → 01_Auditor_Hub.py |
| 92_Git_Hub.py | Renombrar → 02_Git_Hub.py |
| 93_AIPM_Hub.py | Renombrar + Fusionar → 03_AIPM_Hub.py |
| 94_Ritual_Hub.py | Renombrar + Fusionar → 04_Ritual_Hub.py |
| 95_Validator_Hub.py | Renombrar + Fusionar → 05_Validator_Hub.py |
| 96_Tool_Hub.py | Renombrar + Fusionar → 06_Tool_Hub.py |
| 97_Integration_Hub.py | Renombrar + Fusionar → 07_Integration_Hub.py |
| 98_Workflow_Hub.py | Renombrar + Fusionar → 08_Workflow_Hub.py |
| 99_Data_Hub.py | Renombrar + Fusionar → 09_Data_Hub.py |
| 100_General_Hub.py | Renombrar → 10_General_Hub.py |

### Archivos a Eliminar/Mover

| Archivo | Acción |
|---------|--------|
| 00-09_*.py | Mover a Legacy_Backup/ |
| Legacy_Backup/ duplicados | Eliminar |
| AIPM_Fixed/ | Eliminar (fusionado) |

---

## 8. Riesgos y Mitigaciones

| Riesgo | Mitigación |
|--------|------------|
| Romper Hubs durante fusión | Probar cadaHub antes de pasar al siguiente |
| Perder funcionalidad | Mantener backup hasta validar |
| Referencias rotas | Actualizar todos los paths en README |

---

## 9. Comando Final de Validación

```bash
python 04_Engine/08_Scripts_Os/01_Auditor_Hub.py estructura
# Esperado: 0 errores
```

---

## 10. Estado de Avance

| Fase | Estado |
|------|--------|
| Auditoría inicial | ✅ Completado |
| Fusión 91-92 | ✅ Completado |
| Fusión 93-99 | 🔲 Pendiente |
| Reenumeración | 🔲 Pendiente |
| Limpieza | 🔲 Pendiente |
| Validación final | 🔲 Pendiente |

---

**¿Ejecutamos este plan?**
