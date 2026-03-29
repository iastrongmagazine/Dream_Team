---
name: lfg-pro
description: Ciclo autónomo completo Silicon Valley Grade (18 pasos). Usar para features P0/P1 y cambios arquitectónicos.
argument-hint: "[descripción de la feature o tarea compleja]"
---

# 🌀 Workflow: LFG Pro (Doctor Strange — Full Power)

Ciclo de ingeniería autónomo de máxima calidad. Para features críticas, cambios arquitectónicos o trabajo P0/P1.
Ejecutar en orden. No saltarse pasos.

## 📋 Pasos de Ejecución

### FASE 1 — Contexto y Arquitectura

1. **Cargar contexto completo**: `AGENTS.md` + `01_Core/01_Rules/` + `04_Operations/00_Context_Memory/` + **Engram** + `04_Operations/03_Process_Notes/`
2. **Mapear impacto**: Identificar todos los archivos, módulos y dependencias afectados
3. **Brainstorm**: Ejecutar `01_Spider_Brainstorm` — explorar 2-3 enfoques antes de comprometerse
4. **Checkpoint 1**: Confirmar enfoque con el usuario antes de continuar

### FASE 2 — Plan y Tests

1. **Plan detallado**: Ejecutar `02_Professor_X_Plan` — plan formal en `03_Tasks/`
2. **Tests RED** *(si aplica)*: Escribir tests que fallen primero (TDD)
3. **Checkpoint 2**: Validar que el plan cubre todos los casos edge

### FASE 3 — Implementación

1. **Implementar**: Ejecutar `04_Thor_Work` — commits atómicos por fase
2. **Tests GREEN**: Confirmar que todos los tests pasan
3. **Resolver TODOs**: Cerrar todos los TODOs generados durante implementación

### FASE 4 — Calidad y Seguridad

1. **Linting**: `python 08_Scripts_Os/05_Validator_Hub.py --lint`
2. **Validar reglas**: `python 08_Scripts_Os/05_Validator_Hub.py --rules`
3. **Auditoría**: `python 08_Scripts_Os/01_Auditor_Hub.py` (si el cambio es mayor)
4. **Checkpoint 3**: Revisión de seguridad — OWASP Top 10 si hay endpoints o inputs

### FASE 5 — Revisión y Cierre

1. **Revisión completa**: Ejecutar `03_Vision_Review` — 13 agentes en paralelo
2. **Browser test** *(si hay UI)*: Screenshot antes/después con MCP Playwright
3. **Documentar**: Actualizar `01_Core/01_Inventario_Total.md` si hay nuevos scripts
4. **Cierre ritual**: `python 08_Scripts_Os/04_Ritual_Hub.py` → commit final → reportar `✅ DONE`

## ⚡ Cuándo usar Pro vs Lite

- **Pro**: Tasks P0/P1, features nuevas, cambios de arquitectura, trabajo crítico
- **Lite** (`06_AntMan_Lfg_Lite`): Tasks P2/P3, bugs simples, mejoras menores

---

© 2026 PersonalOS | Silicon Valley Grade Engineering.
