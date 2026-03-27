# Sesión 2026-03-17 - Investigación Reglas AI + Skills SDD

## Contexto

Investigar si las reglas de `.cursor` deben añadirse a `.agent` y `.claude`.

## Acciones Realizadas

### 1. Investigación Diferencias entre Carpetas AI

- `.cursor/` - 22 workflows + Skills Core + **Agent Teams Lite (SDD)**
- `.agent/` - 22 workflows + Skills Core (SIN SDD)
- `.claude/` - NO tiene workflows (usa sistema propio)

* *Hallazgo**: Solo `.cursor` tiene `02_Skills/04_Agent_Teams_Lite/` con las 9 skills SDD.

### 2. Verificación MCP Engram

- Ejecutado: `opencode mcp list`
- Resultado: **Engram connected** ✓
- El MCP estaba funcionando, no estaba desactivado.

### 3. Copia Skills SDD a `.agent`

- Creado directorio: `.agent/02_Skills/04_Agent_Teams_Lite/`
- Copiados 9 skills SDD + 3 archivos shared:
  - 01_Sdd_Init
  - 02_Sdd_Explore
  - 03_Sdd_Propose
  - 04_Sdd_Spec
  - 05_Sdd_Design
  - 06_Sdd_Tasks
  - 07_Sdd_Apply
  - 08_Sdd_Verify
  - 09_Sdd_Archive
  - 00_Shared (persistence-contract, engram-convention, openspec-convention)

### 4. Avengers Workflow

- Ejecutado: `python 04_Engine/08_Scripts_Os/55_Avengers_Workflow.py`
- Resultado: 1 ciclo completado (Vision_Review → Hulk_Compound)

## Decisiones

- **SDD en .agent**: SÍ necesario para OpenCode cuando use SDD
- **SDD en .claude**: NO necesario (usa sistema propio de agent commands)

## Próximos Pasos

- [ ] Testear skills SDD con OpenCode
- [ ] Documentar diferencias en Rules del sistema

## Archivos Modificados

- `.agent/02_Skills/04_Agent_Teams_Lite/*` (nuevo)

- --
* Sesión: 2026-03-17*
