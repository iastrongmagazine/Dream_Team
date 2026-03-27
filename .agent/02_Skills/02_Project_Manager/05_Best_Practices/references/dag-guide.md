# DAG Guide

## What is a DAG?

**Directed Acyclic Graph** - A way to model task dependencies without cycles.

## DAG Structure

```json
{
  "tasks": {
    "task-1": {
      "description": "Foundation setup",
      "depends_on": [],
      "status": "pending"
    },
    "task-2": {
      "description": "Config layer",
      "depends_on": ["task-1"],
      "status": "pending"
    },
    "task-3": {
      "description": "Execution",
      "depends_on": ["task-2"],
      "status": "pending"
    }
  }
}
```

## Why DAG?

- **Explicit dependencies** - No hidden order requirements
- **Parallel execution** - Tasks without dependencies can run together
- **Visual clarity** - See the whole picture
- **Error isolation** - Failures don't cascade

## Rules

1. No circular dependencies
2. Each task has explicit `depends_on`
3. Use wave execution (tasks in same wave can parallelize)
4. Store DAG in `tasks.json` or `DAG.md`

## Wave Strategy

- **Wave 1**: Foundation (no deps)
- **Wave 2**: Config (depends on Wave 1)
- **Wave 3**: Execution (depends on Wave 2)
- etc.
