# 🛠️ 03_Skills — Sistema SOTA de Skills

**Versión:** 6.1
**Última actualización:** 2026-03-29
**Source of Truth:** `01_Core/03_Skills/`
**Framework:** Anthropic Skill Creator v2.0 + PersonalOS SOTA

---

## 📂 Estructura Actual (2026-03-29)

```
03_Skills/
├── 00_Skill_Auditor/         ⭐ Auditoría de skills (SOTA)
├── 00_Compound_Engineering/  ⭐ CE Workflows (8 items)
├── 01_Agent_Teams_Lite/      ⭐ SDD Workflow (11 items)
├── 02_Project_Manager/        ⭐ PM Workflow (9 items)
├── 03_Product_Manager/        ⭐ Product (9 items)
├── 04_Product_Design/        ⭐ Design/Taste (13 items)
├── 05_Viba_Coding/          ⭐ Dev Frameworks (18 items)
├── 06_Testing/              ⭐ Testing + GGA (18 items)
├── 07_DevOps/               ⭐ DevOps (13 items)
├── 08_Personal_Os/          ⭐ Personal OS (9 items)
├── 09_Marketing/            ⭐ Marketing (11 items)
├── 10_Backup/               📦 Legacy (5 items)
├── 11_Doc_Processing/       ⭐ Docs (4 items)
├── 12_N8N/                  ⭐ n8n Automation (7 items)
├── 13_System_Master/        ⭐ System (5 items)
├── 14_Anthropic_Harness/    ⭐ Anthropic Patterns (9 items)
├── 15_Skill_Creator/        ⭐ Skill Creator (Anthropic)
└── 08_Plugins/              🔌 Plugins (PersonalOS)
```

**Total: ~160+ skills**

---

## 🏆 LAS 9 CATEGORÍAS DE ANTHROPIC (Framework Oficial)

> **Fuente:** Thariq (Claude Code Team @ Anthropic) - "Lessons from Building Claude Code: How We Use Skills"

### Tabla de Categorías

| # | Categoría | Propósito | Ejemplo PersonalOS |
|---|-----------|-----------|-------------------|
| 1 | **Library / API Reference** | Enseñar a usar librerías | `nextjs-15`, `react-19`, `zod-4` |
| 2 | **Product Verification** | Confirmar features funcionan | `pr-review`, `technical-review` |
| 3 | **Data Fetching** | Obtener datos externos | `analytics-tracking`, `agent-browser` |
| 4 | **Business Process** | Hacer cumplir reglas/workflows | `sdd-workflow`, `planning-tasks-ai` |
| 5 | **Code Scaffolding** | Generar boilerplate | `skill-creator`, `angular-architecture` |
| 6 | **Code Quality** | Code review y linting | `testing-coverage`, `security-review` |
| 7 | **CI/CD** | Deploy y pipelines | Observabilidad, deployment |
| 8 | **Runbooks** | Respuesta a incidentes | `systematic-debugging`, `verification-before-completion` |
| 9 | **Infrastructure Ops** | Operaciones de servidor/DB | `mcp-client`, `django-drf` |

### Mapping con PersonalOS

```
Anthropic Category          → PersonalOS Skills
─────────────────────────────────────────────────
Library / API Reference     → 05_Viba_Coding/* (dev frameworks)
Product Verification        → 06_Testing/*, 14_Anthropic_Harness/*
Data Fetching              → 13_System_Master/04_Mcp_Builder
Business Process           → 01_Agent_Teams_Lite/*, 02_Project_Manager/*
Code Scaffolding           → 15_Skill_Creator, angular-architecture
Code Quality               → 06_Testing/*, pr-review, security-review
CI/CD                      → 07_DevOps/*
Runbooks                   → systematic-debugging, verification
Infrastructure Ops         → 13_System_Master/*, 12_N8N/*
```

---

## 🎯 MEJORES PRÁCTICAS ANTHROPIC 2026 (SOTA)

> **Integradas del paper de Thariq (Anthropic)**

### 1. 📝 Always Include a Gotchas Section

**ERRORES que los docs no dicen:**
```
## ⚠️ Gotchas

- Always check `.env.local` before running `npm run build`
- Never use `--force` in production
- This API rate-limits at 60 req/min — add sleep in batch jobs
```
**Impacto:** Skills con Gotchas mejoran measurablemente la precisión de Claude.

### 2. 📂 Progressive Disclosure

**NO poner todo en un README.** Dividir en sub-archivos:
```
skill/
├── README.md          # Overview only
├── advanced.md        # Pulled on demand
└── troubleshooting.md # Pulled on demand
```
**Por qué:** Contexto es recurso finito. No quemarlo en cosas innecesarias.

### 3. 🎣 On-Demand Hooks (Pattern /careful)

```
# careful skill

During this session, always ask for confirmation before running:
- git reset --hard
- rm -rf
- DROP TABLE
```
**Pattern:** Activar solo cuando necesitas seguridad adicional. No es permanente.

### 4. 📦 Bundle Scripts in Skill Folder

Skills no son solo markdown. Incluir scripts ejecutables:
```
deploy-skill/
├── README.md
└── scripts/
    ├── pre-deploy-check.sh
    ├── rollback.sh
    └── notify-slack.py
```

### 5. ✍️ Write Descriptions That Tell Claude WHEN to Use

| ❌ BAD | ✅ GOOD |
|--------|---------|
| "deployment stuff" | "Production deploys, rollbacks, and health checks" |
| "DB operations" | "PostgreSQL CRUD, migrations, and backups" |
| "code review" | "Type safety, error handling, and security vulnerability review" |

---

## 🔬 SKILL AUDITOR (Sistema de Calidad)

> **Ubicación:** `00_Skill_Auditor/`

El **Skill Auditor** audita skills contra estándares **Anthropic SOTA v5.1** + **Skill Creator v2.0**.

### Criterios de Auditoría

| Criterio | Descripción |
|----------|-------------|
| YAML Frontmatter | name, description con triggers |
| Progressive Disclosure | < 200 líneas ideal, < 500 máx |
| Gotchas Section | Mínimo 3 errores documentados |
| Esencia Original | Propósito claro de la skill |
| State Persistence | Dónde guardar estado |

### Scoring

| Score | Rating |
|-------|--------|
| 90-100% | ✅ Excellent - Ready for production |
| 70-89% | 👍 Good - Minor improvements needed |
| 50-69% | ⚠️ Needs Work - Significant fixes required |
| <50% | ❌ Failed - Do not integrate |

### Uso
```bash
# Auditar una skill
python 00_Skill_Auditor/scripts/audit-skills.py

# Validar esencia
python 00_Skill_Auditor/scripts/validate-essence.py
```

---

## 🤖 SKILL CREATOR (Anthropic Official)

> **Ubicación:** `15_Skill_Creator_Oficial/`, `08_Plugins/01_Staff_Claude_Code/`

El **Skill Creator** genera scaffolding de skills automáticamente mediante conversación.

### Features v2.0

| Feature | Descripción |
|---------|-------------|
| evals.json | Skills que usan evaluación automática |
| Benchmark results | Skills críticas del OS |
| agents/ folder | Sub-agentes especializados |
| references/ | Docs pesadas separadas |

### Estructura Generada
```
skill-name/
├── SKILL.md              # Instrucciones principales
├── README.md             # Documentación
├── references/           # Docs adicionales
│   ├── schemas.md
│   └── examples.md
├── scripts/             # Código reutilizable
├── agents/              # Sub-agentes
└── evals.json          # Evaluación automática
```

---

## 📋 TOP Skills Rankings

### 01_Core (Priority #1)

| # | Skill | Propósito |
|---|-------|-----------|
| 1 | Fork Terminal | Multiplexar terminal sessions |
| 2 | Parallel Orchestration | Agent teams parallel execution |
| 3 | Premium Git Manager | Git workflows avanzados |
| 4 | Subagent Driven Development | Arquitectura multi-agent |
| 5 | **Skill Auditor** | Auditoría de quality |
| 6 | **Skill Creator** | Crear skills automáticamente |

### 05_Viba_Coding (Development Frameworks)

| # | Skill | Propósito |
|---|-------|-----------|
| 1 | **react-19** | React moderno con Server Components |
| 2 | **nextjs-15** | Next.js App Router |
| 3 | **tailwind-4** | Tailwind CSS v4 |
| 4 | **zod-4** | Validación de schemas |
| 5 | **zustand-5** | State management |
| 6 | **ai-sdk-5** | AI SDK integration |
| 7 | **playwright** | E2E testing |
| 8 | **angular** | Angular patterns |

### 06_Testing (Quality)

| # | Skill | Propósito |
|---|-------|-----------|
| 1 | **technical-review** | Code review técnico |
| 2 | **pr-review** | Pull request review |
| 3 | **testing-coverage** | Coverage optimization |
| 4 | **go-testing** | Go testing patterns |
| 5 | **skill-auditor** | Quality Guardian |

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

## 📊 Estadísticas (2026-03-29)

| Carpeta | Skills | Categoría Anthropic |
|---------|--------|---------------------|
| 00_Skill_Auditor | 1 | Quality |
| 01_Agent_Teams_Lite | 9 | Business Process |
| 02_Project_Manager | 9 | Business Process |
| 03_Product_Manager | 8 | Product Verification |
| 04_Product_Design | 11 | Code Quality |
| 05_Viba_Coding | 21 | Library/API Reference |
| 06_Testing | 18 | Code Quality |
| 07_DevOps | 13 | CI/CD |
| 08_Personal_Os | 9 | Runbooks |
| 09_Marketing | 11 | Data Fetching |
| 11_Doc_Processing | 4 | Data Fetching |
| 12_N8N | 7 | Infrastructure Ops |
| 13_System_Master | 5 | Infrastructure Ops |
| 14_Anthropic_Harness | 9 | All Categories |
| 15_Skill_Creator | 1 | Code Scaffolding |

**Total Activo:** 140 skills
**Total con Backup:** 167 skills

---

## 🚀 Uso de Skills

```bash
# Inicializar SDD
/sdd:init

# Explorar dominio
/sdd:explore

# Crear nuevo cambio
/sdd:new [name]

# Auditar skills
/skillaudit

# Crear skill
/skillcreate
```

---

## 📚 Documentación

- [03_Knowledge/01_Research_Knowledge/Skills_TOP_Rankings.md](../../03_Knowledge/01_Research_Knowledge/Skills_TOP_Rankings.md)
- [Sistema_SOTA_Skills.md](../../Sistema_SOTA_Skills.md)
- [Skills_Top_20.md](../../Skills_Top_20.md)

---

## 🧠 El Modelo Mental (Aprendizaje Anthropic)

| Entendimiento Anterior | Entendimiento Correcto |
|------------------------|------------------------|
| Skills = notas markdown | Skills = carpetas (scripts incluidos) |
| Set it and forget it | Mantenimiento continuo |
| Info para Claude | Tools que Claude puede ejecutar |
| Useful add-on | Core workflow infrastructure |

> **La clave:** Skills se **cultivan**, no se construyen.
> No escribas una skill perfecta el día uno. Empieza con un README, agrega Gotchas cuando hits edge cases, re-estructura con Progressive Disclosure cuando el archivo crece, inyecta scripts cuando te pillás dando las mismas instrucciones repetidamente.

---

*"El poder sin control no sirve de nada. El poder con las skills correctas lo cambia todo."*

© 2026 PersonalOS v6.1 — Powered by Anthropic Skill Framework
