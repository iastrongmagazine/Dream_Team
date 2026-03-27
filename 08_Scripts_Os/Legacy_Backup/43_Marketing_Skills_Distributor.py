"""
Script de Distribución de Marketing Skills - PersonalOS v1.0
Automatiza la categorización y despliegue de habilidades de marketing en el sistema.

Alineado con:
- Pilar 0: Comunicación en Español y Visibilidad.
- Pilar 1: Armor Layer y Vitaminización de Scripts.
"""

import os
import sys
import shutil
import io
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import PROJECT_ROOT

# --- CONFIGURACIÓN ARMOR LAYER ---
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

ROOT_DIR = PROJECT_ROOT
SCRIPT_DIR = Path(__file__).resolve().parent

# --- CONFIGURACIÓN DE RUTAS ---
# Nota: SRC_Skills se mantiene como la ruta de descarga original
SRC_Skills = (
    r"c:\Users\sebas\Downloads\marketingSkills-main\marketingSkills-main\Skills"
)
DEST_HIGH_VALUE = os.path.join(
    ROOT_DIR, ".agent", "02_Skills", "02_High_Value", "27_Marketing_Strategy"
)
DEST_UTILITIES = os.path.join(
    ROOT_DIR, ".agent", "02_Skills", "03_Utilities", "29_Marketing_Tech"
)

# --- CATEGORIZACIÓN ---
HIGH_VALUE_FOLDER_NAMES = [
    "copywriting",
    "content-strategy",
    "email-sequence",
    "marketing-ideas",
    "marketing-psychology",
    "pricing-strategy",
    "product-marketing-context",
    "launch-strategy",
    "copy-editing",
    "signup-flow-cro",
    "onboarding-cro",
    "page-cro",
    "form-cro",
    "popup-cro",
    "paywall-upgrade-cro",
]


def distribute_Skills():
    print("=" * 60)
    print("🚀 PersonalOS | MOTOR DE DISTRIBUCIÓN DE MARKETING Skills")
    print("=" * 60)

    if not os.path.exists(SRC_Skills):
        print(f"[ERR] Origen no encontrado: {SRC_Skills}")
        return False

    os.makedirs(DEST_HIGH_VALUE, exist_ok=True)
    os.makedirs(DEST_UTILITIES, exist_ok=True)

    Skills = [
        f for f in os.listdir(SRC_Skills) if os.path.isdir(os.path.join(SRC_Skills, f))
    ]
    total_Skills = len(Skills)

    print(f"[INFO] Detectadas {total_Skills} habilidades para clasificar.")

    for idx, folder in enumerate(Skills, 1):
        src_path = os.path.join(SRC_Skills, folder)

        # Lógica de distribución
        if folder in HIGH_VALUE_FOLDER_NAMES or "cro" in folder:
            dest_path = os.path.join(DEST_HIGH_VALUE, folder)
            category = "High Value (Strategy)"
        else:
            dest_path = os.path.join(DEST_UTILITIES, folder)
            category = "Utilities (Tech)"

        # Reportar progreso (Pilar 0: Visibilidad)
        progress = (idx / total_Skills) * 100
        if idx % 5 == 0 or idx == total_Skills:
            print(f"[{progress: .1f}%] Integrando {folder} -> {category}")

        if os.path.exists(dest_path):
            shutil.rmtree(dest_path)
        shutil.copytree(src_path, dest_path)

    print("\n" + "=" * 60)
    print("✅ DISTRIBUCIÓN COMPLETADA - PURE GREEN")
    print("=" * 60)
    return True


if __name__ == "__main__":
    success = distribute_Skills()
    sys.exit(0 if success else 1)
