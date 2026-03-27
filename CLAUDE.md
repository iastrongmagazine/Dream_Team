# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

---

# 🌐 Constitución Think Different

## 🔴 REGLA 00: Protocolo Génesis (OBLIGATORIO)

Al iniciar una nueva sesión, ejecutar esta secuencia antes de responder:

0. Leer `00_Winter_is_Coming/AGENTS.md` — TU MATRIX, la fuente de verdad completa
1. Leer `01_Core/01_Rules/01_Context_Protocol.mdc` — Reglas de sesión
2. Leer `04_Operations/01_Context_Memory/` y `04_Operations/04_Memory_Brain/` — Último contexto guardado
3. Ejecutar `mem_context(limit=10)` — Últimas 10 sesiones de Engram
4. Ejecutar `mem_session_summary()` — Recuperar estado si hubo compaction
5. Leer los recursos principales: `.agent/`, `01_Core/`, `02_Knowledge/`, `03_Tasks/`, `04_Operations/`
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

## 🏗️ Arquitectura del Sistema (Estructura Real)

```
Think_Different/
│
├── 📁 00_Winter_is_Coming/    # 🟣 TU MATRIX - Fuente de verdad completa
│   ├── AGENTS.md              # Instrucciones del agente (TU POWER)
│   ├── GOALS.md               # Metas, prioridades, estrategia
│   └── BACKLOG.md             # Bandeja de entrada de tareas
│
├── 📁 01_Core/                # Motor: Workflows, Rules, Agents, Skills
│   ├── 00_Workflows/         # 26 workflows tipo Marvel
│   ├── 01_Rules/             # 25 reglas activas
│   ├── 02_Agents/            # 12+ agentes especializados
│   ├── 03_Skills/            # Skills del sistema
│   └── templates/             # Templates
│
├── 📁 02_Knowledge/           # Base de conocimiento
│   └── ...                    # Research, notas, recursos
│
├── 📁 03_Tasks/               # Tareas con YAML frontmatter
│
├── 📁 04_Operations/          # 🧠 Memoria y contexto
│   ├── 01_Context_Memory/    # CTX files (sesiones)
│   ├── 02_Knowledge_Brain/   # Inventario del sistema
│   ├── 03_Process_Notes/     # Notas de sesiones
│   └── 04_Memory_Brain/      # Mapeos y análisis
│
├── 📁 .agent/                # 🔌 Centro de Poder AI
│   ├── 01_Agents/            # Agentes especializados
│   ├── 02_Skills/            # 160+ skills
│   ├── 03_Workflows/         # Workflows avanzados
│   ├── 04_Extensions/        # Hooks (7 activos)
│   └── 05_GGA/               # Guardian Angel Code Review
│
├── 📁 05_System/              # Chasis: Config, Env, MCP
│
├── 📁 06_Archive/             # Baúl: Backups, Legacy
│
├── 📁 07_Projects/            # Labs: Projects, Focus_Now_Lab
│
├── 📄 AGENTS.md               # Referencia simple (apunta a 00_Winter_is_Coming/)
├── 📄 CLAUDE.md                # Config para Claude Code
└── 📄 README.md               # Original PersonalOS
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

Las reglas están en `01_Core/01_Rules/`:
- [Context Protocol](01_Core/01_Rules/01_Context_Protocol.mdc)
- [Pilar Base](01_Core/01_Rules/02_Pilar_Base.mdc)
- [Pilar Motor](01_Core/01_Rules/03_Pilar_Motor.mdc)
- [Y más reglas en](01_Core/01_Rules/)

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

Reports se guardan en: `04_Operations/04_Memory_Brain/`

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
pip install -r 01_Core/Requirements.txt

# Verificar estructura
ls -la
```

---

## 🔧 Scripts del Motor

Scripts principales en `08_Scripts_Os/` y `01_Core/`:

```bash
# Scripts principales
python 08_Scripts_Os/01_Auditor_Hub.py
python 08_Scripts_Os/03_AIPM_Hub.py
python 08_Scripts_Os/04_Ritual_Hub.py

# En 01_Core/
python 01_Core/04_Tools/...

# Validadores
python 08_Scripts_Os/01_Auditor_Hub.py validate
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
