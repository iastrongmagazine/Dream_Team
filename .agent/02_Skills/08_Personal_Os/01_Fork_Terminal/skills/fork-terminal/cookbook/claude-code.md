# Purpose

Create a new Claude code agent to execute the command.

## Variables

DEFAULT_MODEL: claude-sonnet-4.5
BASE_MODEL: claude-sonnet-4.5
FAST_MODEL: claude-haiku-4.5
HEAVY_MODEL: claude-opus-4.5

## Instructions

- For the --model argument, use the DEFAULT_MODEL if not specified. If 'fast' is requested, use the FAST_MODEL. If 'heavy' is requested, use the HEAVY_MODEL.
- Always run with `--dangerously-skip-permissions`
- If the user requested a summary, pass the filled-out fork_summary_user_prompt.md content as the PROMPT argument.

## Workflow

1. Determine which model to use based on user request
2. Construct the command: `claude --model <MODEL> --dangerously-skip-permissions "<PROMPT>"`
3. Execute: `python .claude/skills/fork-terminal/tools/fork_terminal.py "claude --model <MODEL> --dangerously-skip-permissions \"<PROMPT>\""`

## Examples

### Without Summary

```bash
python .claude/skills/fork-terminal/tools/fork_terminal.py "claude --model claude-sonnet-4.5 --dangerously-skip-permissions \"analyze SKILL.md and write a summary to temp/skill-analysis.md\""
```

### With Summary (context handoff)

```bash
python .claude/skills/fork-terminal/tools/fork_terminal.py "claude --model claude-sonnet-4.5 --dangerously-skip-permissions \"<filled fork_summary_user_prompt content here>\""
```
