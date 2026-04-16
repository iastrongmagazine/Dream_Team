# 📝 SOP Prompt: 05_Mcp

> **Carpeta destino:** `01_Core/05_Mcp/`
> **Complementa:** `01_Core/05_Mcp/opencode.json`, `01_Core/05_Mcp/mcp.json`

---

## 🎯 Propósito del Prompt

Crear una configuración MCP (Model Context Protocol) completa para integrar herramientas externas en PersonalOS.

---

## 📋 Prompt Base (Copy-Paste)

```
Eres un Especialista en MCP. Crea una configuración MCP completa para PersonalOS.

## 📍 Contexto del Proyecto
- **Nombre de la herramienta:** [NOMBRE_HERRAMIENTA]
- **Tipo:** [SEARCH/API/TOOL/DATA_SOURCE]
- **Carpeta destino:** `01_Core/05_Mcp/`

## 📂 Estructura Requerida
Guardar en: `01_Core/05_Mcp/[HERRAMIENTA].json` o actualizar `opencode.json`

## 📝 Estructura del Documento

```json
{
  "mcpServers": {
    "[nombre]": {
      "command": "[comando]",
      "args": ["[arg1]", "[arg2]"],
      "env": {
        "VARIABLE": "valor"
      }
    }
  }
}
```

## 📋 Configuración .MD ( Complemento)

Crear también: `01_Core/05_Mcp/00_Config_Mcp/[HERRAMIENTA]/README.md`

```markdown
# [Nombre de la Herramienta MCP]

## 🎯 Propósito
[Qué hace esta herramienta]

## 🔧 Configuración
- **Comando:** `[comando]`
- **Args:** `[args]`
- **Variables:** `[variables]`

## 📦 Dependencias
- [Paquete 1]
- [Paquete 2]

## ✅ Verificación
```bash
[Comando de test]
```

## 🔗 Integración
- **Skills que lo usan:** `[ruta]`
- **Agents que lo usan:** `[ruta]`
```

## 🛠️ Mejores Prácticas

### Seguridad
- [ ] NO hardcodear API keys en JSON
- [ ] Usar variables de entorno
- [ ] No exponer credenciales en logs

### Configuración
- [ ] Documentar variables requeridas
- [ ] Proporcionar valores por defecto seguros
- [ ] Validar al iniciar

## ✅ Checklist de Calidad

- [ ] JSON válido
- [ ] Variables de entorno documentadas
- [ ] README con verificación
- [ ] No hardcodea credenciales
- [ ] Test de conexión incluido
