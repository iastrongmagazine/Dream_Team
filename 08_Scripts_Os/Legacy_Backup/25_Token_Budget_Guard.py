import os
import sys
import subprocess
import io
from typing import Tuple
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
    #      ____  _    _ _____   _____ ______ _______                          #
    #     |  _ \| |  | |  __ \ / ____|  ____|__   __|                         #
    #     | |_) | |  | | |  | | |  __| |__     | |                            #
    #     |  _ <| |  | | |  | | | |_ |  __|    | |                            #
    #     | |_) | |__| | |__| | |__| | |____   | |                            #
    #     |____/ \____/|_____/ \_____|______|  |_|                            #
    #                                                                         #
    #                        B U D G E T   G U A R D                          #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)

class TokenBudgetGuard:
    """
    Sistema de control de presupuesto de tokens para agentes AIPM.
    Previene el sobrecosto y la saturación de contexto mediante límites dinámicos.
    """
    def __init__(self, budget_limit: int = 150000) -> None:
        self.budget_limit = budget_limit
        self.current_usage = 0

    def check_budget(self, projected_tokens: int) -> Tuple[str, str]:
        """
        Verifica si el uso proyectado excede el presupuesto definido.
        """
        try:
            total_projected = self.current_usage + projected_tokens

            if total_projected > self.budget_limit:
                return "BLOCKED", f"[BUDGET_EXCEEDED] Presupuesto excedido: {total_projected} > {self.budget_limit}."

            if total_projected > (self.budget_limit * 0.8):
                return "WARNING", f"[BUDGET_WARNING] Uso cercano al límite ({total_projected}/{self.budget_limit})."

            return "OK", "Presupuesto dentro de límites saludables."
        except Exception as e:
            print(f"[ERROR] Error en validación de presupuesto: {e}")
            return "ERROR", str(e)

    def report_status(self) -> None:
        """
        Genera un reporte visual del estado actual del presupuesto.
        """
        try:
            print(f"\n{Fore.CYAN}[AIPM] TokenBudgetGuard Status:{Style.RESET_ALL}")
            print(f"      Límite: {self.budget_limit}")
            print(f"      Uso Actual: {self.current_usage}")
            print(f"      Disponible: {self.budget_limit - self.current_usage}")

            if self.current_usage > (self.budget_limit * 0.8):
                print(f"{Fore.RED}      [!] CRITICAL: ALTO CONSUMO DE TOKENS.{Style.RESET_ALL}")
                dynamic_speak("Advertencia crítica. El consumo de tokens está cerca del límite.")
        except Exception as e:
            print(f"{Fore.RED}[ERROR] Error al reportar estado: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    print_banner()
    dynamic_speak("Verificando presupuesto de tokens")

    guard = TokenBudgetGuard(budget_limit=100000)
    # Simulación
    status, msg = guard.check_budget(projected_tokens=85000)
    print(f"{Fore.YELLOW}Status: {status} | {msg}{Style.RESET_ALL}")

    status, msg = guard.check_budget(projected_tokens=20000)
    print(f"{Fore.RED}Status: {status} | {msg}{Style.RESET_ALL}")

    guard.report_status()
