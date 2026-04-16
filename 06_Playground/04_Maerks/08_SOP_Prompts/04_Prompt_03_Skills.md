# 📝 SOP Prompt: 03_Skills

> **Carpeta destino:** `01_Core/03_Skills/` (FUENTE DE VERDAD)
> **Complementa:** `.agent/02_Skills/`, `Maerks/06_Skill_Audit.md`, `Maerks/08_Skill_Audit.md`

---

## 🎯 Propósito del Prompt

Crear una skill completa y operacional siguiendo el estándar de PersonalOS. Las skills son la implementación de patrones, workflows y conocimientos especializados.

---

## 📋 Prompt Base (Copy-Paste)

```
Eres un Creador de Skills Expert. Crea una skill completa para PersonalOS.

## 📍 Contexto del Proyecto
- **Nombre de la skill:** [NOMBRE_DE_LA_SKILL]
- **Categoría:** [Vibe_Coding/Testing/DevOps/Marketing/Agent_Teams_Lite/etc.]
- **Carpeta destino:** `01_Core/03_Skills/[CATEGORIA]/[SUBCATEGORIA]/`

## ⚠️ IMPORTANTE: Fuente de Verdad
- **Skills activas:** `01_Core/03_Skills/`
- **Alias en .agent:** `.agent/02_Skills/` (sincronizado)
- **Skill Auditor:** `Maerks/06_Skill_Audit.md` y `Maerks/08_Skill_Audit.md`

## 📝 Estructura Requerida

```
[CARPETA]/
├── SKILL.md              ← OBLIGATORIO
├── README.md             ← Recomendado
├── references/           ← Opcional
│   ├── doc1.md
│   └── doc2.md
├── scripts/              ← Opcional
│   ├── script1.py
│   └── requirements.txt  ← Si hay dependencies
└── assets/               ← Opcional
    └── image.png
```

## 📋 Estructura SKILL.md (FORMATO OFICIAL)

```markdown
---
name: [Nombre de la Skill]
description: [Descripción clara - qué hace]
version: [1.0.0]
sota_principles: [principle1, principle2]
model_recommendation: "[modelo recomendado]"
trigger_keywords: [[keyword1], [keyword2], [keyword3]]
auto_loads_skills: [true/false]
harness_pattern: [planner, generator, evaluator]
---

# [Nombre de la Skill]

## 🎯 Propósito
[Descripción extendida: qué problema resuelve esta skill]

## 🔄 Cuándo Usar
- **Trigger keywords:** "[phrase1]", "[phrase2]"
- **Contexto:** [cuándo es relevante]
- **No usar:** [cuándo NO es relevante]

## 📋 Contenido Principal

### Core Concepts
[Conceptos fundamentales - qué sabe hacer]

### Patrones de Uso
[Cómo se aplica - con ejemplos]

### Integración
[Cómo se conecta con otras skills/agents/workflows]

## 🛠️ Implementación

### Dependencias
- **Skills relacionadas:** `01_Core/03_Skills/[otra_skill]/`
- **Scripts:** `[ruta a scripts si aplica]`
- **Requirements:** `[requirements.txt si tiene]`

### Casos de Uso

#### Caso 1: [Nombre]
```
[Ejemplo de código/prompt]
```

#### Caso 2: [Nombre]
```
[Ejemplo]
```

## 📊 Métricas
- **Utilización:** [frecuencia de uso]
- **Éxito:** [tasa de éxito]
- **Última validación:** [fecha]

## 🔄 Changelog
| Versión   | Fecha      | Cambio           |
|-----------|------------|------------------|
| 1.0.0     | YYYY-MM-DD | Creación inicial |
```

## 🛠️ Integración con Skills Existentes

### Skills Fundamentales
- `01_Core/03_Skills/00_Compound_Engineering/` - Para compound engineering
- `01_Core/03_Skills/01_Agent_Teams_Lite/` - Para agent teams
- `01_Core/03_Skills/14_Anthropic_Harness/` - Para evaluation

### Validación de Esencia
Antes de crear, verificar con:
- `Maerks/06_Skill_Audit.md` - Auditor de skills
- `01_Core/03_Skills/00_Skill_Auditor/` - Skill Auditor

## ⚡ Best Practices SOTA

### Estructura (OBLIGATORIO)
- [ ] SKILL.md con frontmatter completo
- [ ] Versión semver (1.0.0)
- [ ] Trigger keywords claros
- [ ] Model recommendation

### Contenido
- [ ] Propósito claro en 1 oración
- [ ] Cuándo USAR y cuándo NO usar
- [ ] Ejemplos concretos
- [ ] Métricas de uso

### SOTA Principles
- [ ] Adversarial evaluation ( evaluator)
- [ ] Progressive disclosure (info gradual)
- [ ] Checkpoint validation (validar en puntos clave)
- [ ] Observability (logging claro)

## 🎬 Ejemplo de Uso

```
Crear una skill para validación de código Python.

Nombre: Python Type Validator
Categoría: 06_Testing
Trigger: "validar tipos", "type hints", "python typing"
Versión: 1.0.0
```

## ✅ Checklist de Calidad (PARA AUDITOR)

- [ ] Tiene SKILL.md con frontmatter completo
- [ ] Version semver correcta
- [ ] Al menos 3 trigger keywords
- [ ] Propósito claro
- [ ] Casos de uso con ejemplos
- [ ] Dependencias documentadas
- [ ] Changelog presente
- [ ] NO es genérica (específica para PersonalOS)
- [ ] NO viola esencias existentes
- [ ] Pasa audit de esencia
