# Bad Example: sdd-archive

## Scenario: Archiving despite CRITICAL issues

### Orchestrator Prompt
```
Archive add-payment change.
Verification had CRITICAL issues (tests failing).
Mode: openspec
```

### Agent Execution (INCORRECT)

Ignored critical issues, proceeded with archive.

```bash
# Moved to archive anyway
.atl/openspec/changes/add-payment/
  → .atl/openspec/changes/archive/2026-03-30-add-payment/
```

### Why This Is Bad

1. **Violated rule**: "NEVER archive a change that has CRITICAL issues in its verification report"
2. **Critical issues**: Tests failing is CRITICAL
3. **Compromised main specs**: Merged bad changes into source of truth
4. **Should have refused**: Archive should have failed
5. **Violated quality gate**: Verification exists to prevent this

---

## Scenario: Not syncing specs before archiving

### Orchestrator Prompt
```
Archive add-cache change.
Verification passed.
Mode: openspec
```

### Agent Execution (INCORRECT)

Moved to archive immediately, didn't update main specs.

```bash
.atl/openspec/changes/add-cache/
  → .atl/openspec/changes/archive/2026-03-30-add-cache/
```

Main specs still don't have cache requirements!

### Why This Is Bad

1. **Violated rule**: "ALWAYS sync delta specs BEFORE moving to archive"
2. **Lost changes**: Main specs don't have cache functionality
3. **Source of truth stale**: Didn't incorporate delta
4. **Reversed order**: Should sync THEN move
5. **Breaks the cycle**: Future specs won't know about cache

---

## Scenario: Deleting instead of moving to archive

### Orchestrator Prompt
```
Archive add-search change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```bash
# Deleted instead of archiving!
rm -rf .atl/openspec/changes/add-search/
```

### Why This Is Bad

1. **Violated rule**: "The archive is an AUDIT TRAIL — never delete or modify archived changes"
2. **Lost history**: Can't reference what was done
3. **No audit trail**: Future investigation impossible
4. **Violated core principle**: Archives are immutable
5. **Should have moved**: Not deleted

---

## Scenario: Modifying archived change

### Orchestrator Prompt
```
Archive add-api change.
Found typo in archived proposal.
Mode: openspec
```

### Agent Execution (INCORRECT)

```bash
# Moved to archive
.atl/openspec/changes/add-api/
  → .atl/openspec/changes/archive/2026-03-30-add-api/

# Then edited the archived proposal to fix typo!
nano .atl/openspec/changes/archive/2026-03-30-add-api/proposal.md
```

### Why This Is Bad

1. **Violated rule**: "never delete or modify archived changes"
2. **Corrupted audit trail**: Can't trust archived version
3. **Should have known**: Archives are immutable
4. **If typo matters**: Should have kept in active, fixed, then archived

---

## Scenario: Not preserving non-delta requirements

### Orchestrator Prompt
```
Archive update-auth change.
Updates authentication spec.
Mode: openspec
```

### Agent Execution (INCORRECT)

Read existing `.atl/openspec/specs/authentication/spec.md`:
```markdown
# Auth Spec

### Requirement: Session Expiry
The system MUST expire sessions after 30 minutes.

### Requirement: Password Reset
The system MUST support password reset flow.
```

Read delta:
```markdown
# Delta for Auth

## MODIFIED Requirements

### Requirement: Session Expiry
Changed to 60 minutes.
```

Applied delta - REPLACED everything, lost Password Reset!

```markdown
# Auth Spec (after merge - WRONG!)

### Requirement: Session Expiry (Modified)
The system MUST expire sessions after 60 minutes.

[Password Reset requirement is GONE!]
```

### Why This Is Bad

1. **Violated rule**: "When merging into existing specs, PRESERVE requirements not mentioned in the delta"
2. **Lost non-delta**: Password reset wasn't in delta, but still lost
3. **Should have kept**: Everything else intact
4. **Data loss**: Important requirements disappeared

---

## Scenario: Wrong date format in archive

### Orchestrator Prompt
```
Archive add-webhooks change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```bash
# Used wrong date format
.atl/openspec/changes/add-webhooks/
  → .atl/openspec/changes/archive/March-30-2026-add-webhooks/
```

### Why This Is Bad

1. **Violated rule**: "Use ISO date format (YYYY-MM-DD) for archive folder prefix"
2. **Inconsistent**: Different format than other archives
3. **Harder to sort**: Won't sort chronologically
4. **Should be**: 2026-03-30-add-webhooks

---

## Scenario: Incomplete archive verification

### Orchestrator Prompt
```
Archive add-metrics change.
Mode: openspec
```

### Agent Execution (INCORRECT)

Moved folder to archive but didn't verify contents.

```markdown
## Change Archived

**Change**: add-metrics

### Archive Contents
- proposal.md ✅
[Never checked if other files exist]
```

Actual archive was missing design.md!

### Why This Is Bad

1. **Didn't verify**: Should confirm all artifacts present
2. **Incomplete archive**: Missing design.md
3. **Violated rule**: "Verify: Archive contains all artifacts"
4. **Broken audit trail**: Can't reference design later
