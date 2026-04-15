# PersonalOS v6.1 - Comandos y Workflows

## 📋 Comandos Disponibles

### Backlog Triage (pb / eb)
| Comando                                                            | Alias   | Descripción                              |
|--------------------------------------------------------------------|---------|------------------------------------------|
| `python 08_Scripts_Os/Ritual_Fixed/09_Backlog_Triage.py`           | **pb**  | Preview - ver tareas sin crear           |
| `python 08_Scripts_Os/Ritual_Fixed/09_Backlog_Triage.py --execute` | **eb**  | Execute - crear tareas y limpiar backlog |

### Morning Standup
| Comando                                                           | Alias   | Descripción   |
|-------------------------------------------------------------------|---------|---------------|
| `python 08_Scripts_Os/Ritual_Fixed/14_Morning_Standup.py`         |---------| Full standup  |
| `python 08_Scripts_Os/Ritual_Fixed/14_Morning_Standup.py --tasks` |---------| Solo tareas   |
| `python 08_Scripts_Os/Ritual_Fixed/14_Morning_Standup.py --goals` |---------| Solo goals    |

### Weekly Review
| Comando                                                          | Alias   | Descripción           |
|------------------------------------------------------------------|---------|-----------------------|
| `python 08_Scripts_Os/Ritual_Fixed/15_Weekly_Review.py`          |---------| Full review (4 pasos) |
| `python 08_Scripts_Os/Ritual_Fixed/15_Weekly_Review.py --quick`  |---------| Quick (5 min)         |
| `python 08_Scripts_Os/Ritual_Fixed/15_Weekly_Review.py --step 1` |---------| Completed             |
| `python 08_Scripts_Os/Ritual_Fixed/15_Weekly_Review.py --step 2` |---------| Goals                 |
| `python 08_Scripts_Os/Ritual_Fixed/15_Weekly_Review.py --step 3` |---------| Blockers              |
| `python 08_Scripts_Os/Ritual_Fixed/15_Weekly_Review.py --step 4` |---------| Plan next             |

### Content Generation (✍️)
| Comando                                                                               | Alias   | Descripción      |
|---------------------------------------------------------------------------------------|---------|------------------|
| `python 08_Scripts_Os/Ritual_Fixed/18_Generacion_Contenido.py`                        |---------| Modo interactivo |
| `python 08_Scripts_Os/Ritual_Fixed/18_Generacion_Contenido.py --blog --topic "X"`     |---------| Blog post        |
| `python 08_Scripts_Os/Ritual_Fixed/18_Generacion_Contenido.py --linkedin --topic "X"` |---------| LinkedIn         |
| `python 08_Scripts_Os/Ritual_Fixed/18_Generacion_Contenido.py --email --topic "X"`    |---------| Email            |
| `python 08_Scripts_Os/Ritual_Fixed/18_Generacion_Contenido.py --twitter --topic "X"`  |---------| Twitter thread   |

---

## 📖 Origen / Referencia

Basado en: `05_Archive/10_Repos_Gentleman/personal-os-main/examples/workflows/`

| Workflow Original     | Script Actual              |
|-----------------------|----------------------------|
| morning-standup.md    | 14_Morning_Standup.py      |
| weekly-review.md      | 15_Weekly_Review.py        |
| backlog-processing.md | 09_Backlog_Triage.py       |
| content-generation.md | 18_Generacion_Contenido.py | ✅ Actualizado |

---

## 🔧 Aliases (agregados a ~/.bashrc)

```bash
alias pb="python 08_Scripts_Os/Ritual_Fixed/09_Backlog_Triage.py"
alias eb="python 08_Scripts_Os/Ritual_Fixed/09_Backlog_Triage.py --execute"
```

---

## ✅ Estado de Documentación

| Repo Original         | Script Actual              | Estado        |
|-----------------------|----------------------------|---------------|
| morning-standup.md    | 14_Morning_Standup.py      | ✅ Actualizado |
| weekly-review.md      | 15_Weekly_Review.py        | ✅ Actualizado |
| backlog-processing.md | 09_Backlog_Triage.py       | ✅ Actualizado |
| content-generation.md | 18_Generacion_Contenido.py | ✅ Actualizado |

### Scripts en Ritual_Fixed/:
- 08_Ritual_Cierre.py
- 09_Backlog_Triage.py ✅
- 11_Sync_Notes.py
- 12_Update_Links.py
- 13_Validate_Stack.py
- 14_Morning_Standup.py ✅
- 15_Weekly_Review.py ✅
- 16_Clean_System.py
- 17_Ritual_Dominical.py
- 19_Generate_Progress.py
- 50_System_Health_Monitor.py
- 57_Repo_Sync_Auditor.py

---

## 🛠️ Herramientas del Tool Shed

### Tool Shed — Auto-detector de Contexto

| Comando                                           | Descripción                                       |
|---------------------------------------------------|---------------------------------------------------|
| `python 08_Scripts_Os/Tool_Fixed/62_Tool_Shed.py` | Detecta contexto actual y sugiere MCPs relevantes |

**Features:**
- Auto-detección de framework (React, Angular, Next.js, etc.)
- Sugerencia de skills según contexto
- Detección de archivos y patrones

### Skill Harmonizer — Validador de Skills

| Comando                                                  | Descripción                                          |
|----------------------------------------------------------|------------------------------------------------------|
| `python 08_Scripts_Os/Tool_Fixed/63_Skill_Harmonizer.py` | Valida paridad entre skills disponibles y ejecutados |

**Features:**
- 20/20 categorías pasando
- Verifica que cada skill tenga ejecutable + SKILL.md
- Reporte de coverage

### Notifier — Sistema de Notificaciones

| Comando                                          | Descripción                          |
|--------------------------------------------------|--------------------------------------|
| `python 08_Scripts_Os/Tool_Fixed/00_Notifier.py` | Reproduce sonido al completar tareas |

**Uso en scripts:**
```python
import sys
sys.path.insert(0, '08_Scripts_Os/Tool_Fixed')
from 00_Notifier import play_complete
play_complete()
```

---

## ✅ Estado de Scripts (Ritual_Fixed)

| Script                      | Estado        | Notas          |
|-----------------------------|---------------|----------------|
| 08_Ritual_Cierre.py         | ✅ Funcionando | sys.path fixed |
| 09_Backlog_Triage.py        | ✅ Funcionando | Alias: pb/eb   |
| 11_Sync_Notes.py            | ✅ Funcionando |----------------|
| 12_Update_Links.py          | ✅ Funcionando |----------------|
| 13_Validate_Stack.py        | ✅ Funcionando |----------------|
| 14_Morning_Standup.py       | ✅ Funcionando |----------------|
| 15_Weekly_Review.py         | ✅ Funcionando |----------------|
| 16_Clean_System.py          | ✅ Funcionando |----------------|
| 17_Ritual_Dominical.py      | ✅ Funcionando |----------------|
| 19_Generate_Progress.py     | ✅ Funcionando |----------------|
| 50_System_Health_Monitor.py | ✅ Funcionando |----------------|
| 57_Repo_Sync_Auditor.py     | ✅ Funcionando |----------------|

---

## 📚 Skills PersonalOS (01_Core/03_Skills/08_Personal_Os/)

| #   | Skill            | Script Asociado         |
|-----|------------------|-------------------------|
| 10  | Morning_Standup  | 14_Morning_Standup.py   |
| 11  | Weekly_Review    | 15_Weekly_Review.py     |
| 12  | Ritual_Cierre    | 08_Ritual_Cierre.py     |
| 13  | Sync_Notes       | 11_Sync_Notes.py        |
| 14  | Validate_Stack   | 13_Validate_Stack.py    |
| 15  | Update_Links     | 12_Update_Links.py      |
| 16  | Clean_System     | 16_Clean_System.py      |
| 17  | Ritual_Dominical | 17_Ritual_Dominical.py  |
| 18  | Repo_Sync        | 57_Repo_Sync_Auditor.py |

---

*Generado: 2026-03-29 | Actualizado con Tool Shed + Skills v6.1*
