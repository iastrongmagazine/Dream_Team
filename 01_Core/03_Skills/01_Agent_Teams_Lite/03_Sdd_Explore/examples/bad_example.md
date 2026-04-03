# Bad Example: sdd-explore

## Scenario: Guessing without reading code

### Orchestrator Prompt
```
Explore adding dark mode to this React app.
```

### Agent Execution (INCORRECT)

```markdown
## Exploration: Dark Mode

### Current State
React app (probably using styled-components or Tailwind)

### Affected Areas
- Theme files
- CSS files
- Components

### Approaches

1. **CSS Variables** — Use CSS custom properties
2. **Theme Provider** — React Context for theming
3. **Tailwind Dark Mode** — Use Tailwind's dark: prefix

### Recommendation
Use CSS Variables - it's the simplest.

### Risks
- Might not work with all approaches
```

### Why This Is Bad

1. **No actual code reading**: Should check package.json, look at existing theme files, check if Tailwind is used
2. **Vague "probably"**: Not confident, didn't investigate
3. **No file paths**: Should reference actual files like `src/theme/colors.ts` or `tailwind.config.js`
4. **No effort estimation**: Should indicate complexity
5. **Missing return format**: Didn't follow exact structure
6. **No exploration file created when it should have been**: With change name provided, should create `exploration.md`

---

## Scenario: Creating unauthorized files

### Orchestrator Prompt
```
Explore adding file upload feature to this Django project.
Change: add-file-upload
Mode: none
```

### Agent Execution (INCORRECT)

```markdown
## Exploration: File Upload

Created the following files:
- .atl/openspec/changes/add-file-upload/exploration.md
- .atl/openspec/changes/add-file-upload/proposal.md
- .atl/openspec/changes/add-file-upload/spec.md

[Full exploration content...]
```

### Why This Is Bad

1. **Mode is `none`**: Should NOT create any files
2. **Created unauthorized files**: Only exploration.md is allowed with change name
3. **Created proposal and spec**: Those are for sdd-propose and sdd-spec phases
4. **Violated mode contract**: `none` mode means "return result only"

---

## Scenario: Over-complicating a simple exploration

### Orchestrator Prompt
```
Explore adding a contact form to this static HTML site.
```

### Agent Execution (INCORRECT)

```markdown
## Exploration: Contact Form

### Current State
Static HTML site with no backend.

After extensive analysis of 47 files and 12 directories...

### Architecture Considerations
- Monolithic vs Microservices
- GraphQL vs REST
- Kubernetes vs Serverless
- Database: PostgreSQL vs MySQL vs MongoDB vs DynamoDB vs Cassandra

### 15 Alternative Approaches
[Lists 15 different ways to implement a contact form]

### Recommendation
Given the complexity, I recommend a three-month investigation before proceeding.

### Next Steps
- Phase 1: Research (3 months)
- Phase 2: More Research (6 months)
- Phase 3: Final Research (1 year)
```

### Why This Is Bad

1. **Over-engineering a simple feature**: Contact form doesn't need microservices
2. **Didn't read actual files**: Should see it's just static HTML
3. **Analysis paralysis**: Should give practical recommendation
4. **Too verbose**: Orchestrator needs summary, not novel
5. **Missing scope**: This is a tiny feature, not enterprise architecture

---

## Scenario: Not identifying what clarification is needed

### Orchestrator Prompt
```
Explore improving performance.
```

### Agent Execution (INCORRECT)

```markdown
## Exploration: Performance Improvement

### Current State
The app exists.

### Recommendation
Improve performance.
```

### Why This Is Bad

1. **Request too vague**: "improve performance" isn't actionable
2. **Didn't ask for clarification**: Should say what specifically needs performance help
3. **No investigation possible**: Nothing concrete to explore
4. **Violated rule**: "If the request is too vague to explore, say what clarification is needed"
