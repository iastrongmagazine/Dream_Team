# 🗺️ MAPA COMPLETO DEL SISTEMA THINK DIFFERENT AI

> **Fecha:** 2026-03-26  
> **Versión:** 1.0  
> **Propósito:** Mapeo integral de agentes, skills, scripts, hooks, workflows y MCPs

---

## 📊 RESUMEN EJECUTIVO

| Componente              | Cantidad   | Ubicación                       |
|-------------------------|------------|---------------------------------|
| **Agentes Principales** | 12         | `.agent/01_Agents/`             |
| **Especialistas**       | 24         | `.agent/01_Agents/Specialists/` |
| **Perfiles de Negocio** | 5          | `.agent/01_Agents/Perfiles/`    |
| **Skills**              | 128+       | `.agent/02_Skills/`             |
| **Scripts**             | 86+        | `04_Engine/08_Scripts_Os/`      |
| **Workflows**           | 24         | `.agent/03_Workflows/`          |
| **Hooks**               | 12         | `.agent/04_Extensions/hooks/`   |

---

## 🤖 1. AGENTES PRINCIPALES (Pipeline TDD)

**Ubicación:** `.agent/01_Agents/`

| #   | Archivo                        | Propósito                       |
|-----|--------------------------------|---------------------------------|
| 00  | `00_Orchestrator.md`           | Orquestador maestro del sistema |
| 01  | `01_Scope_Rule_Architect.md`   | Define alcance y scope rule     |
| 02  | `02_TDD_Test_First.md`         | Escribe tests primero (Rojo)    |
| 03  | `03_React_Test_Implementer.md` | Implementa features (Verde)     |
| 04  | `04_React_Mentor.md`           | Refactor y mentor (Azul)        |
| 05  | `05_Security_Auditor.md`       | Auditoría de seguridad          |
| 06  | `06_Git_Workflow_Manager.md`   | Gestión de git y commits        |
| 07  | `07_Accessibility_Auditor.md`  | Accesibilidad WCAG              |
| 08  | `08_PRD_Dashboard_Template.md` | Templates de PRD                |
| 09  | `09_Design_SOP_Document.md`    | Documentación de diseño         |
| 10  | `10_Workflow_Orchestrator.md`  | Orquestador de workflows        |
| 11  | `11_AIPM_Judge.md`             | Evaluación de tareas AI         |
| 12  | `12_LFG_Autonomous_Engine.md`  | Motor autónomo para LFG         |

> **Nota:** Estos 12 agentes forman un pipeline TDD. No tocarlos, solo extender.

---

## 🎭 2. ESPECIALISTAS (24 agentes)

**Ubicación:** `.agent/01_Agents/Specialists/`

### Por Categoría

| Categoría            | Especialistas                                                                                     |
|----------------------|---------------------------------------------------------------------------------------------------|
| **Reviewers (Code)** | Kieran-TypeScript, Kieran-Rails, Kieran-Python, Dhh-Rails, Code-Simplicity, Agent-Native          |
| **Design**           | Design-Iterator, Design-Implementation-Reviewer, Figma-Design-Sync                                |
| **Data**             | Data-Migration-Expert, Data-Integrity-Guardian                                                    |
| **Research**         | Repo-Research-Analyst, Best-Practices-Researcher, Framework-Docs-Researcher, Learnings-Researcher |
| **Infrastructure**   | Performance-Oracle, Security-Sentinel, Architecture-Strategist, Deployment-Verification-Agent     |
| **Analysis**         | Pattern-Recognition-Specialist, Git-History-Analyzer                                              |
| **Docs**             | Ankane-Readme-Writer                                                                              |
| **Frontend**         | Julik-Frontend-Races-Reviewer                                                                     |

---

## 👤 3. PERFILES DE NEGOCIO (5)

**Ubicación:** `.agent/01_Agents/Perfiles/`

| #   | Perfil                    | Propósito                               | Keywords                       |
|-----|---------------------------|-----------------------------------------|--------------------------------|
| 01  | `01_Product_Builder.md`   | Entrega features completas (PRD→deploy) | feature, build, crear app      |
| 02  | `02_Data_Engineer.md`     | Pipelines de datos, analytics, ETL      | data, pipeline, analytics      |
| 03  | `03_Marketing_Tech.md`    | Campañas, SEO, contenido, visual        | marketing, seo, ads, content   |
| 04  | `04_Design_Ops.md`        | Design systems, UI/UX sistemático       | design, ui, ux, component      |
| 05  | `05_Platform_Engineer.md` | Infraestructura, MCPs, DevOps           | infrastructure, devops, deploy |

> **Anthropic Integration:** Perfil 01 ya tiene referencias a Anthropic Harness. Perfiles 02-05 necesitan actualización.

---

## 🛠️ 4. SKILLS (128+)

**Ubicación:** `.agent/02_Skills/`

### Por Categoría

| Categoría                   | Subcategorías                       | Skills   | Propósito                      |
|-----------------------------|-------------------------------------|----------|--------------------------------|
| **01_Agent_Teams_Lite**     | SDD Workflow                        | 9        | Spec-Driven Development        |
| **02_Project_Manager**      | PM                                  | 9        | Gestión de proyectos           |
| **03_Product_Manager**      | PRD, Planning                       | 7        | Producto                       |
| **04_Product_Design**       | Taste, Minimalist, Brand            | 11       | Diseño UI/UX                   |
| **05_Vibe_Coding**          | React, Next, Angular, Tailwind, etc | 21       | Frameworks de código           |
| **06_Testing**              | TDD, E2E, Coverage                  | 13       | Testing y QA                   |
| **07_DevOps**               | Deploy, Supabase                    | 12       | DevOps y部署                     |
| **08_Personal_Os**          | CSV, Memory, Docs                   | 10       | OS Personal                    |
| **09_Marketing**            | SEO, Ads, Content, Video            | 32       | Marketing digital              |
| **10_Backup**               | Legacy                              | 177      | Backups                        |
| **11_Doc_Processing**       | OCR, PDF                            | 3        | Procesamiento de docs          |
| **12_N8N**                  | Automation                          | 7        | n8n automation                 |
| **13_System_Master**        | System                              | 1        | Configuración sistema          |
| **14_Anthropic_Harness**    | Evaluator, Context, Sprint          | 3        | **NUEVO** - Patterns Anthropic |
| **00_Compound_Engineering** | Compound                            | 6        | Ingeniería compuesta           |

### Skills Principales (Top 20)

| Skill                    | Ubicación               | Uso                |
|--------------------------|-------------------------|--------------------|
| `Taste_Skill`            | 04_Product_Design       | Diseño premium     |
| `shadcn`                 | 05_Vibe_Coding          | Componentes UI     |
| `React_19`               | 05_Vibe_Coding          | Frontend moderno   |
| `Nextjs_15`              | 05_Vibe_Coding          | Fullstack          |
| `TypeScript`             | 05_Vibe_Coding          | Tipado estricto    |
| `Brainstorming`          | 01_Agent_Teams_Lite     | Exploración ideas  |
| `PRD`                    | 03_Product_Manager      | Requirements       |
| `ce:plan`                | 00_Compound_Engineering | Planning técnico   |
| `ce:work`                | 00_Compound_Engineering | Ejecución          |
| `ce:review`              | 00_Compound_Engineering | Code review        |
| `E2E_Testing`            | 06_Testing              | Playwright         |
| `Observability`          | 07_DevOps               | Métricas           |
| `SEO_Audit`              | 09_Marketing            | SEO                |
| `Content_Creation`       | 09_Marketing            | Copy               |
| `Premium_Image_Studio`   | 09_Marketing            | Imágenes IA        |
| `Video_Visuals_Producer` | 09_Marketing            | Videos             |
| `MCP_Client`             | 05_Vibe_Coding          | Integraciones MCP  |
| `Analytics_Workflow`     | 05_Vibe_Coding          | Análisis datos     |
| `Skill_Creator`          | 13_System_Master        | Crear skills       |
| `Subagent_Driven_Dev`    | 00_Compound_Engineering | SDD con subagentes |

---

## 📜 5. SCRIPTS (86+)

**Ubicación:** `04_Engine/08_Scripts_Os/`

### Hubs (Arquitectura Modular)

| #   | Script                  | Propósito                  |
|-----|-------------------------|----------------------------|
| 01  | `01_Auditor_Hub.py`     | Central de auditorías      |
| 02  | `02_Git_Hub.py`         | Comandos git               |
| 03  | `03_AIPM_Hub.py`        | AI Product Management      |
| 04  | `04_Ritual_Hub.py`      | Rituales (standup, cierre) |
| 05  | `05_Validator_Hub.py`   | Validaciones               |
| 06  | `06_Tool_Hub.py`        | Herramientas               |
| 07  | `07_Integration_Hub.py` | Integraciones              |
| 08  | `08_Workflow_Hub.py`    | Workflows                  |
| 09  | `09_Data_Hub.py`        | Datos y analytics          |
| 10  | `10_General_Hub.py`     | Comandos generales         |

### Subdirectorios

| Directorio              | Contenido                       |
|-------------------------|---------------------------------|
| `11_Anthropic_Harness/` | **NUEVO** - 5 scripts Anthropic |
| `AIPM_Fixed/`           | Scripts AIPM                    |
| `Analytics_Output/`     | Outputs de analytics            |
| `Legacy_Backup/`        | Backups                         |

### Scripts Antropomórficos (Hubs)

```
04_Engine/08_Scripts_Os/
├── 01_Auditor_Hub.py      🤖 Iron Man - Auditor
├── 02_Git_Hub.py         🔧 Thor - Git
├── 03_AIPM_Hub.py        📊 JARVIS - AI PM
├── 04_Ritual_Hub.py      ⏰ Hulk - Rituales
├── 05_Validator_Hub.py   ✅ Rocket - Validaciones
├── 06_Tool_Hub.py        🔨 Widow - Herramientas
├── 07_Integration_Hub.py 🔗 Vision - Integraciones
├── 08_Workflow_Hub.py    🔀 Strange - Workflows
├── 09_Data_Hub.py        📈 Mantis - Datos
└── 10_General_Hub.py     🦸‍♂️ General - Varios
```

---

## 🔄 6. WORKFLOWS (24)

**Ubicación:** `.agent/03_Workflows/`

### Por Tipo

| #   | Workflow                       | Tipo       | Propósito                |
|-----|--------------------------------|------------|--------------------------|
| 00  | `00_Backlog_Processing.md`     | PM         | Procesamiento de backlog |
| 00  | `00_Content_Generation.md`     | Content    | Generación de contenido  |
| 00  | `00_Morning_Standup.md`        | Ritual     | Standup diario           |
| 00  | `00_Weekly_Review.md`          | Ritual     | Revisión semanal         |
| 01  | `01_Iron_Man_Gen.md`           | Auditor    | Generación de auditoría  |
| 01  | `01_Spider_Brainstorm.md`      | Brainstorm | Lluvia de ideas          |
| 02  | `02_Professor_X_Plan.md`       | Planning   | Planificación            |
| 03  | `03_Vision_Review.md`          | Vision     | Revisión de visión       |
| 04  | `04_Thor_Work.md`              | Work       | Trabajo                  |
| 05  | `05_Hulk_Compound.md`          | Compound   | Ingeniería compuesta     |
| 06  | `06_AntMan_Lfg_Lite.md`        | LFG        | LFG Lite                 |
| 07  | `07_Doc_Strange_Lfg.md`        | LFG        | LFG Docs                 |
| 08  | `08_Validar_Reglas.md`         | Rules      | Validación               |
| 09  | `09_Frontend_Premium.md`       | Frontend   | Frontend premium         |
| 09  | `09_Redaccion_de_Docs.md`      | Docs       | Redacción docs           |
| 10  | `10_AI_Task_Template.md`       | Template   | Templates AI             |
| 11  | `11_Ritual_Cierre_Protocol.md` | Ritual     | Protocolo de cierre      |
| 12  | `12_Context_Recovery.md`       | Context    | Recuperación de contexto |
| 13  | `13_System_Health_Audit.md`    | Audit      | Auditoría de salud       |
| 14  | `14_Captura_Rapida.md`         | Capture    | Captura rápida           |
| 15  | `15_Deep_Work_Session.md`      | Work       | Sesión deep work         |
| 16  | `16_Ship_It.md`                | Deploy     | Shipping                 |
| 17  | `17_Anthropic_Harness.md`      | **NUEVO**  | Three-Agent Pattern      |

---

## 🪝 7. HOOKS (12)

**Ubicación:** `.agent/04_Extensions/hooks/`

### Por Tipo

| #                 | Hook                      | Trigger          | Función                       |
|-------------------|---------------------------|------------------|-------------------------------|
| **01_Pre_Tool/**  |                           |                  |                               |
|-------------------| `pre_tool_use.py`         | PreToolUse       | Batería < 15%, bloquea rm -rf |
|-------------------| `csv-single-validator.py` | PreToolUse       | Valida estructura CSV         |
| **02_Post_Tool/** |                           |                  |                               |
|-------------------| `post_tool_use.py`        | PostToolUse      | Backup, voz cada 2 archivos   |
| **03_Lifecycle/** |                           |                  |                               |
|-------------------| `stop.py`                 | Stop             | "Sesión finalizada"           |
|-------------------| `subagent_stop.py`        | SubagentStop     | "Subagente completado"        |
| **04_Sound/**     |                           |                  |                               |
|-------------------| `notification.py`         | UserPromptSubmit | Alerta + voz                  |
|-------------------| `task-complete-sound.ps1` | TodoWrite        | Sonido de completado          |
| **05_Harness/**   |                           |                  |                               |
|-------------------| `context_monitor.py`      | **NUEVO**        | Monitoreo de contexto         |
|-------------------| `eval_trigger.py`         | **NUEVO**        | Disparador de evaluación      |

### Hooks Activos (7)

| Hook             | Script                    | Función             |
|------------------|---------------------------|---------------------|
| PreToolUse       | `pre_tool_use.py`         | Batería + seguridad |
| PreToolUse       | `csv-single-validator.py` | Validación CSV      |
| PostToolUse      | `post_tool_use.py`        | Backup + voz        |
| Stop             | `stop.py`                 | Fin de sesión       |
| SubagentStop     | `subagent_stop.py`        | Fin de subagente    |
| UserPromptSubmit | `notification.py`         | Notificaciones      |
| TodoWrite        | `task-complete-sound.ps1` | Sonidos             |

---

## 🔌 8. MCPs (Model Context Protocols)

**Ubicación:** `05_System/01_MCP/`

> Ver configuración específica en `05_System/01_MCP/`

### MCPs Comunes

- GitHub MCP
- Linear MCP
- Vercel MCP
- Playwright MCP
- Supabase MCP
- Postgres MCP
- Filesystem MCP

---

## 📋 9. COMANDOS SDD

**Slash Commands disponibles:**

| Comando                | Propósito       |
|------------------------|-----------------|
| `/sdd-init`            | Inicializar SDD |
| `/sdd-explore <topic>` | Explorar idea   |
| `/sdd-new <change>`    | Nueva cambio    |
| `/sdd-spec`            | Especificar     |
| `/sdd-design`          | Diseñar         |
| `/sdd-tasks`           | Crear tareas    |
| `/sdd-apply`           | Implementar     |
| `/sdd-verify`          | Verificar       |
| `/sdd-archive`         | Archivar        |

---

## 🔗 10. INTEGRACIONES CLAVE

### Anthropic Harness (NUEVO)

| Componente                 | Ubicación                                       | Propósito              |
|----------------------------|-------------------------------------------------|------------------------|
| **Scripts**                | `04_Engine/08_Scripts_Os/11_Anthropic_Harness/` |                        |
| - `00_Safety_Wrapper.py`   |                                                 | Pre-check de seguridad |
| - `01_Context_Manager.py`  |                                                 | Reset vs Compaction    |
| - `02_Evaluator_Runner.py` |                                                 | QA separado (GAN)      |
| - `03_Sprint_Contract.py`  |                                                 | Negocia "done"         |
| - `04_Playwright_QA.py`    |                                                 | Testing interactivo    |
| **Skills**                 | `.agent/02_Skills/14_Anthropic_Harness/`        |                        |
| - `01_Evaluator_Pattern/`  |                                                 | Adversarial eval       |
| - `02_Context_Management/` |                                                 | Reset vs compaction    |
| - `03_Sprint_Contract/`    |                                                 | Generator + Evaluator  |
| **Workflow**               | `.agent/03_Workflows/17_Anthropic_Harness.md`   | Three-Agent Pattern    |

### Pipeline TDD Original

```
01_Scope_Rule_Architect
    ↓
02_TDD_Test_First (Rojo)
    ↓
03_React_Test_Implementer (Verde)
    ↓
04_React_Mentor (Azul)
```

---

## 📊 11. MÉTRICAS DEL SISTEMA

| Categoría            | Target      | Cómo se mide                    |
|----------------------|-------------|---------------------------------|
| Cycle Time (Feature) | <4 horas    | PRD → deploy                    |
| Test Coverage        | >80%        | npm test --coverage             |
| Lighthouse Score     | >90         | SEO + Performance               |
| PR Size              | <400 líneas | git diff --stat                 |
| Escalations          | 0           | Veces que necesita ayuda humana |

---

## 🗂️ 12. ESTRUCTURA DE DIRECTORIOS

```
Think_Different_AI/
├── 00_Core/                    # ADN: AGENTS.md, GOALS.md, BACKLOG.md
├── 01_Brain/                   # Memoria y conocimiento
│   ├── 01_Context_Memory/     # Memoria JSON + MD
│   ├── 02_Knowledge_Brain/    # Base de conocimiento
│   ├── 03_Process_Notes/       # Notas de sesiones
│   ├── 04_Rules/              # Reglas del sistema
│   └── ...
├── 02_Operations/              # Tasks, Evals, Progress
├── 03_Knowledge/               # Research, Marketing, etc
├── 04_Engine/                  # Scripts (86+)
│   └── 08_Scripts_Os/         # Hubs + Anthropic
├── 05_System/                  # MCP, Templates, Env
├── 06_Archive/                 # Backups
└── 07_Projects/               # Labs
    └── .agent/                 # Config AI
        ├── 01_Agents/         # 12 + 24 + 5 = 41 agentes
        ├── 02_Skills/         # 128+ skills
        ├── 03_Workflows/      # 24 workflows
        ├── 04_Extensions/     # Hooks
        └── 05_GGA/            # Code Review
```

---

## 🎯 CONEXIONES CLAVE

### Agente → Skills → Scripts

```
Product Builder (Perfil 01)
    ↓
    ├→ Brainstorming → ce:brainstorm
    ├→ PRD → prd skill
    ├→ React_19 + TypeScript → 05_Vibe_Coding
    ├→ E2E_Testing → 06_Testing
    └→ Anthropic Components → 11_Anthropic_Harness/
```

### Workflow → Hook → Script

```
Frontend Premium Workflow
    ↓
    pre_tool_use (hook)
    ↓
    05_Validator_Hub (script)
    ↓
    post_tool_use (hook)
```

---

## 📝 NOTAS

1. **No tocar agentes #01-12:** Forman pipeline TDD establecido
2. **Extender con Perfiles:** Los 5 perfiles de negocio complementan los 12 agentes
3. **Anthropic Integration:** Solo Perfil 01 tiene referencias. Perfiles 02-05 necesitan actualización
4. **Skills Backup:** 177 skills legacy en 10_Backup/05_Gentleman/
5. **Hooks Activos:** 7 hooks funcionando + 2 nuevos (Harness)

---

*Documento generado automáticamente - 2026-03-26*
