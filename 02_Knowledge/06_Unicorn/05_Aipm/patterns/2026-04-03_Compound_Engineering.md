---
type: pattern
area: aipm
date: 2026-04-03
status: active
tags: [compound-engineering, multi-agent, orchestration, delegation]
---

## Compound Engineering

### What It Solves
Multi-agent orchestration pattern where different specialized agents collaborate on complex tasks. Each agent specializes in a domain, working together through delegation.

### When to Use
- Complex features requiring multiple domains
- Code review and quality assurance
- Parallel task execution
- Specialized expertise needed

### Architecture

```
                    ┌─────────────┐
                    │   USER     │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │ ORCHESTRATOR│ ← Main agent coordinates
                    │  (Planner)  │
                    └──────┬──────┘
                           │
         ┌───────────────┼───────────────┐
         │               │               │
    ┌────▼────┐    ┌────▼────┐    ┌────▼────┐
    │ Agent A │    │ Agent B │    │ Agent C │
    │ (Code)  │    │ (Review)│    │ (Test)  │
    └────┬────┘    └────┬────┘    └────┬────┘
         │               │               │
         └───────────────┼───────────────┘
                           │
                    ┌──────▼──────┐
                    │   RESULT    │
                    └─────────────┘
```

### Core Concepts

1. **Orchestrator**: Main agent that plans and delegates
2. **Specialized Agents**: Domain-specific agents (code, review, test, etc.)
3. **Delegation Protocol**: How agents communicate
4. **Result Aggregation**: Combining outputs

### Compound Skills Available

| Skill | Purpose | Trigger |
|-------|---------|---------|
| ce:brainstorm | Collaborative idea generation | "brainstorm" |
| ce:plan | Transform specs into implementation plans | "plan this" |
| ce:work | Execute work plans efficiently | "work on this" |
| ce:review | Code review with multiple personas | "review this" |
| ce:compound | Document solved problems | "compound this" |
| ce:ideate | Generate improvement ideas | "improve this" |

### Workflow

1. **Analyze** - Break problem into sub-tasks
2. **Delegate** - Assign to specialized agents
3. **Collect** - Gather results from agents
4. **Synthesize** - Combine into final output
5. **Verify** - Ensure quality

### Example

```
User: "Build a complete authentication system"

Orchestrator breaks down:
├── Agent-A (Code): Implement login/logout
├── Agent-B (Review): Review security
├── Agent-C (Test): Write tests
└── Agent-D (Docs): Document API

Each agent works in parallel
Results combined → Complete system
```

### Best Practices

- Define clear interfaces between agents
- Use appropriate agent for each task
- Aggregate results intelligently
- Handle agent failures gracefully