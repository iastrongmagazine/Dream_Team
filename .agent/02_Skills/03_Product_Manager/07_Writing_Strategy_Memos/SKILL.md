---
name: writing-strategy-memos
description: Redacta y valida memos estratégicos usando Framework FocusFlow centrados en problemas reales. Triggers on: strategy memo, write memo, strategic document, product vision, decision framework.
---

# Writing Strategy Memos

## Esencia Original
> **Propósito:** Fundamentar decisiones de producto en problemas reales de clientes, con claridad estratégica absoluta usando el Framework FocusFlow.
> **Flujo:** Problema → Visión → Principios → Objetivos → Solución → Non-Priorities

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Empezar con la solución sin entender el problema
  - **Por qué**: Construimos cosas que nadie necesita
  - **Solución**: Siempre empezar con "Problem" — máximo 2-3 oraciones, con quotes reales

- **[ERROR]**: Visión vaga o genérica
  - **Por qué**: No diferencia, no inspira
  - **Solución**: 1 sentence memorable y diferenciada

- **[ERROR]**: Principios sin trade-offs reales
  - **Por qué**: No guían decisiones difíciles
  - **Solución**: Cada principio debe implicar un sacrifice claro ("Speed over completeness")

- **[ERROR]**: Sin Non-Priorities explícitos
  - **Por qué**: El scope crece sin control
  - **Solución**: Listar 2-4 cosas que NO hacemos

- **[ERROR]**: Goals sin metricas
  - **Por qué**: No se puede medir éxito
  - **Solución**: 1 Output (resultado) + 2-4 Inputs (levers accionables)

## 📁 Progressive Disclosure

> Para información detallada:
- [references/focusflow-framework.md](references/focusflow-framework.md) — Framework FocusFlow detallado
- [references/memo-examples.md](references/memo-examples.md) — Ejemplos de memos

## 🛠️ Scripts

- [scripts/generate-memo.py](scripts/generate-memo.py) — Genera esqueleto de memo estratégico

## 💾 State Persistence

Guardar memos en:
- `04_Docs/strategy/YYYY-MM-DD-<topic>-memo.md`
- `03_Knowledge/06_Writing/` — Para referencia futura

Este skill implementa el framework **"Workflow Strategy Memo" (FocusFlow)**, diseñado para fundamentar decisiones de producto y proyecto en problemas reales de clientes y una claridad estratégica absoluta.

## When to use this skill

- Creating a new strategy for a product or feature.
- Documenting a workflow or process.
- Refining a vague idea into a concrete, actionable strategic document.
- Validating that a proposal addresses the most critical pain points.
- Antes de iniciar un proyecto complejo en "Amazing World".

## Memo Structure (FocusFlow)

1.  **Problem (2-3 sentences max)**: Identify the core customer pain point. Focus on the _why_ before the _how_. Use direct quotes to ground it.
2.  **Vision (1 sentence)**: Create a one-sentence aspirational goal. Must be memorable and differentiated.
3.  **Principles (3 max)**: Specify what you are willing to sacrifice (e.g., "Speed over completeness"). Each must imply a real tradeoff.
4.  **Goals**: Define 1 **Output** (result) and 2-4 **Inputs** (levers/leves accionables).
5.  **Solution (3-4 initiatives)**: Propose 3-4 key initiatives. Concrete but not a full technical spec.
6.  **Non-Priorities (2-4 points)**: Explicitly state what is out of scope to maintain strategic clarity.

## Workflow

1.  **Define the Problem**: Look for pain points and evidence.
2.  **Articulate the Vision**: Define the north star.
3.  **Establish Principles**: Guide your decisions.
4.  **Set Goals**: Measure success.
5.  **Outline the Solution**: How we get there.
6.  **Explicit Non-Priorities**: What we are NOT doing.

## Instructions

- Utiliza la plantilla en `03_Knowledge/Templates/STRATEGY_MEMO.md` si existe.
- Si existe el script `scripts/generate_memo.py`, úsalo para generar el esqueleto:
  ```bash
  python scripts/generate_memo.py --title "My New Strategy" --output "04_Docs/strategy/my_strategy.md"
  ```

## Resources

- [Template](resources/memo_template.md) (if present in skill folder)
- [Generator Script](scripts/generate_memo.py) (if present in skill folder)
