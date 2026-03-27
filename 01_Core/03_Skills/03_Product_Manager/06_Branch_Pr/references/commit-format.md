# Conventional Commits Format

## Regex Pattern
```
^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(\([a-z0-9\._-]+\))?!?: .+
```

## Format
`type(scope): description` or `type: description`

## Types

| Type | Use For | PR Label |
|------|---------|----------|
| `feat` | New feature | `type:feature` |
| `fix` | Bug fix | `type:bug` |
| `docs` | Documentation | `type:docs` |
| `refactor` | Code restructure | `type:refactor` |
| `chore` | Maintenance | `type:chore` |
| `style` | Formatting | `type:chore` |
| `perf` | Performance | `type:feature` |
| `test` | Tests | `type:chore` |
| `build` | Build system | `type:chore` |
| `ci` | CI/CD | `type:chore` |
| `revert` | Undo change | `type:bug` |
| `feat!`/`fix!` | Breaking | `type:breaking-change` |

## Examples

```
feat(scripts): add Codex support to setup.sh
fix(skills): correct topic key format
docs(readme): update configuration guide
refactor(skills): extract shared logic
chore(ci): add shellcheck validation
perf(scripts): reduce execution time
style(skills): fix markdown formatting
test(scripts): add integration tests
ci(workflows): add branch validation
revert: undo broken change
feat!: redesign skill loading
```

## Rules

1. Lowercase after colon
2. No period at end
50 chars max for subject
4. Blank line between subject and body
5. Body explains WHAT and WHY, not HOW
