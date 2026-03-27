---
name: brainstorming
description: QUÉ HACE: Explora la intención del usuario, requisitos y diseño mediante preguntas y enfoques alternativos. CUÁNDO SE EJECUTA: Antes de cualquier trabajo creativo o modificación compleja para asegurar claridad.
---

# Brainstorming Ideas Into Designs

## 🎯 Overview

Explora la intención del proyecto y define el camino antes de tocar una sola línea de código.

## 📋 Skill Protocol (Armor Layer)

### 🧩 Contexto Requerido

- Intención del usuario clara o vaga (para refinar).
- Acceso a `README.md` y `GOALS.md` para alineación.
- Conocimiento del stack tecnológico base.

### 📦 Output Esperado

- Documento de diseño en `04_Docs/plans/`.
- 2-3 alternativas con trade-offs presentadas.
- Roadmap de implementación de alto nivel aprobado.

### 🚫 Limitaciones

- **No escribe código de producción.**
- No toma decisiones finales sin validación incremental.
- Se limita a la fase conceptual y arquitectónica.

## When to use this skill

- When starting a new feature or component.
- When the user's request is vague or high-level.
- Before writing any code for a complex task.
- When you need to understand user intent, requirements, or constraints.

## Workflow

1.  **Understand Context:** Review project state (files, docs).
2.  **Refine Idea:** Ask single, focused questions (prefer multiple choice).
3.  **Explore Approaches:** Propose 2-3 options with trade-offs.
4.  **Present Design:** Break down the solution into small, validatable sections (200-300 words).
5.  **Document:** Save validated design to `04_Docs/plans/`.

## Instructions

### 1. Understanding the Idea

- Check out the current project state first (files, docs, recent commits).
- Ask questions **one at a time** to refine the idea.
- Prefer **multiple choice questions** when possible, but open-ended is fine too.
- **Only one question per message** - if a topic needs more exploration, break it into multiple questions.
- Focus on understanding: purpose, constraints, success criteria.

### 2. Exploring Approaches

- Propose **2-3 different approaches** with trade-offs.
- Present options conversationally with your recommendation and reasoning.
- Lead with your recommended option and explain why.

### 3. Presenting the Design

- Once you believe you understand what you're building, present the design.
- **Break it into sections** of 200-300 words.
- **Ask after each section** whether it looks right so far.
- Cover: architecture, components, data flow, error handling, testing.
- Be ready to go back and clarify if something doesn't make sense.

### 4. Documentation

- Write the validated design to `04_Docs/plans/YYYY-MM-DD-<topic>-design.md`.
- Commit the design document to git.

### 5. Transition to Implementation

- Ask: "Ready to set up for implementation?"
- If yes, proceed to create a detailed implementation plan (using `planning` skill if available).

## Key Principles

- **One question at a time** - Don't overwhelm with multiple questions.
- **Multiple choice preferred** - Easier to answer than open-ended when possible.
- **YAGNI ruthlessly** - Remove unnecessary features from all designs.
- **Explore alternatives** - Always propose 2-3 approaches before settling.
- **Incremental validation** - Present design in sections, validate each.
- **Be flexible** - Go back and clarify when something doesn't make sense.
