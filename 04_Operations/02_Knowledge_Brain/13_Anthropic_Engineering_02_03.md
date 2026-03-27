# Anthropic Engineering — Posts 8-13

> **Fecha:** 2026-03-26
> **Parte 2 de 3 archivos**

---

## 8. Effective Harnesses for Long-Running Agents

**Fecha:** Nov 26, 2025  
**Autor:** Justin Young

### Resumen

Agents still face challenges working across many context windows. Inspirado en ingenieros humanos, se creó un harness más efectivo para long-running agents.

### El Problema

- Agentes tienden a hacer too much at once — one-shot apps
- Agentes declaran victory prematuramente
- Context windows son limitados

### Solución: Two-Part

**1. Initializer Agent:**
- Primer session configura el ambiente
- Crea feature list (200+ features en JSON)
- init.sh script
- claude-progress.txt file

**2. Coding Agent:**
- Sessions subsecuentes trabajan incrementalmente
- Una feature a la vez
- Commit descriptivo a git
- Actualiza progress file

### Failure Modes y Soluciones

| Problema                                | Solución                            |
|-----------------------------------------|-------------------------------------|
| Declara victory muy temprano            | Feature list con todos los features |
| Ambiente con bugs                       | Git commits + progress updates      |
| Marca features como done prematuramente | Self-verify todos los features      |

### Clave

- **Incremental progress:** Una feature a la vez
- **Clean state después de cada sesión:** Git commit + documentation
- **Testing end-to-end:** Usar browser automation (Puppeteer MCP)

---

## 9. Introducing Advanced Tool Use on Claude Developer Platform

**Fecha:** Nov 24, 2025  
**Autor:** Anthropic Team

### Resumen

Advanced tool use capabilities en Claude Developer Platform. Nuevas features para building agents más capaces.

### Features

- **Computer use:** Claude puede interacturar con computers como humanos
- **Browser automation:** Navegación web completa
- **MCP integration:** Model Context Protocol para tools externos

---

## 10. Code Execution with MCP: Building More Efficient Agents

**Fecha:** Nov 04, 2025  
**Autor:** Anthropic Team

### Resumen

Cómo usar code execution con MCP para build agents más eficientes.

### Beneficios

- Agents pueden ejecutar código para verificar soluciones
- Testing automatizado inline
- Debugging más efectivo

---

## 11. Beyond Permission Prompts: Making Claude Code More Secure and Autonomous

**Fecha:** Oct 20, 2025  
**Autor:** Anthropic Team

### Resumen

Evolución de la seguridad en Claude Code. De permission prompts a sandboxing y auto mode.

### Journey

1. **Manual prompts:** Todo requería aprobación
2. **Sandboxing:** Aislamiento de operaciones peligrosas
3. **Auto mode:** Clasificadores que deciden automáticamente

---

## 12. Effective Context Engineering for AI Agents

**Fecha:** Sep 29, 2025  
**Autor:** Anthropic Team

### Resumen

Técnicas para managear contexto efectivamente en AI agents.

### Conceptos Clave

- **Context window management:** Cómo usar el espacio de contexto eficientemente
- **Compaction:** Resumir conversaciones anteriores
- **Progressive disclosure:** Revelar información gradualmente
- **Tool use optimization:** Cuándo y cómo usar tools

---

## 13. A Postmortem of Three Recent Issues

**Fecha:** Sep 17, 2025  
**Autor:** Anthropic Team

### Resumen

Análisis de tres issues recientes en producción. Lecciones aprendidas.

### Issues Típicos

- Memory leaks en long-running agents
- Tool call failures silenciosos
- Context contamination entre sesiones

---

## FEEDBACK: ¿Qué Nos Falta Implementar?

### DEL ANÁLISIS DE LOS ARTÍCULOS, IMPLEMENTAR:

| #   | Concepto del Artículo                       | Status en Nuestro OS      | Acción                             |
|-----|---------------------------------------------|---------------------------|------------------------------------|
| 1   | **Auto Mode Security** (Post 2)             | ⏳ NO implementado         | Crear skill de security classifier |
| 2   | **Evaluator/Generator Separation** (Post 3) | ✅ Ya en Anthropic Harness | Nada                               |
| 3   | **Eval Awareness Detection** (Post 4)       | ⏳ NO implementado         | Hook para detectar                 |
| 4   | **Agent Teams con Locks** (Post 5)          | ⏳ Parcial                 | Extender con git locks             |
| 5   | **Feature List como JSON** (Post 8)         | ⏳ NO implementado         | Nuevo script                       |
| 6   | **Progress File** (Post 8)                  | ⏳ NO implementado         | Template + script                  |
| 7   | **End-to-End Testing con Browser** (Post 8) | ✅ Playwright ya           | Nada                               |
| 8   | **pass@k metrics** (Post 7)                 | ⏳ NO implementado         | Script de métricas                 |
| 9   | **Graders (code/model/human)** (Post 7)     | ⏳ Parcial                 | Definir framework                  |
| 10  | **Multi-agent con roles** (Post 5)          | ⏳ NO implementado         | Nuevo workflow                     |

---

*Continúa en archivo 13_Anthropic_Engineering_02_03.md*
