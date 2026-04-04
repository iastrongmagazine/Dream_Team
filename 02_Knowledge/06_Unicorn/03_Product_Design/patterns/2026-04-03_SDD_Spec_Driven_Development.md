---
type: pattern
area: product_design
date: 2026-04-03
status: active
tags: [sdd, spec-driven-development, methodology, architecture]
---

## SDD - Spec-Driven Development

### What It Solves
Structured approach to software development where specifications lead the entire process. Prevents "feature creep" and ensures clear requirements before coding.

### When to Use
- Complex features requiring clear scope
- Team collaboration needing shared understanding
- Projects with multiple stakeholders
- When precision matters more than speed

### SDD Phases (Complete Flow)

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   EXPLORE   │ ──► │  PROPOSE   │ ──► │    SPEC    │ ──► │   DESIGN   │
│  (investigate)│  (define intent)│ (requirements)│ (technical) │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
                                                                    │
┌─────────────┐     ┌─────────────┐     ┌─────────────┐              │
│   VERIFY   │ ◄── │   APPLY    │ ◄── │   TASKS   │ ◄────────────┘
│ (validate)  │     (implement)│     (breakdown)│
└─────────────┘     └─────────────┘     └─────────────┘
         │
         ▼
┌─────────────┐
│   ARCHIVE  │
│ (complete) │
└─────────────┘
```

---

### Phase 1: EXPLORE

**Purpose**: Investigate and understand the problem/feature

**Activities**:
- Research existing solutions
- Analyze codebase patterns
- Identify dependencies
- Gather requirements informally

**Artifacts**: 
- Exploration notes
- Code references
- Initial questions

**Output**: Clear understanding of what needs to be built and why

---

### Phase 2: PROPOSE

**Purpose**: Define intent and scope

**Activities**:
- Define feature intent (what and why)
- Set scope boundaries
- Identify success criteria
- Determine approach

**Artifacts**:
- Title and description
- Intent statement
- Scope definition
- Success metrics

**Example**:
```
## Proposal: User Authentication System

### Intent
Add secure authentication to protect user data and enable personalization.

### Scope
- Login/Logout functionality
- Password reset flow
- Session management

### Success Criteria
- Login < 200ms response time
- Support 10k concurrent users
- SOC2 compliant
```

---

### Phase 3: SPEC

**Purpose**: Write detailed requirements

**Activities**:
- Define functional requirements
- Specify edge cases
- Document user flows
- Create acceptance criteria
- Identify data models

**Artifacts**: SPEC.md with:
- Overview
- Functional requirements
- Non-functional requirements
- User flows
- Data models
- Acceptance criteria
- Edge cases

**Example Structure**:
```markdown
# SPEC: User Authentication System

## Overview
Brief description of the feature.

## Functional Requirements
### FR-001: Login
User can login with email/password...

## User Flows
1. User enters credentials
2. System validates
3. Session created
4. Redirect to dashboard

## Acceptance Criteria
- [ ] Login works with valid credentials
- [ ] Error shown for invalid credentials
- [ ] Session persists across page refresh

## Edge Cases
- User enters wrong password 3 times → lock account
- Network timeout during login → show retry option
```

---

### Phase 4: DESIGN

**Purpose**: Create technical design

**Activities**:
- Architecture decisions
- API design
- Database schema
- Component design
- Integration points

**Artifacts**:
- Technical specification
- API contracts
- Database schema
- Component diagrams

**Example**:
```markdown
## Technical Design

### Architecture
- REST API with JWT tokens
- PostgreSQL for persistence
- Redis for session cache

### API Endpoints
- POST /api/auth/login
- POST /api/auth/logout
- POST /api/auth/refresh
- POST /api/auth/reset-password

### Database Schema
users: id, email, password_hash, created_at, updated_at
sessions: id, user_id, token, expires_at
```

---

### Phase 5: TASKS

**Purpose**: Break down into implementable tasks

**Activities**:
- Decompose design into tasks
- Estimate effort
- Prioritize
- Assign dependencies

**Artifacts**:
- Task list with IDs
- Effort estimates
- Dependencies graph
- Priority labels

**Example**:
```markdown
## Tasks

### Authentication Module
- [P1] TASK-001: Create user model and migration
- [P1] TASK-002: Implement password hashing
- [P1] TASK-003: Build login endpoint
- [P2] TASK-004: Add session management
- [P2] TASK-005: Implement logout
- [P3] TASK-006: Add password reset flow
```

---

### Phase 6: APPLY

**Purpose**: Implement the tasks

**Activities**:
- Write code following specs
- Run tests
- Get reviews
- Commit changes

**Artifacts**:
- Implementation code
- Test coverage
- PR descriptions

---

### Phase 7: VERIFY

**Purpose**: Validate implementation against spec

**Activities**:
- Review against acceptance criteria
- Run integration tests
- Get stakeholder sign-off
- Document any deviations

**Artifacts**:
- Verification report
- Test results
- Sign-off confirmation

---

### Phase 8: ARCHIVE

**Purpose**: Complete and document

**Activities**:
- Update main documentation
- Archive delta specs
- Clean up temporary files
- Celebrate completion

**Artifacts**:
- Archived spec package
- Updated main SPEC.md

---

### Key Principles

1. **No code without spec** - Always spec first
2. **Spec is contract** - Don't change mid-implementation without review
3. **Verification required** - Don't claim done without proving it
4. **Artifacts persist** - Keep specs for future reference
5. **Phase gates** - Don't skip phases

### Tools Used
- OpenSpec (file-based storage)
- Engram (memory persistence)
- SDD Skills: sdd-init, sdd-explore, sdd-propose, sdd-spec, sdd-design, sdd-tasks, sdd-apply, sdd-verify, sdd-archive