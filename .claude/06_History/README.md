# 📜 .claude/history — Registro de Sesiones

Historial de logs generados por los hooks del sistema.

---

## 🏗️ Estructura

```
.claude/history/
├── sessions/
│   ├── pre_tool_use.json     # Log de PreToolUse hook
│   ├── post_tool_use.json    # Log de PostToolUse hook
│   ├── stop.json             # Log de Stop hook
│   ├── subagent_stop.json    # Log de SubagentStop hook
│   ├── notification.json     # Log de notificaciones
│   └── voice_state.json      # Estado del contador de voz
│
└── README.md                # Este archivo
```

---

## 📋 Formato de Logs

Cada log es un **array JSON** con entradas:

```json
[
  {
    "timestamp": "2026-03-18T12:30:45.123456",
    "data": {
      "action": "allow",
      "command": "write file.txt",
      "reason": null
    }
  },
  {
    "timestamp": "2026-03-18T12:35:22.456789",
    "data": {
      "action": "block",
      "command": "cat .env",
      "reason": "security_file"
    }
  }
]
```

---

## 🔍 Ver Logs

```bash
# Ver pre-tool logs
type .claude\history\sessions\pre_tool_use.json

# Ver último entry
jq -s '.[-1]' .claude/history/sessions/pre_tool_use.json

# Contar entries
jq 'length' .claude/history/sessions/pre_tool_use.json
```

---

## 🧹 Mantenimiento

### Limpiar logs viejos (> 7 días)

```bash
# PowerShell
Get-ChildItem .claude\history\sessions\*.json | Where-Object { $_.LastWriteTime -lt (Get-Date).AddDays(-7) } | Remove-Item

# Bash
find .claude/history/sessions -name "*.json" -mtime +7 -delete
```

### Limpiar todos los logs

```bash
# Mantener voice_state.json
Remove-Item .claude\history\sessions\*.json -Exclude voice_state.json
```

---

## 📊 Análisis

### Contar acciones por tipo

```bash
# Pre-tool: allow vs block
jq '[.[].data.action] | group_by(.) | map({action: .[0], count: length})' pre_tool_use.json

# Post-tool: archivos más modificados
jq '[.[].data.target_file] | map(split("/") | .[-1]) | group_by(.) | map({file: .[0], count: length}) | sort_by(.count) | reverse' post_tool_use.json
```

---

## 🔗 Integración

Este historial se usa para:
- Debug de hooks
- Auditoría de comandos bloqueados
- Tracking de archivos modificados
- Análisis de patrones de uso

---

**Auto-generado**: 2026-03-18  
**Sistema**: Think Different AI Extensions
