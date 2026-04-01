from config_paths import ROOT_DIR as BASE_DIR
import re
import hashlib
import importlib.util
import os
from typing import List, Generator

# --- CONFIGURACIÓN ARMOR LAYER ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
# BASE_DIR = os.path.dirname(SCRIPT_DIR)  # Era 04_Engine
# Necesitamos llegar al raíz del proyecto (2 niveles arriba de 08_Scripts_Os)
BASE_DIR = os.path.dirname(os.path.dirname(SCRIPT_DIR))


def speak(text: str) -> None:
    """Interfaz de voz integrada."""
    try:
        common_path = os.path.join(
            BASE_DIR, ".agent", "04_Extensions", "hooks", "utils", "common.py"
        )
        if os.path.exists(common_path):
            spec = importlib.util.spec_from_file_location("common", common_path)
            if spec and spec.loader:
                common = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(common)
                if hasattr(common, "speak"):
                    common.speak(text)
                    return
        print(f"[VOZ] {text}")
    except (IOError, ImportError, AttributeError):
        print(f"[VOZ] {text}")


def get_content_hash(text: str) -> str:
    """
    Genera un hash del contenido ignorando espacios en blanco y saltos de línea.
    Esto permite validar que no se pierda información real (texto) durante el formateo.
    """
    pure_content = "".join(text.split())
    return hashlib.sha256(pure_content.encode("utf-8")).hexdigest()


def beautify_markdown(content: str) -> str:
    """
    Aplica reglas de estética premium al contenido Markdown.
    """
    # 1. Normalizar saltos de línea entre títulos y párrafos
    content = re.sub(r"(#+ .*?)\n+", r"\1\n\n", content)

    # 2. Asegurar espacio después de títulos
    content = re.sub(r"(#+ .*?)\n(?!\n)", r"\1\n\n", content)

    # 3. Normalizar listas (un espacio después de el marcador)
    content = re.sub(r"^(\s*[\-\*])\s*", r"\1 ", content, flags=re.MULTILINE)

    # 4. Limpiar múltiples saltos de línea (máximo 2)
    content = re.sub(r"\n{3,}", r"\n\n", content)

    # 5. Asegurar un solo salto al final
    content = content.strip() + "\n"

    return content


def process_file(file_path: str) -> None:
    """
    Procesa un archivo individual y valida su integridad mediante hashing.
    """
    try:
        if not os.path.exists(file_path):
            print(f"[SKIP] No existe: {os.path.basename(file_path)}")
            return

        with open(file_path, "r", encoding="utf-8") as f:
            original_text = f.read()
        original_hash = get_content_hash(original_text)

        beautiful_text = beautify_markdown(original_text)
        beautiful_hash = get_content_hash(beautiful_text)

        # VALIDACIÓN CRÍTICA: Integridad de datos
        if original_hash != beautiful_hash:
            print(
                f"[ERROR] ¡Alerta de integridad en {os.path.basename(file_path)}! El contenido ha cambiado."
            )
            return

        if original_text != beautiful_text:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(beautiful_text)
            print(f"[BEAUTY] Optimizado: {os.path.basename(file_path)}")
        else:
            print(f"[OK] Ya es bello: {os.path.basename(file_path)}")

    except (OSError, UnicodeDecodeError) as e:
        print(f"[EXCEPTION] Error procesando {os.path.basename(file_path)}: {e}")


def main() -> None:
    """Orquestador de belleza documental."""
    print("==============================================")
    print("   [MAGIC] PERSONAL OS : BEAUTY DOC v1.0")
    print("==============================================")

    targets: List[str] = [
        os.path.join(BASE_DIR, "README.md"),
        os.path.join(BASE_DIR, "04_Engine", "README.md"),
        os.path.join(BASE_DIR, "MAPA_MAESTRO_FLUJOS.md"),
        # Inventario principal
        os.path.join(BASE_DIR, "01_Brain", "07_Memory_Brain", "04_Inventario.md"),
    ]

    # Agregar carpetas principales del proyecto
    folders: List[str] = [
        # Core files
        os.path.join(BASE_DIR, "00_Core"),
        # Brain - Memoria y contexto
        os.path.join(BASE_DIR, "01_Brain", "01_Context_Memory"),
        os.path.join(BASE_DIR, "01_Brain", "02_Knowledge_Brain"),
        os.path.join(BASE_DIR, "01_Brain", "03_Process_Notes"),
        os.path.join(BASE_DIR, "01_Brain", "04_Rules"),
        os.path.join(BASE_DIR, "01_Brain", "05_Templates"),
        os.path.join(BASE_DIR, "01_Brain", "06_Backup_Central"),
        os.path.join(BASE_DIR, "01_Brain", "07_Memory_Brain"),
        os.path.join(BASE_DIR, "01_Brain", "09_Momentum_Os"),
        # Operations - Tareas y progreso
        os.path.join(BASE_DIR, "02_Operations", "01_Active_Tasks"),
        os.path.join(BASE_DIR, "02_Operations", "02_Evals"),
        os.path.join(BASE_DIR, "02_Operations", "03_Progress"),
        # Knowledge - Investigación y recursos
        os.path.join(BASE_DIR, "03_Knowledge", "01_Research"),
        os.path.join(BASE_DIR, "03_Knowledge", "02_Notes"),
        os.path.join(BASE_DIR, "03_Knowledge", "03_Resources"),
        os.path.join(BASE_DIR, "03_Knowledge", "04_Examples"),
        os.path.join(BASE_DIR, "03_Knowledge", "05_Marketing"),
        os.path.join(BASE_DIR, "03_Knowledge", "06_Writing"),
        os.path.join(BASE_DIR, "03_Knowledge", "07_Voice"),
        os.path.join(BASE_DIR, "03_Knowledge", "08_Config"),
        # System - Scripts y configuración
        os.path.join(BASE_DIR, "05_System", "01_Core"),
        os.path.join(BASE_DIR, "05_System", "02_Templates"),
        os.path.join(BASE_DIR, "05_System", "05_Docs"),
    ]

    import glob

    for folder in folders:
        if os.path.exists(folder):
            targets.extend(glob.glob(os.path.join(folder, "*.md")))

    if targets:
        speak(f"Embelleciendo {len(targets)} documentos de Personal OS.")
        for target in targets:
            process_file(target)
        speak("Documentación optimizada con éxito.")


if __name__ == "__main__":
    main()
