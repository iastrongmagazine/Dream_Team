# Purpose

Create a new Gemini agent to execute the command.

## Variables

DEFAULT_MODEL: gemini-3-pro
BASE_MODEL: gemini-3-pro
FAST_MODEL: gemini-3-flash
HEAVY_MODEL: gemini-3-deep-think

## Instructions

- Before executing the command, run `gemini --help` to understand the command and its options.
- Always use interactive mode.
- For the model argument, use the DEFAULT_MODEL if not specified. If 'fast' is requested, use the FAST_MODEL. If 'heavy' is requested, use the HEAVY_MODEL.
- Always ensure the session is initialized with maximum permissions for the sub-agent.
- If the user requested a summary, pass the filled-out fork_summary_user_prompt.md content as the PROMPT argument.

## Workflow

1. Determine which model to use based on user request
2. Construct the command: `gemini --model <MODEL> "<PROMPT>"`
3. Execute: `python .claude/skills/fork-terminal/tools/fork_terminal.py "gemini --model <MODEL> \"<PROMPT>\""`

## Examples

### Without Summary

```bash
python .claude/skills/fork-terminal/tools/fork_terminal.py "gemini --model gemini-3-pro \"analyze SKILL.md and create a summary\""
```

### With Summary (context handoff)

```bash
python .claude/skills/fork-terminal/tools/fork_terminal.py "gemini --model gemini-3-pro \"<filled fork_summary_user_prompt content here>\""
```
