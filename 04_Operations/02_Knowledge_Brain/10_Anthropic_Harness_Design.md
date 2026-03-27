# Harness Design for Long-Running Application Development

**Fuente:** [Anthropic Engineering](https://www.anthropic.com/engineering/harness-design-long-running-apps)
**Autor:** Prithvi Rajasekaran (Anthropic Labs)
**Fecha:** March 24, 2026
**Tags:** #harness #agent-design #anthropic #long-running-agents #adversarial-evaluation

---

## Resumen Ejecutivo

Artículo que describe cómo Anthropic construyó un sistema de tres agentes (Planner, Generator, Evaluator) para desarrollo autónomo de aplicaciones completas. El patrón adversarial evaluation (inspirado en GANs) mejora sustancialmente la calidad del output.

---

## Problema: Dos Failure Modes

### 1. Context Anxiety
- Modelos acortan trabajo prematuramente cuando el contexto se llena
- Solución: Context reset (Sonnet 4.5) vs Context compaction (Opus 4.6)

### 2. Self-Evaluation Problem
- Agentes tienden a aprobar su propio trabajo (inclusive cuando es mediocre)
- Solución: QA agent separado del generator

---

## Three-Agent Architecture

| Agente        | Rol                            | Output          |
|---------------|--------------------------------|-----------------|
| **Planner**   | 1-4 oraciones → spec completo  | 16-feature spec |
| **Generator** | Feature por feature (sprints)  | Código          |
| **Evaluator** | QA separado con Playwright MCP | Bugs + grading  |

---

## Criterios de Evaluación (Frontend Design)

| Criterio           | Descripción                             | Peso    |
|--------------------|-----------------------------------------|---------|
| **Design Quality** | Coherencia visual, mood, identidad      | 🔴 ALTO  |
| **Originalidad**   | Custom vs AI slop patterns              | 🔴 ALTO  |
| **Craft**          | Ejecución técnica (typography, spacing) | default |
| **Funcionalidad**  | Usabilidad, tareas completas            | default |

### Peso Aplicado
- Design quality y Originalidad > Craft y Funcionalidad
- Reason: Claude ya es bueno en lo técnico, falla en estética

---

## Resultados Experimentales

### Retro Game Maker
| Harness    | Duration    | Cost   | Result        |
|------------|-------------|--------|---------------|
| Solo       | 20 min      | $9     | App rotas     |
| Full       | 6 hr        | $200   | App funcional |

### Digital Audio Workstation (DAW)
| Phase     | Duration        | Cost        |
|-----------|-----------------|-------------|
| Planner   | 4.7 min         | $0.46       |
| Build R1  | 2 hr 7 min      | $71.08      |
| QA R1     | 8.8 min         | $3.24       |
| Build R2  | 1 hr 2 min      | $36.89      |
| QA R2     | 6.8 min         | $3.09       |
| Build R3  | 10.9 min        | $5.88       |
| QA R3     | 9.6 min         | $4.06       |
| **Total** | **3 hr 50 min** | **$124.70** |

---

## Context Reset vs Compaction

| Método         | Descripción                                | Cuándo Usar                  |
|----------------|--------------------------------------------|------------------------------|
| **Reset**      | Limpia ventana completamente, nuevo agente | Sonnet 4.5 (context anxiety) |
| **Compaction** | Resume misma sesión, historia acortada     | Opus 4.6+                    |

### Hallazgo
- Opus 4.6 NO necesita context reset, solo compaction
- "The better the models get, the more space there is to develop harnesses"

---

## Adversarial Evaluation Pattern

### Cómo Funciona
```
[User Prompt] → [Generator] → [Output]
                              ↓
                    [Evaluator with Playwright MCP]
                              ↓
                     [Feedback] → [Generator]
```

### Por Qué Funciona
1. Separación: Generator ≠ Evaluator
2. Interacción: Evaluador debe USAR la app (no solo leer código)
3. Criterios gradables: "Es hermoso?" → "Sigue principios de diseño?"

### Tuning del Evaluator
- Out of the box, Claude es MALO como QA
- Necesita múltiples iteraciones
- Ejemplos: encontrar casos donde su juicio diverge del humano y ajustar el prompt

---

## Sprint Contract

### Definición
Antes de cada sprint, generator + evaluator negocian "done":
- Generator propone qué construirá
- Evaluator revisa que sea correcto
- Iteran hasta agreement

### Por Qué
- El spec es alto nivel, hay gap con implementación
- Evita que el generator "mueva el goalpost"
- Define criteria verificables ANTES de escribir código

---

## Ejemplo: Contract Criterion

| Criterion                                 | Evaluator Finding                                               |
|-------------------------------------------|-----------------------------------------------------------------|
| Rectangle fill tool allows click-drag     | **FAIL** - only places tiles at start/end, not filling region   |
| User can select and delete spawn points   | **FAIL** - handler requires both selection AND selectedEntityId |
| User can reorder animation frames via API | **FAIL** - route defined after `/{frame_id}`, returns 422       |

---

## Harness Evolution Principle

> "Every component in a harness encodes an assumption about what the model can't do on its own, and those assumptions are worth stress testing, because they may be incorrect, and they can quickly go stale as models improve."

### Implicaciones
- Cuando sale nuevo modelo → re-examinar harness
- Quitar componentes que ya no son load-bearing
- Agregar nuevos para mayor capability

### Con Opus 4.6
- Se pudo REMOVER: sprints, context reset
- Se mantuvo: planner + evaluator
- "Find the simplest solution possible, and only increase complexity when needed"

---

## Lessons Learned

1. **Para tareas difíciles**: Necesitás evaluator
2. **Para tareas easy**: No necesitás evaluator
3. **El evaluator debe INTERACTUAR** con el output (Playwright MCP)
4. **Criterios deben ser gradables** (no subjetivos)
5. **Simplificar cuando el modelo mejora**

---

## Aplicación a Our System

### Perfiles de Agentes
Los 5 perfiles creados ya tienen estructura base. Agregar:

1. **QA Agent separado** para tareas complejas
2. **Sprint contract** para features grandes
3. **Playwright integration** para testing visual
4. **Progressive disclosure** de complexity según modelo

### Skills Related
- `.agent/02_Skills/06_Testing/E2E_Testing/` - Playwright
- `.agent/02_Skills/06_Testing/Integration_Testing/`
- `.agent/02_Skills/06_Testing/Test_Coverage/`

---

## Referencias

- [Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (Nov 2024)
- [Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
- [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Frontend Design Skill](https://github.com/anthropics/claude-code/blob/main/plugins/frontend-design/skills/frontend-design/SKILL.md)
- Claude Agent SDK

---

*Documentado: 2026-03-26*
