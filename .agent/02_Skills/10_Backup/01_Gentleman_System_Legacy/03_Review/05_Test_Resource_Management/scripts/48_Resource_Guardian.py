import os

# Branding de PersonalOS
print("--- PersonalOS: Test Resource Guardian (Skill 48) ---")

def set_resource_limits():
    """
    Script de activación para la Skill 48.
    Configura variables de entorno para limitar workers en frameworks de test.
    """
    print("[NEXUS] Configurando límites de hardware para Pure Green...")

    # Configuración de variables globales de entorno para limitar workers
    os.environ["VITEST_MAX_WORKERS"] = "4"
    os.environ["PLAYWRIGHT_WORKERS"] = "4"
    os.environ["JEST_MAX_WORKERS"] = "4"

    print("[RESULT] Límites establecidos: Máximo 4 workers activos.")
    print("[STATUS] Sistema protegido contra agotamiento de CPU.")

if __name__ == "__main__":
    set_resource_limits()
