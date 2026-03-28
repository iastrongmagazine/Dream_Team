# 🗄️ Tool Shed - MCPs Organizados por Dominio

> **Fecha:** 2026-03-26
> **Inspiración:** Stripe Minions - Tool Shed Pattern

---

## 📊 Resumen

| Tier | Categoría | MCPs | Estado |
|------|-----------|------|--------|
| 01 | Core (siempre activas) | context7, engram, github | ⭐ |
| 02 | Knowledge | obsidian, notion, aim-memory | |
| 03 | Development | playwright, docker, chrome | |
| 04 | Research | firecrawl, exa, supabase | |
| 05 | Visual | excalidraw, pencil | |
| 06 | Productivity | linear, slack, jira | |

---

## 🚀 Quick Reference

### Para coding:
- context7 → Docs de librerías
- github → Repo management

### Para research:
- firecrawl → Web scraping
- exa → Búsqueda web

### Para knowledge:
- engram → Memoria persistente
- obsidian → Notas locales
- notion → Proyectos

### Para testing:
- playwright → E2E testing

---

## 📁 Estructura

```
mcp-tools/
├── 01_core/           # Siempre activas
├── 02_knowledge/      # Notas y memoria
├── 03_development/     # Coding y testing
├── 04_research/       # Investigación web
├── 05_visual/         # Diagramas
└── 06_productivity/   # Gestión de proyectos
```

---

## 🔗 Archivo de Configuración

Las MCPs están configuradas en: `.claude/mcp.json`

---

## 💡 Concepto: Tool Shed

Inspirado en Stripe Minions:
- **Meta-tool** que selecciona herramientas relevantes por contexto
- **Carga selectiva** para evitar token explosion
- **Auto-discovery** de herramientas

---

*Tool Shed v1.0 - Think Different AI*
