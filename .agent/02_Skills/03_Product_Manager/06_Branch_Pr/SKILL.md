---
name: branch-pr
description: >
  PR creation workflow following issue-first enforcement system with conventional commits.
  Triggers on: create PR, pull request, open PR, prepare branch, merge changes.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "2.0"
---

## Esencia Original
> **Propósito:** Crear PRs bien estructurados con issue-link obligatorio, conventional commits y automated checks.
> **Flujo:** Issue approved → Branch feat/desc → Commits → PR con template → Label type → Merge

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: PR sin issue link
  - **Por qué**: GitHub Actions bloquea el PR
  - **Solución**: SIEMPRE incluir "Closes #N" en el body

- **[ERROR]**: Branch con nombre incorrecto
  - **Por qué**: Regex validation falla
  - **Solución**: `type/description` — feat/, fix/, chore/, etc.

- **[ERROR]**: Sin label type:*
  - **Por qué**: Automated check falla
  - **Solución**: Agregar EXACTAMENTE UN label (type:feature, type:bug, etc.)

- **[ERROR]**: Commits sin formato conventional
  - **Por qué**: Difícil de leer el changelog
  - **Solución**: `feat(scope): description` o `fix: description`

- **[ERROR]**: Incluir Co-Authored-By
  - **Por qué**: Violación de las reglas del repo
  - **Solución**: Solo conventional commits, sin AI attribution

## 📁 Progressive Disclosure

> Para información detallada:
- [references/branch-naming.md](references/branch-naming.md) — Convenciones de branch naming
- [references/commit-format.md](references/commit-format.md) — Formato de commits

## 🛠️ Scripts

- [scripts/create-pr.py](scripts/create-pr.py) — Helper para crear PRs

## 💾 State Persistence

Tracking de PRs en:
- GitHub (remote)
- `02_Operations/03_Progress/` — Estado de features en curso

## When to Use

Use this skill when:
- Creating a pull request for any change
- Preparing a branch for submission
- Helping a contributor open a PR

---

## Critical Rules

1. **Every PR MUST link an approved issue** — no exceptions
2. **Every PR MUST have exactly one `type:*` label**
3. **Automated checks must pass** before merge is possible
4. **Blank PRs without issue linkage will be blocked** by GitHub Actions

---

## Workflow

```
1. Verify issue has `status:approved` label
2. Create branch: type/description (see Branch Naming below)
3. Implement changes with conventional commits
4. Run shellcheck on modified scripts
5. Open PR using the template
6. Add exactly one type:* label
7. Wait for automated checks to pass
```

---

## Branch Naming

Branch names MUST match this regex:

```
^(feat|fix|chore|docs|style|refactor|perf|test|build|ci|revert)\/[a-z0-9._-]+$
```

**Format:** `type/description` — lowercase, no spaces, only `a-z0-9._-` in description.

| Type | Branch pattern | Example |
|------|---------------|---------|
| Feature | `feat/<description>` | `feat/user-login` |
| Bug fix | `fix/<description>` | `fix/zsh-glob-error` |
| Chore | `chore/<description>` | `chore/update-ci-actions` |
| Docs | `docs/<description>` | `docs/installation-guide` |
| Style | `style/<description>` | `style/format-scripts` |
| Refactor | `refactor/<description>` | `refactor/extract-shared-logic` |
| Performance | `perf/<description>` | `perf/reduce-startup-time` |
| Test | `test/<description>` | `test/add-setup-coverage` |
| Build | `build/<description>` | `build/update-shellcheck` |
| CI | `ci/<description>` | `ci/add-branch-validation` |
| Revert | `revert/<description>` | `revert/broken-setup-change` |

---

## PR Body Format

The PR template is at `.github/PULL_REQUEST_TEMPLATE.md`. Every PR body MUST contain:

### 1. Linked Issue (REQUIRED)

```markdown
Closes #<issue-number>
```

Valid keywords: `Closes #N`, `Fixes #N`, `Resolves #N` (case insensitive).
The linked issue MUST have the `status:approved` label.

### 2. PR Type (REQUIRED)

Check exactly ONE in the template and add the matching label:

| Checkbox | Label to add |
|----------|-------------|
| Bug fix | `type:bug` |
| New feature | `type:feature` |
| Documentation only | `type:docs` |
| Code refactoring | `type:refactor` |
| Maintenance/tooling | `type:chore` |
| Breaking change | `type:breaking-change` |

### 3. Summary

1-3 bullet points of what the PR does.

### 4. Changes Table

```markdown
| File | Change |
|------|--------|
| `path/to/file` | What changed |
```

### 5. Test Plan

```markdown
- [x] Scripts run without errors: `shellcheck scripts/*.sh`
- [x] Manually tested the affected functionality
- [x] Skills load correctly in target agent
```

### 6. Contributor Checklist

All boxes must be checked:
- Linked an approved issue
- Added exactly one `type:*` label
- Ran shellcheck on modified scripts
- Skills tested in at least one agent
- Docs updated if behavior changed
- Conventional commit format
- No `Co-Authored-By` trailers

---

## Automated Checks (all must pass)

| Check | Job name | What it verifies |
|-------|----------|-----------------|
| PR Validation | `Check Issue Reference` | Body contains `Closes/Fixes/Resolves #N` |
| PR Validation | `Check Issue Has status:approved` | Linked issue has `status:approved` |
| PR Validation | `Check PR Has type:* Label` | PR has exactly one `type:*` label |
| CI | `Shellcheck` | Shell scripts pass `shellcheck` |

---

## Conventional Commits

Commit messages MUST match this regex:

```
^(build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test)(\([a-z0-9\._-]+\))?!?: .+
```

**Format:** `type(scope): description` or `type: description`

- `type` — required, one of: `build`, `chore`, `ci`, `docs`, `feat`, `fix`, `perf`, `refactor`, `revert`, `style`, `test`
- `(scope)` — optional, lowercase with `a-z0-9._-`
- `!` — optional, indicates breaking change
- `description` — required, starts after `: `

Type-to-label mapping:

| Commit type | PR label |
|-------------|----------|
| `feat` | `type:feature` |
| `fix` | `type:bug` |
| `docs` | `type:docs` |
| `refactor` | `type:refactor` |
| `chore` | `type:chore` |
| `style` | `type:chore` |
| `perf` | `type:feature` |
| `test` | `type:chore` |
| `build` | `type:chore` |
| `ci` | `type:chore` |
| `revert` | `type:bug` |
| `feat!` / `fix!` | `type:breaking-change` |

Examples:
```
feat(scripts): add Codex support to setup.sh
fix(skills): correct topic key format in sdd-apply
docs(readme): update multi-model configuration guide
refactor(skills): extract shared persistence logic
chore(ci): add shellcheck to PR validation workflow
perf(scripts): reduce setup.sh execution time
style(skills): fix markdown formatting
test(scripts): add setup.sh integration tests
ci(workflows): add branch name validation
revert: undo broken setup change
feat!: redesign skill loading system
```

---

## Commands

```bash
# Create branch
git checkout -b feat/my-feature main

# Run shellcheck before pushing
shellcheck scripts/*.sh

# Push and create PR
git push -u origin feat/my-feature
gh pr create --title "feat(scope): description" --body "Closes #N"

# Add type label to PR
gh pr edit <pr-number> --add-label "type:feature"
```
