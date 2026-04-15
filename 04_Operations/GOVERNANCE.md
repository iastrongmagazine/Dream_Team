# 🏛️ GOVERNANCE — Reglas de Acceso y Niveles de Autonomía

> **Máquina de Evolución Autónoma v6.1**
> Estado: BASE IMPLEMENTADA
> Fecha: 2026-03-29

---

## 📋 Propósito

Este documento establece las reglas de gobernanza, control de acceso y niveles de autonomía para el sistema de automejora recursiva. Define QUIÉN puede hacer QUÉ y en qué CIRCUNSTANCIAS.

---

## 🎯 Modelo de Gobernanza

```
┌─────────────────────────────────────────────────────────────────────┐
│                      JERARQUÍA DE CONTROL                           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                    🧑‍💻 USUARIO (OWNER)                       │  │
│   │         Decisiones estratégicas, approve de cambios         │  │
│   │                    críticos, veto absolute                   │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                              │                                       │
│                              ▼                                       │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                 🤖 SISTEMA (AUTO-LEARN)                      │  │
│   │     Detección → Diagnóstico → Sugerencia → (maybe) Fix     │  │
│   │                    Nivel de autonomía actual: MANUAL        │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                              │                                       │
│                              ▼                                       │
│   ┌─────────────────────────────────────────────────────────────┐  │
│   │                  ⚙️ SKILLS/AGENTS                           │  │
│   │              Ejecución de tareas específicas                 │  │
│   └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 🔐 Niveles de Autonomía

### Matriz de Autonomía

| Nivel   | Nombre     | Descripción          | Capacidad de Fix    | Requiere Confirmación    |
|---------|------------|----------------------|---------------------|--------------------------|
| **0**   | MANUAL     | Solo sugerencias     | NINGUNA             | SIEMPRE                  |
| **1**   | SUGGESTOR  | Sugiere y espera     | NINGUNA             | SIEMPRE                  |
| **2**   | ASSISTED   | Ejecuta si es seguro | AUTO-FIX SÍ         | Si es riesgoso           |
| **3**   | AUTONOMOUS | Ejecuta con监督        | AUTO-FIX SÍ         | Solo críticos            |
| **4**   | FULL       | Ejecución completa   | TODO                | NUNCA*                   |

> *Con limitaciones de seguridad activas

### Estado Actual: 🟡 NIVEL 0 - MANUAL

```yaml
CURRENT_STATE:
  autonomy_level: 0
  reason: "Fase inicial - validación de comportamiento"
  review_date: "2026-04-01"
  
  allowed_actions:
    - "Detectar problemas"
    - "Diagnosticar causas"
    - "Sugerir soluciones"
    - "Generar reportes"
  
  prohibited_actions:
    - "Modificar archivos"
    - "Ejecutar fixes"
    - "Cambiar configuraciones"
    - "Crear nuevos archivos"
    - "Eliminar archivos"
```

---

## 👤 Roles y Permisos

### Rol: PROPIETARIO (Usuario)

```yaml
OWNER:
  description: "Usuario humano - autoridad máxima"
  
  permissions:
    - Cambiar nivel de autonomía
    - Aprobar/rechazar sugerencias
    - Ejecutar overrides manuales
    - Modificar reglas de gobernanza
    - Acceder a archivos protegidos
    - Vetar cualquier decisión del sistema
  
  responsibilities:
    - Revisar sugerencias semanalmente
    - Aprobar cambios de arquitectura
    - Monitorear health score
    - Intervenir en emergencias
```

### Rol: SISTEMA (Auto-Learn)

```yaml
SYSTEM:
  description: "Motor de automejora recursiva"
  
  permissions:
    - Leer todos los archivos (excepto protegidos)
    - Generar sugerencias
    - Crear reportes
    - Registrar en EVOLUTION_LOG
    - Escanear estructura
    - Analizar calidad
  
  restrictions:
    - NO modificar sin aprobación
    - NO ejecutar en emergencia
    - NO tocar archivos protegidos
    - NO exceder límites de recursos
```

### Rol: GUARDIAN (GGA Pre-Commit)

```yaml
GUARDIAN:
  description: "Guardian Angel - protección de integridad"
  
  permissions:
    - Bloquear commits que violan reglas
    - Validar cambios pre-commit
    - Alertar sobre anomalías
    - Forzar modo emergencia
  
  enforcement_points:
    - Pre-commit hooks
    - Validación de archivos críticos
    - Verificación de sintaxis
```

---

## 📂 Control de Archivos

### Clasificación de Archivos

| Categoría            | Archivos                                     | Auto-Modificable    | Notas                        |
|----------------------|----------------------------------------------|---------------------|------------------------------|
| 🔴 **PROTEGIDOS**     | `AGENTS.md`, `00_Winter_is_Coming/AGENTS.md` | **NUNCA**           | Requiere intervención manual |
| 🟠 **RESTRINGIDOS**   | Configuraciones críticas, claves             | Solo con aprobación | Backup obligatorio           |
| 🟡 **OPERACIONALES**  | Skills, scripts, docs                        | Nivel 2+ con backup | Reversibles                  |
| 🟢 **EVOLUCIONABLES** | Logs, métricas, sugerencias                  | Nivel 3+            | Alta autonomía               |

### Archivos Protegidos (Lista Explícita)

```
PROTECTED_FILES = [
    "AGENTS.md",
    "00_Winter_is_Coming/AGENTS.md",
    ".gemini/GEMINI.md",
    "config.yaml (root)",
    "**/credentials*.json",
    "**/secrets*.yaml",
    "**/.env*",
    "**/MCP*config*.json",
]
```

### Regla de Protección

```python
def can_modify(file_path, autonomy_level):
    """Determina si un archivo puede ser modificado"""
    
    if is_protected(file_path):
        return False, "Archivo protegido - intervención manual requerida"
    
    if autonomy_level == 0:
        return False, "Nivel manual - solo sugerencias"
    
    if autonomy_level == 1:
        return False, "Nivel suggestor - requiere aprobación"
    
    if autonomy_level >= 2:
        if is_risky_operation(file_path):
            return False, "Operación riesgosa - requiere confirmación"
        return True, "Modificación permitida"
```

---

## ⚖️ Reglas de Decisión

### Algoritmo de Evaluación

```
┌─────────────────────────────────────────────────────────────┐
│              MOTOR DE DECISIÓN DE AUTONOMÍA                 │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│   1. RECEPCIÓN DE SUGERENCIA                                │
│              │                                               │
│              ▼                                               │
│   2. CLASIFICAR TIPO DE CAMBIO                              │
│      ├── Estructural (archivos/carpetas)                   │
│      ├── Configuracional (settings)                        │
│      ├── Documental (docs/metadatos)                        │
│      └── Funcional (código/skills)                          │
│              │                                               │
│              ▼                                               │
│   3. EVALUAR NIVEL DE RIESGO                                │
│      ├── 🟢 BAJO: reversible, sin dependencias             │
│      ├── 🟡 MEDIO: requiere backup                         │
│      ├── 🟠 ALTO: puede afectar estabilidad                │
│      └── 🔴 CRÍTICO: archivos protegidos o core             │
│              │                                               │
│              ▼                                               │
│   4. DETERMINAR ACCIÓN SEGÚN AUTONOMÍA ACTUAL               │
│                                                             │
│      Nivel 0 (MANUAL):                                       │
│        → Solo sugerir, nunca ejecutar                       │
│                                                             │
│      Nivel 1 (SUGGESTOR):                                    │
│        → Sugerir + esperar aprobación                       │
│                                                             │
│      Nivel 2 (ASSISTED):                                     │
│        → Auto-ejecutar si BAJO riesgo                       │
│        → Confirmar si MEDIO-ALTO                             │
│                                                             │
│      Nivel 3 (AUTONOMOUS):                                   │
│        → Auto-ejecutar si < ALTO riesgo                     │
│        → Confirmar solo CRÍTICO                              │
│                                                             │
│      Nivel 4 (FULL):                                         │
│        → Ejecutar todo con logging                           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

### Condiciones para Subir Nivel de Autonomía

```yaml
AUTONOMY_PROMOTION_REQUIREMENTS:
  level_0_to_1:
    - "30+ días sin incidentes críticos"
    - "Health Score promedio > 80"
    - "Usuario aprueba"
  
  level_1_to_2:
    - "60+ días en nivel 1 sin incidentes"
    - "Health Score promedio > 85"
    - "10+ sugerencias implementadas exitosamente"
    - "Usuario aprueba"
  
  level_2_to_3:
    - "90+ días en nivel 2"
    - "Health Score promedio > 90"
    - "< 5% de rollbacks necesarios"
    - "Validación de seguridad pasan"
```

---

## 📊 Límites y Controles

### Límites por Nivel

```yaml
LIMITS:
  level_0:
    max_suggestions_per_day: 999   # Ilimitado
    max_auto_fixes: 0
    max_files_modified: 0
  
  level_1:
    max_suggestions_per_day: 50
    max_auto_fixes: 0
    max_files_modified: 0
  
  level_2:
    max_suggestions_per_day: 100
    max_auto_fixes: 10
    max_files_modified: 5
    max_backup_size_mb: 100
  
  level_3:
    max_suggestions_per_day: 999
    max_auto_fixes: 50
    max_files_modified: 20
    max_execution_time_minutes: 30
```

### Controles de Seguridad

```yaml
SECURITY_CONTROLS:
  always_active:
    - "Verificación de archivos protegidos"
    - "Logging de todas las operaciones"
    - "Límites de tasa (rate limiting)"
    - "Backup antes de modificación"
  
  level_dependent:
    - "Confirmación de usuario": nivel < 3
    - "Validación de sintaxis": nivel < 2
    - "Health check post-op": nivel < 2
    - "Rollback automático": nivel >= 3
```

---

## 🔄 Cambios de Gobernanza

### Cómo Modificar Este Documento

```yaml
GOVERNANCE_CHANGE_PROCESS:
  step_1: "Proponer cambio (usuario o sistema)"
  step_2: "Evaluar impacto"
  step_3: "Simular efectos secundarios"
  step_4: "Revisión por usuario (si nivel < 3)"
  step_5: "Implementar cambio"
  step_6: "Documentar en EVOLUTION_LOG"
  step_7: "Monitorear efectos (7 días)"
```

---

## 📈 Métricas de Gobernanza

| Métrica                 | Target      | Medición   |
|-------------------------|-------------|------------|
| Sugerencias aceptadas   | > 70%       | Sistema    |
| Falsos positivos        | < 10%       | Usuario    |
| Intervenciones manuales | Decreciente | Sistema    |
| Time-to-approve         | < 24h       | Usuario    |
| Incidentes de seguridad | 0           | GGA        |

---

## 📝 Auditoría

### Registro de Decisiones

Cada decisión importante debe registrar:

```yaml
DECISION_LOG:
  timestamp: "ISO 8601"
  decision_type: "autonomy_change|permission_change|rule_change"
  from_state: ""
  to_state: ""
  trigger: "user_request|auto_evaluation|incident"
  approver: "usuario|auto"
  rationale: "razón de la decisión"
  side_effects: []
```

---

> **"La autonomía sin gobernanza es caos. La gobernanza sin autonomía es estancamiento."**
>
> — PersonalOS v6.1 Philosophy

---

*Documento vivo - Última actualización: 2026-03-29*
