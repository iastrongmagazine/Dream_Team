---
name: dieter-rams-design
description: QUÉ HACE: Audita y optimiza diseños basándose en los 10 principios de Dieter Rams (simplicidad y utilidad). CUÁNDO SE EJECUTA: Al finalizar prototipos de UI o evaluar flujos de usuario para asegurar que sean esenciales y honestos.

## 📋 Skill Protocol (Armor Layer)

### 🧩 Contexto Requerido
- Diseño propuesto o implementado (código o mockup).
- Entendimiento de la función principal del producto.
- Sin distracciones estéticas irrelevantes.

### 📦 Output Esperado
- Reporte detallado por principio (0-100).
- Identificación de "Red Flags" de diseño.
- 5 pasos accionables para simplificar el diseño ("Menos pero mejor").

### 🚫 Limitaciones
- **No es una skill de diseño artístico.**
- No recomienda añadir funcionalidades; casi siempre recomienda quitar o refinar.
- No es subjetivo; se basa en la lógica funcional.
---

# Dieter Rams Design Validator

Este skill te permite auditar cualquier diseño o concepto basándote en los 10 principios de Dieter Rams: innovador, útil, estético, comprensible, discreto, honesto, duradero, cuidadoso, respetuoso con el medio ambiente y, sobre todo, **menos pero mejor**.

## Cuándo usarlo

- Al finalizar un prototipo de UI.
- Al evaluar la simplicidad de un flujo de usuario.
- Cuando necesites una perspectiva crítica sobre la "honestidad" de un diseño.

## Instrucciones

### Paso 1: Recopilar descripción del diseño

Pide al usuario una descripción detallada del diseño o analiza el código/maqueta actual.

### Paso 2: Ejecutar validación

Puedes usar el script de Python para obtener un reporte estructurado.

```bash
# Ejemplo de ejecución
python 02_Core/skills/dieter_rams_design_skill.py input.json output.json
```

O simplemente realiza el análisis tú mismo (Claude) basándote en la lógica del script:

1. Evalúa cada principio de 0 a 100.
2. Identifica "Red Flags" (exceso de ornamentación, falta de utilidad, etc.).
3. Genera 5 recomendaciones accionables.

## Los 10 Principios

1. **Innovador**: Aprovecha nuevas posibilidades tecnológicas.
2. **Útil**: Enfatiza la utilidad sobre todo.
3. **Estético**: La belleza es integral para la utilidad.
4. **Comprensible**: Diseño intuitivo y auto-revelador.
5. **Discreto**: Neutral y contenido.
6. **Honesto**: No exagera ni manipula.
7. **Duradero**: Atemporal, no sigue modas.
8. **Cuidadoso**: Precisión en cada milímetro.
9. **Respetuoso**: Minimiza el impacto ambiental.
10. **Menos pero mejor**: Concentración en lo esencial.

## Ejemplo de Reporte

Si el score es bajo (<50), califícalo como "Anti-Rams" y sugiere una simplificación radical.
Si el score es alto (>85), felicita al usuario por un diseño "Rams-certified".
