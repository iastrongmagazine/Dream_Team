# Branch Naming Conventions

## Regex Pattern
```
^(feat|fix|chore|docs|style|refactor|perf|test|build|ci|revert)\/[a-z0-9._-]+$
```

## Format
`type/description` — lowercase, no spaces, only `a-z0-9._-`

## Branch Types

| Type | Pattern | Example |
|------|---------|---------|
| Feature | `feat/<desc>` | `feat/user-login` |
| Bug fix | `fix/<desc>` | `fix/zsh-glob-error` |
| Chore | `chore/<desc>` | `chore/update-ci` |
| Docs | `docs/<desc>` | `docs/installation` |
| Style | `style/<desc>` | `style/format` |
| Refactor | `refactor/<desc>` | `refactor/extract-logic` |
| Performance | `perf/<desc>` | `perf/reduce-time` |
| Test | `test/<desc>` | `test/add-coverage` |
| Build | `build/<desc>` | `build/update-deps` |
| CI | `ci/<desc>` | `ci/add-validation` |
| Revert | `revert/<desc>` | `revert/broken-change` |

## Examples

✅ `feat/add-dark-mode`
✅ `fix/login-error`
✅ `docs/update-readme`

❌ `Feature/Add Dark Mode` (wrong case, spaces)
❌ `feat/add dark mode` (spaces)
❌ `feature/add-dark-mode` (wrong type)
