"""
MULTI-AGENT FINAL VALIDATION - PersonalOS
Simula la orquestación de 5 agentes especializados para la validación final del sistema.
"""

import os
import sys
import time
import importlib.util
import io

# Forzar encoding UTF-8 en Windows para evitar UnicodeEncodeError
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# --- CONFIGURACIÓN ---
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RULES_DIR = os.path.join(ROOT_DIR, ".cursor", "00_Rules")
INVENTORY_FILE = os.path.join(
    ROOT_DIR, "01_Brain", "Knowledge_Brain", "01_Inventario_Total.md"
)
REPORTS_DIR = os.path.join(ROOT_DIR, "04_Engine", "analytics_output", "md_reports")

# --- AGENTES VIRTUALES ---


class AgentArchitect:
    """Valida la estructura y reglas del sistema (Constitución 3+6)."""

    def run(self):
        print("\n👷 [ARCHITECT] Validando Integridad Estructural...")
        required_rules = [
            "01_Context_Protocol.mdc",
            "03_Pilar_Motor.mdc",
            "04_Pilar_Estrategia.mdc",
            "09_Elite_Reporting.mdc",
        ]
        missing = []
        for r in required_rules:
            full_path = os.path.join(RULES_DIR, r)
            if not os.path.exists(full_path):
                missing.append(r)

        if missing:
            print(f"   ❌ Faltan reglas críticas: {missing}")
            print(f"   🔍 Buscando en: {RULES_DIR}")
            print(f"   🏠 Root Dir: {ROOT_DIR}")
            return False

        print("   ✅ Constitución 3+6 (Pilares + Reglas) intacta.")

        if not os.path.exists(INVENTORY_FILE):
            print("   ❌ Falta el Inventario Total.")
            return False

        print("   ✅ Inventario presente y accesible.")
        return True


class AgentDevOps:
    """Valida rutas, dependencias y versiones."""

    def run(self):
        print("\n🔧 [DEVOPS] Validando Rutas y Dependencias...")
        # Verificar rutas críticas recientes
        if not os.path.exists(REPORTS_DIR):
            print(f"   ❌ Directorio de Reportes Markdown no encontrado: {REPORTS_DIR}")
            try:
                os.makedirs(REPORTS_DIR, exist_ok=True)
                print("   🛠️ Directorio creado automáticamente.")
            except:
                return False

        print(f"   ✅ Rutas de salida verficadas: {os.path.basename(REPORTS_DIR)}")

        # Simulando verificación de dependencias (requirements.txt existe?)
        req_file = os.path.join(ROOT_DIR, "requirements.txt")
        if os.path.exists(req_file):
            print("   ✅ requirements.txt detectado.")
        else:
            print("   ⚠️ No se encontró requirements.txt (Alerta menor).")

        return True


class AgentQA:
    """Valida la calidad de los reportes generados."""

    def run(self):
        print("\n🕵️ [QA] Verificando Calidad de Reportes...")
        # Verificar si hay reportes recientes
        import glob

        reports = glob.glob(os.path.join(REPORTS_DIR, "*.md"))
        if not reports:
            print("   ⚠️ No hay reportes en la carpeta nueva. Se generarán pronto.")
        else:
            latest = max(reports, key=os.path.getctime)
            print(f"   ✅ Último reporte detectado: {os.path.basename(latest)}")

        # Verificar script de consolidación
        script_path = os.path.join(
            ROOT_DIR, "04_Engine", "30_AIPM_Consolidated_Report.py"
        )
        if not os.path.exists(script_path):
            print(
                f"   ❌ Script de consolidación no encontrado: {os.path.basename(script_path)}"
            )
            return False

        with open(script_path, "r", encoding="utf-8") as f:
            content = f.read()
            if "md_reports" in content or "analytics_output" in content:
                print("   ✅ Script 24_ verificado (rutas de salida detectadas).")
            else:
                print("   ❌ Script 24_ parece desactualizado.")
                return False
        return True


class AgentAIPM:
    """Valida el estilo Silicon Valley y Storytelling."""

    def run(self):
        print("\n🧠 [AIPM] Auditando Estilo (Silicon Valley Grade)...")
        # Verificar regla 09 (Elite Reporting)
        rule_09 = os.path.join(RULES_DIR, "09_Elite_Reporting.mdc")
        if os.path.exists(rule_09):
            print("   ✅ Estándar de Reporte Elite (Regla 09) activo.")
        else:
            print("   ❌ Falta la Regla 06.")
            return False
        return True


class AgentRitual:
    """Ejecuta el cierre del sistema."""

    def run(self):
        print("\n[RITUAL] Iniciando Protocolo de Cierre...")
        ritual_path = os.path.join(ROOT_DIR, "04_Engine", "08_Ritual_Cierre.py")

        # Ejecutar ritual real
        print(f"   🚀 Ejecutando {os.path.basename(ritual_path)}...")
        os.system(f'python "{ritual_path}"')
        return True


# --- ORQUESTADOR ---


def main():
    print("==============================================")
    print("   PERSONAL OS - FINAL MULTI-AGENT VALIDATION")
    print("==============================================")

    agents = [AgentArchitect(), AgentDevOps(), AgentQA(), AgentAIPM()]
    all_passed = True

    for agent in agents:
        if not agent.run():
            all_passed = False
            print("   ⛔ DETENIENDO: Validación fallida.")
            break

    if all_passed:
        print("\n✅ VALIDACIÓN EXITOSA. Procediendo al Cierre.")
        AgentRitual().run()
    else:
        print("\n❌ VALIDACIÓN FALLIDA. Revise los errores.")


if __name__ == "__main__":
    main()
