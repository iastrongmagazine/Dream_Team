# Task Structure Guide

## Bite-Sized Task Granularity

Each task should be 2-5 minutes:

### Format

```markdown
### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

**Step 1: Write the failing test**
[Complete code]

**Step 2: Run test to verify it fails**
Run: `pytest tests/path/test.py::test_name -v`

**Step 3: Write minimal implementation**
[Complete code]

**Step 4: Run test to verify it passes**

**Step 5: Commit**
```

## Rules

1. Exact file paths always
2. Complete code in plan (not "add validation")
3. Reference relevant skills with @ syntax
4. DRY, YAGNI, TDD, frequent commits
