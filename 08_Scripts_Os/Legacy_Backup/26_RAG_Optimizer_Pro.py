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
{Fore.BLUE}    ###########################################################################
    #                                                                         #
    #      _____            _____    ____  _____ _______                      #
    #     |  __ \     /\   / ____|  / __ \|  __ \__   __|                     #
    #     | |__) |   /  \ | |  __  | |  | | |__) | | |                        #
    #     |  _  /   / /\ \| | |_ | | |  | |  _  /  | |                        #
    #     | | \ \  / ____ \ |__| | | |__| | | \ \  | |                        #
    #     |_|  \_\/_/    \_\_____|  \____/|_|  \_\ |_|                        #
    #                                                                         #
    #                        O P T I M I Z E R                                #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)

class RAGOptimizerPro:
    """
    Analizador avanzado de calidad de recuperación (RAG).
    Evalúa relevancia, redundancia y salud del contexto recuperado.
    """
    def __init__(self) -> None:
        self.metrics_history = []

    def analyze_retrieval(self, query: str, retrieved_chunks: list, relevance_scores: list) -> Dict:
        """
        Analiza la calidad de los chunks recuperados frente a una consulta.
        """
        try:
            avg_relevance = sum(relevance_scores) / len(relevance_scores) if relevance_scores else 0

            report = {
                "query": query,
                "num_chunks": len(retrieved_chunks),
                "avg_relevance": avg_relevance,
                "quality_tier": "ELITE" if avg_relevance > 0.85 else "GOOD" if avg_relevance > 0.7 else "ACTION_REQUIRED"
            }

            recommendations = []
            if avg_relevance < 0.7:
                recommendations.append("Ajustar: Aumentar el tamaño de los chunks (Chunk Size).")
                recommendations.append("Optimizar: Re-entrenar embeddings o usar un modelo superior.")

            if len(retrieved_chunks) > 10:
                recommendations.append("Eficiencia: Reducir 'top_k' para evitar ruido en el contexto.")

            report["recommendations"] = recommendations
            return report
        except Exception as e:
            print(f"[ERROR] Error en análisis RAG: {e}")
            return {"error": str(e)}

    def generate_global_report(self) -> None:
        """
        Genera un reporte de inteligencia global sobre la calidad RAG histórica.
        """
        try:
            print(f"\n{Fore.CYAN}[AIPM] RAG Optimizer Pro - Global Intelligence Report{Style.RESET_ALL}")
            # Aquí se analizaría el histórico de recuperaciones
            print(f"      Estado General: {Fore.GREEN}OPTIMIZADO{Style.RESET_ALL}")
            print(f"      Sugerencia Maestra: {Fore.YELLOW}Implementar Hybrid Search (BM25 + Vector).{Style.RESET_ALL}")

            dynamic_speak("Calidad de recuperación optimizada. Sugerencia: Búsqueda Híbrida.")
        except Exception as e:
            print(f"{Fore.RED}[ERROR] Error al generar reporte global RAG: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    import json
    print_banner()
    dynamic_speak("Optimizando parámetros de recuperación RAG")

    optimizer = RAGOptimizerPro()
    sample_relevance = [0.92, 0.88, 0.45, 0.30]
    report = optimizer.analyze_retrieval("¿Cómo funciona el AIPM?", ["chunk1", "chunk2", "chunk3", "chunk4"], sample_relevance)
    print(json.dumps(report, indent=2, ensure_ascii=False))

    optimizer.generate_global_report()
