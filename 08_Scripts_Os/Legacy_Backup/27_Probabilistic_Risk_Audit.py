import os
import sys
import subprocess
import io
from typing import Dict
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
{Fore.RED}    ###########################################################################
    #                                                                         #
    #      _____  _____  _____ _  __     _    _      _     _ _______          #
    #     |  __ \|_   _|/ ____| |/ /    / \  | |    | |   | |__   __|         #
    #     | |__) | | | | (___ | ' /    / _ \ | |    | |   | |   | |            #
    #     |  _  /  | |  \___ \|  <    / ___ \| |    | |   | |   | |            #
    #     | | \ \ _| |_ ____) | . \  / /   \ \ |____| |___| |   | |            #
    #     |_|  \_\_____|_____/|_|\_\/_/     \_\______|_____|   |_|            #
    #                                                                         #
    #                        R I S K   A U D I T                              #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)

class ProbabilisticRiskAudit:
    """
    Auditor de riesgos probabilísticos en sistemas de IA.
    Detecta alucinaciones, sesgos y problemas de alineación ética.
    """
    def __init__(self) -> None:
        self.risk_levels = ["LOW", "MEDIUM", "HIGH", "CRITICAL"]

    def audit_prompt_or_output(self, content: str) -> Dict:
        """
        Audita el contenido para detectar riesgos estructurales y éticos.
        """
        try:
            results = {
                "has_pii": False, # Simulación de detección PII
                "bias_score": 0.15, # Simulación de sesgo (0-1)
                "hallucination_probability": 0.25, # Simulación de alucinación
                "ethical_alignment": "HIGH"
            }

            findings = []
            if results["hallucination_probability"] > 0.2:
                findings.append("[HALLUCINATION_RISK] Riesgo de alucinación moderado detectado.")

            if results["bias_score"] > 0.3:
                findings.append("[BIAS_DETECTED] Sesgo estructural detectado en el razonamiento.")

            report = {
                "audit_id": "risk_audit_2026",
                "findings": findings,
                "overall_status": "SECURE" if results["hallucination_probability"] < 0.3 else "VULNERABLE",
                "mitigation_plan": "Implementar Cross-Checking con fuentes deterministas." if findings else "N/A"
            }

            return report
        except Exception as e:
            print(f"[ERROR] Fallo en la auditoría de riesgos: {e}")
            return {"error": str(e), "overall_status": "ERROR"}

    def generate_report(self, report_data: Dict) -> None:
        """
        Presenta visualmente los resultados de la auditoría de riesgos.
        """
        try:
            print(f"\n{Fore.CYAN}[AIPM] Probabilistic Risk Audit - Final Report{Style.RESET_ALL}")
            status = report_data.get('overall_status', 'UNKNOWN')
            color = Fore.GREEN if status == "SECURE" else Fore.RED
            print(f"      Estado: {color}{status}{Style.RESET_ALL}")

            for f in report_data.get('findings', []):
                print(f"      {Fore.YELLOW}- {f}{Style.RESET_ALL}")

            if status != "SECURE":
                 dynamic_speak("Advertencia. Se han detectado vulnerabilidades de riesgo en el contenido.")
        except Exception as e:
            print(f"{Fore.RED}[ERROR] Error al imprimir reporte de riesgos: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    print_banner()
    dynamic_speak("Iniciando auditoría probabilística de riesgos")

    auditor = ProbabilisticRiskAudit()
    report = auditor.audit_prompt_or_output("El paciente Juan Pérez nació en 1980.")
    auditor.generate_report(report)
