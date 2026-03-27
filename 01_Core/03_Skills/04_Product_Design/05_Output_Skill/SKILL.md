---
name: full-output-enforcement
description: Forces complete output without truncation or placeholders. Triggers on: full output, complete code, no truncation, unabridged, exhaustive output, full file.
---

# Full-Output Enforcement

## Esencia Original
> **Propósito:** Overridear truncación de LLMs — forzar output completo, bans placeholders, splits limpios cuando se alcanza token limit.
> **Flujo:** Detectar request → Generar completo → Si split necesario → Split clean → Continuar

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Usar "// ..." o "// rest of code"
  - **Por qué**: Partial output = broken output
  - **Solución**: Siempre code completo, sin atajos

- **[ERROR]**: "Let me know if you want me to continue"
  - **Por qué**: El usuario tiene que pedir de nuevo, frustrante
  - **Solución**: Generar todo de una, split si es necesario

- **[ERROR]**: Skeleton cuando piden full implementation
  - **Por qué**: No es lo que se pidió
  - **Solución**: Full implementation siempre

- **[ERROR]**: Describir código en vez de escribirlo
  - **Por qué**: El usuario tiene que traducir description a code
  - **Solución**: Escribir el código real

## 📁 Progressive Disclosure

> Para información detallada:
- [references/banned-patterns.md](references/banned-patterns.md) — Patrones banned
- [references/split-strategy.md](references/split-strategy.md) — Estrategia de splits

## 🛠️ Scripts

- [scripts/validate-output.py](scripts/validate-output.py) — Valida output completo

## 💾 State Persistence

Tracking de outputs en:
- `03_Tasks/` — Tasks en progreso

## Baseline

Treat every task as production-critical. A partial output is a broken output. Do not optimize for brevity — optimize for completeness. If the user asks for a full file, deliver the full file. If the user asks for 5 components, deliver 5 components. No exceptions.

## Banned Output Patterns

The following patterns are hard failures. Never produce them:

**In code blocks:** `// ...`, `// rest of code`, `// implement here`, `// TODO`, `/* ... */`, `// similar to above`, `// continue pattern`, `// add more as needed`, bare `...` standing in for omitted code

**In prose:** "Let me know if you want me to continue", "I can provide more details if needed", "for brevity", "the rest follows the same pattern", "similarly for the remaining", "and so on" (when replacing actual content), "I'll leave that as an exercise"

**Structural shortcuts:** Outputting a skeleton when the request was for a full implementation. Showing the first and last section while skipping the middle. Replacing repeated logic with one example and a description. Describing what code should do instead of writing it.

## Execution Process

1. **Scope** — Read the full request. Count how many distinct deliverables are expected (files, functions, sections, answers). Lock that number.
2. **Build** — Generate every deliverable completely. No partial drafts, no "you can extend this later."
3. **Cross-check** — Before output, re-read the original request. Compare your deliverable count against the scope count. If anything is missing, add it before responding.

## Handling Long Outputs

When a response approaches the token limit:

- Do not compress remaining sections to squeeze them in.
- Do not skip ahead to a conclusion.
- Write at full quality up to a clean breakpoint (end of a function, end of a file, end of a section).
- End with:

```
[PAUSED — X of Y complete. Send "continue" to resume from: next section name]
```

On "continue", pick up exactly where you stopped. No recap, no repetition.

## Quick Check

Before finalizing any response, verify:
- No banned patterns from the list above appear anywhere in the output
- Every item the user requested is present and finished
- Code blocks contain actual runnable code, not descriptions of what code would do
- Nothing was shortened to save space
