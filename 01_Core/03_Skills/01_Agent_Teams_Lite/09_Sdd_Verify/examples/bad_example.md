# Bad Example: sdd-verify

## Scenario: Only static analysis, no test execution

### Orchestrator Prompt
```
Verify add-payment change.
Mode: openspec
```

### Agent Execution (INCORRECT)

Looked at code, checked file structure, didn't run anything.

```markdown
## Verification Report

**Change**: add-payment

### Correctness
Looked at the code - seems correct.

### Issues
None found.
```

### Why This Is Bad

1. **Violated rule**: "ALWAYS execute tests — static analysis alone is not verification"
2. **Didn't run tests**: Should have executed `npm test`
3. **Didn't run build**: Should have run `npm run build`
4. **Static only**: Just looked at code
5. **No evidence**: No test results to prove compliance

---

## Scenario: Not building compliance matrix

### Orchestrator Prompt
```
Verify add-search change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
## Verification Report

**Change**: add-search

### Tests
Tests pass.

### Correctness
All requirements implemented.

[No mapping of spec scenarios to tests]
```

### Why This Is Bad

1. **No compliance matrix**: Missing required step
2. **Can't prove compliance**: No mapping of scenarios to tests
3. **Violated rule**: Should cross-reference EVERY spec scenario
4. **"All implemented" isn't enough**: Need to know WHICH tests cover WHICH scenarios

---

## Scenario: Marking compliant without passing tests

### Orchestrator Prompt
```
Verify add-cache change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
## Spec Compliance Matrix

| Requirement   | Scenario    | Test         | Result      |
|---------------|-------------|--------------|-------------|
| Cache Get     | Valid key   | (none found) | ✅ COMPLIANT |
| Cache Set     | Store value | (none found) | ✅ COMPLIANT |

[Marked COMPLIANT but no tests exist!]
```

### Why This Is Bad

1. **Violated rule**: "A spec scenario is only COMPLIANT when a test that covers it has PASSED"
2. **No tests exist**: But marked compliant anyway
3. **UNTESTED should be marked**: Not COMPLIANT
4. **False positive**: Makes it seem verified when not

---

## Scenario: Fixing issues instead of reporting

### Orchestrator Prompt
```
Verify add-auth change.
Mode: openspec
```

### Agent Execution (INCORRECT)

Found missing test coverage, so added tests itself.

```markdown
## Verification Report

**Change**: add-auth

### Issues Found
None - I added the missing tests during verification.
```

### Why This Is Bad

1. **Violated rule**: "DO NOT fix any issues — only report them"
2. **Crossed role boundary**: Verification shouldn't implement
3. **Should have reported**: "Missing test for X scenario - CRITICAL"
4. **Orchestrator decides**: What to do, not verifier

---

## Scenario: Incomplete tasks but still verifying

### Orchestrator Prompt
```
Verify add-notifications change.
Mode: openspec
```

### Agent Execution (INCORRECT)

Read tasks.md - 3 tasks incomplete but proceeded anyway.

```markdown
## Verification Report

**Change**: add-notifications

### Completeness
| Tasks incomplete | 3 |
```

continued to test execution anyway

### Why This Is Bad

1. **Shouldn't verify incomplete**: Core tasks incomplete
2. **Should have flagged**: "CRITICAL if core tasks incomplete"
3. **Wasted verification**: Can't fully verify if not implemented
4. **Violated rule**: "Verify ALL tasks are done" first

---

## Scenario: Not saving verification report

### Orchestrator Prompt
```
Verify add-webhooks change.
Mode: openspec
```

### Agent Execution (INCORRECT)

Ran verification, found issues, but didn't save report.

### Return Summary

```markdown
## Verification Report

**Change**: add-webhooks
[Full report content]

[Never saves to .atl/openspec/changes/add-webhooks/verify-report.md]
```

### Why This Is Bad

1. **In openspec mode**: MUST save report
2. **Violated rule**: "In openspec mode, ALWAYS save the report to verify-report.md"
3. **No audit trail**: Verification not persisted
4. **Can't archive**: sdd-archive needs this
5. **Lost verification**: Future sessions can't see what was found

---

## Scenario: Marking CRITICAL as non-blocking

### Orchestrator Prompt
```
Verify add-payments change.
Mode: openspec
```

### Agent Execution (INCORRECT)

Found: Tests fail (critical issue)

```markdown
## Verification Report

**Change**: add-payments

### Verdict

**PASS**

[Passed despite failing tests!]
```

### Why This Is Bad

1. **Failing tests = CRITICAL**: Rule says "Flag: CRITICAL if exit code != 0"
2. **CRITICAL issues block archive**: "must fix before archive"
3. **Wrong verdict**: Should be FAIL
4. **Violated rule**: "Be objective — report what IS, not what should be"
5. **Compromised integrity**: Verification means nothing if you ignore failures
