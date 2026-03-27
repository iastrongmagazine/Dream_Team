# 🌐 Engram SOTA Ecosystem Registry
*Source of Truth - Project: Think Different*

## 1. Operational Protocols (Hooks)
| Hook                 | Path                                                               | Function                 |
|----------------------|--------------------------------------------------------------------|--------------------------|
| PostToolUse          | `.agent/04_Extensions/hooks/02_Post_Tool/post_tool_use.py`         | Backup & Voice           |
| PreToolUse           | `.agent/04_Extensions/hooks/01_Pre_Tool/pre_tool_use.py`           | Battery/Security         |
| SubagentStop         | `.agent/04_Extensions/hooks/03_Lifecycle/subagent_stop.py`         | Cleanup                  |

## 2. Execution Engine (Scripts Registry - 08_Scripts_Os/)
*Mapping de automatizaciones SOTA.*

| Script                        | Path                                                       | Purpose                         |
|-------------------------------|------------------------------------------------------------|---------------------------------|
| 14_Morning_Standup            | `04_Engine/08_Scripts_Os/14_Morning_Standup.py`            | Standup Standarizado            |
| 56_Organize_Solutions         | `04_Engine/08_Scripts_Os/56_Organize_Solutions.py`         | Hulk Solutions                  |
| 79_System_Guardian            | `04_Engine/08_Scripts_Os/79_System_Guardian.py`            | Validación del Sistema          |
| 53_Structure_Auditor          | `04_Engine/08_Scripts_Os/53_Structure_Auditor.py`          | Auditoría de Estructura         |

## 3. Intelligence Layer (AI Tools & Workflow)
*Transformación SOTA de 05_AI_Tools.md*

### A. Intelligence & Research
- **Tools:** Perplexity, ChatGPT, Claude.
- **Propósito:** Planificación, búsqueda, razonamiento y generación de documentos.
- **Acceso:** Browser / API.

### B. Development & IDEs
- **Tools:** Cursor, Windsurf, Claude Code.
- **Propósito:** Generación de código, refactorización y despliegue in-IDE.
- **Acceso:** MCP, Modo Agente (Shift + Tab).

### C. Operations & Terminal
- **Tools:** Warp, MCP.
- **Propósito:** Interacción con OS y servicios (Supabase, Vercel).
- **Referencia:** `04_Engine/08_Scripts_Os/61_MCP_Health_Check.py`

### D. Code Quality & Ops
- **Tools:** Devin Review, CodeRabbit, Vercel.
- **Propósito:** Code review automatizado, CI/CD y despliegue.

---
*Generated: 2026-03-21 | Status: VALIDATED*
