# 📖 Think Different AI — Reference Guide

> **Versión:** v5.2 Matrix Recargado | **Fecha:** 2026-03-26

---

## 🔄 Flujos de Trabajo

| ID      | Workflow                | Descripción                                   | Script                            |
|---------|-------------------------|-----------------------------------------------|-----------------------------------|
| 01      | 🌅 Morning Standup       | Planificación matutina y enfoque diario       | `14_Morning_Standup.py`           |
| 02      | 📥 Backlog Triage        | Organización, limpieza y priorización         | `09_Backlog_Triage.py`            |
| 03      | 📊 Weekly Review         | Reflexión semanal y planificación             | `15_Weekly_Review.py`             |
| 04      | ⛪ Sunday Ritual         | Mantenimiento sistémico profundo              | `17_Ritual_Dominical.py`          |
| 05      | ✍️ Content Engine       | Generación de contenido y marketing           | `18_Generacion_Contenido.py`      |

---

## ⚡ Comandos Rápidos (CE)

| Comando                | Propósito                                     |
|------------------------|-----------------------------------------------|
| `/ce:ideate`           | Descubrir mejoras de alto impacto             |
| `/ce:brainstorm`       | Explorar requisitos y enfoques                |
| `/ce:plan`             | Generar planes técnicos exhaustivos           |
| `/ce:work`             | Ejecutar con worktrees                        |
| `/ce:review`           | Revisión multi-agente                         |
| `/ce:compound`         | Documentar aprendizajes                       |

---

## 🧩 Skills SDD

| Skill                 | Propósito                                      |
|-----------------------|------------------------------------------------|
| `sdd-init`            | Inicializar contexto SDD + persistencia        |
| `sdd-explore`         | Investigar código/ideas antes de cambios       |
| `sdd-propose`         | Crear propuesta con alcance y riesgos          |
| `sdd-spec`            | Escribir specs con escenarios testeables       |
| `sdd-design`          | Diseño técnico y decisiones                    |
| `sdd-tasks`           | Descomponer en tareas implementables           |
| `sdd-apply`           | Implementar tareas por batches                 |
| `sdd-verify`          | Verificar contra specs y tareas                |
| `sdd-archive`         | Cerrar cambio y archivar artefactos            |

---

## 🎯 Repos Gentleman Ecosystem

| Repo                       | Descripción                                          |
|----------------------------|------------------------------------------------------|
| 🧠 Engram                   | Memoria persistente cross-session                    |
| 🤖 Agent Teams Lite         | Orquestador + 9 subagentes especializados            |
| 🛡️ GGA                     | Code review con IA + pre-commit hook                 |
| ⚙️ Gentle IA               | Configurador del ecosistema                          |
| 🎯 Gentleman Skills         | Skills técnicas curadas                              |
| 🔒 veil.nvim                | Seguridad visual en Neovim                           |
| ⚙️ Gentleman.Dots          | Dotfiles: LazyVim, WezTerm, Tmux/Zellij              |

---

## 📊 Stats Sistema

| Métrica             | Valor                              |
|---------------------|------------------------------------|
| MCPs                | 36 servidores activos              |
| Skills              | 128+ reales                        |
| Workflows           | 5 principales                      |

---

## 🔧 Docs Clave

| Documento                            | Ubicación                                                    |
|--------------------------------------|--------------------------------------------------------------|
| Resumen Sistema                      | `00_Resumen_Sistema_V5.2.md`                                 |
| AGENTS.md                            | `00_Core/AGENTS.md`                                          |
| BACKLOG.md                           | `00_Core/BACKLOG.md`                                         |
| Análisis Stripe Minions              | `Revisar_Analizar/01_Analisis_Stripe_Minions.md`             |
| Gentleman Ecosystem                  | `Revisar_Analizar/02_Gentleman_Ecosystem_Tutorial.md`        |
| **Firecrawl Guide**                  | `Revisar_Analizar/03_Firecrawl_Guide.md` (pendiente)         |
| Tool Shed MCPs                       | `03_Knowledge/08_Config_Mcp/mcp-tools/`                      |
| Resolutions                          | `01_Core/10_Resolutions/`                                    |

---

## 🛠️ Tool Shed Pattern

**Concepto:** 36 MCPs → 8 dominios = ~15 tokens vs 36 tokens

| Dominio                   | MCPs Incluidos                               |
|---------------------------|----------------------------------------------|
| `01_core/`                | context7, engram, github                     |
| `02_knowledge/`           | obsidian, notion, aim-memory                 |
| `03_development/`         | playwright, docker, chrome                   |
| `04_research/`            | firecrawl, exa                               |
| `05_visual/`              | excalidraw                                   |
| `06_productivity/`        | linear                                       |

---

## 📋 Guía de Uso

### 1. Captura de Ideas
- Escribir en `00_Core/BACKLOG.md`

### 2. Procesar Backlog
- Comando: `"Lee AGENTS.md y procesa mi backlog"`
- Crea tareas en `04_Operations/01_Active_Tasks/`

### 3. Planificar
- Usar `/ce:plan` para generar plan técnico

### 4. Ejecutar
- Usar `/ce:work` para implementación

### 5. Revisar
- Usar `/ce:review` para auditoría

---

## 🚀 Ciclo: Plan → Work → Review → Compound → Repeat

---

*_"El orden en el caos es la base de la ejecución implacable."_*
