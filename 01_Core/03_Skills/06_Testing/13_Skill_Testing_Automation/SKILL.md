---
name: skill-testing-automation
description: QUÉ HACE: Suite automatizada para validar el funcionamiento y estructura de todas las skills. CUÁNDO SE EJECUTA: Tras actualizaciones del sistema o cambios en infraestructura para evitar regresiones. Triggers on: testing, QA, quality, validation.
---

# Skill Testing Automation

**Purpose**: Automate the execution and validation of all 23+ skills in the system, generate detailed reports, and track results over time.

---

## 🎯 When to Use This Skill

Use this skill when you need to:

- **Run automated tests** for all skills or specific subsets
- **Validate skill functionality** after system updates
- **Generate test reports** with pass/fail status
- **Track testing progress** over time
- **Identify broken skills** quickly
- **Regression testing** after changes
- **CI/CD integration** for skill validation

---

## 📋 What This Skill Does

### Core Capabilities

1. **Test Execution**
   - Runs individual skill tests
   - Executes entire test suites (phases, categories)
   - Supports quick start (3 skills) and full suite (23 skills)
   - Parallel execution for independent tests

2. **Result Documentation**
   - Auto-updates RESULTS.md with test outcomes
   - Generates detailed test reports
   - Creates timestamped logs
   - Tracks pass/fail/partial status

3. **Reporting**
   - Summary reports by phase
   - Skill-by-skill breakdown
   - Trend analysis over time
   - Issue identification and tracking

4. **Validation**
   - Verifies skill SKILL.md exists
   - Checks skill structure
   - Validates test criteria
   - Confirms expected outputs

---

## 🚀 How to Use

### Quick Commands

```bash
# Run Quick Start (3 essential skills)
python scripts/run_tests.py --quick

# Run full test suite (23 skills)
python scripts/run_tests.py --full

# Run specific phase
python scripts/run_tests.py --phase 1

# Run specific skill
python scripts/run_tests.py --skill brainstorming

# Generate report only
python scripts/run_tests.py --report
```

### Detailed Usage

#### 1. Quick Start Testing (15 minutes)

```
Invoke: "Run quick start tests"
Agent will:
1. Execute tests for: brainstorming, content-creation, systematic-debugging
2. Document results in RESULTS.md
3. Generate quick report
4. Provide go/no-go recommendation for full suite
```

#### 2. Full Suite Testing (4-5 hours)

```
Invoke: "Run full test suite"
Agent will:
1. Execute all 23 tests across 7 phases
2. Update RESULTS.md after each test
3. Generate comprehensive report
4. Identify issues and blockers
5. Provide recommendations
```

#### 3. Phase-Specific Testing

```
Invoke: "Run phase 1 tests" (or phase 2, 3, etc.)
Agent will:
1. Execute all tests in specified phase
2. Document results
3. Generate phase report
4. Suggest next steps
```

#### 4. Individual Skill Testing

```
Invoke: "Test skill: [skill-name]"
Agent will:
1. Locate skill and test definition
2. Execute test with criteria
3. Document result
4. Update tracking
```

---

## 📁 Directory Structure

```
07_Skill/skill-testing-automation/
├── SKILL.md                    # This file
├── scripts/
│   ├── run_tests.py           # Main test runner
│   ├── test_executor.py       # Individual test execution
│   ├── result_tracker.py      # Results documentation
│   ├── report_generator.py    # Report creation
│   └── skill_validator.py     # Skill structure validation
├── templates/
│   ├── test_result.md         # Individual test result template
│   ├── phase_report.md        # Phase summary template
│   └── full_report.md         # Complete suite report template
└── 05_Examples/
    ├── quick_start_run.md     # Example quick start execution
    └── full_suite_run.md      # Example full suite execution
```

---

## 🔧 Test Execution Process

### For Each Test

1. **Preparation**
   - Read test definition from 05_Examples/tests/
   - Verify skill exists and is accessible
   - Load test criteria and expected outcomes

2. **Execution**
   - Invoke skill with test exercise
   - Capture all outputs and interactions
   - Time the execution
   - Monitor for errors

3. **Validation**
   - Check against success criteria
   - Validate output format
   - Verify expected behavior
   - Assess completeness

4. **Documentation**
   - Update RESULTS.md with status
   - Create detailed test log
   - Capture screenshots/outputs if applicable
   - Note any issues or observations

5. **Reporting**
   - Add to phase summary
   - Update overall progress
   - Flag for review if needed

---

## 📊 Test Status Definitions

- **✅ Functional**: All criteria met, skill works as expected
- **⚠️ Partial**: Some criteria met, skill works with limitations
- **❌ Fallido**: Criteria not met, skill has critical issues
- **⏭️ Skipped**: Test not executed (dependency missing, etc.)
- **🔄 Running**: Test currently in progress

---

## 📝 Output Files

### Generated Automatically

1. **RESULTS.md** (updated)
   - Progress checkboxes
   - Status for each test
   - Quick wins, issues, blockers

2. **reports/test*run*[timestamp].md**
   - Complete test execution log
   - Detailed results
   - Timing information
   - Issues encountered

3. **reports/summary\_[timestamp].md**
   - High-level overview
   - Pass/fail statistics
   - Recommendations
   - Next steps

4. **logs/test*[skill-name]*[timestamp].log**
   - Detailed execution log for each skill
   - Outputs captured
   - Errors and warnings

---

## 🎯 Success Criteria for This Skill

This skill is working correctly if it can:

- [x] Execute Quick Start (3 tests) in < 20 minutes
- [x] Execute Full Suite (23 tests) in < 6 hours
- [x] Auto-update RESULTS.md with accurate status
- [x] Generate readable reports
- [x] Identify and flag failing tests
- [x] Handle errors gracefully
- [x] Support parallel execution where possible
- [x] Provide clear next steps

---

## 🔄 Integration with Existing Tests

### Test Definitions Location

All test definitions are in `05_Examples/tests/`:

- `QUICK_START.md` - 3 essential skills
- `phase-1-planning.md` - 5 planning tests
- `phase-2-development.md` - 6 development tests
- `phases-3-7.md` - 12 consolidated tests
- `01_README.md` - Complete 23-test suite

### Test Format

Each test includes:

- **Objective**: What the test validates
- **Exercise**: Specific task to perform
- **Steps**: How to execute
- **Criteria**: Success conditions
- **Expected Result**: What should happen

The automation reads these definitions and executes accordingly.

---

## 🛠️ Advanced Features

### 1. Regression Testing

```bash
# Compare current run with previous
python scripts/run_tests.py --full --compare-with reports/test_run_2026-01-20.md
```

### 2. Continuous Monitoring

```bash
# Run tests on schedule (e.g., daily)
python scripts/run_tests.py --full --schedule daily
```

### 3. Custom Test Suites

```bash
# Run only creative skills
python scripts/run_tests.py --category creative

# Run only Invictus skills
python scripts/run_tests.py --location invictus
```

### 4. Parallel Execution

```bash
# Run independent tests in parallel
python scripts/run_tests.py --full --parallel
```

---

## 📈 Reporting Features

### Summary Report Includes

- Total tests executed
- Pass/fail/partial breakdown
- Execution time per test and total
- Skills by category (functional, partial, failed)
- Trend comparison (if previous runs exist)
- Top issues identified
- Recommendations for fixes

### Detailed Report Includes

- Test-by-test results
- Full output captures
- Error messages and stack traces
- Timing breakdown
- Criteria checklist for each test
- Observations and notes

---

## 🐛 Error Handling

### Graceful Degradation

- If a skill is missing, mark as SKIPPED and continue
- If a test definition is malformed, log error and skip
- If execution times out, mark as FAILED with timeout note
- If dependencies missing, document and skip dependent tests

### Recovery

- Save progress after each test
- Allow resuming from last checkpoint
- Preserve partial results even if suite crashes

---

## 🔍 Validation Checks

Before running tests, the automation validates:

- [x] All skill directories exist
- [x] All SKILL.md files are present
- [x] Test definitions are well-formed
- [x] Required dependencies are available
- [x] Output directories are writable

---

## 💡 Best Practices

1. **Run Quick Start First**
   - Validates core functionality
   - Identifies major issues early
   - Takes only 15 minutes

2. **Review Results Incrementally**
   - Check RESULTS.md after each phase
   - Address blockers before continuing
   - Don't wait until end to review

3. **Use Parallel Execution Wisely**
   - Only for truly independent tests
   - Monitor resource usage
   - Some skills may conflict if run simultaneously

4. **Keep Test Definitions Updated**
   - When skills change, update test criteria
   - Add new tests for new skills
   - Archive obsolete tests

5. **Track Trends Over Time**
   - Compare reports across runs
   - Identify degradation early
   - Celebrate improvements

---

## 🎓 Example Workflows

### Workflow 1: Daily Validation

```bash
# Morning: Quick check
python scripts/run_tests.py --quick

# If all pass: confidence in system
# If any fail: investigate before deep work
```

### Workflow 2: Pre-Release Testing

```bash
# Before major release
python scripts/run_tests.py --full --parallel

# Review report
# Fix critical issues
# Re-run failed tests
# Document known issues
```

### Workflow 3: New Skill Validation

```bash
# After creating new skill
python scripts/run_tests.py --skill my-new-skill

# Verify it passes
# Add to appropriate phase
# Update test suite
```

---

## 📚 Related Resources

- [Test Suite Documentation](../../../05_Examples/tests/01_README.md)
- [Quick Start Guide](../../../05_Examples/tests/QUICK_START.md)
- [Results Tracker](../../../05_Examples/tests/RESULTS.md)
- [Skills Checklist](../../../03_Knowledge/04_Docs/tests/04_Docs/SKILLS_TEST_CHECKLIST.md)
- [System Validation](../../../03_Knowledge/04_Docs/reports/system/SYSTEM_VALIDATION.md)

---

## 🔄 Maintenance

### Adding New Tests

1. Create test definition in appropriate phase file
2. Follow existing format (objective, exercise, steps, criteria)
3. Run validation: `python scripts/run_tests.py --validate`
4. Test manually first
5. Add to automation

### Updating Existing Tests

1. Modify test definition in 05_Examples/tests/
2. Update criteria if skill behavior changed
3. Re-run affected tests
4. Update documentation

### Archiving Obsolete Tests

1. Move to `05_Examples/tests/archived/`
2. Document reason for archival
3. Update test counts in reports

---

## 🎯 Success Metrics

Track these metrics over time:

- **Pass Rate**: % of tests passing
- **Execution Time**: Total time for full suite
- **Coverage**: % of skills with tests
- **Reliability**: Consistency of results across runs
- **Issue Resolution**: Time from failure to fix

---

## 🚨 Troubleshooting

### Common Issues

**Issue**: Tests timing out

- **Solution**: Increase timeout in config, check for infinite loops

**Issue**: Inconsistent results

- **Solution**: Check for race conditions, ensure clean state between tests

**Issue**: Missing dependencies

- **Solution**: Run `python scripts/run_tests.py --check-deps`

**Issue**: Report generation fails

- **Solution**: Check write permissions, verify templates exist

---

## 📞 Support

For issues with this skill:

1. Check logs in `logs/` directory
2. Review error messages in reports
3. Consult [VALIDATION.md](../../../05_Examples/tests/VALIDATION.md)
4. Create issue in tracking system

---

**Last Updated**: 2026-01-21
**Version**: 1.0
**Maintainer**: Invictus Amazing World System

## Esencia Original
> **Propósito:** 14_Skill_Testing_Automation - propósito del skill
> **Flujo:** Pasos principales del flujo de trabajo

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Error común
  - **Por qué**: Explicación
  - **Solución**: Cómo evitar

## 📁 Progressive Disclosure

> Para información detallada:
- [references/guide.md](references/guide.md) — Guía completa

## 🛠️ Scripts

- [scripts/run.py](scripts/run.py) — Script principal

## 💾 State Persistence

Guardar en:
-  — Evaluaciones
-  — Documentación

