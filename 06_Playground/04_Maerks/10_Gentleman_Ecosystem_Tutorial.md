# 🔬 ECOSISTEMA de IA que le falta a tu agente

> **Fuente:** YouTube - "El ECOSISTEMA de IA que le falta a tu agente | Engram + SDD + Skills | Tutorial Completo"
> **Fecha:** 2026-03-26
> **Tipo:** Oro Puro - Configuración de Ecosystem

---

## 📊 Resumen del Video

| Tema            | Descripción                                          |
|-----------------|------------------------------------------------------|
| **Creador**     | Gentleman (Alan)                                     |
| **Stack**       | Engram + SDD + Skills + MCPs                         |
| **Instalación** | `brew install gentelman/gentleman/ai`                |
| **Soporte**     | Windows, Linux, macOS                                |
| **Agentes**     | Claude Code, OpenCode, Gemini, Cursor, Codex, VSCode |

---

## 🏗️ Componentes del Ecosystem

### 1. Engram — Cerebro Virtual

> "Todo lo que vos vas haciendo con la IA lo aprende"

**Funcionalidades:**
- Memoria persistente entre sesiones
- Guardar decisiones de arquitectura
- Recordar bugs y cómo se arreglaron
- Captura automática de conversaciones

**Niveles de acceso:**
1. Busca información de proyecto
2. Busca tipos de acciones
3. Busca detalles completos

**Privacidad:**
- Detecta secrets → los marca como private
- Nunca llegan a la DB

### 2. SDD — Spec-Driven Development

> "Desarrollo basado en especificaciones"

**Fases:**
```
explore → propose → spec → design → tasks → apply → verify → archive
```

**Beneficios:**
- Menos alucinaciones
- Menos ciclos de corrección
- 50-70% ahorro de tokens
- Código versionable y reanudable

### 3. Skills — Contexto Modular

> "Partículas de contexto que se cargan por necesidad"

**Cuándo crear una skill:**
- Algo repetitivo
- Algo particular del proyecto
- Patrones propios

### 4. MCPs — Herramientas

**Recomendados:**
- **context7** — Docs de librerías
- **Notion** — Proyectos
- **shadcn/ui** — Componentes

### 5. OpenSpec — Especificaciones IA

> "Specs legibles por IA"

**Características:**
- Sin ambigüedades
- Versionables
- Eficientes en tokens

---

## 💡 Conceptos Clave

### Orchestrator Principal

- Delega a subagentes
- Mantiene el hilo de la conversación
- **50-70% ahorro de tokens** vs sesión única

### Subagentes

- Hoja en blanco (blank slate)
- Menos ruido
- Más eficientes
- Menos errores

### Human in the Loop

> "Son los que llevan la rienda. No dejen que la IA los maneje."

**Cuándo usar:**
- Antes de continuar si algo no tiene sentido
- Revisar código al final
- Validar cada fase

---

## 🔧 Instalación

```bash
# Con homebrew (recomendado)
brew install gentelmanprogrammingtap/gentlemanai

# O manual
git clone repositorio
./scripts/install.sh
```

### Configuración

| Opción    | Descripción                           |
|-----------|---------------------------------------|
| Voice     | Hablar como Alan / Neutral / Custom   |
| Ecosystem | Full gentleman / Solo Engram / Custom |

---

## 🎯 Modelos Recomendados por Fase

| Fase           | Modelo            | Razón                |
|----------------|-------------------|----------------------|
| Inicializar    | Sonnet            | Rápido               |
| Explorar       | Sonnet            | Rápido               |
| Propuesta      | Opus / Gemini 2.0 | Alto razonamiento    |
| Especificación | Google            | Documentación clara  |
| Diseño         | Opus              | Razonamiento técnico |
| Tareas         | Sonnet            | Liviano              |
| Implementar    | Sonnet / 5.4      | Eficiente            |
| Verificar      | 5.4               | Bug detection        |
| Archivar       | Sonnet            | Liviano              |

**Nota:** "Gemini es un desastre para implementar, pero excellent para razonamiento y documentación"

---

## 🌐 Multi-Agente

- Múltiples subagentes en paralelo
- Asíncronos
- Cada uno con su propia ventana de contexto

---

## 🔗 Links

- [Repositorio Principal](https://github.com/gentleman-programming)
- [Engram](https://github.com/gentleman-programming/engram)
- [Agent Teams Lite](https://github.com/gentleman-programming/agent-teams-lite)
- [Stripe Minions - Agentic Engineering](https://www.youtube.com/watch?v=stripe-minions)
- [Firecrawl AI - Cómo ganar dinero](https://www.youtube.com/watch?v=eH8JdttKIdA)

---

## 📝 Notas Personales

> "La IA no tiene límites. Los límites los tenemos que descubrir."
> — Alan (Gentleman)

---

*Análisis generado: 2026-03-26*
*Fuente: YouTube Transcript*
