# 01_Plan: Restauración Quirúrgica OpenCode (Pure Green)

Este plan detalla la restauración de `opencode.json` tras detectar una corrupción de sintaxis y la inclusión de la clave no reconocida `"plugins"`. El objetivo es volver al estado **Pure Green** sin perder ninguna configuración válida de servidores MCP.

## 🛡️ Garantía de "Zero De-Configuration"
Se han identificado y se preservarán los siguientes servidores activos:
- **exa**: Búsqueda web (Verified).
- **Notion**: Integración de bases de datos (Verified).
- **firecrawl-mcp**: Scraping (Verified).
- **task-master-ai**: Productividad (Recuperado de mcp.json).
- **supadata**: Research (Recuperado de mcp.json).
- **zai-mcp-server**: AI Logic (Recuperado de mcp.json).
- **excalidraw-yctimlin**: Visual (Verified).

## 📋 Propuesta de Cambios

### OpenCode Configuration

#### [MODIFY] [opencode.json](file:///C:/Users/sebas/.config/opencode/opencode.json)
- **Eliminar**: La clave raíz `"plugins"` (Causa del error `Unrecognized key`).
- **Corregir**: Sintaxis JSON (braces y comillas mal cerradas).
- **Restaurar**: La sección `mcpServers` (o `mcp` según versión) con las definiciones limpias.

#### [MODIFY] [opencode.json](file:///c:/Users/sebas/Downloads/01%20Revisar/09%20Versiones/00%20Respaldo%20PC%20Sebas/01%20Github/personal-os/Think_Different/01_Core/05_Mcp/02_OpenCode/opencode.json)
- Sincronizar la configuración limpia al núcleo del proyecto para garantizar la persistencia del estado Pure Green.

### Integration Layer

#### [EXECUTE] [46_Sync_MCP_OpenCode.py](file:///c:/Users/sebas/Downloads/01%20Revisar/09%20Versiones/00%20Respaldo%20PC%20Sebas/01%20Github/personal-os/Think_Different/08_Scripts_Os/09_Integration/46_Sync_MCP_OpenCode.py)
- Ejecutar el script oficial de sincronización para validar la integridad del ecosistema tras la reparación manual.

## 🧪 Plan de Verificación

### Pruebas de Sistema
1. Ejecutar `opencode --help` para confirmar la recuperación del CLI.
2. Ejecutar `python 08_Scripts_Os/07_Integration_Hub.py mcp-sync` para validar la coherencia global.

## ❓ Preguntas Abiertas
- ¿Hay algún token de `EXA_API_KEY` o `NOTION_TOKEN` que deba actualizarse durante esta restauración, o mantenemos los actuales detectados en el sistema?
