# 11_Anthropic_Harness — Anthropic Harness Patterns Scripts

Scripts para implementar el patrón de Anthropic para agentes de larga duración.

> **FILOSOFÍA**: "No te traiciones, no te abandones" — Siempre lo correcto

---

## 📦 Scripts

| # | Script | Propósito |
|---|--------|-----------|
| 00 | `00_Safety_Wrapper.py` | Check de no-regresión antes de ejecutar |
| 01 | `01_Context_Manager.py` | Reset vs Compaction según modelo |
| 02 | `02_Evaluator_Runner.py` | QA Agent separado (GAN pattern) |
| 03 | `03_Sprint_Contract.py` | Negotiate "done" antes de build |
| 04 | `04_Playwright_QA.py` | Testing interactivo para Evaluator |

---

## 🏗️ Patrones Implementados

### Three-Agent Architecture
```
PLANNER → GENERATOR → EVALUATOR
  (spec)    (code)     (QA)
```

### Context Handling
- **Opus 4.6+**: Context compaction (no reset needed)
- **Sonnet 4.5**: Context reset (suffers from context anxiety)

### Adversarial Evaluation
- Generator ≠ Evaluator (NO self-evaluation!)
- Criterios gradables (no subjetivos)
- Pesos: Design Quality + Originalidad > Craft + Funcionalidad

### Sprint Contract
- Generator + Evaluator negotiate "done" upfront
- Evita "scope creep" durante build

---

## 🚀 Uso

```python
# Safety Check
from 11_Anthropic_Harness import run_safety_check

if run_safety_check("01_Context_Manager", {"token_count": 50000}):
    # Execute script
    pass

# Context Manager
from 11_Anthropic_Harness import run_context_manager

result = run_context_manager(token_count=80000)
# result = {'action': 'compact', 'reason': '...', 'model': 'opus-4-6'}

# Evaluator
from 11_Anthropic_Harness import run_evaluator

result = run_evaluator(code_output, output_type="code")
# result.passed = True/False

# Sprint Contract
from 11_Anthropic_Harness import run_sprint_contract

result = run_sprint_contract("sprint_01", "Login", proposal, requirements)

# Playwright QA
from 11_Anthropic_Harness import run_playwright_qa

result = run_playwright_qa("http://localhost:3000", tests)
```

---

## 📚 Referencia

- Artículo: `01_Brain/02_Knowledge_Brain/10_Anthropic_Harness_Design.md`
- Skills: `.agent/02_Skills/14_Anthropic_Harness/`
- Workflow: `.agent/03_Workflows/17_Anthropic_Harness.md`

---

## ⚙️ Requisitos

```bash
pip install anthropic playwright
```

---

*Creado: 2026-03-26 | Versión: 1.0*
