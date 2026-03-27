---
name: writing-strategy-memos
description: QUÉ HACE: Redacta y valida memos estratégicos (Framework FocusFlow) centrados en problemas reales. CUÁNDO SE EJECUTA: Al definir visiones de producto, refinar ideas complejas o fundamentar decisiones estratégicas.
---

# Writing Strategy Memos

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
