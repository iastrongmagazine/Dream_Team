---
name: zinking-transform
description: QUÉ HACE: Transforma textos técnicos en comunicación humana, empática y estratégica ("Zinking"). CUÁNDO SE EJECUTA: Al redactar correos, anuncios o documentación orientada a personas.

## 📋 Skill Protocol (Armor Layer)

### 🧩 Contexto Requerido
- Texto fuente o borrador técnico.
- Perfil del receptor (User Persona).
- Objetivo de la comunicación (Inspirar, Informar, Corregir).

### 📦 Output Esperado
- Versión "Zinked" del texto (más humana y directa).
- Estructura de "Storytelling" aplicada.
- Reducción de fricción cognitiva.

### 🚫 Limitaciones
- **No altera datos técnicos, fechas o valores críticos.**
- No es una skill de traducción pura; es de transformación de tono.
---

# Zinking Transformational Communication

Zinking no es un estilo: es una arquitectura de conexión. Este skill transforma textos fríos, técnicos o autoritarios en puentes de empatía y verdad, priorizando la conexión humana sobre la estructura perfecta.

## Principios Fundamentales

- **Vulnerabilidad Estratégica**: Compartir el proceso, no solo el éxito. ("Recuerdo cuando...", "Me frustró profundamente...").
- **Analogías Cotidianas**: Traducir lo complejo a lo universal con comparaciones del día a día.
- **Validación Empática**: Reconocer y normalizar la experiencia del otro.
- **Calidez (Presencia)**: Tono cercano, pausado y sensorial que invita al lector al momento presente.

## Cuándo usarlo

- Transformar contenido educativo, técnico o inspiracional.
- Humanizar correos, posts en redes sociales (LinkedIn/Twitter) o blogs.
- Antes de publicar documentación técnica que deba sentirse amigable.
- Cuando el usuario mencione el sistema "Zinking".

## Workflow

1.  **Analizar el texto original**: Identifica el mensaje central oculto tras lenguaje frío o autoritario.
2.  **Seleccionar Contexto**: ¿Es `educativo`, `inspiracional`, `tecnico`, o `general`?
3.  **Aplicar la Transformación**:
    - **Inicio**: Añade una mini-historia personal o detalle sensorial.
    - **Cuerpo**: Sustituye imperativos ("debes") por invitaciones ("te invito a"). Añade una analogía.
    - **Cierre**: Termina con una pregunta reflexiva o una tarea pequeña y amable.
4.  **Evaluar "Score Zinking"**:
    - ¿Se siente como hablar con un amigo sabio?
    - ¿Las frases respiran (ritmos variados)?
    - ¿Hay detalles sensoriales (aromas, sonidos, texturas)?

## Guía de Uso (Manual y Automática)

### Transformación Manual

- **Language**: Evita "siempre", "debes". Usa "a menudo", "podrías considerar".
- **Analogies**: "Estructurar el código es como organizar una cocina antes de cocinar".
- **Validation**: "Es normal sentirse abrumado al principio".

### Motor Zinking

Si el entorno lo permite, puedes usar el script de automatización:

```bash
python 07_Skill/zinking-transform/scripts/zinking_writer.py
```

## Resources

- [zinking_writer.py](scripts/zinking_writer.py): Python engine for Zinking transformation.
- [ZinkingWriter.tsx](resources/ZinkingWriter.tsx): Componente UI de referencia.
- [Zinking Principles](scripts/zinking_writer.py#L332-L343): Listado completo de principios técnicos.
