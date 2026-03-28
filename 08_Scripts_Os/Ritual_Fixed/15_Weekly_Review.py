import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
import os
import sys
import subprocess
import io
from colorama import init, Fore, Style

# Initialize Colorama
init()

# =============================================================================
# ARMOR LAYER - PATH RESOLUTION (3-LEVEL)
# =============================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(os.path.dirname(SCRIPT_DIR))

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

def dynamic_speak(text):
    """Interfaz de Voz SOTA v2.2"""
    print(f"{Fore.MAGENTA}🔊 [VOICE]: {text}{Style.RESET_ALL}")
    if sys.platform == "win32":
        try:
            cmd = f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"'
            subprocess.Popen(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except:
            pass

def print_banner():
    banner = rf"""
{Fore.CYAN}    ###########################################################################
    #                                                                         #
    #      __          ________ ______ _  ___     __  _____  ________      __ #
    #     \ \        / /  ____|  ____| |/ / |   \ \  / / __ \|  ____\ \    / / #
    #      \ \  /\  / /| |__  | |__  | ' /| |    \ \/ /| |  | | |__   \ \  / /  #
    #       \ \/  \/ / |  __| |  __| |  < | |     \  / | |  | |  __|   \ \/ /   #
    #        \  /\  /  | |____| |____| . \| |____  | | | |__| | |____   \  /    #
    #         \/  \/   |______|______|_|\_\______| |_|  \____/|______|   \/     #
    #                                                                         #
    #                      W E E K L Y   R E V I E W                          #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)

ROOT_DIR = PROJECT_ROOT

def weekly_review():
    """Ejecuta la revisión semanal del sistema."""
    print("--- 📊 PersonalOS WEEKLY REVIEW v1.0 ---")
    print("\n[INFO] Cosechando logros de la semana...")

    print("\nSecciones del Ritual:")
    print("1. Revisar tareas completadas.")
    print("2. Evaluar progreso contra 00_Core/GOALS.md.")
    print("3. Identificar bloqueos.")
    print("4. Planificar la carga de la próxima semana.")

    print("\n[TIP] Di 'Haz mi revisión semanal' para un análisis profundo.")
    print("\n--- Mens sana in corpore sano. ---")

if __name__ == "__main__":
    weekly_review()
