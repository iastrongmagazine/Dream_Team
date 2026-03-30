#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PersonalOS Installer v2.0

Script de instalación para migrar PersonalOS a otra PC.
Detecta si es la misma máquina o necesita configuración.

Incluye:
- System Guardian integration
- Alias setup (gr, gra, gr-agents)
- Hook registration
"""

import os
import sys
import json
import shutil
import time
import subprocess

# Fix Windows console encoding
if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")

# Agregar scripts al path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(SCRIPT_DIR, "scripts")
sys.path.insert(0, SCRIPTS_DIR)

from detect_machine import detect_same_machine, save_machine_id
from setup_dependencies import install_dependencies, check_git, check_node
from configure_paths import configure_mcp, validate_paths, validate_api_key_format
from validate import run_validation, check_mcp_json, check_machine_id, check_structure

# Importar setup_aliases si existe
try:
    from setup_aliases import setup_guardian_aliases, print_alias_instructions
except ImportError:
    setup_guardian_aliases = None
    print_alias_instructions = None


def print_banner():
    """Imprime el banner del installer"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║   ███████╗ ██████╗ ██╗      █████╗ ██████╗ ██████╗ ██╗   ██╗
║   ██╔════╝██╔═══██╗██║     ██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝
║   ███████╗██║   ██║██║     ███████║██████╔╝██████╔╝ ╚████╔╝
║   ╚════██║██║   ██║██║     ██╔══██║██╔══██╗██╔═══╝   ╚██╗
║   ███████║╚██████╔╝███████╗██║  ██║██║  ██║██║        ██║
║   ╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝        ╚═╝
║                                                              ║
║            ██████╗ ███████╗██╗   ██╗                       ║
║            ██╔══██╗██╔════╝██║   ██║                       ║
║            ██║  ██║█████╗  ██║   ██║                       ║
║            ██║  ██║██╔══╝  ╚██╗ ██╔╝                       ║
║            ██████╔╝███████╗ ╚████╔╝                        ║
║            ╚═════╝ ╚══════╝  ╚═══╝                         ║
║                                                              ║
║                    INSTALLER v1.0.0                         ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """)


def get_config_path(mode="migrate"):
    """Obtiene la ruta del archivo de configuración"""
    if mode == "migrate":
        return os.path.join(SCRIPT_DIR, "config.json")
    else:
        return os.path.join(SCRIPT_DIR, "config.template.json")


def load_config(config_path):
    """Carga el archivo de configuración"""
    if not os.path.exists(config_path):
        return None

    with open(config_path, "r") as f:
        return json.load(f)


def input_path(prompt, default=""):
    """Pide una ruta al usuario con validación"""
    while True:
        path = input(f"{prompt}{f' [{default}]' if default else ''}: ").strip()

        if not path:
            if default:
                path = default
            else:
                print("  ❌ Ruta requerida")
                continue

        # Expandir variables de entorno
        path = os.path.expandvars(path)

        # Validar que existe
        if os.path.exists(path):
            print(f"  ✓ {path}")
            return path
        else:
            # Preguntar si crear o reintentar
            create = input(f"  ⚠ La ruta no existe. ¿Crear? (s/n): ").strip().lower()
            if create == "s":
                try:
                    os.makedirs(path, exist_ok=True)
                    print(f"  ✓ Creado: {path}")
                    return path
                except Exception as e:
                    print(f"  ❌ Error creando: {e}")
            else:
                retry = input("  ¿Otra ruta? (s/n): ").strip().lower()
                if retry != "s":
                    return path  # Usar la ruta de todos modos


def input_api_key(prompt, current="", validate=True):
    """Pide una API key al usuario"""
    while True:
        key = input(f"{prompt}{f' [actual]' if current else ''}: ").strip()

        if not key:
            if current:
                print(f"  → Usando key existente")
                return current
            else:
                print("  ℹ Omitido (Enter)")
                return ""

        # Validar formato básico
        if validate and not validate_api_key_format(
            prompt.lower().replace(" ", "_"), key
        ):
            retry = (
                input("  ⚠ Formato怀疑. ¿Usar de todos modos? (s/n): ").strip().lower()
            )
            if retry != "s":
                continue

        return key


def interactive_config():
    """Configuración interactiva para nuevos usuarios"""
    print("\n" + "=" * 50)
    print("CONFIGURACIÓN INTERACTIVA")
    print("=" * 50 + "\n")

    config = {"mode": "new", "version": "1.0.0", "paths": {}, "api_keys": {}}

    # Pedir rutas
    print("--- RUTAS DEL SISTEMA ---")
    config["paths"]["downloads"] = input_path(
        "Ruta de Downloads",
        "C:\\Users\\" + os.getenv("USERNAME", "user") + "\\Downloads",
    )

    config["paths"]["obsidian_vault"] = input_path("Ruta del Vault de Obsidian")

    config["paths"]["excalidraw"] = input_path(
        "Ruta de Diagramas Excalidraw",
        "C:\\Users\\"
        + os.getenv("USERNAME", "user")
        + "\\Documents\\Diagramas Excalidraw",
    )

    # Validar rutas
    print("\n--- VALIDANDO RUTAS ---")
    validate_paths(config)

    # Pedir APIs
    print("\n--- API KEYS (opcional, Enter para omitir) ---")
    print("Presiona Enter para omitir o usar el valor por defecto\n")

    apis = [
        ("context7", "Context7 API Key"),
        ("exa", "Exa API Key"),
        ("fireflies", "Fireflies API Key"),
        ("github", "GitHub PAT"),
        ("notion", "Notion API Key"),
    ]

    for key_name, prompt in apis:
        config["api_keys"][key_name] = input_api_key(prompt)

    # Guardar configuración
    config_path = os.path.join(SCRIPT_DIR, "config.json")
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

    print(f"\n✓ Configuración guardada: {config_path}")

    return config


def run_installer(mode="migrate"):
    """Ejecuta el instalador"""
    print(f"\n📦 Modo: {mode.upper()}\n")

    # 1. Verificar/crear estructura
    print("1️⃣ Verificando estructura...")
    if not check_structure():
        print("❌ Estructura del proyecto incompleta")
        return False
    print("   ✓ Estructura OK")

    # 2. Instalar dependencias
    print("\n2️⃣ Instalando dependencias...")
    if not install_dependencies():
        print("❌ Error instalando dependencias")
        return False
    print("   ✓ Dependencias OK")

    # 3. Cargar configuración
    print("\n3️⃣ Cargando configuración...")
    config_path = get_config_path(mode)

    if mode == "new":
        config = interactive_config()
    else:
        config = load_config(config_path)
        if not config:
            print(f"⚠ No se encontró config.json, cambiando a modo new")
            config = interactive_config()

    # 4. Configurar MCPs
    print("\n4️⃣ Configurando MCPs...")
    project_root = os.path.dirname(SCRIPT_DIR)
    if not configure_mcp(config, project_root):
        print("❌ Error configurando MCPs")
        return False
    print("   ✓ MCPs OK")

    # 5. Guardar machine_id
    print("\n5️⃣ Registrando máquina...")
    save_machine_id()
    print("   ✓ Machine ID guardado")

    # 6. Configurar aliases de System Guardian
    print("\n6️⃣ Configurando aliases (gr, gra, gr-agents)...")
    if setup_guardian_aliases:
        setup_guardian_aliases()
        print("   ✓ Aliases configurados")
    else:
        print_alias_instructions()
        print("   ⚠ Aliases: manual (ver instrucciones arriba)")

    # 7. Registrar hooks
    print("\n7️⃣ Registrando hooks...")
    from configure_paths import register_hooks

    if register_hooks():
        print("   ✓ Hooks registrados")
    else:
        print("   ⚠ Hooks: manual")

    # 8. Validar
    print("\n8️⃣ Validando instalación...")
    if not check_mcp_json():
        print("⚠ MCP JSON con problemas")

    if not run_validation():
        print("⚠ Validación del stack falló")

    return True


def run_guardian():
    """Ejecuta System Guardian al final de la instalación"""
    print("\n" + "=" * 50)
    print("  SYSTEM GUARDIAN - Validación Final")
    print("=" * 50)

    project_root = os.path.dirname(SCRIPT_DIR)
    guardian_path = os.path.join(
        project_root, "04_ENGINE", "08_Scripts_Os", "79_System_Guardian.py"
    )

    if os.path.exists(guardian_path):
        print("\nEjecutando System Guardian...")
        try:
            result = subprocess.run(
                [sys.executable, guardian_path],
                cwd=project_root,
                capture_output=True,
                text=True,
                timeout=180,
            )
            print(result.stdout)
            if result.stderr:
                print(result.stderr, file=sys.stderr)

            # Mostrar beep si hay issues
            if "FAIL" in result.stdout or "WARN" in result.stdout:
                print("\n⚠️  ISSUES DETECTADOS - Revisa el reporte:")
                print("   04_ENGINE/06_Reports/guardian_latest.md")
                try:
                    import winsound

                    winsound.Beep(1000, 500)
                except:
                    pass
            else:
                print("\n✅ System Guardian: Todo OK")
        except subprocess.TimeoutExpired:
            print("⚠️  System Guardian: Timeout")
        except Exception as e:
            print(f"⚠️  System Guardian: {e}")
    else:
        print("⚠️  System Guardian no encontrado")

    print("=" * 50 + "\n")


def main():
    """Punto de entrada principal"""
    print_banner()

    # Detectar modo
    print("\n🔍 Detectando configuración previa...")
    is_same_machine, message = detect_same_machine()
    print(f"   {message}\n")

    # Determinar modo
    if is_same_machine:
        print("¡Bienvenido de vuelta!")
        mode = "migrate"
    else:
        print("Nueva máquina detectada. Iniciando configuración...")

        # Preguntar si tiene config existente
        config_path = os.path.join(SCRIPT_DIR, "config.json")
        if os.path.exists(config_path):
            use_existing = (
                input("\n¿Tienes un archivo config.json existente? (s/n): ")
                .strip()
                .lower()
            )

            if use_existing == "s":
                mode = "migrate"
            else:
                mode = "new"
        else:
            mode = "new"

    # Ejecutar instalador
    success = run_installer(mode)

    if success:
        # Ejecutar System Guardian al final
        run_guardian()

        print("\n" + "=" * 50)
        print("🎉 ¡INSTALACIÓN COMPLETADA!")
        print("=" * 50)
        print("\nComandos útiles:")
        print("  gr              # System Guardian (dry-run)")
        print("  gra             # System Guardian (con fixes)")
        print("  python 04_Operations/13_Validate_Stack.py")
    else:
        print("\n❌ INSTALACIÓN FALLIDA")
        sys.exit(1)


if __name__ == "__main__":
    main()
