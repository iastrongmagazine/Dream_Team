# Bad Example: sdd-design

## Scenario: Designing without reading codebase

### Orchestrator Prompt
```
Create design for refactor-api change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Design: API Refactor

## Technical Approach

Use Repository pattern with dependency injection.

## Architecture Decisions

### Decision: Database

**Choice**: PostgreSQL with Prisma

**Alternatives**: MongoDB, MySQL

**Rationale**: It's modern and popular.

## File Changes

| File | Action |
|------|--------|
| new-file.ts | Create |
| another.ts | Modify |
```

### Why This Is Bad

1. **Didn't read codebase**: Rule says "ALWAYS read the actual codebase before designing"
2. **No rationale**: "It's modern" isn't valid reason
3. **Generic recommendations**: Not based on actual project
4. **Vague file paths**: "new-file.ts" isn't real
5. **No interfaces**: Missing code examples
6. **No data flow**: Missing diagram or explanation
7. **Violated rule**: "Use the project's ACTUAL patterns and conventions"

---

## Scenario: Including implementation details

### Orchestrator Prompt
```
Create design for add-caching change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Design: Add Caching

## Implementation Details

### Redis Setup

```javascript
const redis = require('redis');
const client = redis.createClient();

client.on('error', (err) => console.log('Redis Client Error', err));

await client.connect();
```

### Cache Middleware

```javascript
app.use(async (req, res, next) => {
  const key = req.originalUrl;
  const cached = await client.get(key);
  
  if (cached) {
    return res.json(JSON.parse(cached));
  }
  
  const originalJson = res.json.bind(res);
  res.json = (data) => {
    client.setEx(key, 3600, JSON.stringify(data));
    return originalJson(data);
  };
  
  next();
});
```

### Next Steps
Just copy this code.
```

### Why This Is Bad

1. **Full implementation**: Should be in tasks/apply, not design
2. **Violated rule**: "Every decision MUST have a rationale (the why)"
3. **Code blocks in wrong phase**: Design describes approach, not code
4. **No decision rationale**: Just says "do this"
5. **"Just copy this code"**: Completely wrong approach

---

## Scenario: Not following existing patterns

### Orchestrator Prompt
```
Create design for add-user-service change.
(Project uses class-based services with dependency injection)
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Design: User Service

## Technical Approach

Use functional programming with pure functions.

## File Changes

| File | Action |
|------|--------|
| src/services/user.ts | Create |

## Interfaces

```typescript
// Using functional approach
export const getUser = (id: string) => {
  return db.users.findById(id);
};
```

[Ignores existing class-based pattern in codebase]
```

### Why This Is Bad

1. **Ignored existing patterns**: Rule says "If you find the codebase uses a pattern different from what you'd recommend, note it but FOLLOW the existing pattern"
2. **Functional vs classes**: Project uses classes, design uses functions
3. **Violated rule**: "Use the project's ACTUAL patterns and conventions, not generic best practices"
4. **Should note deviation**: Even if recommending change, should follow existing

---

## Scenario: Missing required sections

### Orchestrator Prompt
```
Create design for add-admin-panel change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Design: Admin Panel

## Approach

Build admin panel with React.

## Files

- admin.tsx
- admin.css
```

### Why This Is Bad

1. **Missing Architecture Decisions section**: Required
2. **Missing Data Flow**: Required
3. **Missing Interfaces/Contracts**: Required
4. **Missing Testing Strategy**: Required
5. **Vague files**: "admin.tsx" - where? what's the path?
6. **No rationale**: Why React? Why not Vue?
7. **Violated format**: Doesn't follow required template

---

## Scenario: Guessing open questions instead of flagging

### Orchestrator Prompt
```
Create design for add-payment-integration change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Design: Payment Integration

## Technical Approach

Use Stripe.

## Open Questions

- [x] Payment provider: Stripe (decided)
- [x] Webhook handling: Use their SDK (decided)
- [x] Error handling: Try-catch (decided)

[Guessed answers instead of flagging real unknowns]
```

### Why This Is Bad

1. **Guessed instead of asking**: Should flag real questions
2. **Not real decisions**: "Try-catch" isn't a design decision
3. **Violated rule**: "If you have open questions that BLOCK the design, say so clearly — don't guess"
4. **Fake "open questions"**: Marked as [x] but weren't real questions
5. **Should have asked**: What Stripe features? Webhook retry logic? PCI compliance?
