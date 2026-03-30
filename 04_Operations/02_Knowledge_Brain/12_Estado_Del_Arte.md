# 🏛️ ESTADO DEL ARTE — Think Different PersonalOS

> **Versión:** 6.0 (SOTA + Anthropic Integration)
> **Fecha:** 2026-03-26
> **Estado:** ✅ Active | **Python:** 3.14+ | **Skills:** 128+ auditadas

---

## 🚀 RESUMEN EJECUTIVO

| Métrica                 | Valor                      |
|-------------------------|----------------------------|
| **Agentes Principales** | 12 (Pipeline TDD)          |
| **Especialistas**       | 24                         |
| **Perfiles de Negocio** | 5 (SOTA: Anthropic)        |
| **Skills**              | 128+ en 15 categorías      |
| **Scripts**             | 86+ en 10 Hubs             |
| **Workflows**           | 24                         |
| **Hooks**               | 12 (7 activos + Anthropic) |
| **MCPs**                | 36 servidores              |

---

## 🎯 HIGHLIGHTS v6.0 — Anthropic Integration

### 🏗️ Three-Agent Architecture (SOTA Pattern)

> Inspirado en el artículo de Anthropic sobre Harness Design.

| Agente        | Rol                               | Input       | Output         |
|---------------|-----------------------------------|-------------|----------------|
| **Planner**   | 1-4 oraciones → spec completo     | User prompt | Full spec      |
| **Generator** | Construye feature por feature     | Spec        | Código         |
| **Evaluator** | QA separado (NO self-evaluation!) | Running app | Bugs + grading |

**Componentes nuevos:**

| Componente           | Ubicación                                                             | Propósito              |
|----------------------|-----------------------------------------------------------------------|------------------------|
| **Safety Wrapper**   | `08_Scripts_Os/11_Anthropic_Harness/00_Safety_Wrapper.py`   | Pre-check de seguridad |
| **Context Manager**  | `08_Scripts_Os/11_Anthropic_Harness/01_Context_Manager.py`  | Reset vs Compaction    |
| **Evaluator Runner** | `08_Scripts_Os/11_Anthropic_Harness/02_Evaluator_Runner.py` | QA separado (GAN)      |
| **Sprint Contract**  | `08_Scripts_Os/11_Anthropic_Harness/03_Sprint_Contract.py`  | Negocia "done"         |
| **Playwright QA**    | `08_Scripts_Os/11_Anthropic_Harness/04_Playwright_QA.py`    | Testing interactivo    |

**Skills Anthropic:**
- `01_Core/03_Skills/14_Anthropic_Harness/01_Evaluator_Pattern/`
- `01_Core/03_Skills/14_Anthropic_Harness/02_Context_Management/`
- `01_Core/03_Skills/14_Anthropic_Harness/03_Sprint_Contract/`

**Workflow:**
- `.agent/03_Workflows/17_Anthropic_Harness.md`

---

## 🏗️ Arquitectura del Sistema (8 Dimensiones)

```
Think_Different_AI/
├── 00_Core/              # ADN: AGENTS.md, GOALS.md, BACKLOG.md, PROGRESS.md
│
├── 01_Core/             # Cerebro: Memoria, Conocimiento, Reglas
│   ├── 01_Context_Memory/    # Memoria a largo plazo
│   ├── 02_Knowledge_Brain/  # Base de conocimiento (+ 11_System_Mapping.md)
│   ├── 03_Process_Notes/     # Notas de sesiones
│   ├── 04_Rules/             # 21 reglas del sistema
│   ├── 05_Templates/         # Plantillas
│   ├── 06_Backup_Central/   # Backups
│   ├── 07_Memory_Brain/     # Mapeos y análisis
│   ├── 08_Audit_Sota/       # Auditorías SOTA
│   └── 09_Momentum_Os/      # Proyectos de referencia
│
├── 04_Operations/        # Manos: Tasks, Evals, Progress
│   ├── 01_Active_Tasks/     # Tareas activas
│   ├── 02_Evals/            # Evaluaciones
│   ├── 03_Analytics/        # Analíticas
│   └── 04_Progress/         # Reportes
│
├── 03_Knowledge/         # Memoria: Research, Notas, Recursos
│   ├── 01_Research_Knowledge/
│   ├── 02_Notes_Brain/
│   ├── 03_Resources_External/
│   ├── 04_Examples_Guide/
│   ├── 05_Marketing_Strategy/
│   ├── 06_Writing_Content/
│   ├── 07_Voice_Profiles/
│   ├── 08_Config_Files/
│   ├── 09_Archive_Recovery/
│   ├── 10_Repos_Gentleman/
│   ├── 11_Legacy_Resources/
│   ├── 12_Resources/
│   └── 13_Strategic_Plans/
│
├── 04_Operations/            # Motor: Scripts (10 Hubs)
│   ├── 00_Config/
│   ├── 08_Scripts_Os/      # 86+ scripts
│   │   ├── 01_Auditor_Hub.py
│   │   ├── 02_Git_Hub.py
│   │   ├── 03_AIPM_Hub.py
│   │   ├── 04_Ritual_Hub.py
│   │   ├── 05_Validator_Hub.py
│   │   ├── 06_Tool_Hub.py
│   │   ├── 07_Integration_Hub.py
│   │   ├── 08_Workflow_Hub.py
│   │   ├── 09_Data_Hub.py
│   │   ├── 10_General_Hub.py
│   │   └── 11_Anthropic_Harness/  # ⭐ NUEVO
│   └── ...
│
├── 05_System/            # Chasis: Core, MCP, Templates, Env
│   ├── 01_MCP/              # Configuración MCPs
│   ├── 02_Templates/
│   ├── 03_Integrations/
│   ├── 04_Env/
│   ├── 05_Docs/
│   └── 06_Evals/
│
├── 06_Archive/           # Baúl: Backups, Legacy, Docs
│   ├── 00_Backups/
│   ├── 02_Engine_Legacy/
│   ├── 03_Documentation/
│   ├── 04_Plans/
│   ├── 05_Tasks_Archive/
│   ├── 07_Process_Notes_Legacy/
│   ├── 08_Logs/
│   ├── 09_Config_Archive/
│   ├── 10_Structure_Archive/
│   ├── 11_Digital_Garden/
│   ├── 12_Oil_Drilling_Legacy/
│   └── 13_Script_Aud_Perfiles/
│
└── 07_Projects/          # Labs: Projects, Focus_Now_Lab

```

---

## 🤖 AGENTES

### 12 Agentes Principales (Pipeline TDD)

| #   | Archivo                        | Propósito            |
|-----|--------------------------------|----------------------|
| 00  | `00_Orchestrator.md`           | Orquestador maestro  |
| 01  | `01_Scope_Rule_Architect.md`   | Define alcance       |
| 02  | `02_TDD_Test_First.md`         | Tests primero (Rojo) |
| 03  | `03_React_Test_Implementer.md` | Implementa (Verde)   |
| 04  | `04_React_Mentor.md`           | Refactor (Azul)      |
| 05  | `05_Security_Auditor.md`       | Seguridad            |
| 06  | `06_Git_Workflow_Manager.md`   | Git                  |
| 07  | `07_Accessibility_Auditor.md`  | Accesibilidad        |
| 08  | `08_PRD_Dashboard_Template.md` | Templates PRD        |
| 09  | `09_Design_SOP_Document.md`    | Docs diseño          |
| 10  | `10_Workflow_Orchestrator.md`  | Workflows            |
| 11  | `11_AIPM_Judge.md`             | Evaluación AI        |
| 12  | `12_LFG_Autonomous_Engine.md`  | Motor autónomo       |

### 24 Especialistas

Ubicación: `.agent/01_Agents/Specialists/`

- **Code Reviewers:** Kieran-TypeScript, Kieran-Rails, Kieran-Python, Dhh-Rails, Code-Simplicity
- **Design:** Design-Iterator, Design-Implementation-Reviewer, Figma-Design-Sync
- **Data:** Data-Migration-Expert, Data-Integrity-Guardian
- **Research:** Repo-Research-Analyst, Best-Practices-Researcher, Framework-Docs-Researcher
- **Infrastructure:** Performance-Oracle, Security-Sentinel, Architecture-Strategist

### 5 Perfiles de Negocio (SOTA)

Ubicación: `.agent/01_Agents/Perfiles/`

| #   | Perfil                    | Propósito                     | Anthropic   |
|-----|---------------------------|-------------------------------|-------------|
| 01  | `01_Product_Builder.md`   | Features completas PRD→deploy | ✅           |
| 02  | `02_Data_Engineer.md`     | Pipelines datos, ETL          | ✅           |
| 03  | `03_Marketing_Tech.md`    | SEO, ads, contenido           | ✅           |
| 04  | `04_Design_Ops.md`        | Design systems                | ✅           |
| 05  | `05_Platform_Engineer.md` | Infraestructura, MCPs         | ✅           |

---

## 🛠️ SKILLS (128+)

### Por Categoría (01_Core/03_Skills/)

| Categoría            | Skills   | Estado       |
|----------------------|----------|--------------|
| 01_Agent_Teams_Lite  | 9        | ⏭️ Sin tocar |
| 02_Project_Manager   | 9        | ✅ 100%       |
| 03_Product_Manager   | 7        | ✅ 100%       |
| 04_Product_Design    | 11       | ✅ 100%       |
| 05_Vibe_Coding       | 21       | ✅ 100%       |
| 06_Testing           | 13       | ✅ 100%       |
| 07_DevOps            | 12       | ✅ 100%       |
| 08_Personal_Os       | 10       | ✅ 100%       |
| 09_Marketing         | 32       | ✅ 100%       |
| 10_Backup            | 177      | 📦 Legacy     |
| 11_Doc_Processing    | 3        | ✅ 100%       |
| 12_N8N               | 7        | ✅ 100%       |
| 13_System_Master     | 1        | ✅ 100%       |
| 14_Anthropic_Harness | 3        | ⭐ NUEVO      |

### TASTE-SKILLS (Frontend Premium)

| Skill                | Uso                             |
|----------------------|---------------------------------|
| **taste-skill**      | Diseño desde cero - premium     |
| **soft-skill**       | Proyectos premium, invitaciones |
| **minimalist-skill** | Estilo Notion/Linear            |
| **redesign-skill**   | Mejorar proyectos existentes    |
| **output-skill**     | Código completo                 |

---

## 📜 SCRIPTS (86+)

### 10 Hubs Maestros

| Hub   | Script                  | Función        |
|-------|-------------------------|----------------|
| 01    | `01_Auditor_Hub.py`     | Auditorías     |
| 02    | `02_Git_Hub.py`         | Git operations |
| 03    | `03_AIPM_Hub.py`        | AI PM          |
| 04    | `04_Ritual_Hub.py`      | Rituales       |
| 05    | `05_Validator_Hub.py`   | Validación     |
| 06    | `06_Tool_Hub.py`        | Herramientas   |
| 07    | `07_Integration_Hub.py` | Integraciones  |
| 08    | `08_Workflow_Hub.py`    | Workflows      |
| 09    | `09_Data_Hub.py`        | Datos          |
| 10    | `10_General_Hub.py`     | Generales      |

### Scripts Antropomórficos

```
01_Auditor_Hub.py      🤖 Iron Man - Auditor
02_Git_Hub.py         🔧 Thor - Git
03_AIPM_Hub.py        📊 JARVIS - AI PM
04_Ritual_Hub.py      ⏰ Hulk - Rituales
05_Validator_Hub.py   ✅ Rocket - Validaciones
06_Tool_Hub.py        🔨 Widow - Herramientas
07_Integration_Hub.py 🔗 Vision - Integraciones
08_Workflow_Hub.py    🔀 Strange - Workflows
09_Data_Hub.py        📈 Mantis - Datos
10_General_Hub.py     🦸‍♂️ General - Varios
```

---

## 🔄 WORKFLOWS (24)

Ubicación: `.agent/03_Workflows/`

| #     | Workflow                  | Tipo                  |
|-------|---------------------------|-----------------------|
| 00-16 | Workflows clásicos        | Varios                |
| 17    | `17_Anthropic_Harness.md` | ⭐ NUEVO - Three-Agent |

---

## 🪝 HOOKS (12)

Ubicación: `.agent/04_Extensions/hooks/`

| #               | Hook                      | Trigger          | Función             |
|-----------------|---------------------------|------------------|---------------------|
| 01              | `pre_tool_use.py`         | PreToolUse       | Batería + seguridad |
| 02              | `csv-single-validator.py` | PreToolUse       | Validación CSV      |
| 03              | `post_tool_use.py`        | PostToolUse      | Backup + voz        |
| 04              | `stop.py`                 | Stop             | Fin de sesión       |
| 05              | `subagent_stop.py`        | SubagentStop     | Fin de subagente    |
| 06              | `notification.py`         | UserPromptSubmit | Notificaciones      |
| 07              | `task-complete-sound.ps1` | TodoWrite        | Sonidos             |
| **05_Harness/** |                           |                  |                     |
| 08              | `context_monitor.py`      | **NUEVO**        | Monitoreo contexto  |
| 09              | `eval_trigger.py`         | **NUEVO**        | Evaluación          |

---

## 🔌 MCPs (36 servidores)

| Categoría   | MCPs                                |
|-------------|-------------------------------------|
| Búsqueda    | exa, brave-search, stackoverflow    |
| Memoria     | engram, aim-memory-bank, notebooklm |
| Notas       | Notion, mcp-obsidian, obsidian-api  |
| Browser     | Playwright, chrome-devtools         |
| AI & Código | context7, zai-mcp-server, github    |
| Datos       | supabase, postgres, sqlite          |
| Workflow    | n8n-mcp, Linear, jira-extended      |
| Diseño      | excalidraw-yctimlin, pencil         |

---

## 📋 COMANDOS SDD

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

## 📊 MAPA COMPLETO

**Documento detallado:** `01_Core/02_Knowledge_Brain/11_System_Mapping.md`

---

## 🗂️ ESTRUCTURA DE DIRECTORIOS CLAVE

### .agent/ (Config AI)

```
.agent/
├── 01_Agents/              # 12 + 24 + 5 = 41 agentes
│   ├── 00-12_*.md         # Agentes principales
│   ├── Specialists/       # 24 especialistas
│   └── Perfiles/          # 5 perfiles de negocio
├── 02_Skills/             # 128+ skills en 15 cats
├── 03_Workflows/          # 24 workflows
├── 04_Extensions/         # Hooks
└── 05_GGA/                # Code Review
```

### .cursor/ (Sincronizado con .agent/)

Misma estructura que `.agent/` - sincronizado automáticamente.

---

## ✅ CHECKPOINT LIST

- [x] Agentes principales (12) - Pipeline TDD
- [x] Especialistas (24)
- [x] Perfiles de negocio (5) - Anthropic Ready
- [x] Skills (128+) auditadas
- [x] Scripts (86+) en 10 Hubs
- [x] Workflows (24)
- [x] Hooks (12) - 7 activos + Anthropic
- [x] MCPs (36) configurados
- [x] Sistema Mapping completo
- [x] Estado del Arte actualizado

---

## 📝 NOTAS

1. **No tocar agentes #01-12:** Forman pipeline TDD establecido
2. **Extender con Perfiles:** Los 5 perfiles complementan los 12 agentes
3. **Anthropic Integration:** 5/5 perfiles tienen referencias a Harness
4. **Skills Backup:** 177 skills legacy en 10_Backup/05_Gentleman/
5. **QMD:** 2051 archivos indexados (BM25 + Vector)

---

*Documento SOTA v6.0 - 2026-03-26*
