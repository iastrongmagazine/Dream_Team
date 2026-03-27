# Split Strategy

## When to Split
When hitting token limits, split CLEANLY:

### Rules
1. Split at natural boundaries (between functions, components)
2. Never split mid-function
3. Never split mid-line
4. Mark split points clearly

### Split Format
```markdown
## Part 1 of N

[content]

---
继续继续继续 (Continuing in Part 2...)

## Part 2 of N

[content]
```

### Continuation Command
User says: "继续" or "continue" or "next part"
→ Continue exactly where left off

### Response to "Summarize"
If user asks for summary instead of full code:
→ Ask: "Do you want the full code or a summary?"
