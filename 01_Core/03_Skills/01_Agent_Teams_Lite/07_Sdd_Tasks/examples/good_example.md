# Good Example: sdd-tasks

## Scenario: Creating tasks for JWT auth change

### Orchestrator Prompt
```
Create task breakdown for add-jwt-auth change.
Mode: openspec
```

### Agent Execution

First read design.md to understand all file changes and decisions:
- File changes: 3 new, 3 modified
- Decisions: token storage, refresh rotation, library choice

### Agent Creates

```markdown
# Tasks: JWT Authentication

## Phase 1: Foundation

- [ ] 1.1 Add `jsonwebtoken` dependency to `package.json`
- [ ] 1.2 Create `src/utils/jwt.ts` with JWT creation utility
- [ ] 1.3 Create `src/utils/jwt.ts` with JWT validation utility
- [ ] 1.4 Add `AuthConfig` type to `src/types/auth.ts`

## Phase 2: Core Implementation

- [ ] 2.1 Modify `src/routes/login.ts` to generate JWT token pair
- [ ] 2.2 Set HTTP-only cookies in login response
- [ ] 2.3 Modify `src/middleware/auth.ts` to validate JWT from cookie
- [ ] 2.4 Attach user payload to request object in middleware
- [ ] 2.5 Create `src/routes/refresh.ts` for token refresh endpoint

## Phase 3: Integration & Logic

- [ ] 3.1 Implement refresh token rotation in refresh endpoint
- [ ] 3.2 Add refresh token to denylist on logout in `src/routes/logout.ts`
- [ ] 3.3 Modify logout to clear cookies from client

## Phase 4: Testing

- [ ] 4.1 Write unit tests for `src/utils/jwt.ts` - creation
- [ ] 4.2 Write unit tests for `src/utils/jwt.ts` - validation
- [ ] 4.3 Write integration tests: login → protected request
- [ ] 4.4 Write integration tests: token refresh flow
- [ ] 4.5 Write integration tests: logout invalidates token
- [ ] 4.6 Verify all existing tests still pass

## Phase 5: Cleanup

- [ ] 5.1 Remove unused session-related code from `src/middleware/auth.ts`
- [ ] 5.2 Update API documentation for new auth flow
```

### Return Summary

```markdown
## Tasks Created

**Change**: add-jwt-auth
**Location**: .atl/openspec/changes/add-jwt-auth/tasks.md

### Breakdown
| Phase   | Tasks   | Focus                             |
|---------|---------|-----------------------------------|
| Phase 1 | 4       | Foundation - types, utilities     |
| Phase 2 | 5       | Core - login, middleware, refresh |
| Phase 3 | 3       | Integration - rotation, logout    |
| Phase 4 | 6       | Testing - unit + integration      |
| Phase 5 | 2       | Cleanup - remove old code, docs   |
| Total   | 20      |                                   |

### Implementation Order
1. Phase 1 (Foundation) must complete first - other phases depend on jwt.ts
2. Phase 2 (Core) before Phase 3 (Integration)
3. Phase 4 (Testing) can run after each implementation phase
4. Phase 5 (Cleanup) last - needs complete implementation

### Next Step
Ready for implementation (sdd-apply).
```

### Why This Is Good

1. **Hierarchical numbering**: 1.1, 1.2, 2.1, etc.
2. **Concrete actions**: "Add jsonwebtoken to package.json" not "Add auth library"
3. **Ordered by dependency**: Phase 1 before Phase 2
4. **Phase organization**: Infrastructure → Core → Integration → Testing → Cleanup
5. **Specific file paths**: Real files from design
6. **Testable tasks**: Each can be verified
7. **Reference spec scenarios**: Test tasks reference acceptance criteria
8. **Follows format exactly**

---

## Scenario: Tasks with TDD integration

### Orchestrator Prompt
```
Create task breakdown for add-user-search change.
(Project has TDD enabled in config.yaml)
Mode: openspec
```

### Agent Creates

```markdown
# Tasks: User Search Feature

## Phase 1: Foundation

- [ ] 1.1 Add search query validation types to `src/types/search.ts`

## Phase 2: Core Implementation

- [ ] 2.1 RED: Write failing test for search function in `tests/unit/search.test.ts`
- [ ] 2.2 GREEN: Implement basic search in `src/services/search.ts`
- [ ] 2.3 REFACTOR: Clean up search implementation

- [ ] 2.4 RED: Write failing test for search with filters
- [ ] 2.5 GREEN: Add filter logic to search service
- [ ] 2.6 REFACTOR: Extract filter parsing

- [ ] 2.7 RED: Write failing test for search pagination
- [ ] 2.8 GREEN: Add pagination to search results
- [ ] 2.9 REFACTOR: Optimize query builder

## Phase 3: Integration

- [ ] 3.1 Connect search endpoint to service in `src/routes/search.ts`
- [ ] 3.2 Add request validation middleware

## Phase 4: Testing

- [ ] 4.1 Write integration tests: search endpoint flow
- [ ] 4.2 Write integration tests: filter combinations
- [ ] 4.3 E2E test: full search user journey
```

### Why This Is Good

1. **TDD integrated**: RED → GREEN → REFACTOR cycle per task
2. **Test-first**: Each implementation task starts with RED
3. **Follows TDD rule**: "If the project uses TDD, integrate test-first tasks"
4. **Specific tests**: Not "write tests" but specific failing test scenarios
