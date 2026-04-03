# 02_Task: Reconstrucción OpenCode (Pure Green)

- `[ ]` **Fase 1: Continuar con el Respaldo Preventivo**
  - `[ ]` Crear `C:\Users\sebas\.config\opencode\opencode.json.bak`
  - `[ ]` Crear `01_Core/05_Mcp/02_OpenCode/opencode.json.bak`

- `[ ]` **Fase 2: Purga Quirúrgica y Reconstrucción**
  - `[ ]` Eliminar clave `"plugins"` de `~/.config/opencode/opencode.json`.
  - `[ ]` Re-formatear JSON para asegurar sintaxis válida.
  - `[ ]` Inyectar definiciones verificadas para `exa`, `Notion`, `supadata`, `firecrawl`, etc.

- `[ ]` **Fase 3: Sincronización y Validación Global**
  - `[ ]` Sobrescribir `01_Core/05_Mcp/02_OpenCode/opencode.json` con la versión limpia.
  - `[ ]` Ejecutar `python 08_Scripts_Os/09_Integration/46_Sync_MCP_OpenCode.py`.
  - `[ ]` Verificar `opencode --help`.
  - `[ ]` Documentar el estado Pure Green en `walkthrough.md`.
