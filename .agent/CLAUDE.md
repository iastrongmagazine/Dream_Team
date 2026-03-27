# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

---

# 🌐 Constitución Think Different

## 🔴 REGLA 00: Protocolo Génesis (OBLIGATORIO)

Al iniciar una nueva sesión, ejecutar esta secuencia antes de responder:

0. Leer `00_Core/AGENTS.md` — Fundación del Proyecto, todo Gobernado por este Archivo
1. Leer `.cursor/00_Rules/01_Context_Protocol.mdc` — Reglas de sesión
2. Leer `01_Brain/01_Context_Memory/` Y `01_Brain\07_Memory_Brain\` — Último contexto guardado
3. Ejecutar `mem_context(limit=10)` — Últimas 10 sesiones de Engram
4. Ejecutar `mem_session_summary()` — Recuperar estado si hubo compaction
5. Leer Completo cada carpeta de `.agent\` y Leer todo el Proyecto 00-07
6. **Reportar en el chat** un resumen del contexto cargado antes de actuar

---

## ⚖️ Las 12 Leyes Maestras (Legacy Core)

1. **Piensa Primero, Investiga Después**: Lee el código base ANTES de actuar.
2. **Explica Cada Paso**: Transparencia total.
3. **Simplicidad ante Todo**: Soluciones simples y legibles.
4. **Mantén la Documentación al Día**: Cambios significativos = docs actualizadas.
5. **Mantén Documentación Arquitectónica**: Arquitectura interna y externa al día.
6. **Cero Alucinaciones, Solo Hechos**: Basado en investigación real.
7. **Mantén el Inventario Actualizado**: Todo nuevo código/script/conocimiento al inventario.
8. **No Borrar Información sin Permiso**: Preservar la integridad.
9. **Respetar la Estructura Existente**: No modificar carpetas sin instrucción.
10. **Procesos en Formato Lista**: Presenta pasos como listas numeradas.
11. **Estructura de Carpetas**: Solo crear si es estrictamente necesario.
12. **Identificación de Repositorios**: Identificar el repo/directorio antes de operar.

---

## 🔴 REGLAS IMPERATIVAS (OBLIGATORIAS)

### REGLA 1: NO ACTUAR SIN PLAN APROBADO

- **PROHIBIDO** ejecutar cualquier acción sin un plan aprobado por el usuario
- **Siempre** presentar el plan en formato checklist antes de actuar
- **Siempre** esperar confirmación antes de proceder
- **Nunca** actuar por iniciativa propia - Esperar Aprobación

### REGLA 2: ENUMERACIÓN CORRECTA (SIEMPRE)

- **Carpetas:** `XX_Nombre_Carpeta/` (número 2 dígitos, Mayúscula Inicial, Guiones Bajos)
- **Archivos:** `XX_Nombre_Archivo.ext` 
- **ANTES** de crear/mover: Verificar secuencia Existente
- **NUNCA** dejar archivos sueltos sin numerar
- **NUNCA** crear duplicados de numeración

### REGLA 3: CORRECCIÓN DE ERRORES

- Si se detecta numeración incorrecta: DETENERSE
- Documentar qué está mal
- Presentar plan de corrección
- Esperar aprobación antes de ejecutar

---

## 🏗️ Arquitectura del Sistema (8 Dimensiones)

```
Think_Different_AI/
├── 00_Core/                    # ADN: Configuración central, metas y backlog
│   ├── AGENTS.md              # Instrucciones del agente (29KB)
│   ├── GOALS.md               # Metas, prioridades, estrategia Q1 2026
│   ├── BACKLOG.md             # Bandeja de entrada de tareas
│   ├── PROGRESS.md            # Dashboard (68.1% completado)
│   ├── 01_Architecture_Overview.md
│   ├── 02_Operational_Guide.md
│   ├── 03_Slash_Commands.md
│   ├── 04_Architecture_Map.md
│   ├── README.md
│   └── 00_Skills/             # Skills propias del agente
│       ├── Second_Brain/
│       └── security.md
├── 01_Brain/                   # Cerebro: Memoria, Conocimiento y Procesos
│   ├── 01_Context_Memory/       # Memoria a largo plazo (JSON + MD)
│   ├── 02_Knowledge_Brain/     # Base de conocimiento técnico
│   ├── 03_Process_Notes/       # Notas de sesiones (18 archivos)
│   ├── 04_Rules/              # Reglas del sistema (8 archivos)
│   ├── 05_Templates/          # Plantillas para tareas
│   ├── 06_Backup_Central/     # Backups centrales
│   ├── 07_Memory_Brain/       # Mapeos y análisis
│   ├── 08_Audit_Sota/        # Auditorías SOTA
│   └── 09_Momentum_Os/       # Proyectos de referencia
├── 02_Operations/              # Manos: Tasks, Evals, Progress
│   ├── 01_Active_Tasks/
│   ├── 02_Evals/
│   ├── 03_Analytics/
│   └── 04_Progress/
├── 03_Knowledge/               # Memoria: Research, Notes, Resources
│   ├── 01_Research_Knowledge/
│   ├── 02_Notes_Brain/
│   ├── 03_Resources_External/
│   ├── 04_Examples_Guide/
│   ├── 05_Marketing_Strategy/
│   ├── 06_Writing_Content/
│   ├── 07_Voice_Profiles/
│   ├── 08_Config_Files/
│   ├── 09_Archive_Recovery/
│   ├── 10_Repos_Gentleman/
│   ├── 11_Legacy_Resources/
│   ├── 12_Resources/
│   └── 13_Strategic_Plans/
├── 04_Engine/                  # Motor: Scripts automatización
│   ├── 00_Config/
│   ├── 01_Brain/
│   ├── 02_Analytics/
│   ├── 03_Templates/
│   ├── 04_Tools/
│   ├── 05_Tests/
│   ├── 06_Reports/
│   ├── 07_Installer/
│   ├── 08_Scripts_Os/
│   ├── 10_Scripts_Sync/
│   ├── 11_Brain_Engine/
│   ├── 12_Validation/
│   └── 13_Integrations/
├── 05_System/                  # Chasis: Core, Templates, Integrations
│   ├── 01_Core/
│   ├── 02_Templates/
│   ├── 03_Integrations/
│   ├── 04_Env/
│   ├── 05_Docs/
│   └── 06_Evals/
├── 06_Archive/                 # Baúl: Backups, Legacy, Docs
└── 07_Projects/                # Labs: Projects, Tests, Focus_Now_Lab
```

---

## 📁 Estructura .agent/ (Configuración AI)

```
.agent/
├── 00_Rules/                # Reglas del agente
├── 01_Agents/               # Agentes externos configurados
├── 02_Skills/               # Skills organizadas (305 total)
│   ├── 01_Agent_Teams_Lite/ # SDD Workflows (9 skills)
│   ├── 02_Project_Manager/  # Project management (9 skills)
│   ├── 03_Product_Manager/  # Product management (7 skills)
│   ├── 04_Product_Design/   # Design skills (11 skills)
│   ├── 05_Gentleman/        # Gentleman Programming (1 skill)
│   ├── 05_Vibe_Coding/      # Framework skills (21 skills)
│   ├── 06_Testing/          # Testing skills (13 skills)
│   ├── 07_DevOps/           # DevOps skills (12 skills)
│   ├── 08_Personal_Os/      # Personal OS skills (10 skills)
│   ├── 09_Marketing/        # Marketing skills (32 skills)
│   │   ├── 01_Marketing_Strategy/  # (15 sub-skills)
│   │   └── 02_Marketing_Tech/      # (10 sub-skills)
│   ├── 10_Backup/           # Backup/Legacy (177 skills)
│   └── 11_Doc_Processing/   # Document processing (3 skills)
├── 03_Workflows/            # Flujos de trabajo predefinidos
├── 04_Extensions/           # Hooks del sistema
│   └── hooks/               # Hooks activos (7 hooks)
│       ├── 01_Pre_Tool/     # PreToolUse: battery, security
│       ├── 02_Post_Tool/    # PostToolUse: backup, voice
│       ├── 03_Lifecycle/    # Stop, SubagentStop
│       └── 04_Sound/        # Notifications, sounds
├── 05_GGA/                  # Gentleman Guardian Angel (Code Review)
└── README.md
```

---

## 📁 Estructura .cursor/ (Configuración Cursor)

```
.cursor/
├── 00_Rules/            # Reglas de sesión
├── 01_Agents/
├── 02_Skills/           # Skills sincronizadas (mismo contenido que .agent/02_Skills/)
├── 03_Workflows/
├── 04_Extensions/       # Hooks sincronizados
├── 05_GGA/              # GGA sincronizado
├── 06_History/          # Historial de sesiones
│   ├── README.md
│   └── sessions/
│       └── voice_state.json
└── README.md
```

---

## 🔌 Extensiones y Hooks Activos

### 04_Extensions — Sistema de Hooks

**7 Hooks Activos:**

| Hook                         | Trigger                                   | Script                                | Función                                                     |
|------------------------------|-------------------------------------------|---------------------------------------|-------------------------------------------------------------|
| PreToolUse                   | Antes de cada tool                        | `pre_tool_use.py`                     | Batería < 15%, bloquea `rm -rf`, protege `.env`             |
| PreToolUse                   | Antes de cada tool                        | `csv-single-validator.py`             | Valida estructura CSV                                       |
| PostToolUse                  | Después de modificar archivos             | `post_tool_use.py`                    | Backup, voz cada 2 archivos                                 |
| Stop                         | Al cerrar sesión                          | `stop.py`                             | "Sesión finalizada"                                         |
| SubagentStop                 | Al terminar sub-agente                    | `subagent_stop.py`                    | "Subagente completado"                                      |
| UserPromptSubmit             | Usuario envía mensaje                     | `notification.py`                     | Alerta + voz                                                |
| TodoWrite                    | Al usar TodoWrite                         | `task-complete-sound.ps1`             | 🔊 Sonido de completado                                      |

### Configuración

```json
// .claude/settings.local.json
{
  "hooks": {
    "PreToolUse": [...],
    "PostToolUse": [...],
    "Stop": [...],
    "SubagentStop": [...],
    "UserPromptSubmit": [...],
    "TodoWrite": [...]
  }
}
```

---

## 🛡️ GGA (Gentleman Guardian Angel)

Code Review con IA integrado.

```bash
.agent/05_GGA/bin/gga run      # Revisar archivos staged
.agent/05_GGA/bin/gga install  # Instalar pre-commit hook
```

---

## 📚 Directrices del Sistema (Rules Registry)
- [Tech Defaults](01_Brain/04_Rules/00_Tech_Defaults.md)
- [Design Rules](01_Brain/04_Rules/01_Design_Rules.md)
- [Workflow](01_Brain/04_Rules/02_Workflow.md)
- [Code Style](01_Brain/04_Rules/03_Code_Style.md)
- [Testing](01_Brain/04_Rules/04_Testing.md)
- [Security](01_Brain/04_Rules/05_Security.md)
- [Auth UX/UI](01_Brain/04_Rules/06_Auth_UX_UI.md)

---

## 📚 Skills Disponibles

### Skills por Categoría (`.agent/02_Skills/`)

| Categoría                    | Skills               | Ubicación                          |
|------------------------------|----------------------|------------------------------------|
| Agent_Teams_Lite             | 9                    | `01_Agent_Teams_Lite/`             |
| Project_Manager              | 9                    | `02_Project_Manager/`              |
| Product_Manager              | 7                    | `03_Product_Manager/`              |
| Product_Design               | 11                   | `04_Product_Design/`               |
| Gentleman                    | 1                    | `05_Gentleman/`                    |
| Vibe_Coding                  | 21                   | `05_Vibe_Coding/`                  |
| Testing                      | 13                   | `06_Testing/`                      |
| DevOps                       | 12                   | `07_DevOps/`                       |
| Personal_Os                  | 10                   | `08_Personal_Os/`                  |
| Marketing                    | 32                   | `09_Marketing/`                    |
| Backup                       | 177                  | `10_Backup/`                       |
| Doc_Processing               | 3                    | `11_Doc_Processing/`               |
| **TOTAL**                    | **305**              |                                    |

### Gentleman Skills (`.agent/02_Skills/05_Gentleman/`)

| Categoría               | Count               | Ubicación                   |
|-------------------------|---------------------|-----------------------------|
| Plan                    | 8                   | `01_Plan/`                  | ← +1 (07_Double_Code_Review) |
| Work                    | 6                   | `02_Work/`                  |
| Review                  | 6                   | `03_Review/`                |
| Compound                | 15                  | `04_Compound/`              |
| Utilities               | 4                   | `05_Utilities/`             |

### 🔄 REGLA: Double Code Review (OBLIGATORIO)

**Después de TODO plan o sesión significativa, ejecutar Double Code Review:**

```bash
# Al terminar sesión o plan
"Hacé el double code review"
```

**Fases:**
1. **FASE 1**: Planning Status — checklist de planificación
2. **FASE 2**: 6 Sombreros — Information🔵, Emotions🔴, Benefits🟡, Risks🟢, Meta🟣, Process⚪
3. **FASE 3**: Verification — Execution, Completeness, Quality, Lessons Learned

Reports se guardan en: `01_Brain/07_Memory_Brain/00_Code_Reviews/`

### TASTE-SKILLS (PRIORIDAD ALTA PARA FRONTEND)

**Ubicación:** `.agent/02_Skills/04_Product_Design/`

| Skill                            | Uso                                         |
|----------------------------------|---------------------------------------------|
| **taste-skill**                  | Diseño desde cero - premium                 |
| **soft-skill**                   | Proyectos premium, invitaciones             |
| **minimalist-skill**             | Estilo Notion/Linear                        |
| **redesign-skill**               | Mejorar proyectos existentes                |
| **output-skill**                 | Evita código incompleto                     |

---

## ⚙️ Setup

```bash
# Instalar dependencias
pip install -r 05_System/04_Env/Requirements.txt

# Setup inicial del sistema
bash 01_Brain/07_Template/setup.sh
```

---

## 🔧 Scripts del Motor (`04_Engine/`)

```bash
# Workflows
python 04_Engine/08_Scripts_Os/14_Morning_Standup.py
python 04_Engine/08_Scripts_Os/09_Backlog_Triage.py
python 04_Engine/08_Scripts_Os/13_Validate_Stack.py
python 04_Engine/08_Scripts_Os/08_Ritual_Cierre.py

# Porteros (protección de commits)
python 04_Engine/08_Scripts_Os/52_Safe_Commit.py -m "feat: description"
python 04_Engine/08_Scripts_Os/53_Structure_Auditor.py
python 04_Engine/08_Scripts_Os/54_Commit_Guard.py -m "feat: description"
```

---

## ⚖️ Leyes Operativas (HULK AUDIT)
1. **Pensar 3 veces**: Antes de ejecutar, validar el efecto colateral.
2. **Validación Triple**: Todo script y skill debe pasar 3 pruebas (lógica, datos, output).
3. **Esencia**: Nunca romper la esencia del OS original.
4. **Cero alucinaciones**: Toda afirmación basada en lectura directa.

---

## 🎯 Spec-Driven Development (SDD)

Usa los comandos SDD: `/sdd:init`, `/sdd:explore`, `/sdd:new`, `/sdd:spec`, `/sdd:design`, `/sdd:tasks`, `/sdd:apply`, `/sdd:verify`, `/sdd:archive`.

---

## 📋 Estado Actual del Sistema (2026-03-25)

| Categoría                    | Skills               | Esencias               | Estado                                  |
|------------------------------|----------------------|------------------------|-----------------------------------------|
| Agent_Teams_Lite             | 9                    | ✅                      | No tocado (por instrucción)             |
| Project_Manager              | 9                    | ✅ Reales               | 100%                                    |
| Product_Manager              | 7                    | ✅ Reales               | 100%                                    |
| Product_Design               | 11                   | ✅ Reales               | 100%                                    |
| Vibe_Coding                  | 21                   | ✅ Reales               | 100%                                    |
| Testing                      | 13                   | ✅ Reales               | 100%                                    |
| DevOps                       | 12                   | ✅ Reales               | 100%                                    |
| Personal_Os                  | 10                   | ✅ Reales               | 100%                                    |
| Marketing                    | 32                   | ✅ Reales               | 100%                                    |
| Backup                       | 177                  | —                      | SKIPPED                                 |
| Doc_Processing               | 3                    | ✅ Reales               | 100%                                    |
| **TOTAL**                    | **128+**             | **99%**                | **Auditado**                            |

---

© 2026 PersonalOS
