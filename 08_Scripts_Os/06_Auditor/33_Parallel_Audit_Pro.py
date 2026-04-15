import sys
import os
import time
import subprocess
from pathlib import Path

# === PROTOCOLO DE RUTA DINÁMICA (v6.1) ===
_current = Path(__file__).resolve()
_root = next((p for p in _current.parents if (p / "01_Core").exists()), None)
if _root:
    sys.path.insert(0, str(_root / "08_Scripts_Os"))
from config_paths import *

# Intentar importar colorama, si no, fallback a strings vacíos
try:
    from colorama import Fore, Style, init

    init(autoreset=True)
except ImportError:

    class MockColor:
        def __getattr__(self, name):
            return ""

    Fore = Style = MockColor()

# Fix Windows console encoding
if sys.platform == "win32":
    import io

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
{Fore.RED}    ###########################################################################
    #                                                                         #
    #      _____   _    _____         _      _      ______ _                    #
    #     |  __ \ / \  |  __ \       | |    | |    |  ____| |                   #
    #     | |__) / _ \ | |__) | __ _ | |    | |    | |__  | |                   #
    #     |  ___/ ___ \|  _  / / _` || |    | |    |  __| | |                   #
    #     | |  / /   \ \ | \ \| (_| || |____| |____| |____| |____               #
    #     |_| /_/     \_\_| \_\\__,_||______|______|______|______|              #
    #                                                                         #
    #                        P A R A L L E L   A U D I T                      #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


# ROOT_DIR ya viene de config_paths
# Official Skill Tool Path
FORK_TOOL = (
    SKILLS_DIR / "08_Personal_Os" / "01_Fork_Terminal" / "tools" / "fork_terminal.py"
)


def launch_agent(id, name, task_cmd):
    """Lanza un sub-agente usando fork_terminal.py oficial"""
    # El fork_terminal.py oficial toma el comando como args y los une
    # No soporta titulo nativamente en los args, pero podemos usar echo para mostrarlo

    full_cmd = f"echo ==================================== && echo  🕵️ AGENT {id}: {name.upper()} && echo ==================================== && {task_cmd} && echo. && echo ✅ AGENT {id} COMPLETE && pause"

    print(f"🚀 Deploying Agent {id}: {name}")

    # We call the tool with python
    # We must quote the entire command string for the tool argument
    cmd_str = f'python "{FORK_TOOL}" "{full_cmd}"'
    os.system(cmd_str)

    time.sleep(1.5)  # Stagger launch to avoid chaos


def main():
    print_banner()
    dynamic_speak("Activando diez sub agentes en paralelo para auditoría profunda")

    print(f"{Fore.RED}{'=' * 75}{Style.RESET_ALL}")
    print("🚀 ACTIVATING 10 PARALLEL SUB-AGENTS (LFG PRO)")
    print(f"{Fore.RED}{'=' * 75}{Style.RESET_ALL}")

    if not os.path.exists(FORK_TOOL):
        print(f"❌ Error: Fork Tool not found at {FORK_TOOL}")
        return

    # 1. Agente Estructural
    launch_agent(
        1,
        "Stack Integrity",
        f"python {ENGINE_DIR}/01_Ritual/13_Validate_Stack.py",
    )

    # 2. Agente de Reglas
    launch_agent(
        2,
        "Rules Auditor",
        f"python {ENGINE_DIR}/03_Validator/40_Validate_Rules.py",
    )

    # 3. Agente de Enlaces
    launch_agent(
        3,
        "Link Validator",
        f"python {ENGINE_DIR}/01_Ritual/12_Update_Links.py",
    )

    # 4. Agente Beautifier (README)
    launch_agent(
        4,
        "Beautifier README",
        f"python {ENGINE_DIR}/13_Beautify_Tables.py target=README.md",
    )

    # 5. Agente Beautifier (AGENTS)
    launch_agent(
        5,
        "Beautifier AGENTS",
        f"python {ENGINE_DIR}/13_Beautify_Tables.py target=01_Core/AGENTS.md",
    )

    # 6. Agente Beautifier (INVENTORY)
    launch_agent(
        6,
        "Beautifier INVENTORY",
        f"python {ENGINE_DIR}/13_Beautify_Tables.py target=01_Core/01_Inventario_Total.md",
    )

    # 7. Agente Beautifier (CLAUDE)
    launch_agent(
        7,
        "Beautifier CLAUDE",
        f"python {ENGINE_DIR}/13_Beautify_Tables.py target=CLAUDE.md",
    )

    # 8. Agente de Inventario (Skills audit)
    # Simula auditoría de Skills
    launch_agent(
        8,
        "Skill Auditor",
        f'echo Auditing {SKILLS_DIR} vs Inventory... & dir /s "{SKILLS_DIR}"',
    )

    # 9. Agente de Seguridad
    launch_agent(
        9,
        "Security Scanner",
        'echo Scanning for secrets... & findstr /S /I "password secret key" *.py *.md',
    )

    # 10. Agente Reporteador Final (Wait a bit for others potentially, though parallel is fine)
    launch_agent(
        10,
        "Final Reporter",
        f"python {ENGINE_DIR}/03_AIPM_Hub.py",
    )

    print("\n✅ All 10 Agents Deployed.")
    print("   Please review each visible terminal window.")


if __name__ == "__main__":
    main()
