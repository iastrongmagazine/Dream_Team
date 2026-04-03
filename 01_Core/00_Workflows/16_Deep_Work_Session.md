---
name: deep-work
description: Sesión de trabajo profundo — ejecutar una tarea P0/P1 con foco total, sin interrupciones y con checkpoints de energía.
argument-hint: "[tarea P0/P1 a ejecutar]"
---

# 🎯 Workflow: Deep Work Session

Para el trabajo que realmente importa. Sin notificaciones, sin multitarea, sin fricción.
Basado en el principio de Cal Newport: el trabajo profundo produce resultados extraordinarios en tiempo ordinario.

## Cuándo usar

- Tienes una tarea P0 o P1 que requiere concentración sostenida
- Necesitas aprender algo complejo (Python, inglés, nuevo concepto)
- Estás diseñando algo que requiere iteración profunda
- Quieres ejecutar un LFG Lite/Pro sin distracciones

## Duración recomendada

| Tipo de trabajo              | Duración ideal   |
|------------------------------|------------------|
| Escritura / Documentación    | 45-60 min        |
| Diseño UX/UI                 | 60-90 min        |
| Programación / Scripts       | 90-120 min       |
| Aprendizaje (Python/English) | 45-60 min        |
| Review + Revisión            | 30-45 min        |

## El protocolo (antes de empezar)

### 1. Definir la sesión (2 min)

Responder estas 3 preguntas antes de arrancar:

- **¿Cuál es el único output de esta sesión?** (específico, no vago)
- **¿Cómo sabré que terminé?** (criterio de done)
- **¿Qué necesito tener abierto?** (solo lo necesario)

Ejemplo:
```
Output: Tener el script 14_Deep_Work_Timer.py funcionando
Done: El script corre sin errores y guarda el log
Abrir: VS Code + Claude Code + 08_Scripts_Os/
```

### 2. Preparar el contexto (3 min)

```bash
python 08_Scripts_Os/04_Ritual_Hub.py --standup  # Ver prioridades del día
git status                                # Estado limpio antes de empezar
```

Leer la tarea en `03_Tasks/` — entender el scope completo.

### 3. Cerrar lo que distrae

- Silenciar notificaciones
- Cerrar tabs irrelevantes
- Poner música instrumental si ayuda

## Durante la sesión

### Bloques de trabajo

Trabajar en bloques de **25 min** (Pomodoro) o **45 min** (flow state):

```
[25/45 min] → Trabajo profundo
[5/10 min]  → Pausa activa (caminar, agua, sin pantalla)
[repetir]
```

### Regla de captura de distracciones

Si surge una idea o tarea nueva → **Captura Rápida** (workflow 14) sin interrumpir el flujo.
No proceses, solo escribe en `BACKLOG.md` y sigue.

### Checkpoint de energía (cada bloque)

Al finalizar cada bloque, evaluar en 1 segundo:
- 🟢 **Verde**: Flujo alto, seguir
- 🟡 **Amarillo**: Algo de fricción, ajustar approach
- 🔴 **Rojo**: Energía baja → pausa larga o cambiar de tarea

## Al terminar

### Cierre de sesión (5 min)

1. **Documentar**: ¿Qué logré? ¿Qué quedó pendiente? → `04_Operations/03_Process_Notes/` + **Engram**
2. **Commit**: Si hay código → commit atómico descriptivo
3. **Actualizar tarea**: Cambiar `status` en `03_Tasks/`
4. **Captura de aprendizajes**: ¿Qué aprendí hoy que vale la pena guardar?

```bash
python 08_Scripts_Os/04_Ritual_Hub.py   # Si es fin de día
```

## Para sesiones de aprendizaje (Python / English)

### Python Sprint (45 min)

```
[0-5 min]   Revisar qué quiero aprender/construir hoy
[5-35 min]  Escribir código, experimentar, romper cosas
[35-45 min] Documentar lo aprendido en 03_Knowledge/Notes/
```

### English Session (45 min)

```
[0-10 min]  Input: Leer o escuchar contenido en inglés (técnico o estratégico)
[10-30 min] Output: Escribir un párrafo, resumir lo leído, o documentar en inglés
[30-45 min] Revisión: Mejorar lo escrito con Claude como tutor
```

---

© 2026 PersonalOS | El foco no es un lujo — es la ventaja competitiva.
