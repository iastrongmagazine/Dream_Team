"""
validate.py - Valida que la instalación esté correcta
Incluye tests de pytest para verificar scripts del motor.
"""

import os
import sys
import subprocess

# Fix Windows console encoding
if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


def run_validation():
    """Ejecuta la validación del stack"""
    print("=== Validando Instalación ===\n")

    from pathlib import Path

    project_root = Path(__file__).resolve().parents[3]
    engine_dir = project_root / "04_Operations"

    # Ejecutar Validate_Stack.py
    validate_script = engine_dir / "13_Validate_Stack.py"

    if validate_script.exists():
        print("Ejecutando 13_Validate_Stack.py...")
        result = subprocess.run(
            [sys.executable, str(validate_script)],
            cwd=str(project_root),
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            print(result.stdout)
            print("✓ Validación de stack PASS")
            return True
        else:
            print(result.stdout)
            print(f"❌ Validación falló: {result.stderr}")
            return False
    else:
        print(f"⚠ No se encontró {validate_script}")
        return False


def check_mcp_json():
    """Verifica que .mcp.json esté bien formado"""
    print("\n--- Verificando .mcp.json ---")

    from pathlib import Path

    project_root = Path(__file__).resolve().parents[3]
    # Buscar en .claude/ (nueva ubicación) o raíz (legacy)
    mcp_path = project_root / ".claude" / "mcp.json"
    if not mcp_path.exists():
        mcp_path = project_root / ".mcp.json"  # Legacy fallback

    if not mcp_path.exists():
        print("❌ .mcp.json no existe")
        return False

    try:
        import json

        with open(mcp_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        servers = data.get("mcpServers", {})
        print(f"✓ .mcp.json válido con {len(servers)} servidores MCP")

        # Verificar que no tenga placeholders sin reemplazar
        with open(mcp_path, "r") as f:
            content = f.read()

        placeholders = ["{{USER_", "{{"]
        for ph in placeholders:
            if ph in content:
                print(f"⚠ Placeholder encontrado: {ph}")
                return False

        print("✓ Sin placeholders sin reemplazar")
        return True

    except json.JSONDecodeError as e:
        print(f"❌ .mcp.json corrupto: {e}")
        return False
    except Exception as e:
        print(f"❌ Error verificando .mcp.json: {e}")
        return False


def check_machine_id():
    """Verifica que .machine_id exista"""
    print("\n--- Verificando .machine_id ---")

    from pathlib import Path

    project_root = Path(__file__).resolve().parents[3]
    machine_id_path = project_root / "05_System" / "04_Env" / ".machine_id"

    if machine_id_path.exists():
        with open(machine_id_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        if content:
            print(f"✓ .machine_id existe: {content[:8]}...")
            return True
        else:
            print("⚠ .machine_id vacío")
            return False
    else:
        print("❌ .machine_id no existe")
        return False


def check_structure():
    """Verifica estructura de carpetas"""
    print("\n--- Verificando Estructura ---")

    # Detectar project root usando pathlib (case-insensitive en Windows)
    from pathlib import Path

    script_path = Path(__file__).resolve()
    project_root = script_path.parents[3]  # scripts -> Installer -> 04_Operations -> root

    required_dirs = [
        "00_Core",
        "01_Brain",
        "04_Operations",
        "03_Knowledge",
        "04_Operations",
        "05_System",
        "06_Archive",
        "07_Projects",
    ]

    all_ok = True
    for d in required_dirs:
        path = project_root / d
        if path.exists():
            print(f"✓ {d}/")
        else:
            print(f"❌ {d}/ no existe")
            all_ok = False

    return all_ok


def run_tests():
    """Ejecuta la suite de tests con pytest"""
    print("\n--- Ejecutando Tests ---")

    from pathlib import Path

    project_root = Path(__file__).resolve().parents[3]
    tests_dir = project_root / "04_Operations" / "05_Tests"

    if not tests_dir.exists():
        print("⚠ Tests no encontrados")
        return None

    print(f"Ejecutando pytest en {tests_dir}...")

    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", str(tests_dir), "-v", "--tb=short", "-q"],
            cwd=str(project_root),
            capture_output=True,
            text=True,
            timeout=120,
        )

        # Parsear resultado
        output = result.stdout + result.stderr

        # Extraer estadísticas
        passed = output.count("PASSED")
        failed = output.count("FAILED")
        errors = output.count("ERROR")
        total = passed + failed + errors

        if result.returncode == 0:
            print(f"✓ Tests: {passed}/{total} passed")
            return True
        else:
            print(f"⚠ Tests: {passed}/{total} passed, {failed} failed, {errors} errors")
            if failed > 0 or errors > 0:
                print("   Revisa el output arriba para detalles")
            return False

    except subprocess.TimeoutExpired:
        print("⚠ Tests: Timeout (>120s)")
        return None
    except FileNotFoundError:
        print("⚠ pytest no instalado. Ejecuta: pip install pytest")
        return None
    except Exception as e:
        print(f"⚠ Tests: Error - {e}")
        return None


if __name__ == "__main__":
    results = []

    results.append(("Estructura", check_structure()))
    results.append((".machine_id", check_machine_id()))
    results.append((".mcp.json", check_mcp_json()))
    results.append(("Tests", run_tests()))
    results.append(("Stack Validation", run_validation()))

    print("\n" + "=" * 40)
    print("RESUMEN DE VALIDACIÓN")
    print("=" * 40)

    all_pass = True
    for name, result in results:
        if result is None:
            status = "⚠ SKIP"
        elif result:
            status = "✓ PASS"
        else:
            status = "❌ FAIL"
        print(f"{name}: {status}")
        if result is False:
            all_pass = False

    print("=" * 40)

    if all_pass:
        print("🎉 ¡Instalación validada exitosamente!")
        sys.exit(0)
    else:
        print("⚠️ Instalación con problemas. Revisa los errores arriba.")
        sys.exit(1)
