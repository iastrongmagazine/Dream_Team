---
title: "Integración Selectiva: EveryInc/compound-engineering-plugin v2.45.0"
type: feat
date: 2026-03-19
status: plan
priority: high
---

# Integración Selectiva: EveryInc/compound-engineering-plugin v2.45.0

## Overview

Sincronizar el fork local de `compound-engineering-plugin` con el upstream oficial (EveryInc) mientras se preservan las personalizaciones únicas del usuario. El objetivo es obtener las 25+ skills nuevas de upstream sin perder: `skill-creator`, `publish.yml`, `app/`, `spec/`, y configuraciones propias.

## Problem Statement

El fork actual (`01_Every/`) está en versión **2.36.0** con **20 skills**. Upstream está en **2.45.0** con **45 skills**. El gap incluye:

- Workflows autónomos (`lfg`, `slfg`)
- CE workflows maduros (`ce-plan`, `ce-work`, `ce-review`, `ce-compound`)
- Testing nativo (`test-browser`, `test-xcode`, `feature-video`)
- Bug handling completo (`report-bug`, `reproduce-bug`, `resolve-parallel`)
- Release automation (`release-please`)

**Riesgo:** Un merge ciego rompería las personalizaciones del usuario.

## Proposed Solution

**Estrategia: Overlay Integration**

1. Clonar upstream fresco en zona temporal
2. Aplicar personalizaciones como "overlay" sobre upstream limpio
3. Validar y testear el resultado
4. Commit y deploy

## Análisis Previo

### Contenido ÚNICO del Fork (que upstream NO tiene)

| Asset                     | Ubicación Actual                                               | Valor                                               |
|---------------------------|----------------------------------------------------------------|-----------------------------------------------------|
| `skill-creator`           | `plugins/compound-engineering/skills/skill-creator/`           | 3 scripts únicos: init, package, validate           |
| `brainstorming`           | `plugins/compound-engineering/skills/brainstorming/`           | Nueva versión con proceso 4 fases                   |
| `publish.yml`             | `.github/workflows/publish.yml`                                | npm publishing con Bun                              |
| `release-docs`            | `.claude/commands/release-docs.md`                             | Comando personalizado                               |
| `triage-prs`              | `.claude/commands/triage-prs.md`                               | Comando de triaje                                   |
| `Rails demo`              | `app/`, `spec/`                                                | Ejemplo didáctico SQL injection                     |
| `bunfig.toml`             | raíz                                                           | Coverage threshold 80%                              |
| Package scope             | `@every-env` vs `@claude-every`                                | Branding diferenciado                               |

### Skills NUEVAS en Upstream (28+)

| Categoría                  | Skills                                                                                                                                                             |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **CE Workflows**           | `ce-brainstorm`, `ce-compound`, `ce-compound-refresh`, `ce-ideate`, `ce-plan`, `ce-plan-beta`, `ce-review`, `ce-work`, `deepen-plan`, `deepen-plan-beta`           |
| **Testing**                | `test-browser`, `test-xcode`, `feature-video`                                                                                                                      |
| **Bug Handling**           | `report-bug`, `reproduce-bug`, `resolve-parallel`, `resolve-todo-parallel`, `heal-skill`                                                                           |
| **Automation**             | `lfg`, `slfg`                                                                                                                                                      |
| **Utilities**              | `changelog`, `claude-permissions-optimizer`, `create-agent-skill`, `deploy-docs`, `generate_command`, `triage`, `agent-browser`, `agent-native-audit`              |

### Fixes Críticos Incluidos

| Fix                                    | Impacto                                   |
|----------------------------------------|-------------------------------------------|
| Context7 API key auth                  | Previene rate limits                      |
| Serial mode para reviews               | Previene crashes de context               |
| Cross-platform compatibility           | Works con Codex/Gemini/Copilot            |
| Daily sequence numbers                 | Previene colisiones de archivos           |

## Plan de Ejecución

### Fase 1: Preparación y Backup

- [ ] 1.1 Verificar que `Safe_Backup/01_Every/` esté actualizado y limpio
- [ ] 1.2 Crear backup adicional: `Safe_Backup/01_Every_Pre_Integration/`
- [ ] 1.3 Limpiar estado residual de merges fallidos anteriores
- [ ] 1.4 Verificar conectividad a GitHub

### Fase 2: Zona de Integración

- [ ] 2.1 Crear directorio: `07_Projects/01_Projects_Lab/Every_Sync_Zone/`
- [ ] 2.2 Clonar upstream fresco: `git clone https://github.com/EveryInc/compound-engineering-plugin.git`
- [ ] 2.3 Verificar dependencias: `bun install`
- [ ] 2.4 Ejecutar tests base: `bun test`

### Fase 3: Aplicación de Personalizaciones (Overlay)

#### 3.1 Skills Propias
- [ ] 3.1.1 Copiar `plugins/compound-engineering/skills/skill-creator/` → zona de sync
- [ ] 3.1.2 Copiar `plugins/compound-engineering/skills/brainstorming/` → zona de sync
- [ ] 3.1.3 Verificar que no existan conflictos de nombres

#### 3.2 Commands Propios
- [ ] 3.2.1 Copiar `.claude/commands/release-docs.md` → zona de sync
- [ ] 3.2.2 Copiar `.claude/commands/triage-prs.md` → zona de sync
- [ ] 3.2.3 Actualizar referencias si es necesario

#### 3.3 Workflows de CI/CD
- [ ] 3.3.1 Copiar `.github/workflows/publish.yml` → zona de sync
- [ ] 3.3.2 Fusionar con `release-please` de upstream (configurar para que trabajen en conjunto)
- [ ] 3.3.3 Mantener scope `@every-env` en `package.json`

#### 3.4 Ejemplo Didáctico (Rails Demo)
- [ ] 3.4.1 Crear directorio: `examples/rails-demo/`
- [ ] 3.4.2 Mover `app/` → `examples/rails-demo/app/`
- [ ] 3.4.3 Mover `spec/` → `examples/rails-demo/spec/`
- [ ] 3.4.4 Actualizar referencias en documentación

#### 3.5 Configuraciones
- [ ] 3.5.1 Integrar `bunfig.toml` (coverage 80%)
- [ ] 3.5.2 Mantener `.releaserc.json` si es compatible
- [ ] 3.5.3 Revisar `package.json` para dependencias nuevas

### Fase 4: Conciliación

- [ ] 4.1 Resolver cualquier conflicto de merge en configuración
- [ ] 4.2 Asegurar que `workflows:*` y `ce:*` coexistan (backwards compatibility)
- [ ] 4.3 Actualizar `AGENTS.md` con filosofía de Compound Engineering (mantener nota existente)
- [ ] 4.4 Verificar que todas las skills nuevas estén registradas

### Fase 5: Validación

- [ ] 5.1 Ejecutar suite de tests: `bun test`
- [ ] 5.2 Ejecutar Structure Auditor de PersonalOS
- [ ] 5.3 Verificar que no haya archivos huérfanos
- [ ] 5.4 Testear commands personalizados (`release-docs`, `triage-prs`)
- [ ] 5.5 Validar JSON de `.mcp.json` si se modifica

### Fase 6: Commit y Deploy

- [ ] 6.1 Commit: `feat: sync EveryInc v2.45.0 + integrate custom assets`
- [ ] 6.2 Push a origin/main
- [ ] 6.3 Verificar que ambos remotos (Engram, Invictus) estén sincronizados
- [ ] 6.4 Actualizar documentación de PersonalOS (Inventario, etc.)

## Edge Cases y Mitigaciones

| Edge Case                                        | Mitigación                                                                           |
|--------------------------------------------------|--------------------------------------------------------------------------------------|
| Conflicto de versión en `package.json`           | Merge manual, priorizar upstream para dependencias                                   |
| Skills con mismo nombre                          | Upstream gana, preservar scripts únicos en subcarpeta                                |
| CI workflows colisionan                          | Configurar `release-please` para tags, `publish.yml` para npm only en tags           |
| Archivos `.lock` desincronizados                 | Usar `bun.lock` de upstream, re-run `bun install`                                    |

## RTM (Requirements Traceability Matrix)

| Req ID             | Requirement                          | Validation                                                 | Priority             |
|--------------------|--------------------------------------|------------------------------------------------------------|----------------------|
| INT-01             | Upstream v2.45.0 integrado           | `git log` muestra commits de upstream                      | P0                   |
| INT-02             | Skills propias preservadas           | Skills únicas existen en zona de sync                      | P0                   |
| INT-03             | Tests pasan                          | `bun test` 100% pass                                       | P0                   |
| INT-04             | CI/CD funcional                      | Workflows no colisionan                                    | P1                   |
| INT-05             | Documentación actualizada            | AGENTS.md incluye nota de filosofía                        | P1                   |
| INT-06             | Personalizaciones intactas           | `skill-creator`, `publish.yml`, `app/` presentes           | P0                   |

## Evals

### Pre-Integration
- [ ] Verificar backup creado
- [ ] Verificar upstream clonado limpio

### Post-Integration
- [ ] `bun test` pasa 100%
- [ ] Skills contadas: 45+ (20 propias + 25 nuevas)
- [ ] Commands: `release-docs`, `triage-prs` funcionales
- [ ] Workflows: `publish.yml` y `release-please` configurados
- [ ] No hay archivos duplicados o huérfanos

## Resources

- [Upstream repo](https://github.com/EveryInc/compound-engineering-plugin)
- [Fork local](https://github.com/iastrongmagazine/compound-engineering-plugin)
- [PersonalOS AGENTS.md](../../00_Core/AGENTS.md)

## Status

- [x] Plan creado
- [ ] Aprobado por usuario
- [ ] En ejecución
- [ ] Validado
- [ ] Deployado
