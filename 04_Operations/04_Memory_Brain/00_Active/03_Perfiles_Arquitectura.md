# 🏗️ ARQUITECTURA DE 10 PERFILES - Think Different AI

> **Fecha**: 2026-03-25
> **Proyecto**: Think Different AI PersonalOS
> **Estado**: v5.0 - MATRIX RECARGADO

- --

## 🔄 ÚLTIMOS CAMBIOS (2026-03-21)

### Skills System v2.0

| Aspecto                                  | Detalle                                                      |
|------------------------------------------|--------------------------------------------------------------|
| Canonical Source                         | `.agent/02_Skills/` (fuente oficial)                         |
| Mirror                                   | `.cursor/02_Skills/` (README only, sincronizado)             |
| Total Active Skills                      | 99 en 9 perfiles                                             |
| Backup Skills                            | ~200 en 10_Backup/                                           |
| Beautified Documents                     | 85+ markdown docs                                            |

### Estructura de Carpetas Sincronizada

```
.agent/02_Skills/     ← CANONICAL SOURCE (99 skills)
.cursor/02_Skills/    ← MIRROR (README solo)
```

### QMD MCP Integration (PENDIENTE)

- Estado: ⏳ Por otro agente
- Tracking: En 04_Inventario.md

### DigitalGarden (PENDIENTE)

- Estado: ⏳ Por otro agente
- Tracking: En 04_Inventario.md

- --

## 📋 TABLA DE CONTENIDOS

1. [Visión General](#visión-general)
2. [01_Agent_Teams_Lite](#01_agent_teams_lite)
3. [02_Project_Manager](#02_project_manager)
4. [03_Product_Manager](#03_product_manager)
5. [04_Product_Design](#04_product_design)
6. [05_Vibe_Coding](#05_vibe_coding)
7. [06_Testing](#06_testing)
8. [07_DevOps](#07_devops)
9. [08_Personal_Os](#08_personal_os)
10. [09_Marketing](#09_marketing)
11. [10_Backup](#10_backup)

- --

## 👁️ VISIÓN GENERAL

```
┌─────────────────────────────────────────────────────────────────┐
│              10 PERFILES DE SKILLS SOTA                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │ 01_Agent_Teams  │    │ 02_Project_Mgr   │                  │
│  │    Lite         │    │                  │                  │
│  │ SDD Workflow    │    │ Rituales, Tasks  │                  │
│  └──────────────────┘    └──────────────────┘                  │
│                                                                 │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │ 03_Product_Mgr   │    │ 04_Product_Design│                  │
│  │                  │    │                  │                  │
│  │ Estrategia       │    │ UX/UI, Brand     │                  │
│  └──────────────────┘    └──────────────────┘                  │
│                                                                 │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │ 05_Vibe_Coding  │    │ 06_Testing       │                  │
│  │                  │    │                  │                  │
│  │ Frontend, React  │    │ QA, TDD, E2E     │                  │
│  └──────────────────┘    └──────────────────┘                  │
│                                                                 │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │ 07_DevOps       │    │ 08_Personal_Os   │                  │
│  │                  │    │                  │                  │
│  │ Deploy, Infra    │    │ System, Tools    │                  │
│  └──────────────────┘    └──────────────────┘                  │
│                                                                 │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │ 09_Marketing    │    │ 10_Backup        │                  │
│  │                  │    │ 🔒 LEGACY        │                  │
│  │ SEO, Ads, CRO   │    │ No tocar         │                  │
│  └──────────────────┘    └──────────────────┘                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

- --

## 01_Agent_Teams_Lite

### Propósito: SDD Workflow + Orchestration

Sistema de desarrollo dirigido por especificaciones con comandos slash.

### Skills (10)

```
01_Agent_Teams_Lite/
├── 00_Shared/                    # Convenciones compartidas (engram, openspec)

├── 01_Sdd_Init/                  # Inicializar contexto SDD

├── 02_Sdd_Explore/              # Investigar antes de comprometerse

├── 03_Sdd_Propose/             # Crear propuesta formal

├── 04_Sdd_Spec/                # Especificaciones detalladas

├── 05_Sdd_Design/              # Diseño arquitectónico

├── 06_Sdd_Tasks/               # Descomponer en tareas

├── 07_Sdd_Apply/               # Implementar por batches

├── 08_Sdd_Verify/              # Verificar contra specs

└── 09_Sdd_Archive/            # Cerrar y archivar

```

### Trigger Phrases

- "estructurado", "con specs", "formal"
- "crear propuesta", "investigar primero"
- `/sdd:init`, `/sdd:explore`, etc.

### Diferencial SOTA

| Aspecto                       | Competitors                      | Our SOTA                                     |
|-------------------------------|----------------------------------|----------------------------------------------|
| Specs                         | Ad-hoc                           | Fases estructuradas                          |
| Memory                        | Sesión única                     | Engram persistence                           |
| Orchestration                 | Inline execution                 | Sub-agents con fresh context                 |

- --

## 02_Project_Manager

### Propósito: Rituales, Tracking, Ejecución Diaria

Gestión de proyectos, coordinación de equipos, y seguimiento de progreso.

### Skills (8)

```
02_Project_Manager/
├── 01_Morning_Standup/               # Rutina diaria de enfoque

├── 02_Backlog_Processing/          # Triage de notas a tareas

├── 03_Weekly_Review/                # Reflexión semanal

├── 04_Sunday_Ritual/                # Mantenimiento sistémico

├── 05_Best_Practices/               # Patrones de excelencia

├── 06_Finishing_A_Development_Branch/ # Cierre de ramas

├── 07_Running_Tests/               # Ejecutar tests

└── 08_Content_Generation/          # Generación de contenido

```

### Trigger Phrases

- "ritual", "standup", "daily"
- "backlog", "triage", "procesar"
- "weekly review", "cierre de sprint"

### Qué Hace

| Skill                              | Función Principal                                     |
|------------------------------------|-------------------------------------------------------|
| Morning_Standup                    | Priorización diaria, focus en metas                   |
| Backlog_Processing                 | Convertir notas en tareas actionables                 |
| Weekly_Review                      | Métricas, reflección, ajustes                         |
| Sunday_Ritual                      | Mantenimiento, limpieza, alineación                   |
| Finishing_Branch                   | PR flow, merge, cleanup                               |
| Running_Tests                      | Validación pre-commit                                 |
| Content_Generation                 | drafts, docs, contenido                               |

- --

## 03_Product_Manager

### Propósito: Estrategia, Visión, Discovery, Roadmap

Gestión de producto: qué construir y por qué.

### Skills (8)

```
03_Product_Manager/
├── 01_Brainstorming/                 # Exploración de ideas

├── 02_Writing_Plans/                # Planes estructurados

├── 03_Executing_Plans/               # Ejecución sistemática

├── 04_Jira_Epic/                     # Crear epics en Jira

├── 05_Jira_Task/                     # Gestión de tareas

├── 06_Branch_Pr/                     # Workflow de PRs

├── 07_Writing_Strategy_Memos/       # Memos estratégicos (FocusFlow)

└── 08_Planificacion_Tareas_Ai/     # Planificación inteligente

```

### Trigger Phrases

- "roadmap", "estrategia", "producto"
- "priorizar", "features", "epics"
- "brainstorming", "discovery"

### Qué Hace

| Skill                              | Función Principal                                    |
|------------------------------------|------------------------------------------------------|
| Brainstorming                      | Exploración creativa de soluciones                   |
| Writing_Plans                      | Planes de acción estructurados                       |
| Jira_Epic                          | Definición de epics                                  |
| Jira_Task                          | Creación de tareas                                   |
| Strategy_Memos                     | Decisiones estratégicas documentadas                 |
| Planning_Tareas_Ai                 | Priorización con AI                                  |

### Diferencial SOTA

- **FocusFlow Framework**: Framework de memoización estratégica
- **Jira Integration**: Gestión de producto con tickets
- **Brainstorm → Plan → Execute**: Pipeline completo

- --

## 04_Product_Design

### Propósito: UX/UI, Brand, Content, CRO, Psychology

Diseño de producto holístico: desde investigación hasta optimización de conversiones.

### Skills (11)

```
04_Product_Design/
├── 01_Taste_Skill/                    # Diseño premium principal

├── 02_Soft_Skill/                     # Look expensive, Awwwards tier

├── 03_Minimalist_Skill/              # Notion/Linear style

├── 04_Redesign_Skill/                 # Mejorar existentes

├── 05_Output_Skill/                   # Full output enforcement

├── 06_Dieter_Rams_Design/             # Principios de diseño funcional

├── 07_Brand_Identity/                # Sistema de marca

├── 08_Brand_Voice_Generator/          # Voice & tone

├── 09_Canvas_Diagram_Studio/          # Excalidraw diagrams

├── 10_Visual_Language/                # Lenguaje visual

└── 11_Pencil_Design_Studio/          # Identidades visuales

```

### Trigger Phrases

- "diseño", "UI", "UX", "premium"
- "marca", "branding", "identidad"
- "conversión", "CRO", "optimizar"
- "que se sienta", "vibe", "look"

### Qué Hace

| Skill                            | Función Principal                                            |
|----------------------------------|--------------------------------------------------------------|
| Taste_Skill                      | Diseño principal con variance/motion/density                 |
| Soft_Skill                       | Awwwards tier ($150k+ agency)                                |
| Minimalist_Skill                 | Editorial minimalism                                         |
| Redesign_Skill                   | Upgrade de proyectos existentes                              |
| Output_Skill                     | Previene código truncado                                     |
| Dieter_Rams                      | "Menos pero mejor"                                           |
| Brand_Identity                   | Design tokens, voice, consistency                            |
| Brand_Voice                      | Tone of voice generation                                     |
| Canvas_Diagram                   | Diagramas con Excalidraw                                     |

### Config Dial de Taste_Skill

```markdown
DESIGN_VARIANCE (1-10): Experimental layout
MOTION_INTENSITY (1-10): Animaciones
VISUAL_DENSITY (1-10): Densidad de contenido
```

- --

## 05_Vibe_Coding

### Propósito: Frontend, React, Angular, Tailwind, TypeScript

Desarrollo frontend con frameworks modernos y output premium.

### Skills (18)

```
05_Vibe_Coding/
├── 01_React_19/                        # React 19 + Server Components

├── 02_Nextjs_15/                      # Next.js App Router

├── 03_Tailwind_4/                    # Tailwind CSS v4

├── 04_Angular/                        # Angular (architecture/core/forms/performance)

├── 05_TypeScript/                     # TypeScript strict patterns

├── 06_Zustand_5/                      # State management

├── 07_Zod_4/                          # Schema validation

├── 08_Ai_Sdk_5/                       # AI SDK integration

├── 09_Skill_Creator/                  # Crear skills

├── 10_Antigravity_Skill_Creator/       # Skill creator avanzado

├── 11_Mcp_Client/                     # MCP server integration

├── 12_Invoice_Intelligence/            # OCR de facturas

├── 13_Health_Data_Analyst/             # Análisis de salud

├── 14_Django_Drf/                     # Django REST API

├── 15_Server_Api/                     # API design patterns

├── 16_Pytest/                         # Python testing

├── 17_Playwright/                     # E2E testing

└── 18_Firecrawl/                     # Web scraping

```

### Trigger Phrases

- "frontend", "React", "Angular", "Vue"
- "tailwind", "estilos", "componente"
- "TypeScript", "types", "schema"
- "state management", "zustand"

### Stack Covered

| Framework                   | Patterns                                                 |
|-----------------------------|----------------------------------------------------------|
| React 19                    | Server Components, no manual memoization                 |
| Next.js 15                  | App Router, Server Actions, streaming                    |
| Angular                     | Signals, standalone components, zoneless                 |
| Tailwind 4                  | cn() utility, semantic classes                           |
| TypeScript                  | Strict mode, generics, inference                         |
| Zustand 5                   | Slices, middleware, persist                              |
| Zod 4                       | Schema validation, inference                             |

### Output Enforcement

`05_Output_Skill` asegura:
- Código completo (no truncation)
- Todos los archivos necesarios
- Imports correctos
- Deployment-ready

- --

## 06_Testing

### Propósito: QA, TDD, E2E, Coverage, Edge Cases

Framework completo de testing y calidad.

### Skills (14)

```
06_Testing/
├── 01_Test_Driven_Development/        # TDD ciclo Red-Green-Refactor

├── 02_Systematic_Debugging/            # Metodología 4 fases

├── 03_Verification_Before_Completion/   # QA antes de cerrar

├── 04_Verify_And_Commit/              # Verificar + commit

├── 05_Test_Resource_Management/         # Gestión de recursos (max 4 workers)

├── 06_Testing_Coverage/               # Coverage standards

├── 07_Go_Testing/                    # Go testing patterns

├── 08_Tui_Quality/                    # Bubbletea/Lipgloss quality

├── 09_E2E_Testing/                   # Playwright E2E

├── 10_Integration_Testing/            # API, database testing

├── 11_Test_Coverage/                  # Coverage analysis

├── 12_Edge_Case/                     # Boundary testing

├── 13_Evaluation/                     # Agent evaluation

└── 14_Skill_Testing_Automation/       # Meta-testing

```

### Trigger Phrases

- "test", "testing", "TDD"
- "coverage", "edge cases"
- "e2e", "playwright"
- "pytest", "unit test"

### Testing Pyramid

```
        ┌─────────┐
        │   E2E   │     ← 09_E2E_Testing
        ├─────────┤
        │Integration│   ← 10_Integration_Testing
        ├─────────┤
        │  Unit    │     ← 01_TDD, 07_Go_Testing, 16_Pytest
        └─────────┘
```

### TDD Cycle

```
1. RED: Escribir test que falla
2. GREEN: Implementar mínimo para pasar
3. REFACTOR: Mejorar sin romper tests
```

- --

## 07_DevOps

### Propósito: Deployment, Observability, Containers, Infrastructure

Infraestructura y deployment automatizado.

### Skills (12)

```
07_DevOps/
├── 01_Vercel_Deploy/                  # Deploy en Vercel

├── 02_Supabase_Integration/           # Supabase backend

├── 03_MCP_Integration/                # MCP server deployment

├── 04_Observability/                 # Prometheus, Grafana, OpenTelemetry

├── 05_Seo_Audit/                     # SEO analysis

├── 06_Seo_Optimization/                # SEO optimization

├── 07_Data_Visualization/             # Dashboards, gráficos

├── 08_Vercel_React_Best_Practices/  # React performance

├── 09_Using_Git_Worktrees/           # Git worktree management

├── 10_E2b_Sandbox/                  # Cloud sandbox deployment

├── 11_Error_Handling_Patterns/      # Error handling

└── 12_RTM/                          # Requirements Traceability

```

### Trigger Phrases

- "deploy", "deployment", "CI/CD"
- "observability", "monitoring", "logs"
- "docker", "container", "infra"
- "SEO", "analytics"

### Observability Stack

| Pillar                   | Tools                                       |
|--------------------------|---------------------------------------------|
| Metrics                  | Prometheus, Grafana                         |
| Logs                     | Structured JSON (structlog)                 |
| Traces                   | OpenTelemetry, Jaeger                       |
| Alerts                   | Prometheus alerts                           |

- --

## 08_Personal_Os

### Propósito: System, Tools, Scripts, Multi-agent

Sistema operativo personal y automatización.

### Skills (9)

```
08_Personal_Os/
├── 01_Fork_Terminal/                       # Multi-terminal

├── 02_Parallel_Orchestration/             # Agentes paralelos

├── 03_Premium_Git_Manager/                 # Git workflows

├── 04_Subagent_Driven_Development/          # SDD con sub-agents

├── 05_Dispatching_Parallel_Agents/         # Distribución agentes

├── 06_Browser_Use/                        # Automatización navegador

├── 07_Csv_Management/                     # Gestión CSV

├── 08_Managing_Image_Assets/              # Assets de imagen

└── 09_Frictionless_Capture/                # Captura rápida ideas

```

### Trigger Phrases

- "terminal", "script", "automatización"
- "multi-agent", "paralelo"
- "capturar", "nota rápida"
- "git", "workflow"

### Core Philosophy

> "Each unit of engineering work should make subsequent units easier—not harder."

Compound engineering: 80% planning/review, 20% execution.

- --

## 09_Marketing

### Propósito: SEO, Ads, Social, Analytics, Content, CRO

Marketing digital completo con automatización.

### Skills (9)

```
09_Marketing/
├── 01_Marketing_Strategy/                # Estrategia de marketing

│   ├── content-strategy/
│   ├── copywriting/
│   ├── email-sequence/
│   ├── page-cro/
│   ├── pricing-strategy/
│   └── ...
├── 02_Marketing_Tech/                  # Marketing tech stack

│   ├── seo-audit/
│   ├── analytics-tracking/
│   ├── paid-ads/
│   ├── social-content/
│   └── ...
├── 03_Compound_Engine/                 # Compound engineering

├── 04_Premium_Image_Studio/           # Generación de imágenes IA

├── 05_Video_Visuals_Producer/         # Videos con Remotion

├── 06_Content_Creation/               # Generación de contenido

├── 07_Pptx_Generator/                # Presentaciones PPTX

├── 08_Remotion_Video_Creator/        # Videos React

└── 09_Remotion_Best_Practices/       # Remotion optimization

```

### Trigger Phrases

- "marketing", "SEO", "ads"
- "contenido", "copy", "CTA"
- "presentación", "slides"
- "analytics", "CRO"

### Marketing Tech Stack

| Category                  | Tools                                                          |
|---------------------------|----------------------------------------------------------------|
| SEO                       | seo-audit, seo-optimization, programmatic-seo                  |
| Ads                       | paid-ads, competitor-alternatives                              |
| Analytics                 | analytics-tracking, ab-test-setup                              |
| CRO                       | page-cro, signup-flow-cro, popup-cro                           |
| Content                   | content-creation, copywriting, email-sequence                  |
| Visual                    | premium-image-studio, pptx-generator, remotion                 |

- --

## 10_Backup

### Propósito: Legacy Storage (🔒 NO TOCAR)

Respaldo histórico de todas las versiones anteriores.

```
10_Backup/
├── 01_Gentleman_System_Legacy/      # Original Gentleman Programming

├── 02_Every_Canonical/              # Canonical de 07_Every/

├── 03_High_Value_Remaining/         # Duplicados de 02_High_Value/

└── 04_Utilities_Remaining/          # Duplicados de 03_Utilities/

```

### Por Qué No Tocar

- **Historical Reference**: Ver cómo evolucionó el sistema
- **Emergency Rollback**: Si algo sale mal, tenemos respaldo
- **Audit Trail**: Git history de todas las migraciones

- --

## 🔥 NUEVO: COMPOUND ENGINEERING (131 componentes)

### Propósito: Code Review, Research, Workflow Intelligence

El ecosistema CE complementa a Gentleman con inteligencia y validación.

### Componentes

```
00_Compound_Engineering/
├── 01_Agents_Review/        (23 agents) - Code review especializado
├── 02_Agents_DocReview/     (6 agents) - Review de documentos
├── 03_Agents_Design/        (3 agents) - Design review
├── 04_Agents_Research/      (6 agents) - Investigación
├── 05_Agents_Workflow/      (4 agents) - Workflow automation
├── 06_Agents_Docs/          (1 agent) - Documentación
├── 07_Skills/               (41 skills) - Workflow skills
└── 08_MCP/                  (Context7) - 100+ frameworks docs
```

### CE Commands

| Command          | Triggers                 | Propósito            |
|------------------|--------------------------|----------------------|
| `/ce:ideate`     | "idear", "mejorar"       | Descubrir mejoras    |
| `/ce:brainstorm` | "explorar", "requisitos" | Explorar enfoques    |
| `/ce:plan`       | "planear", "plan"        | Crear plan           |
| `/ce:work`       | "ejecutar"               | Ejecutar plan        |
| `/ce:review`     | "review", "revisar"      | Code review          |
| `/ce:compound`   | "documentar"             | Documentar learnings |

### Agents CE Destacados

| Agent                        | Triggers       | Propósito                  |
|------------------------------|----------------|----------------------------|
| `security-sentinel`          | "seguridad"    | Auditorías de seguridad    |
| `performance-oracle`         | "performance"  | Análisis de performance    |
| `architecture-strategist`    | "arquitectura" | Decisiones arquitectónicas |
| `kieran-typescript-reviewer` | "ts review"    | TypeScript review          |

---

## 📊 RESUMEN DE PERFILES (Matrix Recargado)

| #   | Perfil                   | Skills   | Focus                   |
|-----|--------------------------|----------|-------------------------|
| 00  | **Compound_Engineering** | 131      | 🔥 Code Review, Research |
| 01  | Agent_Teams_Lite         | 9        | SDD Workflow            |
| 02  | Project_Manager          | 9        | Rituales, tracking      |
| 03  | Product_Manager          | 7        | Estrategia, producto    |
| 04  | Product_Design           | 11       | UX/UI, Brand, CRO       |
| 05  | Vibe_Coding              | 21       | Frontend, frameworks    |
| 06  | Testing                  | 13       | QA, TDD, E2E            |
| 07  | DevOps                   | 13       | Deploy, infra           |
| 08  | Personal_Os              | 10       | System, tools           |
| 09  | Marketing                | 32       | SEO, ads, content       |
| 11  | Doc_Processing           | 3        | Documentos              |
| 13  | System_Master            | 1        | Guides (nuevo)          |
| 10  | Backup                   | ~204     | Legacy (no tocar)       |

* *TOTAL: ~440 componentes** (139 Gentleman + 131 CE + 100+ Backup)*

## 🎯 DECISION MATRIX: GENTLEMAN vs CE

```
¿Qué querés hacer?
│
├─ Escribir código nuevo     → GENTLEMAN
├─ Framework específico      → GENTLEMAN
├─ Testing                   → GENTLEMAN
├─ DevOps                    → GENTLEMAN
├─ Diseño UI/UX              → GENTLEMAN
├─ Marketing                 → GENTLEMAN
│
├─ Code review               → CE → /ce:review
├─ Auditoría seguridad       → CE → security-sentinel
├─ Análisis performance      → CE → performance-oracle
├─ Decisiones arquitectura   → CE → architecture-strategist
├─ Idear mejoras             → CE → /ce:ideate
├─ Explorar requisitos       → CE → /ce:brainstorm
├─ Planificar                → CE → /ce:plan
└─ Documentar aprendizajes   → CE → /ce:compound
```

- --

## 🎯 COMO ELEGIR EL PERFIL CORRECTO

```
¿Necesitas...?
│
├─ Estructura formal con specs?     → 01_Agent_Teams_Lite
├─ Rituales diarios o tracking?  → 02_Project_Manager
├─ Estrategia o roadmap?            → 03_Product_Manager
├─ Diseño UI/UX o marca?           → 04_Product_Design
├─ Código frontend o frameworks?   → 05_Vibe_Coding
├─ Tests o quality assurance?    → 06_Testing
├─ Deploy o infraestructura?      → 07_DevOps
├─ Automatización o system tools?   → 08_Personal_Os
└─ Marketing o contenido?          → 09_Marketing
```

- --

* Documento creado: 2026-03-21*
* Arquitectura de perfiles SOTA*
