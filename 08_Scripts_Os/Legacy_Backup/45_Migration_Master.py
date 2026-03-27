import os
import re

# Mapeo: Ruta antigua -> Nueva ruta
MAPPING = {
    "02_Operations/Tasks/": "02_Operations/01_Active_Tasks/",
    "02_Operations/Task_End/": "02_Operations/01_Active_Tasks/Task_End/",
    "02_Operations/Evals/": "02_Operations/02_Evals/",
    "02_Operations/Core/": "05_System/05_Core/",
    "01_Brain/Context_Memory/": "01_Brain/01_Context_Memory/",
    "01_Brain/Knowledge_Brain/": "01_Brain/02_Knowledge_Brain/",
    "01_Brain/Process_Notes/": "01_Brain/03_Process_Notes/",
    "01_Brain/Rules/": "01_Brain/04_Rules/",
    "01_Brain/Docs_AI/": "01_Brain/05_Docs_AI/",
    "01_Brain/Template/": "01_Brain/05_Templates/",
    "01_Brain/Archive/": "01_Brain/07_Archive/",
}


def migrate():
    # Obtener directorio base (raíz del proyecto)
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    for root, dirs, files in os.walk(base_dir):
        # Excluir carpetas innecesarias
        if any(
            part in root
            for part in [
                ".git",
                "node_modules",
                "06_Archive",
                "04_Engine",
                "05_System/05_Core",
            ]
        ):
            continue

        for file in files:
            file_path = os.path.join(root, file)
            # No procesar este script
            if "Migration_Master" in file:
                continue

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                new_content = content
                for old, new in MAPPING.items():
                    new_content = new_content.replace(old, new)

                if new_content != content:
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"Updated: {file_path}")
            except Exception as e:
                print(f"Skipping {file_path}: {e}")


if __name__ == "__main__":
    migrate()
