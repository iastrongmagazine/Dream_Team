#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tool Shed - Auto-detector de contexto y selector de MCPs
Carga solo los MCPs necesarios según el contexto de trabajo.

Inspirado en Stripe Minions Tool Shed Pattern
"""

import os
import sys
import json
from pathlib import Path
from datetime import datetime

# === SETUP PATHS ===
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# === IMPORTS ===
try:
    from config_paths import ROOT_DIR
except ImportError:
    ROOT_DIR = PROJECT_ROOT

# === TIERS DE MCPS ===
MCP_TIERS = {
    "core": {
        "name": "Core",
        "description": "Siempre activos",
        "mcps": ["engram", "context7", "github"],
    },
    "knowledge": {
        "name": "Knowledge",
        "description": "Notas y memoria",
        "mcps": ["mcp-obsidian", "obsidian-api", "Notion", "aim-memory-bank"],
    },
    "development": {
        "name": "Development",
        "description": "Coding y testing",
        "mcps": ["Playwright", "chrome-devtools", "docker", "filesystem"],
    },
    "research": {
        "name": "Research",
        "description": "Investigación web",
        "mcps": ["exa", "firecrawl-mcp", "brave-search", "supabase"],
    },
    "visual": {
        "name": "Visual",
        "description": "Diagramas y diseño",
        "mcps": ["excalidraw-yctimlin", "pencil", "magicuidesign-mcp"],
    },
    "productivity": {
        "name": "Productivity",
        "description": "Gestión de proyectos",
        "mcps": ["Linear", "slack", "atlassian", "jira-extended"],
    },
}

# === DETECTOR DE CONTEXTO ===
CONTEXT_KEYWORDS = {
    "development": [
        "code",
        "coding",
        "debug",
        "fix",
        "bug",
        "feature",
        "refactor",
        "test",
        "build",
        "deploy",
        "script",
        "python",
        "javascript",
        "react",
    ],
    "research": [
        "search",
        "research",
        "find",
        "lookup",
        "web",
        "analyze",
        "investigate",
        "explore",
        "look up",
        "buscar",
        "investigar",
    ],
    "knowledge": [
        "note",
        "notes",
        "document",
        "docs",
        "wiki",
        "obsidian",
        "notion",
        "write",
        "redact",
        "escribir",
        "nota",
    ],
    "visual": [
        "diagram",
        "draw",
        "design",
        "chart",
        "flowchart",
        "excalidraw",
        "mermaid",
        "visual",
        "gráfico",
    ],
    "productivity": [
        "task",
        "project",
        "ticket",
        "jira",
        "linear",
        "schedule",
        "plan",
        "tarea",
        "proyecto",
    ],
}


def detect_context(user_input: str = "") -> list:
    """Detecta el contexto de trabajo basado en input del usuario."""
    user_input = user_input.lower()

    detected = ["core"]  # Core siempre activo

    for tier, keywords in CONTEXT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in user_input:
                if tier not in detected:
                    detected.append(tier)
                break

    return detected


def get_mcps_for_tiers(tiers: list) -> list:
    """Retorna lista de MCPs para los tiers detectados."""
    mcps = []
    for tier in tiers:
        if tier in MCP_TIERS:
            mcps.extend(MCP_TIERS[tier]["mcps"])
    return list(set(mcps))  # Remove duplicates


def load_mcp_config() -> dict:
    """Carga la configuración actual de MCPs."""
    mcp_path = ROOT_DIR / "01_Core" / "05_Mcp" / "mcp.json"

    if not mcp_path.exists():
        print(f"[WARN] MCP config not found: {mcp_path}")
        return {"mcpServers": {}}

    with open(mcp_path, "r", encoding="utf-8") as f:
        return json.load(f)


def print_tool_shed(tiers: list):
    """Muestra el Tool Shed actual."""
    print("\n" + "=" * 60)
    print("TOOL SHED - PersonalOS")
    print("=" * 60)
    print(f"\nFecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"\nContextos detectados: {', '.join(tiers)}")
    print()

    print("MCPs por Tier:")
    print("-" * 40)

    all_mcps = []
    for tier in tiers:
        if tier in MCP_TIERS:
            info = MCP_TIERS[tier]
            print(f"\n[{info['name']}] ({info['description']})")
            for mcp in info["mcps"]:
                print(f"   - {mcp}")
                all_mcps.append(mcp)

    print("\n" + "-" * 40)
    print(f"Total MCPs activos: {len(set(all_mcps))}")
    print("=" * 60)


def main():
    """Punto de entrada."""
    # Si hay argumentos, usar como input del usuario
    if len(sys.argv) > 1:
        user_input = " ".join(sys.argv[1:])
    else:
        # Modo interactivo
        print("Tool Shed - Detector de Contexto")
        print("Ingresa contexto (o presiona Enter para modo desarrollo): ")
        user_input = input("> ").strip()

    # Detectar contexto
    tiers = detect_context(user_input if user_input else "development")

    # Mostrar Tool Shed
    print_tool_shed(tiers)

    # Mostrar MCPs disponibles
    mcp_config = load_mcp_config()
    available_mcps = list(mcp_config.get("mcpServers", {}).keys())
    active_mcps = get_mcps_for_tiers(tiers)

    print("\n[OK] MCPs disponibles en config:")
    for mcp in active_mcps:
        status = "[OK]" if mcp in available_mcps else "[MISSING]"
        print(f"   {status} {mcp}")

    print("\n[TIP] Usa esta información para configurar tu sesión de trabajo.")
    print("   Los MCPs activos se cargan automáticamente según el contexto.")


if __name__ == "__main__":
    main()
