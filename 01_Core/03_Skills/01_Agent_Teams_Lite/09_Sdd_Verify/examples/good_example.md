# Good Example: sdd-verify

## Scenario: Verifying JWT auth implementation

### Orchestrator Prompt
```
Verify add-jwt-auth change.
All tasks complete in tasks.md.
Mode: openspec
```

### Agent Execution

#### Step 1: Check Completeness

Read `tasks.md`:
- Total: 20 tasks
- Complete: 20 tasks
- Incomplete: 0

✅ All tasks done

#### Step 2: Check Correctness (Static)

Read `specs/authentication/spec.md`, search codebase:

| Requirement          | Status        | Evidence                                            |
|----------------------|---------------|-----------------------------------------------------|
| JWT Token Validation | ✅ Implemented | `src/middleware/auth.ts` has verifyAccessToken call |
| Token Refresh        | ✅ Implemented | `src/routes/refresh.ts` has rotation logic          |
| Secure Logout        | ✅ Implemented | `src/routes/logout.ts` clears cookies               |

#### Step 3: Check Coherence

Read `design.md`, verify decisions followed:

| Decision          | Followed?   | Notes                               |
|-------------------|-------------|-------------------------------------|
| HTTP-only cookies | ✅ Yes       | Cookie options set `httpOnly: true` |
| Refresh rotation  | ✅ Yes       | New token issued on each refresh    |
| jsonwebtoken lib  | ✅ Yes       | Imported and used                   |

#### Step 4: Run Tests (Real Execution)

Detect test runner: Jest (from package.json)

```bash
$ npm test

PASS tests/unit/jwt.test.ts
PASS tests/unit/middleware.test.ts
PASS tests/integration/auth.test.ts
PASS tests/integration/refresh.test.ts

Tests: 18 passed, 0 failed
```

#### Step 4c: Build Check

```bash
$ npm run build

✓ 12 modules built.
Build time: 2.3s
```

✅ Build passed

#### Step 5: Spec Compliance Matrix

| Requirement          | Scenario          | Test                                   | Result      |
|----------------------|-------------------|----------------------------------------|-------------|
| JWT Token Validation | Valid token       | `auth.test.ts > allows valid token`    | ✅ COMPLIANT |
| JWT Token Validation | Expired → refresh | `refresh.test.ts > refreshes expired`  | ✅ COMPLIANT |
| JWT Token Validation | No token → 401    | `auth.test.ts > rejects missing token` | ✅ COMPLIANT |
| Token Refresh        | Valid refresh     | `refresh.test.ts > issues new tokens`  | ✅ COMPLIANT |
| Token Refresh        | Invalid refresh   | `refresh.test.ts > rejects invalid`    | ✅ COMPLIANT |
| Secure Logout        | User logs out     | `auth.test.ts > clears cookies`        | ✅ COMPLIANT |

**Compliance: 6/6 scenarios compliant**

#### Persist Report

Writes to `.atl/openspec/changes/add-jwt-auth/verify-report.md`

### Return Summary

```markdown
## Verification Report

**Change**: add-jwt-auth
**Version**: 1.0

---

### Completeness
| Metric           | Value   |
|------------------|---------|
| Tasks total      | 20      |
| Tasks complete   | 20      |
| Tasks incomplete | 0       |

---

### Build & Tests Execution

**Build**: ✅ Passed
```
✓ 12 modules built.
```

**Tests**: ✅ 18 passed / 0 failed / 0 skipped

**Coverage**: 87% / threshold: 80% → ✅ Above threshold

---

### Spec Compliance Matrix

| Requirement          | Scenario          | Test                                   | Result      |
|----------------------|-------------------|----------------------------------------|-------------|
| JWT Token Validation | Valid token       | `auth.test.ts > allows valid token`    | ✅ COMPLIANT |
| JWT Token Validation | Expired → refresh | `refresh.test.ts > refreshes expired`  | ✅ COMPLIANT |
| JWT Token Validation | Missing token     | `auth.test.ts > rejects missing token` | ✅ COMPLIANT |
| Token Refresh        | Valid refresh     | `refresh.test.ts > issues new tokens`  | ✅ COMPLIANT |
| Token Refresh        | Invalid refresh   | `refresh.test.ts > rejects invalid`    | ✅ COMPLIANT |
| Secure Logout        | User logs out     | `auth.test.ts > clears cookies`        | ✅ COMPLIANT |

**Compliance summary**: 6/6 scenarios compliant

---

### Correctness (Static — Structural Evidence)
| Requirement          | Status        | Notes                                |
|----------------------|---------------|--------------------------------------|
| JWT Token Validation | ✅ Implemented | Middleware validates on each request |
| Token Refresh        | ✅ Implemented | Rotation logic in refresh endpoint   |
| Secure Logout        | ✅ Implemented | Cookie clearing on logout            |

---

### Coherence (Design)
| Decision          | Followed?   | Notes                             |
|-------------------|-------------|-----------------------------------|
| HTTP-only cookies | ✅ Yes       | httpOnly: true in all cookies     |
| Refresh rotation  | ✅ Yes       | New token issued, old invalidated |
| jsonwebtoken      | ✅ Yes       | Used throughout                   |

---

### Issues Found

**CRITICAL**: None

**WARNING**: None

**SUGGESTION**: None

---

### Verdict

**PASS**

All tasks complete, all tests pass, all spec scenarios verified with passing tests.
```

### Why This Is Good

1. **Executed tests**: Not just static analysis - ran real tests
2. **Ran build**: Verified compilation
3. **Spec compliance matrix**: Every scenario mapped to passing test
4. **COMPLIANT means passed test**: ✅ only when test exists AND passes
5. **Saved report**: Wrote to verify-report.md
6. **No critical issues**: Clean verification
7. **Follows exact format**

---

## Scenario: Verification with warnings

### Agent Execution

Finds issues but not blocking:

- Missing edge case tests (warning)
- Build has deprecation warnings (warning)

### Return Summary

```markdown
## Verification Report

**Change**: add-api

### Verdict

**PASS WITH WARNINGS**

### Issues Found

**WARNING**: Edge case scenarios lack test coverage
- Search with special characters
- Empty search results edge case

**SUGGESTION**: Build warnings about deprecated method
- Consider updating to new API
```

### Why This Is Good

1. **Still passes**: No critical issues
2. **Warns about gaps**: Informs without blocking
3. **Distinguishes severity**: CRITICAL vs WARNING vs SUGGESTION
4. **Follows rule**: "CRITICAL issues = must fix before archive"
