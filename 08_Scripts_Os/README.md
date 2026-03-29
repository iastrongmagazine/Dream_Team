# 08_Scripts_Os — Motor de Automatización

**Versión:** 6.1
**Última actualización:** 2026-03-29
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
├── 11_Anthropic_Harness/     # Anthropic patterns
├── Ritual_Fixed/              # Rituales funcionando (12 scripts)
├── Tool_Fixed/                # Herramientas (6)
├── Validator_Fixed/           # Validadores funcionando
├── Workflow_Fixed/            # Workflows funcionando
└── Legacy_Backup/             # Scripts legacy (referencia)
```

---

## 🎯 Propósito

El **motor de automatización** del PersonalOS - scripts Python para operaciones, auditorías, workflows y rituales diarios.

---

## 📊 Estadísticas

| Área | Cantidad | Estado |
|------|----------|--------|
| Scripts en _Fixed | 26 | ✅ Funcionando |
| Scripts en Legacy_Backup | 60+ | ⚠️ Legacy |
| HUBs principales | 10 | ✅ Activos |

---

## 🔧 Scripts Principales (Ritual_Fixed)

| Script | Función | Skill Asociada |
|--------|---------|----------------|
| `09_Backlog_Triage.py` | Procesa backlog | backlog-processing |
| `14_Morning_Standup.py` | Daily standup | morning-standup |
| `15_Weekly_Review.py` | Revisión semanal | weekly-review |
| `08_Ritual_Cierre.py` | Cierre de sesión | ritual-cierre |
| `11_Sync_Notes.py` | Sincroniza notas | sync-notes |
| `13_Validate_Stack.py` | Valida stack | validate-stack |
| `19_Generate_Progress.py` | Dashboard progreso | - |

---

## 🚀 Uso

```bash
# Ejecutar Morning Standup
python 08_Scripts_Os/Ritual_Fixed/14_Morning_Standup.py

# Ejecutar Weekly Review
python 08_Scripts_Os/Ritual_Fixed/15_Weekly_Review.py

# Ejecutar Ritual de Cierre
python 08_Scripts_Os/Ritual_Fixed/08_Ritual_Cierre.py

# Ver índice completo
cat 08_Scripts_Os/SCRIPTS_INDEX.md
```

---

## 📚 Recursos

- [SCRIPTS_INDEX.md](./SCRIPTS_INDEX.md) — Índice completo de scripts
- [Legacy_Backup](./Legacy_Backup/) — Scripts legacy (referencia)
- [01_Core/03_Skills/08_Personal_Os/](../01_Core/03_Skills/08_Personal_Os/) — Skills asociadas

---

## ✅ Notas Importantes (2026-03-29)

- Scripts en carpetas `_Fixed` están funcionando y probados
- Cada script tiene una skill asociada en `08_Personal_Os`
- Los scripts legacy en Legacy_Backup pueden tener rutas obsoletas

---

*Think Different PersonalOS v6.1 — Motor operativo*
