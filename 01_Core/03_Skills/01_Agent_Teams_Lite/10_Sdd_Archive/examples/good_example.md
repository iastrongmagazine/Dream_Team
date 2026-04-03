# Good Example: sdd-archive

## Scenario: Archiving JWT auth change

### Orchestrator Prompt
```
Archive add-jwt-auth change.
Verification passed with no critical issues.
Mode: openspec
```

### Agent Execution

#### Step 1: Sync Delta Specs to Main Specs

Read existing `.atl/openspec/specs/authentication/spec.md`:
```markdown
# Authentication Specification

## Requirements

### Requirement: Session Authentication

The system MUST maintain user sessions using server-side storage.

[existing requirements...]
```

Apply delta from `.atl/openspec/changes/add-jwt-auth/specs/authentication/spec.md`:

**ADDED Requirements:**
- JWT Token Validation → Appended to end
- Token Refresh → Appended to end  
- Secure Logout → Appended to end

**MODIFIED Requirements:**
- User Authentication → Replaced old session-based with JWT

Result in main spec:
```markdown
# Authentication Specification

## Requirements

### Requirement: JWT Token Validation

The authentication middleware MUST validate JWT access tokens...

### Requirement: Token Refresh

The system MUST provide a mechanism to exchange expired access tokens...

### Requirement: Secure Logout

The system MUST invalidate tokens on logout...

### Requirement: User Authentication (Modified)

The login endpoint MUST validate credentials and return JWT tokens...
```

#### Step 2: Move to Archive

```bash
# Move change folder to archive with date prefix
.atl/openspec/changes/add-jwt-auth/
  → .atl/openspec/changes/archive/2026-03-30-add-jwt-auth/
```

#### Step 3: Verify Archive

- [x] Main specs updated correctly
- [x] Change folder moved to archive
- [x] Archive contains all artifacts (proposal, specs, design, tasks)
- [x] Active changes directory no longer has this change

### Return Summary

```markdown
## Change Archived

**Change**: add-jwt-auth
**Archived to**: .atl/openspec/changes/archive/2026-03-30-add-jwt-auth/

### Specs Synced
| Domain         | Action   | Details                                      |
|----------------|----------|----------------------------------------------|
| authentication | Updated  | 3 added requirements, 1 modified requirement |

### Archive Contents
- proposal.md ✅
- specs/authentication/spec.md ✅
- design.md ✅
- tasks.md ✅ (20/20 tasks complete)

### Source of Truth Updated
The following specs now reflect the new behavior:
- `.atl/openspec/specs/authentication/spec.md`

### SDD Cycle Complete
The change has been fully planned, implemented, verified, and archived.
Ready for the next change.
```

### Why This Is Good

1. **Read existing spec**: Before merging delta
2. **Applied delta correctly**: ADDED appended, MODIFIED replaced
3. **Preserved non-delta requirements**: Kept existing session auth comment
4. **Used ISO date format**: 2026-03-30 prefix
5. **Verified all artifacts**: Checked archive completeness
6. **Removed from active**: No longer in changes/
7. **Follows format exactly**

---

## Scenario: Archiving new domain (no existing spec)

### Orchestrator Prompt
```
Archive add-notifications change.
Verification passed.
(This was a brand new domain - no existing spec)
Mode: openspec
```

### Agent Execution

#### Step 1: Sync Delta Specs

Check if `.atl/openspec/specs/notifications/spec.md` exists → NO

This is a new domain, so copy delta directly:

```bash
.atl/openspec/changes/add-notifications/specs/notifications/spec.md
  → .atl/openspec/specs/notifications/spec.md
```

Created directory: `.atl/openspec/specs/notifications/`

#### Step 2: Move to Archive

```bash
.atl/openspec/changes/add-notifications/
  → .atl/openspec/changes/archive/2026-03-30-add-notifications/
```

### Return Summary

```markdown
## Change Archived

**Change**: add-notifications
**Archived to**: .atl/openspec/changes/archive/2026-03-30-add-notifications/

### Specs Synced
| Domain        | Action   | Details                       |
|---------------|----------|-------------------------------|
| notifications | Created  | Full spec copied (new domain) |

### Archive Contents
- proposal.md ✅
- specs/notifications/spec.md ✅
- design.md ✅
- tasks.md ✅ (12/12 tasks complete)

### Source of Truth Updated
- `.atl/openspec/specs/notifications/spec.md` (new)

### SDD Cycle Complete
```

### Why This Is Good

1. **Detected new domain**: No existing spec to merge
2. **Copied as full spec**: Correct behavior for new domains
3. **Created directory**: Made sure specs/ folder exists

---

## Scenario: Warning before destructive merge

### Orchestrator Prompt
```
Archive remove-checkout change.
Verification passed.
(This removes many existing requirements)
Mode: openspec
```

### Agent Execution

Reads delta spec - sees 15 requirements being REMOVED.

Before proceeding, warns orchestrator:

```markdown
## Warning: Destructive Delta

**Change**: remove-checkout
**Status**: Requires confirmation before archive

### Issue
This delta REMOVES 15 requirements from the main spec:
- All payment processing requirements (8)
- All checkout flow requirements (5)
- All invoice generation requirements (2)

### Risk
This is a large removal. Please confirm you want to proceed with the archive.

### Options
1. **PROCEED**: Archive as-is (main specs will lose 15 requirements)
2. **DEFER**: Keep in active changes for review
3. **PARTIAL**: Archive only ADDED/MODIFIED sections, preserve REMOVED
```

### Why This Is Good

1. **Follows rule**: "If the merge would be destructive, WARN the orchestrator and ask for confirmation"
2. **Flags scope**: 15 requirements is significant
3. **Provides options**: Not just blindly proceeding
4. **Preserves audit trail**: Waits for confirmation

---

## Scenario: Creating archive directory if missing

### Orchestrator Prompt
```
Archive add-metrics change.
First archive operation in this project.
Mode: openspec
```

### Agent Execution

```bash
# Create archive directory (doesn't exist yet)
mkdir -p .atl/openspec/changes/archive

# Move change
.atl/openspec/changes/add-metrics/
  → .atl/openspec/changes/archive/2026-03-30-add-metrics/
```

### Return Summary

```markdown
## Change Archived

**Change**: add-metrics
**Archived to**: .atl/openspec/changes/archive/2026-03-30-add-metrics/

### Specs Synced
| Domain   | Action   | Details    |
|----------|----------|------------|
| metrics  | Created  | New domain |

### Archive Contents
- proposal.md ✅
- specs/metrics/spec.md ✅
- design.md ✅
- tasks.md ✅

### Source of Truth Updated
- `.atl/openspec/specs/metrics/spec.md` (new)
```

### Why This Is Good

1. **Follows rule**: "If .atl/openspec/changes/archive/ doesn't exist, create it"
2. **Handled missing directory**: Not an error
3. **Proceeded correctly**: Archive still works
