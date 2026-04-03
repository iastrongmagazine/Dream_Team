# OpenSpec File Convention (shared across all SDD skills)

## Directory Structure

```
.atl/openspec/
├── config.yaml              <- Project-specific SDD config
├── specs/                   <- Source of truth (main specs)
│   └── {domain}/
│       └── spec.md
└── changes/                 <- Active changes
    ├── archive/             <- Completed changes (YYYY-MM-DD-{change-name}/)
    └── {change-name}/       <- Active change folder
        ├── state.yaml       <- DAG state (orchestrator, survives compaction)
        ├── exploration.md   <- (optional) from sdd-explore
        ├── proposal.md      <- from sdd-propose
        ├── specs/           <- from sdd-spec
        │   └── {domain}/
        │       └── spec.md  <- Delta spec
        ├── design.md        <- from sdd-design
        ├── tasks.md         <- from sdd-tasks (updated by sdd-apply)
        └── verify-report.md <- from sdd-verify
```

## Artifact File Paths

| Skill        | Creates / Reads    | Path                                                                                        |
|--------------|--------------------|---------------------------------------------------------------------------------------------|
| orchestrator | Creates/Updates    | `.atl/openspec/changes/{change-name}/state.yaml` (DAG state for compaction recovery)             |
| sdd-init     | Creates            | `.atl/openspec/config.yaml`, `.atl/openspec/specs/`, `.atl/openspec/changes/`, `.atl/openspec/changes/archive/` |
| sdd-explore  | Creates (optional) | `.atl/openspec/changes/{change-name}/exploration.md`                                             |
| sdd-propose  | Creates            | `.atl/openspec/changes/{change-name}/proposal.md`                                                |
| sdd-spec     | Creates            | `.atl/openspec/changes/{change-name}/specs/{domain}/spec.md`                                     |
| sdd-design   | Creates            | `.atl/openspec/changes/{change-name}/design.md`                                                  |
| sdd-tasks    | Creates            | `.atl/openspec/changes/{change-name}/tasks.md`                                                   |
| sdd-apply    | Updates            | `.atl/openspec/changes/{change-name}/tasks.md` (marks `[x]`)                                     |
| sdd-verify   | Creates            | `.atl/openspec/changes/{change-name}/verify-report.md`                                           |
| sdd-archive  | Moves              | `.atl/openspec/changes/{change-name}/` → `.atl/openspec/changes/archive/YYYY-MM-DD-{change-name}/`    |
| sdd-archive  | Updates            | `.atl/openspec/specs/{domain}/spec.md` (merges deltas into main specs)                           |

## Reading Artifacts

Each skill reads its dependencies from the filesystem:

```
Proposal:  .atl/openspec/changes/{change-name}/proposal.md
Specs:     .atl/openspec/changes/{change-name}/specs/  (all domain subdirectories)
Design:    .atl/openspec/changes/{change-name}/design.md
Tasks:     .atl/openspec/changes/{change-name}/tasks.md
Verify:    .atl/openspec/changes/{change-name}/verify-report.md
Config:    .atl/openspec/config.yaml
Main specs: .atl/openspec/specs/{domain}/spec.md
```

## Writing Rules

- ALWAYS create the change directory (`.atl/openspec/changes/{change-name}/`) before writing artifacts
- If a file already exists, READ it first and UPDATE it (don't overwrite blindly)
- If the change directory already exists with artifacts, the change is being CONTINUED
- Use the `.atl/openspec/config.yaml` `rules` section to apply project-specific constraints per phase

## Config File Reference

```yaml
# .atl/openspec/config.yaml
schema: spec-driven

context: |
  Tech stack: {detected}
  Architecture: {detected}
  Testing: {detected}
  Style: {detected}

rules:
  proposal:
    - Include rollback plan for risky changes
  specs:
    - Use Given/When/Then for scenarios
    - Use RFC 2119 keywords (MUST, SHALL, SHOULD, MAY)
  design:
    - Include sequence diagrams for complex flows
    - Document architecture decisions with rationale
  tasks:
    - Group by phase, use hierarchical numbering
    - Keep tasks completable in one session
  apply:
    - Follow existing code patterns
    tdd: false           # Set to true to enable RED-GREEN-REFACTOR
    test_command: ""     # e.g., "npm test", "pytest"
  verify:
    test_command: ""     # Override for verification
    build_command: ""    # Override for build check
    coverage_threshold: 0  # Set > 0 to enable coverage check
  archive:
    - Warn before merging destructive deltas
```

## Archive Structure

When archiving, the change folder moves to:
```
.atl/openspec/changes/archive/YYYY-MM-DD-{change-name}/
```

Use today's date in ISO format. The archive is an AUDIT TRAIL — never delete or modify archived changes.
