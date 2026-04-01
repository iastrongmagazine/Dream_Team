#!/usr/bin/env python3
"""
88_Frontend_Premium.py — Frontend Premium Workflow Automation
Orquesta creación de UIs premium usando Taste Skills.
Basado en: .agent/03_Workflows/09_Frontend_Premium.md
"""

import os
import sys
import io
import subprocess
import json
from pathlib import Path
from datetime import datetime

try:
    from colorama import init, Fore, Style

    init()
except ImportError:

    class Fore:
        GREEN = YELLOW = RED = CYAN = MAGENTA = BLUE = ""

    class Style:
        RESET_ALL = ""


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
            cmd = f"PowerShell -Command \"Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}')\""
            subprocess.Popen(
                cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
            )
        except:
            pass


def print_banner():
    banner = rf"""
{Fore.GREEN}    ###########################################################################
    #                                                                         #
    #     ______ _                _____       _           _                   #
    #    |  ____| |             |  __ \     | |         | |                  #
    #    | |__  | | __ _ _   _  | |__) |_ _ | |_   ___  | |_   _  ___ __ _  #
    #    |  __| | |/ _` | | | | |  _  / _` || | | / __| | | | | |/ __/ _` | #
    #    | |    | | (_| | |_| | | | \ \ (_| || | || (__  | | |_| | (_| (_| | #
    #    |_|    |_|\__,_|\__, | |_|  \_\__,_||_| \___| |_|\__,_|\___\__,_| #
    #                     __/ |                                              #
    #                    |___/          PREMIUM WORKFLOW                      #
    #                                                                         #
    #           Landing Pages · WebApps · Dashboards · UIs Premium           #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


# =============================================================================
# PROJECT TYPE DETECTION
# =============================================================================

PROJECT_TYPES = {
    "landing": {
        "name": "Landing / Webapp nueva",
        "skills": ["taste-skill", "output-skill"],
        "design_variance": 8,
        "motion_intensity": 6,
        "visual_density": 4,
    },
    "invitation": {
        "name": "Invitación / Evento premium",
        "skills": ["soft-skill", "output-skill"],
        "design_variance": 9,
        "motion_intensity": 8,
        "visual_density": 3,
    },
    "dashboard": {
        "name": "Dashboard / Data-heavy",
        "skills": ["minimalist-skill", "output-skill"],
        "design_variance": 4,
        "motion_intensity": 3,
        "visual_density": 7,
    },
    "redesign": {
        "name": "Legacy upgrade / Redesign",
        "skills": ["redesign-skill", "output-skill"],
        "design_variance": 6,
        "motion_intensity": 5,
        "visual_density": 5,
    },
}

SKILLS_BASE_PATH = ".cursor/02_Skills/11_Taste_Skills"


# =============================================================================
# VALIDATION FUNCTIONS
# =============================================================================


def detect_project_type():
    """Solicita al usuario el tipo de proyecto."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("🎯 TIPO DE PROYECTO")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    print("\nSelecciona el tipo de proyecto:\n")
    for key, value in PROJECT_TYPES.items():
        print(f"  {Fore.GREEN}{key}{Style.RESET_ALL}: {value['name']}")

    print(f"\n  {Fore.YELLOW}Ejemplo: 'landing'{Style.RESET_ALL}")
    return None


def verify_stack():
    """Verifica el stack tecnológico del proyecto."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("📦 VERIFICACIÓN DE STACK")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    checks = []

    # Verificar package.json
    package_json = os.path.join(PROJECT_ROOT, "package.json")
    if os.path.exists(package_json):
        print(f"{Fore.GREEN}[OK] package.json encontrado{Style.RESET_ALL}")
        checks.append(True)

        try:
            with open(package_json, "r", encoding="utf-8") as f:
                pkg = json.load(f)

            # Detectar framework
            deps = {**pkg.get("dependencies", {}), **pkg.get("devDependencies", {})}

            frameworks = {
                "next": "Next.js",
                "react": "React",
                "vue": "Vue",
                "angular": "Angular",
                "@angular/core": "Angular",
                "svelte": "Svelte",
                "astro": "Astro",
            }

            for dep, name in frameworks.items():
                if dep in deps:
                    print(
                        f"{Fore.GREEN}[OK] Framework: {name} v{deps[dep]}{Style.RESET_ALL}"
                    )
                    break

            # Verificar Tailwind
            if "tailwindcss" in deps:
                print(
                    f"{Fore.GREEN}[OK] Tailwind CSS: {deps['tailwindcss']}{Style.RESET_ALL}"
                )
            else:
                print(f"{Fore.YELLOW}[WARN] Tailwind no encontrado{Style.RESET_ALL}")

            # Verificar Radix/Phosphor (anti-emoji)
            radix = "radix-ui-react" in str(deps) or "@radix-ui" in str(deps)
            if radix:
                print(
                    f"{Fore.GREEN}[OK] Radix UI detectado (anti-emoji ready){Style.RESET_ALL}"
                )

        except json.JSONDecodeError:
            print(f"{Fore.RED}[ERR] package.json corrupto{Style.RESET_ALL}")
            checks.append(False)
    else:
        print(f"{Fore.YELLOW}[WARN] package.json no encontrado{Style.RESET_ALL}")
        checks.append(False)

    # Verificar node_modules
    node_modules = os.path.join(PROJECT_ROOT, "node_modules")
    if os.path.isdir(node_modules):
        print(f"{Fore.GREEN}[OK] node_modules instalado{Style.RESET_ALL}")
    else:
        print(
            f"{Fore.YELLOW}[WARN] node_modules no encontrado — ejecutar npm install{Style.RESET_ALL}"
        )

    return all(checks) if checks else False


def verify_skills():
    """Verifica que las Taste Skills estén disponibles."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("🎨 TASTE SKILLS DISPONIBLES")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    skills_path = os.path.join(PROJECT_ROOT, SKILLS_BASE_PATH)
    required_skills = [
        "taste-skill",
        "soft-skill",
        "minimalist-skill",
        "redesign-skill",
        "output-skill",
    ]

    available = []
    for skill in required_skills:
        skill_path = os.path.join(skills_path, skill, "SKILL.md")
        if os.path.exists(skill_path):
            print(f"{Fore.GREEN}[OK] {skill}{Style.RESET_ALL}")
            available.append(skill)
        else:
            print(f"{Fore.YELLOW}[SKIP] {skill} no encontrado{Style.RESET_ALL}")

    return available


def print_config_template(
    project_type, design_variance, motion_intensity, visual_density
):
    """Imprime la configuración recomendada para taste-skill."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("⚙️ CONFIGURACIÓN TASTE-SKILL")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    print(f"""
  {Fore.GREEN}Project Type:{Style.RESET_ALL} {project_type}

  {Fore.MAGENTA}DESIGN_VARIANCE{Style.RESET_ALL} (1-10): {design_variance}   # {"Alta variación" if design_variance > 7 else "Balanceado" if design_variance > 4 else "Conservador"}
  {Fore.MAGENTA}MOTION_INTENSITY{Style.RESET_ALL} (1-10): {motion_intensity}  # {"Muy animado" if motion_intensity > 7 else "Sutil" if motion_intensity > 4 else "Estático"}
  {Fore.MAGENTA}VISUAL_DENSITY{Style.RESET_ALL} (1-10): {visual_density}    # {"Denso" if visual_density > 7 else "Balanceado" if visual_density > 4 else "Airy"}
""")


def print_anti_emoji_rules():
    """Muestra las reglas anti-emoji."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("🚫 REGLAS ANTI-EMOJI")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    print(f"""
  {Fore.RED}EMOJIS BANEADOS{Style.RESET_ALL}

  {Fore.GREEN}Usar en su lugar:{Style.RESET_ALL}
    • Radix Icons (@radix-ui/react-icons)
    • Phosphor Icons (phosphor-react)
    • SVG inline personalizados

  {Fore.YELLOW}Motivo:{Style.RESET_ALL} Emojis degradan la experiencia premium.
""")


def print_generation_checklist():
    """Imprime el checklist de generación."""
    print(f"\n{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")
    print("✅ CHECKLIST DE GENERACIÓN")
    print(f"{Fore.CYAN}{'=' * 60}{Style.RESET_ALL}")

    checklist = [
        "Componentes limpios y reutilizables",
        "Tailwind con clases legibles",
        "Animaciones sutiles (fade-in, scroll)",
        "Dark mode implementado",
        "Responsive por defecto",
        "Sin emojis (solo SVG/Icons)",
        "Código completo (sin placeholders)",
        "Dependencias en package.json",
    ]

    for i, item in enumerate(checklist, 1):
        print(f"  {i}. [ ] {item}")


def main():
    """Ejecuta el workflow Frontend Premium."""
    print_banner()
    dynamic_speak("Iniciando Frontend Premium Workflow")

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{Fore.MAGENTA}🕐 Workflow iniciado: {timestamp}{Style.RESET_ALL}")

    # Verificar stack
    stack_ok = verify_stack()

    # Verificar skills
    available_skills = verify_skills()

    # Mostrar configuración para landing (default)
    config = PROJECT_TYPES["landing"]
    print_config_template(
        config["name"],
        config["design_variance"],
        config["motion_intensity"],
        config["visual_density"],
    )

    # Reglas anti-emoji
    print_anti_emoji_rules()

    # Checklist
    print_generation_checklist()

    # Resumen
    print(f"\n{Fore.GREEN}{'=' * 60}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}🎨 FRONTEND PREMIUM — Workflow listo{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'=' * 60}{Style.RESET_ALL}")

    print(
        f"\n  Skills disponibles: {', '.join(available_skills) if available_skills else 'Ninguna'}"
    )
    print(f"  Stack verificado: {'✅' if stack_ok else '⚠️ Parcial'}")
    print(
        f"\n  {Fore.YELLOW}💡 Usa las skills con: @taste-skill/SKILL.md + @output-skill/SKILL.md{Style.RESET_ALL}"
    )

    dynamic_speak("Frontend Premium Workflow completado")


if __name__ == "__main__":
    main()
