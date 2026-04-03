# Skill Registry — Think Different PersonalOS v6.1

> ⚠️ **NOTA**: Este archivo es una referencia. El registry real está en:
> ```
> 02_Knowledge/04_Docs/99_ATL/skill-registry.md
> ```
>
> La fuente de verdad del OS está en `01_Core/`.

---

## Proyecto: Think_Different

**Última actualización:** 2026-03-31

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
└── .claude/rules/         # Reglas Claude Code → apuntan a 01_Core/01_Rules/
```

### Skills Principales

| Categoría | Skill | Propósito |
|-----------|-------|-----------|
| **Agent Teams** | sdd-* (9 fases) | SDD workflow |
| **Compound** | ce:* | Compound Engineering |
| **Skill Creator** | Skill_Creator_Official | Crear skills v2.0 |
| **Data** | Silicon_Valley_Data_Analyst | Análisis de datos |
| **SEO** | SEO_SOTA_Master | SEO técnico |
| **Personal Life OS** | quick-capture, plan-my-day, daily-notes, recording-mode, returns-tracker | Productividad personal — Hillary |

### HUBs Disponibles (08_Scripts_Os/)

| Hub | Propósito |
|-----|-----------|
| 01_Auditor | Validación del sistema |
| 02_Git | Operaciones Git |
| 03_AIPM | Monitoreo de performance IA |
| 04_Ritual | Rituales de sesión |
| 05_Validator | Validación de código |
| 06_Tool | Gestión de herramientas |
| 07_Integration | Integraciones MCP |
| 08_Workflow | Automatización de workflows |
| 09_Data | Procesamiento de datos |
| 10_General | Utilidades generales |

### Validators (04_Operations/)

| Tool | Ubicación |
|------|-----------|
| skill_validator.py | `08_Scripts_Os/Validator_Fixed/` |
| skill_security_scan.py | `08_Scripts_Os/Validator_Fixed/` |

---

*Este archivo es generado por SDD Init. La fuente de verdad está en `02_Knowledge/04_Docs/99_ATL/`.*
