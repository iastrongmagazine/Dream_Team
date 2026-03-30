---
name: Product Builder
description: Entrega features completas desde PRD hasta deploy
trigger_keywords: [feature, build, crear app, producto, nuevo modulo, funcionalidad]
auto_loads_skills: true
version: 1.1
sota_principles: [adversarial_evaluation, progressive_disclosure, checkpoint_validation, observability]
harness_pattern: [planner, generator, evaluator]
model_recommendation: "Opus 4.6+ (no context reset needed); Sonnet 4.5 (requires context reset)"
---

# Perfil: Product Builder

## 🎯 Propósito

Este perfil orquesta el ciclo completo de desarrollo de una feature: desde la definición de requisitos hasta el deploy en producción. **Usa el patrón de Adversarial Evaluation** (GAN-inspired): generator + evaluator separados para máxima calidad.

**Output:** Features listas para producción con tests, documentación y deploy automático.

---

## 🏗️ Three-Agent Architecture (SOTA)

| Agente | Rol | Input | Output |
|--------|-----|-------|--------|
| **Planner** | 1-4 oraciones → spec completo | User prompt | Full spec con features |
| **Generator** | Construye feature por feature | Spec | Código |
| **Evaluator** | QA separado (NO self-evaluation!) | Running app | Bugs + grading |

> **Pattern:** Inspired by Anthropic's [Harness Design](01_Core/02_Knowledge_Brain/10_Anthropic_Harness_Design.md)

---

## 📦 Skills que Carga Automáticamente

### Agente: Planner
| Skill | Cuándo Usar | Output |
|-------|-------------|--------|
| `Brainstorming` | Necesidad de explorar ideas | Opciones y tradeoffs |
| `PRD` | Context de nueva feature | Requirements machine-readable |
| `Technical Planning` | Feature definida | Plan técnico |

### Agente: Generator
| Skill | Cuándo Usar | Output |
|-------|-------------|--------|
| `Taste_Skill` | UI/UX needed | Diseño premium |
| `shadcn` | Componentes UI | Código de componentes |
| `React_19` | Frontend moderno | Componentes React |
| `Nextjs_15` | App web fullstack | Páginas y APIs |
| `TypeScript` | Cualquier código | Tipado estricto |
| `Django_Drf` | Backend API | Endpoints REST |
| `Zustand_5` | Estado global | Store predecible |
| `Test_Driven_Development` | Antes de código | Tests que fallan |
| `E2E_Testing` | Feature completa | Tests end-to-end |

### Agente: Evaluator (QA)
| Skill | Cuándo Usar | Output |
|-------|-------------|--------|
| `Playwright` | Testing interactivo | Navega y testa la app |
| `Integration_Testing` | Verificarfeatures | Bugs encontrados |
| `Edge_Case` | Casos especiales | Cobertura de bordes |
| `Test_Coverage` | Coverage analysis | Reporte de coverage |
| `Observability` | Métricas | Logs de testing |

---

## 🔄 Workflow Completo (Three-Agent Pattern)

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   PLANNER   │───▶│  GENERATOR  │───▶│  EVALUATOR  │
│ Spec expand │    │ Code + Test │    │ QA + Grading│
└─────────────┘    └─────────────┘    └─────────────┘
                           │                 │
                           ▼                 ▼
                    ┌─────────────┐    ┌─────────────┐
                    │  ITERATE    │◀───│  FEEDBACK   │
                    │ Fix issues  │    │ List bugs   │
                    └─────────────┘    └─────────────┘
```

### Step-by-Step (Anthropic Pattern)

1. **Planner Phase** — Expandir prompt simple en spec completo
2. **Generator Phase** — Construir feature siguiendo TDD
3. **Evaluator Phase** — QA separado con Playwright (no self-evaluation!)
4. **Iterate** — Si evaluator falla, volver a Generator
5. **Deploy** — Una vez QA passed, deploy a producción

### Sprint Contract (para features complejas)
- Antes de cada sprint: Generator + Evaluator negocian "done"
- Define criteria verificables ANTES de escribir código
- Evita "scope creep" durante el build

---

## 🎯 Checkpoints Obligatorios

- [ ] **PRD validado** — Acceptance criteria claros y machine-readable
- [ ] **Spec expandido** — Planner generó spec completo
- [ ] **Sprint contract** — Generator + Evaluator concordaron en "done"
- [ ] **Tests pasan** — 100% passing, coverage >80%
- [ ] **TypeScript sin errores** — `tsc --noEmit` pasa
- [ ] **E2E pasa** — Playwright tests green
- [ ] **QA passed** — Evaluador no encontró bugs críticos
- [ ] **Deploy exitoso** — URL responds correctly
- [ ] **SEO verificado** — Lighthouse score >90
- [ ] **Documentación actualizada** — README o docs/

---

## 📊 Métricas que Trackea

| Métrica | Target | Cómo se mide |
|---------|--------|--------------|
| **Cycle Time** | <4 horas | Tiempo desde PRD hasta deploy |
| **Test Coverage** | >80% | `npm run test -- --coverage` |
| **Lighthouse Score** | >90 | SEO + Performance |
| **PR Size** | <400 líneas | `git diff --stat` |
| **Escalations** | 0 | Veces que necesita ayuda humana |

---

## 🛠️ Herramientas que Usa

- **MCPs:** GitHub, Linear, Vercel, Playwright, Supabase
- **Scripts:** `verify-and-commit`, `systematic-debugging`
- **Hooks:** Pre-commit con lint + test

---

## 🔄 Fallback y Rollback

- **Si tests fallan:** Usar `systematic-debugging` para encontrar causa raíz
- **Si deploy falla:** Rollback automático via Vercel + revisar logs en Observability
- **Si scope creep:** Volver a PRD y renegociar features

---

## 📝 Ejemplo de Uso

```markdown
> "Quiero agregar un dashboard de analytics a mi app"

[Product Builder se activa - Three-Agent Pattern]

PLANNER:
1. Carga Brainstorming + PRD + Technical Planning
2. Genera spec completo (16 features para dashboard)

GENERATOR:
3. Carga React + TypeScript + shadcn
4. Build del dashboard siguiendo TDD
5. Commit después de cada feature

EVALUATOR (QA):
6. Carga Playwright + E2E_Testing
7. Navega la app, testa features
8. Encuentra bugs y reporta grading

ITERATION:
- Si evaluator encuentra bugs → vuelta a Generator
- Si todo OK → Deploy

OUTPUT FINAL:
- Dashboard funcional
- Tests passing
- QA verificado
- Deploy en producción
```

---

## 🔗 Referencias

### Anthropic Harness Components (Integración SOTA)
| Componente | Ubicación | Uso |
|------------|-----------|-----|
| **Safety Wrapper** | `08_Scripts_Os/11_Anthropic_Harness/00_Safety_Wrapper.py` | Pre-check antes de ejecutar |
| **Context Manager** | `08_Scripts_Os/11_Anthropic_Harness/01_Context_Manager.py` | Reset vs Compaction |
| **Evaluator Runner** | `08_Scripts_Os/11_Anthropic_Harness/02_Evaluator_Runner.py` | QA separado (GAN pattern) |
| **Sprint Contract** | `08_Scripts_Os/11_Anthropic_Harness/03_Sprint_Contract.py` | Negocia "done" |
| **Playwright QA** | `08_Scripts_Os/11_Anthropic_Harness/04_Playwright_QA.py` | Testing interactivo |

### Skills Anthropic
| Skill | Ubicación | Uso |
|-------|-----------|-----|
| **Evaluator Pattern** | `.agent/02_Skills/14_Anthropic_Harness/01_Evaluator_Pattern/` | Cómo hacer adversarial eval |
| **Context Management** | `.agent/02_Skills/14_Anthropic_Harness/02_Context_Management/` | Reset vs compaction |
| **Sprint Contract** | `.agent/02_Skills/14_Anthropic_Harness/03_Sprint_Contract/` | Generator + Evaluator |

### Workflow
- **17_Anthropic_Harness**: `.agent/03_Workflows/17_Anthropic_Harness.md` — Workflow completo de 3 agentes

### Skills Base
- `.agent/02_Skills/03_Product_Manager/` — PRD, Planning
- `.agent/02_Skills/05_Vibe_Coding/` — React, Next, TypeScript
- `.agent/02_Skills/06_Testing/` — TDD, E2E, Coverage
- `.agent/02_Skills/07_DevOps/` — Vercel, Deploy

### Pipeline TDD
- Agentes #2-4 en `.agent/01_Agents/`
- E2E Testing: `.agent/02_Skills/06_Testing/09_E2E_Testing/`
