# Operational Guide (v5.2)

## Reglas de Oro
1. **Pensar 3 veces**: Antes de ejecutar, validar el efecto colateral.
2. **Validación Triple**: Todo script y skill debe pasar 3 pruebas (lógica, datos, output).
3. **Esencia**: Nunca romper la esencia del OS original.

---

## Scripts del Motor

### Ejecución Diaria
| Script                              | Propósito                              | Ubicación                              |
|-------------------------------------|----------------------------------------|----------------------------------------|
| `09_Backlog_Triage.py`              | Procesar backlog con dedup             | `04_Operations/08_Scripts_Os/`         |
| `14_Morning_Standup.py`             | Daily standup                          | `04_Operations/08_Scripts_Os/`         |
| `13_Validate_Stack.py`              | Validar herramientas                   | `04_Operations/08_Scripts_Os/`         |
| `08_Ritual_Cierre.py`               | Ritual de cierre                       | `04_Operations/08_Scripts_Os/`         |

### Mantenimiento del Sistema
| Script                                | Propósito                         |
|---------------------------------------|-----------------------------------|
| `53_Structure_Auditor.py`             | Valida carpetas 00-07             |
| `40_Validate_Rules.py`                | Valida reglas                     |
| `55_Avengers_Workflow.py`             | Review → Compound                 |
| `63_Audit_Sync_Master.py`             | Sincronización master             |
| `79_System_Guardian.py`               | Validación completa               |

---

## v5.2 Nuevas Capacidades

### Tool Shed Pattern
- 36 MCPs organizados en 8 dominios
- Evita token explosion en contexto
- **Archivo:** `03_Knowledge/08_Config_Mcp/mcp-tools/`

### Docs Analizadas
| Doc                             | Ubicación                                                         | Propósito                   |
|---------------------------------|-------------------------------------------------------------------|-----------------------------|
| Stripe Minions                  | `Revisar_Analizar/01_Analisis_Stripe_Minions.md`                  | Patrones MCP                |
| Gentleman Ecosystem             | `Revisar_Analizar/02_Gentleman_Ecosystem_Tutorial.md`             | Framework SDD               |
| Firecrawl Guide                 | `Revisar_Analizar/03_Firecrawl_Guide.md`                          | Web scraping IA             |

### Skills SDD
- `sdd-init`, `sdd-explore`, `sdd-propose`, `sdd-spec`
- `sdd-design`, `sdd-tasks`, `sdd-apply`, `sdd-verify`, `sdd-archive`
- **Ubicación:** `~/.config/opencode/skills/gentleman/`

---

## Workflows Principales

### SDD (Spec-Driven Development)
```
explore → propose → spec → design → tasks → apply → verify → archive
```

### Compound Engineering (Every)
```
Ideate → Brainstorm → Plan → Work → Review → Compound → Repeat
```

### Backlog Flow
1. Extraer ítems de `00_Core/BACKLOG.md`
2. Usar `04_Operations/08_Scripts_Os/09_Backlog_Triage.py`
3. Crear tareas en `04_Operations/01_Active_Tasks/`
4. Vincular con metas en `00_Core/GOALS.md`

---

## Comandos Útiles

### Slash Commands
| Comando                    | Descripción                            |
|----------------------------|----------------------------------------|
| `/gr`                      | System Guardian (dry-run)              |
| `/gr --apply`              | System Guardian + auto-fix             |
| `/gr --agents`             | Solo 3 agentes de revisión             |

### Engram (Memoria)
| Comando                           | Descripción                                 |
|-----------------------------------|---------------------------------------------|
| `mem_save`                        | Guardar decisión/descubrimiento             |
| `mem_search`                      | Buscar en memoria                           |
| `mem_session_summary`             | Resumen de sesión                           |

### QMD (Búsqueda)
| Comando                                | Descripción                       |
|----------------------------------------|-----------------------------------|
| `bun qmd.js query <query>`             | Búsqueda híbrida                  |
| `bun qmd.js status`                    | Ver estado del índice             |
