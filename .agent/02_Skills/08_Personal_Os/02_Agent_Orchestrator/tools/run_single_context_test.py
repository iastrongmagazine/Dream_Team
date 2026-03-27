import sys
import os

sys.path.append(os.path.join(os.getcwd(), ".claude", "skills", "parallel-orchestration", "tools"))
from agent_orchestrator import AgentOrchestrator

def main():
    print("TESTING CONTEXT INJECTION (Single Agent)")
    orchestrator = AgentOrchestrator()

    # Simple task to verify context injection visually
    orchestrator.add_agent(
        "Context Scout",
        "Verify Context Injection",
        "echo CHECKING CONTEXT... && dir .claude\\skills\\fork-terminal\\prompts"
    )

    orchestrator.launch()

if __name__ == "__main__":
    main()
