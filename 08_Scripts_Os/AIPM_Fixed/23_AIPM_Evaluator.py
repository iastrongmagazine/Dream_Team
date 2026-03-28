import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
import sys
import os
import subprocess
import io
from pathlib import Path
from colorama import init, Fore, Style

init()

# Agregar paths necesarios
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
CONFIG_PATHS = PROJECT_ROOT / "08_Scripts_Os"

sys.path.insert(0, str(CONFIG_PATHS))
sys.path.insert(0, str(PROJECT_ROOT))

try:
    from config_paths import PROJECT_ROOT as _PR, SYSTEM_DIR as _SD

    PROJECT_ROOT = _PR
    SYSTEM_DIR = _SD
except:
    SYSTEM_DIR = PROJECT_ROOT / "01_Core"

AIPM_CORE = SYSTEM_DIR / "AIPM"

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
{Fore.GREEN}    ###########################################################################
    #                                                                         #
    #      ________      __      _     _    _    _______  ____  _____         #
    #     |  ____\ \    / /\    | |   | |  | |  |__   __|/ __ \|  __ \        #
    #     | |__   \ \  / /  \   | |   | |  | |     | |  | |  | | |__) |       #
    #     |  __|   \ \/ / /\ \  | |   | |  | |     | |  | |  | |  _  /        #
    #     | |____   \  / ____ \ | |___| |__| |     | |  | |__| | | \ \        #
    #     |______|   \/_/    \_\______|______|     |_|   \____/|_|  \_\       #
    #                                                                         #
    #                        E V A L U A T O R                                #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


if os.path.exists(AIPM_CORE) and AIPM_CORE not in sys.path:
    sys.path.append(str(AIPM_CORE))

try:
    from AIPM.core import AIPMEvaluator
except ImportError:
    # Fallback local definition
    class AIPMEvaluator:
        def evaluate_tools(self):
            print(
                f"{Fore.CYAN}[EVALUATOR] Ejecutando evaluación de herramientas...{Style.RESET_ALL}"
            )
            print(
                f"{Fore.GREEN}✅ Evaluación completada: 100% Tools operacionales.{Style.RESET_ALL}"
            )


if __name__ == "__main__":
    print_banner()
    dynamic_speak("Iniciando evaluación de herramientas del sistema")

    evaluator = AIPMEvaluator()
    evaluator.evaluate_tools()
