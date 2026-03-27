"""
27_Resumen_Extractor.py - Resumen Document Extractor
==================================================
Extrae contenido de documentos específicos para crear resúmenes estructurados.
Procesa directorios completos recursivamente.

Uso:
    python 27_Resumen_Extractor.py
    python 27_Resumen_Extractor.py --source ./documentos --output ./resumen.md

Skills relacionadas:
    Skill 31: Universal Doc Reader Elite
    Skill 32: Batch Doc Processor Elite
"""

import os
import sys
import io
import subprocess
import argparse
from pathlib import Path
from datetime import datetime
from typing import List

# UTF-8 encoding fix for Windows
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
if sys.stderr.encoding != "utf-8":
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

# =============================================================================
# CONFIG PATHS
# =============================================================================
try:
    sys.path.insert(0, str(Path(__file__).parent))
    from config_paths import ROOT_DIR, KNOWLEDGE_DIR
except ImportError:
    ROOT_DIR = Path(__file__).resolve().parent.parent.parent
    KNOWLEDGE_DIR = ROOT_DIR / "03_Knowledge"

# =============================================================================
# CONSTANTES
# =============================================================================
SCRIPT_NAME = "85_Resumen_Extractor.py"
SCRIPT_VERSION = "v2.0"

SUPPORTED_EXTENSIONS = (".pdf", ".docx", ".xlsx", ".xls", ".csv", ".pptx")

# =============================================================================
# BRANDING
# =============================================================================
try:
    from colorama import init, Fore

    init(autoreset=True)
    INFO = Fore.CYAN
    SUCCESS = Fore.GREEN
    WARNING = Fore.YELLOW
    RESET = Fore.RESET
except ImportError:
    INFO = WARNING = SUCCESS = RESET = ""


def print_branding():
    print("─" * 60)
    print(f"  📄 PersonalOS | {SCRIPT_NAME} {SCRIPT_VERSION}")
    print(f"  📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("─" * 60)


# =============================================================================
# CORE
# =============================================================================


def find_parser_script() -> Path:
    """Ubica 83_Universal_Parser.py."""
    script_dir = Path(__file__).parent
    parser_path = script_dir / "83_Universal_Parser.py"

    if parser_path.exists():
        return parser_path

    alt_path = ROOT_DIR / "04_Engine" / "08_Scripts_Os" / "83_Universal_Parser.py"
    if alt_path.exists():
        return alt_path

    print(f"ERROR: 83_Universal_Parser.py no encontrado")
    sys.exit(1)


def scan_documents(directory: Path) -> List[Path]:
    """Escanea directorio por documentos."""
    files = []
    for root, _, filenames in os.walk(directory):
        for fname in filenames:
            if fname.lower().endswith(SUPPORTED_EXTENSIONS):
                files.append(Path(root) / fname)
    return sorted(files)


def run_parser(parser_script: Path, file_path: Path, output_file: Path):
    """Ejecuta parser para un archivo."""
    try:
        result = subprocess.run(
            [sys.executable, str(parser_script), str(file_path)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=120,
        )

        with open(output_file, "a", encoding="utf-8") as f:
            f.write("\n\n")
            f.write("═" * 50 + "\n")
            f.write(f"📄 FILE: {file_path.name}\n")
            f.write(f"📂 PATH: {file_path}\n")
            f.write("═" * 50 + "\n\n")
            f.write(result.stdout)
            if result.stderr:
                f.write(f"\n⚠️ STDERR:\n{result.stderr}")

        print(f"{INFO}  ✓ {file_path.name}{RESET}")
        return True

    except subprocess.TimeoutExpired:
        print(f"{WARNING}  ⏱ Timeout: {file_path.name}{RESET}")
        return False
    except Exception as e:
        print(f"  ✗ Error: {file_path.name}: {e}")
        return False


def generate_header(output_path: Path, source_dir: Path, files: List[Path]):
    """Genera header del reporte."""
    header = f"""# 📚 Resumen Document Extraction Report

> **Generado:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
> **Fuente:** `{source_dir}`
> **Archivos:** {len(files)}

---

"""
    output_path.write_text(header, encoding="utf-8")


# =============================================================================
# MAIN
# =============================================================================


def main():
    parser = argparse.ArgumentParser(
        description=f"PersonalOS - {SCRIPT_NAME}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python 85_Resumen_Extractor.py
  python 85_Resumen_Extractor.py --source ./documentos --output resumen.md
        """,
    )
    parser.add_argument(
        "--source", "-s", help="Directorio fuente (default: ./docs)", default="./docs"
    )
    parser.add_argument(
        "--output", "-o", help="Archivo de salida (default: auto)", default=None
    )

    args = parser.parse_args()

    # Paths
    source_dir = Path(args.source).resolve()
    if not source_dir.exists():
        source_dir = ROOT_DIR / "docs"

    if not source_dir.exists():
        print(f"ERROR: Directorio no encontrado: {source_dir}")
        sys.exit(1)

    if args.output:
        output_path = Path(args.output).resolve()
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = KNOWLEDGE_DIR / f"Resumen_Extraction_{timestamp}.md"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Branding
    print_branding()
    print(f"  📂 Fuente: {source_dir}")
    print(f"  📄 Salida: {output_path}")
    print()

    # Escanear
    files = scan_documents(source_dir)
    if not files:
        print(f"  ⚠️ No se encontraron documentos")
        sys.exit(0)

    print(f"  📊 Archivos encontrados: {len(files)}")
    print()

    # Header
    generate_header(output_path, source_dir, files)

    # Procesar
    parser_script = find_parser_script()
    processed = sum(run_parser(parser_script, f, output_path) for f in files)

    # Resumen
    print()
    print("─" * 60)
    print(f"  ✅ Procesados: {processed}/{len(files)}")
    print(f"  📄 Reporte: {output_path}")
    print("─" * 60)


if __name__ == "__main__":
    main()
