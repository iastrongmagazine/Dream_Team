# Bad Example: sdd-propose

## Scenario: Missing required sections

### Orchestrator Prompt
```
Create proposal for add-search change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Proposal: Add Search Feature

## Intent

Add search to the app.

## Approach

We'll use Elasticsearch.

## Affected Files

- search.ts
- index.ts
- stuff.ts
```

### Why This Is Bad

1. **No rollback plan**: REQUIRED by rules
2. **No success criteria**: REQUIRED by rules
3. **Vague intent**: "add search" isn't specific enough
4. **Vague files**: "stuff.ts" isn't a real path
5. **No scope**: What's in/out of scope?
6. **No risks**: Not considered
7. **No dependencies**: Not identified
8. **Incomplete return summary**: Missing required format

---

## Scenario: Writing implementation details

### Orchestrator Prompt
```
Create proposal for refactor-user-service change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Proposal: Refactor User Service

## Intent

Refactor the user service to use the new architecture.

## Approach

Create `UserService` class with:
- `async getUser(id: string): Promise<User>`
- `async createUser(data: CreateUserDTO): Promise<User>`
- `async updateUser(id: string, data: UpdateUserDTO): Promise<User>`
- `async deleteUser(id: string): Promise<void>`

Use dependency injection with `Container`. Import from `src/di/container.ts`.

## Scope

Everything related to users.

## Rollback Plan

Undo what we did.
```

### Why This Is Bad

1. **Implementation in proposal**: Should be in design, not proposal
2. **Code included**: Method signatures shouldn't be here
3. **Vague scope**: "Everything related to users" isn't clear
4. **Vague rollback**: "Undo what we did" isn't actionable
5. **Violates rule**: "Keep the proposal CONCISE - it's a thinking tool, not a novel"
6. **Proposal should describe WHAT, not HOW**

---

## Scenario: Ignoring existing proposal

### Orchestrator Prompt
```
Create proposal for update-pricing change.
(Proposal already exists from previous session)
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Proposal: Update Pricing

## Intent

Change pricing tiers.

## Scope

- Change prices

## [Creates entirely new proposal, ignores existing]
```

### Why This Is Bad

1. **Didn't read existing proposal**: Rule says "READ it first and UPDATE it"
2. **Overwrote existing work**: Lost previous context
3. **Should have read**: `.atl/openspec/changes/update-pricing/proposal.md`
4. **Violated persistence contract**: Must read existing before creating

---

## Scenario: Using openspec mode but not creating files

### Orchestrator Prompt
```
Create proposal for add-admin-panel change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
## Proposal Created

**Change**: add-admin-panel

### Summary
- **Intent**: Add admin panel
- **Scope**: Many features
- **Approach**: Use admin library
- **Risk Level**: Low

[Never creates .atl/openspec/changes/add-admin-panel/proposal.md]
```

### Why This Is Bad

1. **In openspec mode**: MUST create `proposal.md` file
2. **Violated rule**: "In openspec mode, ALWAYS create the proposal.md file"
3. **Only returned summary**: Missing detailed proposal content
4. **Not following persistence contract**

---

## Scenario: Missing file paths in Affected Areas

### Orchestrator Prompt
```
Create proposal for add-api change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Proposal: Add REST API

## Intent

Add a REST API.

## Scope

- API endpoints
- Controllers
- Models

## Affected Areas

| Area            | Impact   | Description   |
|-----------------|----------|---------------|
| Backend stuff   | Modified | Changes       |
| Frontend things | New      | More changes  |
```

### Why This Is Bad

1. **No concrete paths**: Should be `src/controllers/user.ts`, not "backend stuff"
2. **Violated rule**: "Use concrete file paths in Affected Areas when possible"
3. **Vague descriptions**: "Changes" doesn't explain anything
