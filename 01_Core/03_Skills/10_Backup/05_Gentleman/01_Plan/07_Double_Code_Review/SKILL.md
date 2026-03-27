---
name: double-code-review
description: Doble Code Review estilo Silicon Valley desde múltiples perspectivas. Triggers on: double review, code review, six hats, revisión completa, plan review, quality check.
---

# Double Code Review — Silicon Valley Protocol

## Esencia Original
> **Propósito:** Revisión profunda de planes y código desde 6 perspectivas (sombreros) + verificación de cumplimiento.
> **Flujo:** Planning check → 6 Sombreros review → Verification → Lessons learned

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Hacer un solo review
  - **Por qué**: Sesgo único, se colan errores
  - **Solución**: SIEMPRE doble review — planning + execution

- **[ERROR]**: No seguir las 6 perspectivas
  - **Por qué**: Se pierden ángulos importantes
  - **Solución**: Seguir Information🔵, Emotions🔴, Benefits🟡, Risks🟢, Meta🟣, Process⚪

- **[ERROR]**: Review sin action items
  - **Por qué**: Se revisa pero no se corrige
  - **Solución**: Siempre terminar con checklist de acciones

## 📁 Progressive Disclosure

> Para información detallada:
- [references/hat-review.md](references/hat-review.md) — Guía de los 6 sombreros
- [references/verification-template.md](references/verification-template.md) — Template de verificación

## 🛠️ Scripts

- [scripts/run-review.py](scripts/run-review.py) — Ejecuta review estructurado

## 💾 State Persistence

Guardar reviews en:
- `01_Brain/07_Memory_Brain/00_Code_Reviews/`
- `01_Core/02_Evals/`

## PURPOSE

Implementar el **Doble Code Review** estilo Silicon Valley. Después de crear cualquier plan, se hace una revisión profunda desde múltiples ópticas con "sombreros" (perspectivas), buscando edge cases, inconsistencias y gaps. El segundo review verifica si lo planificado se cumplió y qué falta.

---

## FILOSOFÍA

> "Trust but verify. Y si no verificaste dos veces, no verificaste nada." — Principios Think Different

El doble review no es paranoia, es **profesionalismo de élite**. Silicon Valley companies hacen esto porque funciona.

---

## STRUCTURE: 3 PHASES

### FASE 1: PLANNING (Pre-Review)

Ya existe el plan. Antes de revisar, asegurar que:

- [ ] Plan tiene objetivos claros y medibles
- [ ] Plan tiene scope definido
- [ ] Plan tiene dependencias identificadas
- [ ] Plan tiene success criteria explícitos
- [ ] Plan tiene timeline/orden de ejecución

### FASE 2: FIRST REVIEW — The Hat Review (6 Sombreros)

**Reviewer 1** usa 6 sombreros (metáforas de Edward de Bono):

| Sombrero | Color | Pregunta | Foco |
|----------|-------|----------|------|
| **Information** | 🔵 Azul | ¿Qué sabemos? | Facts, data, información disponible |
| **Emotions** | 🔴 Rojo | ¿Cómo nos sentimos? | Intuitión, emociones, gut feeling |
| **Caution** | 🟡 Amarillo | ¿Qué podría salir bien? | Beneficios, oportunidades, optimismos |
| **Caution** | 🟢 Verde | ¿Qué puede salir mal? | Peligros, risks, problemas potenciales |
| **Creation** | 🟣 Púrpura | ¿Qué es esto realmente? | Meta-view, qué estamos haciendo, big picture |
| **Process** | ⚪ Blanco | ¿Cómo llegamos aquí? | Proceso, metodología, paso a paso |

#### Checklist por Sombrero:

**🔵 SOMBRERO AZUL — Information**
```
□ ¿Tenemos todos los facts necesarios?
□ ¿Qué información nos falta?
□ ¿Hay datos contradictorios?
□ ¿La información es source-of-truth o rumor?
□ ¿Qué sabemos vs qué asumimos?
```

**🔴 SOMBRERO ROJO — Emotions**
```
□ ¿Cómo me siento sobre este plan?
□ ¿Mi intuición dice que va a funcionar?
□ ¿Hay algo que "no me cierra"?
□ ¿Estoy siendo realista o optimistics en exceso?
□ ¿Mis emociones están sesgando mi juicio?
```

**🟡 SOMBRERO AMARILLO — Benefits**
```
□ ¿Qué beneficios trae este plan?
□ ¿Qué oportunidades aprovecha?
□ ¿Cómo mejora la situación actual?
□ ¿Qué stakeholder se beneficia?
□ ¿Cuál es el ROI/valor de hacer esto?
```

**🟢 SOMBRERO VERDE — Risks**
```
□ ¿Qué puede salir mal?
□ ¿Cuáles son los edge cases obvios?
□ ¿Qué pasa si X no existe?
□ ¿Qué pasa si la dependency falla?
□ ¿Qué pasa con casos límite (empty, null, huge)?
□ ¿Qué risks tenemos si no hacemos esto?
□ ¿Cuáles son los failure modes?
```

**🟣 SOMBRERO PÚRPURA — Meta**
```
□ ¿Qué estamos haciendo realmente?
□ ¿Por qué estamos haciendo esto?
□ ¿Esto se alinea con los goals del proyecto?
□ ¿Hay otra forma más simple de lograr lo mismo?
□ ¿Estamos resolviendo el problema correcto?
□ ¿Esto escala o es un workaround temporal?
```

**⚪ SOMBRERO BLANCO — Process**
```
□ ¿El proceso de creación del plan fue sólido?
□ ¿Seguimos la metodología correcta?
□ ¿Qué steps nos faltan en el proceso?
□ ¿Hay gaps en el workflow?
□ ¿Estamos siguiendo los estándares del proyecto?
```

### FASE 3: SECOND REVIEW — Verification Check

**Reviewer 2** (o una iteración más profunda) verifica:

#### 3A: Execution Verification
```
□ ¿El plan fue ejecutado según lo escrito?
□ ¿Qué se desvió del plan original?
□ ¿Las desviaciones fueron documentadas?
□ ¿Se cumplieron los success criteria?
□ ¿El timeline se respetó?
```

#### 3B: Completeness Check
```
□ ¿Qué se hizo vs qué se planeó?
□ ¿Qué se dejó de hacer y por qué?
□ ¿Hay tasks pendientes arrastradas?
□ ¿Hay blockers sin resolver?
□ ¿Qué necesita hacerse después?
```

#### 3C: Quality Check
```
□ ¿El código resultante sigue los estándares?
□ ¿Hay debt técnico acumulado?
□ ¿Los tests pasaron?
□ ¿La documentación está actualizada?
□ ¿Los commits son atómicos y bien descriptos?
```

#### 3D: Lessons Learned
```
□ ¿Qué aprendimos haciendo esto?
□ ¿Qué haríamos diferente?
□ ¿Qué patrones establecimos?
□ ¿Qué debe documentarse para el futuro?
```

---

## OUTPUT DEL DOUBLE REVIEW

El review genera un documento estructurado:

```markdown
# Double Code Review Report
## Plan: [Nombre del Plan]
## Fecha: YYYY-MM-DD
## Reviewers: [Nombres/Roles]

---

## FASE 1: Planning Status
[Checklist de planificación]

## FASE 2: First Review — Hat Analysis

### 🔵 Sombrero Azul
[Hallazgos de información]

### 🔴 Sombrero Rojo  
[Hallazgos emocionales/intuitivos]

### 🟡 Sombrero Amarillo
[Beneficios identificados]

### 🟢 Sombrero Verde
[Risks y edge cases]

### 🟣 Sombrero Púrpura
[Meta-análisis]

### ⚪ Sombrero Blanco
[Análisis de proceso]

## FASE 3: Second Review — Verification

### 3A: Execution
[Verificación de ejecución]

### 3B: Completeness
[Qué se hizo vs qué se debía hacer]

### 3C: Quality
[Verificación de calidad]

### 3D: Lessons Learned
[Aprendizajes]

---

## VERDICT

| Aspecto | Status | Notes |
|---------|--------|-------|
| Planificación | ✅/⚠️/❌ | |
| Ejecución | ✅/⚠️/❌ | |
| Completitud | ✅/⚠️/❌ | |
| Calidad | ✅/⚠️/❌ | |

## RECOMMENDATIONS

1. [Recomendación prioritaria]
2. [Recomendación secundaria]
3. ...

## NEXT STEPS

- [ ] [Acción inmediata]
- [ ] [Acción para sig sprint]
- [ ] ...

---
```

---

## TRIGGERS — Cuándo usar esta skill

| Trigger | Descripción |
|---------|-------------|
| Plan creado | Después de crear cualquier plan (01_Plan/, 04_Docs/plans/) |
| Sprint review | Al cerrar un sprint o fase de trabajo |
| Pre-commit | Antes de commit final de una feature |
| Post-mortem | Después de incidentes o problemas |
| Sesión cierra | Al terminar sesión significativa |
| Code review | Cualquier revisión de código mayor |

---

## INTEGRACIÓN CON OTROS SKILLS

| Skill | Relación |
|-------|----------|
| `systematic-debugging` | Se usa ANTES si hay bugs activos |
| `verification-before-completion` | Complemento — verifica output |
| `test-driven-development` | Si hay bugs, aplica TDD post-review |
| `edge-case-skill` | Alimenta el 🟢 Sombrero Verde |

---

## ANTI-PATTERNS — Qué NO hacer

❌ **No saltarse hats** — cada sombrero existe por una razón  
❌ **No unificar perspectives** — el punto es ver desde ángulos distintos  
❌ **No rush** — el review rápido es review malo  
❌ **No solo negative** — el 🟡 Sombrero Amarillo es crítico  
❌ **No skip verification** — el segundo review NO es opcional  

---

## EJEMPLO DE USO

```bash
# Al terminar una sesión o plan:
# "Ejecutá el double code review de esta sesión"
```

El sistema:
1. Cargará este skill
2. Aplicará los 6 sombreros
3. Verificará ejecución
4. Generará el report
5. Guardará en 01_Brain/07_Memory_Brain/00_Code_Reviews/

---

## SAVED ARTIFACTS

Los reports se guardan en:
```
01_Brain/07_Memory_Brain/00_Code_Reviews/
├── YYYY-MM-DD_[plan-name]_review.md
└── index.md  (índice de todos los reviews)
```

---

**© 2026 Think Different AI System — Silicon Valley Protocol v1.0**
