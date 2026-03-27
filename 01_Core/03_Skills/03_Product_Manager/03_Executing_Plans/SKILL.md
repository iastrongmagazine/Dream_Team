---
name: executing-plans
description: Ejecuta un plan de acción previamente escrito, manteniendo la trazabilidad y el orden. Triggers on: execute plan, run plan, implement plan, follow plan, batch execution.
---

## Esencia Original
> **Propósito:** Ejecutar planes paso a paso por batches, con checkpoints para review del arquitecto.
> **Flujo:** Cargar plan → Review crítico → Ejecutar batch → Reportar → Continuar

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Ejecutar todo de una sin checkpoints
  - **Por qué**: Si hay un error, perdés todo el progreso
  - **Solución**: Batches de 3 tasks, reportar entre batches

- **[ERROR]**: No revisar el plan antes de ejecutar
  - **Por qué**: El plan puede tener errores que se propagan
  - **Solución**: Review crítico antes de empezar

- **[ERROR]**: Adivinar cuando no entendés una instrucción
  - **Por qué**: Implementás algo que no es lo que se pide
  - **Solución**: Preguntar, no asumir

- **[ERROR]**: Saltarse verificaciones intermedias
  - **Por qué**: Bugs se cuelan y son difíciles de debuggear
  - **Solución**: Seguir cada step de verificación del plan

## 📁 Progressive Disclosure

> Para información detallada:
- [references/batch-execution.md](references/batch-execution.md) — Guía de ejecución por batches
- [references/checkpoint-template.md](references/checkpoint-template.md) — Template de checkpoint

## 🛠️ Scripts

- [scripts/execute-plan.py](scripts/execute-plan.py) — Helper para ejecutar planes

## 💾 State Persistence

Seguimiento de ejecución en:
- `03_Tasks/` — Tasks en progreso
- Checkpoint reports entre batches

# Executing Plans

## Overview

Load plan, review critically, execute tasks in batches, report for review between batches.

**Core principle:** Batch execution with checkpoints for architect review.

**Announce at start:** "I'm using the executing-plans skill to implement this plan."

## The Process

### Step 1: Load and Review Plan

1. Read plan file
2. Review critically - identify any questions or concerns about the plan
3. If concerns: Raise them with your human partner before starting
4. If no concerns: Create TodoWrite and proceed

### Step 2: Execute Batch

**Default: First 3 tasks**

For each task:

1. Mark as in_progress
2. Follow each step exactly (plan has bite-sized steps)
3. Run verifications as specified
4. Mark as completed

### Step 3: Report

When batch complete:

- Show what was implemented
- Show verification output
- Say: "Ready for feedback."

### Step 4: Continue

Based on feedback:

- Apply changes if needed
- Execute next batch
- Repeat until complete

### Step 5: Complete Development

After all tasks complete and verified:

- Announce: "I'm using the finishing-a-development-branch skill to complete this work."
- **REQUIRED SUB-SKILL:** Use superpowers:finishing-a-development-branch
- Follow that skill to verify tests, present options, execute choice

## When to Stop and Ask for Help

**STOP executing immediately when:**

- Hit a blocker mid-batch (missing dependency, test fails, instruction unclear)
- Plan has critical gaps preventing starting
- You don't understand an instruction
- Verification fails repeatedly

**Ask for clarification rather than guessing.**

## When to Revisit Earlier Steps

**Return to Review (Step 1) when:**

- Partner updates the plan based on your feedback
- Fundamental approach needs rethinking

**Don't force through blockers** - stop and ask.

## Remember

- Review plan critically first
- Follow plan steps exactly
- Don't skip verifications
- Reference skills when plan says to
- Between batches: just report and wait
- Stop when blocked, don't guess
