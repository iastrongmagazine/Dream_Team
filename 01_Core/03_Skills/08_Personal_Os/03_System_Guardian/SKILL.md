---
name: System Guardian - Recordatorio Crítico
description: SKILL DE PROTECCIÓN - Se activa en cada tarea para recordarte las instrucciones críticas obligatorias
version: 1.0.1
trigger_keywords: ["--", "recordar", "instrucciones", "recordatorio", "sistema", "protocolo", "tarea", "empezar", "comenzar", "haz", "hace", "realiza", "ejecuta", "ayuda", "que debes hacer"]
auto_loads_skills: true
alwaysApply: true
priority: 100
---

# 🛡️ System Guardian - Instrucciones Críticas

## 🎯 Propósito
Esta skill se CARGA MANUALMENTE cuando el usuario inicia una tarea. Su función es recordarle al agente las instrucciones CRÍTICAS que debe seguir DURANTE toda la tarea.

## ⚠️ INSTRUCCIONES OBLIGATORIAS (DEBE RECORDAR EN CADA TAREA)

### 1. **IDIOMA**
- ✅ **SIEMPRE** Español en chat (es mi idioma natal)
- ✅ Usar español rioplatense: laburo, ponete las piedras, boludo, quilombo, bancá, dale, etc.

### 2. **SONIDO AL FINALIZAR** (OBLIGATORIO)
- ✅ Al terminar **CUALQUIER** tarea importante, ejecutar:
  ```bash
  powershell -ExecutionPolicy Bypass -File ".agent/04_Extensions/hooks/04_Sound/task-complete-sound.ps1"
  ```
- ✅ O usar `speak("tarea completada")` para voz

### 3. **PROTOCOLO CONTEXTO** (AL INICIAR)
- [ ] Leer `00_Winter_is_Coming/AGENTS.md`
- [ ] Leer `01_Core/01_Rules/01_Context_Protocol.mdc`
- [ ] Ejecutar `mem_context(limit=10)`
- [ ] **Reportar contexto** antes de actuar

### 4. **SUPER CAMPEONES** (Si aplica)
- Si el usuario dice "Super campeones" → Activar metodología:
  - 1 Director + 8 Agentes (4 Jugadores + 4 Auditores)
  - Plan → Work → Review → Compound → Audit

### 5. **REGLAS IMPERATIVAS**
- ✅ **REGLA 1:** NO actuar sin plan aprobado
- ✅ **REGLA 2:** Enumeración correcta (XX_Nombre)
- ✅ **REGLA 3:** Si detectás numeración incorrecta → DETENERSE y esperar aprobación

## 🔄 Cuándo Activarse

### Activación MANUAL (recomendada)
Al inicio de cada tarea, el usuario o el agente DEBE cargar esta skill para recordar las instrucciones.

### Activación por Keywords
- "recordar instrucciones", "qué debo hacer", "protocolo", "empezar tarea"

## 📋 Checklist de each Tarea

```markdown
## ✅ Pre-Tarea
- [ ] Leer contexto de memoria (mem_context)
- [ ] Cargar System Guardian (esta skill)
- [ ] Reportar contexto al usuario

## 🏃 Durante la Tarea
- [ ] Mantener español en chat
- [ ] Solicitar aprobación antes de actuar (REGLA 1)

## 🎯 Post-Tarea
- [ ] **BEEP** - Ejecutar sonido de completado
- [ ] Guardar en Engram si hay decisiones/discoveries
- [ ] Session summary si es fin de sesión
```

## 🔗 Dependencias

### Skills a cargar después
- `01_Core/03_Skills/00_Compound_Engineering/` - Si requiere compound engineering
- Skills específicas de la tarea

### Archivos de referencia
- `CLAUDE.md` - Configuración principal
- `00_Winter_is_Coming/AGENTS.md` - Fuente de verdad

## 🧠 Cómo Usar Esta Skill

### Paso 1: Al iniciar tarea
```
Cargar skill: System Guardian
```

### Paso 2: Verificar contexto
```
- mem_context(limit=10)
- Leer AGENTS.md si es nueva sesión
```

### Paso 3: Ejecutar tarea
```
- Mantener español
- Solicitar aprobación para cada paso
- Usar speak() para confirmaciones importantes
```

### Paso 4: Finalizar tarea
```
powershell -ExecutionPolicy Bypass -File ".agent/04_Extensions/hooks/04_Sound/task-complete-sound.ps1"
```

## ✅ Verification

Para verificar que seguiste las instrucciones:
- [ ] ¿Hablé en español?
- [ ] ¿Ejecuté beep al terminar?
- [ ] ¿Pedí aprobación antes de actuar?
- [ ] ¿Guardé en Engram si correspondía?

## 📊 Changelog

| Versión | Fecha | Cambio |
|---------|-------|--------|
| 1.0.0 | 2026-03-28 | Creación inicial |
