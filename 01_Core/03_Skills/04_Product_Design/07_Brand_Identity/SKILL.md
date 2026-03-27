---
name: brand-identity
description: Fuente única de verdad para guías de marca, diseño y tono de voz. Triggers on: brand guidelines, brand identity, design tokens, voice tone, brand consistency.
---

# Brand Identity & Guidelines

## Esencia Original
> **Propósito:** Fuente única de verdad para guías de marca — asegurar consistencia estricta en UI, estilos, copys y activos.
> **Flujo:** Leer Design Tokens → Aplicar Voice & Tone → Validar coherencia

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Inventar colores fuera del sistema
  - **Por qué**: Rompe consistencia de marca
  - **Solución**: Solo usar Design Tokens definidos

- **[ERROR]**: Copys que no siguen Voice & Tone
  - **Por qué**: Marca pierde personalidad coherente
  - **Solución**: Referenciar voice guidelines siempre

- **[ERROR]**: Assets visuales inconsistentes
  - **Por qué**: Usuario no reconoce la marca
  - **Solución**: Usar solo iconos, colores, tipografía del brand

- **[ERROR]**: No validar coherencia al final
  - **Por qué**: Errores se colan en output
  - **Solución**: Checklist visual y narrativa al final

## 📁 Progressive Disclosure

> Para información detallada:
- [references/design-tokens.md](references/design-tokens.md) — Design tokens
- [references/voice-tone.md](references/voice-tone.md) — Voice & Tone guide

## 🛠️ Scripts

- [scripts/validate-brand.py](scripts/validate-brand.py) — Valida alineación de marca

## 💾 State Persistence

Guardar brand assets en:
- `03_Knowledge/08_Config/brand/`
- Tokens en `resources/`

## 📋 Skill Protocol (Armor Layer)

### 🧩 Contexto Requerido
- Diseño o componente que requiere alineación de marca.
- Acceso a `resources/` (tokens, voice, assets).
- Conocimiento de la audiencia objetivo.

### 📦 Output Esperado
- Assets o código que respetan estrictamente los Design Tokens.
- Copy alineado con el Voice & Tone de Invictus.
- Checklist de coherencia visual y narrativa.

### 🚫 Limitaciones
- **No inventa colores o estilos fuera del sistema de diseño.**
- No es una skill de creatividad libre; es de ejecución bajo guías.
---

# Brand Identity & Guidelines

Brand Name: [INSERT BRAND NAME HERE]
This skill defines the core constraints for visual design and technical implementation for the brand. You must adhere to these guidelines strictly to maintain consistency.

## Reference Documentation

Depending on the task you are performing, consult the specific resource files below. Do not guess brand elements; always read the corresponding file.

### For Visual Design & UI Styling

If you need exact colors, fonts, border radii, or spacing values, read:
👉 [`resources/design-tokens.json`](resources/design-tokens.json)

### For Coding & Component Implementation

If you are generating code, choosing libraries, or structuring UI components, read the technical constraints here:
👉 [`resources/tech-stack.md`](resources/tech-stack.md)

### For Copywriting & Content Generation

If you are writing marketing copy, error messages, documentation, or user-facing text, read the persona guidelines here:
👉 [`resources/voice-tone.md`](resources/voice-tone.md)

### For Logos & Brand Assets

If you need the official logo or brand imagery, read:
👉 [`resources/assets.md`](resources/assets.md)

### For Interaction & UX Trust

If you are designing interactions, states, or feedback loops, read:
👉 [`resources/ux-trust-guidelines.md`](resources/ux-trust-guidelines.md)

### For Layout & Data Hierarchy

If you are designing dashboards or data-heavy screens, read:
👉 [`resources/invisible-ui-guidelines.md`](resources/invisible-ui-guidelines.md)
