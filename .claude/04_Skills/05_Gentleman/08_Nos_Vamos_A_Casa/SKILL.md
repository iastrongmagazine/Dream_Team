---
name: nos-vamos-a-casa
description: QUÉ HACE: Orquesta un ritual de 8 pasos (auditoría, tests, voz, notas, commit) para un cierre perfecto. CUÁNDO SE EJECUTA: Al finalizar la sesión de trabajo diaria para asegurar continuidad.

## 📋 Skill Protocol (Armor Layer)

### 🧩 Contexto Requerido
- Sesión de trabajo finalizada.
- Repositorio Git inicializado.
- Scripts de validación y hooks operativos.

### 📦 Output Esperado
- Todos los tests de la suite en verde.
- Nota de sesión actualizada en `09_Process_Notes`.
- Commit final y push realizados.
- Notificación de voz confirmando el éxito del ritual.

### 🚫 Limitaciones
- **No se puede cerrar si hay tests fallidos.** El agente debe proponer fix o revertir cambios inestables.
- No deja procesos en segundo plano activos.
---

# nos-vamos-a-casa 🏠

Estrategia de cierre y validación sistemática de fin de sesión.

## 🎯 Objetivo

Asegurar que el sistema Invictus esté en un estado perfecto (auditado, validado y documentado) antes de finalizar el trabajo, automatizando los pasos repetitivos de verificación y guardado.

## 🛠️ Herramientas Utilizadas

- **Scripts de Validación**: `07_Skill/skill-testing-automation/scripts/run_tests.py`
- **Hooks de Notificación**: `09_System/hooks/03_notification.py` (con voz activa)
- **Orquestador**: `08_Workflow/ritual_cierre.py`

## 🔄 El Ritual de 8 Pasos

Cuando el usuario indica "Nos Vamos a Casa", el agente debe ejecutar:

1.  **Auditoría de Rutas**: Verificar que no existan enlaces rotos.
2.  **Test de Hooks**: Validar `pre_tool_use`, `post_tool_use` y `notification`.
3.  **Chequeo de Sistema**: Correr la suite de validación rápida.
4.  **Aviso de Voz**: Confirmar el éxito de los tests mediante TTS.
5.  **Nota de Sesión**: Crear o actualizar la nota en `01_Core/03_Process_Notes/Sessions/`.
6.  **ADR Check**: Verificar si hubo decisiones arquitectónicas que documentar.
7.  **Sincronización**: Verificar dependencias `uv`.
8.  **Commit Final**: Preparar el mensaje de commit y realizar el push.

## 💡 Mejores Prácticas

- **Nunca omitir la validación**: Si un test falla, el ritual se detiene y se debe corregir el error antes de salir.
- **Voz Descriptiva**: Usar la notificación de voz para resumir el estado global (ej: "Sistema validado. 25 de 25 tests exitosos.").
- **Limpieza de Raíz**: Asegurar que ningún archivo temporal o log quedó en la raíz fuera de `.claude/`.

---

> [!IMPORTANT]
> Este ritual es el guardián de la continuidad del proyecto. Ignorarlo aumenta la deuda técnica y el riesgo de pérdida de contexto en la siguiente sesión.
