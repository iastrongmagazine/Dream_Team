# Quick Run Example

Este ejemplo muestra cómo ejecutar el Quick Start de tests (3 skills esenciales, ~15 minutos).

## Escenario

Usuario quiere validar rápidamente que el sistema funciona antes de hacer un commit.

## Conversación

**User:** "Run quick start tests"

**Assistant:** "I'll run the quick start test suite (3 essential skills, ~15 minutes)."

```bash
cd [ruta-externa] Context Bunker/AI Strong Bunker/Invictus/Amazing_World
python 07_Skill/skill-testing-automation/scripts/run_tests.py --quick
```

**Output:**
```
╔══════════════════════════════════════════════════════════╗
║         Running Quick Start Tests (3 skills)             ║
╚══════════════════════════════════════════════════════════╝

Phase 1: Planning & Design
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[1/3] Testing: brainstorming
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
  Duration: 2 min

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phase 4: Content & Communication
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[2/3] Testing: content-creation
  📍 Location: 07_Skill/content-creation/
  🎯 Objective: Validate content generation and guidelines

  ✅ Ejercicio: "Post educativo sobre prompt engineering"

  Criteria Check:
  ✅ Content follows brand voice
  ✅ AI Strong principles reflected
  ✅ Actionable content provided
  ✅ ZINKING style optional elements present

  Status: ✅ FUNCTIONAL
  Duration: 5 min

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Phase 3: Testing & Debugging
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[3/3] Testing: systematic-debugging
  📍 Location: 07_Skill/systematic-debugging/
  🎯 Objective: Validate debugging methodology

  ✅ Ejercicio: Simulated import error in Python module

  Criteria Check:
  ✅ Hypothesis formulated
  ✅ Step-by-step investigation logged
  ✅ Root cause identified
  ✅ Fix applied and verified
  ✅ Prevention steps documented

  Status: ✅ FUNCTIONAL
  Duration: 8 min

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

╔══════════════════════════════════════════════════════════╗
║                    SUMMARY                               ║
╚══════════════════════════════════════════════════════════╝

Total Tests: 3/3 completed
✅ Functional: 3
⚠️ Partial: 0
❌ Failed: 0
⏭️ Skipped: 0

Success Rate: 100%
Total Duration: 15 min

📊 Full Report: 05_Examples/tests/reports/test_run_2026-01-22_1047.md
📋 Updated: 05_Examples/tests/RESULTS.md
```

**Assistant:**
```
✅ Quick start tests completed successfully

Test Summary:
- Total: 3/3 completed
- ✅ Functional: 3
- ⚠️ Partial: 0
- ❌ Failed: 0

All essential skills are working as expected. The system is ready for commits.

Full report: 05_Examples/tests/reports/test_run_2026-01-22_1047.md

**Next steps:**
Since all tests passed, you can now:
1. Verify your work is complete using verification-before-completion skill (#14)
2. Create a commit using verify-and-commit skill
```

## Notes

- Quick start ejecuta 3 skills representativos de diferentes fases
- Toma ~15 minutos (útil para validación rápida)
- Ideal para pre-commit checks o validación después de cambios menores
- Si algún test falla, el report sugiere usar systematic-debugging
