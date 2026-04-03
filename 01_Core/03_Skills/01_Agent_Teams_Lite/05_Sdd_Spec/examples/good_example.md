# Good Example: sdd-spec

## Scenario: Writing delta spec for JWT auth change

### Orchestrator Prompt
```
Write specs for add-jwt-auth change.
Mode: openspec
```

### Agent Execution

First, read the existing proposal to understand affected areas:
- `src/middleware/auth.ts`
- `src/routes/login.ts`
- `src/routes/logout.ts`
- `src/utils/jwt.ts` (new)
- `src/types/auth.ts`

### Agent Creates

```
.atl/openspec/changes/add-jwt-auth/specs/
└── authentication/
    └── spec.md
```

### spec.md Content

```markdown
# Delta for Authentication

## ADDED Requirements

### Requirement: JWT Token Validation

The authentication middleware MUST validate JWT access tokens on every protected request.

The system SHALL extract tokens from HTTP-only cookies and verify signature, expiration, and claims.

#### Scenario: Valid access token

- GIVEN a valid access token in the request cookie
- WHEN the request is made to a protected endpoint
- THEN the request proceeds with the user context attached
- AND the token payload is available to the handler

#### Scenario: Expired access token

- GIVEN an expired access token in the request cookie
- WHEN the request is made to a protected endpoint
- THEN the system SHALL attempt to refresh using the refresh token
- AND if refresh succeeds, proceed with new access token
- AND if refresh fails, return 401 Unauthorized

#### Scenario: Missing access token

- GIVEN no access token in the request
- WHEN the request is made to a protected endpoint
- THEN return 401 Unauthorized
- AND include WWW-Authenticate header

### Requirement: Token Refresh

The system MUST provide a mechanism to exchange expired access tokens for new ones using refresh tokens.

The refresh endpoint SHALL validate the refresh token and issue new access + refresh tokens.

#### Scenario: Successful refresh

- GIVEN a valid, non-expired refresh token
- WHEN the client requests token refresh
- THEN return new access token (15 min) and new refresh token
- AND the old refresh token SHALL be invalidated (rotation)

#### Scenario: Invalid refresh token

- GIVEN an invalid or revoked refresh token
- WHEN the client requests token refresh
- THEN return 401 Unauthorized
- AND do not issue new tokens

### Requirement: Secure Logout

The system MUST invalidate tokens on logout to prevent use after user intends to leave.

#### Scenario: User initiates logout

- GIVEN an authenticated user with valid tokens
- WHEN the user calls the logout endpoint
- THEN invalidate the refresh token (add to denylist)
- AND clear the cookie from client
- AND return 200 OK

## MODIFIED Requirements

### Requirement: User Authentication (Modified)

**Previously**: The login endpoint creates a session and returns session ID in cookie.

**New Requirement**: The login endpoint MUST validate credentials and return JWT tokens in HTTP-only secure cookies.

The system SHALL issue access token (15 min) and refresh token (7 days) upon successful authentication.

#### Scenario: Successful login

- GIVEN valid username and password
- WHEN the user calls POST /login with credentials
- THEN validate credentials against database
- AND return 200 OK with access token and refresh token in HTTP-only cookies
- AND set SameSite=strict, Secure, HttpOnly flags

#### Scenario: Invalid credentials

- GIVEN invalid username or password
- WHEN the user calls POST /login
- THEN return 401 Unauthorized
- AND do not issue any tokens
```

### Return Summary

```markdown
## Specs Created

**Change**: add-jwt-auth

### Specs Written
| Domain         | Type   | Requirements        | Scenarios   |
|----------------|--------|---------------------|-------------|
| authentication | Delta  | 3 added, 1 modified | 7 total     |

### Coverage
- Happy paths: ✅ Covered (valid token, successful login, successful refresh)
- Edge cases: ✅ Covered (expired token, missing token, invalid credentials, invalid refresh)
- Error states: ✅ Covered (401 responses with proper headers)

### Next Step
Ready for design (sdd-design). If design already exists, ready for tasks (sdd-tasks).
```

### Why This Is Good

1. **Delta format**: Correctly uses ADDED/MODIFIED sections
2. **RFC 2119 keywords**: MUST, SHALL used correctly
3. **Given/When/Then**: Every requirement has scenarios
4. **Testable scenarios**: Someone could write tests from these
5. **Happy + edge cases**: Both covered
6. **No implementation details**: Describes WHAT, not HOW
7. **Created correct file structure**: `specs/authentication/spec.md`
8. **Follows return format exactly**

---

## Scenario: Writing full spec for new domain

### Orchestrator Prompt
```
Write specs for add-notifications change - this is a brand new domain.
Mode: openspec
```

### Agent Execution

No existing spec at `.atl/openspec/specs/notifications/spec.md`, so creates full spec:

```markdown
# Notifications Specification

## Purpose

This specification defines the in-app notification system for real-time user alerts.

## Requirements

### Requirement: Notification Delivery

The system MUST deliver notifications to users in real-time via WebSocket connection.

The notification service SHOULD store notifications for users who are offline.

#### Scenario: Online user receives notification

- GIVEN a user with active WebSocket connection
- WHEN a notification is triggered for that user
- THEN deliver notification immediately via WebSocket
- AND display notification in UI

#### Scenario: Offline user has notification

- GIVEN a user without active WebSocket connection
- WHEN that user logs in
- THEN deliver missed notifications via REST API
- AND mark notifications as read when user views them
```

### Why This Is Good

1. **Full spec format**: Correctly identified no existing spec
2. **Purpose section**: Explains domain context
3. **Requirements with scenarios**: Proper structure
4. **Follows rule**: "If NO existing specs exist for the domain, write a FULL spec"
