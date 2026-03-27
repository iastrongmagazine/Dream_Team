---
name: system-master
description: >
  Master orchestrator for Think Different AI ecosystem.
  TRIGGERS: "gentleman o compound", "qué usar", "cómo lo hago",
  "workflow", "sistema", "que skill", "empezar proyecto",
  "code review", "idear", "planear", "diseñar", "deploy",
  "testear", "documentar", "investigar", "feature", "bug",
  "mejorar", "instalar", "configurar", "migrar", "dark mode".
  Use before starting ANY significant development task.
argument-hint: "[what you want to accomplish]"
---

# 🎯 System Master - Guía Maestra del Ecosistema

## Esencia Original

> Original purpose of this skill. This section preserves WHY this skill exists.

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: No verificar si la tarea requiere Gentleman o CE
  - **Por qué**: Usar la herramienta equivocada ralentiza el trabajo
  - **Solución**: Consultar la Quick Decision Matrix antes de actuar

- **[ERROR]**: Saltarse /ce:brainstorm antes de code
  - **Por qué**: Sin exploración de requisitos, el código no resuelve el problema
  - **Solución**: Siempre hacer brainstorm primero

- **[ERROR]**: No hacer /ce:review antes de commit
  - **Por qué**: Código sin review tiene más bugs
  - **Solución**: Ejecutar /ce:review siempre antes de commit

- **[ERROR]**: No documentar con /ce:compound
  - **Por qué**: Sin documentación, el conocimiento se pierde
  - **Solución**: Siempre hacer compound después de completar features

## 🧠 Quick Decision Matrix

**GENTLEMAN = MANOS** → Ejecutar código
**CE = CEREBRO** → Inteligencia + Validación

| ¿Qué querés hacer? | Usá |
|---------------------|-----|
| Escribir código nuevo | Gentleman |
| Framework (React, Angular, Tailwind) | Gentleman |
| Testing (Playwright, Pytest) | Gentleman |
| DevOps (Docker, Deploy) | Gentleman |
| Diseño UI/UX | Gentleman |
| Marketing (SEO, Ads) | Gentleman |
| Code review | CE → /ce:review |
| Seguridad | CE → security-sentinel |
| Performance | CE → performance-oracle |
| Idear mejoras | CE → /ce:ideate |
| Explorar requisitos | CE → /ce:brainstorm |
| Planificar | CE → /ce:plan |
| Documentar | CE → /ce:compound |

## 🔄 Workflow Ideal: Matrix Recargado

1. /ce:ideate → Descubrir oportunidades
2. /ce:brainstorm → Explorar enfoques
3. Gentleman → Escribir código
4. /ce:review → Validar con 23+ agents
5. /ce:work → Ejecutar plan
6. /ce:compound → Documentar learnings

## 🚀 Commands Reference

### CE Commands
| Comando | Triggers | Propósito |
|---------|----------|-----------|
| /ce:ideate | "idear", "mejorar" | Descubrir mejoras |
| /ce:brainstorm | "explorar", "requisitos" | Explorar enfoques |
| /ce:plan | "planear", "plan" | Crear plan |
| /ce:work | "ejecutar", "implementar" | Ejecutar plan |
| /ce:review | "review", "revisar" | Code review |
| /ce:compound | "documentar", "aprendizajes" | Documentar |

### Gentleman Categories
- **Vibe Coding**: react-19, nextjs-15, tailwind-4, typescript
- **Testing**: test-driven-development, e2e-testing-skill, playwright
- **DevOps**: mcp-integration, observability-skill, github-pr
- **Design**: taste-skill, minimalist-skill, brand-voice-generator
- **Marketing**: content-creation, social-content, programmatic-seo

## ⚠️ Gotchas

### CE
- /ce:plan requiere output de /ce:brainstorm
- /ce:work necesita archivo de plan válido
- /ce:review usa worktrees - no romper el repo

### Gentleman
- Testear después de cada cambio
- Usar taste-skill solo si conocés el estilo

## 📚 Referencias
- [Comandos CE](references/commands-ce.md)
- [Skills Gentleman](references/commands-gentleman.md)
- [Gotchas](references/gotchas.md)
- [Ejemplos REALES](references/examples.md)
