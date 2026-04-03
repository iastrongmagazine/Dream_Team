---
type: pattern
area: aipm
date: 2026-04-03
status: active
tags: [agent-orchestration, multi-agent, coordination, workflow]
---

## Agent Orchestration Patterns

### What It Solves
Systematic approaches to coordinating multiple AI agents to work together on complex tasks. Different from simple delegation - includes planning, monitoring, and result synthesis.

### When to Use
- Complex workflows requiring multiple specialized agents
- Parallel execution of independent tasks
- Sequential workflows with dependencies
- Quality assurance through multiple perspectives

---

## Pattern 1: Sequential Chain

### Description
Agents execute one after another, passing results forward.

```
Agent A → Agent B → Agent C → Agent D
```

### Use Case
- Linear workflows where each step depends on previous
- Code: Write → Review → Test → Deploy

### Example
```python
result_a = agent_a.execute("Write authentication code")
result_b = agent_b.execute(f"Review: {result_a}")
result_c = agent_c.execute(f"Test: {result_b}")
final = agent_d.execute(f"Deploy: {result_c}")
```

---

## Pattern 2: Parallel Fan-Out

### Description
One agent spawns multiple agents simultaneously, then aggregates results.

```
        ┌─ Agent A ─┐
Orch ───┼─ Agent B ─┼──► Aggregate
        └─ Agent C ─┘
```

### Use Case
- Independent tasks that can run simultaneously
- Code review by multiple personas
- Testing on different platforms

### Example
```python
results = await Promise.all([
    agent_code.execute(task),
    agent_review.execute(task),
    agent_test.execute(task)
])
final = aggregate(results)
```

---

## Pattern 3: Supervisor Pattern

### Description
A supervisor agent manages a team of worker agents, assigning tasks and handling results.

```
        ┌──────────────┐
        │  Supervisor │
        │   (agent)    │
        └──────┬───────┘
               │
    ┌──────────┼──────────┐
    │          │          │
┌───▼───┐ ┌───▼───┐ ┌───▼───┐
│Agent 1│ │Agent 2│ │Agent 3│
└───────┘ └───────┘ └───────┘
```

### Use Case
- Dynamic task assignment
- Load balancing between agents
- Error handling and retry

---

## Pattern 4: Router Pattern

### Description
An agent analyzes incoming requests and routes to the most appropriate specialist agent.

```
User → Router Agent → Specialized Agent → Response
```

### Use Case
- Multi-domain systems
- Intent detection
- Skill-based routing

### Example
```
If request contains "review" → route to Review Agent
If request contains "test" → route to Test Agent  
If request contains "deploy" → route to Deploy Agent
```

---

## Pattern 5: Pipeline Pattern

### Description
Data flows through multiple transformation stages, each handled by a specialized agent.

```
Input → Agent A → Data → Agent B → Data → Agent C → Output
```

### Use Case
- Data processing pipelines
- Content creation workflows
- Multi-stage transformations

---

## Pattern 6: Feedback Loop

### Description
Agent output feeds back as input for refinement, iterating until quality threshold.

```
Agent → Output → Evaluation → (pass?) → Output
                      │
                      └── no ──► Agent (refine)
```

### Use Case
- Code generation with refinement
- Content generation
- Complex problem solving

---

## Implementation in PersonalOS

### Tools Used
- **Task Tool**: Execute sub-agents
- **Delegate Tool**: Persistent delegation
- **Engram**: Memory across sessions

### Configuration

```yaml
orchestration:
  strategy: sequential|parallel|supervisor|router|pipeline|feedback
  max_retries: 3
  timeout: 300s
  aggregation: first|all|majority|weighted
```

### Monitoring
- Track agent execution times
- Log delegation chains
- Measure success rates

---

## Best Practices

1. **Define clear interfaces** - Agents communicate through structured data
2. **Set appropriate timeouts** - Long-running agents need limits
3. **Handle failures** - What happens when an agent fails?
4. **Aggregate wisely** - How to combine multiple results?
5. **Monitor performance** - Track agent efficiency

### Anti-Patterns
- Too many parallel agents (resource exhaustion)
- No error handling
- Synchronous waiting when parallel possible
- Ignoring agent failures