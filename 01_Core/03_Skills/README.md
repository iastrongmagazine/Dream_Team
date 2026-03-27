# 🛠️ 02_Skills — Sistema SOTA de Skills

**Versión:** 4.0  
**Última actualización:** 2026-03-26  
**Source of Truth:** `.agent/02_Skills/`  
**Sync Target:** `.cursor/02_Skills/`

---

## 📂 Estructura Actual (2026-03-26)

```
02_Skills/
├── 00_Compound_Engineering/ ⭐ CE Workflows (8 items)
├── 00_Skill_Auditor/         ⭐ Auditoría (3 items)
├── 01_Agent_Teams_Lite/      ⭐ SDD Workflow (11 items)
├── 02_Project_Manager/        ⭐ PM Workflow (9 items)
├── 03_Product_Manager/       ⭐ Product (9 items)
├── 04_Product_Design/        ⭐ Design/Taste (13 items)
├── 05_Vibe_Coding/           ⭐ Dev Frameworks (18 items)
├── 06_Testing/               ⭐ Testing + GGA (18 items)
├── 07_DevOps/                ⭐ DevOps (13 items)
├── 08_Personal_Os/           ⭐ Personal OS (9 items)
├── 09_Marketing/             ⭐ Marketing (11 items)
├── 10_Backup/                📦 Legacy (5 items)
├── 11_Doc_Processing/        ⭐ Docs (4 items)
├── 12_N8N/                   ⭐ n8n Automation (7 items)
├── 13_System_Master/         ⭐ System (5 items)
└── 14_Anthropic_Harness/    ⭐ Anthropic Patterns + Plugins (9 items)
```

**Total: ~160+ skills**

> **IMPORTANTE:** `05_Gentleman_System/` es BACKUP histórico. `07_Every/` es la versión ACTIVA.

---

## 🏆 TOP Skills Rankings

### 01_Core (Priority #1)

| #     | Skill                         | Propósito                        |
|-------|-------------------------------|----------------------------------|
| 1     | Fork Terminal                 | Multiplexar terminal sessions    |
| 2     | Parallel Orchestration        | Agent teams parallel execution   |
| 3     | Premium Git Manager           | Git workflows avanzados          |
| 4     | Subagent Driven Development   | Arquitectura multi-agent         |
| 5     | Antigravity Skill Creator     | Crear skills automáticamente     |

### 04_Product_Manager (Priority #5 — PM Workflow)

| #     | Skill                      | Propósito                         |
|-------|----------------------------|-----------------------------------|
| 1     | brainstorming              | Exploración de ideas              |
| 2     | writing-plans              | Creación de planes                |
| 3     | executing-plans            | Ejecución de planes               |
| 4     | jira-epic                  | Creación de epics en Jira         |
| 5     | jira-task                  | Gestión de tareas en Jira         |
| 6     | github-pr                  | Workflow de PRs                   |
| 7     | writing-strategy-memos     | Memos estratégicos                |
| 8     | planning-tasks-ai          | Planificación con AI              |

### 06_Taste_Skills (Priority #6 — Premium Design)

| #     | Skill                  | Propósito                                | Uso                    |
|-------|------------------------|------------------------------------------|------------------------|
| 1     | **taste-skill**        | Diseño premium variance/motion/density   | OBLIGATORIO frontend   |
| 2     | **soft-skill**         | Look expensive — Awwwards tier           | Premium projects       |
| 3     | **minimalist-skill**   | Notion/Linear style                      | Dashboards             |
| 4     | **redesign-skill**     | Upgrade proyectos existentes             | Legacy projects        |
| 5     | **output-skill**       | Full output enforcement                  | Siempre                |

### 07_Every/01_Plan (Planning)

| #     | Skill             | Propósito                  |
|-------|-------------------|----------------------------|
| 1     | deep-research     | Investigación exhaustiva   |
| 2     | brainstorming     | Generación de ideas        |
| 3     | writing-plans     | Documentación de planes    |
| 4     | executing-plans   | Ejecución sistemática      |
| 5     | issue-creation    | Creación de issues         |

### 07_Every/02_Work (Development)

| #     | Skill            | Propósito                                          |
|-------|------------------|----------------------------------------------------|
| 1     | **react-19**     | React moderno con Server Components                |
| 2     | **nextjs-15**    | Next.js App Router                                 |
| 3     | **tailwind-4**   | Tailwind CSS v4                                    |
| 4     | **zod-4**        | Validación de schemas                              |
| 5     | **zustand-5**    | State management                                   |
| 6     | **ai-sdk-5**     | AI SDK integration                                 |
| 7     | **playwright**   | E2E testing                                        |
| 8     | **angular**      | Angular (architecture, core, forms, performance)   |

### 07_Every/03_Review (Quality)

| #     | Skill                  | Propósito               |
|-------|------------------------|-------------------------|
| 1     | **technical-review**   | Code review técnico     |
| 2     | **pr-review**          | Pull request review     |
| 3     | **testing-coverage**   | Coverage optimization   |
| 4     | **go-testing**         | Go testing patterns     |
| 5     | **tui-quality**        | TUI quality standards   |

### 07_Every/04_Compound (Compound Engineering)

| #     | Skill                              | Propósito                  |
|-------|------------------------------------|----------------------------|
| 1     | **gentleman-trainer**              | Training workflows         |
| 2     | **analytics-workflow**             | Analytics implementation   |
| 3     | **dieter-rams-design**             | Design principles          |
| 4     | **advanced-context-engineering**   | Context optimization       |
| 5     | **memory-protocol**                | Memory patterns            |
| 6     | **compound-engine**                | Compound engineering       |

### 07_Every/05_Utilities (SOTA Tools)

| #     | Skill                     | Propósito                   |
|-------|---------------------------|-----------------------------|
| 1     | **mcp-integration**       | MCP server setup            |
| 2     | **e2e-testing-skill**     | E2E test automation         |
| 3     | **edge-case-skill**       | Edge case handling          |
| 4     | **evaluation-skill**      | Evaluation frameworks       |
| 5     | **test-coverage-skill**   | Test coverage analysis      |
| 6     | **observability-skill**   | Metrics, logging, tracing   |

---

## 🔄 Sincronización

```bash
# Sync .agent → .cursor (unidirectional)
python 08_Scripts_Os/55_Sync_Skills.py --confirm
```

### Flujo:
1. Detectar cambios en `.agent/`
2. Backup automático de `.cursor/`
3. Copiar `.agent` → `.cursor`

---

## 📊 Estadísticas (2026-03-25)

| Carpeta                | Skills     | Rol            |
|------------------------|------------|----------------|
| 01_Agent_Teams_Lite    | 9          | SDD            |
| 02_Project_Manager     | 9          | PM             |
| 03_Product_Manager     | 8          | Product        |
| 04_Product_Design      | 11         | Design         |
| 05_Vibe_Coding         | 21         | Dev            |
| 06_Testing             | 18         | Testing+GGA    |
| 07_DevOps              | 13         | DevOps         |
| 08_Personal_Os         | 9          | OS             |
| 09_Marketing           | 11         | Marketing      |
| 10_Backup/05_Gentleman | 27         | Legacy         |
| 11_Doc_Processing      | 4          | Docs           |
| 12_N8N                 | 7          | Automation     |

**Total Activo:** 140 skills
**Total con Backup:** 167 skills

---

## 📚 Documentación

- [03_Knowledge/01_Research_Knowledge/Skills_TOP_Rankings.md](../../03_Knowledge/01_Research_Knowledge/Skills_TOP_Rankings.md) — Rankings completos
- [Sistema_SOTA_Skills.md](../../Sistema_SOTA_Skills.md) — Guía maestra
- [Skills_Top_20.md](../../Skills_Top_20.md) — Rankings TOP 20

---

## 🚀 Uso de Skills

Las skills se invocan automáticamente según el contexto o manualmente:

```bash
/sdd:init        # Inicializar SDD
/sdd:explore     # Explorar dominio
/sdd:new [name]  # Crear nuevo cambio
```

### Reglas de Uso:

1. **Sincronización:** `.agent/07_Every/` → `.cursor/02_Skills/`
2. **Taste-Skills:** Usar `06_Taste_Skills/` para TODO frontend
3. **SDD:** Usar `03_Agent_Teams_Lite/` para desarrollo guiado por specs
4. **Backup:** `05_Gentleman_System/` es referencia histórica — NO editar

---

---

_"El poder sin control no sirve de nada. El poder con las skills correctas lo cambia todo."_

© 2026 PersonalOS
