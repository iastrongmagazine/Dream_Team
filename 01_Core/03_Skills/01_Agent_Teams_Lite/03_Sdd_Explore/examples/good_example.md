# Good Example: sdd-explore

## Scenario: Exploring JWT authentication implementation

### Orchestrator Prompt
```
Explore implementing JWT authentication for this Express.js API.
Change name: add-jwt-auth
Mode: openspec
```

### Agent Execution

```markdown
## Exploration: JWT Authentication

### Current State
The API currently uses session-based authentication stored in memory. 
- `src/middleware/auth.ts` - middleware that checks session
- `src/routes/login.ts` - creates session on login
- `src/routes/logout.ts` - destroys session
- No token-based auth exists

### Affected Areas
- `src/middleware/auth.ts` — will need new JWT validation logic
- `src/routes/login.ts` — will return JWT instead of setting session
- `src/routes/logout.ts` — will handle token blacklisting
- `src/utils/jwt.ts` — NEW: JWT creation/validation utilities

### Approaches

1. **Stateless JWT with HTTP-Only Cookie** — Store JWT in HTTP-only cookie
   - Pros: Secure against XSS, stateless, scales well
   - Cons: CSRF vulnerability, can't easily revoke tokens
   - Effort: Medium

2. **Stateless JWT in LocalStorage** — Client stores JWT
   - Pros: Simple to implement, supports mobile apps
   - Cons: Vulnerable to XSS attacks
   - Effort: Low

3. **Refresh Token Rotation** — Short-lived access + long-lived refresh tokens
   - Pros: Best security, supports token revocation
   - Cons: Most complex, more infrastructure
   - Effort: High

### Recommendation
**Approach 1: Stateless JWT with HTTP-Only Cookie**

Use refresh token rotation for production-ready security:
- Access token: 15 minutes, stored in HTTP-only cookie
- Refresh token: 7 days, stored in HTTP-only cookie with rotation

This balances security with implementation effort.

### Risks
- CSRF protection needed (same-site cookie mitigates)
- Token revocation requires blacklist/denylist
- Logout must rotate refresh token

### Ready for Proposal
Yes. Clear scope: JWT middleware, login/logout updates, new utility file.

---

## Additional Notes
- Found existing test patterns in `tests/` using Jest
- Project uses TypeScript with strict mode
- No existing JWT library - will need to add `jsonwebtoken` package
```

### Why This Is Good

1. **Investigated actual code**: Read real files, not guessed
2. **Clear current state**: What exists vs what's needed
3. **Multiple approaches with tradeoffs**: Table format is clear
4. **Concrete recommendation**: Not indecisive
5. **Risks identified**: Real security concerns
6. **Follows return format**: Exact structure required
7. **Saved to file**: Correctly created `.atl/openspec/changes/add-jwt-auth/exploration.md`

---

## Scenario: Standalone exploration without change name

### Orchestrator Prompt
```
Explore implementing real-time notifications for this React app.
(No change name provided - this is a standalone exploration)
Mode: engram
```

### Agent Execution

```markdown
## Exploration: Real-Time Notifications

### Current State
- React 18 SPA with REST API backend
- No WebSocket infrastructure exists
- Notifications currently polling every 30 seconds
- Backend: Node.js + Express

### Affected Areas
- Frontend: Need WebSocket client integration
- Backend: Need WebSocket server (Socket.io or ws)
- Database: May need notification storage for offline users

### Approaches

1. **Socket.io** — Full-featured WebSocket abstraction
   - Pros: Fallbacks, rooms, auto-reconnect, battle-tested
   - Cons: Larger bundle size (~40KB)
   - Effort: Low

2. **Native WebSockets** — Browser WebSocket API
   - Pros: No extra dependency, smaller
   - Cons: Must handle reconnection, fallbacks manually
   - Effort: Medium

3. **Server-Sent Events (SSE)** — One-way server→client
   - Pros: Simple, works over HTTP/2, automatic reconnect
   - Cons: One-directional only, no client→server messages
   - Effort: Low

### Recommendation
**Socket.io** for rapid implementation, especially if bidirectional communication may be needed later.

### Risks
- WebSocket connections consume server resources
- Need load balancer configuration for sticky sessions
- Mobile app compatibility considerations

### Ready for Proposal
Yes - scope is clear. Recommend starting with Socket.io.

---

**Note**: This exploration was saved to Engram (topic: sdd/explore/realtime-notifications) per mode: engram.
```

### Why This Is Good

1. **No file created**: Correct - standalone exploration doesn't create files
2. **Saved to Engram**: Correct per engram mode
3. **Investigated actual state**: Real understanding of current architecture
4. **Practical recommendation**: Socket.io is sensible choice
