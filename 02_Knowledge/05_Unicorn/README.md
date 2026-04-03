# 05_Unicorn — Unicorn Engineering Knowledge Base

**Versión:** 1.1  
**Fecha:** 2026-04-03  
**Estado:** ✅ Construido

---

## Propósito

Almacenar TODO el conocimiento SOTA de las 6 áreas del Unicorn Engineering para que el OS evolucione automáticamente con contexto de nivel Silicon Valley.

---

## Las 6 Áreas

| # | Área | Descripción |
|---|------|-------------|
| 1 | **01_Pm** | Project Management - Delivery, timeline, recursos |
| 2 | **02_Pdm** | Product Management - Estrategia, users, metrics |
| 3 | **03_Product_Design** | Product Design - UX, wireframes, Design Sprint |
| 4 | **04_Art_Director** | Art Director - Visual, branding, design system |
| 5 | **05_Aipm** | AI Product Manager - AI, prompts, agents |
| 6 | **06_Engineering** | Engineering - Full-stack, arquitectura, código |

---

## Estructura por Área

Cada área tiene:

```
{area}/
├── decisions/    # Decisiones importantes tomadas
├── lessons/      # Lecciones aprendidas
├── patterns/     # Patterns SOTA del área
├── [sub área]    # Subcarpetas específicas
```

---

## Template Estándar

```markdown
---
type: {decision|lesson|pattern}
area: {pm|pdm|product_design|art|aipm|engineering}
date: 2026-04-03
status: {active|deprecated}
---

## Título

### Contexto
[Qué estaba pasando]

### Qué ocurrió / Decisión
[Detalle]

### Por qué
[Reasoning]

### Aplicación
[Cómo aplicamos]

### Tags
[area, metodologia, contexto]
```

---

## Cómo Contribuir

1. **Cada decisión importante** → `decisions/`
2. **Cada lección aprendida** → `lessons/`
3. **Cada pattern SOTA** → `patterns/`
4. **Guardar en Engram** → con topic_key `unicorn/{area}`

---

## Metodologías SOTA por Área

### 01_PM (Project Management)
- Hybrid Agile-Waterfall, Agile 3.0 + OKR Integration
- Flow-Based Project Management, Spotify Model
- Linear, Height, Zenhub, ClickUp 3.0

### 02_PdM (Product Management)
- Continuous Discovery + OKRs, Product-Led Growth
- HEART Metrics (Google), AARRR Pirate Metrics, RICE Scoring
- Jobs-to-Be-Done (JTBD), AI-assisted discovery

### 03_Product_Design
- Design Sprint, Double Diamond, Lean UX
- JTBD, Design System 4.0, UX Research

### 04_Art_Director
- AI Creative Direction, Data-Driven Emotional Design
- Design System 4.0, Brand Coherence Framework
- Neo-Brutalism + Soft UI, Motion-first design

### 05_AIPM (AI Product Manager)
- Agent Orchestration, Prompt Patterns (10+)
- Skills System, HITL, Context Engineering
- ML Fundamentals, Ethical AI Frameworks

### 06_Engineering
- Agentic Coding, Context Engineering
- Serverless + Edge, RSC, Micro-frontends
- TypeScript Strict, React 19 + Signals, Tailwind 4

---

*Unicorn Engineering - Conocimiento nivel Silicon Valley*