#!/usr/bin/env bash
# Task Complete Sound Hook
# Plays a sound when a task is completed

set -euo pipefail

if [ "$OSTYPE" = "win32" ]; then
    # Windows - using PowerShell
    powershell -Command "[Console]::Beep(800, 200); [Console]::Beep(1000, 200); [Console]::Beep(1200, 300)"
else
    # macOS
    if command -v afplay &>/dev/null; then
        afplay /System/Library/Sounds/Glass.aiff 2>/dev/null || echo "✅ Tarea completada"
    # Linux
    elif command -v beep &>/dev/null; then
        beep -f 800 -l 200 -n 1000 -l 200 -n 1200 -l 300
    else
        echo "✅ Tarea completada"
    fi
fi

echo "🔔 [HOOK] Task completed - Sound played"
