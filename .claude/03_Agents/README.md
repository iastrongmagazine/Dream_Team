# 🤖 01_Agents — Sistema de Agentes Especializados

Este directorio contiene los agentes especializados del sistema Think Different AI. Cada agente tiene un dominio específico de responsabilidad.

---

## 📂 Estructura del Directorio

```
01_Agents/
├── 01_Scope_Rule_Architect/    # Arquitectura y estructura
├── 02_TDD_Test_First/         # Desarrollo guiado por tests
├── 03_React_Test_Implementer/  # Implementación de código
├── 04_React_Mentor/           # Optimización y refactor
├── 05_Security_Auditor/       # Auditoría de seguridad
├── 06_Git_Workflow_Manager/   # Gestión de Git y PRs
├── 07_Accessibility_Auditor/  # Accesibilidad WCAG
├── 08_PRD_Dashboard_Template/ # Plantillas de producto
├── 09_Design_SOP_Document/    # Documentos de diseño
├── 10_Workflow_Orchestrator/  # Orquestación TDD
├── Specialists_Squad/         # Escuadrón de especialistas
│   ├── TDD_Specialist/       # Especialista TDD
│   ├── Security_Specialist/   # Especialista Seguridad
│   ├── Git_Specialist/        # Especialista Git
│   └── Refactor_Specialist/   # Especialista Refactor
```

---

## 🏆 Catálogo de Agentes (12 + Specialists Squad)

### Agentes Principales

| #  | Agente                 | Dominio        | Prioridad | Estado |
| -- | ---------------------- | -------------- | --------- | ------ |
| 01 | Scope Rule Architect   | Arquitectura   | CRÍTICA   | ✅      |
| 02 | TDD Test-First         | Tests (RED)    | ALTA      | ✅      |
| 03 | React Test Implementer | Código (GREEN) | ALTA      | ✅      |
| 04 | React Mentor           | Refactor       | MEDIA     | ✅      |
| 05 | Security Auditor       | Seguridad      | CRÍTICA   | ✅      |
| 06 | Git Workflow Manager   | Pull Request   | ALTA      | ✅      |
| 07 | Accessibility Auditor  | Accesibilidad  | MEDIA     | ✅      |
| 08 | PRD Dashboard Template | Producto       | BAJA      | ✅      |
| 09 | Design SOP Document    | Producto       | BAJA      | ✅      |
| 10 | Workflow Orchestrator  | Orquestación   | CRÍTICA   | ✅      |

### Specialists Squad

| Especialidad  | Agente              | Función                       | Estado   |
| ------------- | ------------------- | ----------------------------- | -------- |
| TDD           | TDD_Specialist      | Dominio profundo de testing   | ✅        |
| Seguridad     | Security_Specialist | Auditorías OWASP              | ✅        |
| Git           | Git_Specialist      | Gestión avanzada de versiones | ✅        |
| Refactor      | Refactor_Specialist | Optimización de código        | ✅        |

---

## 🔄 Flujo de Trabajo TDD (7 Fases)

```
FASE 1: ARQUITECTURA
    ↓ (Scope Rule definida)
FASE 2: TESTS (RED)
    ↓ (Tests fallando)
FASE 3: IMPLEMENTACIÓN (GREEN)
    ↓ (Tests pasando)
FASE 4: REFACTORIZACIÓN (REFACTOR)
    ↓ (Código optimizado)
FASE 5: SEGURIDAD
    ↓ (OWASP auditado)
FASE 6: PULL REQUEST
    ↓ (Documentación completa)
FASE 7: ACCESIBILIDAD (opcional)
    ↓
✅ MERGE TO MAIN
```

### Duración Estimada por Fase

| Fase   | Duración   | Output                    |
| ------ | ---------- | ------------------------- |
| FASE 1 | 30-60 min  | Documento de arquitectura |
| FASE 2 | 1-2 horas  | Suite de tests (RED)      |
| FASE 3 | 2-4 horas  | Código funcional (GREEN)  |
| FASE 4 | 1-2 horas  | Código refactorizado      |
| FASE 5 | 30-60 min  | Reporte de seguridad      |
| FASE 6 | 30 min     | PR completo               |
| FASE 7 | 30-60 min  | Reporte accesibilidad     |
| **Total** | **6-11 horas** | Feature completa          |

---

## 🚀 Cómo Usar los Agentes

### Opción A: Orquestador Automático (Recomendado)

```bash
# Usar el agente Workflow Orchestrator
"Necesito implementar [funcionalidad]. Orquesta las 7 fases del flujo TDD."

El orquestador:
1. Ejecutará cada fase secuencialmente
2. Validará checkpoints entre fases
3. Generará commits por fase
4. Creará el PR final
```

### Opción B: Manual (Fase por Fase)

```bash
# FASE 1: Arquitectura
Agente #01: "Define la arquitectura para [feature]"

# FASE 2: Tests (RED)
Agente #02: "Escribe tests para [feature] basado en la arquitectura"

# FASE 3: Implementación (GREEN)
Agente #03: "Implementa código para pasar los tests de [feature]"

# FASE 4: Refactor
Agente #04: "Refactoriza [feature] optimizando performance"

# FASE 5: Seguridad
Agente #05: "Audita seguridad de [feature]"

# FASE 6: Pull Request
Agente #06: "Crea PR para [feature]"

# FASE 7: Accesibilidad (Opcional)
Agente #07: "Audita accesibilidad de [feature]"
```

---

## 📊 Métricas de Éxito

| Agente            | Métrica Clave                        | Target   |
| ----------------- | ------------------------------------ | -------- |
| #01 Architect     | Decisiones GLOBAL/LOCAL documentadas | 100%     |
| #02 TDD Test      | Coverage                             | ≥80%     |
| #03 Implementer   | Tests pasando                        | 100%     |
| #04 Mentor        | Performance mejorado                 | +20%     |
| #05 Security      | Vulnerabilidades HIGH/CRITICAL       | 0        |
| #06 Git Workflow  | Commits con Conventional Commits     | 100%     |
| #07 Accessibility | WCAG 2.1 AA compliance               | ≥85%     |

---

## 🔗 Integración con el Sistema

| Componente           | Relación                              |
| -------------------- | ------------------------------------- |
| `.agent/02_Skills/`  | 57 skills que potencian a los agentes |
| `.agent/03_Workflows/` | 21 workflows que invocan agentes      |
| `08_Scripts_Os/`     | Scripts de automatización             |
| `.claude/agents/`    | 3 subagentes nativos de Claude Code   |

---

## 📋 Principios Fundamentales

1. **Arquitectura Antes de Código** (FASE 1)
2. **Tests Antes de Implementación** (FASE 2: RED)
3. **Código Mínimo Funcional** (FASE 3: GREEN)
4. **Refactorización Segura** (FASE 4: REFACTOR)
5. **Seguridad No Negociable** (FASE 5)
6. **Documentación Completa** (FASE 6)
7. **Accesibilidad Universal** (FASE 7 - Opcional)

---

## ✅ Estado del Sistema

| Componente          | Cantidad   | Estado   |
| ------------------- | ---------- | -------- |
| Agentes Principales | 10         | ✅        |
| Specialists Squad   | 4          | ✅        |
| Total Agentes       | 14         | ✅        |
| Flujo TDD           | 7 fases    | ✅        |

---

_"Los agentes trabajan. Tú decides qué construir."_
