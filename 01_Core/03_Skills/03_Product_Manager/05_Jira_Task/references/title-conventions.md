# Title Conventions

## Format

```
[TYPE] Brief description (components)
```

## Types

| Type | Use For |
|------|---------|
| `[BUG]` | Something broken that worked before |
| `[FEATURE]` | New functionality |
| `[ENHANCEMENT]` | Improvement to existing feature |
| `[REFACTOR]` | Code restructure without behavior change |
| `[DOCS]` | Documentation only |
| `[CHORE]` | Maintenance, dependencies, CI/CD |

## Components

| Component | Use For |
|-----------|---------|
| `(API)` | Backend only |
| `(UI)` | Frontend only |
| `(SDK)` | Prowler SDK only |
| `(API + UI)` | Both |
| `(Full Stack)` | All |

## Examples

- `[BUG] AWS GovCloud cannot connect - STS region hardcoded (API + UI)`
- `[FEATURE] Add dark mode toggle (UI)`
- `[REFACTOR] Migrate E2E tests to POM (UI)`
- `[ENHANCEMENT] Improve scan performance (SDK)`

## Priority

| Priority | Criteria |
|----------|----------|
| **Critical** | Production down, data loss, security |
| **High** | Blocks users, no workaround |
| **Medium** | Has workaround, subset of users |
| **Low** | Nice to have, cosmetic |
