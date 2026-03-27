import sys
import os

sys.path.append(os.path.join(os.getcwd(), ".claude", "skills", "parallel-orchestration", "tools"))
from agent_orchestrator import AgentOrchestrator

def main():
    print("INITIALIZING 10-AGENT STRESS TEST via ORCHESTRATOR")
    orchestrator = AgentOrchestrator()

    # --- GROUP 1: IO STRESS (Agents 1-3) ---
    orchestrator.add_agent("Agent 1 - Maker", "Create Temp Tree A",
        "mkdir temp_a && cd temp_a && echo file1 > f1.txt && echo file2 > f2.txt && dir")

    orchestrator.add_agent("Agent 2 - Maker", "Create Temp Tree B",
        "mkdir temp_b && cd temp_b && echo file1 > f1.txt && echo file2 > f2.txt && dir")

    orchestrator.add_agent("Agent 3 - Maker", "Create Temp Tree C",
        "mkdir temp_c && cd temp_c && echo file1 > f1.txt && echo file2 > f2.txt && dir")

    # --- GROUP 2: READER STRESS (Agents 4-6) ---
    orchestrator.add_agent("Agent 4 - Reader", "Read README Info",
        "type .agent\\skills\\README.md | findstr \"Agent\"")

    orchestrator.add_agent("Agent 5 - Reader", "Read Config Info",
        "type AGENT_CONFIG.md || echo Config not found")

    orchestrator.add_agent("Agent 6 - Reader", "Read Skill Index",
        "type .agent\\skills\\QUICK_REFERENCE.md")

    # --- GROUP 3: SEARCH STRESS (Agents 7-9) ---
    orchestrator.add_agent("Agent 7 - Searcher", "Find YAML content",
        "findstr /s \"name:\" .agent\\skills\\*.md")

    orchestrator.add_agent("Agent 8 - Searcher", "Find Python files",
        "dir /s /b *.py")

    orchestrator.add_agent("Agent 9 - Searcher", "Find Markdown files",
        "dir /s /b *.md")

    # --- GROUP 4: VALIDATOR (Agent 10) ---
    orchestrator.add_agent("Agent 10 - Validator", "Validate Installation",
        "bash 07_Skill/validate-skills.sh")

    # Launch everything
    orchestrator.launch()

if __name__ == "__main__":
    main()
