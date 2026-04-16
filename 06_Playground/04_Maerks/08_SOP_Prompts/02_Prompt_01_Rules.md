# 📝 SOP Prompt: 01_Rules

> **Carpeta destino:** `01_Core/01_Rules/`
> **Complementa:** `01_Core/01_Rules/` (existente), `Maerks/09_Dream_Team.md`

---

## 🎯 Propósito del Prompt

Crear una regla del sistema (rule) que defina comportamiento, estándares o protocolos para los agentes.

---

## 📋 Prompt Base (Copy-Paste)

```
Eres un Arquitecto de Reglas de Sistema. Crea una regla completa para PersonalOS.

## 📍 Contexto del Proyecto
- **Nombre de la regla:** [NOMBRE_DE_LA_REGLA]
- **Tipo:** [CONTEXTO/MOTOR/BASE/ESTRATEGIA/INTEGRACIÓN]
- **Ubicación actual de reglas:** `01_Core/01_Rules/`

## 📂 Estructura Requerida
Guardar en: `01_Core/01_Rules/NN_Nombre_Regla.mdc`

## 🎭 Pilar associated
- **Pilar Base:** Si es fundamental → `02_Pilar_Base.mdc`
- **Pilar Motor:** Si es de ejecución → `03_Pilar_Motor.mdc`
- **Pilar Estrategia:** Si es de planificación → `04_Pilar_Estrategia.mdc`

## 📝 Estructura del Documento (FORMATO .MDC)

```markdown
---
name: [Nombre de la Regla]
description: [Descripción corta de qué hace]
globs: ["patrón1/**/*.md", "patrón2/**/*.py"]
alwaysApply: [true/false]
priority: [1-10]
---

# 🔒 [Nombre de la Regla]

## 📖 Descripción
[Descripción extendida: qué problema resuelve, por qué existe]

## 🎯 Cuándo Aplicar
- Cuando se detecta: [patrón/keyword/contexto]
- En fase: [Planificación/Ejecución/Revisión/Documentación]
- Para agentes: [lista de agentes]

## 📋 Reglas Específicas

### Regla 1: [Nombre]
- **Qué:** [qué hacer]
- **Cuándo:** [condición]
- **Por qué:** [rationale]

### Regla 2: [Nombre]
[Igual estructura]

## ⚠️ Excepciones
- [Excepción 1 y cuándo aplica]
- [Excepción 2 y cuándo aplica]

## 🔗 Dependencias
- **Rules relacionadas:** `01_Core/01_Rules/[otras reglas]`
- **Skills relacionadas:** `01_Core/03_Skills/[skill]`
- **Workflows:** `01_Core/00_Workflows/[workflow]`

## 📊 Validación
- **Cómo verificar:** [comando/test/review]
- **Qué validar:** [lista de checks]

## 🔄 Historial de Cambios
| Fecha      | Cambio           | Autor    |
|------------|------------------|----------|
| YYYY-MM-DD | Creación inicial | [Nombre] |
```

## 🛠️ Integración con Sistema Existente

### Reglas Fundamentales a Consultar
- `01_Core/01_Rules/01_Context_Protocol.mdc` - Protocolo de contexto
- `01_Core/01_Rules/05_ritual-integrity.mdc` - Integridad de rituales

### Patrones de Nomenclatura
- **Número de regla:** 2 dígitos (01-99)
- **Extensión:** `.mdc` (Markdown + Frontmatter)
- **Nombre:** `XX_Nombre_Descriptivo.mdc`

## ⚡ Best Practices SOTA

1. **Globs específicos**: Define patrones precisos, no `**/*`
2. **Frontmatter completo**: name, description, globs, alwaysApply, priority
3. **Casos de borde**: Documenta explícitamente qué NO aplicar
4. **Dependencias claras**: Lista otras rules/skills que necesitan cargar

## 🎬 Ejemplo de Uso

```
Crear una regla para validar que todo código Python tenga type hints.

Nombre: Python Type Hints Required
Prioridad: 8
Globs: ["01_Core/**/*.py", "08_Scripts_Os/**/*.py"]
```

## ✅ Checklist de Calidad

- [ ] Frontmatter completo (name, description, globs, alwaysApply, priority)
- [ ] Casos de uso claros (cuándo aplicar)
- [ ] Casos de borde/excepciones documentados
- [ ] Dependencias con otras rules
- [ ] Validación definida
- [ ] Sigue numbering secuencial
- [ ] Extensión `.mdc` correcta
