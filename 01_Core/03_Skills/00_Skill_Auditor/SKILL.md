---
name: skill-auditor
description: Audit and validate skills against Anthropic SOTA standards. Triggers on: audit skills, validate skills, check skills quality, skill review, skill health check, skill compliance, audit skill structure.
---

# Skill Auditor

> **Level**: System Critical — Quality Guardian

Audita skills contra los estándares **Anthropic SOTA v5.1** + **Skill Creator v2.0** de PersonalOS.

---

## When to Use This Skill

- Después de crear/modificar una skill
- Revisión semanal de skills
- Antes de hacer commit
- Cuando una skill no funciona
- Para auditar skills antes de集成 al OS
- Verificar compliance con estándares PersonalOS

---

## Esencia Original

> **Metaskill**: La skill que audita otras skills para asegurar calidad, consistencia y estándares Anthropic.

Esta skill es el **guardián de calidad** del PersonalOS. Sin ella, skills de baja calidad degradan la experiencia del usuario y del agente.

---

## 📊 Criterios de Auditoría (SOTA v5.1)

### 1. YAML Frontmatter (REQUIRED)

| Campo | Requisito | Validación |
|-------|-----------|------------|
| `name` | Max 64 chars, lowercase, números, guiones | Regex: `^[a-z0-9-]+$` |
| `name` | Formato gerund (verb + -ing) | Ej: `processing-pdfs`, `onboarding-agent` |
| `name` | PROHIBIDO: "claude", "anthropic" | No puede contener estas palabras |
| `description` | Max 1024 caracteres | Longitud válida |
| `description` | Debe incluir triggers semánticos | "triggers on:" presente |

### 2. Progressive Disclosure

| Criterio | Límite | Notas |
|----------|--------|-------|
| SKILL.md líneas | < 200 ideal, < 500 max | Contar líneas reales |
| references/ existe | Requerido si SKILL.md > 200 líneas | Para docs pesadas |
| scripts/ existe | Opcional | Si hay código reutilizable |
| assets/ existe | Opcional | Si hay templates |

### 3. Gotchas Section (REQUIRED)

| Criterio | Requisito |
|----------|-----------|
| Sección presente | "## ⚠️ Gotchas" o "## Gotchas" |
| Mínimo errors | 3 errores documentados |
| Estructura | Cada gotcha tiene "Por qué" + "Solución" |
| Específicos | No genéricos, específicos a esta skill |

### 4. Esencia Original (REQUIRED)

| Criterio | Requisito |
|----------|-----------|
| Sección presente | "## Esencia Original" |
| Propósito claro | Define el propósito original de la skill |
| Metaskill documentada | Explica qué problema resuelve |

### 5. State Persistence (RECOMMENDED)

| Criterio | Requisito |
|----------|-----------|
| Mentioned | Referencia a dónde guardar estado |
| Location específica | `${CLAUDE_PLUGIN_DATA}` o ruta válida |

### 6. v2.0 Features (OPTIONAL para SOTA)

| Feature | Cuando aplica |
|---------|---------------|
| evals.json | Skills que usan Skill Creator v2.0 |
| Benchmark results | Skills críticas del OS |
| agents/ folder | Si tiene subagentes |

---

## 🚨 Errores Comunes a Evitar

### ERROR 1: Description Marketing
- **Por qué**: No le dice al modelo cuándo activar la skill
- **Solución**: Incluir triggers semánticos: `triggers on: keyword1, keyword2`

### ERROR 2: SKILL.md Excesivo
- **Por qué**: Satura el context window, peor rendimiento
- **Solución**: Usar `references/` para docs > 200 líneas

### ERROR 3: Sin Gotchas
- **Por qué**: La skill no aprende de errores previos
- **Solución**: Documentar mínimo 3 errores con "Por qué" y "Solución"

### ERROR 4: Gotchas Genéricas
- **Por qué**: Errores como "don't make mistakes" no aportan valor
- **Solución**: Ser específico: "Don't skip error handling in API calls"

### ERROR 5: name con Mayúsculas
- **Por qué**: Rompe YAML parsing en algunos sistemas
- **Solución**: Usar siempre lowercase: `skill-name`, no `SkillName`

### ERROR 6: Sin Esencia Original
- **Por qué**: Sin ella, la skill pierde su propósito original
- **Solución**: Documentar "## Esencia Original" al inicio

---

## 📁 Progressive Disclosure

> Para información detallada:

- [references/audit-criteria.md](references/audit-criteria.md) — Checklist completo de auditoría
- [references/anthropic-standards.md](references/anthropic-standards.md) — Estándares Anthropic originales
- [08_Skill_Creation_SOTA.md](../08_Skill_Creation_SOTA/SKILL.md) — Documento SOTA v5.1

---

## 🛠️ Scripts de Auditoría

| Script | Propósito |
|--------|-----------|
| [scripts/audit-skills.py](scripts/audit-skills.py) | Analiza todas las skills en un directorio |
| [scripts/validate-essence.py](scripts/validate-essence.py) | Verifica esencia original preservada |
| [scripts/fix-missing.py](scripts/fix-missing.py) | Corrige archivos faltantes automáticamente |

---

## Flujo de Auditoría

```
1. EJECUTAR: audit-skills.py → Analizar todas las skills
2. REVISAR: Ver PASS/FAIL de cada criterio
3. VALIDAR: validate-essence.py → Verificar esencia preservada
4. CORREGIR: fix-missing.py → Crear archivos faltantes
5. VERIFICAR: Probar scripts y evals
6. SCORE: Calcular rating final (90%+ = Excellent)
```

---

## 📊 Output Format

```
📋 AUDIT REPORT: [skill-name]

✅ PASS (8):
- YAML frontmatter (name, description, triggers)
- Gotchas section (3+ errors)
- Progressive disclosure (< 200 líneas)
- References folder exists
- Scripts folder exists
- Esencia Original section
- State Persistence mentioned

❌ FAIL (2):
- evals.json missing (v2.0 recommendation)

📊 SUMMARY:
Total checks: 10
Passed: 8
Failed: 2
Score: 80% — Good (Needs minor improvements)
```

---

## State Persistence

Reportes de auditoría se guardan en:
- `${CLAUDE_PLUGIN_DATA}/skill-auditor/reports/`
- O en `reports/` local de la skill

---

## Scoring

| Score | Rating | Acción |
|-------|--------|--------|
| 90-100% | ✅ Excellent | Ready for production |
| 70-89% | 👍 Good | Minor improvements needed |
| 50-69% | ⚠️ Needs Work | Significant fixes required |
| <50% | ❌ Failed | Do not integrate |

---

*Skill Version: 2.0*
*Framework: Anthropic Skill Creator v2.0 + PersonalOS SOTA v5.1*
*Last Updated: 2026-03-27*
