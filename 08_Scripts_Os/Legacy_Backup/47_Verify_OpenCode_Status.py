#!/usr/bin/env python3
"""
Verificación del estado de OpenCode y ecosistema Gentleman.
Este script comprueba que todo está configurado correctamente.
"""

import os
import json
from pathlib import Path


def check_file_exists(path, description):
    """Verifica si un archivo existe."""
    if Path(path).exists():
        print(f"[OK] {description}: {path}")
        return True
    else:
        print(f"[ERROR] {description}: NO ENCONTRADO - {path}")
        return False


def check_directory_exists(path, description):
    """Verifica si un directorio existe."""
    if Path(path).is_dir():
        print(f"[OK] {description}: {path}")
        return True
    else:
        print(f"[ERROR] {description}: NO ENCONTRADO - {path}")
        return False


def count_mcps(config_path):
    """Cuenta los MCPs configurados."""
    try:
        with open(config_path, "r") as f:
            config = json.load(f)
        mcps = config.get("mcp", {})
        return len(mcps)
    except:
        return 0


def count_skills(skills_dir):
    """Cuenta las skills instaladas."""
    try:
        skills_path = Path(skills_dir)
        if skills_path.is_dir():
            return len([d for d in skills_path.iterdir() if d.is_dir()])
    except:
        pass
    return 0


def main():
    print("=" * 60)
    print("VERIFICACION DE OPENCODE Y ECOSISTEMA GENTLEMAN")
    print("=" * 60)

    root = Path(__file__).parent.parent

    # Verificar archivos de configuración
    print("\n[ARCHIVOS DE CONFIGURACION]")
    opencode_config = (
        root
        / "03_Knowledge"
        / "Resources"
        / "Gentleman.Dots"
        / "GentlemanOpenCode"
        / "opencode.json"
    )
    check_file_exists(opencode_config, "Configuracion OpenCode")

    # Verificar documentación
    print("\n[DOCUMENTACION]")
    check_file_exists(
        root / "03_Knowledge" / "OpenCode_Integration.md", "OpenCode Integration"
    )
    check_file_exists(
        root / "03_Knowledge" / "OpenCode_Commands_Reference.md", "Commands Reference"
    )
    check_file_exists(
        root / "03_Knowledge" / "OpenCode_Active_Configuration.md",
        "Active Configuration",
    )

    # Verificar skills
    print("\n[SKILLS]")
    skills_dir = (
        root
        / "03_Knowledge"
        / "Resources"
        / "Gentleman.Dots"
        / "GentlemanOpenCode"
        / "skill"
    )
    num_skills = count_skills(skills_dir)
    print(f"[OK] Skills instaladas: {num_skills}")
    check_directory_exists(skills_dir, "Directorio de skills")

    # Verificar MCPs
    print("\n[MCPS]")
    num_mcps = count_mcps(opencode_config)
    print(f"[OK] MCPs configurados: {num_mcps}")

    # Verificar agentes
    print("\n[AGENTES]")
    try:
        with open(opencode_config, "r") as f:
            config = json.load(f)
        agents = config.get("agent", {})
        print(f"[OK] Agentes configurados: {len(agents)}")
        for agent_name in agents.keys():
            print(f"   - {agent_name}")
    except:
        print("[ERROR] No se pudieron leer los agentes")

    # Verificar repositorios del ecosistema
    print("\n[REPOSITORIOS DEL ECOSISTEMA]")
    repos = [
        ("engram", root / "01_Brain" / "Engram"),
        ("agent-teams-lite", root / ".agent" / "02_Skills" / "04_Agent_Teams_Lite"),
        ("gga", root / ".agent" / "gga"),
    ]
    for repo_name, repo_path in repos:
        check_directory_exists(repo_path, repo_name)

    # Resumen final
    print("\n" + "=" * 60)
    print("RESUMEN FINAL")
    print("=" * 60)

    status = "[OK]" if num_mcps > 0 and num_skills > 0 else "[WARNING]"
    print(f"{status} OpenCode esta {'OPERATIVO' if num_mcps > 0 else 'INCOMPLETO'}")
    print(f"   - MCPs: {num_mcps}/22")
    print(f"   - Skills: {num_skills}/24+")
    print(f"   - Agentes: {len(agents) if 'agents' in locals() else 0}/3")

    print("\n[PROXIMOS PASOS]")
    print("1. Abre OpenCode")
    print("2. Usa Tab para seleccionar agente")
    print("3. Prueba: 'Usa Exa para buscar informacion sobre IA'")
    print("4. Usa /sdd:init para proyectos SDD")

    print("\n[DOCUMENTACION]")
    print("- OpenCode Integration: 03_Knowledge/OpenCode_Integration.md")
    print("- Commands Reference: 03_Knowledge/OpenCode_Commands_Reference.md")
    print("- Active Config: 03_Knowledge/OpenCode_Active_Configuration.md")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
