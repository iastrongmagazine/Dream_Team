---
name: ship
description: De terminado → publicado. El workflow para llevar un proyecto del repo a manos reales de usuarios. Sin esto, el sistema acumula trabajo invisible.
argument-hint: "[nombre del proyecto a publicar]"
---

# 🚀 Workflow: Ship It (Lanzar al mundo)

El trabajo que nadie ve no existe. Este workflow convierte "está listo" en "está vivo".

> "Make something people want. Then tell them about it." — Paul Graham

## Cuándo usar

- Terminaste un proyecto, feature o herramienta
- Tienes contenido de valor listo para publicar
- Quieres añadir algo a tu portfolio público
- Completaste un LFG Pro y quieres que el mundo lo vea

## Los 4 niveles de Ship

| Nivel | Audiencia | Ejemplos |
|-------|-----------|---------|
| **L1 — Interno** | Solo tú | Commit final, documentación interna |
| **L2 — Privado** | Personas específicas | Link directo, WhatsApp, email |
| **L3 — Comunidad** | Tu red | Twitter/X, LinkedIn, grupos |
| **L4 — Público** | El mundo | GitHub público, Product Hunt, blog |

## Flujo completo

### FASE 1 — Validar que está listo (10 min)

Antes de publicar, confirmar:

- [ ] ¿El output hace lo que prometía? (test manual rápido)
- [ ] ¿Hay datos sensibles, credenciales o rutas personales? → Limpiar
- [ ] ¿El README explica qué es y cómo usarlo?
- [ ] ¿El código/diseño representa bien tu estándar de calidad?

Si algún check falla → resolver antes de continuar.

### FASE 2 — Documentar el contexto (15 min)

Crear o actualizar la documentación de entrega:

**Para proyectos técnicos:**

```markdown
## ¿Qué es?
[1 oración clara]

## ¿Para quién?
[usuario específico]

## ¿Cómo usarlo?
[pasos mínimos para arrancar]

## ¿Qué problema resuelve?
[antes vs después]
```

**Para diseño / UX:**

- Screenshot o video de la solución
- Decisiones de diseño clave (1-3 principios aplicados)
- Link a Figma o prototipo si aplica

### FASE 3 — Git & GitHub (5 min)

```bash
git add .
git commit -m "feat: [descripción clara del proyecto]"
git push origin main
```

Si el repo debe ser público:

```bash
# En GitHub: Settings → Change visibility → Public
# O crear nuevo repo público desde github.com
```

### FASE 4 — Escribir el mensaje de lanzamiento (15 min)

Adaptar según el nivel de ship (L2/L3/L4):

**Template corto (L2/L3):**

```
[Hook — qué problema resuelve en 1 línea]

Construí [nombre] — [descripción de 2 oraciones].

[Qué aprendí / qué lo hace diferente]

→ [Link]
```

**Template completo (L4 — Twitter/X, LinkedIn):**

```
[Hook poderoso — la tensión o el insight]

El problema:
[situación actual que es frustrante]

Lo que construí:
[solución específica con resultado concreto]

Lo más interesante del proceso:
[1 insight técnico o de diseño que valga la pena compartir]

→ [Link al proyecto/repo/demo]
```

### FASE 5 — Distribuir

Según el nivel elegido:

- **L2**: Enviar directamente a quien le sirva
- **L3**: Publicar en Twitter/X, LinkedIn, comunidades relevantes
- **L4**: GitHub público + Product Hunt + newsletter si tienes

### FASE 6 — Registrar en el portfolio (5 min)

```
→ 03_Knowledge/06_Writing_Content/portfolio.md  (o crear si no existe)

Añadir:
- Nombre del proyecto
- Fecha de lanzamiento
- Link
- Métricas iniciales (stars, views, feedback recibido)
- Qué aprendí
```

## Regla de Ship Mínimo Viable

Si el workflow completo se siente pesado → **hacer solo FASE 1 + FASE 3 + la primera mitad de FASE 4**.

Publicar algo imperfecto hoy > publicar algo perfecto nunca.

## Anti-patrones a evitar

- ❌ "Todavía no está listo" (siempre habrá algo más)
- ❌ Limpiar/refactorizar infinitamente antes de publicar
- ❌ Esperar el momento perfecto para anunciar
- ❌ Ship sin documentar → nadie entiende qué construiste

---

© 2026 PersonalOS | El trabajo invisible no cuenta. Ship early, ship often.
