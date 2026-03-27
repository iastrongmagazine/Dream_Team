#!/usr/bin/env python3
"""
05_Harness/context_monitor.py — Context Monitor Hook

Hook de PreToolUse para detectar context anxiety antes de ejecutar.
Similar a pre_tool_use.py pero específico para el sistema de harness.

VERSIÓN: 1.0
 fecha: 2026-03-26
 FILOSOFÍA: "No te traiciones, no te abandones" — Siempre lo correcto
"""

import os
import sys
import json
from pathlib import Path

# ========================
# CONFIGURATION
# ========================

# Thresholds
CONTEXT_ANXIETY_THRESHOLD = 0.80  # 80% de tokens
WARNING_THRESHOLD = 0.60  # 60% warning

# Log file
LOG_FILE = ".claude/logs/context_monitor.log"


def check_context():
    """Check current context for anxiety indicators"""

    # Get token count from environment (if available)
    token_count = int(os.getenv("CONTEXT_TOKEN_COUNT", 0))

    # If no token count, try to get from Claude's context
    if token_count == 0:
        # Try to read from Claude's context file if available
        context_file = Path(".claude/current_context.json")
        if context_file.exists():
            try:
                with open(context_file) as f:
                    data = json.load(f)
                    token_count = data.get("token_count", 0)
            except:
                pass

    # Default threshold (200K for most models)
    max_tokens = 200000

    usage = token_count / max_tokens if max_tokens > 0 else 0

    # Determine action
    if usage >= CONTEXT_ANXIETY_THRESHOLD:
        status = "CRITICAL"
        action = "RESET"
        message = f"Context at {usage:.0%} - context anxiety likely"
    elif usage >= WARNING_THRESHOLD:
        status = "WARNING"
        action = "COMPACT"
        message = f"Context at {usage:.0%} - consider compaction"
    else:
        status = "OK"
        action = "CONTINUE"
        message = f"Context at {usage:.0%} - healthy"

    # Log
    log_entry = {
        "status": status,
        "action": action,
        "token_count": token_count,
        "usage": usage,
        "message": message,
    }

    print(f"\n🧠 CONTEXT MONITOR: {status}")
    print(f"   Usage: {usage:.0%} ({token_count}/{max_tokens})")
    print(f"   Action: {action}")
    print(f"   Message: {message}\n")

    # Save to log
    try:
        Path(LOG_FILE).parent.mkdir(parents=True, exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except:
        pass

    # Return action for integration
    return action, status


def main():
    """Main entry point"""
    action, status = check_context()

    # Exit with code based on status
    if status == "CRITICAL":
        print("⚠️  Consider running Context Manager before proceeding")
        sys.exit(0)  # Don't block, just warn
    elif status == "WARNING":
        print("💡 Tip: Consider running Context Manager")
        sys.exit(0)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
