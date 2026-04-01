# Scripts Index — PersonalOS Think Different v6.1

> **Total Scripts:** 89+ (HUBs + Legacy)
> **Last Updated:** 2026-03-29
> **Validation:** Auditorías PASANDO - Sistema OPERATIVO

---

## 📊 Estado del Sistema (Post-Auditoría)

| Auditoría      | Estado   | Notas                      |
|----------------|----------|----------------------------|
| **Estructura** | ✅ PASS   | 8 carpetas (00-08) válidas |
| **Links**      | ✅ PASS   | Links verificados          |
| **Skills**     | ✅ FIXED  | 46 elementos renombrados   |
| **Health**     | ✅ PASS   | Estructura OK              |
| **.bashrc**    | ✅ FIXED  | Alias corregidos           |

---

## 🏗️ Orchestration HUBs (08_Scripts_Os/)

| #   | Script               | Purpose                   | Status   |
|-----|----------------------|---------------------------|----------|
| 01  | `Auditor_Hub.py`     | Orquestador de Auditorías | ✅ ACTIVO |
| 02  | `Git_Hub.py`         | Orquestador de Git/Repos  | ✅ ACTIVO |
| 03  | `AIPM_Hub.py`        | Métricas AIPM             | ✅ ACTIVO |
| 04  | `Ritual_Hub.py`      | Rituales (Start/End)      | ✅ ACTIVO |
| 05  | `Validator_Hub.py`   | Validaciones              | ✅ ACTIVO |
| 06  | `Tool_Hub.py`        | Herramientas              | ✅ ACTIVO |
| 07  | `Integration_Hub.py` | Integraciones MCP         | ✅ ACTIVO |
| 08  | `Workflow_Hub.py`    | Workflows SOTA            | ✅ ACTIVO |
| 09  | `Data_Hub.py`        | Datos/Sync                | ✅ ACTIVO |
| 10  | `General_Hub.py`     | Utilidades                | ✅ ACTIVO |
| 11  | `Auto_Learn_Hub.py`  | Motor de automejora       | ✅ ACTIVO |
| 12  | `Context_Usage_Bar.py` | Barra de uso de contexto | ✅ ACTIVO |
| 13  | `Beautify_Tables.py` | Formateo de tablas        | ✅ ACTIVO |
| 14  | `Beauty_Doc.py`      | Documentos embellecidos   | ✅ ACTIVO |

### Usage

```bash
# Desde cualquier ubicación (aliases en .bashrc)
gr              # Auditor_Hub.py - Dry run
audit           # Auditor_Hub.py
git-hub         # Git_Hub.py
aipm            # AIPM_Hub.py
ritual          # Ritual_Hub.py
validate        # Validator_Hub.py

# O directamente
cd Think_Different
python 08_Scripts_Os/01_Auditor_Hub.py estructura
python 08_Scripts_Os/01_Auditor_Hub.py skills
python 08_Scripts_Os/01_Auditor_Hub.py health
python 08_Scripts_Os/01_Auditor_Hub.py profundo
```

---

## 📁 Estructura v6.1 (Confirmed)

```
Think_Different/
├── 00_Winter_is_Coming/     ✅ Goals, Backlog, AGENTS.md
├── 01_Core/                 ✅ Skills (19 cats), Agents, MCP, Server
│   └── 03_Skills/          # Skills numeradas (00-17)
├── 02_Knowledge/            ✅ Base de conocimiento
├── 03_Tasks/                ✅ 17+ tareas activas
├── 04_Operations/           ✅ Memoria, Brain, Notas
├── 05_Archive/              ✅ Repos, Legacy
├── 07_Projects/             ✅ Proyectos
└── 08_Scripts_Os/           ✅ 10 HUBs + Legacy_Backup
```

---

## 🎯 Skills (01_Core/03_Skills/)

| #   | Categoría                        | Skills             |
|-----|----------------------------------|--------------------|
| 00  | `00_Compound_Engineering`        | 8 sub-skills       |
| 00  | `00_Personal_Os_Stack`           | Core OS            |
| 00  | `00_Skill_Auditor`               | Auditor            |
| 01  | `01_Agent_Teams_Lite`            | SDD Workflows      |
| 02  | `02_Project_Manager`             | 8 workflows        |
| 03  | `03_Product_Manager`             | 7 workflows        |
| 04  | `04_Product_Design`              | 11 workflows       |
| 05  | `05_Vibe_Coding`                 | 17 frameworks      |
| 06  | `06_Testing`                     | 17 workflows       |
| 07  | `07_DevOps`                      | 12 workflows       |
| 08  | `08_Personal_Os`                 | 9 workflows        |
| 09  | `09_Marketing`                   | 10 workflows       |
| 10  | `10_Backup`                      | 5 sub-categorías   |
| 11  | `11_Doc_Processing`              | 3 workflows        |
| 12  | `12_N8N`                         | 7 workflows        |
| 13  | `13_System_Master`               | Master skill       |
| 14  | `14_Anthropic_Harness`           | 8 evaluators       |
| 15  | `15_Skill_Creator_Oficial`       | Skill Creator v2.0 |
| 16  | `16_Silicon_Valley_Data_Analyst` | Data Analyst       |
| 17  | `17_SEO_SOTA_Master`             | SEO Master         |

**Total: 19 categorías de skills**

---

## 🔧 Legacy Scripts (Legacy_Backup/)

Scripts legacy en `08_Scripts_Os/Legacy_Backup/` — referensiados por números:

| #     | Script      | Purpose                        |
|-------|-------------|--------------------------------|
| 00-90 | +80 scripts | Workflows, AIPM, Quality, etc. |

> ⚠️ Algunos scripts legacy pueden tener rutas obsoletas (`.agent/02_Skills`). Auditoría en progreso.

---

## ✅ Comandos del Sistema

| Comando       | Función                   |
|---------------|---------------------------|
| `gr`          | System Guardian (dry-run) |
| `gr --apply`  | Aplicar fixes             |
| `gr --agents` | Agentes de revisión       |
| `/sdd:*`      | SDD Workflow              |
| `/ce:*`       | Compound Engineering      |
| `engram`      | Memoria persistente       |

---

## 📝 Notas Importantes

1. **Rutas v6.1**: Skills ahora en `01_Core/03_Skills/` (antes `.agent/02_Skills/`)
2. **.bashrc**: Alias configurados con rutas absolutas
3. **34_Skill_Auditor.py**: Corregido para auto-detectar categorías

---

## 🔗 Scripts → Skills Mapping (2026-03-29)

Scripts en 01_Ritual con sus skills asociadas:

| Script                        | Skill              | Estado   |
|-------------------------------|--------------------|----------|
| `09_Backlog_Triage.py`        | backlog-processing | ✅ Existe |
| `14_Morning_Standup.py`       | morning-standup    | ✅ Creado |
| `15_Weekly_Review.py`         | weekly-review      | ✅ Creado |
| `08_Ritual_Cierre.py`         | ritual-cierre      | ✅ Creado |
| `11_Sync_Notes.py`            | sync-notes         | ✅ Creado |
| `13_Validate_Stack.py`        | validate-stack     | ✅ Creado |
| `12_Update_Links.py`          | update-links       | ✅ Creado |
| `16_Clean_System.py`          | clean-system       | ✅ Creado |
| `17_Ritual_Dominical.py`      | ritual-dominical   | ✅ Creado |
| `57_Repo_Sync_Auditor.py`     | repo-sync          | ✅ Creado |
| `50_System_Health_Monitor.py` | system-guardian    | ✅ Existe |

---

## 📁 Scripts por Carpeta (01_Ritual)

| Script                        | Función              |
|-------------------------------|----------------------|
| `08_Ritual_Cierre.py`         | Cierre de sesión     |
| `09_Backlog_Triage.py`        | Procesa backlog      |
| `11_Sync_Notes.py`            | Sincroniza notas     |
| `12_Update_Links.py`          | Actualiza enlaces    |
| `13_Validate_Stack.py`        | Valida stack tech    |
| `14_Morning_Standup.py`       | Daily standup        |
| `15_Weekly_Review.py`         | Weekly review        |
| `16_Clean_System.py`          | Limpia sistema       |
| `17_Ritual_Dominical.py`      | Ritual dominical     |
| `18_Generacion_Contenido.py`  | Generación contenido |
| `19_Generate_Progress.py`     | Dashboard progreso   |
| `50_System_Health_Monitor.py` | Health monitor       |
| `57_Repo_Sync_Auditor.py`     | Repo sync            |

---

*Actualizado: 2026-04-01 — Carpetas renombradas a nomenclatura canónica (XX_Nombre)*
