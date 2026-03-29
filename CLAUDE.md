# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working in this repository.

---

# Constitucion Think Different

## REGLA 00: Protocolo Genesis (OBLIGATORIO)

**REGLA ORO: SIN CONTEXTO NO HAY CHAT**

- **PROHIBIDO** chatear sin cargar contexto primero
- Antes de responder: ejecutar `engram_mem_context(limit=10)`
- Si hay session_summary previo, cargarlo

**IDIOMA:**
- **SIEMPRE** Espanol en chat (es mi idioma natal)
- Usar espanol rioplatense: laburo, ponete las pilas, boludo, quilombo, banca, dale, etc.

**REPORTE OBLIGATORIO (cada tarea = reporte):**
- Porcentaje de avance completado
- Que tarea termine
- En que tarea estoy
- Cual es la proxima tarea

---

Al iniciar una nueva sesion, ejecutar esta secuencia antes de responder:

0. Leer `00_Winter_is_Coming/AGENTS.md` y SIEMPRE Comunicarte en Espanol en Chat
1. Leer `00_Winter_is_Coming/GOALS.md` — Metas y prioridades
2. Leer `00_Winter_is_Coming/BACKLOG.md` — Bandeja de entrada
3. Ejecutar `engram_mem_context(limit=10)` — Ultimas 10 sesiones de Engram
4. Ejecutar `engram_mem_session_summary()` — Recuperar estado si hubo compaction
5. Leer los recursos principales: `01_Core/`, `02_Knowledge/`, `04_Operations/`
6. **Reportar en el chat** un resumen del contexto cargado antes de actuar

---

## Las 12 Leyes Maestras

1. **Piensa Primero, Investiga Despues**: Lee el codigo base ANTES de actuar.
2. **Explica Cada Paso**: Transparencia total.
3. **Simplicidad ante Todo**: Soluciones simples y legibles.
4. **Mantén la Documentacion al Dia**: Cambios significativos = docs actualizadas.
5. **Mantén Documentacion Arquitectonica**: Arquitectura interna y externa al dia.
6. **Cero Alucinaciones, Solo Hechos**: Basado en investigacion real.
7. **Mantén el Inventario Actualizado**: Todo nuevo codigo/script/conocimiento al inventario.
8. **No Borrar Informacion sin Permiso**: Preservar la integridad.
9. **Respetar la Estructura Existente**: No modificar carpetas sin instruccion.
10. **Procesos en Formato Lista**: Presenta pasos como listas numeradas.
11. **Estructura de Carpetas**: Solo crear si es estrictamente necesario.
12. **Identificacion de Repositorios**: Identificar el repo/directorio antes de operar.

---

## REGLAS IMPERATIVAS (OBLIGATORIAS)

### REGLA 1: NO ACTUAR SIN PLAN APROBADO

- **PROHIBIDO** ejecutar cualquier accion sin un plan aprobado por el usuario
- **Siempre** presentar el plan en formato checklist antes de actuar
- **Siempre** esperar confirmacion antes de proceder
- **Nunca** actuar por iniciativa propia - Esperar Aprobacion

### REGLA 2: ENUMERACION CORRECTA (SIEMPRE)

- **Carpetas:** `XX_Nombre_Carpeta/` (numero 2 digitos, Mayuscula Inicial, Guiones Bajos)
- **Archivos:** `XX_Nombre_Archivo.ext`
- **ANTES** de crear/mover: Verificar secuencia Existente
- **NUNCA** dejar archivos sueltos sin numerar
- **NUNCA** crear duplicados de numeracion

### REGLA 3: CORRECCION DE ERRORES

- Si se detecta numeracion incorrecta: DETENERSE
- Documentar que esta mal
- Presentar plan de correccion
- Esperar aprobacion antes de ejecutar

---

# Arquitectura del Sistema (Estructura Real v6.1)

```
Think_Different/
|
|--- 00_Winter_is_Coming/     # MATRIX: Goals, Backlog, AGENTS.md
|--- 01_Core/                 # CORE: Skills, Agents, MCP, Server
|    |--- 03_Skills/          # Skills numeradas (00-17)
|    |--- 03_Agents/          # Agent definitions
|    |--- 02_Evals/           # Evaluations
|    |--- 05_Mcp/             # MCP servers config
|    |--- 09_Server/          # Python MCP server
|    |--- 10_Templates/       # Templates
|    +--- 01_Rules/           # Rules del sistema
|
|--- 02_Knowledge/            # Base de conocimiento
|--- 03_Tasks/               # Tareas con YAML frontmatter
|--- 04_Operations/           # Memoria y contexto
|    |--- 01_Auto_Improvement/ # Motor de automejora
|    |--- 04_Memory_Brain/    # Mapeos y analisis
|    |--- 05_Plans/           # Planes
|    |--- 06_Solutions/        # Soluciones
|    |--- 07_Installer/       # Instalador
|    |--- 08_Auditorias/      # Auditorias
|
|--- 05_Archive/             # Archivo: Repos, legacy
|    |--- 10_Repos_Gentleman/ # Repos Gentleman
|
|--- 06_Playground/          # Area de pruebas
|--- 07_Projects/            # Proyectos activos
|--- 08_Scripts_Os/          # HUBs: Auditor, Git, AIPM, Ritual, etc.
|    |--- Auditor_Fixed/      # Scripts de auditoria
|    |--- Ritual_Fixed/       # Scripts de rituales
|    |--- Legacy_Backup/      # Scripts legacy
|
|--- Maerks/                  # Maerks workspace
|--- Otros/                   # Otros recursos
|
|--- AGENTS.md                # Root entry (apunta a 00_Winter_is_Coming/)
|--- CLAUDE.md                # Config para Claude Code
|--- README.md                # Documentacion principal
|--- Dream_Team.md           # Equipo de agentes
```

---

# Estructura .agent/ (Configuracion AI)

```
.agent/
|--- 00_Rules/                # Reglas del agente
|--- 01_Agents/               # Agentes externos configurados
|--- 02_Skills/               # Skills organizadas (legacy backup)
|--- 03_Skills/               # Skills PRINCIPALES (01_Core/03_Skills/)
|--- 04_Extensions/          # Hooks del sistema
|    +--- hooks/              # Hooks activos
|        |--- 01_Pre_Tool/    # PreToolUse: battery, security
|        |--- 02_Post_Tool/  # PostToolUse: backup, voice
|        |--- 03_Lifecycle/   # Stop, SubagentStop
|        +--- 04_Sound/      # Notifications, sounds
|--- 05_GGA/                 # Gentleman Guardian Angel (Code Review)
```

---

# HUB Scripts

Centralized HUBs in `08_Scripts_Os/`:

| Hub | Script | Proposito |
|-----|--------|-----------|
| **Auditor** | `01_Auditor_Hub.py` | System validation: structure, links, skills, health |
| **Git** | `02_Git_Hub.py` | Git operations + structure audits |
| **AIPM** | `03_AIPM_Hub.py` | AI Performance Monitoring |
| **Ritual** | `04_Ritual_Hub.py` | Session rituals: open, close, recovery |
| **Validator** | `05_Validator_Hub.py` | Code validation: rules, stack, patterns |
| **Tool** | `06_Tool_Hub.py` | Tool integration and management |
| **Integration** | `07_Integration_Hub.py` | MCP and external integrations |
| **Workflow** | `08_Workflow_Hub.py` | Workflow automation |
| **Data** | `09_Data_Hub.py` | Data processing and analytics |
| **General** | `10_General_Hub.py` | General utilities |

---

# Skills Disponibles

## Skills por Categoria (`01_Core/03_Skills/`)

| Categoria | Skills | Ubicacion |
|-----------|--------|-----------|
| **00_Compound_Engineering** | 8 | `00_Compound_Engineering/` |
| **00_Personal_Os_Stack** | Core OS | `00_Personal_Os_Stack/` |
| **00_Skill_Auditor** | Auditor | `00_Skill_Auditor/` |
| **01_Agent_Teams_Lite** | SDD Workflows | `01_Agent_Teams_Lite/` |
| **02_Project_Manager** | Project management | `02_Project_Manager/` |
| **03_Product_Manager** | Product management | `03_Product_Manager/` |
| **04_Product_Design** | Design skills | `04_Product_Design/` |
| **05_Vibe_Coding** | Framework skills | `05_Vibe_Coding/` |
| **06_Testing** | Testing skills | `06_Testing/` |
| **07_DevOps** | DevOps skills | `07_DevOps/` |
| **08_Personal_Os** | Personal OS skills | `08_Personal_Os/` |
| **09_Marketing** | Marketing skills | `09_Marketing/` |
| **10_Backup** | Backup/Legacy | `10_Backup/` |
| **11_Doc_Processing** | Document processing | `11_Doc_Processing/` |
| **12_N8N** | N8N workflows | `12_N8N/` |
| **13_System_Master** | Master skill | `13_System_Master/` |
| **14_Anthropic_Harness** | Evaluators | `14_Anthropic_Harness/` |
| **15_Skill_Creator_Oficial** | Skill Creator v2.0 | `15_Skill_Creator_Oficial/` |
| **16_Silicon_Valley_Data_Analyst** | Data Analyst | `16_Silicon_Valley_Data_Analyst/` |
| **17_SEO_SOTA_Master** | SEO Master | `17_SEO_SOTA_Master/` |

**Total: 19 categorias de skills**

---

# Sistema de Auto-Mejora Recursiva

Ubicacion: `04_Operations/01_Auto_Improvement/`

```
01_Auto_Improvement/
|--- 01_Engine/
|    |--- detector.py         # Detecta issues criticos
|    |--- analyzer.py        # Analiza y clasifica
|    |--- executor.py        # Aplica fixes
|    |--- learner.py         # Aprende de fixes
|    +--- recursive_improvement_engine.py
|
|--- 02_Rules/
|    +--- rules_engine.py    # Motor de reglas
|
|--- 04_Triggers/
|    +--- manual_trigger.py  # Disparador manual
```

---

# Comandos Rapidos (Aliases en .bashrc)

```bash
# Hubs principales
gr              # System Auditor (Auditor Hub)
audit           # System Auditor (mismo que gr)
git-hub         # Git operations
aipm            # AI Performance Monitoring
ritual          # Session rituals
validate        # Code validation

# System Guardian
gr-dry          # Dry run validation
gr-apply        # Apply fixes
gr-agents       # Run agent review
```

---

# SDD Workflow

Usa los comandos SDD: `/sdd:init`, `/sdd:explore`, `/sdd:new`, `/sdd:spec`, `/sdd:design`, `/sdd:tasks`, `/sdd:apply`, `/sdd:verify`, `/sdd:archive`.

---

# Compound Engineering

Usa los comandos CE: `/ce:ideate`, `/ce:brainstorm`, `/ce:plan`, `/ce:work`, `/ce:review`, `/ce:compound`.

---

# GGA — Guardian Angel (Code Review)

Code review con IA integrado.

```bash
.agent/05_GGA/bin/gga run      # Revisar archivos staged
.agent/05_GGA/bin/gga install  # Instalar pre-commit hook
```

---

# Reglas Fundamentales

## Regla Fundamental: Modificacion del OS

**Solo el IA** tiene la autoridad y la capacidad para modificar el nucleo del sistema PersonalOS (codigo, scripts, configuracion). El usuario es el estratega y dueño de la vision; el IA es el ejecutor responsable de mantener la pureza tecnica y la integridad del sistema (Pure Green).

---

# Estado Actual del Sistema (2026-03-29)

| Categoria | Estado |
|-----------|--------|
| Estructura (00-08) | ✅ PASS |
| HUBs (01-10) | ✅ ACTIVE |
| Skills (19 categorias) | ✅ OPERATIONAL |
| Auto-Improvement Engine | ✅ OPERATIONAL |
| Git Estado | ✅ CLEAN |

---

© 2026 PersonalOS v6.1
