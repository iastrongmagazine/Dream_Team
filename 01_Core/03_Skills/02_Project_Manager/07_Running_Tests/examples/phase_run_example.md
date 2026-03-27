# Phase Run Example

Este ejemplo muestra cómo ejecutar tests de una fase específica.

## Escenario

Usuario ha trabajado en skills de planificación y quiere validar solo esa fase antes de continuar.

## Conversación

**User:** "Run phase 1 tests"

**Assistant:** "I'll run Phase 1 tests (Planning & Design: 5 skills, ~45-60 minutes)."

```bash
cd [ruta-externa] Context Bunker/AI Strong Bunker/Invictus/Amazing_World
python 07_Skill/skill-testing-automation/scripts/run_tests.py --phase 1
```

**Output:**
```
╔══════════════════════════════════════════════════════════╗
║         Running Phase 1: Planning & Design Tests         ║
║                    (5 skills)                            ║
╚══════════════════════════════════════════════════════════╝

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[1/5] Testing: brainstorming
  📍 Location: 07_Skill/brainstorming/
  🎯 Objective: Validate requirement and design exploration

  ✅ Ejercicio: "Sistema de notificaciones push para usuarios"

  Criteria Check:
  ✅ Clear requirements generated
  ✅ At least 3 use cases identified
  ✅ Technical considerations documented
  ✅ UX considerations documented
  ✅ Unresolved questions listed

  Status: ✅ FUNCTIONAL
  Duration: 10 min

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[2/5] Testing: writing-plans
  📍 Location: 07_Skill/writing-plans/
  🎯 Objective: Validate technical plan creation

  ✅ Ejercicio: "Plan de implementación para sistema de autenticación"

  Criteria Check:
  ✅ Plan follows template structure
  ✅ Technical approach clearly defined
  ✅ Implementation steps with time estimates
  ✅ Risks and mitigations identified
  ⚠️ Testing strategy partially defined (missing edge cases)

  Status: ⚠️ PARTIAL
  Duration: 12 min
  Notes: Testing section needs more detail on edge case coverage

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[3/5] Testing: writing-strategy-memos
  📍 Location: 07_Skill/writing-strategy-memos/
  🎯 Objective: Validate strategy documentation

  ✅ Ejercicio: "Strategy memo for AI Strong community growth"

  Criteria Check:
  ✅ Context and problem clearly stated
  ✅ Strategic options analyzed
  ✅ Recommendation with clear rationale
  ✅ Success metrics defined
  ✅ Risks identified

  Status: ✅ FUNCTIONAL
  Duration: 15 min

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[4/5] Testing: brand-identity
  📍 Location: 07_Skill/brand-identity/
  🎯 Objective: Validate brand guideline application

  ✅ Ejercicio: "Design component for user dashboard"

  Criteria Check:
  ✅ Design tokens applied correctly
  ✅ Voice and tone guidelines followed
  ✅ Trust and UX principles integrated
  ✅ Technical stack constraints respected

  Status: ✅ FUNCTIONAL
  Duration: 8 min

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[5/5] Testing: dieter-rams-design
  📍 Location: 07_Skill/dieter-rams-design/
  🎯 Objective: Validate design principles application

  ✅ Ejercicio: "Simplify complex settings UI"

  Criteria Check:
  ✅ Applied at least 3 of Rams' 10 principles
  ✅ Justification for each principle
  ✅ Concrete design decisions made
  ✅ User benefit clearly articulated

  Status: ✅ FUNCTIONAL
  Duration: 10 min

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔══════════════════════════════════════════════════════════╗
║                    PHASE 1 SUMMARY                       ║
╚══════════════════════════════════════════════════════════╝

Total Tests: 5/5 completed
✅ Functional: 4
⚠️ Partial: 1 (writing-plans)
❌ Failed: 0
⏭️ Skipped: 0

Success Rate: 80% functional, 20% partial
Total Duration: 55 min

⚠️ ATTENTION NEEDED:
- writing-plans: Testing strategy needs more edge case detail

📊 Full Report: 05_Examples/tests/reports/test_run_2026-01-22_1115.md
📋 Updated: 05_Examples/tests/RESULTS.md
```

**Assistant:**
```
⚠️ Phase 1 tests completed with 1 partial result

Test Summary:
- Total: 5/5 completed
- ✅ Functional: 4
- ⚠️ Partial: 1
- ❌ Failed: 0

Phase 1 (Planning & Design) is mostly working well.

**Issue to address:**
- writing-plans skill: Testing strategy section needs more detail on edge case coverage

**Recommendations:**
1. Review writing-plans skill documentation in 07_Skill/writing-plans/SKILL.md
2. Consider updating the skill to enforce edge case documentation
3. For now, manually ensure testing strategies cover edge cases when using this skill

Full report: 05_Examples/tests/reports/test_run_2026-01-22_1115.md

**Next steps:**
- Fix the partial issue, or
- Accept partial status and proceed with other phases
- Run full suite when ready for comprehensive validation
```

## Notes

- Phase-specific testing útil cuando:
  - Has modificado skills de una fase específica
  - Quieres validar un área del sistema sin correr todo
  - Estás desarrollando nuevos skills en una fase

- Fases disponibles (1-7):
  1. Planning & Design (5 skills, ~45-60 min)
  2. Development (6 skills, ~60-75 min)
  3. Testing & Debugging (3 skills, ~30-45 min)
  4. Content & Communication (4 skills, ~40-50 min)
  5. Analytics & Data (2 skills, ~25-35 min)
  6. Orchestration (2 skills, ~35-45 min)
  7. Strategy (1 skill, ~15-20 min)

- Partial results indican que el skill funciona pero con limitaciones
- El report sugiere qué hacer con cada partial/failed test
