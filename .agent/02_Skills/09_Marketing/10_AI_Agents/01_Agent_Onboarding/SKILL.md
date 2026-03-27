---
name: onboarding-agent-employee
description: Onboards AI agents as team members with role definition, context setup, and working agreements. Triggers on: new agent, add team member, hire agent, setup agent context, agent onboarding, integrate new AI, define agent role.
---

# Agent Onboarding

> **Esencia Original**: Tratar al agente como un empleado nuevo — con onboarding estructurado, responsabilidades claras y acuerdos de trabajo definidos.

Onboard a new AI agent as if it were a hired employee — define role, responsibilities, context, and working agreements.

## When to Use This Skill

- User says: "new agent", "add team member", "hire agent"
- User says: "setup agent context", "onboard agent", "integrate new AI"
- User says: "agent responsibilities", "define agent role"
- User needs to add an AI agent to the team/workflow

## Pre-Flight Checklist

- [ ] Identify the agent's primary function (what problem does it solve?)
- [ ] Gather existing context it needs (docs, codebase, processes)
- [ ] Define success metrics for this agent
- [ ] Determine communication style and frequency

## Workflow

### Phase 1: Role Definition

1. **Define the Role**: What title best fits this agent's purpose?
   - Example: "Research Analyst", "Code Reviewer", "Content Strategist"

2. **Set Responsibilities**: What are this agent's PRIMARY responsibilities?
   - Max 3-5 key areas
   - Focus on what it OWNS, not just what it can do

3. **Success Metrics**: How do we measure if this agent is doing well?
   - Quantifiable outcomes, not vague "good work"

### Phase 2: Context Setup

1. **Gather Necessary Context**:
   - Relevant documentation files
   - Codebase areas it needs to understand
   - Team processes and conventions
   - Previous decisions and patterns

2. **Organize Context**:
   - Create a dedicated folder for this agent's context
   - Use consistent naming: `agent-{role}/`
   - Include README with role overview

### Phase 3: Working Agreements

1. **Communication Protocol**:
   - How often should it report back?
   - What counts as a "blocker" that needs escalation?
   - Preferred format for updates (summary, detailed, etc.)

2. **Quality Standards**:
   - What level of perfection is expected?
   - When should it ask for clarification vs. make assumptions?
   - What are the non-negotiables?

3. **Handoff Points**:
   - When does it hand off to humans?
   - What decisions can it make autonomously?

## Gotchas (Common Mistakes)

- **Don't**: Give the agent too many responsibilities at once — start with 1-3 focus areas
- **Don't**: Skip the success metrics — you'll never know if it's working
- **Don't**: Give it access to everything — follow principle of least privilege
- **Don't**: Set it and forget it — schedule regular check-ins
- **Don't**: Assume it knows your preferences — document them explicitly
- **Don't**: Skip the "known limitations" section — you'll forget what the agent struggles with
- **Don't**: Use vague metrics like "good work" — be specific and quantifiable

## Scripts & Templates

### Template: Agent Context README

```markdown
# {Agent Role} - Context Document

## Purpose
[What problem does this agent solve?]

## Responsibilities
- [Responsibility 1]
- [Responsibility 2]
- [Responsibility 3]

## Success Metrics
- [Metric 1: measurable outcome]
- [Metric 2: measurable outcome]

## Context Provided
- [Link to relevant docs]
- [Link to codebase areas]
- [Link to processes]

## Communication
- Check-in frequency: [daily/weekly/as-needed]
- Escalation triggers: [what requires immediate attention]
- Format: [how it should report back]

## Quality Bar
- [Non-negotiable standard]
- [Non-negotiable standard]

## Known Limitations
- [What this agent struggles with]
- [When to double-check its work]
```

### Script: Create Agent Context

```bash
# Create agent context directory
AGENT_NAME="agent-name"
mkdir -p ".agent-context/$AGENT_NAME"
mkdir -p ".agent-context/$AGENT_NAME/docs"
mkdir -p ".agent-context/$AGENT_NAME/references"

# Create README from template
cat > ".agent-context/$AGENT_NAME/README.md" << 'EOF'
# {Role} - Context Document

## Purpose
[What problem does this agent solve?]

## Responsibilities
- 

## Success Metrics
- 

## Context Provided
- 

## Communication
- Check-in frequency: 
- Escalation triggers: 
- Format: 

## Quality Bar
- 

## Known Limitations
- 
EOF

echo "Created .agent-context/$AGENT_NAME/"
```

## Progressive Disclosure

**For detailed workflows**: See [scripts/onboarding-workflow.md](scripts/onboarding-workflow.md)

**For role-specific templates**: See [scripts/role-templates.md](scripts/role-templates.md)

**For common agent types**: See [scripts/agent-types.md](scripts/agent-types.md)

**For example contexts**: See [references/example-contexts/](references/example-contexts/)

---

*This skill follows the Anthropic Skills Framework v5.0 — goal-oriented, not a rigid recipe.*