# Anthropic Standards for Skills

Based on Lessons from Building Claude Code (Thariq Shihipar)

## Core Principle: Steering Distribution

Skills are "forcing functions" that push Claude out of its default probability distribution toward specific, unique outputs.

## 9 Types of Skills (Anthropic Categorization)

1. **Library & API Reference** - How to use libs/CLIs
2. **Product Verification** - Testing/verification workflows
3. **Data Fetching & Analysis** - Connect to data/monitoring
4. **Business Process & Team Automation** - Repetitive workflows
5. **Code Scaffolding & Templates** - Generate boilerplate
6. **Code Quality & Review** - Enforce quality standards
7. **CI/CD & Deployment** - Deploy/push code
8. **Runbooks** - Symptom → Investigation → Report
9. **Infrastructure Operations** - Routine maintenance

## Best Practices

### 1. Description is For the Model
- NOT marketing text
- Semantic triggers user actually says
- Example: "triggers on: weekly planning, review progress, goal check-in"

### 2. Gotchas Section (Most Valuable!)
- Document errors Claude commonly makes
- Build incrementally over time
- Like training a new employee

### 3. Progressive Disclosure
- Don't cram everything in SKILL.md
- Use references/ for heavy docs
- Use scripts/ for automation

### 4. Avoid Railroading
- Goal-oriented > rigid recipes
- Give Claude flexibility to adapt
- Example GOOD: "Prepare interview questions for this role"

### 5. Use Scripts & Code
- Pre-built scripts = Claude composes, doesn't reconstruct
- Reduces token usage
- More reliable

### 6. State Persistence
- Store data between runs
- Use `${CLAUDE_PLUGIN_DATA}` for stable storage
- Enables continuity

### 7. On-Demand Hooks
- Restrict tools when needed
- Only activate when skill runs
- Example: `/careful` blocks dangerous commands

## Anti-Patterns

❌ Stating the obvious
❌ Rigid workflows without flexibility
❌ No error documentation
❌ Everything in one file
❌ Marketing-style descriptions

## Resources

- [Anthropic Skills Docs](https://code.claude.com/docs/en/skills)
- [Skill Creator](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills)
