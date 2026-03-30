# Bad Example: sdd-init

## Scenario: Guessing the tech stack instead of detecting

### Orchestrator Prompt
```
Initialize SDD for this project.
```

### Agent Execution (INCORRECT)

```markdown
## SDD Initialized

**Project**: some-project
**Stack**: React, Node.js, MongoDB (assumed)
**Persistence**: engram

The project uses React frontend and Node backend with MongoDB database.
```

### Why This Is Bad

1. **Guessed instead of detected**: No actual file reading happened
2. **Missing specific versions**: "React" isn't enough - which version?
3. **No detection evidence**: Didn't show what files were read
4. **Config not created**: If openspec mode, should create config.yaml
5. **Return format incomplete**: Missing required envelope fields

---

## Scenario: Creating unnecessary placeholder files

### Orchestrator Prompt
```
Initialize SDD for my Python FastAPI project.
```

### Agent Execution (INCORRECT)

```markdown
## SDD Initialized

**Project**: fastapi-app
**Stack**: Python, FastAPI
**Persistence**: openspec

### Structure Created
- openspec/config.yaml
- openspec/specs/
- openspec/specs/placeholder.md ← BAD: Don't create this!
- openspec/specs/api/placeholder.md ← BAD!
- openspec/changes/
- openspec/changes/archive/

### Context
This is a FastAPI project.
```

### Why This Is Bad

1. **Created placeholder spec files**: The skill explicitly says "NEVER create placeholder spec files - specs are created via sdd-spec during a change"
2. **Config too verbose**: Should be under 10 lines of context
3. **Missing detected details**: What Python version? What database? What testing framework?
4. **No evidence of reading actual files**: Should check pyproject.toml, requirements.txt, etc.

---

## Scenario: Ignoring existing openspec directory

### Orchestrator Prompt
```
Initialize SDD for this project that already has openspec/.
```

### Agent Execution (INCORRECT)

```markdown
## SDD Initialized

**Project**: existing-project
**Stack**: Angular, NestJS, PostgreSQL
**Persistence**: openspec

Created fresh openspec/ directory structure.
```

### Why This Is Bad

1. **Ignored existing structure**: Should check if openspec/ already exists
2. **Overwrote potentially valuable data**: The rule says "If the project already has an `openspec/` directory, report what exists and ask the orchestrator if it should be updated"
3. **No warning to orchestrator**: Should ask before overwriting
4. **Not reading current config**: Should read existing config.yaml to understand current state
