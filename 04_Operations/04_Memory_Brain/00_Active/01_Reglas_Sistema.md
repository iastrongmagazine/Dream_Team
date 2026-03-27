# 📜 REGLAS DEL SISTEMA - Think Different AI

> **Fecha**: 2026-03-25
> **Proyecto**: Think Different AI PersonalOS
> **Estado**: v5.0 - MATRIX RECARGADO

- --

## 🔄 SISTEMA ACTUAL (2026-03-25)

### Matrix Recargado

| Métrica               | Cantidad   | Estado               |
|-----------------------|------------|----------------------|
| **Skills Totales**    | ~440       | ✅                    |
| **Skills Gentleman**  | 139+       | ✅                    |
| **CE Componentes**    | 131        | ✅                    |
| **Scripts Activos**   | 13         | ✅ (de 93 originales) |
| **MCPs Configurados** | 35         | ✅                    |
| **Hooks Activos**     | 7          | ✅                    |

- --

## 🔴 REGLAS FUNDAMENTALES

### 00. Protocolo Génesis (OBLIGATORIO)

Al iniciar una nueva sesión, ejecutar esta secuencia **ANTES** de responder:

1. Leer `@AGENTS.md` en `00_Core/AGENTS.md`
2. Leer `.cursor/00_Rules/01_Context_Protocol.mdc` (reglas de sesión)
3. Leer `01_Brain/01_Context_Memory/` (memoria a largo plazo)
4. Leer `01_Brain/03_Process_Notes/` (contexto reciente)
5. Leer Todo el Proyecto en General
6. **Reportar en chat** un resumen del contexto cargado

- --

## ⚙️ REGLAS OPERATIVAS

### 01. Orchestrator Mode

* *YOU ARE A COORDINATOR, NOT AN EXECUTOR.**

| Allowed Actions                 | NOT Allowed                                  |
|---------------------------------|----------------------------------------------|
| Short answers                   | Reading/writing code inline                  |
| Coordinate phases               | Analyzing code inline                        |
| Show summaries                  | Writing specs/proposals inline               |
| Ask decisions                   | Doing "quick" analysis                       |
| Track state                     | Any execution work                           |

* *Hard Stop Rule**: Antes de usar Read, Edit, Write, o Grep en archivos source/config/skill:
1. **STOP** — ¿Es orquestación o ejecución?
2. Si ejecución → **DELEGATE A SUB-AGENT**
3. **"It's just a small change" NO ES válido**

### 02. Pure Green Protocol

> El sistema debe estar 100% funcional después de cada cierre de sesión.

- No dejar cambios unstaged
- Commit atómico antes de cerrar
- Verificar que todo funciona

### 03. Commit Rules

1. **NEVER** add "Co-Authored-By" or AI attribution
2. **USE** conventional commits: `feat:`, `fix:`, `chore:`, `docs:`
3. **NEVER** build after changes
4. **ALWAYS** verify before commit

- --

## 🎯 REGLAS DE TAREAS

### Task Types (SOTA / Media / Corta)

| Tipo                    | Descripcion                                        | Tiempo Est.                 | Ejemplos                                             |
|-------------------------|----------------------------------------------------|-----------------------------|------------------------------------------------------|
| **SOTA**                | Investigación profunda, arquitectura               | 2-4 horas                   | Reorganizar sistema, nueva metodología               |
| **Media**               | Features, refactoring                              | 30-60 min                   | Agregar feature, refactorizar módulo                 |
| **Corta**               | Fixes, small changes                               | 5-15 min                    | Bug fix, typo, small improvement                     |

### Task Template

```yaml
- --
title: [Actionable task name]
category: [technical|outreach|research|writing|content|admin|personal|other]
priority: [P0|P1|P2|P3]
status: n  # n=not_started, s=started, b=blocked, d=done

created_date: [YYYY-MM-DD]
due_date: [YYYY-MM-DD]  # optional

estimated_time: [minutes]  # optional

resource_refs:
  - path/to/reference.md
- --

# [Task name]

## Context

Tie to goals and reference material.

## Next Actions

- [ ] Step one
- [ ] Step two

## Progress Log

- YYYY-MM-DD: Notes, blockers, decisions.
```

- --

## 🏷️ REGLAS DE NOMBRADO (SKILLS)

### Convenciones Estrictas

| Regla                                 | Correcto                           | Incorrecto                         |
|---------------------------------------|------------------------------------|------------------------------------|
| 2 dígitos para números                | `01_Project_Manager`               | `1_Project_Manager`                |
| PascalCase                            | `01_Morning_Standup`               | `01_morning_standup`               |
| Guion bajo para separar               | `01_Brand_Identity`                | `01-brand-identity`                |
| Secuencia PERFECTA                    | `01, 02, 03...`                    | `01, 03, 05...`                    |
| Primera letra MAYÚSCULA               | `01_Project_Manager`               | `01_project_manager`               |

### Estructura de Perfiles (Matrix Recargado)

```
.agent/02_Skills/
├── 00_Compound_Engineering/  (131 componentes) 🔥 CE
│   ├── 01_Agents_Review/     (23 agents)
│   ├── 02_Agents_DocReview/  (6 agents)
│   ├── 03_Agents_Design/     (3 agents)
│   ├── 04_Agents_Research/   (6 agents)
│   ├── 05_Agents_Workflow/   (4 agents)
│   ├── 06_Agents_Docs/       (1 agent)
│   ├── 07_Skills/            (41 skills)
│   └── 08_MCP/               (Context7)
├── 01_Agent_Teams_Lite/   (9 skills)
├── 02_Project_Manager/    (9 skills)
├── 03_Product_Manager/    (7 skills)
├── 04_Product_Design/     (11 skills)
├── 05_Vibe_Coding/        (21 skills)
├── 06_Testing/            (13 skills)
├── 07_DevOps/             (13 skills)
├── 08_Personal_Os/        (10 skills)
├── 09_Marketing/          (32 skills)
├── 11_Doc_Processing/     (3 skills)
├── 12_N8N/                (n8n)
├── 13_System_Master/      (nuevo - guides)
└── 10_Backup/             (~204 legacy)
```

**Total**: ~440 componentes (139 Gentleman + 131 CE + 100+ Backup)

- --

## 📝 REGLAS DE MEMORY (ENGRAM)

### Cuándo Guardar (MANDATORY)

Llamar `mem_save` INMEDIATAMENTE después de:

| Situación                             | Ejemplo                                       |
|---------------------------------------|-----------------------------------------------|
| Bug fix completado                    | "Fixed N+1 query in UserList"                 |
| Decisión arquitectónica               | "Chose Zustand over Redux"                    |
| Descubrimiento no obvio               | "FTS5 MATCH syntax is NOT LIKE"               |
| Cambio de configuración               | "JWT auth added to middleware"                |
| Patrón establecido                    | "Naming convention: PascalCase"               |
| Preferencia descubierta               | "User prefers morning sessions"               |

### Formato de mem_save

```markdown
* *What**: [concise description]
* *Why**: [reasoning or problem]
* *Where**: [files/paths affected]
* *Learned**: [gotchas, edge cases] (optional)
```

### Cuándo Buscar Memory

- User dice "remember", "acordate", "qué hicimos"
- Primera línea de mensaje menciona proyecto/feature
- User pide algo que podría haber sido hecho antes

- --

## 🪝 REGLAS DE HOOKS

### Sistema de Hooks (6 Activos)

| Hook                                    | Trigger                                     | Función                                                         | Status                 |
|-----------------------------------------|---------------------------------------------|-----------------------------------------------------------------|------------------------|
| `pre_tool_use.py`                       | Antes de cada tool                          | Batería < 15%, rm -rf protection, .env protection               | ✅                      |
| `csv-single-validator.py`               | Antes de CSV tools                          | Valida estructura CSV                                           | ✅                      |
| `post_tool_use.py`                      | Después de modificar archivos               | Backup, voz cada 2 archivos                                     | ✅                      |
| `stop.py`                               | Al cerrar sesión                            | "Sesión finalizada"                                             | ✅                      |
| `subagent_stop.py`                      | Al terminar sub-agente                      | "Subagente completado"                                          | ✅                      |
| `notification.py`                       | User envía mensaje                          | Alerta + voz                                                    | ✅                      |

### Hook de Naming (PENDIENTE)

```python
# Reglas a evaluar:

# 1. 2 dígitos: ^\d{2}_

# 2. PascalCase: ^[0-9]{2}[A-Z]

# 3. Secuencia PERFECTA: 01, 02, 03...

# 4. Primera letra MAYÚSCULA

```

- --

## 🔄 REGLAS DE SDD WORKFLOW

### Fases SDD

```
explore → propose → spec → design → tasks → apply → verify → archive
```

### Result Contract

Cada fase retorna:

```json
{
  "status": "success|partial|fail",
  "executive_summary": "1-2 sentences",
  "artifacts": ["artifact1", "artifact2"],
  "next_recommended": "next_phase",
  "risks": ["risk1", "risk2"]
}
```

- --

## 🚫 ANTI-PATTERNS (NUNCA HACER)

- ❌ Read source code to "understand" → Delegate
- ❌ Write/edit code inline → Delegate
- ❌ Write specs/proposals inline → Delegate
- ❌ Do "quick" analysis inline → Delegate
- ❌ Skip mem_save after decisions → ALWAYS save
- ❌ Move files without written plan → Write plan first
- ❌ Multiple parallel agents without coordination → Coordinate first

- --

## ✅ CHECKLIST DE SESIÓN

Antes de cerrar sesión, verificar:

- [ ] Pure Green: todo commiteado y funcional
- [ ] mem_session_summary llamado
- [ ] No cambios unstaged
- [ ] Hook de voz/notificación ejecutado
- [ ] Resumen de sesión reportado al usuario

- --

- --

## 🔗 ALIASES TERMINAL

### System Guardian (gr, gra, gr-agents)

| Alias                     | Type                   | Script                                              |
|---------------------------|------------------------|-----------------------------------------------------|
| `gr`                      | dry-run                | `79_System_Guardian.py --dry-run`                   |
| `gra`                     | --apply                | `79_System_Guardian.py --apply`                     |
| `gr-agents`               | --agents               | `79_System_Guardian.py --agents-only`               |

* *Location**: `~/gr`, `~/.bashrc` functions
* *Source**: `04_Engine/08_Scripts_Os/79_System_Guardian.py`

### CE Commands (ce-*)

| Alias                        | Description                               | Source Script                                               |
|------------------------------|-------------------------------------------|-------------------------------------------------------------|
| `ce-commit`                  | Safe commit with validation               | `04_Engine/08_Scripts_Os/52_Safe_Commit.py`                 |
| `ce-guard`                   | Commit guardrails                         | `04_Engine/08_Scripts_Os/52_Commit_Guard.py`                |
| `ce-audit`                   | Engineering audit                         | `04_Engine/08_Scripts_Os/42_Audit_Engineering.py`           |
| `ce-structure`               | Structure auditor                         | `04_Engine/08_Scripts_Os/53_Structure_Auditor.py`           |

* *Location**: `04_Engine/00_Config/aliases.sh`

- --

* Documento creado: 2026-03-21*
* Reglas actualizadas post-migración de skills SOTA*
* System Guardian v1.0 + Aliases agregados*
