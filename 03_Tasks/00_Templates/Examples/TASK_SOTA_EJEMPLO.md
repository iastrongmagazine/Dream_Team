---
Title: Task Template SOTA - Ejemplo
Category: system_design
Priority: P1
Status: draft
Created_Date: 2026-03-20
Estimated_Effort: 4 hours
Dependencies: [Ninguna]
Tags:
  - system
  - skills
  - refactor
Resource_Refs:
  - 01_Brain/04_Rules/
  - 04_Agent_Teams_Lite/
  - 06_Taste_Skills/
---

# Task: Reestructurar Skills - Eliminar Duplicados

## Context

Reorganizar estructura de Skills en .agent/ para eliminar 89 duplicados entre 05_Gentleman y 07_Every.

## Next Actions

- [ ] Identificar skills duplicadas
- [ ] Definir versión winner
- [ ] Crear script validación
- [ ] Actualizar documentación
- [ ] Sincronizar cambios

## Progress Log

- 2026-03-20: Tarea creada

---

## 1. Task Overview

**Title:** Reestructurar Skills - Eliminar Duplicados

**Goal Statement:** Consolidar 89 skills duplicadas, estableciendo 07_Every como versión ACTIVA y 05_Gentleman como BACKUP histórico.

## 2. Project Analysis

**Tech Stack:**

| Componente                  | Valor                           |
|-----------------------------|---------------------------------|
| Framework                   | PersonalOS CLI                  |
| Lenguaje                    | Python 3.12                     |
| Base_Datos                  | N/A                             |
| UI                          | Terminal/Markdown               |
| Autenticación               | N/A                             |
| Arquitectura                | Scripts + Skills                |

**Current State:**
- 05_Gentleman: 98 skills (Mar 3-18)
- 07_Every: 98 skills (Mar 19-20)
- 89 duplicados identificados
- No hay proceso de validación

## 3. Problem & Success

**Problem Statement:**
Skills duplicadas en dos carpetas causando confusión sobre cuál usar.

**Success Criteria:**

- [ ] 89 duplicados mapeados
- [ ] 07_Every = ACTIVO
- [ ] 05_Gentleman = BACKUP
- [ ] Script validación creado
- [ ] Documentación actualizada

## 4. Development Mode

| Aspecto                        | Valor                             |
|--------------------------------|-----------------------------------|
| Project Stage                  | Feature / Refactor                |
| Breaking Changes               | Avoid (naming only)               |
| Data Handling                  | Preserve (no loss)                |
| User Base                      | AI Agents                         |
| Priority                       | Speed > Stability                 |

## 5. Requirements

**Functional Requirements:**

- Sistema detecta duplicados por nombre
- Sistema compara fechas de modificación
- Sistema determina versión winner
- Sistema genera reporte tabular

**Non-Functional Requirements:**

| Aspecto                   | Requisito                           |
|---------------------------|-------------------------------------|
| Performance               | <5 segundos                         |
| Security                  | Solo lectura                        |
| Usability                 | Output markdown claro               |

## 6. Data & Database

**Database Schema Changes:** N/A

**Data Model Updates:** N/A

**Data Migration Plan:** N/A

## 7. API & Backend

**Server Actions:** N/A

**Database Queries:** N/A

## 8. Frontend

**New Components:** N/A

**Page Updates:** N/A

**State Management:** N/A

## 9. Implementation Plan

1. **Phase 1:** Análisis
   - [ ] Escanear carpetas
   - [ ] Extraer nombres frontmatter
   - [ ] Comparar fechas

2. **Phase 2:** Script
   - [ ] Crear 57_Validate_Skills_Duplicates.py
   - [ ] Generar reporte
   - [ ] Test

3. **Phase 3:** Documentación
   - [ ] Actualizar Inventario Total
   - [ ] Crear Skills_TOP_Rankings.md
   - [ ] Actualizar README.md

## 10. SDD Workflow

- [ ] `/sdd:init`
- [ ] `/sdd:spec`
- [ ] `/sdd:design`
- [ ] `/sdd:tasks`
- [ ] `/sdd:apply`

## 11. GGA Code Review

- [ ] `.agent/05_GGA/bin/gga run`
- [ ] Apply fixes
- [ ] Verify all passing

## 12. AI Instructions

**Mandatory Process:**

1. Leer SKILL.md para extraer name del frontmatter
2. Usar regex para parsear `--- name: xxx ---`
3. Comparar timestamps con os.path.getmtime()
4. Output tabla markdown
5. Actualizar checkboxes
6. Run git status

## 13. Impact Analysis

**Second-Order Impact:**

| Tipo                               | Impacto                                     |
|------------------------------------|---------------------------------------------|
| Posibles Regresiones               | Scripts con rutas antiguas                  |
| Performance                        | N/A                                         |
| User Workflow                      | Ninguno (backward compatible)               |

## 14. Strategic Alignment

**Alineación GOALS.md:**

| Métrica                           | Descripción                                          |
|-----------------------------------|------------------------------------------------------|
| North Star                        | Sistema organizado = mejor contexto IA               |
| PersonalOS Priority               | P0                                                   |

---

## Design Audit (Dieter Rams)

- [x] ¿Es innovador y útil? Sí - automatización
- [x] ¿Es estético y comprensible? Tablas claras
- [x] ¿Es discreto y honesto? No oculta información
- [x] ¿Es duradero y cuida cada detalle? Backups

## Version

**Version:** 1.0

**Changelog:**

- 2026-03-20: Creado desde sesión de trabajo
