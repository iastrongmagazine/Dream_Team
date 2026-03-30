#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Update Links - PersonalOS v6.1
Actualiza enlaces del sistema.
"""

import os
import sys
import glob
import subprocess
import io
from pathlib import Path

# === SETUP PATHS ===
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# === IMPORTS ===
try:
    from config_paths import (
        ROOT_DIR,
        BRAIN_DIR,
        BRAIN_RULES_DIR,
        COMPOUND_ENGINE_DIR,
        ENGINE_DIR,
    )
except ImportError:
    ROOT_DIR = PROJECT_ROOT
    BRAIN_DIR = PROJECT_ROOT / "04_Operations"
    BRAIN_RULES_DIR = BRAIN_DIR / "04_Memory_Brain"
    COMPOUND_ENGINE_DIR = (
        PROJECT_ROOT / "01_Core" / "03_Skills" / "00_Compound_Engineering"
    )
    ENGINE_DIR = PROJECT_ROOT / "08_Scripts_Os"

# === COLOR SETUP ===
try:
    from colorama import init, Fore, Style

    init(autoreset=True)
except ImportError:

    class Fore:
        CYAN = GREEN = RED = YELLOW = MAGENTA = ""

    class Style:
        RESET_ALL = ""


REQUIRED_DIRS = [
    "00_Core",
    "01_Brain",
    "02_Operations",
    "03_Knowledge",
    "04_Engine",
    "05_System",
    "06_Archive",
]
for d in REQUIRED_DIRS:
    if not (PROJECT_ROOT / d).exists():
        print(f"[WARN] Required directory not found: {d}")

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


def dynamic_speak(text):
    """Interfaz de Voz SOTA v2.2"""
    print(f"{Fore.MAGENTA}🔊 [VOICE]: {text}{Style.RESET_ALL}")
    if sys.platform == "win32":
        try:
            cmd = f"PowerShell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}')\""
            subprocess.Popen(
                cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
        except:
            pass


def print_banner():
    banner = rf"""
{Fore.BLUE}    ###########################################################################
    #                                                                         #
    #      _      _____ _   _ _  __  _    _ _____  _____         _______ ______ #
    #     | |    |_   _| \ | | |/ / | |  | |  __ \|  __ \     /\|__   __|  ____|#
    #     | |      | | |  \| | ' /  | |  | | |__) | |  | |   /  \  | |  | |__   #
    #     | |      | | | . ` |  <   | |  | |  ___/| |  | |  / /\ \ | |  |  __|  #
    #     | |____ _| |_| |\  | . \  | |__| | |    | |__| | / ____ \| |  | |____ #
    #     |______|_____|_| \_|_|\_\  \____/|_|    |_____/ /_/    \_\_|  |______|#
    #                                                                         #
    #                        L I N K   U P D A T E R                          #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


ROOT_DIR = PROJECT_ROOT


# Real mapping of path renames for v4.0
RENAMES = {
    # ai_docs renaming (XX_)
    "ai_docs/Process_Notes/01_setup_standares_sv_2026-02-02.md": "ai_docs/Process_Notes/01_setup_standares_sv_2026-02-02.md",
    "ai_docs/Template/01_ai_task_template.md": "ai_docs/Template/01_ai_task_template.md",
    "ai_docs/Template/02_process_note_template.md": "ai_docs/Template/02_process_note_template.md",
    "ai_docs/Docs_AI/01_anthropic_slash_commands.md": "ai_docs/Docs_AI/01_anthropic_slash_commands.md",
    "ai_docs/Docs_AI/02_anthropic_subagents.md": "ai_docs/Docs_AI/02_anthropic_subagents.md",
    "ai_docs/Docs_AI/03_anthropic_output_styles.md": "ai_docs/Docs_AI/03_anthropic_output_styles.md",
    "ai_docs/Docs_AI/04_anthropic_quick_start.md": "ai_docs/Docs_AI/04_anthropic_quick_start.md",
    "ai_docs/Docs_AI/05_cc_hooks_docs.md": "ai_docs/Docs_AI/05_cc_hooks_docs.md",
    "ai_docs/Docs_AI/06_cc_hooks_repomix.xml": "ai_docs/Docs_AI/06_cc_hooks_repomix.xml",
    "ai_docs/Docs_AI/07_openai_quick_start.md": "ai_docs/Docs_AI/07_openai_quick_start.md",
    "ai_docs/Docs_AI/08_user_prompt_hook.md": "ai_docs/Docs_AI/08_user_prompt_hook.md",
    "ai_docs/Docs_AI/09_uv_scripts.md": "ai_docs/Docs_AI/09_uv_scripts.md",
    # Workflows_Python renaming (XX_)
    # Mapeo de nombres old snake_case → PascalCase actual
    "01_ritual_cierre.py": "01_Ritual_Cierre.py",
    "02_backlog_triage.py": "09_Backlog_Triage.py",
    "03_ai_task_planner.py": "03_AI_Task_Planner.py",
    "04_sync_notes.py": "11_Sync_Notes.py",
    "05_update_links.py": "12_Update_Links.py",
    "06_validate_stack.py": "13_Validate_Stack.py",
    "07_morning_standup.py": "07_Morning_Standup.py",
    "08_weekly_review.py": "08_Weekly_Review.py",
    "09_clean_system.py": "16_Clean_System.py",
    "10_ritual_dominical.py": "17_Ritual_Dominical.py",
    "11_generacion_contenido.py": "18_Generacion_Contenido.py",
    # AIPM scripts
    "15_aipm_trace_logger.py": "22_AIPM_Trace_Logger.py",
    "16_aipm_evaluator.py": "23_AIPM_Evaluator.py",
    "17_aipm_interview_sim.py": "24_AIPM_Interview_Sim.py",
    "18_token_budget_guard.py": "25_Token_Budget_Guard.py",
    "19_rag_optimizer_pro.py": "26_RAG_Optimizer_Pro.py",
    "20_probabilistic_risk_audit.py": "27_Probabilistic_Risk_Audit.py",
    "21_aipm_control_center.py": "28_AIPM_Control_Center.py",
    "23_guardrails_service.py": "29_Guardrails_Service.py",
    "24_aipm_consolidated_report.py": "30_AIPM_Consolidated_Report.py",
}


def update_links():
    """
    Iterates through the project files and replaces legacy paths with updated ones.
    """
    print_banner()
    dynamic_speak("Sincronizando enlaces internos")

    print(f"{Fore.CYAN}Starting safe link update in {ROOT_DIR}{Style.RESET_ALL}")
    count = 0
    # Search for common text-based files
    for root, dirs, files in os.walk(ROOT_DIR):
        # Skip internal or archived directories
        if any(x in root for x in (".git", ".venv", "__pycache__", "10_Archive")):
            continue

        for file in files:
            if not file.endswith((".md", ".py", ".sh", ".json")):
                continue

            p = os.path.join(root, file)

        try:
            with open(p, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()

            new_content = content
            for old, new in RENAMES.items():
                new_content = new_content.replace(old, new)

            if new_content != content:
                with open(p, "w", encoding="utf-8") as f:
                    f.write(new_content)
                print(f"Updated: {os.path.relpath(p, ROOT_DIR)}")
                count += 1
        except (OSError, IOError) as e:
            print(f"Error processing {p}: {e}")

    print(f"Finished. {count} files updated.")


def validate_workflows():
    """Valida que los workflows principales existan."""
    print("\n--- [VALIDATE] Workflows principales ---")

    workflows_dir = os.path.join(ROOT_DIR, ".agent", "03_Workflows")

    if not os.path.exists(workflows_dir):
        print(f"[WARNING] Directorio Workflows no encontrado: {workflows_dir}")
        return False

    # Verificar workflows principales
    key_workflows = ["README.md", "00_Backlog_Processing.md", "00_Morning_Standup.md"]
    missing = []

    for wf in key_workflows:
        if not os.path.exists(os.path.join(workflows_dir, wf)):
            missing.append(wf)

    if missing:
        print(f"[WARNING] Workflows faltantes: {', '.join(missing)}")
        return False

    print("[OK] Workflows principales validados.")
    return True


if __name__ == "__main__":
    update_links()
    validate_workflows()
