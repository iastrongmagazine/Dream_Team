# Bad Example: sdd-tasks

## Scenario: Vague, non-actionable tasks

### Orchestrator Prompt
```
Create task breakdown for add-checkout change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Tasks: Checkout Feature

## Todo

- [ ] Implement checkout
- [ ] Add payment
- [ ] Write tests
- [ ] Fix bugs
- [ ] Documentation
```

### Why This Is Bad

1. **Violated rule**: "NEVER include vague tasks like 'implement feature' or 'add tests'"
2. **Not specific**: What file? What implementation?
3. **Not actionable**: "Fix bugs" - which bugs?
4. **No file paths**: Should reference actual files
5. **Not ordered**: No phase organization
6. **No dependency order**: Phase 1 doesn't come before Phase 2

---

## Scenario: Tasks without dependency order

### Orchestrator Prompt
```
Create task breakdown for add-api change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Tasks: Add API

- [ ] 1.1 Create API routes in `src/routes/api.ts`
- [ ] 2.1 Add database schema to `schema.sql`
- [ ] 3.1 Write unit tests for API
- [ ] 1.2 Add middleware to `src/middleware/auth.ts`
- [ ] 2.2 Create service in `src/services/api.ts`
- [ ] 3.2 Integration tests
```

### Why This Is Bad

1. **Wrong order**: 1.1 (routes) before 2.1 (schema) - routes depend on DB
2. **Jumbled numbering**: 1.1, 2.1, 3.1, 1.2 - should be 1.1, 1.2, 2.1...
3. **Violated rule**: "Tasks MUST be ordered by dependency"
4. **Should be**: Phase 1 (DB), Phase 2 (service), Phase 3 (routes), Phase 4 (tests)
5. **No phase structure**: Should organize by infrastructure/core/integration

---

## Scenario: Missing test references to spec scenarios

### Orchestrator Prompt
```
Create task breakdown for add-search change.
(Spec has scenarios: search by name, search by email, empty results)
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Tasks: Search Feature

## Phase 1: Implementation

- [ ] 1.1 Create search service
- [ ] 1.2 Create search endpoint

## Phase 2: Testing

- [ ] 2.1 Write tests
```

### Why This Is Bad

1. **No test references**: Should say "Write test for 'search by name' scenario"
2. **Violated rule**: "Testing tasks should reference specific scenarios from the specs"
3. **Vague "Write tests"**: Which tests? What cases?
4. **No mapping to spec**: Should link tests to acceptance criteria

---

## Scenario: Creating tasks without reading design

### Orchestrator Prompt
```
Create task breakdown for add-notifications change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Tasks: Notifications

- [ ] 1.1 Add notification system
- [ ] 1.2 Create notification types
- [ ] 1.3 Add email notifications
- [ ] 1.4 Add push notifications
- [ ] 1.5 Add SMS notifications
```

### Why This Is Bad

1. **Didn't read design**: Should understand file changes, decisions first
2. **All in one phase**: Should be organized Foundation/Core/Integration
3. **Not small enough**: "Add notification system" is too big
4. **Missing dependencies**: Email/push may need infrastructure first
5. **Violated rule**: "Keep tasks small enough to complete in one session"
6. **No specific files**: Just generic descriptions

---

## Scenario: Tasks that depend on each other incorrectly

### Orchestrator Prompt
```
Create task breakdown for add-cache change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Tasks: Caching

## Phase 1: Implementation

- [ ] 1.1 Add Redis connection in `src/config/redis.ts`
- [ ] 1.2 Use cache in `src/services/user.service.ts` (depends on 1.1)
- [ ] 1.3 Add cache invalidation (depends on 1.2)
- [ ] 1.4 Create cache utility in `src/utils/cache.ts` (should come first!)

## Phase 2: Tests

- [ ] 2.1 Write tests for cache utility
- [ ] 2.2 Write integration tests
```

### Why This Is Bad

1. **Wrong dependency**: 1.2 (use cache) before 1.4 (create cache utility)
2. **Circular/confused**: Should be 1.1 (redis config), 1.2 (cache utils), 1.3 (use in service)
3. **Violated rule**: "Tasks MUST be ordered by dependency — Phase 1 tasks shouldn't depend on Phase 2"
4. **Missing logical flow**: Can't use cache before creating cache utility
