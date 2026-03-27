# Notion

> **Categoría:** Knowledge (Tier 2)
> **Uso:** Proyectos y tareas en Notion

## Descripción

Integración con Notion para gestión de proyectos y bases de datos.

## Uso Principal

```bash
# Buscar páginas
query: "CV Jesus Obando"

# Listar databases
database_id: "proyectos"
```

## Configuración

```json
"Notion": {
  "command": "npx.cmd",
  "args": ["-y", "@notionhq/notion-mcp-server@latest"],
  "env": {
    "NOTION_TOKEN": "ntn_..."
  }
}
```

## Casos de Uso

- 📋 Gestión de proyectos
- 📊 Bases de datos
- 📝 Notas colaborativas

---

*Tier 2 - Knowledge*
