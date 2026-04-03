# Good Example: sdd-init

## Scenario: Initializing a Next.js TypeScript project

### Orchestrator Prompt
```
Initialize SDD for this Next.js 15 project with TypeScript.
```

### Agent Execution

```markdown
## SDD Initialized

**Project**: my-next-app
**Stack**: Next.js 15, TypeScript, Tailwind CSS, App Router
**Persistence**: engram

### Context Detected
- **Framework**: Next.js 15 with App Router (detected from package.json)
- **Language**: TypeScript strict mode (detected from tsconfig.json)
- **Styling**: Tailwind CSS 4 (detected from tailwind.config.ts)
- **Testing**: Jest + React Testing Library (detected from package.json)
- **Linting**: ESLint with Next.js plugin (detected from package.json)

### Persistence Backend
- Mode resolved to: `engram`
- Project context saved to Engram
- Topic key: `sdd-init/my-next-app`

### Next Steps
Ready for /sdd-explore <topic> or /sdd-new <change-name>.
```

### Why This Is Good

1. **Detected actual stack**: Read package.json, tsconfig.json to find real tech
2. **Concise context**: Under 10 lines, focused on relevant info
3. **Follows return format**: Uses exact envelope structure required
4. **No files created in none/engram mode**: Correct behavior
5. **Actionable next steps**: Clear path forward for orchestrator

---

## Scenario: Initializing a Go project with openspec

### Orchestrator Prompt
```
Initialize SDD for this Go API project using openspec mode.
```

### Agent Execution

```markdown
## SDD Initialized

**Project**: orders-api
**Stack**: Go 1.21, Chi router, PostgreSQL, sqlc
**Persistence**: openspec

### Structure Created
- .atl/openspec/config.yaml ← Project config with detected context
- .atl/openspec/specs/      ← Ready for specifications
- .atl/openspec/changes/    ← Ready for change proposals
- .atl/openspec/changes/archive/ ← Archive directory

### Config Generated
```yaml
schema: spec-driven

context: |
  Tech stack: Go 1.21, Chi router, PostgreSQL, sqlc
  Architecture: Clean Architecture with handlers/services/repository layers
  Testing: Go testing (built-in), testify for assertions
  Style: golangci-lint, gofmt

rules:
  proposal:
    - Include rollback plan for risky changes
    - Identify affected modules/packages
  specs:
    - Use Given/When/Then format for scenarios
    - Use RFC 2119 keywords (MUST, SHALL, SHOULD, MAY)
  design:
    - Include sequence diagrams for complex flows
    - Document architecture decisions with rationale
  tasks:
    - Group tasks by phase (infrastructure, implementation, testing)
    - Keep tasks small enough to complete in one session
  apply:
    - Follow Go conventions (package naming, error handling)
    - Load relevant skills: go-testing
  verify:
    - Run go test ./...
    - Run go build ./...
```

### Next Steps
Ready for /sdd-explore <topic> or /sdd-new <change-name>.
```

### Why This Is Good

1. **Created correct directory structure**: All required folders present
2. **Config is project-specific**: Based on actual detected stack
3. **Rules applied**: Custom rules for Go project included
4. **Follows format exactly**: Matches required return envelope
