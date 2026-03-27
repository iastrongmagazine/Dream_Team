import sys
import os

# Add tools directory to path
sys.path.append(os.path.join(os.getcwd(), ".claude", "skills", "parallel-orchestration", "tools"))

from agent_orchestrator import AgentOrchestrator

def main():
    print("INITIALIZING FULL SYSTEM TEST via ORCHESTRATOR")
    orchestrator = AgentOrchestrator()

    # AGENT 1: Logic Skills Validator
    # Checks brainstorming and antigravity-skill-creator
    orchestrator.add_agent(
        "Agent Logic",
        "Validate Logic & Creation Skills",
        "echo CHECKING LOGIC SKILLS && "
        "echo --------------------- && "
        "echo [brainstorming] && "
        "type .agent\\skills\\brainstorming\\SKILL.md | findstr \"name:\" && "
        "echo. && "
        "echo [antigravity-skill-creator] && "
        "type .agent\\skills\\antigravity-skill-creator\\SKILL.md | findstr \"name:\""
    )

    # AGENT 2: Development Skills Validator
    # Checks TDD, Systematic Debugging, Verification
    orchestrator.add_agent(
        "Agent Dev",
        "Validate Development Skills",
        "echo CHECKING DEV SKILLS && "
        "echo ------------------ && "
        "echo [test-driven-development] && "
        "type .agent\\skills\\test-driven-development\\SKILL.md | findstr \"Iron Law\" && "
        "echo. && "
        "echo [systematic-debugging] && "
        "type .agent\\skills\\systematic-debugging\\SKILL.md | findstr \"Iron Law\" && "
        "echo. && "
        "echo [verification-before-completion] && "
        "type .agent\\skills\\verification-before-completion\\SKILL.md | findstr \"Iron Law\""
    )

    # AGENT 3: Operations Skills Validator
    # Checks Git Worktrees, Finishing Branch, Planning
    orchestrator.add_agent(
        "Agent Ops",
        "Validate Ops & Planning Skills",
        "echo CHECKING OPS SKILLS && "
        "echo ----------------- && "
        "echo [using-git-worktrees] && "
        "dir .agent\\skills\\using-git-worktrees\\SKILL.md && "
        "echo. && "
        "echo [finishing-a-development-branch] && "
        "dir .agent\\skills\\finishing-a-development-branch\\SKILL.md && "
        "echo. && "
        "echo [writing-plans] && "
        "dir .agent\\skills\\writing-plans\\SKILL.md"
    )

    # AGENT 4: Global Documentation Validator
    # Checks README, Config reports
    orchestrator.add_agent(
        "Agent Docs",
        "Validate Global Documentation",
        "echo CHECKING DOCUMENTATION && "
        "echo --------------------- && "
        "echo [README.md] && "
        "dir .agent\\skills\\README.md && "
        "echo. && "
        "echo [QUICK_REFERENCE.md] && "
        "dir .agent\\skills\\QUICK_REFERENCE.md && "
        "echo. && "
        "echo [AGENT_CONFIG.md] && "
        "type AGENT_CONFIG.md | findstr \"Priority\""
    )

    # Launch everything
    orchestrator.launch()

if __name__ == "__main__":
    main()
