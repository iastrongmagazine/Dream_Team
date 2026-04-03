# PLAN: Fix Auto Improvement System Issues

**Date:** 2026-03-30  
**ID:** 2026-03-30-002  
**Status:** PLANNED

---

## Executive Summary

Fix 1,338 issues detected by the Auto Improvement System:
- **49 BROKEN_IMPORT** (HIGH priority) - Python files con imports que fallan
- **1,289 NAMING_INCONSISTENCY** (LOW priority) - Archivos con naming inconsistente

---

## Issue Breakdown

| Type                 | Count   | Severity   | Auto-Fixable   |
|----------------------|---------|------------|----------------|
| BROKEN_IMPORT        | 49      | HIGH       | Yes            |
| NAMING_INCONSISTENCY | 1289    | LOW        | No             |

---

## Priority Strategy

### Priority 1: BROKEN_IMPORT (CRITICAL)
These cause actual failures. Must fix.

**Pattern identificado:**
- `Legacy_Backup/` - Archivos viejos sin mantener
- `04_`, `05_` prefix files - Scripts renombrados que rompieron imports

**Approach:**
1. Analizar los 49 archivos con imports rotos
2. Determinar si el archivo destino existe
3. Fix del import path O eliminar el import si no se usa
4. Verificar con test de import

### Priority 2: NAMING_INCONSISTENCY (ANALYSIS)
Estos son 1,289 archivos con naming inconsistent. Antes de fixear:

**Questions:**
- Son solo diferencias de snake_case vs camelCase?
- Son archivos duplicados?
- Son referencias a archivos que ya no existen?

**Approach:**
1. Sample de 50 archivos para entender el patrón
2. Decidir si el fix bulk tiene sentido O es riesgo de romper
3. Si tiene sentido → crear script de bulk fix
4. Si no → documentar y marcar como "won't fix"

---

## Tasks

### Phase 1: Fix Broken Imports

- [ ] **1.1** Get full list of 49 broken import files with exact error
- [ ] **1.2** Categorize by fix type:
  - [ ] Fix import path (archivo existe, path incorrecto)
  - [ ] Add dependency (archivo no existe, se necesita crear)
  - [ ] Remove dead import (se usa pero no existe)
  - [ ] Mark as TODO (legacy, no critical)
- [ ] **1.3** Fix imports that exist → update paths
- [ ] **1.4** Remove dead imports → clean code
- [ ] **1.5** Test: `python -c "import ..."` para cada archivo fixeado

### Phase 2: Analyze Naming Inconsistencies

- [ ] **2.1** Sample 50 files from naming issues
- [ ] **2.2** Identify patterns:
  - [ ] snake_case vs camelCase
  - [ ] Duplicates with different names
  - [ ] Old references
- [ ] **2.3** Decision: Fix bulk O Won't Fix
- [ ] **2.4** If Fix: Create auto-fix script
- [ ] **2.5** If Won't Fix: Document rationale

---

## Risk Analysis

| Risk                   | Impact   | Mitigation                  |
|------------------------|----------|-----------------------------|
| Break working code     | HIGH     | Test cada fix individually  |
| Too many naming issues | MEDIUM   | Focus only on critical ones |
| False positives        | LOW      | Manual review before apply  |

---

## Success Criteria

- [ ] 0 BROKEN_IMPORT issues remaining
- [ ] NAMING_INCONSISTENCY analyzed with decision documented
- [ ] Health score improves from 75/100

---

## Timeline Estimate

- Phase 1: 30 min - 1 hour
- Phase 2: 1-2 hours (analysis + decision)
- Total: 2-3 hours

---

## Related Files

- `04_Operations/01_Auto_Improvement/01_Engine/detector.py` - Source of detection
- `04_Operations/01_Auto_Improvement/02_Rules/auto_fix_rules.json` - Auto-fix rules
- `get_issues.py` - Script to get current issues
