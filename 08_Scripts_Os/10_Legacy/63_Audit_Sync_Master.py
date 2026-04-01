#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
63_Audit_Sync_Master.py
=======================
PersonalOS - Audit Sync Master

Este script mapea, detecta cambios y actualiza automaticamente los arrays
de validacion en los scripts de auditoria cuando se agregan nuevas carpetas,
skills o recursos al sistema.

Ejecutar desde: 04_Engine/08_Scripts_Os/
Uso: python 63_Audit_Sync_Master.py

Flujo:
1. Mapea scripts de auditoria (lee DIMENSIONS, listas)
2. Escanea estructura actual (00-06 + subcarpetas)
3. Compara expectativas vs realidad
4. Actualiza arrays automaticamente
5. Reporta cambios

Integracion: Llamado desde 08_Ritual_Cierre.py
"""

import os
import sys
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Tuple

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import ROOT_DIR, OPERATIONS_DIR, OPERATIONS_ANALYTICS_DIR

# Fix encoding for Windows
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except:
        pass

# ============================================================
# CONFIGURACION
# ============================================================

# Dimensiones oficiales del OS (00-06)
OS_DIMENSIONS = [
    "00_Core",
    "01_Brain",
    str(OPERATIONS_DIR.name),
    "03_Knowledge",
    "04_Engine",
    "05_System",
    "06_Archive",
]

# Scripts de auditoria a mapear
AUDIT_SCRIPTS = [
    "53_Structure_Auditor.py",
    "40_Validate_Rules.py",
    "34_Skill_Auditor.py",
    "57_Repo_Sync_Auditor.py",
]

# ============================================================
# FUNCIONES DE ESCANEO
# ============================================================


def get_current_dimensions() -> List[str]:
    """Escanea las carpetas actuales en ROOT."""
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent.parent

    dimensions = []
    for item in os.listdir(root_dir):
        path = root_dir / item
        if item.startswith("0") and os.path.isdir(path):
            dimensions.append(item)
    return sorted(dimensions)


def get_knowledge_subdirs() -> List[str]:
    """Escanea subcarpetas en 03_Knowledge."""
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent.parent
    knowledge_dir = root_dir / "03_Knowledge"

    if not knowledge_dir.exists():
        return []

    subdirs = []
    for item in os.listdir(knowledge_dir):
        path = knowledge_dir / item
        if os.path.isdir(path) and not item.startswith("."):
            subdirs.append(item)
    return sorted(subdirs)


def get_external_repos() -> List[str]:
    """Detecta repos externos (como 10_Repos_Gentleman)."""
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent.parent
    knowledge_dir = root_dir / "03_Knowledge"

    repos = []
    if not knowledge_dir.exists():
        return repos

    for item in os.listdir(knowledge_dir):
        path = knowledge_dir / item
        if os.path.isdir(path):
            # Detectar repos clonados (tienen .git) o carpetas que parecen repos
            git_dir = path / ".git"
            if git_dir.exists() or (item.startswith("10_") or item.startswith("11_")):
                repos.append(item)
    return sorted(repos)


def get_taste_skills() -> List[str]:
    """Detecta skills de Taste-Skill disponibles."""
    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent.parent
    taste_dir = root_dir / "03_Knowledge" / "10_Repos_Gentleman" / "taste-skill"

    skills = []
    if not taste_dir.exists():
        return skills

    for item in os.listdir(taste_dir):
        skill_path = taste_dir / item / "SKILL.md"
        if os.path.isdir(taste_dir / item) and skill_path.exists():
            skills.append(item)
    return sorted(skills)


# ============================================================
# FUNCIONES DE ANALISIS
# ============================================================


def compare_structure() -> Dict:
    """Compara la estructura actual con las expectativas."""

    script_dir = Path(__file__).resolve().parent
    root_dir = script_dir.parent.parent

    current_dims = get_current_dimensions()
    knowledge_subdirs = get_knowledge_subdirs()
    external_repos = get_external_repos()
    taste_skills = get_taste_skills()

    # Detectar nuevas carpetas
    new_dims = [d for d in current_dims if d not in OS_DIMENSIONS]

    return {
        "timestamp": datetime.now().isoformat(),
        "root_dir": str(root_dir),
        "current_dimensions": current_dims,
        "expected_dimensions": OS_DIMENSIONS,
        "new_dimensions": new_dims,
        "knowledge_subdirs": knowledge_subdirs,
        "external_repos": external_repos,
        "taste_skills": taste_skills,
        "status": "OK" if not new_dims else "CHANGES_DETECTED",
    }


def parse_audit_script(script_name: str) -> Dict:
    """Parsea un script de auditoria para encontrar sus arrays de validacion."""
    script_dir = Path(__file__).resolve().parent
    script_path = script_dir / script_name

    if not script_path.exists():
        return {"error": "Script no encontrado"}

    content = script_path.read_text(encoding="utf-8")

    # Buscar arrays DIMENSIONS
    dimensions_match = re.search(r"DIMENSIONS\s*=\s*\[(.*?)\]", content, re.DOTALL)

    result = {
        "script": script_name,
        "dimensions_found": [],
        "has_dimensions": dimensions_match is not None,
    }

    if dimensions_match:
        dims = re.findall(r'"([^"]+)"', dimensions_match.group(1))
        result["dimensions_found"] = dims

    return result


# ============================================================
# FUNCIONES DE ACTUALIZACION
# ============================================================


def update_structure_auditor(structure_info: Dict) -> Tuple[bool, str]:
    """Actualiza 53_Structure_Auditor.py con la estructura actual."""

    script_dir = Path(__file__).resolve().parent
    script_path = script_dir / "53_Structure_Auditor.py"

    if not script_path.exists():
        return False, "Script no encontrado"

    content = script_path.read_text(encoding="utf-8")

    # Buscar el array DIMENSIONS
    dimensions_match = re.search(r"(DIMENSIONS\s*=\s*\[)(.*?)(\])", content, re.DOTALL)

    if not dimensions_match:
        return False, "No se encontro DIMENSIONS para actualizar"

    # Extraer dimensiones actuales del script
    current_dims_in_script = re.findall(r'"([^"]+)"', dimensions_match.group(2))

    # Comparar con lo esperado
    expected_dims = OS_DIMENSIONS

    if set(current_dims_in_script) != set(expected_dims):
        # Reemplazar el array
        new_dims_str = (
            "\n    " + ",\n    ".join([f'"{d}"' for d in expected_dims]) + ",\n"
        )

        new_content = (
            dimensions_match.group(1) + new_dims_str + dimensions_match.group(3)
        )

        content = content.replace(dimensions_match.group(0), new_content)

        # Agregar comentario de ultima actualizacion
        timestamp = datetime.now().strftime("%Y-%m-%d")
        if f"# Updated: {timestamp}" not in content:
            header = "# Updated: " + timestamp + " - Auto-sync by 63_Audit_Sync_Master"
            content = content.replace(
                "DIMENSIONS = [", "DIMENSIONS = [  # " + timestamp, 1
            )

        script_path.write_text(content, encoding="utf-8")
        return True, f"Actualizado a {expected_dims}"

    return False, "No necesita actualizacion"


# ============================================================
# MAIN
# ============================================================


def main():
    """Funcion principal."""
    print("\n" + "=" * 60)
    print("   63_AUDIT_SYNC_MASTER - PersonalOS")
    print("=" * 60 + "\n")

    # 1. Escanear estructura actual
    print("[1/4] Escaneando estructura actual...")
    structure_info = compare_structure()

    print(f"  [OK] Dimensiones: {structure_info['current_dimensions']}")
    print(f"  [OK] Subcarpetas 03_Knowledge: {structure_info['knowledge_subdirs']}")
    print(f"  [OK] Repos externos: {structure_info['external_repos']}")
    print(f"  [OK] Taste-Skills: {structure_info['taste_skills']}")
    print(f"  [OK] Estado: {structure_info['status']}\n")

    # 2. Analizar scripts de auditoria
    print("[2/4] Analizando scripts de auditoria...")
    audit_analysis = []
    for script_name in AUDIT_SCRIPTS:
        result = parse_audit_script(script_name)
        audit_analysis.append(result)
        status = "[OK]" if result.get("has_dimensions") else "[--]"
        print(f"  {status} {script_name}")

    # 3. Actualizar scripts
    print("\n[3/4] Actualizando scripts...")
    updates = []

    success, message = update_structure_auditor(structure_info)
    updates.append(
        {"script": "53_Structure_Auditor.py", "success": success, "message": message}
    )

    status_icon = "[OK]" if success else "[--]"
    print(f"  {status_icon} 53_Structure_Auditor.py: {message}")

    # 4. Resumen
    print("\n" + "=" * 60)
    print("RESUMEN")
    print("=" * 60)

    if structure_info["new_dimensions"]:
        print(
            f"  [WARN] Nuevas dimensiones detectadas: {structure_info['new_dimensions']}"
        )
        print(f"         (No son parte del OS 00-06)")

    print(f"  Subcarpetas en 03_Knowledge: {len(structure_info['knowledge_subdirs'])}")
    print(f"  Repos externos: {len(structure_info['external_repos'])}")

    if structure_info["external_repos"]:
        print(f"  Taste-Skills disponibles: {structure_info['taste_skills']}")

    print("=" * 60 + "\n")

    # Guardar reporte en log
    log_dir = OPERATIONS_ANALYTICS_DIR

    if log_dir.exists():
        report_lines = [
            "63_AUDIT_SYNC_MASTER Report",
            "=" * 40,
            f"Timestamp: {structure_info['timestamp']}",
            f"Status: {structure_info['status']}",
            f"Dimensions: {structure_info['current_dimensions']}",
            f"Knowledge Subdirs: {structure_info['knowledge_subdirs']}",
            f"External Repos: {structure_info['external_repos']}",
            f"Taste Skills: {structure_info['taste_skills']}",
            f"Updates: {updates}",
        ]
        log_file = (
            log_dir / f"audit_sync_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        )
        log_file.write_text("\n".join(report_lines), encoding="utf-8")
        print(f"[LOG] Reporte guardado: {log_file}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
