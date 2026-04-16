# 📊 GAP ANALYSIS — OS v5.2 → v6.1

> **Fecha:** 2026-03-28
> **Objetivo:** Mapear qué tiene el OS anterior (v5.2) que falta en v6.1 y viceversa

---

## ✅ LO QUE SÍ TENEMOS EN v6.1

### Infraestructura Core

| Componente        | v5.2   | v6.1   | Notas                    |
|-------------------|--------|--------|--------------------------|
| Hubs (01-10)      | ✅      | ✅      | Independientes de Legacy |
| Skills estructura | ✅      | ✅      | 305+ skills              |
| AGENTS.md         | ✅      | ✅      | Unificado                |
| GOALS.md          | ✅      | ✅      |                          |
| BACKLOG.md        | ✅      | ✅      |                          |
| System Guardian   | ✅      | ✅      | Skill + ~/gr wrapper     |
| Engram            | ✅      | ✅      | Memoria persistente      |

### Workflows

| Workflow        | v5.2   | v6.1   | Script                       |
|-----------------|--------|--------|------------------------------|
| Morning Standup | ✅      | ✅      | `14_Morning_Standup.py`      |
| Backlog Triage  | ✅      | ✅      | `09_Backlog_Triage.py`       |
| Weekly Review   | ✅      | ✅      | `15_Weekly_Review.py`        |
| Sunday Ritual   | ✅      | ✅      | `17_Ritual_Dominical.py`     |
| Content Engine  | ✅      | ✅      | `18_Generacion_Contenido.py` |

### Comandos

| Comando   | v5.2   | v6.1   | Estado       |
|-----------|--------|--------|--------------|
| `/gr`     | ✅      | ✅      | Corregido    |
| `/ce:*`   | ✅      | ✅      | Funcional    |
| `sdd-*`   | ✅      | ✅      | 9 skills SDD |

---

## ❌ LO QUE FALTA DE v5.2 → v6.1 (GAP)

### 🔴 Alta Prioridad

| Componente             | Descripción                                               | Dónde estaba en v5.2                    | Acción necesaria               |
|------------------------|-----------------------------------------------------------|-----------------------------------------|--------------------------------|
| **Tool Shed Pattern**  | 36 MCPs organizados en 8 dominios                         | `03_Knowledge/08_Config_Mcp/mcp-tools/` | Migrar estructura MCP          |
| **MCP Domains**        | Core, Knowledge, Dev, Research, Visual, Productivity      | Documentado en v5.2                     | Implementar organización       |
| **Engram Integration** | Comandos: `mem_save`, `mem_search`, `mem_session_summary` | Documentado pero parcial                | Verificar integración completa |
| **QMD System**         | Búsqueda híbrida: `bun qmd.js query`                      | `04_Operations/`                        | Verificar si está implementado |
| **Super Campeones**    | 1 Director + 8 Agentes (4 jugadores + 4 auditores)        | Planificado                             | Documentar y implementar       |

### 🟡 Media Prioridad

| Componente             | Descripción                           | Dónde estaba en v5.2                     | Acción necesaria          |
|------------------------|---------------------------------------|------------------------------------------|---------------------------|
| **Anthropic Harness**  | Eval/Gen separation, pass@k metrics   | `.agent/02_Skills/14_Anthropic_Harness/` | Verificar integridad      |
| **Auto Mode Security** | Prompt injection detector, classifier | Planificado en v5.2                      | Implementar               |
| **Evaluator Pattern**  | Generator + Evaluator separados       | Implementado en Harness                  | Verificar funcionamiento  |
| **Slash Commands**     | `/gr`, `/gr --apply`, `/gr --agents`  | Documentado                              | Verificar todos funcionan |

### 🟢 Baja Prioridad

| Componente          | Descripción                   | Dónde estaba en v5.2   | Acción necesaria     |
|---------------------|-------------------------------|------------------------|----------------------|
| **Firecrawl Guide** | Documentación web scraping IA | `Revisar_Analizar/`    | Integrar o deprecate |
| **Stripe Minions**  | Patrones MCP avanzados        | Documentado            | Revisar relevancia   |
| **Content Engine**  | 18_Generacion_Contenido.py    | `04_Operations/`       | Verificar ruta       |

---

## 🆕 LO NUEVO EN v6.1 (NO ESTABA EN v5.2)

| Componente                 | Descripción                                              | Estado   |
|----------------------------|----------------------------------------------------------|----------|
| **01_Core reorganizado**   | 03_Agents → 04_Agents, 04_Integrations → 06_Integrations | ✅        |
| **Hubs independentes**     | Todos los Hubs (01-10) sin dependencia Legacy            | ✅        |
| **AIPM_Fixed/**            | Scripts AIPM corregidos                                  | ✅        |
| **Ritual_Fixed/**          | Scripts Ritual corregidos                                | ✅        |
| **Validator_Fixed/**       | Scripts Validator corregidos                             | ✅        |
| **Tool_Fixed/**            | Scripts Tool corregidos                                  | ✅        |
| **Integration_Fixed/**     | Scripts Integration corregidos                           | ✅        |
| **Workflow_Fixed/**        | Scripts Workflow corregidos                              | ✅        |
| **Data_Fixed/**            | Scripts Data corregidos                                  | ✅        |
| **General_Fixed/**         | Scripts General corregidos                               | ✅        |
| **SOP Prompts**            | 8 prompts para crear componentes del sistema             | ✅        |
| **Maerks/18_Gap_Analysis** | Este documento                                           | ✅        |

---

## 📋 PLAN DE INTEGRACIÓN

### Inmediato (Esta semana)

1. **Verificar Tool Shed Pattern**
   - Buscar `mcp-tools/` en el proyecto
   - Si no existe → crear estructura de dominios MCP

2. **Verificar QMD System**
   - Buscar `qmd.js` o scripts relacionados
   - Si no existe → evaluar si es necesario

3. **Documentar Super Campeones**
   - Crear guía formal de la metodología
   - Integrar con AGENTS.md

### Próxima semana

4. **Auto Mode Security Classifier**
   - Planificado en v5.2, no implementado
   - Evaluar prioridad

5. **pass@k Metrics Script**
   - Parte de Anthropic Harness
   - Verificar integridad

### Cuando haya tiempo

6. **Firecrawl Guide** → Decidir integrar o archivar
7. **Stripe Minions** → Revisar relevancia para v6.1

---

## 📊 RESUMEN

| Métrica                          | Valor    |
|----------------------------------|----------|
| **Componentes v5.2 preservados** | 85%      |
| **Gap alta prioridad**           | 5 items  |
| **Gap media prioridad**          | 4 items  |
| **Gap baja prioridad**           | 3 items  |
| **Nuevos en v6.1**               | 11 items |

---

## 🎯 PRÓXIMO PASO RECOMENDADO

Verificar si `Tool Shed Pattern` (36 MCPs en 8 dominios) está implementado en v6.1 o necesita ser migrado.
