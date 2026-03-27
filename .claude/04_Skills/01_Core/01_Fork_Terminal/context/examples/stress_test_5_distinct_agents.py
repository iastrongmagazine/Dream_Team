"""
Prueba de Estrés Mejorada: 5 Agentes Claude Diferenciados
Lanza 5 terminales que simulan ser agentes Claude, cada uno con una misión distinta.
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

def load_distinct_stress_test():
    print("\n" + "=" * 60)
    print("🤖 PRUEBA DE ORQUESTACIÓN: 5 SUB-AGENTES CLAUDE")
    print("=" * 60)

    fork_script = Path(".claude/skills/fork-terminal/tools/fork_terminal.py")

    # Definimos 5 misiones diferentes
    missions = [
        {"name": "Agent-Search", "url": "https://google.com", "task": "Buscando datos..."},
        {"name": "Agent-Docs", "url": "https://wikipedia.org", "task": "Leyendo documentación..."},
        {"name": "Agent-Code", "url": "https://github.com", "task": "Clonando repositorio..."},
        {"name": "Agent-Math", "url": "https://wolframalpha.com", "task": "Calculando funciones..."},
        {"name": "Agent-News", "url": "https://news.ycombinator.com", "task": "Analizando tendencias..."}
    ]

    agents = []

    print("\n🚀 Desplegando enjambre de agentes...")

    for i, mission in enumerate(missions, 1):
        print(f"  ➤ Lanzando {mission['name']} -> {mission['task']}")

        # Construimos un comando compuesto para Windows (cmd.exe)
        # 1. Simula el inicio de Claude
        # 2. Espera 2 segundos
        # 3. Abre la URL específica
        # 4. Pausa para que veas la terminal

        # Nota: Usamos 'timeout 2' para esperar y 'start' para abrir URL
        cmd_content = (
            f"echo [CLAUDE SUB-AGENT #{i}] Iniciando... && "
            f"echo Tarea: {mission['task']} && "
            f"ping 127.0.0.1 -n 4 > nul && "
            f"echo Abriendo {mission['url']}... && "
            f"start {mission['url']} && "
            f"echo Mision cumplida. && "
            f"pause"
        )

        full_command = f'python "{fork_script}" "{cmd_content}"'

        process = subprocess.Popen(full_command, shell=True)
        agents.append(process)

        time.sleep(1) # Un segundo entre lanzamientos para ver la cascada

    print("\n✅ Todos los agentes están operando.")
    print(f"📊 Instancias activas: {len(agents)}")
    print("\nObserva cómo se abren 5 terminales y luego 5 sitios web diferentes.")

if __name__ == "__main__":
    load_distinct_stress_test()
