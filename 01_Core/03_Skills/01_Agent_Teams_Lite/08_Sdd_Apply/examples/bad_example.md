# Bad Example: sdd-apply

## Scenario: Implementing without reading specs

### Orchestrator Prompt
```
Implement tasks for add-payment change.
Tasks: Phase 1 (create payment service)
Mode: openspec
```

### Agent Execution (INCORRECT)

```typescript
// src/services/payment.ts
// Created without reading spec

export function processPayment(amount: number) {
  // Just assuming it needs Stripe
  const stripe = require('stripe')('sk_test_xxx');
  return stripe.charges.create({ amount });
}
```

### Why This Is Bad

1. **Violated rule**: "ALWAYS read specs before implementing — specs are your acceptance criteria"
2. **Didn't read spec**: Should know requirements first
3. **Didn't read design**: Should know architecture decisions
4. **Wrong approach**: Assumed Stripe without checking design
5. **No type safety**: Using `any` implicitly
6. **Hardcoded API key**: Security issue

---

## Scenario: Freelancing different approach than design

### Orchestrator Prompt
```
Implement tasks for add-cache change.
Tasks: Phase 1 (Redis setup)
Mode: openspec
```

### Agent Execution (INCORRECT)

```typescript
// src/utils/cache.ts
// Design said: Use node-cache (in-memory), but agent used Redis

import Redis from 'ioredis';

const redis = new Redis();

export const cache = {
  get: (key: string) => redis.get(key),
  set: (key: string, value: string, ttl: number) => redis.setex(key, ttl, value),
  del: (key: string) => redis.del(key),
};
```

### Why This Is Bad

1. **Violated rule**: "ALWAYS follow the design decisions — don't freelance a different approach"
2. **Design said in-memory**: Used Redis instead
3. **Added infrastructure**: Redis requires Redis server
4. **Not following design**: Design clearly specified node-cache
5. **Should flag deviation**: "If you discover the design is wrong or incomplete, NOTE IT" - not just do different thing

---

## Scenario: Not marking tasks as complete

### Orchestrator Prompt
```
Implement tasks for add-auth change.
Tasks: Phase 1 (4 tasks)
Mode: openspec
```

### Agent Execution (INCORRECT)

Completed tasks 1.1-1.4 but didn't update tasks.md.

### Return Summary

```markdown
## Implementation Progress

**Change**: add-auth

### Completed Tasks
All 4 tasks completed

### Files Changed
- package.json
- src/utils/jwt.ts
- src/types/auth.ts

[Never updates tasks.md to mark [x]]
```

### Why This Is Bad

1. **Violated rule**: "In openspec mode, mark tasks complete in tasks.md AS you go, not at the end"
2. **No tracking**: Can't see what's done
3. **tasks.md still shows all incomplete**
4. **Orchestrator can't see progress**
5. **Should have marked**: `- [x] 1.1 Add jsonwebtoken...`

---

## Scenario: TDD mode but skipping RED

### Orchestrator Prompt
```
Implement tasks for add-search change.
Tasks: Phase 2, search implementation
(Project has TDD enabled)
Mode: openspec
```

### Agent Execution (INCORRECT)

```typescript
// src/services/search.ts
// Just wrote implementation directly, no tests first

export async function searchUsers(query: string): Promise<User[]> {
  // Implementation...
  return results;
}
```

### Return Summary

```markdown
## Implementation Progress

**Change**: add-search
**Mode**: TDD (detected)

### Completed Tasks
- [x] 2.1 Implement search function

[No RED test step - wrote implementation directly]
```

### Why This Is Bad

1. **Violated rule**: "If TDD mode is detected, ALWAYS follow the RED → GREEN → REFACTOR cycle — never skip RED"
2. **No failing test first**: Should have written test that fails before implementation
3. **Violated TDD principle**: Test-first is core to TDD
4. **Skipped RED**: Most important step
5. **Should have written**: Failing test first, then implementation

---

## Scenario: Implementing tasks not assigned

### Orchestrator Prompt
```
Implement tasks for add-upload change.
Tasks: Phase 1 only (tasks 1.1-1.2)
Mode: openspec
```

### Agent Execution (INCORRECT)

Completed Phase 1 tasks, then also did Phase 2 and Phase 3.

### Return Summary

```markdown
## Implementation Progress

**Change**: add-upload

### Completed Tasks
- [x] 1.1 Create upload service
- [x] 1.2 Add file type validation
- [x] 2.1 Create upload endpoint (wasn't assigned!)
- [x] 2.2 Add S3 integration (wasn't assigned!)
- [x] 3.1 Write tests (wasn't assigned!)
```

### Why This Is Bad

1. **Violated rule**: "NEVER implement tasks that weren't assigned to you"
2. **Should only do**: Tasks 1.1-1.2
3. **Overstepped**: Did 5 tasks instead of 2
4. **Orchestrator controls scope**: Can't just do everything
5. **May block other work**: Maybe tasks depend on external factors

---

## Scenario: Deviating from design without noting

### Orchestrator Prompt
```
Implement tasks for add-api change.
Mode: openspec
```

### Agent Execution (INCORRECT)

Design said: "Use REST API with JSON responses"

Implementation used: GraphQL

```typescript
// src/graphql/schema.ts
// Used GraphQL instead of REST as in design
```

### Return Summary

```markdown
## Implementation Progress

**Change**: add-api

### Completed Tasks
- [x] 1.1 Create API endpoint

### Deviations from Design
None
```

### Why This Is Bad

1. **Used different approach**: GraphQL instead of REST
2. **Didn't note deviation**: Violated "If you discover the design is wrong or incomplete, NOTE IT in your return summary"
3. **Lied in return**: Said "none" but there were deviations
4. **Violated rule**: "don't silently deviate"
5. **Should have flagged**: Note that GraphQL was used and why
