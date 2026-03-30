# Good Example: sdd-apply

## Scenario: Implementing JWT tasks with TDD

### Orchestrator Prompt
```
Implement tasks for add-jwt-auth change.
Tasks: Phase 1, tasks 1.1-1.4 (Foundation)
Mode: openspec
```

### Agent Execution

First, read context:
1. Read `specs/authentication/spec.md` - understand requirements
2. Read `design.md` - understand architecture decisions
3. Read `tasks.md` - see tasks to complete
4. Read `package.json` - check current dependencies
5. Read `src/types/auth.ts` - understand existing types

### Task 1.1: Add jsonwebtoken dependency

```bash
# Added to package.json:
"jsonwebtoken": "^9.0.0",
"@types/jsonwebtoken": "^9.0.0",
```

### Task 1.2-1.3: Create JWT utilities

```typescript
// src/utils/jwt.ts
import jwt from 'jsonwebtoken';
import type { JwtPayload, AuthConfig } from '../types/auth';

export function createAccessToken(payload: Omit<JwtPayload, 'iat' | 'exp'>, config: AuthConfig): string {
  return jwt.sign(payload, config.accessTokenSecret, {
    expiresIn: config.accessTokenExpiry,
  });
}

export function createRefreshToken(payload: Omit<JwtPayload, 'iat' | 'exp'>, config: AuthConfig): string {
  return jwt.sign(payload, config.refreshTokenSecret, {
    expiresIn: config.refreshTokenExpiry,
  });
}

export function verifyAccessToken(token: string, config: AuthConfig): JwtPayload | null {
  try {
    return jwt.verify(token, config.accessTokenSecret) as JwtPayload;
  } catch {
    return null;
  }
}

export function verifyRefreshToken(token: string, config: AuthConfig): JwtPayload | null {
  try {
    return jwt.verify(token, config.refreshTokenSecret) as JwtPayload;
  } catch {
    return null;
  }
}
```

### Task 1.4: Add AuthConfig type

```typescript
// src/types/auth.ts (adding to existing)
export interface AuthConfig {
  accessTokenSecret: string;
  refreshTokenSecret: string;
  accessTokenExpiry: string;
  refreshTokenExpiry: string;
}
```

### Mark tasks complete

Updates `tasks.md`:
```markdown
## Phase 1: Foundation

- [x] 1.1 Add `jsonwebtoken` dependency to `package.json`
- [x] 1.2 Create `src/utils/jwt.ts` with JWT creation utility
- [x] 1.3 Create `src/utils/jwt.ts` with JWT validation utility
- [x] 1.4 Add `AuthConfig` type to `src/types/auth.ts`
```

### Return Summary

```markdown
## Implementation Progress

**Change**: add-jwt-auth
**Mode**: Standard

### Completed Tasks
- [x] 1.1 Add `jsonwebtoken` dependency to `package.json`
- [x] 1.2 Create `src/utils/jwt.ts` with JWT creation utility
- [x] 1.3 Create `src/utils/jwt.ts` with JWT validation utility
- [x] 1.4 Add `AuthConfig` type to `src/types/auth.ts`

### Files Changed
| File | Action | What Was Done |
|------|--------|---------------|
| `package.json` | Modified | Added jsonwebtoken dependencies |
| `src/utils/jwt.ts` | Created | JWT creation and validation utilities |
| `src/types/auth.ts` | Modified | Added AuthConfig interface |

### Deviations from Design
None — implementation matches design.

### Issues Found
None.

### Remaining Tasks
- Phase 2: Core Implementation (5 tasks)
- Phase 3: Integration (3 tasks)
- Phase 4: Testing (6 tasks)
- Phase 5: Cleanup (2 tasks)

### Status
4/20 tasks complete. Ready for next batch (Phase 2).
```

### Why This Is Good

1. **Read context first**: Read specs, design, tasks before coding
2. **Followed specs**: JWT creation/validation matched spec requirements
3. **Followed design**: Used AuthConfig from design
4. **Match existing patterns**: TypeScript, proper imports
5. **Marked tasks complete**: Updated tasks.md as went
6. **Follows return format**: Exact structure
7. **No deviations**: Matches design

---

## Scenario: TDD workflow execution

### Orchestrator Prompt
```
Implement tasks for add-search change.
Tasks: Phase 2, tasks 2.1-2.3 (search implementation with TDD)
Mode: openspec
(Project has TDD enabled)
```

### Agent Execution

### Task 2.1: RED - Write failing test first

```typescript
// tests/unit/search.test.ts
describe('searchUsers', () => {
  it('should return users matching name query', async () => {
    // Given: mock DB with users
    const mockDb = [{ id: '1', name: 'John' }];
    
    // When: search with 'John'
    const result = await searchUsers('John', { db: mockDb });
    
    // Then: return matching user
    expect(result).toEqual([{ id: '1', name: 'John' }]);
  });
});
```

Run test → **FAILS** (searchUsers doesn't exist yet)

### Task 2.2: GREEN - Write minimum code

```typescript
// src/services/search.ts
export async function searchUsers(query: string, options: { db: any[] }) {
  return options.db.filter(user => user.name.includes(query));
}
```

Run test → **PASSES**

### Task 2.3: REFACTOR - Clean up

```typescript
// src/services/search.ts (refactored)
import type { User } from '../types/user';

export async function searchUsers(query: string, options: { db: User[] }): Promise<User[]> {
  if (!query.trim()) {
    return [];
  }
  
  const normalizedQuery = query.toLowerCase();
  return options.db.filter(user => 
    user.name.toLowerCase().includes(normalizedQuery)
  );
}
```

Run test → **STILL PASSES**

### Why This Is Good

1. **RED first**: Wrote failing test before implementation
2. **Minimal GREEN**: Only what's needed to pass
3. **REFACTOR after**: Cleaned up with better naming
4. **Test passes after each**: Verified at each stage
5. **Follows TDD cycle**: RED → GREEN → REFACTOR
6. **Violated rule not broken**: "If TDD mode is detected, ALWAYS follow the RED → GREEN → REFACTOR cycle"
