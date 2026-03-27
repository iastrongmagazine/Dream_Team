"""
Demo Agent Script
Simula un agente secundario trabajando en una tarea delegada.
"""

import time
import sys
from datetime import datetime

def simulate_agent_work(task_name):
    """Simula el trabajo de un agente en una tarea específica."""

    print("=" * 60)
    print("🤖 AGENTE SECUNDARIO INICIADO")
    print("=" * 60)
    print(f"\n📋 Tarea asignada: {task_name}")
    print(f"⏰ Hora de inicio: {datetime.now().strftime('%H:%M:%S')}")
    print(f"🔧 Python version: {sys.version.split()[0]}")
    print("\n" + "-" * 60)

    # Simular pasos de trabajo
    steps = [
        "Analizando contexto del proyecto...",
        "Leyendo archivos relevantes...",
        "Procesando información...",
        "Generando análisis...",
        "Preparando reporte..."
    ]

    for i, step in enumerate(steps, 1):
        print(f"\n[Paso {i}/{len(steps)}] {step}")
        time.sleep(0.5)  # Simular trabajo
        print("  ✓ Completado")

    print("\n" + "-" * 60)
    print("\n✅ TAREA COMPLETADA EXITOSAMENTE")
    print("\n📊 Resultados:")
    print("  • Archivos analizados: 12")
    print("  • Líneas procesadas: 1,847")
    print("  • Tiempo total: 2.5s")
    print("\n" + "=" * 60)
    print("🎯 Agente secundario finalizó su trabajo")
    print("=" * 60)

    input("\n\nPresiona ENTER para cerrar esta ventana...")

if __name__ == "__main__":
    task = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "Análisis de código"
    simulate_agent_work(task)
