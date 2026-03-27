# -*- coding: utf-8 -*-
"""
System Guardian v2.0 - Validador y Actualizador de Documentacion PersonalOS
==========================================================================


FUNCIONALIDADES:
  [1]  Estructura Validation  - Verifica que carpetas 00-07 existan
  [2]  Naming Convention     - Valida formato XX_Nombre.md/.py
  [3]  Index Generator      - Genera/actualiza README.md en cada carpeta
  [4]  Orphan Detection     - Encuentra archivos sin numerar
  [5]  Broken Links         - Detecta refs a rutas que no existen
  [6]  Ghost Files          - Archivos en INDEX que no existen
  [7]  Auto-Fix             - Corrige issues menores automaticamente
  [8]  Report               - Genera reporte de cambios

USO:
    python 79_System_Guardian.py          # Dry-run (solo reporte)
    python 79_System_Guardian.py --apply  # Aplica fixes automaticamente
    python 79_System_Guardian.py --no-beautify  # Skip beautify (rapido)
    python 79_System_Guardian.py --beautify-only  # Solo beautify

REPORTE: Se guarda en 04_Engine/06_Reports/guardian_YYYY-MM-DD_HHMMSS.md
"""

import sys
import os
import re
import datetime
from pathlib import Path
from typing import List, Tuple, Optional
from dataclasses import dataclass, field

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import PROJECT_ROOT

SCRIPT_DIR = Path(__file__).resolve().parent

# =============================================================================
# VOICE OUTPUT (ASCII-only, Windows TTS compatible)
# =============================================================================
# VOICE OUTPUT (ASCII-only, Windows TTS compatible)
# =============================================================================


def dynamic_speak(text: str):
    """Voz ASCII-only para System Guardian."""
    print(f"[VOICE] {text}")


# =============================================================================
# CONSTANTES
# =============================================================================

EXPECTED_DIMENSIONS = [
    "00_Core",
    "01_Brain",
    "02_Operations",
    "03_Knowledge",
    "04_Engine",
    "05_System",
    "06_Archive",
    "07_Projects",
]

NAMING_PATTERN = re.compile(r"^\d{2,3}_[A-Z][a-zA-Z0-9_]*\.(?:md|py)$")

VALID_EXTENSIONS = {".md", ".py", ".txt", ".json", ".yaml", ".yml", ".sh"}

EXCLUDED_DIRS = {
    ".git",
    "__pycache__",
    "node_modules",
    ".venv",
    "venv",
    ".cursor",
    ".agent",
    ".vscode",
    ".claude",
    "05_GGA",
    "06_History",
    ".mcp",
    ".pytest_cache",
}

EXCLUDED_FILES = {
    "README.md",
    "CLAUDE.md",
    "LICENSE",
    ".gitignore",
    "package.json",
    "package-lock.json",
    "AGENTS.md",
    "GOALS.md",
    "BACKLOG.md",
    "PROGRESS.md",
    "SLASH_COMMANDS.md",
    "tree.txt",
}

REPORTS_DIR = PROJECT_ROOT / "04_Engine" / "06_Reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

BEAUTIFY_SCRIPT = SCRIPT_DIR / "35_Beautify_Tables.py"

# =============================================================================
# DATA CLASSES
# =============================================================================


@dataclass
class ValidationResult:
    step: int
    name: str
    status: str  # PASS, FAIL, WARN, SKIP
    message: str = ""
    details: List[str] = field(default_factory=list)
    fixes_applied: int = 0

    def __str__(self) -> str:
        icon = {
            "PASS": "[OK]",
            "FAIL": "[X]",
            "WARN": "[WARN]",
            "SKIP": "[SKIP]",
            "RUN": "[RUN]",
        }.get(self.status, "[?]")
        msg = f"[{self.step}/8] {icon} {self.name}"
        if self.message:
            msg += f": {self.message}"
        return msg


@dataclass
class GuardianReport:
    timestamp: str = ""
    results: List[ValidationResult] = field(default_factory=list)
    orphans: List[str] = field(default_factory=list)
    broken_links: List[str] = field(default_factory=list)
    ghost_files: List[str] = field(default_factory=list)
    naming_issues: List[str] = field(default_factory=list)
    auto_fixes: List[str] = field(default_factory=list)

    def add_result(self, result: ValidationResult):
        self.results.append(result)


# =============================================================================
# UTILIDADES - SIN EMOJIS, SOLO ASCII
# =============================================================================


def print_step(step: int, status: str, name: str, detail: str = ""):
    icon = {
        "PASS": "[OK]",
        "FAIL": "[X]",
        "WARN": "[WARN]",
        "SKIP": "[SKIP]",
        "RUN": "[RUN]",
    }.get(status, "[?]")
    msg = f"[{step}/8] {icon} {name}"
    if detail:
        msg += f": {detail}"
    print(msg)


def print_substep(msg: str):
    print(f"      |-- {msg}")


def read_file(path: Path) -> Optional[str]:
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        return None


def write_file(path: Path, content: str) -> bool:
    try:
        path.write_text(content, encoding="utf-8")
        return True
    except Exception:
        return False


def to_relative(target: Path) -> str:
    """Convierte ruta a relativa respect al PROJECT_ROOT."""
    try:
        return str(target.relative_to(PROJECT_ROOT))
    except ValueError:
        return str(target)


def safe_walk(
    root: Path, max_depth: int = 5
) -> List[Tuple[Path, List[str], List[str]]]:
    """Walk seguro que evita recursion infinita y symlinks."""
    results = []
    exclude_dirs = EXCLUDED_DIRS

    for dirpath, dirnames, filenames in os.walk(str(root)):
        p_dir = Path(dirpath)
        depth = dirpath[len(str(root)) :].count(os.sep)

        if depth >= max_depth:
            dirnames.clear()
            continue

        # Filtrar dirnames IN-PLACE para evitar explorar symlinks/excluidos
        dirnames[:] = [
            d
            for d in dirnames
            if d not in exclude_dirs
            and not d.startswith(".")
            and not os.path.islink(os.path.join(dirpath, d))
        ]

        results.append((p_dir, dirnames, filenames))

    return results


def extract_file_links(content: str) -> List[str]:
    """Extrae links internos del proyecto desde contenido markdown."""
    links = []
    for match in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content):
        link = match[1].strip()
        # Skip URLs externos y anchors
        if link.startswith(("http://", "https://", "mailto:", "git@", "#")):
            continue
        # Skip rutas absolutas fuera del proyecto (Regla 22)
        if re.match(r"^[A-Za-z]:[/\\]", link):
            continue
        links.append(link)
    return links


# =============================================================================
# PASO 1: ESTRUCTURA VALIDATION
# =============================================================================


def validate_structure() -> ValidationResult:
    print_step(1, "RUN", "Estructura Validation")

    missing = []
    for dim in EXPECTED_DIMENSIONS:
        path = PROJECT_ROOT / dim
        if path.exists():
            print_substep(f"[OK] {dim}")
        else:
            missing.append(dim)
            print_substep(f"[X] Falta: {dim}")

    status = "FAIL" if missing else "PASS"
    message = f"{len(missing)} carpetas faltantes" if missing else "8/8 carpetas OK"

    return ValidationResult(
        step=1,
        name="Estructura Validation",
        status=status,
        message=message,
        details=missing,
    )


# =============================================================================
# PASO 2: NAMING CONVENTION
# =============================================================================


def validate_naming(apply: bool = False) -> Tuple[ValidationResult, List[str]]:
    print_step(2, "RUN", "Naming Convention")

    issues: List[str] = []
    fixes_applied = 0

    for dim in EXPECTED_DIMENSIONS:
        dim_path = PROJECT_ROOT / dim
        if not dim_path.exists():
            continue

        for walk_dir, subdirs, files in safe_walk(dim_path, max_depth=3):
            for filename in files:
                file_path = walk_dir / filename

                # Skip excluded
                if filename in EXCLUDED_FILES:
                    continue
                if file_path.suffix not in VALID_EXTENSIONS:
                    continue

                # Solo archivos en carpetas principales (profundidad <= 2)
                rel = to_relative(file_path)
                depth = rel.count(os.sep)

                if depth > 3:
                    continue

                # Skip archivos en subcarpetas profundas
                parts = rel.split(os.sep)
                if len(parts) > 4:
                    continue

                # SCOPE: Solo validar naming en 04_Engine/08_Scripts_Os/ (motor scripts)
                if "04_Engine/08_Scripts_Os/" not in rel:
                    continue

                if not NAMING_PATTERN.match(filename):
                    issues.append(rel)
                    print_substep(f"[WARN] {rel}")

                    if apply:
                        new_name = f"XX_{Path(filename).stem}{file_path.suffix}"
                        new_path = file_path.parent / new_name
                        if not new_path.exists():
                            try:
                                file_path.rename(new_path)
                                fixes_applied += 1
                                print_substep(f"[FIX] -> {new_name}")
                            except OSError:
                                pass

    status = "FAIL" if issues else "PASS"
    message = f"{len(issues)} issues" if issues else "100% compliant"

    result = ValidationResult(
        step=2,
        name="Naming Convention",
        status=status,
        message=message,
        details=issues,
        fixes_applied=fixes_applied,
    )
    return result, issues


# =============================================================================
# PASO 3: INDEX GENERATOR
# =============================================================================


def generate_indexes() -> ValidationResult:
    print_step(3, "RUN", "Index Generator")

    updated = 0

    for dim in EXPECTED_DIMENSIONS:
        dim_path = PROJECT_ROOT / dim
        if not dim_path.exists():
            continue

        readme_path = dim_path / "README.md"

        # Recopilar archivos numerados
        items = []
        for item in sorted(dim_path.iterdir()):
            if item.name in {".git", "__pycache__", "README.md"}:
                continue
            if item.is_file() and item.suffix in {".md", ".py"}:
                if re.match(r"^\d{2,3}_", item.name):
                    items.append(item)

        # Generar contenido
        content = f"# {dim}\n\n"
        content += f"> **Total items:** {len(items)}\n"
        content += (
            f"> **Last Updated:** {datetime.datetime.now().strftime('%Y-%m-%d')}\n\n"
        )

        if items:
            content += "## Items\n\n"
            content += "| # | Name | Type |\n"
            content += "|---|------|------|\n"
            for i, item in enumerate(items, 1):
                content += f"| {i} | {item.stem} | {item.suffix[1:].upper()} |\n"
        else:
            content += "_No items yet._\n"

        # Escribir solo si cambio
        if readme_path.exists():
            existing = read_file(readme_path)
            if existing and existing.strip() != content.strip():
                write_file(readme_path, content)
                updated += 1
                print_substep(f"[X] Actualizado: {dim}/README.md")
        else:
            write_file(readme_path, content)
            updated += 1
            print_substep(f"[NEW] Creado: {dim}/README.md")

    status = "WARN" if updated else "PASS"
    message = f"{updated} indexes actualizados" if updated else "Todos al dia"

    return ValidationResult(
        step=3,
        name="Index Generator",
        status=status,
        message=message,
        fixes_applied=updated,
    )


# =============================================================================
# PASO 4: ORPHAN DETECTION
# =============================================================================


def detect_orphans() -> Tuple[ValidationResult, List[str]]:
    print_step(4, "RUN", "Orphan Detection")

    orphans: List[str] = []

    for dim in EXPECTED_DIMENSIONS:
        dim_path = PROJECT_ROOT / dim
        if not dim_path.exists():
            continue

        for item in dim_path.iterdir():
            if item.is_file() and item.suffix in {".md", ".py"}:
                if item.name.upper() == "README.MD":
                    continue
                if re.match(r"^\d{2,3}_", item.name):
                    continue
                orphans.append(to_relative(item))
                print_substep(f"[ORPHAN] {to_relative(item)}")

    status = "WARN" if orphans else "PASS"
    message = f"{len(orphans)} archivos sin numerar" if orphans else "Sin orphans"

    return ValidationResult(
        step=4, name="Orphan Detection", status=status, message=message, details=orphans
    ), orphans


# =============================================================================
# PASO 5: BROKEN LINKS
# =============================================================================


def detect_broken_links() -> Tuple[ValidationResult, List[str]]:
    print_step(5, "RUN", "Broken Links")

    broken: List[str] = []

    for dim in EXPECTED_DIMENSIONS:
        dim_path = PROJECT_ROOT / dim
        if not dim_path.exists():
            continue

        for walk_dir, _, filenames in safe_walk(dim_path, max_depth=4):
            for filename in filenames:
                if not (filename.endswith(".md") and filename != "README.md"):
                    continue

                md_file = walk_dir / filename
                content = read_file(md_file)
                if not content:
                    continue

                for link in extract_file_links(content):
                    if not link.strip():
                        continue
                    if link.startswith(("http://", "https://", "mailto:", "git@")):
                        continue

                    # Normalize and resolve
                    link = link.replace("\\", "/")
                    if "#" in link:
                        link = link.split("#")[0]

                    if link.startswith("/"):
                        target = PROJECT_ROOT / link.lstrip("/")
                    else:
                        target = md_file.parent / link

                    if target.is_symlink():
                        continue

                    if not target.exists():
                        broken.append(
                            f"{to_relative(md_file)} -> {to_relative(target)}"
                        )
                        print_substep(
                            f"[BROKEN] {md_file.name} -> {to_relative(target)}"
                        )

    status = "WARN" if broken else "PASS"
    message = f"{len(broken)} links rotos" if broken else "Sin links rotos"

    return ValidationResult(
        step=5, name="Broken Links", status=status, message=message, details=broken
    ), broken


# =============================================================================
# PASO 6: GHOST FILES
# =============================================================================


def detect_ghost_files() -> Tuple[ValidationResult, List[str]]:
    print_step(6, "RUN", "Ghost Files")

    ghosts: List[str] = []

    for dim in EXPECTED_DIMENSIONS:
        dim_path = PROJECT_ROOT / dim
        if not dim_path.exists():
            continue

        readme_path = dim_path / "README.md"
        if not readme_path.exists():
            continue

        content = read_file(readme_path)
        if not content:
            continue

        for match in re.findall(r"(\d{2,3}_\w+\.(?:md|py))", content):
            file_path = dim_path / match
            if not file_path.exists():
                ghosts.append(to_relative(file_path))
                print_substep(f"[GHOST] {match} (referenciado pero no existe)")

    status = "WARN" if ghosts else "PASS"
    message = f"{len(ghosts)} ghost files" if ghosts else "Sin ghosts"

    return ValidationResult(
        step=6, name="Ghost Files", status=status, message=message, details=ghosts
    ), ghosts


# =============================================================================
# PASO 7: AUTO-FIX
# =============================================================================


def auto_fix(report: GuardianReport, apply: bool) -> ValidationResult:
    print_step(7, "RUN", "Auto-Fix")

    fixes: List[str] = []

    if not apply:
        print_substep("Modo dry-run: simulando fixes...")
        return ValidationResult(
            step=7,
            name="Auto-Fix",
            status="WARN",
            message=f"{len(report.naming_issues)} fixes simulados (use --apply)",
            details=[f"Simulated: {i}" for i in report.naming_issues[:5]],
        )

    # Archivar orphans
    for orphan in report.orphans:
        orphan_path = PROJECT_ROOT / orphan
        if orphan_path.exists():
            archive_dir = PROJECT_ROOT / "06_Archive" / "05_Tasks_Archive"
            archive_dir.mkdir(parents=True, exist_ok=True)
            backup_path = archive_dir / orphan_path.name
            try:
                orphan_path.rename(backup_path)
                fixes.append(f"Archivado: {orphan}")
                print_substep(f"[FIX] Archivado: {orphan}")
            except OSError:
                pass

    status = "PASS" if fixes else "SKIP"
    message = f"{len(fixes)} fixes aplicados" if fixes else "Sin fixes necesarios"

    return ValidationResult(
        step=7,
        name="Auto-Fix",
        status=status,
        message=message,
        details=fixes,
        fixes_applied=len(fixes),
    )


# =============================================================================
# PASO 8: REPORT
# =============================================================================


def generate_report(report: GuardianReport, apply: bool) -> ValidationResult:
    print_step(8, "RUN", "Report Generation")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")
    report_path = REPORTS_DIR / f"guardian_{timestamp}.md"

    content = f"""# System Guardian Report

**Generated:** {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
**Mode:** {"APPLY" if apply else "DRY-RUN"}
**Project:** {PROJECT_ROOT.name}

---

## Summary

| Metric | Value |
|--------|-------|
| Steps Completed | {len(report.results)} |
| Naming Issues | {len(report.naming_issues)} |
| Orphan Files | {len(report.orphans)} |
| Broken Links | {len(report.broken_links)} |
| Ghost Files | {len(report.ghost_files)} |
| Auto-Fixes | {sum(r.fixes_applied for r in report.results)} |

---

## Step Results

"""

    for result in report.results:
        content += f"### Step {result.step}: {result.name}\n\n"
        content += f"**Status:** {result.status}\n"
        content += f"**Message:** {result.message}\n"
        if result.details:
            content += f"\n**Details:**\n"
            for detail in result.details[:20]:  # Limitar a 20 para no inflar el reporte
                content += f"- `{detail}`\n"
            if len(result.details) > 20:
                content += f"- ... and {len(result.details) - 20} more\n"
        content += "\n"

    write_file(report_path, content)
    print_substep(f"[FILE] Guardado: {to_relative(report_path)}")

    # Also save latest
    latest_path = REPORTS_DIR / "guardian_latest.md"
    write_file(latest_path, content)

    return ValidationResult(
        step=8,
        name="Report Generation",
        status="PASS",
        message=f"Guardado en {report_path.name}",
    )


# =============================================================================
# OPTIONAL: BEAUTIFY (import directo, no subprocess)
# =============================================================================


def run_beautify() -> int:
    """Corre beautify en todos los MD usando import directo (rapido)."""
    print_step(9 if "--beautify-only" in sys.argv else 0, "RUN", "Beautify Tables")

    if not BEAUTIFY_SCRIPT.exists():
        print_substep("[WARN]  Script beautify no encontrado")
        return 0

    # Importar beautify como modulo (evita subprocess overhead)
    import importlib.util

    spec = importlib.util.spec_from_file_location("beautify", BEAUTIFY_SCRIPT)
    if spec is None or spec.loader is None:
        print_substep("[WARN]  No se pudo cargar beautify")
        return 0

    # Ejecutar beautify directamente (una sola vez)
    try:
        spec.loader.exec_module(beautify_module)
    except Exception as e:
        print_substep(f"[WARN] Error al inicializar beautify: {e}")
        return 0

    beautified = 0
    total = 0

    for dim in EXPECTED_DIMENSIONS:
        dim_path = PROJECT_ROOT / dim
        if not dim_path.exists():
            continue

        for md_file in dim_path.rglob("*.md"):
            total += 1
            if md_file.name == "README.md":
                continue

            try:
                # Usar la función ya cargada
                result = beautify_module.beautify_file(str(md_file))
                if result:
                    beautified += 1
                    print_substep(f"[OK] {to_relative(md_file)}")
            except Exception:
                # Si no tiene la funcion, skipear
                pass

    print_substep(f"Beautified: {beautified}/{total} archivos")
    return beautified


# =============================================================================
# MAIN
# =============================================================================


def print_banner():
    banner = r"""
###########################################################################
#                                                                         #
#     _____  ______ _____   _____  ____  _   _          _        ____    #
#    |  __ \|  ____|  __ \ / ____|/ __ \| \ | |   /\   | |      / __ \   #
#    | |__) | |__  | |__) | (___ | |  | |  \| |  /  \  | |     | |  | |  #
#    |  ___/|  __| |  _  / \___ \| |  | | . ` | / /\ \ | |     | |  | |  #
#    | |    | |____| | \ \ ____) | |__| | |\  |/ ____ \| |____ | |__| |  #
#    |_|    |______|_|  \_\_____/ \____/|_| \_/_/    \_\______| \____/   #
#                                                                         #
#                  S Y S T E M   G U A R D I A N   v 2 . 0               #
###########################################################################
"""
    print(banner)


def main():
    print_banner()
    print()

    dynamic_speak("Iniciando System Guardian")

    # Parse args
    apply = "--apply" in sys.argv
    no_beautify = "--no-beautify" in sys.argv
    beautify_only = "--beautify-only" in sys.argv

    if apply:
        print("[MODE] APLICAR fixes")
    else:
        print("[MODE] DRY-RUN (simulacion)")
    if no_beautify:
        print("[MODE] SKIP beautify")
    print()

    # Crear reporte
    report = GuardianReport(timestamp=datetime.datetime.now().isoformat())

    # =========================================================================
    # PASOS 1-8 (excepto si es beautify-only)
    # =========================================================================
    if not beautify_only:
        # Paso 1
        result = validate_structure()
        report.add_result(result)

        # Paso 2
        result, naming_issues = validate_naming(apply)
        report.add_result(result)
        report.naming_issues = naming_issues

        # Paso 3
        result = generate_indexes()
        report.add_result(result)

        # Paso 4
        result, orphans = detect_orphans()
        report.add_result(result)
        report.orphans = orphans

        # Paso 5
        result, broken_links = detect_broken_links()
        report.add_result(result)
        report.broken_links = broken_links

        # Paso 6
        result, ghost_files = detect_ghost_files()
        report.add_result(result)
        report.ghost_files = ghost_files

        # Paso 7
        result = auto_fix(report, apply)
        report.add_result(result)
        report.auto_fixes = result.details

        # Paso 8
        result = generate_report(report, apply)
        report.add_result(result)

    # =========================================================================
    # BEAUTIFY (opcional, solo si no es beautify-only y no es no-beautify)
    # =========================================================================
    if not no_beautify and not beautify_only:
        print()
        run_beautify()

    if beautify_only:
        run_beautify()

    # =========================================================================
    # RESUMEN FINAL
    # =========================================================================
    print()
    print("=" * 70)
    print("  RESUMEN FINAL - SYSTEM GUARDIAN")
    print("=" * 70)

    for result in report.results:
        print(result)

    print()
    print(
        f"[FILE] Reporte guardado en: {to_relative(REPORTS_DIR / 'guardian_latest.md')}"
    )
    print("=" * 70)

    dynamic_speak("System Guardian finalizado")


if __name__ == "__main__":
    main()
