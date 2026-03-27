- --
Title: Task Template SOTA
Category: template
Priority: P0
Status: active
Created_Date: 2026-03-20
Estimated_Effort: 1-8 hours
Dependencies: [task refs]
Tags:
  - sota
  - complete
  - production
Resource_Refs:
  - 01_Brain/04_Rules/
  - 04_Agent_Teams_Lite/
  - 06_Taste_Skills/
  - .agent/05_GGA/
- --

# Task Template PersonalOS (SOTA)

## Context

[Descripción breve del problema/tarea]

## Next Actions

- [ ] Acción 1
- [ ] Acción 2

## Progress Log

- YYYY-MM-DD: [evento]

- --

## 1. Task Overview

* *Title:** [Título de la tarea]

* *Goal Statement:** [¿Qué queremos lograr y por qué?]

## 2. Project Analysis

* *Tech Stack:**

| Componente                    | Valor                                           |
|-------------------------------|-------------------------------------------------|
| Framework                     | [Next.js 15]                                    |
| Lenguaje                      | [TypeScript]                                    |
| Base_Datos                    | [PostgreSQL]                                    |
| UI                            | [Tailwind CSS]                                  |
| Autenticación                 | [NextAuth/JWT]                                  |
| Arquitectura                  | [App Router, Server Components]                 |

* *Current State:** [Estado actual del código]

## 3. Problem & Success

* *Problem Statement:** [Definición del problema específico]

* *Success Criteria:**

- [ ] Criterio 1 medible
- [ ] Criterio 2 medible

## 4. Development Mode

| Aspecto                          | Valor                                 |
|----------------------------------|---------------------------------------|
| Project Stage                    | [New / Feature / Fix]                 |
| Breaking Changes                 | [Acceptable / Avoid]                  |
| Data Handling                    | [Preserve / Migrate]                  |
| User Base                        | [Quién será afectado]                 |
| Priority                         | [Speed vs Stability]                  |

## 5. Requirements

* *Functional Requirements:**

- User can [acción]
- System automatically [comportamiento]
- When [condition] then [response]

* *Non-Functional Requirements:**

| Aspecto                     | Requisito                               |
|-----------------------------|-----------------------------------------|
| Performance                 | [<200ms]                                |
| Security                    | [Validaciones]                          |
| Usability                   | [UX/Accessibility]                      |
| Responsive                  | [Mobile/Tablet/Desktop]                 |

## 6. Data & Database

* *Database Schema Changes:**

```sql
[SQL schema si aplica]
```

* *Data Model Updates:**

```typescript
[Types/Interfaces]
```

* *Data Migration Plan:**

1. Backup
2. Apply changes
3. Transform data
4. Validate

## 7. API & Backend

* *Server Actions:**

| Operación                  | Descripción                  |
|----------------------------|------------------------------|
| Create                     | [qué]                        |
| Update                     | [qué]                        |
| Delete                     | [qué]                        |

* *Database Queries:**

| Query                   | Descripción                   |
|-------------------------|-------------------------------|
| Fetch                   | [datos]                       |
| Filter                  | [condiciones]                 |

## 8. Frontend

* *New Components:**

| Componente                  | Propósito                  |
|-----------------------------|----------------------------|
| [Nombre]                    | [qué]                      |

* *Page Updates:**

| Página                   | Cambios                   |
|--------------------------|---------------------------|
| [Página]                 | [qué]                     |

* *State Management:** [Zustand/Context/Server State]

## 9. Implementation Plan

1. **Phase 1:** [Nombre]
   - [ ] Step 1
   - [ ] Step 2

2. **Phase 2:** [Nombre]
   - [ ] Step 1

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

* *Mandatory Process:**

1. Analizar código base antes de escribir
2. No usar `any` en TypeScript
3. Seguir Taste-Skills si es UI
4. Actualizar checkboxes
5. Run lint + typecheck antes de commit

## 13. Impact Analysis

* *Second-Order Impact:**

| Tipo                                 | Impacto                    |
|--------------------------------------|----------------------------|
| Posibles Regresiones                 | [lista]                    |
| Performance                          | [concerns]                 |
| User Workflow                        | [impacts]                  |

## 14. Strategic Alignment

* *Alineación GOALS.md:**

| Métrica                             | Descripción                               |
|-------------------------------------|-------------------------------------------|
| North Star                          | [Cómo acerca a la visión]                 |
| PersonalOS Priority                 | [P0/P1/P2/P3]                             |

- --

## Design Audit (Dieter Rams)

- [ ] ¿Es innovador y útil?
- [ ] ¿Es estético y comprensible?
- [ ] ¿Es discreto y honesto?
- [ ] ¿Es duradero y cuida cada detalle?

## Version

* *Version:** 1.0

* *Changelog:**

- YYYY-MM-DD: Creado
