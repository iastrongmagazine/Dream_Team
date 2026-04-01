# Think Different PersonalOS v6.1

[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-orange)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Version](https://img.shields.io/badge/Version-6.1-green)]()
[![Status](https://img.shields.io/badge/Status-100%25%20--%20Production%20Ready-blue)]()

> 🧠 **Sistema operativo personal potenciador con IA** - Múltiples agentes, skills SOTA, y automatización completa.

- --

## 📊 Estado del Sistema

| Métrica            | Valor       |
|:-------------------|:-----------:|
| **Overall Health** | **100%** ✅ |
| **Skills**         |    160+     |
| **Rules**          |     23      |
| **MCPs**           |     36+     |
| **HUBs**           |     10      |
| **SDD Workflows**  |      9      |

- --

## 📂 Estructura del Sistema (v6.1)

```
Think_Different/
├── 00_Winter_is_Coming/          # Goals, Backlog, AGENTS.md (ESTRATÉGICO)

├── 01_Core/                      # Motor: Skills, Agents, MCPs, Rules 💾

│   ├── 01_Rules/                 # 23 reglas del sistema

│   ├── 03_Skills/                # 160+ skills (19 categorías)

│   ├── 05_Mcp/                   # Configuración MCP

│   └── 07_Hooks/                 # Hooks del sistema

├── 02_Knowledge/                 # Documentación, Research, Notas

│   └── 04_Docs/                   # Docs del sistema, SDD Registry

├── 03_Tasks/                     # Tareas activas (gitignored)

├── 04_Operations/                # Auto Improvement, Scripts

│   └── 01_Auto_Improvement/      # Motor de automejora

├── 05_Archive/                   # Legacy archivado

├── 06_Playground/                # Área de pruebas

├── 07_Projects/                  # Proyectos activos

├── 08_Scripts_Os/                # 10 HUBs operativos

│   ├── 03_Validator/              # skill_validator.py, skill_security_scan.py

│   └── 02_Tool/                  # Tool Shed, Skill Harmonizer, Notifier

├── .agent/                       # Backup estratégico

├── .atl/                         # SDD Registry (referencia)

└── .gga                          # Guardian Angel (Code Review)

```

- --

## 🚀 Quick Start

```bash
# En tu AI assistant (OpenCode, Claude Code, etc.)

1. Leer AGENTS.md
2. Ejecutar engram_mem_context(limit: 10)
3. ¡Listo para trabajar!
```

- --

## 🛠️ Componentes Principales

### Skills System (160+)

| Categoría                   | Skills  | Propósito                                    |
|:----------------------------|:-------:|:---------------------------------------------|
| **00_Compound_Engineering** |    8    | Compound Engineering                         |
| **00_Personal_Os_Stack**    |  Core   | Stack del OS                                 |
| **00_Skill_Auditor**        | Auditor | Validación de skills                         |
| **01_Agent_Teams_Lite**     |    9    | SDD Workflows                                |
| **02-17**                   |  150+   | Especializadas (PM, Design, SEO, Data, etc.) |

### HUBs (08_Scripts_Os/)

| Hub             | Script                  | Propósito                   |
|:----------------|:------------------------|:----------------------------|
| **Auditor**     | `01_Auditor_Hub.py`     | Auditorías del sistema      |
| **Git**         | `02_Git_Hub.py`         | Operaciones Git             |
| **AIPM**        | `03_AIPM_Hub.py`        | AI Performance Monitoring   |
| **Ritual**      | `04_Ritual_Hub.py`      | Rituales de sesión          |
| **Validator**   | `05_Validator_Hub.py`   | Validación de código        |
| **Tool**        | `06_Tool_Hub.py`        | Gestión de herramientas     |
| **Integration** | `07_Integration_Hub.py` | Integraciones MCP           |
| **Workflow**    | `08_Workflow_Hub.py`    | Automatización de workflows |
| **Data**        | `09_Data_Hub.py`        | Procesamiento de datos      |
| **General**     | `10_General_Hub.py`     | Utilidades generales        |

### Validators

| Tool                       | Ubicación                        | Función                |
|:---------------------------|:---------------------------------|:-----------------------|
| **skill_validator.py**     | `08_Scripts_Os/03_Validator/` | Valida estructura SOTA |
| **skill_security_scan.py** | `08_Scripts_Os/03_Validator/` | Escaneo de seguridad   |

- --

## 📋 Comandos SDD

Usa los comandos SDD para trabajo estructurado:

```
/sdd-init           # Inicializar contexto SDD

/sdd-explore        # Explorar tema

/sdd-propose        # Crear propuesta

/sdd-spec           # Especificación

/sdd-design         # Diseño técnico

/sdd-tasks          # Descomponer tareas

/sdd-apply          # Implementar

/sdd-verify         # Verificar

/sdd-archive        # Archivar

```

- --

## 🔧 Comandos CE (Compound Engineering)

```
/ce:ideate          # Generar ideas

/brainstorm         # Lluvia de ideas

/ce:plan            # Crear plan

/ce:work            # Ejecutar trabajo

/ce:review          # Revisar

/ce:compound        # Documentar conocimiento

```

- --

## ⚙️ GGA — Guardian Angel

Code review automático integrado:

```bash
.agent/05_GGA/bin/gga run      # Revisar archivos staged

.agent/05_GGA/bin/gga install  # Instalar pre-commit hook

```

### Reglas GGA

- TypeScript: `const`/`let` solo, no `var`
- React: Componentes funcionales, named exports

- --

## 📁 Convenciones de Nombres

| Tipo            | Patrón                | Ejemplo                      |
|:----------------|:----------------------|:-----------------------------|
| **Directorios** | `XX_Nombre/`          | `01_Core/`, `04_Operations/` |
| **Archivos**    | `XX_Nombre.ext`       | `01_Report_Status.md`        |
| **Scripts**     | `##_Nombre_Script.py` | `01_Auditor_Hub.py`          |
| **Skills**      | `SKILL.md`            | En cada skill                |

- --

## 📚 Documentación

| Documento                | Ubicación                                           |
|:-------------------------|:----------------------------------------------------|
| **AGENTS.md**            | `00_Winter_is_Coming/AGENTS.md`                     |
| **RULES_INDEX**          | `01_Core/01_Rules/RULES_INDEX.md`                   |
| **Skills README**        | `01_Core/03_Skills/README.md`                       |
| **Scripts INDEX**        | `08_Scripts_Os/SCRIPTS_INDEX.md`                    |
| **OS Integration Audit** | `02_Knowledge/04_Docs/OS_Integration_Audit_v6.1.md` |
| **Edge Cases**           | `02_Knowledge/04_Docs/OS_Edge_Cases_Analysis.md`    |

- --

## 🎯 Workflow Diario

1. **Inicio de sesión**: `engram_mem_context()` + leer GOALS.md
2. **Trabajo**: Usar SDD commands para tareas complejas
3. **Cierre**: `engram_mem_session_summary()`

- --

## 📄 Licencia

CC BY-NC-SA 4.0 - Uso no comercial permitido.

- --

* Think Different PersonalOS v6.1 — Production Ready ✅*
