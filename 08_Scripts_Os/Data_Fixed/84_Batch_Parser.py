import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
"""
26_Batch_Parser.py - Batch Doc Processor Elite
============================================
Procesa masivamente directorios completos de documentos.
Utiliza 25_Universal_Parser.py para cada archivo.

Uso:
    python 26_Batch_Parser.py ./documentos/
    python 26_Batch_Parser.py ./documentos/ --recursive --output reporte.md

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
from typing import List, Optional

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
SCRIPT_NAME = "84_Batch_Parser.py"
SCRIPT_VERSION = "v2.0"
SKILL_ID = "32"
SKILL_NAME = "Batch Doc Processor Elite"

SUPPORTED_EXTENSIONS = (
    ".pdf",
    ".docx",
    ".doc",
    ".xlsx",
    ".xls",
    ".csv",
    ".pptx",
    ".psd",
    ".psb",
    ".tiff",
    ".tif",
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".md",
    ".txt",
)

# =============================================================================
# BRANDING & COLORS
# =============================================================================
try:
    from colorama import init, Fore

    init(autoreset=True)
    INFO = Fore.CYAN
    SUCCESS = Fore.GREEN
    WARNING = Fore.YELLOW
    ERROR = Fore.RED
    RESET = Fore.RESET
except ImportError:
    INFO = WARNING = SUCCESS = ERROR = RESET = ""


def print_branding():
    """Header premium del script."""
    print("─" * 60)
    print(f"  🦾 PersonalOS | Skill {SKILL_ID}: {SKILL_NAME}")
    print(f"  ⚡ {SCRIPT_NAME} {SCRIPT_VERSION}")
    print("─" * 60)
    print(f"  📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  📂 Root: {ROOT_DIR}")
    print("─" * 60)
    print()


def print_info(msg: str):
    print(f"{INFO}  ℹ️  {msg}{RESET}")


def print_success(msg: str):
    print(f"{SUCCESS}  ✅ {msg}{RESET}")


def print_error(msg: str):
    print(f"{ERROR}  ❌ {msg}{RESET}", file=sys.stderr)


def print_warning(msg: str):
    print(f"{WARNING}  ⚠️  {msg}{RESET}")


# =============================================================================
# CORE LOGIC
# =============================================================================


def find_parser_script() -> Path:
    """Ubica 83_Universal_Parser.py."""
    script_dir = Path(__file__).parent
    parser_path = script_dir / "83_Universal_Parser.py"

    if parser_path.exists():
        return parser_path

    # Fallback: buscar en otros locations
    alt_paths = [
        ROOT_DIR / "83_Universal_Parser.py",
        ROOT_DIR / "04_Engine" / "08_Scripts_Os" / "83_Universal_Parser.py",
    ]
    for alt in alt_paths:
        if alt.exists():
            return alt

    print_error(f"83_Universal_Parser.py no encontrado")
    sys.exit(1)


def scan_files(directory: Path, recursive: bool) -> List[Path]:
    """Escanea directorio por archivos soportados."""
    files = []

    if recursive:
        for root, _, filenames in os.walk(directory):
            for fname in filenames:
                if fname.lower().endswith(SUPPORTED_EXTENSIONS):
                    files.append(Path(root) / fname)
    else:
        for fname in os.listdir(directory):
            fpath = directory / fname
            if fpath.is_file() and fname.lower().endswith(SUPPORTED_EXTENSIONS):
                files.append(fpath)

    return sorted(files)


def process_file(parser_script: Path, file_path: Path, output_file: Path) -> bool:
    """Procesa un archivo individual."""
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
            f.write("═" * 60 + "\n")
            f.write(f"📄 FILE: {file_path.name}\n")
            f.write(f"📂 PATH: {file_path}\n")
            f.write(f"📦 SIZE: {file_path.stat().st_size:,} bytes\n")
            f.write("═" * 60 + "\n\n")
            f.write(result.stdout)
            if result.stderr:
                f.write(f"\n⚠️ STDERR:\n{result.stderr}")
        return True

    except subprocess.TimeoutExpired:
        print_warning(f"Timeout: {file_path.name}")
        return False
    except Exception as e:
        print_error(f"Error procesando {file_path.name}: {e}")
        return False


def generate_header(
    output_path: Path, source_dir: Path, recursive: bool, files: List[Path]
):
    """Genera header del reporte."""
    header = f"""# 📚 Batch Extraction Report

| Propiedad | Valor |
|----------|-------|
| **Fecha** | {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} |
| **Fuente** | `{source_dir}` |
| **Recursivo** | {"Sí" if recursive else "No"} |
| **Archivos detectados** | {len(files)} |

---

"""
    output_path.write_text(header, encoding="utf-8")


# =============================================================================
# MAIN
# =============================================================================


def main():
    parser = argparse.ArgumentParser(
        description=f"PersonalOS Skill {SKILL_ID} - {SKILL_NAME}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos:
  python 84_Batch_Parser.py ./documentos/
  python 84_Batch_Parser.py ./documentos/ --recursive
  python 84_Batch_Parser.py ./documentos/ -o mi_reporte.md
        """,
    )
    parser.add_argument("input_dir", help="Directorio raíz para buscar archivos")
    parser.add_argument(
        "--output",
        "-o",
        help="Archivo de salida (default: auto-generated)",
        default=None,
    )
    parser.add_argument(
        "--recursive",
        "-r",
        action="store_true",
        help="Buscar recursivamente en subdirectorios",
    )

    args = parser.parse_args()

    # Validar directorio
    source_dir = Path(args.input_dir).resolve()
    if not source_dir.exists():
        print_error(f"Directorio no encontrado: {source_dir}")
        sys.exit(1)
    if not source_dir.is_dir():
        print_error(f"No es un directorio: {source_dir}")
        sys.exit(1)

    # Output path
    if args.output:
        output_path = Path(args.output).resolve()
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = KNOWLEDGE_DIR / f"Batch_Extraction_{timestamp}.md"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Branding
    print_branding()
    print_info(f"Directorio: {source_dir}")
    print_info(f"Salida: {output_path}")
    print_info(f"Recursivo: {'Sí' if args.recursive else 'No'}")
    print()

    # Escanear archivos
    files = scan_files(source_dir, args.recursive)
    if not files:
        print_warning("No se encontraron archivos soportados")
        print_info(f"Formatos: {', '.join(SUPPORTED_EXTENSIONS)}")
        sys.exit(0)

    print_info(f"Archivos encontrados: {len(files)}")
    print()

    # Generar header
    generate_header(output_path, source_dir, args.recursive, files)

    # Procesar
    parser_script = find_parser_script()
    processed = 0
    errors = 0

    for i, file_path in enumerate(files, 1):
        print_info(f"[{i}/{len(files)}] {file_path.name}")
        if process_file(parser_script, file_path, output_path):
            processed += 1
        else:
            errors += 1

    # Resumen
    print()
    print("─" * 60)
    print(f"  📊 Resumen:")
    print(f"     Procesados: {processed}/{len(files)}")
    if errors:
        print(f"     Errores: {errors}")
    print(f"     Salida: {output_path}")
    print("─" * 60)
    print_success("Procesamiento batch completo")

    # Guardar metadata
    meta_path = output_path.with_suffix(".meta.json")
    meta_content = {
        "source_dir": str(source_dir),
        "output": str(output_path),
        "recursive": args.recursive,
        "files_count": len(files),
        "processed": processed,
        "errors": errors,
        "timestamp": datetime.now().isoformat(),
    }
    import json

    meta_path.write_text(json.dumps(meta_content, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
