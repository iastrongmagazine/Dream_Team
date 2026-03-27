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
{Fore.YELLOW}    ###########################################################################
    #                                                                         #
    #       _____ ____  _   _ _______ ______ _   _ _______                    #
    #      / ____/ __ \| \ | |__   __|  ____| \ | |__   __|                   #
    #     | |   | |  | |  \| |  | |  | |__  |  \| |  | |                      #
    #     | |   | |  | | . ` |  | |  |  __| | . ` |  | |                      #
    #     | |___| |__| | |\  |  | |  | |____| |\  |  | |                      #
    #      \_____\____/|_| \_|  |_|  |______|_| \_|  |_|                      #
    #                                                                         #
    #                        C O N T E N T   E N G I N E                      #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)

ROOT_DIR = PROJECT_ROOT

def content_generation():
    """Genera ideas de contenido basadas en el contexto actual."""
    print_banner()
    dynamic_speak("Motor de inteligencia creativa activado")

    print(f"\n{Fore.YELLOW}{'=' * 75}{Style.RESET_ALL}")
    print("✍️  CONTENT ENGINE - DESBLOQUEANDO GENIALIDAD")
    print(f"{Fore.YELLOW}{'=' * 75}{Style.RESET_ALL}")

    print("\nOpciones de Redacción:")
    print("- Blog Post / Artículo")
    print("- Email de Outreach")
    print("- LinkedIn / Twitter Thread")

    print("\n[TIP] Di 'Necesito escribir un [tipo]' para activar la generación con alma.")
    print("\n--- Motor de contenido listo. ---")

if __name__ == "__main__":
    content_generation()
