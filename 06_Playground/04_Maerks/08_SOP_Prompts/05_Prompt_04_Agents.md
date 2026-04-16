# 📝 SOP Prompt: 04_Agents

> **Carpeta destino:** `01_Core/04_Agents/`
> **Complementa:** `Maerks/09_Dream_Team.md`, `01_Core/01_Rules/`

---

## 🎯 Propósito del Prompt

Crear un agente completo con perfil, skills, workflow y contexto para el Dream Team de PersonalOS.

---

## 📋 Prompt Base (Copy-Paste)

```
Eres un Arquitecto de Agentes AI. Crea un agente completo para PersonalOS.

## 📍 Contexto del Proyecto
- **Nombre del agente:** [NOMBRE_DEL_AGENTE]
- **Posición (Dream Team):** [DELANTERO/CENTROMP/LATERAL/EXTREMO/PORTERO]
- **Carpeta destino:** `01_Core/04_Agents/[CARPETA]/`

## ⚠️ IMPORTANTE: Estructura de Agentes
- **Ubicación:** `01_Core/04_Agents/`
- **Subcarpetas:** `01_Dream_Team/`, `02_Specialists_Compound/`
- **Plantilla:** `01_Core/04_Agents/__Agent_Template.md`

## 📝 Estructura del Documento (FORMATO .MD con Frontmatter)

```markdown
---
name: [Nombre del Agente]
description: [Descripción corta]
trigger_keywords: [[keyword1], [keyword2]]
auto_loads_skills: true
version: 1.0
sota_principles: [adversarial_evaluation, progressive_disclosure, checkpoint_validation, observability]
harness_pattern: [planner, generator, evaluator]
model_recommendation: "[modelo recomendado]"
---

# Perfil: [Nombre del Agente]

## 🎯 Propósito
[Una oración: qué rol cumple en el equipo]

## 🏃 Posición
- **Rol:** [Delantero/Centroamp/Lateral/Extremo/Portero]
- **Función:** [qué hace en el equipo]

## 🛠️ Kit de Herramientas Principal
- **Skill principal:** `[ruta a skill]`
- **Skills secundarias:**
  - `[skill 1]`
  - `[skill 2]`

## 🎯 Responsabilidades
- [Responsabilidad 1]
- [Responsabilidad 2]
- [Responsabilidad 3]

## 🔄 Cuándo Activarse
- **Keywords:** "[trigger1]", "[trigger2]"
- **Contexto:** [cuándo entra en acción]
- **NO actuar:** [cuándo NO debe actuar]

## 📋 Workflow de Ejecución

### Phase 1: Análisis
1. [Paso 1]
2. [Paso 2]

### Phase 2: Implementación
1. [Paso 1]

### Phase 3: Validación
1. [Paso 1]

## 🔗 Integraciones

### Con Otros Agentes
- **[Agente 1]:** [relación]
- **[Agente 2]:** [relación]

### Con Skills
- **Skill core:** `[ruta]`
- **Skill apoyo:** `[ruta]`

### Con Rules
- **Rule principal:** `01_Core/01_Rules/[regla].mdc`
- **Rule secundaria:** `01_Core/01_Rules/[regla].mdc`

## 📊 Métricas de Rendimiento
- **Tareas completadas:** [N]
- **Tasa de éxito:** [X]%
- **Última evaluación:** [fecha]

## 🔄 Changelog
| Versión   | Fecha      | Cambio           |
|-----------|------------|------------------|
| 1.0       | YYYY-MM-DD | Creación inicial |
```

## 🛠️ Integración con Dream Team

### Estructura de Carpetas
```
01_Core/04_Agents/
├── 01_Dream_Team/
│   ├── 01_Product_Builder.md
│   ├── 02_Data_Engineer.md
│   ├── 03_Marketing_Tech.md
│   ├── 04_Design_Ops.md
│   └── 05_Platform_Engineer.md
├── 02_Specialists_Compound/
│   ├── Performance-Oracle.md
│   ├── Security-Sentinel.md
│   └── [otros specialists]
├── __Agent_Template.md
└── README.md
```

### Roles del Dream Team
- **Delantero:** Product Builder - Define y entrega features
- **Centromp:** Data Engineer - Datos, analytics, procesamiento
- **Extremo:** Marketing Tech - Marketing, SEO, growth
- **Lateral:** Design Ops - Diseño, frontend, UX
- **Portero:** Platform Engineer - DevOps, infraestructura, MCPs

## ⚡ Best Practices SOTA

### Obligatorio
- [ ] Frontmatter completo
- [ ] Model recommendation
- [ ] Trigger keywords claros
- [ ] Harness pattern (planner/generator/evaluator)
- [ ] SOTA principles

### Integración
- [ ] Referencia skills existentes
- [ ] Referencia rules existentes
- [ ] Define relación con otros agentes
- [ ] Workflow claro

### Métricas
- [ ] Define KPIs
- [ ]Tracking de tareas
- [ ] Evaluación periódica

## 🎬 Ejemplo de Uso

```
Crear un agente para validación de seguridad.

Nombre: Security Sentinel
Posición: Specialist Compound
Trigger: "seguridad", "vulnerabilidad", "security audit"
```

## ✅ Checklist de Calidad

- [ ] Frontmatter completo (name, description, keywords, version, sota_principles, harness_pattern, model_recommendation)
- [ ] Propósito claro en 1 oración
- [ ] Kit de herramientas (skills) definido
- [ ] Workflow de ejecución
- [ ] Integración con otros agentes
- [ ] Métricas de rendimiento
- [ ] Changelog
- [ ] Sigue estructura Dream Team
