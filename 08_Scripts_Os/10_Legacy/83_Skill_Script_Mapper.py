"""
83_Skill_Script_Mapper.py - Armor Layer Protected
"""

import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import PROJECT_ROOT

REQUIRED_DIRS = [
    "00_Core",
    "01_Brain",
    "02_Operations",
    "03_Knowledge",
    "04_Engine",
    "05_System",
    "06_Archive",
]
for d in REQUIRED_DIRS:
    if not (PROJECT_ROOT / d).exists():
        print(f"[WARN] Required directory not found: {d}")

ROOT_DIR = PROJECT_ROOT
SKILLS_DIR = ROOT_DIR / ".agent" / "02_Skills"
ENGINE_DIR = ROOT_DIR / "04_Engine"
BORRADOR_PATH = ROOT_DIR / "BORRADOR_MAPEO_SISTEMA.md"
REPORTE_PATH = (
    ROOT_DIR / "01_Brain" / "07_Memory_Brain" / "07_Mapping_Skills_Scripts.md"
)

ALIASES = {
    "gr": "79_System_Guardian.py",
    "gra": "79_System_Guardian.py",
    "gr-agents": "79_System_Guardian.py",
    "ce-commit": "52_Safe_Commit.py",
    "ce-guard": "54_Commit_Guard.py",
    "ce-audit": "42_Audit_Engineering.py",
    "ce-structure": "53_Structure_Auditor.py",
}

# 1. Get physical scripts
physical_scripts = {}  # normalized_name -> (actual_filename, relative_path)
all_filenames = set()

if ENGINE_DIR.exists():
    for root, _, files in os.walk(ENGINE_DIR):
        if "__pycache__" in root:
            continue
        for file in files:
            if file.endswith(".py"):
                path = Path(root) / file
                all_filenames.add(file)
                # Normalize: remove leading digits, lowercase, remove separators and .py
                base_name = re.sub(r"^\d+_", "", file).replace(".py", "")
                norm_name = (
                    base_name.lower().replace("_", "").replace("-", "").replace(" ", "")
                )
                physical_scripts[norm_name] = (file, path.relative_to(ROOT_DIR))
                # Store by full lowercase name too
                physical_scripts[file.lower()] = (file, path.relative_to(ROOT_DIR))


def normalize_text(text):
    # Remove digits at start, .py at end, and all separators
    t = re.sub(r"^\d+_", "", text)
    t = t.replace(".py", "").lower().replace("_", "").replace("-", "").replace(" ", "")
    return t


def find_script_by_name(name):
    norm = normalize_text(name)
    if norm in physical_scripts:
        return physical_scripts[norm]
    # Try searching for the name as a substring of any physical script
    for p_norm, val in physical_scripts.items():
        if norm in p_norm and len(norm) > 4:
            return val
    return None


skill_mappings = []
used_scripts = set()
skill_ghosts = set()

if SKILLS_DIR.exists():
    for root, dirs, files in os.walk(SKILLS_DIR):
        if "10_Backup" in root:
            continue
        skill_dir = Path(root)
        profile_name = (
            skill_dir.parent.name if skill_dir.parent != SKILLS_DIR else "N/A"
        )
        skill_name = skill_dir.name

        # Check if it's a skill directory (has SKILL.md or is a leaf)
        if "SKILL.md" in files or "command" in dirs or not dirs:
            refs_raw = set()

            # MODE A: Name Convention Matching (Priority)
            match = find_script_by_name(skill_name)
            if match:
                refs_raw.add(match[0])

            # MODE B: Content Search
            for root2, _, files2 in os.walk(skill_dir):
                for f2 in files2:
                    if f2.endswith((".md", ".json", ".txt", ".sh", ".py")):
                        try:
                            content = (Path(root2) / f2).read_text(encoding="utf-8")
                        except:
                            continue

                        # 1. Patterns: python script.py
                        py_calls = re.findall(
                            r"(?:python|python3)\s+((?:[a-zA-Z0-9_\-/\.]+)?\d{0,3}_?[a-zA-Z0-9_\-]+\.py)",
                            content,
                        )
                        for ref in py_calls:
                            refs_raw.add(ref)

                        # 2. Alias search
                        for alias in ALIASES.keys():
                            if re.search(rf"\b{alias}\b", content):
                                refs_raw.add(alias)

                        # 3. Soft name search in content
                        for p_norm, (fname, _) in physical_scripts.items():
                            if len(p_norm) > 5:
                                base = re.sub(r"^\d+_", "", fname).replace(".py", "")
                                if base in content and base.lower() != "script":
                                    refs_raw.add(fname)

            for raw_ref in refs_raw:
                edge_case = ""
                # Resolve reference
                if raw_ref in ALIASES:
                    script_name = ALIASES[raw_ref]
                    edge_case = f"Alias: {raw_ref} -> {script_name}"
                elif raw_ref in all_filenames:
                    script_name = raw_ref
                else:
                    file_name = Path(raw_ref).name
                    match = find_script_by_name(file_name)
                    if match:
                        script_name = match[0]
                        if script_name.lower() != file_name.lower():
                            edge_case = f"Matched: {file_name} -> {script_name}"
                    else:
                        script_name = file_name
                        edge_case = "Script No Encontrado"

                if script_name in all_filenames:
                    status = "✅ ACTIVE"
                    used_scripts.add(script_name)
                else:
                    status = "❌ MISSING"
                    skill_ghosts.add(skill_name)
                    if not edge_case:
                        edge_case = "Script No Encontrado"

                skill_mappings.append(
                    {
                        "profile": profile_name,
                        "skill": skill_name,
                        "script": script_name,
                        "status": status,
                        "edge": edge_case,
                    }
                )

# 3. Parse Cross-imports in Engine
cross_imports = []
for fname in all_filenames:
    # Find relative path
    rel_path = None
    for n, (f, p) in physical_scripts.items():
        if f == fname:
            rel_path = p
            break

    if not rel_path:
        continue

    try:
        content = (ROOT_DIR / rel_path).read_text(encoding="utf-8")
    except:
        continue

    py_calls = re.findall(
        r"(?:python|python3)\s+((?:[a-zA-Z0-9_\-/\.]+)?\d+[a-zA-Z0-9_\-]+\.py)", content
    )
    for ref in py_calls:
        f_ref = Path(ref).name
        match = find_script_by_name(f_ref)
        if match:
            s_called = match[0]
            used_scripts.add(s_called)
            cross_imports.append(
                {
                    "caller": fname,
                    "called": s_called,
                    "status": "✅ ACTIVE",
                    "type": "Subprocess",
                }
            )

# 4. Orphans
orphans = all_filenames - used_scripts

# 5. Build Markdown
md = f"""# 🗺️ BORRADOR MAPEO DEL SISTEMA: SKILLS ↔ SCRIPTS

> **Estado**: ✅ COMPLETO (Smarter Mapping v5.1)
> **Fecha**: 2026-03-21

Este documento identifica la conexión entre Skills y Scripts mediante comandos, alias y convenciones de nombres.

---

## 🎯 1. Criterios de Auditoría

1. **Mapping por Nomenclatura**: Vinculación automática por nombre (ej. `Morning_Standup` -> `14_Morning_Standup.py`).
2. **Búsqueda de Alias**: Resolución dinámica de alias (`gr`, `ce-commit`).
3. **Escaneo de Contenido**: Detección de nombres de scripts dentro de la documentación de Skills.
4. **Validación Física**: Comprobación de existencia real en `04_Engine`.

---

## 🔗 2. Mapeo Integral de Skills

### 2.1 Skills Ejecutoras (Operando Scripts OS)
> Skills con vinculación confirmada al motor central.

| Perfil de Skill | Nombre de la Skill | Script Invocado | Estado | Nota / Edge Case |
|-----------------|-------------------|-----------------|--------|------------------|
"""

seen_maps = set()
for m in sorted(skill_mappings, key=lambda x: (x["profile"], x["skill"])):
    if m["status"] != "✅ ACTIVE":
        continue
    id_str = f"{m['profile']}|{m['skill']}|{m['script']}"
    if id_str in seen_maps:
        continue
    seen_maps.add(id_str)
    md += f"| `{m['profile']}` | `{m['skill']}` | `{m['script']}` | `{m['status']}` | `{m['edge']}` |\n"

md += """
### 2.2 Referencias Externas / Sin Mapeo Core
> Skills con menciones a scripts que no residen en `04_Engine`.

| Perfil de Skill | Nombre de la Skill | Referencia | Estado | Detalle |
|-----------------|-------------------|------------|--------|---------|
"""

for m in sorted(skill_mappings, key=lambda x: (x["profile"], x["skill"])):
    if m["status"] == "✅ ACTIVE":
        continue
    id_str = f"{m['profile']}|{m['skill']}|{m['script']}"
    if id_str in seen_maps:
        continue
    seen_maps.add(id_str)
    md += f"| `{m['profile']}` | `{m['skill']}` | `{m['script']}` | `{m['status']}` | `{m['edge']}` |\n"

md += """
---

## 🛠️ 3. Dependencias Internas de Scripts (Cross-Calls)

| Script Padre | Script Invocado | Tipo | Estado |
|--------------|-----------------|------|--------|
"""
seen_cross = set()
for c in cross_imports:
    id_str = f"{c['caller']}|{c['called']}"
    if id_str in seen_cross:
        continue
    seen_cross.add(id_str)
    md += f"| `{c['caller']}` | `{c['called']}` | `{c['type']}` | `{c['status']}` |\n"

md += """
---

## 👻 4. Scripts Huérfanos (04_Engine)

Scripts físicos sin invocaciones detectadas desde Skills.

| Nombre del Script | Ruta | Categoría Sugerida |
|-------------------|------|--------------------|
"""
for s in sorted(list(orphans)):
    # Find relative path
    rel = "04_Engine/..."
    for n, (f, p) in physical_scripts.items():
        if f == s:
            rel = str(p)
            break
    md += f"| `{s}` | `{rel}` | `Standalone/Core` |\n"

md += """
---

## ⚙️ 5. Protocolo de Pruebas (Validación Funcional)

> **⚠️ PENDIENTE DE APROBACIÓN ("GO") DEL USUARIO**

---
*Generado por PersonalOS AI - Mapeo v5.1*
"""

BORRADOR_PATH.write_text(md, encoding="utf-8")
REPORTE_PATH.parent.mkdir(parents=True, exist_ok=True)
REPORTE_PATH.write_text(md, encoding="utf-8")
print("✅ Mapeo v5.1 completado.")
