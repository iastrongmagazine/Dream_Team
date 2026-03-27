# Project Manager

## Purpose
Workflow orchestration for project management tasks including standups, backlog triage, reviews, and development rituals. Maintains project momentum and team coordination.

## Skills Included
| # | Skill | Trigger | Status | Enhancements |
|---|-------|---------|--------|--------------|
| 01 | Morning Standup | "standup", "daily", "reunión matutina" | ✅ ELITE | Gotchas + References + Scripts |
| 02 | Backlog Processing | "backlog", "triage", "priorizar" | ✅ IMPROVED | Gotchas added |
| 03 | Weekly Review | "weekly review", "revisión semanal" | 🔲 Pending | - |
| 04 | Sunday Ritual | "sunday ritual", "cierre semanal" | 🔲 Pending | - |
| 05 | Best Practices | "best practices", "buenas prácticas" | 🔲 Pending | - |
| 06 | Finishing Dev Branch | "finish branch", "cerrar rama" | 🔲 Pending | - |
| 07 | Running Tests | "run tests", "ejecutar tests" | 🔲 Pending | - |
| 08 | Content Generation | "generate content", "generar contenido" | 🔲 Pending | - |

## Enhancement Status (Anthropic Skills)
- ✅ **Gotchas**: Error patterns to avoid (Anthropic pattern)
- ✅ **References**: Progressive disclosure docs
- ✅ **Scripts**: Executable automation scripts

## Usage
```
"run morning standup"        # Generate daily standup report
"process the backlog"       # Triage and prioritize backlog items
"weekly review"              # Conduct weekly project review
"sunday ritual"              # Execute end-of-week cleanup
"best practices check"      # Review code against standards
"finish my feature branch"   # Complete branch with PR workflow
"run all tests"             # Execute test suite
```

## Related Profiles
- Agent Teams Lite (task breakdown and execution)
- Product Manager (requirements and priorities)
- Testing (quality assurance)

## Elite Validation (Skill 01)
All scripts tested 3x with real data:
- `format-standup.py` → ✅ Shows real tasks + [BLOCKED] flags
- `check-blockers.py --action` → ✅ Lists blockers + suggestions
- `--include-p2` → ✅ Includes P2 correctly
