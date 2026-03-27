# 📚 Mejores Prácticas de Claude - Blog Oficial

## 🎯 Resumen Ejecutivo

Este documento recopila las mejores prácticas oficiales de Anthropic para construir agentes y workflows efectivos con Claude, extraídas del blog oficial.

* *Última actualización**: 2026-03-10
* *Fuente**: https://claude.com/blog

- --

## 🔄 Patrones de Workflow para Agentes AI

### 1. Workflow Secuencial (Sequential)

* *Cuándo usar:**
- Tareas con dependencias claras donde el paso B necesita el output del paso A
- Procesos de múltiples etapas (data pipelines, draft-review-polish)
- Transformaciones de datos donde cada etapa agrega valor específico

* *Ejemplos:**
- Generar copy de marketing → traducir a múltiples idiomas
- Extraer datos de documentos → validar contra schema → cargar en base de datos
- Pipeline de moderación: extraer contenido → clasificar → aplicar reglas → enrutar

* *Tradeoffs:**
- ✅ Mejora la precisión al enfocar cada agente en una subtarea específica
- ❌ Añade latencia (cada paso espera el anterior)

* *Pro Tip:** Primero intenta con un solo agente. Si es suficiente, no añadas complejidad innecesaria.

### 2. Workflow Paralelo (Parallel)

* *Cuándo usar:**
- Subtareas independientes que beneficien de procesamiento simultáneo
- Múltiples perspectivas sobre el mismo problema
- Separación de preocupaciones (diferentes equipos pueden optimizar agentes independientemente)

* *Ejemplos:**
- Evaluación automática (cada agente verifica diferentes métricas de calidad)
- Code review (múltiples agentes examinan diferentes categorías de vulnerabilidades)
- Análisis de documentos (extracción de temas, análisis de sentimiento, verificación factual en paralelo)

* *Tradeoffs:**
- ✅ Velocidad mejorada y separación de preocupaciones
- ❌ Costo mayor (múltiples llamadas API concurrentes)

* *Pro Tip:** Diseña tu estrategia de agregación ANTES de implementar. ¿Votación mayoritaria? ¿Promedio de confianza? ¿Deferir al agente más especializado?

### 3. Workflow Evaluator-Optimizer (Evaluador-Optimizador)

* *Cuándo usar:**
- Calidad inicial no es suficiente
- Criterios de calidad medibles y objetivos
- Mejora iterativa justifica el costo adicional

* *Ejemplos:**
- Documentación técnica (generar docs → verificar completitud y claridad)
- Comunicaciones profesionales (redactar email → evaluar tono y cumplimiento)
- Consultas SQL (escribir query → verificar eficiencia y seguridad)

* *Tradeoffs:**
- ✅ Salidas de mayor calidad mediante bucles de feedback estructurados
- ❌ Multiplica uso de tokens y añade tiempo de iteración

* *Pro Tip:** Define criterios de parada claros ANTES de empezar. Límites de iteraciones y umbrales de calidad específicos.

- --

## 🏗️ Arquitectura de Code Review con Agentes

### Sistema de Review Multi-Agente

* *Patrón implementado por Anthropic:**
1. **Fan-out**: Disparar múltiples agentes en paralelo para buscar bugs
2. **Verificación**: Agentes verifican bugs para filtrar falsos positivos
3. **Ranking**: Clasificar bugs por severidad
4. **Fan-in**: Consolidar resultados en un único comentario overview

* *Resultados internos de Anthropic:**
- Antes: 16% de PRs recibían comentarios sustanciales
- Ahora: 54% de PRs reciben comentarios sustanciales
- PRs grandes (>1000 líneas): 84% encuentran issues (promedio 7.5)
- PRs pequeños (<50 líneas): 31% encuentran issues (promedio 0.5)
- Menos del 1% de findings marcados como incorrectos

* *Costo promedio:** $15-25 por review (escala con tamaño y complejidad del PR)

### Control de Costos

- **Límites mensuales por organización**: Definir gasto total mensual
- **Control a nivel de repositorio**: Habilitar reviews solo en repos específicos
- **Dashboard analítico**: Track de PRs revisados, tasa de aceptación, costo total

- --

## 📊 Métricas de Impacto

### Para Code Review

- **Coverage**: % de PRs que reciben review sustancial
- **Precision**: % de findings correctos (menos de 1% falsos positivos en Anthropic)
- **ROI**: bugs críticos capturados antes de merge

### Para Workflows

- **Latencia**: Tiempo total de ejecución vs. agente único
- **Costo**: Tokens usados vs. calidad mejorada
- **Calidad**: Métricas objetivas vs. baseline de agente único

- --

## 🎯 Reglas de Decisión

### ¿Cuándo usar workflows vs. agente único?

1. **Intenta con agente único primero** - Si funciona, no añadas complejidad
2. **Identifica dónde falla** - Latencia? Calidad? Capacidad?
3. **Elige el patrón apropiado**:
   - Dependencias claras → Secuencial
   - Tareas independientes + bottleneck de latencia → Paralelo
   - Calidad insuficiente + criterios medibles → Evaluator-Optimizer

### Combinación de Patrones

- Un workflow evaluator-optimizer puede usar evaluación paralela
- Un workflow secuencial puede incluir procesamiento paralelo en ciertas etapas
- **Regla**: La complejidad debe justificarse con beneficios medibles

- --

## 🛠️ Agent Skills - Habilidades Especializadas

### Anatomía de una Skill

Una skill es un directorio que contiene un archivo `SKILL.md` con:
1. **Metadata (YAML frontmatter)**: `name` y `description` - cargados en el prompt del sistema al inicio
2. **Cuerpo principal**: Instrucciones detalladas que Claude carga solo cuando es relevante
3. **Archivos vinculados**: Recursos adicionales que Claude puede navegar bajo demanda

### Principio de Divulgación Progresiva

- **Nivel 1**: Metadata básica (siempre cargada)
- **Nivel 2**: Contenido principal de SKILL.md (cargado cuando es relevante)
- **Nivel 3+**: Archivos vinculados (navegados solo cuando necesario)

### Ejemplo: Skill de PDF

```yaml
- --
name: pdf-skill
description: Habilidades para manipular documentos PDF
- --
```
- Permite a Claude llenar formularios PDF
- Incluye scripts Python para extraer campos de formularios
- Mantiene el núcleo de la skill ligero mediante división de archivos

### Desarrollo de Skills

1. **Empieza con evaluación**: Identifica gaps específicos en tus agentes
2. **Estructura para escalar**: Divide contenido cuando SKILL.md se vuelva demasiado grande
3. **Piensa desde la perspectiva de Claude**: Monitoriza cómo usa la skill en escenarios reales
4. **Itera con Claude**: Pídele que capture enfoques exitosos y errores comunes en skills reutilizables

### Consideraciones de Seguridad

- Instala solo skills de fuentes confiables
- Audita skills antes de usarlos (lee archivos y dependencias de código)
- Verifica instrucciones que conecten a fuentes externas no confiables

### Skills vs. Context Window

- Las skills permiten cargar información solo cuando se necesita
- El tamaño de contexto es effectively ilimitado
- Claude carga la metadata de todas las skills al inicio, pero solo lee el contenido cuando es relevante

- --

## 📋 Checklist para Implementación

### Antes de Empezar

- [ ] ¿Puede un agente único manejar la tarea efectivamente?
- [ ] ¿Identificaste dónde falla el enfoque actual?
- [ ] ¿Tienes métricas base para medir mejora?

### Durante la Implementación

- [ ] Define estrategia de agregación (para workflows paralelos)
- [ ] Establece criterios de parada claros (para evaluator-optimizer)
- [ ] Implementa manejo de fallos y retry logic
- [ ] Considera restricciones de latencia y costo
- [ ] Diseña skills con divulgación progresiva para escabilidad

### Después de Implementar

- [ ] Mide mejora vs. baseline de agente único
- [ ] Ajusta parámetros basado en métricas reales
- [ ] Documenta tradeoffs y decisiones de arquitectura
- [ ] Monitoriza uso de skills en escenarios reales

- --

## 🔗 Referencias

- **Blog Oficial**: https://claude.com/blog
- **Artículo de Workflows**: https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
- **Artículo de Code Review**: https://claude.com/blog/code-review
- **Artículo de Agent Skills**: https://claude.com/blog/equipping-agents-for-the-real-world-with-agent-skills
- **White Paper**: "Building effective AI agents: architecture patterns and implementation frameworks"

- --

## 📝 Notas del Sistema

- Este documento se sincroniza automáticamente con el blog de Claude
- Las mejores prácticas se integran en los workflows de SDD
- Los agentes de revisión usan estos patrones para evaluación de código
