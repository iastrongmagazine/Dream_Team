---
name: skill-auditor
description: Audit and validate skills against Anthropic standards. Triggers on: audit skills, validate skills, check skills, skill review, analyze skills quality, skill health check.
---

# Skill Auditor

> Analiza, valida y corrige skills contra los estándares Anthropic.

## Esencia Original
> Metaskill: La skill que audit otras skills para asegurar calidad, consistencia y estándares.

## 🎯 Objetivo

Auditar las skills del Project Manager para verificar:
- Cumplimiento de estándares Anthropic
- Preservación de esencia original
- Scripts funcionando
- Estructura correcta

## When to Use

- Después de crear/modificar una skill
- Revisión semanal de skills
- Antes de hacer commit
- Cuando una skill no funciona

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: No verificar triggers semánticos
  - **Por qué**: Description debe tener keywords que el usuario usa
  - **Solución**: Usar triggers como "morning routine", "weekly review"

- **[ERROR]**: No verificar Gotchas
  - **Por qué**: Sin Gotchas, la skill no aprende de errores
  - **Solución**: Mínimo 3 errores documentados

- **[ERROR]**: No verificar Progressive Disclosure
  - **Por qué**: SKILL.md no debe tener más de 200 líneas
  - **Solución**: Usar references/ para docs pesadas

- **[ERROR]**: No probar scripts
  - **Por qué**: Scripts pueden tener errores
  - **Solución**: Ejecutar scripts antes de commit

- **[ERROR]**: No verificar esencia original
  - **Por qué**: Cada skill tiene un propósito original
  - **Solución**: Documentar "Esencia Original" en SKILL.md

---

## 📁 Progressive Disclosure

> Para información detallada:
- [references/audit-criteria.md](references/audit-criteria.md) — Checklist de auditoría
- [references/anthropic-standards.md](references/anthropic-standards.md) — Estándares Anthropic

---

## 🛠️ Scripts

- [scripts/audit-skills.py](scripts/audit-skills.py) — Analiza todas las skills
- [scripts/validate-essence.py](scripts/validate-essence.py) — Verifica esencia original
- [scripts/fix-missing.py](scripts/fix-missing.py) — Corrige archivos faltantes

---

## 📋 Flujo de Auditoría

1. **Ejecutar `audit-skills.py`** → Analizar todas las skills
2. **Revisar resultados** → Ver PASS/FAIL de cada criteria
3. **Ejecutar `validate-essence.py`** → Verificar esencia preservada
4. **Ejecutar `fix-missing.py`** → Crear archivos faltantes
5. **Probar scripts** → Verificar que funcionan

---

## 📊 Output Format

```
📋 AUDIT REPORT

✅ PASS (8):
- Description triggers
- Gotchas section
- Progressive disclosure
- Scripts exist
- YAML frontmatter
- References exist
- Workflow documented
- State persistence

❌ FAIL (1):
- Script: check-blockers.py - ERROR: timeout

📊 SUMMARY:
Total: 9
Passed: 8
Failed: 1
Score: 89%
```

---

## 💾 State Persistence

Guardar reportes de auditoría en:
- `${CLAUDE_PLUGIN_DATA}/skill-auditor/reports/`
- O en `reports/` local
