# Good Example: sdd-propose

## Scenario: Creating proposal for JWT auth change

### Orchestrator Prompt
```
Create proposal for add-jwt-auth change.
Exploration analysis available in exploration.md.
Mode: openspec
```

### Agent Execution

```markdown
# Proposal: JWT Authentication

## Intent

Replace session-based authentication with JWT tokens to enable stateless authentication and better scalability. Current session storage in memory doesn't persist across server restarts and doesn't support horizontal scaling.

## Scope

### In Scope
- JWT middleware for token validation
- Updated login endpoint returning access + refresh tokens
- Logout with refresh token rotation
- HTTP-only cookie storage for tokens
- Token refresh endpoint

### Out of Scope
- OAuth2 social login (future work)
- Multi-factor authentication (future work)
- User registration flow changes
- API key authentication

## Approach

Use access token + refresh token with rotation:
- Access token: 15 minutes, stored in HTTP-only secure cookie
- Refresh token: 7 days, stored in HTTP-only secure cookie with rotation on each use
- Use `jsonwebtoken` library for Node.js

## Affected Areas

| Area                     | Impact   | Description                               |
|--------------------------|----------|-------------------------------------------|
| `src/middleware/auth.ts` | Modified | Replace session check with JWT validation |
| `src/routes/login.ts`    | Modified | Return JWT tokens instead of session      |
| `src/routes/logout.ts`   | Modified | Handle token blacklisting                 |
| `src/utils/jwt.ts`       | New      | JWT creation and validation utilities     |
| `src/types/auth.ts`      | Modified | Add token payload types                   |

## Risks

| Risk                 | Likelihood   | Mitigation                                  |
|----------------------|--------------|---------------------------------------------|
| XSS via cookie       | Low          | HTTP-only + secure flags on cookies         |
| Token theft          | Low          | Short-lived access tokens, refresh rotation |
| Logout not immediate | Medium       | Implement denylist for access tokens        |
| CSRF                 | Low          | SameSite=strict cookie attribute            |

## Rollback Plan

1. Revert changes to `src/middleware/auth.ts` to use old session logic
2. Restore original `login.ts` and `logout.ts` handlers
3. Delete `src/utils/jwt.ts`
4. Deploy - sessions will work immediately (tokens ignored)

## Dependencies

- `jsonwebtoken` package addition to package.json
- No database schema changes required

## Success Criteria

- [ ] Login returns JWT tokens in HTTP-only cookies
- [ ] Authenticated requests work with JWT
- [ ] Token refresh works seamlessly
- [ ] Logout invalidates tokens
- [ ] All existing tests pass
- [ ] No regression in login/logout UX
```

### Why This Is Good

1. **Clear intent**: Explains WHY this change is needed
2. **Concrete scope**: In/out of scope clearly defined
3. **High-level approach**: References exploration recommendation
4. **Specific file paths**: Not vague - real file names
5. **Risk table**: Likelihood and mitigation for each
6. **Specific rollback**: Step-by-step revert plan
7. **Success criteria**: Measurable outcomes
8. **Created proposal.md**: In correct location

---

## Return Summary

```markdown
## Proposal Created

**Change**: add-jwt-auth
**Location**: .atl/openspec/changes/add-jwt-auth/proposal.md

### Summary
- **Intent**: Replace sessions with JWT for stateless auth and scalability
- **Scope**: 5 deliverables in, 3 items deferred
- **Approach**: Access + refresh token with HTTP-only cookies
- **Risk Level**: Medium

### Next Step
Ready for specs (sdd-spec) or design (sdd-design).
```

### Why Return Summary Is Good

1. **Follows exact format**: Matches required template
2. **One-line summaries**: Concise for orchestrator
3. **Clear next step**: Tells orchestrator what's next
