# Changelog

## 1.5.0 - 2026-04-01

### Added
- **`00_Plan_Hillary_Integration.md`**: Plan de integración Hillary Life OS → PersonalOS v6.1 (5 skills: Quick Capture, Plan My Day, Daily Notes, Recording Mode, Returns Tracker)
- **`02_Plan_Restauracion_Opencode.md`**: Plan de restauración quirúrgica de `opencode.json` (Pure Green Recovery)
- **`03_Task_Restauracion_Opencode.md`**: Checklist de ejecución para restauración de OpenCode

### Fixed
- **`01_Core/05_Mcp/01_Claude_Code/mcp.json`**: TestSprite migrado a path absoluto + env var `TESTSPRITE_PRIMARY`; notebooklm actualizado a `npx -y notebooklm-mcp@latest`
- **`01_Core/05_Mcp/02_OpenCode/opencode.json`**: Migración de `npx.cmd` → `npx` en todos los servidores MCP (cross-platform); eliminada clave inválida `plugins`; restaurados servidores exa, Notion, firecrawl, task-master-ai, supadata, zai-mcp-server, excalidraw
- **`README.md`**: Corregidos paths obsoletos `Validator_Fixed/` → `03_Validator/` y `Tool_Fixed/` → `02_Tool/`

### Removed
- **`PLAN_HILLARY_INTEGRATION.md`**: Renombrado a `00_Plan_Hillary_Integration.md` siguiendo convención de numeración canónica

---

## 1.4.0 - 2026-04-01

### Refactor — Nomenclatura canónica y saneamiento total
- **`08_Scripts_Os/`**: Renombradas 10 carpetas `*_Fixed` a nomenclatura `XX_Nombre`:
  - `Ritual_Fixed` → `01_Ritual`
  - `Tool_Fixed` → `02_Tool`
  - `Validator_Fixed` → `03_Validator`
  - `Workflow_Fixed` → `04_Workflow`
  - `AIPM_Fixed` → `05_AIPM`
  - `Auditor_Fixed` → `06_Auditor`
  - `Data_Fixed` → `07_Data`
  - `General_Fixed` → `08_General`
  - `Integration_Fixed` → `09_Integration`
  - `Legacy_Backup` → `10_Legacy`
- **`01_Core/07_Hooks/`**: `05_Post_Hulk_Compound` → `06_Post_Hulk_Compound` (prefijo duplicado resuelto)
- **`01_Core/09_Server/00_Env/config_paths.py`**: DIMENSIONS actualizadas a v6.1 (9 dimensiones correctas), ENGINE_DIR corregido a `08_Scripts_Os`
- **`01_Core/Requirements.txt`**: Unificado con versiones actuales (`mcp>=1.26.0`, `anthropic>=0.84.0`, `python-dotenv>=1.0.0`, `colorama>=0.4.6`)
- **`01_Core/09_Server/00_Env/Requirements.txt`**: Sincronizado con fuente de verdad (agregado `colorama>=0.4.6`)
- **`01_Core/09_Server/00_Config_Aliases/aliases.sh`**: Agregados aliases para hubs 11-14 (`auto-learn`, `context-bar`, `beautify`, `beauty-doc`), rutas absolutas via `$PERSONAL_OS_ROOT`, auto-detección de raíz
- **`.claude/01_Commands/genesis.md`**: Corregido script invocado (`04_Ritual_Hub.py --mode genesis` en vez de `08_Ritual_Cierre.py`)
- **`01_Core/07_Hooks/06_Post_Hulk_Compound/post_hulk_compound.py`**: Corregido `project_root` (era `_ext_root.parent.parent` → ahora `_ext_root.parent`) y ruta a `56_Organize_Solutions.py`
- **Documentación**: Actualizadas referencias en `CLAUDE.md`, `AGENTS.md`, `08_Scripts_Os/README.md`, `08_Scripts_Os/SCRIPTS_INDEX.md`

---

## 1.3.0 - 2026-04-01

### Fixed
- **`.claude/settings.local.json`**: Eliminado sonido en `PostToolUse` (disparaba en cada tool call — ruidoso e inútil)
- **`.claude/settings.local.json`**: `UserPromptSubmit` usaba `--notify` sin argumento (error de runtime) → corregido a `--beep`
- **`CLAUDE.md`**: Git Estado actualizado de MODIFIED → CLEAN
- **`CLAUDE.md`**: Fecha de última actualización corregida a 2026-04-01

### Sound System — Comportamiento final
- `TodoWrite` → `notification.py --task-complete` ✅ (suena cuando el agente actualiza tareas)
- `Stop` → `stop.py` ✅ (suena + System Guardian al cerrar sesión)
- `UserPromptSubmit` → `notification.py --beep` ✅ (beep simple al recibir mensaje)
- `PostToolUse` → solo `post_tool_use.py` (sin sonido — era demasiado ruidoso)

---

## 1.2.0 - 2026-03-31

### Fixed
- **config_paths.py**: 3 rutas rotas corregidas (`PLAYGROUND_DIR`, `KNOWLEDGE_RESOURCES_DIR`, `KNOWLEDGE_EXAMPLES_DIR`)
- **50_System_Health_Monitor.py**: `sys.path` apuntaba a ROOT en vez de `08_Scripts_Os/`; master files check 3 niveles → 2 niveles
- **53_Structure_Auditor.py**: `ENGINE_DIR` duplicado (`08_Scripts_Os/08_Scripts_Os`); DIMENSIONS actualizadas a v6.1 (9 dimensiones)
- **08_Ritual_Cierre.py**: `sys.path` apuntaba a PROJECT_ROOT en vez de `08_Scripts_Os/`
- **14_Morning_Standup.py**: `sys.path` apuntaba a `Legacy_Backup/` inexistente
- **02_Git_Hub.py**: ARMOR LAYER movido antes del import de `config_paths`
- **`.claude/rules/*.md`**: Todas las rutas apuntaban a `01_Core/04_Rules/` (inexistente) → corregido a `01_Core/01_Rules/` con nombres `.mdc` correctos
- **`.claude/settings.local.json`**: Hooks actualizados para usar `01_Core/07_Hooks/04_Sound/notification.py` (script correcto con sonido real)
- **post_tool_use.py**: Beep silenciado → ahora loguea éxito o error

### Added
- **Formato de reporte 15%**: CLAUDE.md y .agent/CLAUDE.md actualizados con 5 campos obligatorios (qué hice, qué estoy haciendo, próximo paso, pendientes, tiempo estimado)
- **OpenCode sound plugin**: `sound-on-complete.ts` corregido para Windows (PowerShell correcto)
- **~/.config/opencode/AGENTS.md**: Reporte 15% configurado igual que Claude Code
- **`.atl/openspec/`**: Movido desde raíz del proyecto a `.atl/openspec/`

### Verified
- Auditor Hub: `=== ESTATUS: SALUDABLE ===` (todas las dimensiones OK)
- Structure Auditor: 9 dimensiones v6.1 validadas
- `.claude/rules` carga reglas reales desde `01_Core/01_Rules/`

---

## 1.1.0 - 2026-03-29

### Added
- **PersonalOS v6.1** - Workspace reorganization
- **Anthropic SOTA Practices** (2026): CLAUDE.md, Plan then Execute, Custom Tools, Git Workflows, Specific Prompting, Context Management, Headless Mode + Hooks
- **Anthropic 9 Skill Categories**: Library/API, Product Verification, Data Fetching, Business Process, Code Scaffolding, Code Quality, CI/CD, Runbooks, Infrastructure Ops
- **Sound Notifications**: OpenCode notify plugin (kdco/notify) + configured hooks for Claude Code (.claude/settings.local.json)
- **22 Rules Updated** with XML format from 02_Pilar_Base.mdc

### Fixed
- Obsolete paths: 01_Brain → 04_Operations, 00_Core → 00_Winter_is_Coming
- Workspace structure documentation (00-08 + Maerks)

### Verified
- Tool versions: Python 3.14.2, uv 0.10.4, Git 2.53.0, Node.js v24.12.0, npm 11.6.2, OpenCode 1.3.6, Engram 1.10.10

---

## 1.0.0 - 2026-03-27

- Initial release
- Skill: personal-os - Sistema completo de productividad
- Skill: sdd-workflow - Metodología Spec-Driven Development
- Skill: system-guardian - Validación automática de proyectos
