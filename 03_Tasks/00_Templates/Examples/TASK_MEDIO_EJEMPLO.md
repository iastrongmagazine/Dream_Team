---
Title: Task Template Medio - Ejemplo
Category: feature
Priority: P1
Status: draft
Created_Date: 2026-03-20
Estimated_Effort: 2 hours
Tags:
  - feature
  - backend
  - api
Resource_Refs:
  - 01_Core/04_Rules/
  - 01_Core/05_Templates/
---

# Task: Agregar Backup a Sync Skills

## Context

Agregar script de backup automático antes de sincronizar skills .agent → .cursor.

## Next Actions

- [ ] Crear función backup con timestamp
- [ ] Integrar en 55_Sync_Skills.py
- [ ] Test con dry-run
- [ ] Commit

## Progress Log

- 2026-03-20: Tarea creada

---

## 1. Task Overview

**Title:** Backup Automático en Sync Skills

**Goal Statement:** Agregar backup automático antes de sincronizar para tener rollback si falla.

## 2. Project Analysis

**Tech Stack:**

| Componente                | Valor                     |
|---------------------------|---------------------------|
| Framework                 | Python CLI                |
| Lenguaje                  | Python 3.12               |
| Base_Datos                | N/A                       |
| UI                        | Terminal                  |

**Current State:**
- Sync Skills existe y funciona
- No hay backup automático
- Riesgo si falla sincronización

## 3. Problem & Success

**Problem Statement:**
No hay forma de rollback si la sincronización falla o borra archivos importantes.

**Success Criteria:**

- [ ] Función backup creada
- [ ] Timestamp en nombre carpeta
- [ ] Integrada en sync principal
- [ ] Test exitoso

## 4. Development Mode

| Aspecto                        | Valor                           |
|--------------------------------|---------------------------------|
| Project Stage                  | Feature                         |
| Breaking Changes               | None                            |
| Data Handling                  | Preserve                        |
| User Base                      | AI Agents                       |
| Priority                       | Stability > Speed               |

## 5. Requirements

**Functional Requirements:**

- Backup se ejecuta antes de sync
- Carpeta con timestamp: `backup_YYYYMMDD_HHMMSS`
- Incluye todos los archivos sincronizados

**Non-Functional Requirements:**

| Aspecto                   | Requisito                                    |
|---------------------------|----------------------------------------------|
| Performance               | <10 segundos                                 |
| Security                  | Solo copia, no modifica origen               |

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

1. **Phase 1:** Función Backup
   - [ ] Crear función backup()
   - [ ] Test con carpeta dummy

2. **Phase 2:** Integración
   - [ ] Agregar llamada antes de sync
   - [ ] Test completo

## 10. AI Instructions

**Mandatory Process:**

1. Leer script existente para patterns
2. No usar `any` - usar Path type hints
3. Agregar tests
4. Run lint

## 11. Impact Analysis

| Tipo                               | Impacto                              |
|------------------------------------|--------------------------------------|
| Posibles Regresiones               | Ninguna                              |
| Performance                        | +5 segundos por backup               |

## 12. Strategic Alignment

| Métrica                           | Descripción                |
|-----------------------------------|----------------------------|
| North Star                        | Safety first               |
| PersonalOS Priority               | P1                         |

---

## Design Audit (Dieter Rams)

- [x] ¿Es innovador y útil? Sí - safety
- [x] ¿Es estético y comprensible? Simple
- [x] ¿Es discreto y honesto? Protege datos
- [x] ¿Es duradero? Siempre útil

## Version

**Version:** 1.0

**Changelog:**

- 2026-03-20: Creado
