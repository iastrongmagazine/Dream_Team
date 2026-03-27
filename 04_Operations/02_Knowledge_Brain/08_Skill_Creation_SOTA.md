# Super Documento: Skill Creation System (v5.0 SOTA)

> Guía definitiva para crear skills de nivel producción siguiendo estándares Anthropic + PersonalOS.
> **Última actualización**: 2026-03-25

---

## 📋 Tabla de Contenidos

1. [Filosofía Core](#1-filosofía-core)
2. [Anatomía de una Skill](#2-anatomía-de-una-skill)
3. [YAML Frontmatter (Obligatorio)](#3-yaml-frontmatter-obligatorio)
4. [Estructura de Directorios](#4-estructura-de-directorios)
5. [Progressive Disclosure](#5-progressive-disclosure)
6. [Gotchas Section](#6-gotchas-section)
7. [Degrees of Freedom](#7-degrees-of-freedom)
8. [Scripts & Código](#8-scripts--código)
9. [Checklist de Calidad](#9-checklist-de-calidad)
10. [Errores Comunes a Evitar](#10-errores-comunes-a-evitar)
11. [Proceso de Creación](#11-proceso-de-creación)

---

## 1. Filosofía Core

### Steering Distribution (Principio Fundamental)

Skills no son "atajos" — son **funciones de fuerza** que sacan al agente de su "distribución promedio" y lo empujan hacia soluciones específicas, creativas y adaptadas a tu contexto.

> **"Don't State the Obvious"** — Enfocarse en información que el modelo NO tiene en su default thinking.

### Los 2 Pilares

| Pilar                      | Descripción                                        |
|----------------------------|----------------------------------------------------|
| **Goal-Oriented**          | Dar información + flexibilidad, NO recetas rígidas |
| **Progressive Disclosure** | Cargar contexto en etapas, no saturar de entrada   |

---

## 2. Anatomía de una Skill

```
skill-name/
├── SKILL.md              # (OBLIGATORIO) Instrucciones principales
├── scripts/              # (OPCIONAL) Código ejecutable
├── references/           # (OPCIONAL) Docs pesadas
└── assets/               # (OPCIONAL) Templates, imágenes, etc.
```

### SKILL.md (Required)

```
---
name: [gerund-name]       # Required
description: [触发条件]     # Required
---

# [Skill Title]

## When to Use This Skill
[Triggers semánticos]

## Workflow
[Pasos de alto nivel]

## Gotchas (Common Mistakes)
[Errores documentados]

## Progressive Disclosure
[Referencias a archivos externos]

## Scripts & Templates
[Código reutilizable]
```

---

## 3. YAML Frontmatter (Obligatorio)

### name (REQUIRED)

- **Máximo**: 64 caracteres
- **Formato**: Solo lowercase, números, guiones
- **Forma**: Gerund (verb + -ing)
- **PROHIBIDO**: "anthropic", "claude"

```yaml
# ✅ GOOD
name: onboarding-agent-employee
name: processing-pdfs
name: managing-databases

# ❌ BAD
name: Onboarding Agent      # Mayúsculas
name: onboarding_agent      # Guiones bajos
name: claude-onboarding     # "claude" prohibido
```

### description (REQUIRED)

- **Máximo**: 1024 caracteres
- **Contenido**: Qué hace + **CUÁNDO activarlo** (triggers)
- **Enfoque**: Tercera persona, NO marketing

```yaml
# ✅ GOOD - Incluye triggers específicos
description: Onboards AI agents as team members with role definition, context setup, and working agreements. Triggers on: new agent, add team member, hire agent, setup agent context, agent onboarding, integrate new AI.

# ❌ BAD - Marketing vago
description: A comprehensive tool for managing agents and team workflows with advanced features.
```

**Patrón para description**:
```
[Qué hace]. Triggers on: [keyword1], [keyword2], [keyword3], [más keywords que el usuario dice].
```

---

## 4. Estructura de Directorios

### Nivel de Profundidad

```
# ✅ CORRECTO - Un nivel
skill/
├── SKILL.md
└── references/
    └── workflow.md

# ❌ INCORRECTO - Demasiados niveles
skill/
├── SKILL.md
└── references/
    └── subfolder/
        └── deep/
            └── workflow.md  # Too deep!
```

### Nombres de Carpetas

```bash
# ✅ lowercase, números si es necesario
01_Agent_Onboarding/
02_Executive_Assistant/
03_Head_Of_Marketing/

# ❌ Mayúsculas, espacios
Agent Onboarding/     # NO
agent-onboarding/    # Evitar
```

---

## 5. Progressive Disclosure

### El Problema

Si metés todo en SKILL.md:
- Context window se satura
- El modelo no puede encontrar lo que necesita
- Peor rendimiento

### La Solución: 3 Niveles de Carga

| Nivel                             | Cuándo                 | Tamaño      |
|-----------------------------------|------------------------|-------------|
| **Metadata** (name + description) | Siempre en context     | ~100 words  |
| **SKILL.md body**                 | Cuando skill triggerea | <500 líneas |
| **Bundled resources**             | Cuando necesita        | Ilimitado   |

### Patrones de Progressive Disclosure

#### Pattern 1: High-level guide + references

```markdown
## Advanced features

- **Complex workflows**: See [workflows.md](references/workflows.md)
- **Output quality**: See [output-patterns.md](references/output-patterns.md)
- **API reference**: See [reference.md](references/reference.md)
```

#### Pattern 2: Domain-specific organization

```
skill-name/
├── SKILL.md (overview + navigation)
└── references/
    ├── finance.md
    ├── sales.md
    └── marketing.md
```

#### Pattern 3: Conditional details

```markdown
## Basic usage
[Simple instructions]

**For advanced scenarios**: See [ADVANCED.md](references/ADVANCED.md)
```

---

## 6. Gotchas Section

### Por qué es el activo más valioso

- Documentar errores pasados evita que el agente los repita
- Es como entrenar un empleado junior
- **Se construye incrementalmente** con cada ejecución

### Cómo escribir Gotchas

```markdown
## Gotchas (Common Mistakes)

- **Don't**: Give the agent too many responsibilities at once — start with 1-3 focus areas
- **Don't**: Skip the success metrics — you'll never know if it's working
- **Don't**: Give it access to everything — follow principle of least privilege
```

### Estructura de Gotcha

```
- **[ERROR]**: [Título del error]
  - **Por qué**: [Explicación técnica]
  - **Solución**: [Cómo evitarlo]
```

### Mínimo recomendados

- **Mínimo**: 3 gotchas por skill
- **Mejor**: 5-8 gotchas
- **Actualizar**: Con cada ejecución que revele un nuevo error

---

## 7. Degrees of Freedom

### Cuándo usar cada nivel

| Nivel                           | Uso                                                          | Ejemplo                                                      |
|---------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| **HIGH** (text-based)           | Múltiples enfoques válidos, decisiones dependen del contexto | "Analyze the code and suggest improvements"                  |
| **MEDIUM** (pseudocode/scripts) | Patrón preferido existe, algo de variación aceptable         | "Use the template in scripts/template.py and customize X, Y" |
| **LOW** (specific commands)     | Operaciones frágiles, consistencia crítica                   | "Run `npm install` then `npm run build`"                     |

### Ejemplos Prácticos

```markdown
# HIGH freedom (heurística)
## Code review process
1. Analyze the code structure and organization
2. Check for potential bugs or edge cases
3. Verify error handling is present

# MEDIUM freedom (template)
## Create PR
Use this template:
```markdown
## Summary
[One sentence]

## Changes
- [Change 1]
- [Change 2]
```

# LOW freedom (comando específico)
## Install dependencies
Run: `npm install && npm run build`
```

---

## 8. Scripts & Código

### Cuándo incluir scripts

| Cuándo                                   | Ejemplo                   |
|------------------------------------------|---------------------------|
| Mismo código se reescribe frecuentemente | `rotate_pdf.py`           |
| Se necesita confiabilidad determinística | Validación de archivos    |
| Automatización repetitiva                | Generación de boilerplate |

### Estructura de scripts/

```
skill-name/
├── SKILL.md
└── scripts/
    ├── rotate_pdf.py        # Ejecutable
    ├── validate.py         # Ejecutable
    └── constants.py        # Utilidad (puede leerse)
```

### Reglas de scripting

- **No paths Windows** — Usar forward slashes `/`
- **Documentar** — Cada script con docstring o comentarios
- **Probar** — Ejecutar antes de commit
- **Dependencias** — Listar en SKILL.md

---

## 9. Checklist de Calidad

### ✅ Core Quality

- [ ] name usa gerund form (verb + -ing)
- [ ] name tiene max 64 chars, lowercase, números, guiones
- [ ] description incluye triggers semánticos
- [ ] description NO es marketing vago
- [ ] SKILL.md body tiene <500 líneas
- [ ] Información pesada en references/

### ✅ Gotchas Section

- [ ] Mínimo 3 gotchas documentados
- [ ] Gotchas son específicos, no genéricos
- [ ] Incluyen "Por qué" y "Solución"

### ✅ Progressive Disclosure

- [ ] SKILL.md ссылается на references/
- [ ] Referencias son un nivel de profundidad
- [ ] No hay más de 3-5 referencias en SKILL.md

### ✅ Degrees of Freedom

- [ ] Alta libertad para decisiones creativas
- [ ] Baja libertad para operaciones frágiles
- [ ] Scripts para código reutilizable

### ✅ Testing (si aplica)

- [ ] Scripts probados
- [ ] Sin errores de sintaxis
- [ ] Dependencias documentadas

---

## 10. Errores Comunes a Evitar

| Error                  | Por qué                             | Solución                              |
|------------------------|-------------------------------------|---------------------------------------|
| Description marketing  | No le dice al modelo cuándo activar | Incluir triggers semánticos           |
| Todo en SKILL.md       | Satura context window               | Usar references/                      |
| Sin Gotchas            | Skill no aprende de errores         | Documentar 3+ errores                 |
| Recipes rígidos        | No permite adaptación               | Goal-oriented, no pasos fijos         |
| Paths Windows          | Rompe en Linux/Mac                  | Usar forward slashes                  |
| Nombre con mayúsculas  | Rompe YAML                          | lowercase siempre                     |
| Sin ejemplos concretos | Ambigüedad                          | Incluir ejemplos en scripts/templates |

---

## 11. Proceso de Creación

### Flujo Recomendado

```
1. ENTENDER → Cuáles son los casos de uso concretos?
2. PLANEAR → Qué scripts/references/assets necesito?
3. CREAR → init_skill.py o mkdir manual
4. IMPLEMENTAR → Escribir SKILL.md + recursos
5. AUDITAR → Verificar contra checklist
6. ITERAR → Probar y mejorar
```

### Paso 1: Entender con Ejemplos

Preguntar:
- "¿Cómo se usaría esta skill?"
- "¿Qué dirías para activarla?"
- Ejemplos: "new agent", "onboard agent"

### Paso 2: Planear Contenidos

| Si...                  | Entonces incluir...   |
|------------------------|-----------------------|
| Mismo código reescrito | scripts/rotar_pdf.py  |
| Docs pesadas           | references/schema.md  |
| Templates reuse        | assets/template.html  |

### Paso 3: Implementar SKILL.md

```
---
name: [gerund-name]
description: [Qué hace + triggers]
---

# [Título]

## When to Use This Skill
- [Trigger 1]
- [Trigger 2]

## [Sección principal]
[Contenido con degree of freedom apropiado]

## Gotchas (Common Mistakes)
- **Don't**: [Error 1]
- **Don't**: [Error 2]

## Progressive Disclosure
- [Referencia 1]
- [Referencia 2]

## Scripts & Templates
```[código]
```
```

### Paso 4: Auditar

Verificar contra el checklist de sección 9.

---

## 📚 Recursos

- [Anthropic Skills Docs](https://docs.anthropic.com/en/docs/claude-code/skills)
- [Best Practices](https://docs.anthropic.com/en/docs/claude-code/best-practices)
- [Agent Skills Engineering](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)
- [Skill Creator](https://claude.ai/blog/improving-skill-creator-test-measure-and-refine-agent-skills)

---

*Documento mantenido por PersonalOS — Actualizado 2026-03-25 v5.0*
