# Purpose

Execute a raw CLI command.

## Instructions

- Before executing the command, run `<command> --help` to understand the command and its options.
- Validate that the command is safe and appropriate for the user's request.

## Workflow

1. Understand the user's requested CLI command
2. Optionally run `<command> --help` to verify command syntax
3. Construct the full command string
4. Execute: `python .claude/skills/fork-terminal/tools/fork_terminal.py "<FULL_COMMAND>"`

## Examples

### Simple command

```bash
python .claude/skills/fork-terminal/tools/fork_terminal.py "dir /s"
```

### Multiple commands

```bash
python .claude/skills/fork-terminal/tools/fork_terminal.py "cd src && npm run build"
```

### Long-running process

```bash
python .claude/skills/fork-terminal/tools/fork_terminal.py "npm run dev"
```
