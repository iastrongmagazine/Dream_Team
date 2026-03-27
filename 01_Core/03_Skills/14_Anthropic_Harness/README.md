# 14_Anthropic_Harness — Anthropic Harness Patterns Skills

Skills para implementar el patrón de Anthropic para agentes de larga duración.

> **FILOSOFÍA**: "No te traiciones, no te abandones" — Siempre lo correcto

---

## 📦 Skills

| # | Skill | Propósito |
|---|-------|-----------|
| 01 | `01_Evaluator_Pattern/` | Adversarial Evaluation (GAN pattern) |
| 02 | `02_Context_Management/` | Reset vs Compaction según modelo |
| 03 | `03_Sprint_Contract/` | Negotiate "done" antes de build |
| 04 | `04_Auto_Mode_Security/` | Security wrapper para Auto Mode |
| 05 | `05_Pass_At_Metrics/` | Métricas de evaluación |
| 06 | `06_Eval_Awareness/` | Detección de contexto |
| 07 | `07_Feature_List_JSON/` | Generación de features |
| 08 | `08_Graders_Framework/` | Framework de grading |

---

## 🔌 Claude Code Plugins Instalados

| # | Plugin | Ubicación | Propósito |
|---|--------|-----------|-----------|
| 1 | `pr-review-toolkit` | `.claude/plugins/...` | 6 agentes de code review especializados |
| 2 | `security-guidance` | `.claude/plugins/...` | Guías de seguridad oficiales |
| 3 | `agent-sdk-dev` | `.claude/plugins/...` | Desarrollo Agent SDK apps |
| 4 | `claude-code-setup` | `.claude/plugins/...` | Analizador de automatizaciones |

> **Instalación**: Manual (bug en marketplace) - GitHub clone + registered in `installed_plugins.json`

---

## 🏗️ Arquitectura

```
                    ┌─────────────────────────────────────────────┐
                    │           ANTHROPIC HARNESS                 │
                    └─────────────────────────────────────────────┘
                                      │
           ┌──────────────────────────┼──────────────────────────┐
           │                          │                          │
           ▼                          ▼                          ▼
┌─────────────────────┐  ┌─────────────────────┐  ┌─────────────────────┐
│  CONTEXT MANAGER    │  │   EVALUATOR        │  │  SPRINT CONTRACT   │
│  (Skill 02)        │  │   (Skill 01)       │  │  (Skill 03)        │
│                     │  │                     │  │                    │
│ • Reset vs Compact  │  │ • QA separado       │  │ • Define "done"    │
│ • Detectar anxiety  │  │ • Grading criteria │  │ • Negotiate terms  │
│ • Opus vs Sonnet    │  │ • GAN pattern      │  │ • Verify after     │
└─────────────────────┘  └─────────────────────┘  └─────────────────────┘
           │                          │                          │
           └──────────────────────────┼──────────────────────────┘
                                      │
                                      ▼
                    ┌─────────────────────────────────────────────┐
                    │         THREE-AGENT PATTERN                │
                    │  PLANNER → GENERATOR → EVALUATOR          │
                    └─────────────────────────────────────────────┘
```

---

## 🚀 Uso

Cargar skill según necesidad:

```
/load_skill anthropic_harness/evaluator_pattern
/load_skill anthropic_harness/context_management  
/load_skill anthropic_harness/sprint_contract
```

---

## 📚 Scripts Relacionados

En `08_Scripts_Os/11_Anthropic_Harness/`:

| Script | Función |
|--------|---------|
| `00_Safety_Wrapper.py` | Validaciones pre-ejecución |
| `01_Context_Manager.py` | Lógica de context |
| `02_Evaluator_Runner.py` | Lógica de QA |
| `03_Sprint_Contract.py` | Lógica de contracts |
| `04_Playwright_QA.py` | Testing interactivo |

---

## 📖 Referencia Principal

- Artículo completo: `01_Brain/02_Knowledge_Brain/10_Anthropic_Harness_Design.md`
- Workflow: `.agent/03_Workflows/17_Anthropic_Harness.md`

---

## 🎯 Integración con Perfiles

| Perfil | Skills que usa |
|--------|---------------|
| Product Builder | 01 + 02 + 03 |
| Design Ops | 01 + 03 |
| Data Engineer | 01 + 02 |
| Marketing Tech | 01 + 02 |
| Platform Engineer | 02 + 03 |

---

*Creado: 2026-03-26 | Versión: 1.0*
