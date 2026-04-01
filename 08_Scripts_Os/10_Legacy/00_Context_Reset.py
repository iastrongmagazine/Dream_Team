"""
CONTEXT RESET - PersonalOS v1.0
Automates "Rule 0" of the Circular Workflow.
Reads latest session note and rules registry to provide a context briefing.
"""

from config_paths import ROOT_DIR, BRAIN_NOTES_DIR, BRAIN_RULES_DIR, BRAIN_KNOWLEDGE_DIR
import os
import glob
import argparse

# Configuración de Colores
try:
    from colorama import init, Fore, Style

    init(autoreset=True)
    SUCCESS = Fore.GREEN
    INFO = Fore.CYAN
    WARNING = Fore.YELLOW
    RESET = Style.RESET_ALL
except ImportError:
    SUCCESS = INFO = WARNING = RESET = ""


# Rutas
Process_Notes_DIR = BRAIN_NOTES_DIR
RULES_REGISTRY = os.path.join(BRAIN_RULES_DIR, "Rules_Registry.md")
INVENTORY_TOTAL = os.path.join(BRAIN_KNOWLEDGE_DIR, "01_Inventario_Total.md")


def get_latest_note():
    """Retrieves the most recent process note from the archive."""
    if not os.path.exists(Process_Notes_DIR):
        return None
    notes = glob.glob(os.path.join(Process_Notes_DIR, "*.md"))
    notes.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return notes[0] if notes else None


def main():
    """Main execution flow for context recovery."""
    print(f"{INFO}--- [CONTEXT RESET: RECUPERACIÓN DE ESTADO] ---{RESET}")

    note = get_latest_note()
    if note:
        print(
            f"{SUCCESS}✔ Última nota de proceso encontrada: {os.path.basename(note)}{RESET}"
        )
        print(f"\n{INFO}--- RESUMEN DE ÚLTIMA SESIÓN ---{RESET}")
        with open(note, "r", encoding="utf-8") as f:
            print(f.read(500) + "...")
    else:
        print(
            f"{WARNING}⚠ No se encontraron notas de proceso en {Process_Notes_DIR}{RESET}"
        )

    # Nuevo: Soporte para Briefing de Tarea
    parser = argparse.ArgumentParser(description="Context Reset for PersonalOS")
    parser.add_argument(
        "--task", help="Ruta a una tarea específica para generar briefing"
    )
    args, _ = parser.parse_known_args()

    if args.task:
        task_path = os.path.abspath(args.task)
        if os.path.exists(task_path):
            print(
                f"\n{SUCCESS}🚀 GENERANDO BRIEFING DE IGNICIÓN PARA: {os.path.basename(task_path)}{RESET}"
            )
            with open(task_path, "r", encoding="utf-8") as f:
                content = f.read()
            # Extraer título y objetivo (simplificado)
            print(f"{INFO}Copie lo siguiente en un nuevo chat:{RESET}")
            print("-" * 30)
            print(f"Estoy trabajando en PersonalOS V1.0.")
            print(f"Tarea: {os.path.basename(task_path)}")
            print(f"Por favor, analiza el archivo de tarea y dame un plan de acción.")
            print("-" * 30)

    if os.path.exists(RULES_REGISTRY):
        print(f"\n{INFO}--- REGLAS ACTIVAS (Últimas 3) ---{RESET}")
        with open(RULES_REGISTRY, "r", encoding="utf-8") as f:
            lines = f.readlines()
        # Find the last few rules starting with ###
        rules = [l for l in lines if l.startswith("###")][-3:]
        for r in rules:
            print(f"{SUCCESS}• {r.strip('# ')}{RESET}")
    else:
        print(f"{WARNING}⚠ No se encontró el Rules Registry en {RULES_REGISTRY}{RESET}")

    if os.path.exists(INVENTORY_TOTAL):
        print(f"\n{INFO}--- [ARSENAL DISPONIBLE] ---{RESET}")
        print(
            f"{SUCCESS}✔ Inventario maestro detectado. Listo para máximo rendimiento.{RESET}"
        )
        print(f"{INFO}Ubicación: {os.path.relpath(INVENTORY_TOTAL, ROOT_DIR)}{RESET}")

    print(f"\n{SUCCESS}ESTADO: Contexto recuperado. Listo para operar.{RESET}")


if __name__ == "__main__":
    main()
