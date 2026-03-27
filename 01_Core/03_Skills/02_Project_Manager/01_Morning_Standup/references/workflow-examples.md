# Morning Standup — Workflow Examples

## Example 1: Ideal Standup

```
🎯 Today's Focus (3 tasks max)

1. [P0] Complete API endpoint /users/:id — est: 45min
   → Blocked by: Awaiting DB schema from Backend team

2. [P1] Write unit tests for user auth — est: 30min
   → Part of: Q1 OKR User Authentication

3. [P1] Review PR #234 — est: 15min
   → Reviewer assigned: @frontend-team

⚡ Quick Wins: Update README (10min)
🚧 Blockers: 1 task blocked (see below)
```

## Example 2: Blocked Tasks Present

```
🚧 BLOCKED TASKS:

- Task: "Integrate Stripe payments"
  - Blocker: "Waiting for API keys from Finance"
  - Action: Ping @finance-team in Slack
  
- Task: "Fix login bug on iOS"
  - Blocker: "Can't reproduce on simulator"
  - Action: Schedule sync with Mobile team
```

## Example 3: Goal Alignment

```
📎 Aligning with Q1 Goals:

- Goal: "Launch user authentication"
  → Tasks: 1, 2 (above)
  
- Goal: "Improve code coverage to 80%"
  → Tasks: Writing tests for user auth
```

## Output Format

```markdown
## 🎯 Today's Focus

1. [P0] Task Name — est: Time
   → Context/Why

2. [P1] Task Name — est: Time
   → Context/Why

3. [P1] Task Name — est: Time
   → Context/Why

## ⚡ Quick Wins
- Quick task — est: Time

## 🚧 Blockers
- Task: "Name" — Blocker: "Reason"
  → Action: What to do
```
