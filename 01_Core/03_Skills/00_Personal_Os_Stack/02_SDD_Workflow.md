---
name: "sdd-workflow"
description: "Spec-Driven Development - Metodología completa para desarrollo estructurado con specs, diseño y tareas"
---

# SDD Workflow

Spec-Driven Development (SDD) es la metodología principal del PersonalOS.

## Fases del SDD

| Fase | Comando | Propósito |
|------|---------|-----------|
| Explore | `/sdd:explore` | Investigar código/ideas |
| Propose | `/sdd:propose` | Crear propuesta |
| Spec | `/sdd:spec` | Escribir specs detalladas |
| Design | `/sdd:design` | Diseño técnico |
| Tasks | `/sdd:tasks` | Descomponer en tareas |
| Apply | `/sdd:apply` | Implementar código |
| Verify | `/sdd:verify` | Verificar contra specs |
| Archive | `/sdd:archive` | Archivar y documentar |

## Cuándo Usar SDD

- Features sustanciales que requieren specs
- Cambios arquitectónicos
- Nuevas integraciones
- Cualquier trabajo que necesite planificación

## Artefactos

Cada fase genera artefactos que se guardan en:
- **Engram** (memoria persistente)
- **openspec/** (archivos locales)

## Reglas

1. NO implementar sin specs aprobadas
2. Cada tarea debe ser atómica
3. Verificar contra specs antes de marcar como done
4. Documentar decisiones en el proceso
