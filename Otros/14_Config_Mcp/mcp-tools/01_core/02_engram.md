# engram

> **Categoría:** Core (Tier 1)
> **Uso:** Memoria persistente entre sesiones

## Descripción

Sistema de memoria persistente que sobrevive entre sesiones de Claude Code.

## Uso Principal

```bash
# Guardar contexto
mem_save(title, content, type, project)

# Buscar memoria
mem_search(query, project)

# Recuperar observación
mem_get_observation(id)
```

## Configuración

```json
"engram": {
  "transport": "stdio",
  "command": "./05_System/05_Core/Engram/engram.exe",
  "args": ["mcp"]
}
```

## Casos de Uso

- 💾 Guardar decisiones de arquitectura
- 🔍 Recordar trabajo de sesiones anteriores
- 📝 Mantener contexto de proyectos

---

*Tier 1 - Siempre activa*
