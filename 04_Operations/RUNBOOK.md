# 🚨 RUNBOOK — Protocolos de Emergencia y Resiliencia

> **Máquina de Evolución Autónoma v6.1**
> Estado: BASE IMPLEMENTADA
> Fecha: 2026-03-29

---

## 📋 Propósito

Este documento establece los protocolos de emergencia, contingencia y resiliencia para el sistema de automejora recursiva. Define cómo el sistema debe actuar ante fallos, inconsistencias o situaciones de riesgo.

---

## 🎯 Principios Fundamentales

### Regla de Oro

> **Ningún proceso de automejora puede comprometer la integridad del sistema host.**

### Jerarquía de Seguridad

| Prioridad   | Descripción                     | Acción                           |
|-------------|---------------------------------|----------------------------------|
| 1️⃣         | **Protección de datos**         | Backup antes de cualquier cambio |
| 2️⃣         | **Protección de configuración** | Archivos críticos inmutables     |
| 3️⃣         | **Protección de memoria**       | Consistencia de Engram           |
| 4️⃣         | **Mejora continua**             | Solo si 1-3 están seguras        |

---

## 🚨 Protocolos de Emergencia

### Protocolo 1: DETECCIÓN DE FALLO

```yaml
FALLO_DETECTADO:
  criterios:
    - Health Score < 50
    - Error en ciclo de automejora
    - Inconsistencia en memoria
    - Archivo crítico corrupto
  
  respuesta:
    nivel_1:
      action: "Detener ciclo de automejora"
      notify: "Usuario (si nivel > P1)"
    
    nivel_2:
      action: "Generar reporte de incidentes"
      notify: "Usuario inmediatamente"
    
    nivel_3:
      action: "Activar modo recuperación"
      notify: "Usuario + historial para análisis"
```

### Protocolo 2: FALLO EN CICLO DE AUTOMEJORA

```
┌─────────────────────────────────────────────────────────────┐
│                   CICLO DE EMERGENCIA                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   ERROR DETECTADO                                           │
│        │                                                    │
│        ▼                                                    │
│   ┌─────────────┐    SÍ     ┌──────────────────┐         │
│   │ ¿Es seguro? │ ────────▶ │ Aplicar fix      │         │
│   └─────────────┘           │ automático       │         │
│        │ NO                  └──────────────────┘         │
│        ▼                                                 │
│   ┌─────────────────────┐                               │
│   │ Registrar incidente │                               │
│   │ Generar reporte      │                               │
│   │ Notificar usuario    │                               │
│   └─────────────────────┘                               │
│        │                                                    │
│        ▼                                                    │
│   ┌─────────────────────┐                               │
│   │ Esperar intervención │                               │
│   │ humana              │                               │
│   └─────────────────────┘                               │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Protocolo 3: INCONSISTENCIA DE MEMORIA

**Síntomas:**
- Engram retorna información contradictoria
- Sesión previa no se recupera
- CTX tiene datos corruptos

**Acciones:**
```python
MEMORY_EMERGENCY = {
    "step_1": "Exportar estado actual de memoria",
    "step_2": "Validar integridad de CTX files",
    "step_3": "Si corrupt: restaurar desde backup",
    "step_4": "Si recuperable: sincronizar con Engram",
    "step_5": "Documentar incidente en EVOLUTION_LOG.md"
}
```

### ProtocolO 4: ARCHIVO CRÍTICO AFECTADO

**Archivos Protegidos (NUNCA modificar automáticamente):**
- `AGENTS.md` y derivados
- `00_Winter_is_Coming/AGENTS.md`
- Archivos de configuración de habilidades críticas

```yaml
PROTECTED_FILES:
  - "AGENTS.md"
  - "00_Winter_is_Coming/AGENTS.md"
  - "config.yaml" (raíz)
  - "*.json" de autenticación
  
  response:
    if_system_attempts_modify:
      - BLOQUEAR modificación
      - Registrar intento en EVOLUTION_LOG
      - Notificar usuario inmediatamente
```

---

## 🔒 Modos de Operación

### Modo: 🟢 NORMAL

```yaml
normal_mode:
  description: "Operación estándar"
  autonomy_level: 2  # Sugiere y ejecuta si.safe()
  checks:
    - daily_scan: enabled
    - auto_fix_safe: enabled
    - auto_fix_risky: disabled
    - evolution: suggestion_only
  
  limits:
    max_auto_fixes_per_day: 10
    max_files_modified: 5
    require_confirmation: ["architecture", "workflow"]
```

### Modo: 🟡 ADVERTENCIA

```yaml
warning_mode:
  trigger:
    - "Health Score < 70"
    - "2+ ciclos fallidos consecutivos"
    - "Usuario solicita supervisión"
  
  autonomy_level: 1  # Solo sugiere
  actions:
    - "Detener auto-fixes automáticos"
    - "Generar reporte para usuario"
    - "Sugerir intervención manual"
  
  limits:
    max_auto_fixes_per_day: 0
    require_confirmation: ALL
```

### Modo: 🔴 EMERGENCIA

```yaml
emergency_mode:
  trigger:
    - "Health Score < 30"
    - "Fallo crítico en ciclo"
    - "Archivo protegido en riesgo"
  
  autonomy_level: 0  # Manual only
  actions:
    - "Detener TODA automejora"
    - "Crear backup inmediato"
    - "Notificar usuario"
    - "Esperar intervención humana"
  
  exit_criteria:
    - "Usuario verifica sistema estable"
    - "Health Score > 70"
    - "Validación manual completada"
```

---

## 🛡️ Resiliencia del Sistema

### Checkpoints de Seguridad

```yaml
SECURITY_CHECKPOINTS:
  before_any_fix:
    - ✅ Verificar archivo no está en lista protegida
    ✅ Confirmar backup existe
    ✅ Validar que cambio es reversible
    ✅ Verificar que no rompe dependencias
  
  during_fix:
    - ✅ Monitorear uso de recursos
    - ✅ Registrar cada paso
    - ✅ Poder hacer rollback inmediato
  
  after_fix:
    - ✅ Validar integridad del sistema
    - ✅ Verificar health score mejoró
    - ✅ Documentar en EVOLUTION_LOG
```

### Sistema de Rollback

```python
ROLLBACK_PROCEDURE = """
1. IDENTIFICAR: ¿Qué cambio causó el problema?
2. EVALUAR: ¿Es seguro revertir?
3. RESPALDO: ¿Tenemos snapshot antes del cambio?
4. REVERTIR: Aplicar cambio inverso
5. VALIDAR: Health score > pre-cambio
6. DOCUMENTAR: Incidente en EVOLUTION_LOG
"""
```

---

## 📊 Métricas de Resiliencia

| Métrica              | Target   | Alerta si   |
|----------------------|----------|-------------|
| Uptime del sistema   | > 99%    | < 95%       |
| Éxito de auto-fixes  | > 80%    | < 60%       |
| Rollbacks necesarios | < 5%     | > 15%       |
| Recovery Time        | < 5 min  | > 15 min    |
| False Positives      | < 10%    | > 20%       |

---

## 📞 Notificaciones

### Matriz de Notificaciones

| Evento                     | Nivel   | Destinatario   | Canal           |
|----------------------------|---------|----------------|-----------------|
| Auto-fix exitoso           | INFO    | Sistema        | Log             |
| Sugerencia de mejora       | BAJO    | Usuario        | Dashboard       |
| Fix requiere confirmación  | MEDIO   | Usuario        | Prompt          |
| Modo advertencia activo    | ALTO    | Usuario        | Alert           |
| Modo emergencia activo     | CRÍTICO | Usuario + Log  | Alert + File    |
| Archivo protegido afectado | CRÍTICO | Usuario        | Alert + Bloqueo |

---

## 🔄 Procedimientos de Recuperación

### Recuperación Post-Fallo

```yaml
POST_FAILURE_RECOVERY:
  step_1: "Evaluar estado actual"
    - Health Score
    - Archivos afectados
    - Logs disponibles
  
  step_2: "Determinar causa raíz"
    - Analizar EVOLUTION_LOG
    - Revisar último ciclo
    - Identificar punto de fallo
  
  step_3: "Aplicar corrección"
    - Si seguro: auto-fix
    - Si riesgoso: sugerencia manual
  
  step_4: "Validar recuperación"
    - Health Score debe mejorar
    - Ningún archivo protegido afectado
    - Memoria consistente
  
  step_5: "Documentar"
    - Actualizar EVOLUTION_LOG
    - Crear regla si es repetible
```

---

## 📝 Registro de Incidentes

Cada incidente debe registrar:

```yaml
INCIDENT_REPORT:
  timestamp: "ISO 8601"
  severity: "P0|P1|P2|P3"
  type: "auto_fix_fail|memory_corrupt|protected_file|unknown"
  affected_files: []
  recovery_time: "minutos"
  root_cause: "descripción"
  resolution: "cómo se resolvió"
  prevention: "regla futura si aplica"
```

---

> **"Un sistema que no puede recuperarse de sus propios errores, no merece evolucionar."**
>
> — PersonalOS v6.1 Philosophy

---

*Documento vivo - Última actualización: 2026-03-29*
