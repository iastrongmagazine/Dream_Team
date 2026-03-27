import os

# Definir reglas de reemplazo
# Mapa: {ruta_antigua: ruta_nueva}
replacements = {
    "01_Brain/Knowledge_Brain/": "01_Brain/02_Knowledge_Brain/",
    "01_Brain/Process_Notes/": "01_Brain/03_Process_Notes/",
    "02_Operations/Tasks/": "02_Operations/01_Active_Tasks/",
    "00_Knowledge/": "03_Knowledge/",
}


def is_binary(filepath):
    try:
        with open(filepath, "rb") as f:
            chunk = f.read(1024)
            return b"\0" in chunk
    except:
        return True


def replace_in_file(filepath):
    if is_binary(filepath):
        return

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)

        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Actualizado: {filepath}")
    except Exception as e:
        print(f"Error procesando {filepath}: {e}")


# Directorios objetivo limitados
target_dirs = [".agent", ".cursor", ".claude", "00_Core"]
files_to_check = ["README.md", "CLAUDE.md"]

print("Iniciando refactorización atómica de rutas...")

# Procesar directorios
for target in target_dirs:
    if os.path.exists(target):
        for root, dirs, files in os.walk(target):
            for file in files:
                filepath = os.path.join(root, file)
                if ".git" in filepath:
                    continue
                replace_in_file(filepath)

# Procesar archivos individuales
for file in files_to_check:
    if os.path.exists(file):
        replace_in_file(file)

print("Finalizada refactorización.")
