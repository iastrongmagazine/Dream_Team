---
type: discovery
area: pm
date: 2026-03-21
status: active
tags: [skills-mapping, profiles, project-manager, ux-ui, testing]
---

## Skills Mapping: Profiles 04-06

### Context
Complete mapping of skills from profiles 04_Project_Manager, 05_UX_UI, and 06_Testing_QA in `.agent/02_Skills/Profiles/`

### Summary

| Profile | Skills | Location |
|---------|--------|----------|
| **04_Project_Manager** | 12 | `.agent/02_Skills/Profiles/04_Project_Manager/` |
| **05_UX_UI** | 4 | `.agent/02_Skills/Profiles/05_UX_UI/` |
| **06_Testing_QA** | 15 | `.agent/02_Skills/Profiles/06_Testing_QA/` |
| **TOTAL** | **31** | |

---

## 04_PROJECT_MANAGER (12 Skills)

| # | Skill | Description | Triggers |
|---|-------|--------------|----------|
| 1 | branch-pr | PR creation workflow, issue-first enforcement | "creating a pull request" |
| 2 | commit-hygiene | Conventional commits, branch naming standards | "commit creation" |
| 3 | docs-alignment | Documentation alignment for Engram | "changing APIs" |
| 4 | executing-plans | Execute action plans with traceability | "ejecuta plan" |
| 5 | github-pr | PR creation with conventional commits | "creating PRs" |
| 6 | issue-creation | Issue workflow for Agent Teams Lite | "creating GitHub issue" |
| 7 | jira-epic | Create Jira epics (Prowler format) | "create an epic" |
| 8 | jira-task | Create Jira tasks (Prowler format) | "create a Jira task" |
| 9 | planificacion-tareas-ai | ShipKit framework for task planning | "planea esto" |
| 10 | project-structure | File location rules for Engram | "creating files" |
| 11 | verify-and-commit | Automated verification + commit | "después de validación" |
| 12 | writing-plans | Create implementation plans | "escribe el plan" |

---

## 05_UX_UI (4 Skills)

| # | Skill | Description | Triggers |
|---|-------|--------------|----------|
| 1 | redesign-skill | Upgrade existing projects to premium | "rediseñar proyecto" |
| 2 | soft-skill | High-end visual design (Awwwards-tier) | "diseño premium" |
| 3 | tui-quality | Bubbletea/Lipgloss quality rules | "TUI changes" |
| 4 | ui-elements | UI elements creation for Engram dashboard | "dashboard UI" |

---

## 06_TESTING_QA (15 Skills)

| # | Skill | Description | Triggers |
|---|-------|--------------|----------|
| 1 | e2e-testing | Playwright E2E testing | "e2e testing" |
| 2 | edge-case | Edge case identification and testing | "edge cases" |
| 3 | elite-agent-auditor | Industrial-level agent auditing | "audita esta skill" |
| 4 | go-testing | Go testing patterns | "Go tests" |
| 5 | integration-testing | Multi-component testing | "integration testing" |
| 6 | observability | Metrics, Logs, Traces for AI agents | "monitoring" |
| 7 | pr-review-deep | Deep technical PR review | "risky refactor" |
| 8 | pr-review | GitHub PR/Issue review | "pr review" |
| 9 | rtm | Requirements Traceability Matrix | "RTM" |
| 10 | systematic-debugging | 4-phase root cause methodology | "debugging" |
| 11 | technical-review | Technical exercise review | "technical exercises" |
| 12 | test-coverage | Coverage analysis and improvement | "test coverage" |
| 13 | test-driven-development | Red-Green-Refactor TDD | "TDD" |
| 14 | test-resource-management | Test resource management | "recursos de test" |
| 15 | verification-before-completion | Pre-completion QC | "verification" |

---

## Dependency Map

```
writing-plans ──→ executing-plans ──→ verify-and-commit ──→ verification-before-completion
      │
      └──→ planificacion-tareas-ai ──→ jira-task ←── jira-epic

commit-hygiene ──→ branch-pr ──→ github-pr
                     ↑
issue-creation ─────┘

systematic-debugging ──→ test-driven-development
        │
        └──→ verification-before-completion

pr-review ──→ pr-review-deep
```

### Notes
- Profile 04_Project_Manager is most dependent (planning → execution → verification chain)
- Profile 05_UX_UI is independent - no cross-dependencies
- Profile 06_Testing_QA has skills that support each other
- 7 skills have Spanish triggers

### Location
`.agent/02_Skills/Profiles/`