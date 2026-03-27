# 🤖 AI Agents Course - Remy Gasill

> **Fuente:** YouTube - (17) Creación de agentes de IA que realmente funcionan (Curso completo)
> **Video:** https://www.youtube.com/watch?v=eA9Zf2-qYYM
> **Fecha:** 2026-03-25

---

## 📚 Conceptos Fundamentales

### 1. Chat vs Agent

| Chat                    | Agent                                 |
|-------------------------|---------------------------------------|
| Question → Answer       | Goal → Result                         |
| Ping-pong (uno por uno) | Loop continuo                         |
| Termina en 1 respuesta  | Planifica, ejecuta, entrega resultado |

### 2. Agent Loop (El corazón del agente)

```
Goal → Observe → Think → Act → Repeat → Complete
```

- **Observe**: Revisa contexto, archivos, herramientas disponibles
- **Think**: Decide qué hacer下一步
- **Act**: Ejecuta la acción
- **Repeat**: Repite hasta que la tarea esté completa

### 3. Componentes de un Agente

| Componente    | Descripción                                       |
|---------------|---------------------------------------------------|
| **LLM**       | Cerebro: Claude, GPT, Gemini, etc.                |
| **Loop**      | Continúa hasta完成任务 (no se detiene en 1 respuesta) |
| **Tools**     | Conexiones MCP a herramientas externas            |
| **Context**   | Archivos .md con información del negocio          |

---

## 📁 Archivos Clave

### agents.md / claude.md
- System prompt / contexto permanente
- Rol del agente
- Info sobre ti y tu negocio
- Preferencias de trabajo
- **Se carga en cada sesión** como parte del observe step

### memory.md
- **Persiste preferencias entre sesiones**
- Guarda correcciones ("no uses cheers, usa warm regards")
- Se actualiza automáticamente cuando corriges al agente
- **Importante**: No todo va aquí, solo preferencias importantes

### Skills (SOPs para AI)
- Procesos empaquetados
- Una vez creado, nunca más hace falta explicar el proceso
- Se crean usando el **skill creator** o manualmente después de un proceso

---

## 🔌 MCP - Model Context Protocol

### Qué es MCP
- **Traductor universal** entre LLM y herramientas
- Antes: Claude (inglés) → Notion (español) → Gmail (francés) → requerían desarrollos complejos
- Ahora: MCP traduce automáticamente

### Cómo conectar tools
```bash
# En Claude Code / Co-Work / Anti-Gravity:
Connectors → Browse Connectors → Gmail, Calendar, Notion, Stripe, Granola
```

---

## 🏗️ Estructura de Carpetas Sugerida

```
Mi_Empresa/
├── claude.md           # Contexto global
├── memory.md           # Memoria global
├── executive_assistant/
│   ├── claude.md       # Rol: Asistente ejecutivo
│   ├── memory.md       # Preferencias específicas
│   └── skills/         # Skills del asistente
├── head_of_marketing/
│   ├── claude.md       # Rol: Director de marketing
│   └── skills/
│       ├── viral_hooks/
│       └── ads_analysis/
└── content_team/
    └── skills/
```

---

## 🎯 Tips Prácticos

### Onboarding de un agente (como empleado real)
1. **No esperes que sepa todo** - dale contexto primero
2. **agents.md** = contrato de trabajo
3. **memory.md** = preferencias que aprende
4. **Skills** = procesos que domina

### Mejores prácticas
- Mantener `claude.md` en ~200 líneas máximo
- Solo guardar cosas sustanciales en memory.md
- Crear skills para TODO proceso repetitivo
- Skills pueden encadenarse (skill chaining)

### Automatización
- **Scheduled Tasks**: Ejecutar skills en horarios específicos
- Ejemplo: "Morning brief" a las 9:00 AM diario
- Scraping automático de marketplaces

---

## 🔗 Herramientas Mentionadas

| Herramienta       | Tipo           | Notas                       |
|-------------------|----------------|-----------------------------|
| Claude Code       | Agent Harness  | Desktop app                 |
| Co-Work           | Agent Harness  | UI simple para beginners    |
| Anti-Gravity      | Agent Harness  | Similar a Claude Code       |
| OpenCode/OpenCore | Agent Harness  | Más autonomía, más complejo |
| Perplexity        | Search + Agent | Investigación automática    |
| Granola           | Tool           | Meeting notes               |
| Notion            | Tool           | Project management          |
| Stripe            | Tool           | Pagos                       |
| Gmail             | Tool           | Email                       |

---

## 💡 Quotes Importantes

> "Chat is question to answer. Agent is goal to result."

> "Context engineering > Prompt engineering"

> "Once you explain something once, you never have to explain it ever again."

> "Everyone will have an AIOS - AI Operating System"

---

## 🔄 Aplicación a PersonalOS

Este curso valida la arquitectura actual de PersonalOS:
- ✅ Estructura de carpetas por rol (executive_assistant, head_of_marketing)
- ✅ Uso de claude.md como contexto
- ✅ Skills en carpetas separadas
- ✅ MCP para conectar herramientas
- ✅ Memory para persistir preferencias

**Próximo paso:** Implementar los patrones de este curso en las skills SOTA-MCP.
