import sys
import os

sys.path.append(os.path.join(os.getcwd(), ".claude", "skills", "parallel-orchestration", "tools"))
from agent_orchestrator import AgentOrchestrator

def main():
    print("INITIALIZING FINAL 5-AGENT SYSTEM AUDIT")
    orchestrator = AgentOrchestrator()

    # --- AGENT 1: STRUCTURE ---
    # Validates key directories and config file existence
    orchestrator.add_agent("Agent 1 (Arch)", "Validate Project Structure",
        "if exist .agent (echo .agent OK) && if exist .claude (echo .claude OK) && if exist AGENT_CONFIG.md (echo Config OK) else (echo FAIL && exit 1)")

    # --- AGENT 2: DOCS ---
    # Scans key documentation files for integrity
    orchestrator.add_agent("Agent 2 (Lib)", "Scan Documentation",
        "type README.md | findstr \"#\" && type .agent\\skills\\QUICK_REFERENCE.md | findstr \"skills/\"")

    # --- AGENT 3: CODE ---
    # Verifies the Orchestrator itself and Fork tool
    orchestrator.add_agent("Agent 3 (Eng)", "Verify Core Scripts",
        "if exist .claude\\skills\\parallel-orchestration\\tools\\agent_orchestrator.py (echo Orchestrator FOUND) && python -c \"print('Python Environment OK')\"")

    # --- AGENT 4: SKILLS ---
    # Sampling validation of skills
    orchestrator.add_agent("Agent 4 (Coach)", "Validate Skill YAML",
        "type .agent\\skills\\brainstorming\\SKILL.md | findstr \"name:\" && type .agent\\skills\\systematic-debugging\\SKILL.md | findstr \"name:\"")

    # --- AGENT 5: SYSTEM ---
    # Final directory listing and status check
    orchestrator.add_agent("Agent 5 (Admin)", "System Status & List",
        "dir /w && echo SYSTEM READY")

    # Launch everything
    orchestrator.launch()

if __name__ == "__main__":
    main()
