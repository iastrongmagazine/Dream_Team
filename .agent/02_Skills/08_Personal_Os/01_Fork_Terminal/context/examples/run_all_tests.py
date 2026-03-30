"""
All-in-One Test Suite
Ejecuta todas las demos del Fork Terminal Skill en secuencia.
"""

import subprocess
import time
import sys
from pathlib import Path

# Force UTF-8 for Windows console
try:
    sys.stdout.reconfigure(encoding='utf-8')
except AttributeError:
    pass # Python < 3.7 or not proper stdout


def print_header(title):
    """Imprime un header formateado."""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def run_demo(demo_name, script_path, description):
    """Ejecuta una demo individual."""
    print(f"\n🎯 {demo_name}")
    print(f"   {description}")
    print("-" * 70)

    fork_script = Path("01_Core/03_Skills/fork-terminal/tools/fork_terminal.py")
    command = f'python "{fork_script}" "python {script_path}"'

    print(f"\n📋 Comando: {command}")
    print("\n⏳ Ejecutando...")

    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ Demo ejecutada exitosamente")
            if result.stdout:
                print(f"   Output: {result.stdout.strip()}")
        else:
            print(f"❌ Error al ejecutar demo")
            if result.stderr:
                print(f"   Error: {result.stderr.strip()}")

        return result.returncode == 0

    except Exception as e:
        print(f"❌ Excepción: {str(e)}")
        return False

def main():
    print_header("🧪 FORK TERMINAL SKILL - TEST SUITE COMPLETO")

    print("\n📌 Este script ejecutará todas las demos en secuencia.")
    print("   Cada demo se abrirá en una nueva ventana de terminal.")
    print("   Cierra cada ventana para continuar con la siguiente.")

    # input("\n⏸️  Presiona ENTER para comenzar...")
    print("\n🚀 Iniciando demos automáticamente...")

    demos = [
        {
            'name': 'Demo 1: Agente Simple',
            'script': '01_Core/03_Skills/fork-terminal/context/05_Examples/demo_agent.py',
            'description': 'Simula un agente básico trabajando en una tarea'
        },
        {
            'name': 'Demo 2: Orquestación Avanzada',
            'script': '01_Core/03_Skills/fork-terminal/context/05_Examples/orchestration_demo.py',
            'description': 'Demuestra orquestación con contexto aislado'
        },
        {
            'name': 'Demo 3: Simulación Claude Code',
            'script': '01_Core/03_Skills/fork-terminal/context/05_Examples/claude_fork_demo.py',
            'description': 'Simula un agente Claude Code real siendo forked'
        }
    ]

    results = []

    for i, demo in enumerate(demos, 1):
        print_header(f"DEMO {i}/{len(demos)}")

        success = run_demo(
            demo['name'],
            demo['script'],
            demo['description']
        )

        results.append({
            'name': demo['name'],
            'success': success
        })

        if i < len(demos):
            print("\n⏳ Esperando 2 segundos antes de la siguiente demo...")
            time.sleep(2)

    # Resumen final
    print_header("📊 RESUMEN DE RESULTADOS")

    print("\n")
    for i, result in enumerate(results, 1):
        status = "✅ PASÓ" if result['success'] else "❌ FALLÓ"
        print(f"  {i}. {result['name']}: {status}")

    total = len(results)
    passed = sum(1 for r in results if r['success'])

    print("\n" + "-" * 70)
    print(f"\n  Total de demos: {total}")
    print(f"  Exitosas: {passed}")
    print(f"  Fallidas: {total - passed}")
    print(f"  Tasa de éxito: {(passed/total)*100:.1f}%")

    print("\n" + "=" * 70)

    if passed == total:
        print("  🎉 ¡TODAS LAS DEMOS PASARON EXITOSAMENTE!")
        print("  🟢 El Fork Terminal Skill está completamente funcional")
    else:
        print("  ⚠️  Algunas demos fallaron. Revisa los errores arriba.")

    print("=" * 70)

    # input("\n\nPresiona ENTER para finalizar...")
    print("\n👋 Pruebas finalizadas.")

if __name__ == "__main__":
    main()
