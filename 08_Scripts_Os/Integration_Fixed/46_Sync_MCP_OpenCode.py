import sys
from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
"""
46_Sync_MCP_OpenCode.py - Armor Layer Protected
Sincronización automática de MCPs entre .mcp.json y opencode.json

Este script sincroniza la configuración de los servidores MCP entre:
- .mcp.json (configuración principal del sistema)
- 03_Knowledge/Resources/Gentleman.Dots/GentlemanOpenCode/opencode.json (configuración de OpenCode)

Objetivo: Mantener consistencia en la configuración de MCPs en todo el ecosistema.
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

sys.path.insert(0, str(Path(__file__).parent))
from config_paths import PROJECT_ROOT, KNOWLEDGE_DIR

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


class MCPSynchronizer:
    def __init__(self):
        self.root_dir = PROJECT_ROOT

        new_path = self.root_dir / ".claude" / "mcp.json"
        if new_path.exists():
            self.mcp_config_path = new_path
        else:
            self.mcp_config_path = self.root_dir / ".mcp.json"
        self.opencode_config_path = (
            self.root_dir
            / "03_Knowledge"
            / "Resources"
            / "Gentleman.Dots"
            / "GentlemanOpenCode"
            / "opencode.json"
        )

    def load_mcp_config(self):
        """Carga la configuración de .mcp.json"""
        try:
            with open(self.mcp_config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"[ERROR] No se encontró {self.mcp_config_path}")
            return None
        except json.JSONDecodeError as e:
            print(f"[ERROR] Error al parsear {self.mcp_config_path}: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"❌ Error al parsear {self.mcp_config_path}: {e}")
            return None

    def load_opencode_config(self):
        """Carga la configuración de opencode.json"""
        try:
            with open(self.opencode_config_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"[ERROR] No se encontró {self.opencode_config_path}")
            return None
        except json.JSONDecodeError as e:
            print(f"[ERROR] Error al parsear {self.opencode_config_path}: {e}")
            return None
        except json.JSONDecodeError as e:
            print(f"❌ Error al parsear {self.opencode_config_path}: {e}")
            return None

    def convert_mcp_to_opencode_format(self, mcp_servers):
        """
        Convierte la configuración de .mcp.json al formato de opencode.json

        Formato .mcp.json:
        {
          "mcpServers": {
            "server-name": {
              "transport": "stdio",
              "command": "npx.cmd",
              "args": [...],
              "env": {...}
            }
          }
        }

        Formato opencode.json:
        {
          "mcp": {
            "server-name": {
              "command": [...],
              "enabled": true,
              "type": "local",
              "env": {...}
            }
          }
        }
        """
        opencode_mcp = {}

        for server_name, config in mcp_servers.items():
            opencode_config = {"enabled": True}

            # Determinar el tipo de servidor
            if "transport" in config:
                if config["transport"] == "streamableHttp":
                    opencode_config["type"] = "remote"
                    opencode_config["url"] = config.get("url", "")
                    if "headers" in config and config["headers"]:
                        opencode_config["headers"] = config["headers"]
                else:
                    opencode_config["type"] = "local"

            # Configurar command/args
            if "command" in config:
                if "args" in config:
                    # Combinar command y args en un array
                    command_list = [config["command"]] + config["args"]
                    opencode_config["command"] = command_list
                else:
                    opencode_config["command"] = [config["command"]]

            # Configurar environment variables
            if "env" in config and config["env"]:
                # Priorizar variables de entorno del sistema si están definidas
                env_config = config["env"].copy()
                for key in env_config:
                    if key in os.environ:
                        env_config[key] = os.environ[key]
                opencode_config["env"] = env_config

            # Si no hay command pero sí url, es remoto
            if "url" in config and "command" not in opencode_config:
                opencode_config["type"] = "remote"
                opencode_config["url"] = config["url"]
                if "headers" in config and config["headers"]:
                    opencode_config["headers"] = config["headers"]

            opencode_mcp[server_name] = opencode_config

        return opencode_mcp

    def sync_mcp_to_opencode(self):
        """Sincroniza los MCPs de .mcp.json a opencode.json"""
        print("[INFO] Iniciando sincronización de MCPs...")

        # Cargar configuraciones
        mcp_config = self.load_mcp_config()
        if not mcp_config:
            return False

        opencode_config = self.load_opencode_config()
        if not opencode_config:
            return False

        # Convertir formato
        mcp_servers = mcp_config.get("mcpServers", {})
        opencode_mcp = self.convert_mcp_to_opencode_format(mcp_servers)

        # Actualizar opencode.json
        opencode_config["mcp"] = opencode_mcp

        # Guardar con formato
        try:
            with open(self.opencode_config_path, "w", encoding="utf-8") as f:
                json.dump(opencode_config, f, indent=2, ensure_ascii=False)
            print(f"[OK] Configuración actualizada en {self.opencode_config_path}")
            print(f"[INFO] Total MCPs sincronizados: {len(opencode_mcp)}")
            return True
        except Exception as e:
            print(f"[ERROR] Error al guardar opencode.json: {e}")
            return False

    def backup_configs(self):
        """Crea backup de los archivos de configuración"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = self.root_dir / "01_Brain" / "Context_Memory" / "backups"
        backup_dir.mkdir(parents=True, exist_ok=True)

        try:
            # Backup .mcp.json
            backup_mcp = backup_dir / f".mcp.json.backup_{timestamp}"
            with open(self.mcp_config_path, "r", encoding="utf-8") as f:
                content = f.read()
            with open(backup_mcp, "w", encoding="utf-8") as f:
                f.write(content)

            # Backup opencode.json
            backup_opencode = backup_dir / f"opencode.json.backup_{timestamp}"
            with open(self.opencode_config_path, "r", encoding="utf-8") as f:
                content = f.read()
            with open(backup_opencode, "w", encoding="utf-8") as f:
                f.write(content)

            print(f"[OK] Backups creados en {backup_dir}")
            return True
        except Exception as e:
            print(f"[ERROR] Error al crear backups: {e}")
            return False

    def run(self):
        """Ejecuta el proceso completo de sincronización"""
        print("=" * 60)
        print("Sincronizador de MCPs para OpenCode")
        print("=" * 60)

        # Crear backups primero
        if not self.backup_configs():
            print("[WARNING] Continuando sin backup...")

        # Sincronizar
        success = self.sync_mcp_to_opencode()

        if success:
            print("\n[OK] Sincronización completada exitosamente!")
            print("\nPróximos pasos:")
            print("1. Reinicia OpenCode para cargar la nueva configuración")
            print("2. Verifica los MCPs disponibles con /mcp-list")
            print("3. Prueba un MCP específico para confirmar funcionamiento")
        else:
            print("\n[ERROR] Sincronización fallida. Revisa los errores anteriores.")

        print("=" * 60)
        return success


if __name__ == "__main__":
    synchronizer = MCPSynchronizer()
    success = synchronizer.run()
    exit(0 if success else 1)
