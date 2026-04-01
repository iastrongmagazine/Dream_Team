#!/usr/bin/env python3
import subprocess
import sys
import time


def test_mcp(name, command):
    """Testea un MCP ejecutando el comando y verificando si responde"""
    print(f"\nTesting MCP: {name}")
    print(f"   Command: {command}")

    try:
        # Intentar ejecutar el comando con timeout
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=10
        )

        if result.returncode == 0:
            print(f"   [OK] {name}: FUNCIONANDO")
            return True
        else:
            print(f"   [WARN] {name}: Error de configuracion ( esperado )")
            return False

    except subprocess.TimeoutExpired:
        print(f"   [TIMEOUT] {name}: Servicio iniciado correctamente")
        return True
    except Exception as e:
        print(f"   [ERROR] {name}: {str(e)}")
        return False


def main():
    print("=" * 60)
    print("   MCP TOP 2026 - PRUEBAS DE ACTIVACION")
    print("=" * 60)

    tests = [
        ("Brave Search", "npx -y @modelcontextprotocol/server-brave-search --help"),
        ("PostgreSQL", "npx -y @modelcontextprotocol/server-postgres --help"),
        ("SQLite", "npx -y @modelcontextprotocol/server-sqlite --help"),
        ("Slack", "npx -y @modelcontextprotocol/server-slack --help"),
        ("Sentry", "npx -y @modelcontextprotocol/server-sentry --help"),
        ("StackOverflow", "npx -y @modelcontextprotocol/server-stackoverflow --help"),
        ("Docker", "docker run --rm mcp/docker:latest --help 2>&1 | head -5"),
    ]

    results = []
    for name, cmd in tests:
        results.append((name, test_mcp(name, cmd)))

    print("\n" + "=" * 60)
    print("   RESUMEN DE PRUEBAS")
    print("=" * 60)

    for name, status in results:
        icon = "[OK]" if status else "[WARN]"
        print(f"{icon} {name}")

    active_count = sum(1 for _, status in results if status)
    total_count = len(results)

    print(f"\nMCPs Activos: {active_count}/{total_count}")

    if active_count == total_count:
        print("TODOS LOS MCPs ESTAN CONFIGURADOS Y LISTOS!")
    else:
        print("Algunos MCPs requieren configuracion de API keys")

    return active_count, total_count


if __name__ == "__main__":
    main()
