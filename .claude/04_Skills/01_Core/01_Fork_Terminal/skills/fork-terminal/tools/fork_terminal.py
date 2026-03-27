#!/usr/bin/env -S uv run
"""Fork a new terminal window with a command."""

import platform
import subprocess
import os
import sys

def fork_terminal(command: str) -> str:
    """Open a new Terminal window and run the specified command."""
    system = platform.system()
    cwd = os.getcwd()

    if system == "Darwin":  # macOS
        # Build shell command - use single quotes for cd to avoid escaping issues
        # Then escape everything for AppleScript
        shell_command = f"cd '{cwd}' && {command}"
        # Escape for AppleScript: backslashes first, then quotes
        escaped_shell_command = shell_command.replace("\\", "\\\\").replace('"', '\\"')

        try:
            result = subprocess.run(
                ["osascript", "-e", f'tell application "Terminal" to do script "{escaped_shell_command}"'],
                capture_output=True,
                text=True,
            )
            output = f"stdout: {result.stdout.strip()}\nstderr: {result.stderr.strip()}\nreturn_code: {result.returncode}"
            return output
        except Exception as e:
            return f"Error: {str(e)}"

    elif system == "Windows":
        # Use /d flag to change drives if necessary
        # We explicitly provide a Title "Agent Terminal" to 'start' so it doesn't misinterpret quotes in the command as the title.
        # We also wrap the entire command block for /k in quotes to handle directory spaces safely.

        cmd_sequence = f'cd /d "{cwd}" && {command}'
        final_command = f'start "Agent Terminal" cmd /k "{cmd_sequence}"'

        try:
            # shell=True is required to use the 'start' command
            subprocess.Popen(final_command, shell=True)
            return "Windows terminal launched"
        except Exception as e:
            return f"Error launching Windows terminal: {str(e)}"

    else:  # Linux and others
        raise NotImplementedError(f"Platform {system} not supported")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        output = fork_terminal(" ".join(sys.argv[1:]))
        print(output)
