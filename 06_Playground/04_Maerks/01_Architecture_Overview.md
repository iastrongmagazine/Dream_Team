# Architecture Overview (7 Dimensions)

## 🏗️ Dimensiones del Sistema
| Dimensión                    | Propósito                           | Contenido Clave                                    |
|------------------------------|-------------------------------------|----------------------------------------------------|
| `00_Core/`                   | ADN y estrategias                   | AGENTS.md, BACKLOG.md, GOALS.md                    |
| `01_Core/`                   | Mapa, contexto y reglas             | Context_Memory, Knowledge_Brain, Rules             |
| `04_Operations/`             | Ejecución diaria                    | Active_Tasks, Evals, Progress                      |
| `03_Knowledge/`              | Memoria a largo plazo               | Research, Notes, Resources                         |
| `04_Operations/`             | Automatización                      | Scripts (Python), Tools                            |
| `05_System/`                 | Chasis                              | MCP, Env, Core                                     |
| `06_Archive/`                | Histórico                           | Backups, Legacy                                    |

---

## 🎯 v5.2 Matrix Recargado - Actualización

### Nuevos Componentes
| Componente                        | Descripción                                                             |
|-----------------------------------|-------------------------------------------------------------------------|
| **Tool Shed Pattern**             | 36 MCPs organizados en 8 dominios (Stripe Minions inspired)             |
| **Docs Analizadas**               | Stripe Minions, Gentleman Ecosystem, Firecrawl                          |
| **Skills Instaladas**             | 4 externas (find-skills, shadcn, mcp-builder, prd)                      |

### Docs Clave (v5.2)
| Documento                       | Ubicación                                                         | Descripción                               |
|---------------------------------|-------------------------------------------------------------------|-------------------------------------------|
| Resumen Sistema                 | `Revisar_Analizar/00_Resumen_Sistema_V5.2.md`                     | Overview completo del sistema             |
| Reference Guide                 | `Revisar_Analizar/00_Reference_Guide.md`                          | Guía de referencia rápida                 |
| Stripe Minions                  | `Revisar_Analizar/01_Analisis_Stripe_Minions.md`                  | Análisis de patrones MCP                  |
| Gentleman Ecosystem             | `Revisar_Analizar/02_Gentleman_Ecosystem_Tutorial.md`             | Tutorial del ecosistema                   |
| **Firecrawl Guide**             | `Revisar_Analizar/03_Firecrawl_Guide.md`                          | Guía de web scraping con IA               |

---

## 🛠️ Tool Shed Pattern (8 Dominios)

Organización de 36 MCPs para evitar token explosion:

| Dominio                    | MCPs                                                      | Propósito                            |
|----------------------------|-----------------------------------------------------------|--------------------------------------|
| `01_search/`               | exa, brave-search, stackoverflow                          | Búsqueda web y código                |
| `02_memory/`               | engram, aim-memory-bank, notebooklm                       | Memoria persistente                  |
| `03_notes/`                | Notion, mcp-obsidian, obsidian-api                        | Gestión de notas                     |
| `04_browser/`              | Playwright, chrome-devtools                               | Automatización browser               |
| `05_ai_code/`              | context7, github, zai, task-master, anthropic             | AI y código                          |
| `06_data/`                 | supabase, postgres, sqlite, Amplitude                     | Datos y DB                           |
| `07_workflow/`             | n8n, Linear, atlassian, jira                              | Workflow y productividad             |
| `08_design/`               | excalidraw, pencil                                        | Diseño y diagramas                   |

**Referencia:** `Revisar_Analizar/01_Analisis_Stripe_Minions.md`

---

## 🔄 Gentleman Ecosystem

Framework completo que integra:

| Componente               | Propósito                                      | Archivo Clave                                           |
|--------------------------|------------------------------------------------|---------------------------------------------------------|
| **Engram**               | Memoria persistente cross-session              | Configurado en `.mcp.json`                              |
| **SDD**                  | Spec-Driven Development workflow               | `~/.config/opencode/skills/gentleman/`                  |
| **Skills**               | Módulos de contexto especializados             | 128+ skills organizadas                                 |
| **Compound**             | 50-70% token savings                           | Skills `ce-*` en `06_Compound_Engineering/`             |

### SDD Workflow
```
explore → propose → spec → design → tasks → apply → verify → archive
```

**Docs:** `Revisar_Analizar/02_Gentleman_Ecosystem_Tutorial.md`

---

## 🔥 Firecrawl Integration

Web scraping y extracción de datos con IA.

### Ideas de Negocio (del video analyzed)
1. **Lead Generation** - Extraer emails de directorios de empresas
2. **Competitive Intelligence** - Monitorizar precios y productos de competidores
3. **Content Aggregation** - Recopilar contenido de múltiples fuentes
4. **Job Posting Aggregation** - Centralizar ofertas de empleo
5. **Real Estate Data** - Extraer propiedades y precios
6. **Academic Research** - Recopilar papers y publicaciones

**Docs:** `Revisar_Analizar/03_Firecrawl_Guide.md`

---

## 🛡️ System Guardian

Validación automática del proyecto (pasos 1-8) + 3 agentes de revisión:

```bash
gr              # Dry-run
gra             # Con --apply
gr-agents       # Solo 3 agents
```

**Script:** `04_Operations/08_Scripts_Os/79_System_Guardian.py` |
