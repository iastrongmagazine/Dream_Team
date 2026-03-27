# 🌟 04_Extensions — Sistema de Hooks y Utilidades

Sistema de extensiones para Claude Code: hooks de ciclo de vida, notificaciones, validaciones y utilidades compartidas.

---

## 🏗️ Arquitectura

```
04_Extensions/
├── hooks/                      # Hooks de Claude Code
│   ├── 01_Pre_Tool/           # Ejecuta ANTES de cada tool
│   │   └── pre_tool_use.py
│   ├── 02_Post_Tool/          # Ejecuta DESPUÉS de cada tool
│   │   └── post_tool_use.py
│   ├── 03_Lifecycle/          # Hooks de ciclo de vida
│   │   ├── stop.py
│   │   └── subagent_stop.py
│   └── 04_Sound/              # Notificaciones de audio
│       ├── notification.py
│       └── task-complete-sound.ps1
│
├── 02_Utils/                  # Utilidades compartidas
│   └── common.py              # speak(), visual_alert(), log_to_json()
│
├── 03_Validators/             # Validadores automáticos
│   └── csv-single-validator.py
│
└── README.md                  # Este archivo
```

---

## ⚡ Hooks Activos (6 hooks)

| Hook             | Trigger                         | Script                  | Función                          |
| ---------------- | ------------------------------- | ----------------------- | -------------------------------- |
| `PreToolUse`     | Antes de cada tool              | `pre_tool_use.py`       | Batería, seguridad, `rm -rf` block |
| `PreToolUse`     | Antes de cada tool              | `csv-single-validator.py` | Valida archivos CSV              |
| `PostToolUse`    | Después de modificar archivos   | `post_tool_use.py`      | Backup, voz, logs                |
| `Stop`           | Al cerrar sesión                | `stop.py`               | "Sesión finalizada"              |
| `SubagentStop`   | Al terminar sub-agente          | `subagent_stop.py`      | "Subagente completado"           |
| `UserPromptSubmit` | Cuando el usuario envía mensaje | `notification.py`       | Alerta visual + voz              |
| `TodoWrite`      | Al usar TodoWrite               | `task-complete-sound.ps1` | Sonido de completado             |

---

## 📋 Configuración en `settings.local.json`

```json
{
  "permissions": {
    "allow": [
      "Bash(ls:*)",
      "Bash(python3 -c \":*\")"
    ]
  },
  "hooks": {
    "PreToolUse": [
      { "hooks": [{ "type": "command", "command": "python .agent/04_Extensions/hooks/01_Pre_Tool/pre_tool_use.py" }] },
      { "hooks": [{ "type": "command", "command": "python .agent/04_Extensions/03_Validators/csv-single-validator.py" }] }
    ],
    "PostToolUse": [
      { "hooks": [{ "type": "command", "command": "python .agent/04_Extensions/hooks/02_Post_Tool/post_tool_use.py" }] }
    ],
    "Stop": [
      { "hooks": [{ "type": "command", "command": "python .agent/04_Extensions/hooks/03_Lifecycle/stop.py" }] }
    ],
    "SubagentStop": [
      { "hooks": [{ "type": "command", "command": "python .agent/04_Extensions/hooks/03_Lifecycle/subagent_stop.py" }] }
    ],
    "UserPromptSubmit": [
      { "hooks": [{ "type": "command", "command": "python .agent/04_Extensions/hooks/04_Sound/notification.py --notify" }] }
    ],
    "TodoWrite": [
      { "hooks": [{ "type": "command", "command": "powershell -ExecutionPolicy Bypass -NoProfile -WindowStyle Hidden -File .agent/04_Extensions/hooks/04_Sound/task-complete-sound.ps1" }] }
    ]
  }
}
```

---

## 🎯 Qué Hace Cada Hook

### 01_Pre_Tool/pre_tool_use.py

**Ejecuta ANTES de cada operación:**

| Check       | Condición   | Acción            |
| ----------- | ----------- | ----------------- |
| Batería     | < 15%       | Cancela operación |
| Destructivo | `rm -rf`    | Bloquea comando   |
| Seguridad   | `cat .env`  | Bloquea acceso    |

### 02_Post_Tool/post_tool_use.py

**Ejecuta DESPUÉS de modificar archivos:**

| Acción   | Detalle                                                  |
| -------- | -------------------------------------------------------- |
| Backup   | `.claude/backups/{file}_{timestamp}.bak`                 |
| Linters  | Print (Ruff/Prettier ready)                              |
| Voz      | Notifica cada 2 archivos (.md, .py, .json, .yaml, .toml) |

### 03_Validators/csv-single-validator.py

**Ejecuta ANTES de operar con archivos CSV:**

| Check      | Acción                       |
| ---------- | ---------------------------- |
| Extension  | Solo procesa `.csv`          |
| Estructura | Valida columnas consistentes |
| Empty      | Warning si archivo vacío     |

### 03_Lifecycle/stop.py

**Al cerrar sesión:**
- 🔊 "Sesión finalizada. Todos los procesos se han detenido correctamente."

### 03_Lifecycle/subagent_stop.py

**Al terminar sub-agente:**
- 🔊 "Subagente ha completado su tarea correctamente."

### 04_Sound/notification.py

**Cuando el usuario envía un mensaje:**
- 🔊 Síntesis de voz (System.Speech/SAPI)
- 🖥️ Alerta visual (msg.exe/MessageBox)

### 04_Sound/task-complete-sound.ps1

**Al usar TodoWrite:**
- 🔊 Sonido del sistema (Asterisk)

---

## 🔧 Variables de Entorno

| Variable                   | Default   | Descripción          |
| -------------------------- | --------- | -------------------- |
| `ENABLE_VOICE_NOTIFICATIONS` | `1`       | Toggle global de voz |
| `BYPASS_BATTERY_CHECK`     | `0`       | Skip battery check   |

---

## 🚀 Quick Commands

```bash
# Test sound
powershell -ExecutionPolicy Bypass -File ".agent/04_Extensions/hooks/04_Sound/task-complete-sound.ps1"

# Test notification
python .agent/04_Extensions/hooks/04_Sound/notification.py --notify

# Test pre-tool (skip battery)
BYPASS_BATTERY_CHECK=1 python .agent/04_Extensions/hooks/01_Pre_Tool/pre_tool_use.py

# Validate CSV manually
python .agent/04_Extensions/03_Validators/csv-single-validator.py archivo.csv

# View logs
type .claude\history\sessions\post_tool_use.json
```

---

## 🧹 Mantenimiento

### Limpiar Backups Viejos (> 7 días)

```bash
# PowerShell
Get-ChildItem .claude\backups\*.bak | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-7) } | Remove-Item

# Bash
find .claude/backups -name "*.bak" -mtime +7 -delete
```

### Desactivar Todos los Hooks

```json
{
  "disableAllHooks": true
}
```

---

## 📦 Silicon Valley Best Practices

| Practice               | Implementation                       |
| ---------------------- | ------------------------------------ |
| **Separación de Concerns** | Hooks categorizados por fase         |
| **DRY**                | `02_Utils/common.py` centraliza lógica |
| **Fail-Safe**          | Errores silenciados                  |
| **Async**              | `subprocess.Popen` no bloquea        |
| **Configurable**       | ENV vars para toggles                |
| **Testeable**          | Scripts standalone                   |

---

## 📊 Resumen Final

| Item           | Count   | Detail                                                       |
| -------------- | ------- | ------------------------------------------------------------ |
| **Hooks Activos** | 6       | PreTool, PostTool, Stop, SubagentStop, UserPrompt, TodoWrite |
| **Validaciones** | 3       | Battery, Destructive Commands, CSV Structure                 |
| **Notificaciones** | 2       | Voice (System.Speech), Sound (Windows)                       |
| **Logging**    | ✅       | JSON en `.claude/history/sessions/`                          |
| **Backup**     | ✅       | Auto en `.claude/backups/`                                   |

---

**Last Updated**: 2026-03-18  
**Version**: 2.0.0 — Full Integration  
**Maintainer**: Think Different AI System
