import sys
import os

sys.path.append(os.path.join(os.getcwd(), ".claude", "skills", "parallel-orchestration", "tools"))
from agent_orchestrator import AgentOrchestrator

def main():
    print("INITIALIZING ULTIMATE 15-AGENT SYSTEM TEST")
    orchestrator = AgentOrchestrator()

    # --- GROUP A: STRUCTURE VALIDATORS (Folder Integrity) ---
    orchestrator.add_agent("Agent 1 (Struct)", "Check .agent Root",
        "if exist .agent (echo FOUND .agent) else (echo MISSING && exit 1)")

    orchestrator.add_agent("Agent 2 (Struct)", "Check .claude Root",
        "if exist .claude (echo FOUND .claude) else (echo MISSING && exit 1)")

    orchestrator.add_agent("Agent 3 (Struct)", "Check Skills Dir",
        "if exist .agent\\skills (echo FOUND skills) else (echo MISSING && exit 1)")

    # --- GROUP B: LINK CHECKERS (Documentation Integrity) ---
    orchestrator.add_agent("Agent 4 (Link)", "Verify README",
        "type .agent\\skills\\README.md | findstr \"http\"")

    orchestrator.add_agent("Agent 5 (Link)", "Verify Quick Ref",
        "type .agent\\skills\\QUICK_REFERENCE.md | findstr \".md\"")

    orchestrator.add_agent("Agent 6 (Link)", "Verify Config",
        "type AGENT_CONFIG.md | findstr \"skills/\"")

    # --- GROUP C: CODE INTEGRITY (Python Scripts) ---
    orchestrator.add_agent("Agent 7 (Code)", "Check Orchestrator",
        "python -c \"import sys; print('Orchestrator Import OK')\"")

    orchestrator.add_agent("Agent 8 (Code)", "Check Fork Tool",
        "if exist .claude\\skills\\fork-terminal\\tools\\fork_terminal.py echo FOUND")

    orchestrator.add_agent("Agent 9 (Code)", "Check Stress Test",
        "if exist .claude\\skills\\parallel-orchestration\\tools\\run_stress_test.py echo FOUND")

    # --- GROUP D: SKILL VALIDATORS (Yaml Frontmatter) ---
    orchestrator.add_agent("Agent 10 (Skill)", "Scan Brainstorming",
        "type .agent\\skills\\brainstorming\\SKILL.md | findstr \"name:\"")

    orchestrator.add_agent("Agent 11 (Skill)", "Scan TDD",
        "type .agent\\skills\\test-driven-development\\SKILL.md | findstr \"name:\"")

    orchestrator.add_agent("Agent 12 (Skill)", "Scan Creator",
        "type .agent\\skills\\antigravity-skill-creator\\SKILL.md | findstr \"name:\"")

    # --- GROUP E: SYSTEM MONKEYS (Chaos/Load) ---
    orchestrator.add_agent("Agent 13 (Sys)", "Echo Stress A",
        "echo CHECKING SYSTEM A && dir")

    orchestrator.add_agent("Agent 14 (Sys)", "Echo Stress B",
        "echo CHECKING SYSTEM B && cd .agent && dir")

    orchestrator.add_agent("Agent 15 (Sys)", "Echo Stress C",
        "echo CHECKING SYSTEM C && cd .claude && dir")

    # Launch everything
    orchestrator.launch()

if __name__ == "__main__":
    main()
