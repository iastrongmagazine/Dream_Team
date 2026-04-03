---
title: "fix: Integrar Auto Improvement con System Guardian"
type: fix
status: active
date: 2026-03-30
origin: 00_Plan_Automejora_Recursiva_v6.1.md
---

# Plan: Integrar Auto Improvement con System Guardian

## Overview

Completar FASE 2 del plan de Automejora Recursiva integrando el motor de Auto Improvement con el System Guardian existente.

## Problem Frame

El plan de Automejora Recursiva v6.1 estableció 4 fases:
- FASE 1: Fundación ✅
- FASE 2: Motor ⚠️ (falta System Guardian)
- FASE 3: Aprendizaje ✅
- FASE 4: Evolución ✅

La integración con System Guardian está pendiente.

## Requirements Trace

- R1. Auto Improvement debe ejecutarse desde System Guardian
- R2. System Guardian debe mostrar resultados del Auto Improvement
- R3. Integración con hooks de sesión (stop.py)

## Scope Boundaries

- NO modificar el core de System Guardian (79_System_Guardian.py)
- NO modificar la arquitectura del Auto Improvement
- SÍ integrar mediante CLI commands

## Context & Research

### Relevant Code and Patterns

- `08_Scripts_Os/Legacy_Backup/79_System_Guardian.py` - System Guardian existente
- `04_Operations/01_Auto_Improvement/01_Engine/recursive_improvement_engine.py` - Auto Improvement
- `01_Core/07_Hooks/03_Lifecycle/stop.py` - Hook con integración Guardian

### External References

- CLI interface del Auto Improvement ya existe
- Hook de stop.py ya tiene flag `--guardian`

## Key Technical Decisions

- **Decision**: Usar CLI commands en lugar de imports directos
- **Rationale**: Mantiene desacoplamiento entre módulos

## Open Questions

### Resolved During Planning

- Q: ¿Cómo invocar Auto Improvement desde System Guardian?
- R: Mediante CLI: `python 04_Operations/01_Auto_Improvement/01_Engine/recursive_improvement_engine.py --scan`

### Deferred to Implementation

- Ninguno

## Implementation Units

- [ ] **Unit 1: Verificar CLI de Auto Improvement funciona**

**Goal:** Confirmar que el CLI puede ejecutarse independientemente

**Files:**
- Test: `python 04_Operations/01_Auto_Improvement/01_Engine/recursive_improvement_engine.py --scan`

**Verification:**
- Output muestra "Issues detectados" sin errores

---

- [ ] **Unit 2: Agregar comando en System Guardian**

**Goal:** Añadir opción para ejecutar Auto Improvement desde System Guardian

**Dependencies:** Unit 1

**Files:**
- Modify: `08_Scripts_Os/Legacy_Backup/79_System_Guardian.py`

**Approach:**
- Añadir opción en menú: "Auto Improvement Scan"
- Ejecutar CLI y capturar output
- Mostrar resultados en reporte

**Test scenarios:**
- Ejecutar desde System Guardian muestra resultados

**Verification:**
- Output de System Guardian incluye Auto Improvement

---

- [ ] **Unit 3: Verificar hook stop.py funciona con --guardian**

**Goal:** Confirmar que el hook de sesión ejecuta Auto Improvement

**Dependencies:** Unit 1

**Files:**
- Modify: `01_Core/07_Hooks/03_Lifecycle/stop.py` (ya tiene lógica)

**Test scenarios:**
- Ejecutar stop.py --guardian ejecuta scan

**Verification:**
- Hook ejecuta y muestra resultados

---

## System-Wide Impact

- **Interaction**: System Guardian llama a Auto Improvement
- **Error propagation**: Si Auto Improvement falla, Guardian continúa

## Risks & Dependencies

- Dependencia: Python con path correcto
- Riesgo: Encoding issues en Windows (ya resueltos en Engine)

## Documentation / Operational Notes

- No requiere documentación adicional
- CLI ya documentado en el engine

## Sources & References

- Origin: [00_Plan_Automejora_Recursiva_v6.1.md](file:///c:/Users/sebas/Downloads/01%20Revisar/09%20Versiones/00%20Respaldo%20PC%20Sebas/01%20Github/personal-os/Think_Different/00_Plan_Automejora_Recursiva_v6.1.md)
- Related code: 79_System_Guardian.py, recursive_improvement_engine.py
