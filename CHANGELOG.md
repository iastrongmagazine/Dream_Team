# Changelog

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
