---
name: writing-plans
description: Crea planes de implementación paso a paso para tareas complejas y documentación operacional. Triggers on: write plan, create plan, technical planning, implementation plan, SOP, runbook, playbook.
---

## 📋 Skill Protocol (Armor Layer)

### 🧩 Contexto Requerido
- Diseño o arquitectura previa validada.
- Lista de archivos afectados identificada.
- Definición de "Hecho" (Definition of Done) clara.

### 📦 Output Esperado
- Plan de acción detallado paso a paso en markdown.
- Identificación de riesgos potenciales y dependencias.
- Checklist de verificación para cada fase.

### 🚫 Limitaciones
- **No ejecuta los comandos**, solo define la ruta lógica de trabajo.
- No es para tareas triviales que no requieren secuencia lógica.
---

# Writing Plans

## Esencia Original
> **Propósito:** Crear planes de implementación detallados (2-5 min por task) y documentación operacional que la gente realmente sigue.
> **Flujo:** Diseño validado → Tareas bite-sized → Checklist → Ejecución

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Planes vagos ("agregar validación")
  - **Por qué**: El implementador no sabe qué hacer
  - **Solución**: Código completo en el plan, paths exactos

- **[ERROR]**: Tasks grandes (>15 min)
  - **Por qué**: Difícil de debuggear, pierde contexto
  - **Solución**: Bite-sized tasks de 2-5 minutos

- **[ERROR]**: No incluir tests en el plan
  - **Por qué**: TDD se pierde, bugs se cuelan
  - **Solución**: Cada task incluye failing test → implementar → commit

- **[ERROR]**: SOPs sin Definition of Done
  - **Por qué**: El operador no sabe cuándo terminar
  - **Solución**: Checklist al inicio del SOP

## 📁 Progressive Disclosure

> Para información detallada:
- [references/sop-templates/](references/sop-templates/) — Plantillas de SOPs
- [references/task-structure.md](references/task-structure.md) — Estructura de tareas

## 🛠️ Scripts

- [scripts/plan-generator.py](scripts/plan-generator.py) — Genera esqueleto de plan

## 💾 State Persistence

Guardar planes en:
- `04_Docs/plans/YYYY-MM-DD-<feature-name>.md`
- `04_Docs/sops/YYYY-MM-DD-<process-name>.md`

## Overview

Write comprehensive implementation plans assuming the engineer has zero context for our codebase and questionable taste. Document everything they need to know: which files to touch for each task, code, testing, docs they might need to check, how to test it. Give them the whole plan as bite-sized tasks. DRY. YAGNI. TDD. Frequent commits.

Assume they are a skilled developer, but know almost nothing about our toolset or problem domain. Assume they don't know good test design very well.

**Announce at start:** "I'm using the writing-plans skill to create the implementation plan."

**Context:** This should be run in a dedicated worktree (created by brainstorming skill).

**Save plans to:** `04_Docs/plans/YYYY-MM-DD-<feature-name>.md`

## Bite-Sized Task Granularity

**Each step is one action (2-5 minutes):**

- "Write the failing test" - step
- "Run it to make sure it fails" - step
- "Implement the minimal code to make the test pass" - step
- "Run the tests and make sure they pass" - step
- "Commit" - step

## Plan Document Header

**Every plan MUST start with this header:**

```markdown
# [Feature Name] Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies/libraries]

---
```

## Task Structure

````markdown
### Task N: [Component Name]

**Files:**

- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

**Step 1: Write the failing test**

```python
def test_specific_behavior():
    result = function(input)
    assert result == expected
```
````

**Step 2: Run test to verify it fails**

Run: `pytest tests/path/test.py::test_name -v`
Expected: FAIL with "function not defined"

**Step 3: Write minimal implementation**

```python
def function(input):
    return expected
```

**Step 4: Run test to verify it passes**

Run: `pytest tests/path/test.py::test_name -v`
Expected: PASS

**Step 5: Commit**

```bash
git add tests/path/test.py src/path/file.py
git commit -m "feat: add specific feature"
```

````

## Remember
- Exact file paths always
- Complete code in plan (not "add validation")
- Exact commands with expected output
- Reference relevant skills with @ syntax
- DRY, YAGNI, TDD, frequent commits

## Execution Handoff

After saving the plan, offer execution choice:

**"Plan complete and saved to `04_Docs/plans/<filename>.md`. Two execution options:**

**1. Subagent-Driven (this session)** - I dispatch fresh subagent per task, review between tasks, fast iteration

**2. Parallel Session (separate)** - Open new session with executing-plans, batch execution with checkpoints

**Which approach?"**

**If Subagent-Driven chosen:**
- **REQUIRED SUB-SKILL:** Use superpowers:subagent-driven-development
- Stay in this session
- Fresh subagent per task + code review

**If Parallel Session chosen:**
- Guide them to open new session in worktree
- **REQUIRED SUB-SKILL:** New session uses superpowers:executing-plans

---

## SOP & Documentation Creation

This skill also supports creating operational documentation that people actually follow.

### When to Create SOPs

Use SOP creation when you need to:
- Document repeatable processes (deployments, incidents, maintenance)
- Create runbooks for on-call engineers
- Build troubleshooting guides
- Formalize technical procedures
- Create checklists for quality control

### SOP Document Types

Available templates in `references/sop-templates/`:

| Template | Use For |
|----------|---------|
| `runbook.md` | Incidents, emergencies, on-call |
| `standard-sop.md` | Any repeatable process |
| `how-to-guide.md` | One-off tasks, setup |
| `onboarding-guide.md` | New person ramping up |
| `decision-tree.md` | Complex if/then flows |
| `checklist.md` | QC, verification |

### SOP Writing Principles

**Core rules:**
1. **Definition of Done first** - Put success criteria at the top as a checklist
2. **Be specific** - Use numbers, names, thresholds (not "as needed" or "regularly")
3. **Action-first steps** - Start with verbs, not descriptions
4. **Warnings come first** - Before the dangerous step, not after
5. **Clear decision points** - "If X, then Y" not "handle based on priority"

### Creating an SOP

1. **Choose template** from `references/sop-templates/`
2. **Fill in sections:**
   - Definition of Done (checklist)
   - When to Use This
   - Prerequisites
   - The Process (numbered steps)
   - Verify Completion
   - When Things Go Wrong
   - Questions? (who to contact)
3. **Save to:** `04_Docs/sops/YYYY-MM-DD-<process-name>.md`

**Example SOP structure:**

```markdown
# [Process Name]

> **TL;DR:** One sentence - what, when, who.

## Definition of Done

This is complete when:
- [ ] [Primary outcome]
- [ ] [Verification step]
- [ ] [Any handoff/notification]

## When to Use This
[Trigger conditions]

## Prerequisites
[What you need before starting]

## The Process
[Numbered steps - the actual work]

## Verify Completion
[Return to Definition of Done, confirm all checked]

## When Things Go Wrong
[Common issues and fixes]

## Questions?
[Who to contact]
````

**See templates in `references/sop-templates/` for complete examples.**

```

---

## ⚡ Planificación Avanzada: Framework ShipKit (MODO SOTA)

Para tareas de ingeniería de alta complejidad, el Agente DEBE adoptar el framework de 5 pasos para garantizar la resiliencia del sistema:

### 1. El Proceso ShipKit
1.  **Investigación Profunda**: Análisis exhaustivo del codebase, tipos y dependencias reales. No asumir; verificar archivos.
2.  **Análisis de Enfoques**: Evaluar 2-3 soluciones técnicas antes de proponer una.
3.  **Generación de Recomendación**: Justificar la elección técnica basada en el Pilar 1 (Armor Layer).
4.  **Breakdown de Tareas**: Crear el `implementation_plan.md` con checklist de vitaminas.
5.  **Validación de Vitaminas**: Asegurar que el plan incluya tareas para Banners ASCII, Voz (TTS) y Audio.

### 2. Inyección de Vitaminas (AI Task Vitamin Injection)
Cuando el usuario solicite "Ajuste de tareas", se activa el protocolo de vitaminización:
- Ejecutar `python 08_Scripts_Os/03_AI_Task_Planner.py` para inyectar el esqueleto SOTA.
- **BUCLE DE ANÁLISIS**: El agente debe rellenar manualmente las secciones de "Impacto de Segundo Orden" y "Manejo de Datos" con datos reales (esquemas, modelos), no placeholders.

---
© 2026 PersonalOS | ShipKit Planning Engine

```
