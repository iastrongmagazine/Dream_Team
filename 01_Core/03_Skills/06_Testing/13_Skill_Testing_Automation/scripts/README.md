# Skill Testing Automation - Scripts

This directory contains the automation scripts for testing skills.

## Scripts

- **run_tests.py** - Main test runner with CLI
- **test_executor.py** - Executes individual skill tests
- **result_tracker.py** - Updates RESULTS.md with outcomes
- **report_generator.py** - Creates markdown reports
- **skill_validator.py** - Validates system before testing

## Usage

```bash
# Quick start (3 skills, ~15 min)
python run_tests.py --quick

# Full suite (23 skills, ~4-5 hours)
python run_tests.py --full

# Specific phase
python run_tests.py --phase 1

# Single skill
python run_tests.py --skill brainstorming

# Validate system
python run_tests.py --validate
```

## Requirements

- Python 3.7+
- No external dependencies (uses stdlib only)

## Architecture

```
run_tests.py (orchestrator)
    ├── test_executor.py (executes tests)
    ├── result_tracker.py (updates RESULTS.md)
    ├── report_generator.py (creates reports)
    └── skill_validator.py (validates system)
```

## Output

- **reports/** - Generated test reports
- **logs/** - Detailed execution logs
- **05_Examples/tests/RESULTS.md** - Updated with results

---

See [../SKILL.md](../SKILL.md) for complete documentation.
