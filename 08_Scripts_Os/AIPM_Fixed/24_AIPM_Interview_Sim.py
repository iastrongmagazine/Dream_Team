import os
import random
import json
import importlib.util
import sys
import io
import subprocess
from pathlib import Path
from typing import Dict, Any, Optional
from colorama import init, Fore, Style

init()

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import PROJECT_ROOT, SYSTEM_DIR

SCRIPT_DIR = Path(__file__).resolve().parent
AIPM_CORE = SYSTEM_DIR / "01_Core"

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
{Fore.YELLOW}    ###########################################################################
    #                                                                         #
    #      _____ _   _ _______ ______ _____ _      _      _                   #
    #     |_   _| \ | |__   __|  ____|  __ \ \    / \    / \                  #
    #       | | |  \| |  | |  | |__  | |__) \ \  / _ \  / _ \                 #
    #       | | | . ` |  | |  |  __| |  _  / \ \/ / \ \/ / \ \                #
    #      _| |_| |\  |  | |  | |____| | \ \  \  /   \  /   \ \               #
    #     |_____|_| \_|  |_|  |______|_|  \_\  \/     \/     \_\              #
    #                                                                         #
    #                        I N T E R V I E W                                #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


if os.path.exists(AIPM_CORE) and AIPM_CORE not in sys.path:
    sys.path.insert(0, str(AIPM_CORE))

from AIPM.logger import AIPMTraceLogger
from AIPM.core import AIPMEvaluator


class AIPMInterviewSim:
    """
    Simulador de entrevistas técnicas AIPM Senior.
    Utiliza un pool de preguntas extraídas de benchmarks reales de 2026.
    """

    def __init__(self) -> None:
        self.logger = AIPMTraceLogger()
        self.evaluator = AIPMEvaluator()
        self.questions = [
            {
                "id": "Q1",
                "topic": "Escalabilidad",
                "question": "¿Cómo evaluarías, reducirías riesgos, desplegarías y escalarías un sistema de IA probabilístico?",
            },
            {
                "id": "Q2",
                "topic": "Incertidumbre",
                "question": "¿Cómo gestionas el razonamiento bajo incertidumbre cuando los resultados del modelo no son deterministas?",
            },
            {
                "id": "Q3",
                "topic": "Dependencias",
                "question": "Explica cómo gestionarías las dependencias críticas entre la calidad de los datos y el rendimiento del modelo.",
            },
            {
                "id": "Q4",
                "topic": "Arquitectura de Conocimiento",
                "question": "¿Por qué es importante entender los LLMs como 'sistemas de conocimiento comprimido' al diseñar un producto?",
            },
            {
                "id": "Q5",
                "topic": "Economía de Tokens",
                "question": "¿Cómo afectan los tokens al balance entre coste, velocidad y rendimiento en una API de producción?",
            },
            {
                "id": "Q6",
                "topic": "Niveles de Prompting",
                "question": "Diferencia entre el nivel Conversacional (ChatGPT) y el nivel de Modelo (Playground/API) en la ingeniería de producto.",
            },
            {
                "id": "Q7",
                "topic": "Las 4 C's",
                "question": "Aplica las 4 C's (Claridad, Contexto, Restricciones, Ejemplos) para optimizar un prompt de clasificación legal.",
            },
            {
                "id": "Q8",
                "topic": "Selección de Modelos",
                "question": "¿Bajo qué criterios elegirías un SLM (Small Model) frente a un LLM fundacional para una app móvil?",
            },
            {
                "id": "Q9",
                "topic": "RAG & Alucinaciones",
                "question": "Diseña una estrategia para mitigar alucinaciones en un sistema RAG que consulta bases de datos técnicas.",
            },
            {
                "id": "Q10",
                "topic": "Guardrails & Ética",
                "question": "¿Cómo implementarías barreras de seguridad (Guardrails) para evitar fugas de PII en una integración de IA?",
            },
            {
                "id": "Q11",
                "topic": "Stakeholders",
                "question": "¿Cómo explicarías a un cliente que el éxito de un producto de IA es probabilístico y no una garantía de código fijo?",
            },
            {
                "id": "Q12",
                "topic": "KPIs de IA",
                "question": "Define 3 métricas de éxito para un agente de soporte que priorice la precisión sobre la velocidad.",
            },
            {
                "id": "Q13",
                "topic": "Presupuesto",
                "question": "Si el costo de inferencia sube un 40%, ¿qué ajustes técnicos harías en el flujo de prompts para compensarlo?",
            },
            {
                "id": "Q14",
                "topic": "Lead Delivery",
                "question": "¿Cómo lideras un equipo técnico cuando los resultados de los experimentos de IA fallan en la fase de prototipo?",
            },
            {
                "id": "Q15",
                "topic": "Futuro AIPM",
                "question": "¿Cuál es la diferencia fundamental entre un PM tradicional y un AIPM de cara al año 2026?",
            },
        ]

    def start_interview(self) -> Dict[str, str]:
        """
        Inicia la sesión de entrevista y selecciona una pregunta aleatoria.
        """
        print_banner()
        dynamic_speak("Bienvenido al simulador de entrevistas élite A I P M")

        print("\n" + "=" * 50)
        print("🎯 BIENVENIDO AL SIMULADOR DE ENTREVISTAS AIPM 2026")
        print("=" * 50)

        # Seleccionar una pregunta al azar
        q = random.choice(self.questions)
        print(f"\n[TOPIC: {q['topic']}]")
        print(f"👉 PREGUNTA: {q['question']}")
        print("-" * 50)

        return q

    def evaluate_answer(
        self, question: Dict[str, str], answer: str, thought_process: str
    ) -> Optional[Dict[str, Any]]:
        """
        Evalúa la respuesta usando el motor AIPM y genera métricas de trazabilidad.
        """
        try:
            print("\n[AIPM] Analizando respuesta del candidato...")

            # Simulamos métricas de la interacción
            # Se asumen valores realistas para un Senior
            metadata = {
                "model": "AIPM_Judge_Engine",
                "latency_ms": 1500,
                "tokens": len(answer) // 4,
                "cot_tokens": len(thought_process) // 4,
                "response_tokens": len(answer) // 4,
                "context_before": 120000,
                "context_after": 121500,
                "mcp_tokens": 45000,  # Simulación de carga pesada de MCP
                "skill_tokens": 35000,  # Simulación de Skills activas
                "prompt_tokens": 15000,  # System Prompt + Instructions
                "history_tokens": 25000,  # Historial de chat
            }

            trace_path = self.logger.log_trace(
                agent_id="AIPM_Sim_Judge",
                input_text=question["question"],
                output_text=answer,
                thought_process=thought_process,
                metadata=metadata,
            )

            if not trace_path:
                print("[ERROR] No se pudo generar la traza de evaluación.")
                return None

            report = self.evaluator.evaluate_trace(trace_path)

            if not report:
                print("[ERROR] El evaluador no devolvió un reporte válido.")
                return None

            print("\n" + "*" * 50)
            print(
                f"🏆 SCORE FINAL: {Fore.GREEN}{report['quality_score']}/10{Style.RESET_ALL}"
            )
            print(
                f"📢 FEEDBACK: {Fore.CYAN}{report['judge_feedback']}{Style.RESET_ALL}"
            )
            print("*" * 50)

            if report.get("actionable_recommendations"):
                print(
                    f"\n{Fore.YELLOW}💡 RECOMENDACIONES PARA EL PRÓXIMO NIVEL:{Style.RESET_ALL}"
                )
                for rec in report["actionable_recommendations"]:
                    print(
                        f"- {rec.get('concept', 'General')}: {rec.get('explanation') or rec.get('issue')}"
                    )

            if report["quality_score"] >= 8:
                dynamic_speak(
                    "Felicidades. Has demostrado un nivel senior excepcional."
                )
            else:
                dynamic_speak(
                    "Sigue practicando. El camino a la maestría requiere iteración constante."
                )

            return report
        except Exception as e:
            print(f"[ERROR] Fallo en la simulación de entrevista: {e}")
            return None


if __name__ == "__main__":
    sim = AIPMInterviewSim()
    # Simulación de un flujo completo para validar el motor
    q = sim.start_interview()

    # Simulación de respuesta Senior
    sim_answer = "Para escalar un sistema probabilístico, implementaría una arquitectura de Guardrails dual (input/output) y usaría un SLM ajustado para micro-tareas, reduciendo latencia y coste."
    sim_thought = "Analizando la pregunta de escalabilidad. Priorizando balance de latencia vs precisión. Inyectando concepto de SLM y Guardrails."

    sim.evaluate_answer(q, sim_answer, sim_thought)
