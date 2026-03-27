# Agent Teams Lite

## Purpose
Orchestration framework for coordinating multi-agent workflows using SDD (Spec-Driven Development). Enables parallel task execution with proper delegation patterns and state management.

## Skills Included
| # | Skill | Trigger | Description |
|---|-------|---------|-------------|
| 01 | sdd-init | "sdd init", "iniciar sdd" | Initialize SDD context, detect stack and bootstrap persistence |
| 02 | sdd-explore | "sdd explore {topic}", "investigar" | Explore and investigate ideas before committing to changes |
| 03 | sdd-propose | "sdd propose", "crear propuesta" | Create change proposals with intent, scope, and approach |
| 04 | sdd-spec | "sdd spec", "especificación" | Write specifications with requirements and scenarios |
| 05 | sdd-design | "sdd design", "diseño técnico" | Create technical design documents with architecture decisions |
| 06 | sdd-tasks | "sdd tasks", "descomponer tareas" | Break down changes into implementation task checklists |
| 07 | sdd-apply | "sdd apply", "implementar" | Implement tasks following specs and design |
| 08 | sdd-verify | "sdd verify", "verificar" | Validate that implementation matches specs, design, and tasks |
| 09 | sdd-archive | "sdd archive", "archivar" | Sync delta specs to main specs and archive completed changes |

## Usage
```
/sdd init                    # Initialize SDD in project
/sdd explore {topic}        # Explore an idea or feature
/sdd new {change}           # Create full SDD cycle for new change
/sdd ff {change}            # Fast-forward: propose -> spec -> design -> tasks
/sdd apply {change}         # Implement tasks from a change
/sdd verify {change}        # Verify implementation
/sdd archive {change}       # Archive completed change
```

## Related Profiles
- Project Manager (planning and task management)
- Product Manager (requirements and specifications)
