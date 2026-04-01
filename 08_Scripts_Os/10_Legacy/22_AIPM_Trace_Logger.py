import sys
import os
import subprocess
import io
from pathlib import Path
from colorama import init, Fore, Style

init()

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import PROJECT_ROOT, SYSTEM_DIR

SCRIPT_DIR = Path(__file__).resolve().parent
AIPM_CORE = SYSTEM_DIR / "01_Core" / "AIPM"  # Ruta real del sistema (05_System/01_Core/AIPM)

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
{Fore.CYAN}    ###########################################################################
    #                                                                         #
    #      _______ _____            _____ ______   _                            #
    #     |__   __|  __ \     /\   / ____|  ____| | |                           #
    #        | |  | |__) |   /  \ | |    | |__    | |                           #
    #        | |  |  _  /   / /\ \| |    |  __|   | |                           #
    #        | |  | | \ \  / ____ \ |____| |____  | |____                       #
    #        |_|  |_|  \_\/_/    \_\_____|______| |______|                      #
    #                                                                         #
    #                        T R A C E   L O G G E R                          #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


if os.path.exists(AIPM_CORE) and AIPM_CORE not in sys.path:
    sys.path.insert(0, str(AIPM_CORE))

try:
    from AIPM.logger import AIPMTraceLogger
except ImportError:
    # Fallback local definition if module not found
    class AIPMTraceLogger:
        def log_event(self, area, event, metadata):
            print(
                f"{Fore.YELLOW}[TRACE] {area} | {event} | {metadata}{Style.RESET_ALL}"
            )


if __name__ == "__main__":
    print_banner()
    dynamic_speak("Iniciando trazabilidad de eventos AIPM")

    logger = AIPMTraceLogger()
    logger.log_event(
        "Genesis", "INITIALIZATION", {"status": "SUCCESS", "version": "4.1"}
    )
    print(f"{Fore.GREEN}✅ Evento de inicialización registrado.{Style.RESET_ALL}")
