import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
"""
61_MCP_Health_Check.py - Armor Layer Protected
Verifica estado de MCPs configurados
============================================================
Ejecuta checks en los MCPs del archivo .mcp.json

Uso:
  python 04_Engine/08_Scripts_Os/61_MCP_Health_Check.py
"""

import json
import subprocess
import sys
import socket
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

# Armor Layer: Config paths inline
_SCRIPT_DIR = Path(__file__).resolve().parent
_PROJECT_ROOT = _SCRIPT_DIR.parent.parent
sys.path.insert(0, str(_PROJECT_ROOT))
sys.path.insert(0, str(_SCRIPT_DIR.parent))
try:
    from config_paths import PROJECT_ROOT
except:
    PROJECT_ROOT = _PROJECT_ROOT

REQUIRED_DIRS = [
    "00_Core",
    "01_Brain",
    "02_Operations",
    "03_Knowledge",
    "04_Engine",
    "05_System",
    "06_Archive",
]
for d in REQUIRED_DIRS:
    if not (PROJECT_ROOT / d).exists():
        print(f"[WARN] Required directory not found: {d}")

ROOT_DIR = PROJECT_ROOT


def get_mcp_file_path():
    """Obtiene la ruta del archivo mcp.json con fallback legacy"""
    new_path = ROOT_DIR / ".claude" / "mcp.json"
    if new_path.exists():
        return new_path
    legacy_path = ROOT_DIR / ".mcp.json"
    if legacy_path.exists():
        return legacy_path
    return new_path


MCP_FILE = get_mcp_file_path()

# Check ports para MCPs locales comunes
LOCAL_PORTS = {
    "obsidian-api": 27124,
    "eagle-mcp": 41596,
}


def check_port(host, port):
    """Check if port is open"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except:
        return False


def load_mcp_config():
    """Carga configuración de MCPs"""
    with open(MCP_FILE, encoding="utf-8") as f:
        return json.load(f)["mcpServers"]


def check_npx():
    """Check if npx is available (tries npx and npx.cmd for Windows)"""
    # Try npx first (Linux/Mac/WSL)
    try:
        result = subprocess.run(["npx", "--version"], capture_output=True, timeout=5)
        if result.returncode == 0:
            return True
    except:
        pass

    # Try npx.cmd (Windows)
    try:
        result = subprocess.run(
            ["npx.cmd", "--version"], capture_output=True, timeout=5
        )
        if result.returncode == 0:
            return True
    except:
        pass

    return False


def check_mcp(name, config, npx_available):
    """Check individual MCP"""
    transport = config.get("transport", "unknown")
    url = config.get("url", "")
    command = config.get("command", "")

    status = "UNKNOWN"
    detail = ""

    # Check based on type
    if transport == "streamableHttp":
        # Parse URL
        is_https = "https" in url
        host = "localhost"
        port = 443 if is_https else 80

        # Extract host and port from URL
        if "://" in url:
            parts = url.split("://")[1].split("/")[0]
            if ":" in parts:
                host, port_str = parts.split(":")
                port = int(port_str)
            else:
                host = parts

        if "localhost" in url or "127.0.0.1" in url:
            # Local server
            if check_port(host, port):
                status = "ACTIVE"
                detail = f"{host}:{port}"
            else:
                status = "OFFLINE"
                detail = f"{host}:{port} not responding"
        else:
            # Remote cloud
            status = "CLOUD"
            detail = f"{host}:{port}"

    elif transport == "stdio":
        if "npx" in command:
            if npx_available:
                status = "READY"
                detail = "npx available"
            else:
                status = "ERROR"
                detail = "npx not found"
        elif command.endswith(".exe"):
            exe_path = Path(command)
            if exe_path.exists():
                status = "READY"
                detail = f"exe exists"
            else:
                status = "ERROR"
                detail = "exe not found"
        elif command == "docker":
            status = "READY"
            detail = "needs docker"
        else:
            status = "READY"
            detail = command

    # Color based on status
    color = Fore.WHITE
    if status == "ACTIVE":
        color = Fore.GREEN
    elif status == "READY":
        color = Fore.CYAN
    elif status == "OFFLINE":
        color = Fore.RED
    elif status == "ERROR":
        color = Fore.RED
    elif status == "CLOUD":
        color = Fore.YELLOW

    return status, detail, color


def main():
    print(f"{Style.BRIGHT}{'=' * 60}")
    print(f"MCP Health Check")
    print(f"{'=' * 60}")

    # Check npx first
    npx_available = check_npx()
    print(f"\n{'npx':<15} {'status':<10}")
    print(f"{'-' * 25}")
    print(
        f"{'npx':<15} {Fore.GREEN if npx_available else Fore.RED}{'AVAILABLE' if npx_available else 'NOT FOUND'}"
    )

    mcp_servers = load_mcp_config()
    total = len(mcp_servers)

    print(f"\n{Fore.CYAN}{Style.BRIGHT}Total MCPs configured: {total}")

    active_count = 0
    ready_count = 0
    error_count = 0

    print(f"\n{Style.BRIGHT}{'Name':<30} {'Status':<10} {'Detail'}")
    print(f"{'-' * 70}")

    for name, config in mcp_servers.items():
        status, detail, color = check_mcp(name, config, npx_available)

        if status == "ACTIVE":
            active_count += 1
        elif status == "READY":
            ready_count += 1
        elif status == "ERROR":
            error_count += 1

        print(f"{name:<30} {color}{status:<10}{Style.RESET_ALL} {detail}")

    print(f"\n{Fore.GREEN}{Style.BRIGHT}{'=' * 60}")
    print(f"Summary")
    print(f"{'=' * 60}")
    print(f"  {Fore.GREEN}Active (running): {active_count}")
    print(f"  {Fore.CYAN}Ready (available): {ready_count}")
    print(f"  {Fore.RED}Error: {error_count}")
    print(f"  {Fore.YELLOW}Cloud: {total - active_count - ready_count - error_count}")

    print(
        f"\n{Fore.YELLOW}Note: Open Cursor/OpenCode and type '@' to verify actual active tools."
    )
    print(f"      Some MCPs may show 'READY' here but fail to load in the client.")


if __name__ == "__main__":
    main()
