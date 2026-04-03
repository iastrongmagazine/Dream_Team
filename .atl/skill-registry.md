# Skill Registry — Think Different PersonalOS v6.1

> ⚠️ **NOTA**: Este archivo es una referencia. El registry real está en:
> ```
> 02_Knowledge/04_Docs/99_ATL/skill-registry.md
> ```
>
> La fuente de verdad del OS está en `01_Core/`.

---

## Proyecto: Think_Different

**Última actualización:** 2026-04-03

### Convenciones del Proyecto

| Convención | Patrón |
|------------|--------|
| Directorios | `XX_Nombre/` (numerados) |
| Scripts | `##_Nombre_Script.py` |
| Reportes | `01_Report_Status.md` |
| Skills | `SKILL.md` en directorios de skills |
| Backup | `.agent/` refleja `01_Core/` |

### Estructura del OS (v6.1)

```
Think_Different/
├── 00_Winter_is_Coming/    # Goals, Backlog, AGENTS.md
├── 01_Core/               # Skills, Agents, MCPs, Rules (FUENTE)
│   ├── 01_Rules/          # 23 reglas (.mdc) — fuente de verdad
│   └── 03_Skills/         # 19 categorías de skills
├── 02_Knowledge/          # Documentación
│   └── 04_Docs/           # Docs del sistema
│       └── 99_ATL/        # SDD Registry real
├── 03_Tasks/              # Tareas activas
├── 04_Operations/         # Auto Improvement, Scripts
├── 06_Playground/         # Área de pruebas
├── 07_Projects/           # Proyectos activos
├── 08_Scripts_Os/         # HUBs (10 scripts) + config_paths.py
├── .agent/                # Backup estratégico + Hooks
├── .atl/                  # SDD Registry (este archivo) + openspec/
│   └── openspec/          # SDD config y cambios
└── .claude/rules/         # Reglas Claude Code → apuntan a 01_Core/01_Rules/
```

### SDD Configuration

| Item | Valor |
|------|-------|
| Modo | openspec |
| Strict TDD | ❌ disabled |
| Config | `.atl/openspec/config.yaml` |

### Available Skills (Global OpenCode)

| Categoría | Skill | Propósito |
|-----------|-------|-----------|
| **Agent Teams** | sdd-* (9 fases) | SDD workflow |
| **SDD Init** | sdd-init | Initialize SDD context |
| **SDD Explore** | sdd-explore | Explore ideas before committing |
| **SDD Propose** | sdd-propose | Create change proposals |
| **SDD Spec** | sdd-spec | Write specifications |
| **SDD Design** | sdd-design | Create technical designs |
| **SDD Tasks** | sdd-tasks | Break down into tasks |
| **SDD Apply** | sdd-apply | Implement tasks |
| **SDD Verify** | sdd-verify | Validate implementation |
| **SDD Archive** | sdd-archive | Archive completed changes |
| **Compound** | ce:* | Compound Engineering (brainstorm, plan, work, review, compound) |
| **Skill Creator** | Skill_Creator_Official | Crear skills v2.0 |
| **Data** | Silicon_Valley_Data_Analyst | Análisis de datos |
| **SEO** | SEO_SOTA_Master | SEO técnico |
| **Personal Life OS** | quick-capture, plan-my-day, daily-notes, recording-mode, returns-tracker | Productividad personal — Hillary |
| **Utilities** | playwright, pytest, react-19, nextjs-15, tailwind-4, zustand-5, etc. | Framework-specific tools |
| **Marketing** | social-content, paid-ads, seo-audit, programmatic-seo, referral-program | Marketing tech |
| **Review** | pr-review, github-pr, judgment-day, systematic-debugging, verification-before-completion | Code review workflows |

### Project Conventions (AGENTS.md)

- Root AGENTS.md → GGA pre-commit hook
- Core rules → 00_Winter_is_Coming/AGENTS.md
- Code review rules: No `var`, prefer interfaces, no `any`, functional components, named exports

### Skill Registry Sources

- User-level: `~/.config/opencode/skills/`
- Project-level: `.agent/02_Skills/`
- SDD Config: `.atl/openspec/config.yaml`

---

*Este archivo es generado por SDD Init. La fuente de verdad está en `02_Knowledge/04_Docs/99_ATL/`.*