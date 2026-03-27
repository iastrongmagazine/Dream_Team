import os
import sys
import io
import subprocess
import glob
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
    #       _____ _      ______          _   _    _____                      #
    #      / ____| |    |  ____|   /\   | \ | |  / ____|     /\              #
    #     | |    | |    | |__     /  \  |  \| | | (___      /  \             #
    #     | |    | |    |  __|   / /\ \ | . ` |  \___ \    / /\ \            #
    #     | |____| |____| |____ / ____ \| |\  |  ____) |  / ____ \           #
    #      \_____|______|______/_/    \_\_| \_| |_____/  /_/    \_\          #
    #                                                                         #
    #                         S H I P   I T   V A L I D A T O R               #
    #                       P E R S O N A L   O S                             #
    ###########################################################################{Style.RESET_ALL}
"""
    print(banner)


ROOT_DIR = PROJECT_ROOT

# =============================================================================
# VALIDATION FUNCTIONS
# =============================================================================


def check_no_pending_tasks():
    """Verifica que no haya tareas pendientes en 02_Operations/01_Active_Tasks/."""
    tasks_dir = os.path.join(ROOT_DIR, "02_Operations", "01_Active_Tasks")
    if not os.path.exists(tasks_dir):
        print(
            f"{Fore.YELLOW}[WARN] Directorio de tareas activas no encontrado{Style.RESET_ALL}"
        )
        return True  # Si no existe, asumimos que no hay tareas pendientes

    # Buscar archivos .md en la raíz del directorio (excluyendo subdirectorios)
    md_files = [
        f
        for f in os.listdir(tasks_dir)
        if f.endswith(".md") and os.path.isfile(os.path.join(tasks_dir, f))
    ]

    if md_files:
        print(
            f"{Fore.RED}[ERR] Hay {len(md_files)} tareas pendientes en Active Tasks:{Style.RESET_ALL}"
        )
        for f in md_files[:5]:  # Mostrar solo las primeras 5
            print(f"  - {f}")
        if len(md_files) > 5:
            print(f"  ... y {len(md_files) - 5} más")
        return False
    else:
        print(
            f"{Fore.GREEN}[OK] No hay tareas pendientes en Active Tasks{Style.RESET_ALL}"
        )
        return True


def check_system_health():
    """Valida el stack tecnológico (dependencias y estructura)."""
    checks = []

    # Check Python
    version = sys.version.split()[0]
    print(f"[OK] Python: {version}")
    checks.append(True)

    # Check uv
    try:
        result = subprocess.run(
            ["uv", "--version"], capture_output=True, text=True, check=False
        )
        if result.returncode == 0:
            print(f"[OK] uv: {result.stdout.strip()}")
            checks.append(True)
        else:
            print("[ERR] uv: No encontrado")
            checks.append(False)
    except FileNotFoundError:
        print("[ERR] uv: No instalado")
        checks.append(False)

    # Check git
    try:
        result = subprocess.run(
            ["git", "--version"],
            capture_output=True,
            text=True,
            check=False,
            cwd=ROOT_DIR,
        )
        if result.returncode == 0:
            print(f"[OK] Git: {result.stdout.strip()}")
            checks.append(True)
        else:
            print("[ERR] Git: No encontrado")
            checks.append(False)
    except FileNotFoundError:
        print("[ERR] Git: No instalado")
        checks.append(False)

    # Check core structure
    critical_files = {
        "Raíz: README.md": os.path.join(ROOT_DIR, "README.md"),
        "Raíz: CLAUDE.md": os.path.join(ROOT_DIR, "CLAUDE.md"),
        "Config: settings.local.json": os.path.join(
            ROOT_DIR, ".claude", "settings.local.json"
        ),
        "Core: Server.py": os.path.join(
            ROOT_DIR, "05_System", "01_Core", "mcp", "Server.py"
        ),
    }

    print("-" * 30)
    print("Chequeo de Estructura Personal OS")
    all_ok = True
    for name, path in critical_files.items():
        if os.path.exists(path):
            print(f"[OK] {name}")
        else:
            print(f"[ERR] {name} (No encontrado en {path})")
            all_ok = False
            checks.append(False)
    print("-" * 30)

    if all_ok:
        checks.append(True)

    return all(checks)


def check_git_clean():
    """Verifica que no haya cambios pendientes en Git."""
    try:
        # Verificar si hay cambios staged o unstaged
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=False,
            cwd=ROOT_DIR,
        )
        if result.returncode == 0:
            if result.stdout.strip():
                print(
                    f"{Fore.RED}[ERR] Hay cambios pendientes en Git:{Style.RESET_ALL}"
                )
                # Mostrar los primeros 5 cambios
                changes = result.stdout.strip().split("\n")
                for change in changes[:5]:
                    print(f"  {change}")
                if len(changes) > 5:
                    print(f"  ... y {len(changes) - 5} más")
                return False
            else:
                print(f"{Fore.GREEN}[OK] Git está limpio{Style.RESET_ALL}")
                return True
        else:
            print(f"{Fore.RED}[ERR] No se pudo verificar Git{Style.RESET_ALL}")
            return False
    except Exception as e:
        print(f"{Fore.RED}[ERR] Error al verificar Git: {e}{Style.RESET_ALL}")
        return False


def main():
    """Ejecuta todas las validaciones necesarias antes de hacer un ship."""
    print_banner()
    dynamic_speak("Iniciando validaciones para Ship It")

    print(f"{Fore.CYAN}{'=' * 75}{Style.RESET_ALL}")
    print("VALIDACIONES PRE-SHIP — PersonalOS")
    print(f"{Fore.CYAN}{'=' * 75}{Style.RESET_ALL}")

    # Ejecutar validaciones
    tasks_ok = check_no_pending_tasks()
    health_ok = check_system_health()
    git_ok = check_git_clean()

    print(f"\n{Fore.CYAN}{'=' * 75}{Style.RESET_ALL}")
    print("RESUMEN DE VALIDACIONES")
    print(f"{Fore.CYAN}{'=' * 75}{Style.RESET_ALL}")
    print(
        f"Tareas pendientes: {Fore.GREEN if tasks_ok else Fore.RED}{'✅ OK' if tasks_ok else '❌ FALLO'}{Style.RESET_ALL}"
    )
    print(
        f"Salud del sistema: {Fore.GREEN if health_ok else Fore.RED}{'✅ OK' if health_ok else '❌ FALLO'}{Style.RESET_ALL}"
    )
    print(
        f"Git limpio: {Fore.GREEN if git_ok else Fore.RED}{'✅ OK' if git_ok else '❌ FALLO'}{Style.RESET_ALL}"
    )

    if tasks_ok and health_ok and git_ok:
        print(
            f"\n{Fore.GREEN}🎉 READY TO SHIP — Todas las validaciones pasaron{Style.RESET_ALL}"
        )
        dynamic_speak("Listo para hacer ship")
        sys.exit(0)
    else:
        print(
            f"\n{Fore.RED}🚫 BLOCKED — Resuelve los problemas antes de hacer ship{Style.RESET_ALL}"
        )
        dynamic_speak("Bloqueado: hay problemas que resolver")
        sys.exit(1)


if __name__ == "__main__":
    main()
