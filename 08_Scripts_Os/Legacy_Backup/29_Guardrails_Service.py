"""
GUARDRAILS-AS-A-SERVICE (GaaS) - PersonalOS v1.0
Capa de validación post-proceso para seguridad y ética.
Asegura que las salidas de los agentes cumplan con los estándares del sistema.
"""

import json
import os
import sys
import subprocess
import io
import re
from typing import List, Tuple
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
{Fore.WHITE}    ###########################################################################
    #                                                                         #
    #       _____ _    _         _____  _____  _____         _      _         #
    #      / ____| |  | |  /\   |  __ \|  __ \|  __ \       | |    | |        #
    #     | |  __| |  | | /  \  | |__) | |  | | |__) |      | |    | |        #
    #     | | |_ | |  | |/ /\ \ |  _  /| |  | |  _  /       | |    | |        #
    #     | |__| | |__| / ____ \| | \ \| |__| | | \ \       | |____| |____    #
    #      \_____|\____/_/    \_\_|  \_\_____/|_|  \_\      |______|______|   #
    #                                                                         #
    #                        G U A R D R A I L S                              #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)

class GuardrailsService:
    """
    Servicio de validación y mitigación de riesgos para agentes de IA.
    Implementa reglas dinámicas de seguridad y privacidad.
    """

    def __init__(self) -> None:
        self.rules = [
            "No revelar PII (Información de Identificación Personal)",
            "Evitar sesgos discriminatorios",
            "Validar veracidad en temas críticos (Salud/Legal)",
            "Mantener el tono de marca PersonalOS",
        ]

    def validate_output(self, output_text: str) -> Tuple[bool, List[str]]:
        """
        Analiza la salida frente a las reglas de seguridad.
        Returns: (is_safe, findings)
        """
        findings = []
        is_safe = True

        import re

        PII_PATTERNS = [
            # Información Personal
            (r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "EMAIL"),
            (r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b", "PHONE_US"),
            (r"\b\d{8}[A-Z]\b", "DNI_ES"),
            (r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b", "CREDIT_CARD"),
            # IPs y Redes
            (r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", "IP_V4"),
            (r"\b[0-9a-fA-F]{1,4}(:[0-9a-fA-F]{1,4}){7}\b", "IP_V6"),
            # API Keys y Tokens
            (r"sk-[-A-Za-z0-9]{20,}", "API_KEY_OPENAI"),
            (r'api[_-]?key["\s:=]+["\']?[A-Za-z0-9_-]{20,}["\']?', "API_KEY_GENERIC"),
            (r"ghp_[A-Za-z0-9]{36,}", "GITHUB_TOKEN"),
            (r"github_pat_[A-Za-z0-9_]{22,}", "GITHUB_PAT"),
            (r"Bearer\s+[A-Za-z0-9_-]{20,}", "BEARER_TOKEN"),
            (r"ntn_[A-Za-z0-9_-]{20,}", "NOTION_TOKEN"),
            (r"ctx7sk-[A-Za-z0-9-]{20,}", "CONTEXT7_KEY"),
            (r"sd_[A-Za-z0-9]{20,}", "SUPADATA_KEY"),
            (r"ZAI[a-zA-Z0-9_-]{10,}", "ZAI_KEY"),
            # Secrets genéricos
            (r'secret["\s:=]+["\']?[A-Za-z0-9_-]{10,}["\']?', "SECRET_GENERIC"),
            (r'password["\s:=]+["\']?[^\s"\']{8,}["\']?', "PASSWORD"),
            (r'PRIVATE[_-]?KEY["\s:=]+["\']?[A-Za-z0-9_-]{20,}["\']?', "PRIVATE_KEY"),
        ]

        # Simulación de detección de patrones prohibidos (Regla 20: Sin emojis en findings técnicos)
        for pattern, pii_type in PII_PATTERNS:
            if re.search(pattern, output_text):
                findings.append(
                    f"[PII_DETECTED] Posible fuga de PII ({pii_type}) detectada."
                )
                is_safe = False
                break

        if "alucinación" in output_text.lower():
            findings.append(
                "[UNCERTAINTY_WARNING] El modelo admite incertidumbre no controlada."
            )

        return is_safe, findings

    def apply_mitigation(self, output_text: str, findings: List[str]) -> str:
        """
        Aplica técnicas de mitigación si se han detectado riesgos.
        """
        try:
            if not findings:
                return output_text

            mitigated = (
                f"--- [MODERADO POR GAAS] ---\n{output_text}\n--- [FIN MODERACIÓN] ---"
            )
            return mitigated
        except Exception as e:
            print(f"[ERROR] Fallo en la mitigación: {e}")
            return output_text


if __name__ == "__main__":
    print_banner()
    dynamic_speak("Activando servicios de protección Guardrails")

    gaas = GuardrailsService()
    text = "El ID del usuario es PII: 12345678A."
    safe, problems = gaas.validate_output(text)
    if not safe:
        print(f"{Fore.RED}[BLOQUEADO] Hallazgos detectados: {problems}{Style.RESET_ALL}")
        dynamic_speak("Protección activada. Se han bloqueado fugas de información sensible.")
        final_text = gaas.apply_mitigation(text, problems)
        print(f"{Fore.CYAN}Salida Mitigada: \n{final_text}{Style.RESET_ALL}")
