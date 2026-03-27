---
name: writing-plans
description: QUÉ HACE: Crea planes de implementación paso a paso para tareas complejas Y documentación operacional (SOPs, runbooks, playbooks). CUÁNDO SE EJECUTA: Después del brainstorming y antes de la implementación, O cuando se necesita documentar procesos repetibles.

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

```
