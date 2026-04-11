# 08_Scripts_Os — Motor de Automatización

**Versión:** 6.1
**Última actualización:** 2026-04-10
**Estado:** ✅ Activo

---

## 📂 Estructura (Workspace)

```
Think_Different/
├── 00_Winter_is_Coming/    # Goals, Backlog, Memoria (ESTRATÉGICO)
├── 01_Core/               # Motor: Skills, Agents, MCPs, Workflows 💾
├── 02_Knowledge/          # Documentación, Research, Notas 📚
├── 03_Tasks/             # Tareas activas (YAML frontmatter)
├── 04_Operations/        # Memoria y Procesos
├── 05_Archive/           # Legacy archivado 📦
├── 06_Playground/       # Pruebas y experimentos
├── 07_Projects/         # Proyectos activos
├── 08_Scripts_Os/       # Scripts operativos ✅
└── Maerks/             # Tests legacy, planes
```

---

## 📂 Estructura 08_Scripts_Os

```
08_Scripts_Os/
├── README.md                    # Este archivo
├── SCRIPTS_INDEX.md             # Índice de scripts
├── config_paths.py              # Rutas centralizadas (actualizado)
├── qmd.sh                      # Script QMD
├── testsprite_failover.sh      # Failover para TestSprite
├── tarea_lista.bat             # Sonido de notificación Windows
├── 00_Sound_Engine.py          # Motor de sonido general
├── 01_Auditor_Hub.py           # Auditor principal
├── 02_Git_Hub.py              # Operaciones Git
├── 03_AIPM_Hub.py             # AIPM logging
├── 04_Ritual_Hub.py           # Orquestador de rituales
├── 05_Validator_Hub.py         # Validador de reglas
├── 06_Tool_Hub.py             # Herramientas varias
├── 07_Integration_Hub.py       # Integraciones MCP
├── 08_Workflow_Hub.py         # Workflows SOTA
├── 09_Data_Hub.py             # Datos y sincronización
├── 10_General_Hub.py          # Utilidades generales
├── 11_Auto_Learn_Hub.py       # Hub de auto-aprendizaje
├── 12_Context_Usage_Bar.py    # Barra de uso de contexto
├── 13_Beautify_Tables.py      # Script de embellecimiento Markdown
├── 14_Beauty_Doc.py           # Evaluador visual de documentos
├── 11_Anthropic_Harness/     # Anthropic patterns
├── 01_Ritual/                 # Rituales (12 scripts)
├── 02_Tool/                   # Herramientas (Tool Shed, Skill Harmonizer, Notifier)
├── 03_Validator/              # Validadores
├── 04_Workflow/               # Workflows
├── 05_AIPM/                   # AIPM scripts
├── 06_Auditor/                # Auditor scripts
├── 07_Data/                   # Data scripts
├── 08_General/                # General utilities
├── 09_Integration/            # Integration scripts
├── 10_Legacy/                 # Scripts legacy (referencia)
└── 12_Audits/                 # Archivos de auditorías
```

---

## 🎯 Propósito

El **motor de automatización** del PersonalOS - scripts Python para operaciones, auditorías, workflows y rituales diarios.

---

## 📊 Estadísticas

| Área                        | Cantidad   | Estado        |
|-----------------------------|------------|---------------|
| Scripts en 01-09_Carpetas   | 26         | ✅ Funcionando |
| Scripts en 10_Legacy        | 60+        | ⚠️ Legacy     |
| HUBs principales (00-14)    | 15         | ✅ Activos     |

---

## 🔧 Scripts Principales (01_Ritual)

| Script                    | Función            | Skill Asociada     |
|---------------------------|--------------------|--------------------|
| `09_Backlog_Triage.py`    | Procesa backlog    | backlog-processing |
| `14_Morning_Standup.py`   | Daily standup      | morning-standup    |
| `15_Weekly_Review.py`     | Revisión semanal   | weekly-review      |
| `08_Ritual_Cierre.py`     | Cierre de sesión   | ritual-cierre      |
| `11_Sync_Notes.py`        | Sincroniza notas   | sync-notes         |
| `13_Validate_Stack.py`    | Valida stack       | validate-stack     |
| `19_Generate_Progress.py` | Dashboard progreso |--------------------|

---

## 🚀 Uso

```bash
# Ejecutar Morning Standup
python 08_Scripts_Os/01_Ritual/14_Morning_Standup.py

# Ejecutar Weekly Review
python 08_Scripts_Os/01_Ritual/15_Weekly_Review.py

# Ejecutar Ritual de Cierre
python 08_Scripts_Os/01_Ritual/08_Ritual_Cierre.py

# Ver índice completo
cat 08_Scripts_Os/SCRIPTS_INDEX.md
```

---

## 📚 Recursos

- [SCRIPTS_INDEX.md](./SCRIPTS_INDEX.md) — Índice completo de scripts
- [10_Legacy](./10_Legacy/) — Scripts legacy (referencia)
- [01_Core/03_Skills/08_Personal_Os/](../01_Core/03_Skills/08_Personal_Os/) — Skills asociadas

---

## ✅ Notas Importantes (2026-04-01)

- Scripts organizados en carpetas numeradas `01_Ritual` a `09_Integration`
- Cada script tiene una skill asociada en `08_Personal_Os`
- Los scripts legacy en `10_Legacy/` pueden tener rutas obsoletas

---

*Think Different PersonalOS v6.1 — Motor operativo*
