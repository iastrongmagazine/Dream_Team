# 📝 SOP Prompt: 00_Workflows

> **Carpeta destino:** `01_Core/00_Workflows/`
> **Complementa:** `01_Core/01_Rules/`, `Maerks/09_Dream_Team.md`

---

## 🎯 Propósito del Prompt

Crear un workflow completo y operacional para el sistema PersonalOS, siguiendo patrones Marvel (Iron Man, Thor, etc.) y estándares SOTA.

---

## 📋 Prompt Base (Copy-Paste)

```
Eres un Arquitecto de Sistemas AI. Crea un workflow completo para PersonalOS.

## 📍 Contexto del Proyecto
- **Nombre:** [NOMBRE_DEL_WORKFLOW]
- **Tipo:** Workflow de [PLANIFICACIÓN/EJECUCIÓN/REVISIÓN/AUDITORÍA/DOCUMENTACIÓN]
- **Fuente de verdad:** `01_Core/03_Skills/` para skills, `01_Core/01_Rules/` para reglas

## 📂 Estructura Requerida
Guardar en: `01_Core/00_Workflows/NN_Nombre_Workflow.md`

## 🎭 Metodología
Usa la metodología de "Compound Engineering":
1. **Plan** → Define objetivos y steps
2. **Work** → Implementa
3. **Review** → Verifica calidad
4. **Compound** → Documenta lessons learned

## 📝 Estructura del Documento

```markdown
---
name: [Nombre]
description: [Descripción corta]
trigger_keywords: [[keyword1], [keyword2]]
always_apply: [true/false]
---

# [Nombre del Workflow]

## 🎯 Propósito
[Una oración: qué hace este workflow]

## 🔄 Cuándo Ejecutar
- Cuando el usuario dice: "[trigger phrases]"
- Cuando se detecta: [condiciones]

## 📋 Pasos

### Phase 1: [Nombre]
1. [Step 1]
2. [Step 2]

### Phase 2: [Nombre]
1. [Step 1]

## 🔗 Dependencias
- Skills: `[ruta a skill]`
- Rules: `[ruta a regla]`
- Agents: `[ruta a agente]`

## 📊 Métricas
- [Métrica 1]
- [Métrica 2]

## 🔄 Rollback
[Qué hacer si falla]
```

## 🛠️ Integración con Reglas Existentes

### Reglas a Cargar (OBLIGATORIO)
- `01_Core/01_Rules/01_Context_Protocol.mdc` - Protocolo de contexto
- `01_Core/01_Rules/03_Pilar_Motor.mdc` - Pilar motor
- `Maerks/09_Dream_Team.md` - Metodología del equipo

### Skills Recomendadas
- `01_Core/03_Skills/00_Compound_Engineering/` - Para compound engineering
- `01_Core/03_Skills/01_Agent_Teams_Lite/` - Para agent teams

## ⚡ Best Practices SOTA

1. **Adversarial Evaluation**: Incluye siempre un "evaluator" que cuestione el output
2. **Progressive Disclosure**: Muestra info gradualmente, no todo upfront
3. **Checkpoint Validation**: Valida en puntos clave, no solo al final
4. **Observability**: Incluye logging claro de cada paso

## 🎬 Ejemplo de Uso

```
/sdd-new workflow-seo-audit

Nombre: SEO Audit Workflow
Tipo: Auditoría
Trigger: "auditar seo", "revisar seo", "seo audit"
```

## ✅ Checklist de Calidad

- [ ] Tiene trigger keywords claros
- [ ] Incluye phases con pasos específicos
- [ ] Referencia skills existentes
- [ ] Referencia rules existentes
- [ ] Tiene métricas definidas
- [ ] Tiene plan de rollback
- [ ] Sigue metodología Compound Engineering
