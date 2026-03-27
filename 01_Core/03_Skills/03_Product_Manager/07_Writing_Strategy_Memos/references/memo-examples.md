# Strategy Memo Examples

## Example 1: AI-Powered Documentation

### Problem
Customers spend 4+ hours writing documentation that becomes outdated in weeks. As one PM said: "Our docs are stale the moment we hit publish."

### Vision
Make documentation write itself from code, keeping always in sync.

### Principles
- **Automation over manual**: Never ask a human to copy-paste
- **Fresh over complete**: Something current beats everything stale
- **Developer experience over features**: If it's not effortless, it won't happen

### Goals
- **Output**: 90% reduction in documentation time
- **Inputs**:
  - Auto-generate API docs from code
  - Sync changelogs from commits
  - Update guides on merge

### Solution
1. Build doc generator from OpenAPI spec
2. Create commit-to-changelog pipeline
3. Add doc sync to CI/CD

### Non-Priorities
- Marketing content (separate team)
- Video tutorials (Q3)
- Multi-language (Phase 2)

---

## Example 2: Faster Onboarding

### Problem
New hires take 3 weeks to first meaningful commit. "I spent my first week just setting up my environment." — New engineer

### Vision
Any developer ships code on day one.

### Principles
- **Local over cloud**: Dev environment is sacred
- **Defaults over options**: One way to do it
- **Guide over document**: Interactive > static

### Goals
- **Output**: First commit within 4 hours
- **Inputs**:
  - One-command setup
  - Guided first task
  - Auto-configured IDE

### Solution
1. Create `make setup` with all deps
2. Build interactive tutorial in VS Code
3. Pre-configure devcontainer

### Non-Priorities
- Windows native support (use WSL)
- Custom IDE support (VS Code only)
- Legacy project setup (deprecated)
