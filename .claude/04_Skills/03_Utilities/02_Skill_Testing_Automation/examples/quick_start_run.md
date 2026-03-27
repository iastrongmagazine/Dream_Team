# Quick Start Example Run

This is an example of running the quick start tests.

## Command

```bash
python scripts/run_tests.py --quick
```

## Expected Output

```
🚀 Running Quick Start Tests (3 skills, ~15 minutes)
============================================================

[1/3] Testing: brainstorming
------------------------------------------------------------
   📝 Exercise: Sistema de notificaciones push para usuarios...
   📂 Location: Amazing World/07_Skill/brainstorming
   📝 Updated RESULTS.md for brainstorming
✅ brainstorming: FUNCTIONAL

[2/3] Testing: content-creation
------------------------------------------------------------
   📝 Exercise: Hilo de 5 tweets sobre 'Productividad con IA'...
   📂 Location: Invictus/07_Skill/content-creation
   📝 Updated RESULTS.md for content-creation
✅ content-creation: FUNCTIONAL

[3/3] Testing: systematic-debugging
------------------------------------------------------------
   📝 Exercise: TypeError: Cannot read property 'name' of undefined...
   📂 Location: Amazing World/07_Skill/systematic-debugging
   📝 Updated RESULTS.md for systematic-debugging
✅ systematic-debugging: FUNCTIONAL

============================================================
✅ Quick Start Complete in 12.3 minutes
📊 Report: reports/quick_start_20260121_220125.md
📝 Results updated in: 05_Examples/tests/RESULTS.md
```

## Generated Report

**File**: `reports/quick_start_20260121_220125.md`

```markdown
# Quick Start Test Report

**Date**: 2026-01-21 22:01:25
**Duration**: 12.3 minutes
**Tests**: 3

## Summary

- ✅ Functional: 3
- ⚠️ Partial: 0
- ❌ Failed: 0

## Results

### ✅ brainstorming

- **Status**: FUNCTIONAL
- **Time**: 245.2s
- **Criteria Met**: 4

### ✅ content-creation

- **Status**: FUNCTIONAL
- **Time**: 312.8s
- **Criteria Met**: 5

### ✅ systematic-debugging

- **Status**: FUNCTIONAL
- **Time**: 178.5s
- **Criteria Met**: 5

## Recommendation

✅ **GO**: All tests passed or partial. Safe to proceed with full suite.
```

## Updated RESULTS.md

The following sections were updated:

### Progress Section

```
Total Skills: 23
Completados: 3
Funcionales: 3
Parciales: 0
Fallidos: 0
Pendientes: 20

Tasa de éxito: 13%
```

### Quick Wins Section

```
## ✅ Quick Wins (Completados)

- ✅ brainstorming - 2026-01-21 22:01
- ✅ content-creation - 2026-01-21 22:06
- ✅ systematic-debugging - 2026-01-21 22:09
```

### Checkboxes

```
- [x] Test 01: brainstorming
- [x] Test 15: content-creation
- [x] Test 12: systematic-debugging
```

## Next Steps

Based on successful quick start:

1. ✅ Core skills working
2. ✅ System validated
3. ⬜ Ready for Phase 1 (5 tests)
4. ⬜ Or proceed to full suite (23 tests)

**Recommendation**: Proceed with confidence to full suite or phase-by-phase testing.
