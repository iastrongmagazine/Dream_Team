---
name: running-tests
description: QUÉ HACE: Ejecuta pruebas de skills/scripts y genera reportes de estado detallados. CUÁNDO SE EJECUTA: Al validar la integridad del sistema tras cambios, actualizaciones o antes de commits importantes.
---

# Running Tests

## When to use this skill

- When user says "Run tests", "Test the system", "Quick start tests"
- When user requests "Run phase [N] tests" or "Test skill [name]"
- After making changes to skills or system components
- Before committing work to validate functionality
- When validating system integrity after updates

## Workflow

- [ ] **1. Identify scope**: Clarify which tests to run if ambiguous
  - Quick Start: 3 tests (~15 minutes)
  - Full Suite: 23 tests (~4-5 hours)
  - Specific Phase: Tests for phase 1-7
  - Single Skill: Test one specific skill by name

- [ ] **2. Navigate to test directory**

  ```bash
  cd [Amazing_World_root_directory]
  ```

- [ ] **3. Execute appropriate test command**
  - Based on scope identified in step 1
  - Monitor for errors, timeouts, or blockers during execution
  - Wait for completion before proceeding

- [ ] **4. Review test results**
  - Read updated `05_Examples/tests/RESULTS.md`
  - Check generated report in `05_Examples/tests/reports/` (if available)
  - Count totals: Functional, Partial, Failed, Skipped

- [ ] **5. Present summary to user**
  - Include: Total tests run/completed
  - Show status with emoji indicators (✅ ⚠️ ❌ ⏭️)
  - Link to full report file
  - Highlight critical failures

- [ ] **6. Recommend next actions**
  - If failures: Suggest using systematic-debugging skill (#12)
  - If all pass: Suggest verify-and-commit skill
  - If partial: Suggest investigating specific issues

## Instructions

### Command Mapping

Choose the appropriate command based on user request:

**Quick Start** (3 skills, ~15 minutes):

```bash
python 07_Skill/skill-testing-automation/scripts/run_tests.py --quick
```

**Full Suite** (23 skills, ~4-5 hours):

```bash
python 07_Skill/skill-testing-automation/scripts/run_tests.py --full
```

**Specific Phase** (1-7):

```bash
python 07_Skill/skill-testing-automation/scripts/run_tests.py --phase N
```

Replace `N` with phase number (1-7)

**Single Skill**:

```bash
python 07_Skill/skill-testing-automation/scripts/run_tests.py --skill SKILLNAME
```

Replace `SKILLNAME` with the skill name (e.g., `brainstorming`)

### Asking for Clarification

If user request is ambiguous:

- "Run tests" → Ask: "Which tests? (quick start / full suite / specific phase)"
- Mention time estimates to help user decide
- Suggest quick start for fast validation, full suite for comprehensive check

### Error Handling

**If Python not available:**

- Report error clearly
- Suggest manual execution from `05_Examples/tests/` directory
- Provide link to `05_Examples/tests/QUICK_START.md` or `05_Examples/tests/01_README.md`

**If tests timeout:**

- Report which test timed out
- Ask user: "Continue with remaining tests or investigate this one?"
- If continuing, note the timeout in summary

**If skill-testing-automation missing:**

- Report that automation infrastructure is not found
- Suggest running tests manually using test documentation
- Provide path to `05_Examples/tests/` for manual execution

**If run_tests.py fails to execute:**

- Check Python version: `python --version` (needs 3.x)
- Try `python3` instead of `python`
- Report error message to user with full output

### Interpreting Results

**Status Indicators:**

- ✅ **Functional**: All criteria met, skill works as expected
- ⚠️ **Partial**: Some criteria met, works with limitations
- ❌ **Failed**: Criteria not met, critical issues present
- ⏭️ **Skipped**: Not executed (dependencies missing)
- 🔄 **Running**: Currently executing

**RESULTS.md Format:**

- Checkboxes: `[x]` = complete, `[~]` = partial, `[!]` = failed, `[ ]` = pending
- Progress counters show Total/Completed/Functional/Partial/Failed/Pending
- "Quick Wins" section shows completed tests
- "Necesitan Atención" shows partial tests
- "Bloqueados" shows failed tests

### Report Generation

After test execution:

- Auto-generated report in `05_Examples/tests/reports/test_run_[timestamp].md`
- Summary report in `05_Examples/tests/reports/summary_[timestamp].md`
- Individual skill logs in `05_Examples/tests/logs/` (if available)

Present the most relevant report path to user.

## Related Skills

**Before running tests:**

- **#8 executing-plans**: Implement features before testing
- **#10 antigravity-skill-creator**: Create new skills to test

**After running tests:**

- **#14 verification-before-completion**: Use before marking tasks complete (REQUIRED)
- **#2 verify-and-commit**: If all tests pass, verify and commit work
- **#12 systematic-debugging**: If tests fail, debug systematically

**For understanding tests:**

- Review `05_Examples/tests/01_README.md` for full test suite documentation
- Review `05_Examples/tests/QUICK_START.md` for quick start guide
- Review `05_Examples/tests/INDEX.md` for navigation

## Examples

See `05_Examples/` directory for:

- `quick_run_example.md` - Example of quick start execution
- `phase_run_example.md` - Example of phase-specific execution

## Tips

- **Quick validation**: Use `--quick` for fast feedback loop
- **Before commits**: Always run tests before creating commits
- **After changes**: Run tests for affected phase/skill specifically
- **Full validation**: Use `--full` before major milestones or releases
- **Time management**: Quick start = coffee break, Full suite = deep work block

## Integration with Test Suite

This skill is a user-friendly wrapper around the existing test automation system:

**Core Infrastructure:**

- Location: `07_Skill/skill-testing-automation/`
- Script: `scripts/run_tests.py`
- Documentation: `SKILL.md`, `01_README.md`

**Test Definitions:**

- Location: `05_Examples/tests/`
- Full suite: `01_README.md` (23 tests across 7 phases)
- Quick start: `QUICK_START.md` (3 essential tests)
- Phase tests: `phase-1-planning.md`, `phase-2-development.md`, `phases-3-7.md`

**Result Tracking:**

- File: `05_Examples/tests/RESULTS.md`
- Auto-updated by run_tests.py
- Manual tracking also supported

**Reports:**

- Generated in: `05_Examples/tests/reports/`
- Formats: Full report, summary, individual skill logs
- Timestamped for session tracking
