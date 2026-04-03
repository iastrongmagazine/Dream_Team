# Bad Example: sdd-spec

## Scenario: Writing implementation instead of spec

### Orchestrator Prompt
```
Write specs for add-jwt-auth change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Spec: JWT Authentication

## Implementation

### JWT Middleware

```typescript
export function authMiddleware(req: Request, res: Response, next: NextFunction) {
  const token = req.cookies.accessToken;
  if (!token) {
    return res.status(401).json({ error: 'No token' });
  }
  
  try {
    const decoded = jwt.verify(token, process.env.JWT_SECRET!);
    req.user = decoded;
    next();
  } catch (err) {
    return res.status(401).json({ error: 'Invalid token' });
  }
}
```

### Login Handler

```typescript
app.post('/login', async (req, res) => {
  const { email, password } = req.body;
  const user = await validateUser(email, password);
  
  const accessToken = jwt.sign({ userId: user.id }, secret, { expiresIn: '15m' });
  const refreshToken = jwt.sign({ userId: user.id }, refreshSecret, { expiresIn: '7d' });
  
  res.cookie('accessToken', accessToken, { httpOnly: true });
  res.cookie('refreshToken', refreshToken, { httpOnly: true });
  
  res.json({ success: true });
});
```

## Next Steps
Implement this code.
```

### Why This Is Bad

1. **Implementation, not spec**: Code belongs in design/apply, not spec
2. **Violated rule**: "DO NOT include implementation details in specs — specs describe WHAT, not HOW"
3. **No Given/When/Then**: Just code blocks
4. **No RFC 2119 keywords**: No "MUST", "SHALL", etc.
5. **No scenarios**: Just code
6. **Violated core principle**: Specs = requirements, not implementation

---

## Scenario: Missing scenarios for requirements

### Orchestrator Prompt
```
Write specs for add-user-profile change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Delta for User Profile

## ADDED Requirements

### Requirement: View Profile

The system MUST allow users to view their profile.

### Requirement: Edit Profile

The system SHOULD allow users to edit their profile.

### Requirement: Delete Profile

Users MAY delete their profile.
```

### Why This Is Bad

1. **No scenarios**: Rule says "Every requirement MUST have at least ONE scenario"
2. **Cannot test**: How would someone write tests from this?
3. **Vague requirements**: "allow users to view" - how?
4. **Missing Given/When/Then format**
5. **No testability**: Violated core TDD principle

---

## Scenario: Not reading existing specs before delta

### Orchestrator Prompt
```
Write specs for update-checkout change.
(Existing specs at .atl/openspec/specs/payments/spec.md)
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Delta for Checkout

## ADDED Requirements

### Requirement: New Payment Flow

The system MUST implement new payment flow.

[Creates delta without reading existing .atl/openspec/specs/payments/spec.md]
```

### Why This Is Bad

1. **Didn't read existing spec**: Should read `.atl/openspec/specs/payments/spec.md` first
2. **May create conflicts**: Need to understand current behavior
3. **Violated rule**: "If .atl/openspec/specs/{domain}/spec.md exists, read it to understand CURRENT behavior"
4. **Delta without context**: Don't know what's already there

---

## Scenario: Wrong format - using bullet points instead of Given/When/Then

### Orchestrator Prompt
```
Write specs for add-search change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Delta for Search

## ADDED Requirements

### Requirement: Search Users

The system MUST let users search for other users.

- User types in search box
- System shows matching results
- User clicks result
- Profile opens

### Requirement: Search Filters

The system SHOULD support filters.
- Filter by location
- Filter by name
- Filter by date
```

### Why This Is Bad

1. **No Given/When/Then**: Just bullet points
2. **Violated rule**: "ALWAYS use Given/When/Then format for scenarios"
3. **Not testable**: Can't write automated test from this
4. **Informal language**: Should be structured

---

## Scenario: Not using RFC 2119 keywords

### Orchestrator Prompt
```
Write specs for add-logging change.
Mode: openspec
```

### Agent Execution (INCORRECT)

```markdown
# Delta for Logging

## ADDED Requirements

### Requirement: Request Logging

We want to log all incoming requests.

It would be good to include response times.

Maybe add log levels.

### Requirement: Error Logging

Errors should be logged.
```

### Why This Is Bad

1. **No RFC 2119 keywords**: Should use MUST, SHALL, SHOULD, MAY
2. **Informal language**: "We want", "It would be good"
3. **Ambiguous**: "should be logged" - is it required or optional?
4. **Violated rule**: "ALWAYS use RFC 2119 keywords for requirement strength"
5. **Cannot verify compliance**: No clear requirement to test against
