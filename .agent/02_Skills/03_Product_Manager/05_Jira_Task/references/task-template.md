# Task Template

## Bug Template (Sibling Tasks)

```markdown
## Description

**Current State:**
- What's broken
- Impact on users

**Expected State:**
- What should happen

## Acceptance Criteria
- [ ] Fix bug X
- [ ] Add regression test

## Technical Notes
- Affected files: `path/to/file`

## Testing
- [ ] Reproduce bug
- [ ] Verify fix
- [ ] Run regression tests
```

## Feature Template (Parent + Children)

### Parent (User-facing)
```markdown
## Description
{User-facing description}

## User Story
As a {user}, I want to {action} so that {benefit}.

## Acceptance Criteria
- [ ] User can {do something}

## Child Tasks
- [ ] [FEATURE] {Name} (API)
- [ ] [FEATURE] {Name} (UI)
```

### Child (Technical)
```markdown
## Description
Technical implementation for {component}.

## Parent Task
[FEATURE] {Name}

## Acceptance Criteria (Technical)
- [ ] {Technical requirement}

## Related Tasks
- Parent: {link}
- Blocked by: {link}
```
