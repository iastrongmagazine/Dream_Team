# Receta: Auditoría SEO y de Contenido

Este escenario permite delegar la auditoría SEO y de contenido de una página web a un agente aislado, evitando que el chat principal se sature con reportes técnicos extensos.

## 🎯 Caso de Uso

Ideal para:

- Analizar competidores.
- Auditar landings antes de publicar.
- Revisar posts de blog para asegurar calidad SEO.

## 📋 Prerrequisitos

- Tener instalado `fork-terminal`.
- (Opcional) Acceso a herramientas CLI de SEO si se desea ir más allá de la demo.

## 🛠️ Workflow

### 1. Preparar la tarea

El agente principal debe identificar:

- **URL Objetivo**: La página a analizar.
- **Keywords**: Las palabras clave a verificar.

### 2. Comando de Ejecución

Usar `fork_terminal` para lanzar el agente de marketing.

**Sintaxis:**

```bash
python 01_Core/03_Skills/fork-terminal/tools/fork_terminal.py "python 01_Core/03_Skills/fork-terminal/examples/marketing_agent_demo.py"
```

### 3. Ejemplo de Prompt para el Usuario

Si el usuario dice: _"Analiza el SEO de mi landing page"_, el agente debería responder:

> "Entendido. Voy a lanzar un agente de marketing especializado en un terminal separado para auditar tu landing page. Esto me permitirá entregarte un reporte limpio sin llenar nuestro chat de datos técnicos intermedios."

## 💡 Personalización

Puedes modificar `marketing_agent_demo.py` para incluir llamadas a APIs reales como:

- Google PageSpeed Insights API
- SEMRush API
- OpenAI API (para análisis de sentimiento o sugerencias de redacción)

---

**Nota:** Esta receta utiliza un script de demostración (`marketing_agent_demo.py`) que simula el proceso. Para uso en producción, reemplaza la simulación con lógica real de scraping y análisis.
