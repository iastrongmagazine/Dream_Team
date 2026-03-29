#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Progress Reporter - Sistema de reportería de avance
Muestra progreso, tiempo estimado, y notifica al completar cada tarea.

Uso:
    python 01_Progress_Reporter.py
"""

import os
import sys
import time
from pathlib import Path
from datetime import datetime, timedelta

# === SETUP PATHS ===
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# === SOUND SETUP ===
SOUND_SCRIPT = (
    PROJECT_ROOT
    / ".agent"
    / "04_Extensions"
    / "hooks"
    / "04_Sound"
    / "task-complete-sound.ps1"
)


def play_sound():
    """Reproduce sonido de notificación."""
    if SOUND_SCRIPT.exists():
        try:
            import subprocess

            subprocess.run(
                [
                    "powershell.exe",
                    "-ExecutionPolicy",
                    "Bypass",
                    "-File",
                    str(SOUND_SCRIPT),
                ],
                capture_output=True,
                timeout=3,
            )
        except:
            pass


def print_progress_bar(current: int, total: int, width: int = 30) -> str:
    """Genera barra de progreso."""
    filled = int(width * current / total) if total > 0 else 0
    bar = "=" * filled + "-" * (width - filled)
    pct = (current / total * 100) if total > 0 else 0
    return f"[{bar}] {pct:.0f}%"


def format_time(seconds: float) -> str:
    """Formatea tiempo en formato legible."""
    if seconds < 60:
        return f"{int(seconds)}s"
    elif seconds < 3600:
        mins = int(seconds / 60)
        return f"{mins}m"
    else:
        hours = int(seconds / 3600)
        mins = int((seconds % 3600) / 60)
        return f"{hours}h {mins}m"


class ProgressReporter:
    """Reportero de progreso con notificaciones."""

    def __init__(self, task_name: str, total_steps: int, description: str = ""):
        self.task_name = task_name
        self.total_steps = total_steps
        self.description = description
        self.current_step = 0
        self.start_time = time.time()
        self.step_times = []

        # Header inicial
        self.print_header()

    def print_header(self):
        """Imprime header del progreso."""
        print("\n" + "=" * 60)
        print(f"PROGRESO: {self.task_name}")
        if self.description:
            print(f"Descripcion: {self.description}")
        print("=" * 60)
        print(f"Tareas totales: {self.total_steps}")
        print(f"Inicio: {datetime.now().strftime('%H:%M:%S')}")
        print("-" * 60)

    def complete_step(self, step_name: str):
        """Marca un paso como completado."""
        self.current_step += 1
        step_time = time.time() - self.start_time - sum(self.step_times)
        self.step_times.append(step_time)

        # Calcular tiempo estimado
        avg_time = sum(self.step_times) / len(self.step_times)
        remaining_steps = self.total_steps - self.current_step
        eta_seconds = avg_time * remaining_steps

        # Progress bar
        bar = print_progress_bar(self.current_step, self.total_steps)

        # Print
        print(f"\n[COMPLETADO {self.current_step}/{self.total_steps}] {step_name}")
        print(f"  Progreso: {bar}")
        print(f"  Tiempo paso: {format_time(step_time)}")

        if remaining_steps > 0:
            eta = format_time(eta_seconds)
            print(f"  ETA restantes: ~{eta}")
        else:
            # Ultimo paso - reporte final
            total_time = time.time() - self.start_time
            print(f"\n  Tiempo total: {format_time(total_time)}")

        # Sonido al completar paso
        play_sound()

    def finish(self, pending_items: list = None):
        """Finaliza el reportero."""
        total_time = time.time() - self.start_time
        print("\n" + "=" * 60)
        print("TAREA COMPLETADA")
        print("=" * 60)
        print(f"Tarea: {self.task_name}")
        print(f"Pasos completados: {self.current_step}/{self.total_steps}")
        print(f"Tiempo total: {format_time(total_time)}")

        # Mostrar pendientes si hay
        if pending_items:
            print("\n" + "-" * 60)
            print("PENDIENTES:")
            for i, item in enumerate(pending_items, 1):
                print(f"  {i}. {item}")

        # Sonido final
        play_sound()
        play_sound()  # Doble beep para énfasis


def demo_usage():
    """Demo de cómo usar el reporter."""
    print("\n" + "=" * 60)
    print("PROGRESS REPORTER - DEMO")
    print("=" * 60)

    # Ejemplo de uso
    reporter = ProgressReporter(
        task_name="Integrar Notificaciones al Sistema",
        total_steps=5,
        description="Agregar sistema de sonidos y progreso",
    )

    steps = [
        "Crear modulo de sonido",
        "Integrar con scripts existentes",
        "Agregar al Skill Auditor",
        "Testing y verificacion",
        "Documentar uso",
    ]

    for step in steps:
        time.sleep(0.5)  # Simular trabajo
        reporter.complete_step(step)

    # Pendientes opcionales
    pendientes = ["Actualizar documentacion", "Verificar en otra sesion"]

    reporter.finish(pending_items=pendientes)


# === MAIN ===
if __name__ == "__main__":
    # Si hay argumentos, ejecutar modo simple
    if len(sys.argv) > 1:
        # Modo: python 01_Progress_Reporter.py "Tarea" paso total
        if len(sys.argv) >= 4:
            step_name = sys.argv[1]
            current = int(sys.argv[2])
            total = int(sys.argv[3])

            bar = print_progress_bar(current, total)
            print(f"\n[COMPLETADO {current}/{total}] {step_name}")
            print(f"  Progreso: {bar}")
            play_sound()
        else:
            print("Usage:")
            print("  python 01_Progress_Reporter.py")
            print("  python 01_Progress_Reporter.py 'Step Name' current total")
    else:
        demo_usage()
