"""
Prueba de Estrés: 5 Agentes Simultáneos
Lanza 5 instancias de navegador abriendo google.com al mismo tiempo para verificar la capacidad de paralelización real.
"""

import subprocess
import time
import sys
from pathlib import Path

# Force UTF-8 for Windows console
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass

def load_stress_test():
    print("\n" + "=" * 60)
    print("🔥 PRUEBA DE ESTRÉS: 5 AGENTES SIMULTÁNEOS")
    print("=" * 60)
    print("Objetivo: Abrir 5 ventanas de navegador en paralelo (google.com)")

    fork_script = Path(".claude/skills/fork-terminal/tools/fork_terminal.py")

    # El comando que ejecutará cada "agente"
    # start https://google.com es el comando nativo de Windows para abrir URL en navegador default
    target_command = "start https://google.com"

    agents = []

    print("\n🚀 Lanzando agentes...")

    for i in range(1, 6):
        print(f"  ➤ Iniciando Agente #{i}...")

        # Construimos el comando completo para fork_terminal.py
        # Le pasamos el comando 'start https://google.com'
        full_command = f'python "{fork_script}" "{target_command}"'

        # Usamos Popen para lanzarlos sin esperar (non-blocking) y lograr simultaneidad real
        process = subprocess.Popen(full_command, shell=True)
        agents.append(process)

        # Pequeña pausa para no saturar instantáneamente el kernel
        time.sleep(0.5)

    print("\n✅ Todos los agentes han sido despachados.")
    print(f"📊 Instancias activas: {len(agents)}")
    print("\nDeberías ver 5 nuevas pestañas/ventanas de navegador abriéndose ahora mismo.")

    print("\nEsperando 5 s para finalizar script principal...")
    time.sleep(5)
    print("👋 Prueba finalizada.")

if __name__ == "__main__":
    load_stress_test()
