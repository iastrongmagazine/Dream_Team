# 📝 SOP Prompt: 06_Integrations

> **Carpeta destino:** `01_Core/06_Integrations/`
> **Complementa:** `01_Core/06_Integrations/` (existente)

---

## 🎯 Propósito del Prompt

Crear una integración externa (Fireflies, Granola, etc.) completa con configuración, skills y documentación.

---

## 📋 Prompt Base (Copy-Paste)

```
Eres un Especialista en Integraciones. Crea una integración completa para PersonalOS.

## 📍 Contexto del Proyecto
- **Nombre de la integración:** [NOMBRE_INTEGRACION]
- **Tipo:** [MEETING_TOOL/CRM/ANALYTICS/EXTERNAL_SERVICE]
- **Carpeta destino:** `01_Core/06_Integrations/[CARPETA]/`

## 📂 Estructura Requerida

```
01_Core/06_Integrations/[NOMBRE]/
├── README.md              ← Configuración principal
├── SETUP_SKILL.md        ← Skill de setup
├── mcp-config.json       ← Configuración MCP (si aplica)
└── skills/
    └── [skill_name]/
        └── SKILL.md
```

## 📝 Estructura README.md

```markdown
# [Nombre de la Integración]

## 🎯 Propósito
[Qué hace esta integración]

## 🔧 Configuración

### Requisitos
- [Requisito 1]
- [Requisito 2]

### Variables de Entorno
| Variable   | Descripción   | Obligatoria   |
|------------|---------------|---------------|
| [VAR]      | [desc]        | [S/N]         |

### Pasos de Setup
1. [Paso 1]
2. [Paso 2]

## ✅ Verificación
```bash
[Comando de test]
```

## 🔗 Integración con Skills
- **Skill principal:** `[ruta]`
- **Skills relacionadas:** `[ruta]`

## 🔗 Integración con Agents
- **Agent que lo usa:** `[ruta]`
```

## 📝 Estructura SETUP_SKILL.md

```markdown
---
name: [Nombre] Setup
description: Skill para configurar [herramienta]
trigger_keywords: ["setup [herramienta]", "configurar [herramienta]"]
---

# Skill: [Nombre] Setup

## 🎯 Propósito
[Qué hace esta skill de setup]

## 📋 Pasos

### 1. [Nombre del paso]
```bash
[Comando]
```

### 2. [Nombre del paso]
```bash
[Comando]
```

## ✅ Verificación
[Cómo verificar que todo está bien]
```

## 🛠️ Mejores Prácticas

### Seguridad
- [ ] NO hardcodear API keys
- [ ] Usar variables de entorno
- [ ] Validar credenciales

### Documentación
- [ ] Pasos claros paso a paso
- [ ] Screenshots si es posible
- [ ] Troubleshooting section

## ✅ Checklist de Calidad

- [ ] README.md completo
- [ ] SETUP_SKILL.md con pasos
- [ ] Variables de entorno documentadas
- [ ] Comando de verificación
- [ ] Troubleshooting
- [ ] MCP config si aplica
