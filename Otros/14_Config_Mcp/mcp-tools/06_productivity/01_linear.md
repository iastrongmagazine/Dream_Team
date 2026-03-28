# Linear

> **Categoría:** Productivity (Tier 6)
> **Uso:** Issue tracking y project management

## Descripción

Integración con Linear para gestión de issues.

## Uso Principal

```bash
# Crear issue
title: "Fix login bug"
team: "engineering"

# Listar issues
filter: "assigned_to_me"
```

## Configuración

```json
"Linear": {
  "transport": "streamableHttp",
  "url": "https://mcp.linear.app/mcp",
  "headers": {
    "Authorization": "Bearer lin_api_..."
  }
}
```

## Casos de Uso

- 📋 Gestión de issues
- 🗺️ Roadmaps
- 📊 Project tracking

---

*Tier 6 - Productivity*
