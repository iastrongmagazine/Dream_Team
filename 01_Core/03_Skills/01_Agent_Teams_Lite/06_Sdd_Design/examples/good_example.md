# Good Example: sdd-design

## Scenario: Creating design for JWT auth

### Orchestrator Prompt
```
Create design for add-jwt-auth change.
Mode: openspec
```

### Agent Execution

First, read relevant files to understand existing patterns:
- Read `src/middleware/auth.ts` - current session middleware
- Read `src/routes/login.ts` - current login logic
- Read `src/routes/logout.ts` - current logout logic
- Read existing `package.json` - check for jsonwebtoken

### Agent Creates

```markdown
# Design: JWT Authentication

## Technical Approach

Implement stateless JWT authentication with access + refresh token rotation:
- Access token: 15-minute JWT in HTTP-only cookie
- Refresh token: 7-day JWT with rotation on each use
- Token denylist for immediate logout

This maps to proposal's approach of "Access + refresh token with HTTP-only cookies".

## Architecture Decisions

### Decision: Token Storage

**Choice**: HTTP-only secure cookies for both access and refresh tokens

**Alternatives considered**: 
- LocalStorage for access token (rejected: XSS vulnerability)
- Authorization header with Bearer token (rejected: more complex client implementation)
- Session storage (rejected: doesn't scale horizontally)

**Rationale**: HTTP-only cookies are secure against XSS, require no client-side code changes beyond cookie handling, and work with existing cookie infrastructure.

### Decision: Refresh Token Rotation

**Choice**: Rotate refresh token on each use (invalidate old, issue new)

**Alternatives considered**:
- Single refresh token without rotation (rejected: no revocation capability)
- Redis-based token blacklist (rejected: additional infrastructure complexity)

**Rationale**: Rotation provides implicit logout capability and limits damage from token theft. Simpler than blacklist infrastructure.

### Decision: JWT Library

**Choice**: `jsonwebtoken` npm package

**Alternatives considered**:
- `jose` (rejected: more complex API)
- `njwt` (rejected: less maintained)

**Rationale**: Battle-tested, TypeScript types included, widely used.

## Data Flow

```
┌─────────┐     POST /login      ┌─────────────┐
│  Client │ ──────────────────▶  │  Login API  │
└─────────┘                      └─────────────┘
      │                                  │
      │ Set-Cookie: access_token        │
      │◀─────────────────────────────────┤
      │ Set-Cookie: refresh_token       │
                                      │
      │ Access Request                  │
      │ Cookie: access_token            ▼
      ▼                          ┌─────────────┐
┌─────────┐ ◀─────────────────── │  Middleware │
│Protected│                      └─────────────┘
│ Endpoint│                             │
└─────────┘                             │
      │                            Validate JWT
      │                                  │
      │ 401 if expired                  ▼
      │◀────────────────────────── ┌─────────────┐
                                  │   JWT       │
                                  │  Utilities  │
                                  └─────────────┘
```

## File Changes

| File                     | Action   | Description                               |
|--------------------------|----------|-------------------------------------------|
| `src/utils/jwt.ts`       | Create   | JWT creation, validation, refresh logic   |
| `src/middleware/auth.ts` | Modify   | Replace session check with JWT validation |
| `src/routes/login.ts`    | Modify   | Return JWT tokens in cookies              |
| `src/routes/logout.ts`   | Modify   | Invalidate refresh token                  |
| `src/routes/refresh.ts`  | Create   | Token refresh endpoint                    |
| `src/types/auth.ts`      | Modify   | Add JWT payload types                     |
| `package.json`           | Modify   | Add jsonwebtoken dependency               |

## Interfaces / Contracts

```typescript
// src/types/auth.ts
interface JwtPayload {
  userId: string;
  email: string;
  iat: number;
  exp: number;
}

interface TokenPair {
  accessToken: string;
  refreshToken: string;
}

interface AuthConfig {
  accessTokenSecret: string;
  refreshTokenSecret: string;
  accessTokenExpiry: string; // '15m'
  refreshTokenExpiry: string; // '7d'
}
```

## Testing Strategy

| Layer       | What to Test                             | Approach                     |
|-------------|------------------------------------------|------------------------------|
| Unit        | JWT creation, validation, refresh logic  | Mock secrets, test with jest |
| Unit        | Middleware token extraction & validation | Mock request/response        |
| Integration | Login → protected endpoint flow          | Supertest with test DB       |
| Integration | Token refresh flow                       | Supertest                    |
| E2E         | Full auth user journey                   | Playwright                   |

## Migration / Rollback

No migration required - this is new authentication path alongside existing (will be swapped in middleware priority).

## Open Questions

- [ ] None - all decisions resolved in exploration
```

### Return Summary

```markdown
## Design Created

**Change**: add-jwt-auth
**Location**: .atl/openspec/changes/add-jwt-auth/design.md

### Summary
- **Approach**: Access + refresh JWT with HTTP-only cookies, token rotation
- **Key Decisions**: 3 decisions documented (token storage, rotation, library)
- **Files Affected**: 3 new, 3 modified, 0 deleted
- **Testing Strategy**: unit + integration + e2E planned

### Open Questions
None

### Next Step
Ready for tasks (sdd-tasks).
```

### Why This Is Good

1. **Read actual code**: Investigated before designing
2. **Follows proposal approach**: Maps to proposal's intent
3. **Decisions with rationale**: Each has "why" explained
4. **ASCII diagram**: Clear data flow
5. **Concrete file paths**: Real files from codebase
6. **Interfaces in code blocks**: TypeScript examples
7. **Testing strategy**: Layer-by-layer approach
8. **No open questions**: Everything resolved
9. **Follows format exactly**

---

## Scenario: Design with open questions

### Orchestrator Prompt
```
Create design for add-database-migration change.
Mode: openspec
```

### Agent Execution

```markdown
# Design: Database Migration System

## Technical Approach

Create a migration system to manage database schema changes.

## Architecture Decisions

### Decision: Migration Tool

**Choice**: Use `node-pg-migrate`

**Alternatives considered**: 
- Custom migration scripts (rejected: reinventing wheel)
- TypeORM migrations (rejected: couples to ORM)

**Rationale**: Best-in-class for Node/PostgreSQL, supports rollback.

[... more sections ...]

## Open Questions

- [ ] **PG_VERSION**: Should we support PostgreSQL 13 or 14+ only?
  - Team preference: 14+ (more features)
  - Risk: Some users on 13
- [ ] **MIGRATION_NAMING**: kebab-case or snake_case?
  - Current codebase uses snake_case
- [ ] **CI_INTEGRATION**: Run migrations automatically in CI or manual?
  - Need team input on safety preference
```

### Why This Is Good

1. **Acknowledges open questions**: Instead of guessing
2. **Flagged clearly**: "Need team input"
3. **Violated rule handled properly**: "If you have open questions that BLOCK the design, say so clearly — don't guess"
