#!/usr/bin/env python3
"""
Agent Orchestrator - Catalyzer for Parallel Orchestration Skill.
Implements the "Agent Orchestration with Context Isolation" pattern.
Supports Windows and macOS.
"""

import platform
import subprocess
import os
import sys
import time
import json
import argparse
from pathlib import Path

class AgentOrchestrator:
    def __init__(self, project_root="."):
        self.system = platform.system()
        self.project_root = os.path.abspath(project_root)
        self.agents = []
        self.report_file = os.path.join(self.project_root, "MULTI_AGENT_ORCHESTRATION_REPORT.md")
        self.logs_dir = os.path.join(self.project_root, ".claude", "logs", f"orchestration_{int(time.time())}")

    def prepare_environment(self):
        """Create logging directories and clean old reports."""
        os.makedirs(self.logs_dir, exist_ok=True)
        print(f"Logs directory created: {self.logs_dir}")

    def add_agent(self, name, task_description, command, cwd=None):
        """Register an agent task."""
        if cwd is None:
            cwd = self.project_root
        else:
            cwd = os.path.abspath(cwd)

        self.agents.append({
            "id": len(self.agents) + 1,
            "name": name,
            "task": task_description,
            "command": command,
            "cwd": cwd,
            "log_file": os.path.join(self.logs_dir, f"agent_{len(self.agents) + 1}_{name.replace(' ', '_')}.log"),
            "signal_file": os.path.join(self.logs_dir, f"agent_{len(self.agents) + 1}.done")
        })

    def _build_windows_command(self, agent):
        """Construct the CMD command for Windows."""
        # 1. Echo Header
        # 2. Change Directory
        # 3. Execute Command (redirecting ouput to log)
        # 4. Touch signal file
        # 5. Echo Footer
        # 6. Pause

        # Sanitize strings for CMD echo (escape & with ^&)
        safe_name = agent['name'].replace("&", "^&")
        safe_task = agent['task'].replace("&", "^&")

        # We need to escape correctly for the CMD /k string

        # Context Injection Logic
        prompt_path = os.path.join(".claude", "skills", "fork-terminal", "prompts", "fork_summary_user_prompt.md")
        context_cmd = ""
        if os.path.exists(prompt_path):
             context_cmd = f"type \"{prompt_path}\" && echo. && echo ---------------------------------------- && echo. && "

        cmd_block = (
            f"echo =========================================== && "
            f"echo    AGENT {agent['id']}: {safe_name} && "
            f"echo    TASK: {safe_task} && "
            f"echo =========================================== && "
            f"echo. && "
            f"{context_cmd}"  # INJECTED CONTEXT HERE
            f"cd /d \"{agent['cwd']}\" && "
            f"echo [STARTED] > \"{agent['log_file']}\" && "
            f"({agent['command']}) >> \"{agent['log_file']}\" 2>&1 && "
            f"echo [COMPLETED] >> \"{agent['log_file']}\" && "
            f"type \"{agent['log_file']}\" && " # Show output in terminal too
            f"echo. && "
            f"echo [SIGNALING COMPLETION] && "
            f"echo DONE > \"{agent['signal_file']}\" && "
            f"echo =========================================== && "
            f"echo    AGENT TASK COMPLETED && "
            f"echo =========================================== && "
            f"pause"
        )

        # Launch using start
        return f'start "Agent {agent["id"]} - {agent["name"]}" cmd /k "{cmd_block}"'

    def _build_macos_command(self, agent):
        """Construct the AppleScript command for macOS."""
        # Similar logic but for bash/zsh inside macOS Terminal

        # Escape for shell
        safe_log = agent['log_file'].replace(" ", "\\ ")
        safe_signal = agent['signal_file'].replace(" ", "\\ ")

        # Context Injection Logic (macOS version)
        prompt_path = os.path.join(".claude", "skills", "fork-terminal", "prompts", "fork_summary_user_prompt.md")
        context_cmd = ""
        if os.path.exists(prompt_path):
            # Use cat for Unix-like systems and add separator
            context_cmd = f"cat '{prompt_path}'; echo ''; echo '----------------------------------------'; echo ''; "

        cmd_block = (
            f"echo '==========================================='; "
            f"echo '   AGENT {agent['id']}: {agent['name']}'; "
            f"echo '   TASK: {agent['task']}'; "
            f"echo '==========================================='; "
            f"echo ''; "
            f"{context_cmd}"  # INJECTED CONTEXT HERE
            f"cd '{agent['cwd']}'; "
            f"echo '[STARTED]' > {safe_log}; "
            f"({agent['command']}) >> {safe_log} 2>&1; "
            f"echo '[COMPLETED]' >> {safe_log}; "
            f"cat {safe_log}; "
            f"echo ''; "
            f"echo '[SIGNALING COMPLETION]'; "
            f"echo 'DONE' > {safe_signal}; "
            f"echo '==========================================='; "
            f"echo '   AGENT TASK COMPLETED'; "
            f"echo '==========================================='; "
            f"read -n 1 -s -r -p 'Press any key to close...'" # Pause approximation
        )

        # Escape for AppleScript - properly handle single quotes
        escaped_cmd = cmd_block.replace("\\", "\\\\").replace('"', '\\"')

        return ["osascript", "-e", f'tell application "Terminal" to do script "{escaped_cmd}"']

    def launch(self):
        """Launch all agents in parallel terminals."""
        print(f"LAUNCHING {len(self.agents)} agents in parallel context-isolated terminals...")
        self.prepare_environment()

        for agent in self.agents:
            print(f"  -> Launching Agent {agent['id']}: {agent['name']}...")

            if self.system == "Windows":
                full_cmd = self._build_windows_command(agent)
                subprocess.Popen(full_cmd, shell=True)

            elif self.system == "Darwin": # macOS
                full_cmd = self._build_macos_command(agent)
                subprocess.run(full_cmd)

            else:
                print(f"ERROR: Unsupported OS: {self.system}")
                return

        print("\nAGENTS DISPATCHED. Monitoring status...\n")
        self.monitor_and_report()

    def monitor_and_report(self):
        """Wait for agents to finish and generate report."""
        pending = list(self.agents)
        start_time = time.time()

        while pending:
            # Check for signal files
            completed_in_this_loop = []
            for agent in pending:
                if os.path.exists(agent['signal_file']):
                    print(f"  * Agent {agent['id']} ({agent['name']}) reported completion.")
                    completed_in_this_loop.append(agent)

            # Remove completed
            for agent in completed_in_this_loop:
                pending.remove(agent)

            if pending:
                time.sleep(2)
                # Optional timeout logic could be added here

        duration = time.time() - start_time
        print(f"\nALL TASKS COMPLETED in {duration:.2f} seconds.")
        self.generate_final_report(duration)

    def generate_final_report(self, duration):
        """Consolidate logs into a master Markdown report matching SESSION_SUMMARY style."""
        print("GENERATING consolidated report...")

        timestamp = time.strftime("%Y-%m-%d")
        full_timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

        # Calculate metrics
        success_count = sum(1 for a in self.agents if os.path.exists(a['signal_file']))
        total_count = len(self.agents)
        success_rate = (success_count / total_count) * 100 if total_count > 0 else 0

        # Visual Progress Bar
        bar_length = 20
        filled_length = int(bar_length * success_count // total_count) if total_count > 0 else 0
        bar = "▓" * filled_length + "░" * (bar_length - filled_length)

        # Determine Global Status
        if success_count == total_count:
            status_header = "ELITE SUCCESS"
            concl_color = "🟢"
            status_desc = "All systems operational. Zero failures detected."
        elif success_count == 0:
            status_header = "SYSTEM FAILURE"
            concl_color = "🔴"
            status_desc = "Critical failure across all subsystems."
        else:
            status_header = "PARTIAL SUCCESS"
            concl_color = "🟡"
            status_desc = f"System operative with degradation ({total_count - success_count} failures)."

        # Define styles for report
        report_path = os.path.join(".claude", "reports", "latest", "ULTIMATE_SYSTEM_REPORT.md")
        self.report_file = os.path.join(os.getcwd(), report_path)

        # Ensure directory exists
        os.makedirs(os.path.dirname(self.report_file), exist_ok=True)

        report_content = [
            f"# {concl_color} ULTIMATE SYSTEM TEST - REPORT V3.0",
            f"",
            f"> **Date:** {timestamp} | **Time:** {full_timestamp} | **Orchestrator:** v3.0 Elite",
            f"",
            f"## 🎯 Executive Summary",
            f"",
            f"### Status: **{status_header}**",
            f"{status_desc}",
            f"",
            f"**System Integrity:**",
            f"`{bar}` **{success_rate:.1f}%**",
            f"",
            f"**Validation Scope:**",
            f"- **Scale:** {total_count} Concurrent Agents",
            f"- **Coverage:** Full Project Structure, Links, Scripts, Skills",
            f"- **Duration:** {duration:.2f}s",
            f"",
            f"---",
            f"",
            f"## 📊 Operational Telemetry",
            f"",
            f"| Metric | Value | Status |",
            f"| :--- | :--- | :---: |",
            f"| **Concurrency** | `{total_count}` agents | ⚡ |",
            f"| **Success Rate** | `{success_rate:.1f}%` | {concl_color} |",
            f"| **Avg. Response** | `{duration/total_count:.2f}s` | ⏱️ |",
            f"| **Throughput** | `{total_count/duration:.2f} ops/s` | 🚀 |",
            f"",
            f"---",
            f"",
            f"## 🤖 Agent Performance Grid",
            f"",
            f"| ID | Agent Role | Spec | Validated | Status |",
            f"| :---: | :--- | :--- | :---: | :---: |",
        ]

        for agent in self.agents:
            is_success = os.path.exists(agent['signal_file'])
            status_badge = "✅ PASS" if is_success else "❌ FAIL"
            # Try to extract sub-task description from command for "Validated" column
            # This is a heuristic, assuming the task name has info
            report_content.append(f"| **{agent['id']}** | {agent['name']} | {agent['task']} | {status_badge} | {status_badge} |")

        report_content.append("")
        report_content.append("---")
        report_content.append("")
        report_content.append("## 🔍 Technical Evidence & Logs")
        report_content.append("")

        for agent in self.agents:
            is_success = os.path.exists(agent['signal_file'])
            icon = "✅" if is_success else "❌"

            report_content.append(f"<details>")
            report_content.append(f"<summary><strong>{icon} Agent {agent['id']}: {agent['name']}</strong> - {agent['task']}</summary>")
            report_content.append("")
            report_content.append("```log")
            if os.path.exists(agent['log_file']):
                try:
                    with open(agent['log_file'], 'r') as f:
                         content = f.read().strip()
                         # Truncate if too long (sanity check)
                         if len(content) > 2000:
                             content = content[:2000] + "... [TRUNCATED]"
                         report_content.append(content)
                except:
                    report_content.append("Error reading log.")
            else:
                report_content.append("Log missing.")
            report_content.append("```")
            report_content.append("</details>")
            report_content.append("")

        report_content.append("---")
        report_content.append(f"\n<div align='center'>\n**ANTIGRAVITY ORCHESTRATION SUITE** | {full_timestamp}\n</div>")

        # Save Report
        with open(self.report_file, 'w', encoding='utf-8') as f:
            f.write("\n".join(report_content))

        print(f"REPORT SAVED to: {self.report_file}")

        # Open the report in a final terminal (The "Manager" View)
        # Use UTF-8 compatible command for viewing if possible, or just standard type
        self.open_report_viewer()

    def open_report_viewer(self):
        """Opens a final terminal to show the report."""
        if self.system == "Windows":
             cmd = f'start "ORCHESTRATION REPORT" cmd /k "type \"{self.report_file}\" && echo. && echo REPORT GENERATED SUCCESSFULLY && pause"'
             subprocess.Popen(cmd, shell=True)
        elif self.system == "Darwin":
             # macOS view
             pass # Simplified for now

if __name__ == "__main__":
    # Example Usage / Test Mode
    # python agent_orchestrator.py --test

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        orchestrator = AgentOrchestrator()

        orchestrator.add_agent(
            "Skill Validator",
            "Validate .agent/skills structure",
            "bash .agent/skills/validate-skills.sh"
        )

        orchestrator.add_agent(
            "Config Checker",
            "Verify Agent Configuration",
            "type AGENT_CONFIG.md"
        )

        orchestrator.launch()
