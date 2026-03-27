# Wave Execution

## Concept

Wave execution groups tasks that can run in parallel into "waves" or "phases".

## Example Wave Structure

```
Wave 1 (Foundation)
├── task-1: Setup repo
├── task-2: Create config
└── task-3: Init tests

Wave 2 (Core)
├── task-4: Build core (depends on 1,2)
├── task-5: Write tests (depends on 3)
└── task-6: Documentation (depends on 1)

Wave 3 (Polish)
├── task-7: Integration (depends on 4,5)
├── task-8: Review (depends on 6)
└── task-9: Deploy (depends on 7)
```

## Benefits

- **Parallelism**: Tasks in same wave can run together
- **Clarity**: Each wave has a clear goal
- **Progress**: Easy to see what's done vs pending
- **Recovery**: If wave fails, you know exactly what to retry

## Rules

1. Each wave should complete before next starts
2. Tasks in same wave should be roughly same size
3. Max 5 tasks per wave
4. Document dependencies clearly

## Best Practices

- Start each wave with a clear objective
- End each wave with a validation step
- Keep waves short (1-2 days max)
