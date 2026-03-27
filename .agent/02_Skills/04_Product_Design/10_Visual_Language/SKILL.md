---
name: engram-visual-language
description: >
  Reglas de lenguaje visual para Engram — styling, typography, spacing.
  Triggers on: dashboard styling, visual identity, typography, spacing, engram design, visual language.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

## Esencia Original
> **Propósito:** Mantener consistencia visual en superficies de Engram — dashboard styling, typography, spacing, paleta TUI-inspired.
> **Flujo:** Leer reglas → Aplicar palette → Validar jerarquía → Check breathing room

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Usar estética de SaaS genérico
  - **Por qué**: Pierde identidad de Engram
  - **Solución**: Sentirse como Engram, no como admin panel cualquiera

- **[ERROR]**: Containers sin jerarquía
  - **Por qué**: Todo se ve igual, confunde al usuario
  - **Solución**: Strong hierarchy, fewer containers, clearer breathing room

- **[ERROR]**: Ignorar accents TUI-inspired
  - **Por qué**: Rompe la identidad visual única
  - **Solución**: Usar mono/display accents intencionalmente

- **[ERROR]**: Spacing inconsistente
  - **Por qué**: Se ve amateur, no profesional
  - **Solución**: Usar sistema de spacing consistente

## 📁 Progressive Disclosure

> Para información detallada:
- [references/visual-rules.md](references/visual-rules.md) — Reglas visuales detalladas
- [references/palette-engram.md](references/palette-engram.md) — Paleta de Engram

## 🛠️ Scripts

- [scripts/validate-visual.py](scripts/validate-visual.py) — Valida lenguaje visual

## 💾 State Persistence

Guardar cambios en:
- `styles.css` del dashboard
- Notas en `03_Knowledge/08_Config/visual/`

## When to Use

Use this skill when:
- Editing `styles.css`
- Creating new dashboard sections or states
- Refining layout, spacing, typography, or color use

---

## Visual Rules

1. The dashboard must feel like Engram, not a generic SaaS admin.
2. Prefer strong hierarchy, fewer containers, and clearer breathing room.
3. Use the TUI-inspired palette and mono/display accents intentionally.
4. Format machine timestamps and raw identifiers into human-scannable UI.
5. Decorative framing must never make content harder to read.

---

## Density Rules

- Avoid box-inside-box repetition unless it clarifies information grouping.
- Important text must never touch borders or feel cramped.
- Metrics should read instantly.
- Tables should stay clean, aligned, and visually quieter than hero areas.
