# VIDEO ANALYSIS REPORT: PM + Agent Team - What Could Go Wrong?

**Date:** 2026-04-03  
**Source:** [Product School Live / O Corres o Te Encaramas](https://www.youtube.com/live/3psHUg6KzOo?si=Y6bZACLup04IfPCF)  
**Host:** Aníbal  
**Guest:** Ariel Contreras (Head of Product)

---

## 1. RESUMEN DEL VIDEO (Executive Summary)

El video explora la transformación radical del rol de Product Manager (PM) ante la llegada de equipos de agentes autónomos. Ariel Contreras argumenta que el PM tradicional que solo gestiona tickets está destinado a desaparecer. En el futuro cercano (2026), un solo PM asistido por agentes podrá realizar el trabajo que antes requería un equipo de 5 personas. La clave no es la programación, sino la **gestión de contexto y principios**.

---

## 2. METODOLOGÍAS NOMBRADAS

- **Agentic Workflows:** Coordinación de múltiples agentes para tareas de extremo a extremo.
- **Continuous Discovery:** Uso de IA para sintetizar feedback de usuarios constantemente.
- **POC (Proof of Concept) Accelerators:** Reducción drástica del tiempo para validar ideas técnicas.
- **Context Engineering:** La habilidad más crítica; alimentar a los agentes con la información exacta para obtener resultados precisos (98% de precisión mencionado).

---

## 3. METODOLOGÍAS IMPLEMENTADAS / RECOMENDADAS

- **File Stack Management:** Cada agente debe tener un conjunto de archivos (Identidad, Rol, Principios, Instrucciones) que evolucionan con el tiempo.
- **Principle-Based Management:** En lugar de dar instrucciones paso a paso, se definen principios de "qué es un buen resultado".
- **Compounding Corrections:** Tratar los errores de los agentes como datos valiosos para mejorar los prompts de forma permanente.

---

## 4. DEMOS REALIZADOS (En contexto)

- **Automatización de Documentación:** Generación del 98% de PRDs y specs técnicos usando Claude Code/OpenCode.
- **Gestión de 8 Agentes:** Referencia al sistema de Shubham Saboo donde 8 agentes cubren investigación, diseño, código, QA y marketing.

---

## 5. LISTA DE PROMPTS (ES / EN)

### Escenario A: Definición de Principios para un Agente
- **ES:** "Tu objetivo es filtrar noticias de IA. Principio: Solo muestra herramientas que un desarrollador pueda usar hoy. Ignora noticias corporativas de inversión."
- **EN:** "Your goal is to filter AI news. Principle: Only surface tools developers can use today. Ignore corporate investment news."

### Escenario B: Corrección Permanente
- **ES:** "Este resultado es demasiado genérico. De ahora en adelante, para cada recomendación, incluye un ejemplo de código real y un enlace a la documentación oficial."
- **EN:** "This output is too generic. From now on, for every recommendation, include a real code example and a link to the official documentation."

### Escenario C: Alineación de Contexto
- **ES:** "Lee nuestro archivo AGENTS.md y asegúrate de que cualquier propuesta de arquitectura siga el patrón de Micro-frontends definido."
- **EN:** "Read our AGENTS.md file and ensure any architecture proposal follows the defined Micro-frontends pattern."

---

## 6. VERIFICACIÓN VS PERSONALOS

| Componente | Estado en OS | Mejora Sugerida |
|------------|--------------|-----------------|
| **Context Injection** | ✅ Implementado | Automatizar la actualización de "Principios" basada en fallos detectados en sesiones. |
| **Agent Roles** | ✅ Implementado | Crear una jerarquía de agentes donde uno actúe como "Chief of Staff" para monitorear a los demás. |
| **Document Automation** | ✅ Implementado | Integrar la Skill `Video_Intel` para que la documentación de nuevos aprendizajes sea 100% autónoma. |

---

## 7. PLAN DE IMPLEMENTACIÓN PARA EL OS

1. **Crear Skill `Agent_Governor`:** Para gestionar la "evolución permanente" de los principios de cada agente basándose en feedback.
2. **Implementar `Context_Refresher`:** Un hook que, al detectar un error corregido, lo guarde en el archivo de principios del agente correspondiente.
3. **Refactorizar `Video_Intel`:** Para que use `supadata` por defecto, garantizando transcripciones rápidas sin depender de hardware local.

---

## 8. REGISTRO DE VIDEO (Registry Entry)

- **URL:** https://www.youtube.com/live/3psHUg6KzOo
- **Temas:** IA en Product Management, Equipos de Agentes, Optimización de Roles, Gestión de Contexto.
- **Recomendación:** Migrar el foco de "escribir código" a "escribir principios".

---
*Think Different PersonalOS - Unicorn Engineering SOTA 2026*