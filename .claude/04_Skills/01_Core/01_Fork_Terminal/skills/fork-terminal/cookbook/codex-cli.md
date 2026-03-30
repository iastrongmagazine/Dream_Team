# Purpose

Create a new Codex/OpenAI agent to execute the command.

## Variables

DEFAULT_MODEL: gpt-5.2
BASE_MODEL: gpt-5.2
FAST_MODEL: gpt-5-mini
HEAVY_MODEL: gpt-5-codex-max

## Instructions

- Before executing the command, run `codex --help` to understand the command and its options.
- Always use interactive mode.
- For the model argument, use the DEFAULT_MODEL if not specified. If 'fast' is requested, use the FAST_MODEL. If 'heavy' is requested, use the HEAVY_MODEL.
- Always enable unrestricted execution mode for the sub-agent task.
- If the user requested a summary, pass the filled-out fork_summary_user_prompt.md content as the PROMPT argument.

## Workflow

1. Determine which model to use based on user request
2. Construct the command: `codex --model <MODEL> "<PROMPT>"`
3. Execute: `python 01_Core/03_Skills/fork-terminal/tools/fork_terminal.py "codex --model <MODEL> \"<PROMPT>\""`

## Examples

### Without Summary

```bash
python 01_Core/03_Skills/fork-terminal/tools/fork_terminal.py "codex --model gpt-5.2 \"review the codebase and suggest improvements\""
```

### With Summary (context handoff)

```bash
python 01_Core/03_Skills/fork-terminal/tools/fork_terminal.py "codex --model gpt-5.2 \"<filled fork_summary_user_prompt content here>\""
```
