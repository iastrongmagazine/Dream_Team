import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
66_Alert_Manager.py
===================
PersonalOS - Alert Manager

Sistema centralizado de alertas que notifica cuando fallan los auditores.
Integrado con Discord, niveles de severidad y auto-stop.

Uso:
  python 66_Alert_Manager.py --level ERROR --script "53_Structure_Auditor.py" --message "Carpeta faltante"

Como módulo:
  from 66_Alert_Manager import alert
  alert(level="ERROR", script="53_Structure_Auditor.py", message="...")

Integración: Se ejecuta después de cada auditor en 08_Ritual_Cierre.py
"""

import os
import sys
import json
import requests
import subprocess
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List
from enum import Enum

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import ROOT_DIR, OPERATIONS_ANALYTICS_DIR

# Fix encoding for Windows
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except:
        pass

# ============================================================
# CONFIGURACIÓN
# ============================================================


class AlertLevel(Enum):
    """Niveles de severidad de alertas."""

    INFO = 0
    WARNING = 1
    ERROR = 2
    CRITICAL = 3


# Paths
SCRIPT_DIR = Path(__file__).resolve().parent
CONFIG_FILE = ROOT_DIR / "05_System" / "04_Env" / "alerts_config.json"
LOG_DIR = OPERATIONS_ANALYTICS_DIR / "alerts"

# Colores para console
COLORS = {
    "INFO": "\033[94m",  # Azul
    "WARNING": "\033[93m",  # Amarillo
    "ERROR": "\033[91m",  # Rojo
    "CRITICAL": "\033[95m",  # Magenta
    "RESET": "\033[0m",
}

# ============================================================
# CARGAR CONFIGURACIÓN
# ============================================================


def load_config() -> Dict:
    """Carga configuración de alertas."""
    default_config = {
        "discord_webhook": "",
        "channels": ["console", "log"],
        "stop_on_error": True,
        "log_path": str(LOG_DIR),
        "notify_voz": True,
    }

    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                return {**default_config, **json.load(f)}
        except Exception:
            return default_config
    return default_config


def save_config(config: Dict) -> None:
    """Guarda configuración de alertas."""
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=2)


# ============================================================
# NOTIFICACIONES
# ============================================================


def notify_voz(mensaje: str) -> None:
    """Notifica por voz usando 64_Campanilla."""
    try:
        campanilla_path = SCRIPT_DIR / "64_Campanilla.py"
        if campanilla_path.exists():
            result = subprocess.run(
                [sys.executable, str(campanilla_path)], capture_output=True, timeout=10
            )
    except Exception:
        pass  # Silencioso si falla


def send_discord_webhook(
    webhook_url: str, level: str, script: str, message: str
) -> bool:
    """Envía notificación a Discord."""
    if not webhook_url:
        return False

    colors = {
        "INFO": 3447003,  # Azul
        "WARNING": 16776960,  # Amarillo
        "ERROR": 15158332,  # Rojo
        "CRITICAL": 10038562,  # Rojo oscuro
    }

    emojis = {"INFO": "ℹ️", "WARNING": "⚠️", "ERROR": "❌", "CRITICAL": "🚨"}

    embed = {
        "embeds": [
            {
                "title": f"{emojis.get(level, '🔔')} ALERTA PersonalOS - {level}",
                "color": colors.get(level, 16711680),
                "fields": [
                    {"name": "Nivel", "value": level, "inline": True},
                    {"name": "Script", "value": script, "inline": True},
                    {"name": "Mensaje", "value": message},
                    {"name": "Timestamp", "value": datetime.now().isoformat()},
                ],
                "footer": {"text": "PersonalOS Alert Manager"},
            }
        ]
    }

    try:
        response = requests.post(webhook_url, json=embed, timeout=10)
        return response.status_code == 200
    except Exception as e:
        print(f"[Discord Error] {e}")
        return False


def log_alert(level: str, script: str, message: str, config: Dict) -> None:
    """Guarda alerta en archivo de log."""
    log_path = Path(config.get("log_path", str(LOG_DIR)))
    log_path.mkdir(parents=True, exist_ok=True)

    log_file = log_path / f"alerts_{datetime.now().strftime('%Y%m')}.log"

    entry = {
        "timestamp": datetime.now().isoformat(),
        "level": level,
        "script": script,
        "message": message,
    }

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")


def print_alert(level: str, script: str, message: str) -> None:
    """Imprime alerta en console con color."""
    color = COLORS.get(level, COLORS["RESET"])
    icons = {"INFO": "ℹ️", "WARNING": "⚠️", "ERROR": "❌", "CRITICAL": "🚨"}

    icon = icons.get(level, "🔔")
    print(f"{color}{icon} [{level}] {script}: {message}{COLORS['RESET']}")


# ============================================================
# LÓGICA PRINCIPAL
# ============================================================


def should_stop(level: str) -> bool:
    """Determina si el proceso debe detenerse."""
    return level in ["ERROR", "CRITICAL"]


def alert(
    level: str = "INFO",
    script: str = "Unknown",
    message: str = "",
    force_voz: bool = False,
) -> bool:
    """
    Función principal de alertas.

    Args:
        level: INFO, WARNING, ERROR, CRITICAL
        script: Nombre del script que generó la alerta
        message: Mensaje descriptivo
        force_voz: Forzar notificación de voz

    Returns:
        bool: True si el proceso debe detenerse (ERROR/CRITICAL)
    """
    # Normalizar nivel
    level = level.upper()
    valid_levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]
    if level not in valid_levels:
        level = "INFO"

    # Cargar configuración
    config = load_config()

    # Notificación por voz (reutiliza 64_Campanilla)
    if force_voz or level in ["ERROR", "CRITICAL"]:
        if config.get("notify_voz", True):
            notify_voz(f"Alerta {level} en {script}")

    # Console
    if "console" in config.get("channels", []):
        print_alert(level, script, message)

    # Discord (solo ERROR/CRITICAL)
    if level in ["ERROR", "CRITICAL"]:
        if "discord" in config.get("channels", []) and config.get("discord_webhook"):
            send_discord_webhook(config["discord_webhook"], level, script, message)

    # Log (todos los niveles)
    if "log" in config.get("channels", []):
        log_alert(level, script, message, config)

    # Retornar si debe detenerse
    return should_stop(level)


def check_and_alert(
    script_name: str, return_code: int, output: str = "", config: Dict = None
) -> bool:
    """
    Verifica resultado de un script y genera alerta si falló.

    Args:
        script_name: Nombre del script
        return_code: Código de retorno (0 = OK)
        output: Output del script (opcional)
        config: Configuración (opcional)

    Returns:
        bool: True si debe detenerse el proceso
    """
    if config is None:
        config = load_config()

    if return_code == 0:
        # Todo OK, solo loggear si es DEBUG
        if config.get("debug", False):
            print(f"✓ {script_name}: OK")
        return False

    # Falló - determinar nivel
    level = "ERROR"
    if "CRITICAL" in output.upper() or return_code > 1:
        level = "CRITICAL"

    # Extraer mensaje de error
    message = f"Return code: {return_code}"
    if output:
        lines = output.strip().split("\n")
        error_lines = [l for l in lines if "ERROR" in l.upper() or "FAIL" in l.upper()]
        if error_lines:
            message = error_lines[0][:200]  # Truncar si es muy largo

    return alert(level=level, script=script_name, message=message)


# ============================================================
# CLI
# ============================================================


def main():
    """Interfaz de línea de comandos."""
    import argparse

    parser = argparse.ArgumentParser(description="PersonalOS Alert Manager")
    parser.add_argument(
        "--level", default="INFO", choices=["INFO", "WARNING", "ERROR", "CRITICAL"]
    )
    parser.add_argument("--script", default="CLI", help="Nombre del script")
    parser.add_argument("--message", default="", help="Mensaje de alerta")
    parser.add_argument("--voz", action="store_true", help="Forzar notificación de voz")
    parser.add_argument(
        "--setup", action="store_true", help="Configurar Discord webhook"
    )

    args = parser.parse_args()

    if args.setup:
        webhook = input("Discord Webhook URL: ").strip()
        config = load_config()
        config["discord_webhook"] = webhook
        if webhook:
            config["channels"] = ["console", "log", "discord"]
        save_config(config)
        print("✓ Configuración guardada")
        return

    # Ejecutar alerta
    should_stop = alert(
        level=args.level, script=args.script, message=args.message, force_voz=args.voz
    )

    if should_stop:
        print("\n⚠️  El proceso debe detenerse debido a errores críticos.")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
