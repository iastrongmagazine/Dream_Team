import sys
import os

sys.path.append(os.path.join(os.getcwd(), ".claude", "skills", "parallel-orchestration", "tools"))
from agent_orchestrator import AgentOrchestrator

def main():
    print("INITIALIZING 20-AGENT SWARM STRESS TEST")
    orchestrator = AgentOrchestrator()

    # GROUP 1: IO STRUCTURE (1-5)
    for i in range(1, 6):
        orchestrator.add_agent(f"Swarm-{i} (IO)", f"Check IO Block {i}", f"dir .claude")

    # GROUP 2: DOC SCANNERS (6-10)
    for i in range(6, 11):
        orchestrator.add_agent(f"Swarm-{i} (Doc)", f"Scan Manuals {i}", "type README.md | findstr \"Agent\"")

    # GROUP 3: PING/ECHO (11-15) - Fast tasks
    for i in range(11, 16):
        orchestrator.add_agent(f"Swarm-{i} (Ping)", f"Ping Check {i}", f"echo AGENT-{i} ALIVE && echo PONG")

    # GROUP 4: SKILL VALIDATORS (16-20)
    skills = ["brainstorming", "brand-identity", "executing-plans", "writing-plans", "systematic-debugging"]
    for i, skill in enumerate(skills):
        agent_num = 16 + i
        orchestrator.add_agent(f"Swarm-{agent_num} (Skill)", f"Validate {skill}", \
            f"if exist .agent\\skills\\{skill}\\SKILL.md (echo OK) else (echo FAIL)")

    # Launch the swarm
    orchestrator.launch()

if __name__ == "__main__":
    main()
