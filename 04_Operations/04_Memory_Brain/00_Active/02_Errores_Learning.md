# ❌ ERRORES Y APRENDIZAJES - Think Different AI

> **Fecha**: 2026-03-25
> **Proyecto**: Think Different AI PersonalOS
> **Estado**: v5.0 - MATRIX RECARGADO

- --

## 🔄 ÚLTIMOS CAMBIOS (2026-03-21)

### Skills System v2.0 Completado

| Aspecto                                  | Antes                                        | Después                                    |
|------------------------------------------|----------------------------------------------|--------------------------------------------|
| Canonical Source                         | Confuso (múltiples ubicaciones)              | `.agent/02_Skills/`                        |
| Cursor Skills                            | Sincronizado manualmente                     | README only (espejo)                       |
| Context Memory                           | Duplicado (08_Context_Memory)                | Solo 01_Context_Memory/                    |
| Numeración                               | Rotas (huecos, duplicados)                   | PERFECTA (01-09 secuencial)                |
| Backup Central                           | No existía                                   | 05_Archive/06_Backup_Central/                |

### QMD MCP Integration (PENDIENTE)

- Estado: ⏳ Por otro agente
- Tracking: En 04_Inventario.md - Próximos Pasos

### DigitalGarden (PENDIENTE)

- Estado: ⏳ Por otro agente
- Tracking: En 04_Inventario.md - Próximos Pasos

- --

## 🚨 ERRORES CRÍTICOS

### Error 0: Sesión de Reorganización del 2026-03-21

* *Fecha**: 2026-03-21

* *What Happened**:
Reorganización completa del sistema ejecutada exitosamente:

1. **Skills Reorganization**
   - 99 skills organizadas en 9 perfiles (01-09) + 10_Backup
   - READMEs agregados a cada perfil
   - Canonical source: `.agent/02_Skills/`

2. **Context Memory Cleanup**
   - Removidas carpetas duplicadas (08_Context_Memory, Context_Memory)
   - Solo 01_Context_Memory/ como source of truth

3. **Backup Central Created**
   - Nueva carpeta: `05_Archive/06_Backup_Central/`
   - Estructura: 01_Config, 02_Mcp, 03_Agents, 04_Projects, 05_Repos

4. **Documentation Beautified**
   - 85 markdown documents beautificados
   - `35_Beautify_Tables.py` aplicado
   - `36_Beauty_Doc.py` actualizado

5. **Inventory Created**
   - `04_Inventario.md` creado con inventario completo

6. **01_Brain Sequence**
   - Completo: 01, 02, 03, 04, 05, 06, 07, 09
   - Gap 08: removido (era duplicado)

* *Resultado**: ✅ Sistema más limpio y organizado

- --

### Error 1: Reorganización de Skills Sin Plan

* *Fecha**: 2026-03-21 (sesión actual)

* *What Happened**:
Se intentó reorganizar skills con múltiples agentes simultáneos (4 agentes a la vez) sin tener un plan escrito aprobado.

* *Problema**:
- Los agentes movieron archivos sin verificar primero
- Numeración rota (03 duplicated, 04 duplicated, 05 duplicated)
- Estructura caótica con duplicados
- Contexto perdido por múltiples cambios simultáneos

* *Solución Aplicada**:
1. Inmediatamente revertido a commit `d0574d1`
2. Creado plan escrito detallado con mapeo completo
3. Ejecutado migración perfil por perfil controlado
4. Commit exitoso: `154ae06`

* *Learned**:
- ⚠️ **NUNCA mover skills/archivos sin crear PLAN escrito primero**
- ⚠️ **Modo Plan (solo lectura) antes de ejecución**
- ⚠️ **Aprobación explícita del usuario antes de ejecutar**
- ⚠️ **Si algo falla, revertir inmediatamente**
- ⚠️ **Ejecución controlada perfil por perfil**

- --

### Error 2: Contexto Perdido por Compacción

* *When**: Múltiples sesiones largas

* *What Happened**:
Contexto window se llena → compaction → state loss → decisiones olvidadas

* *Solución**:
```markdown
## AFTER COMPACTION

1. IMMEDIATELY call mem_session_summary
2. Then call mem_context
3. Only THEN continue working
```

* *Learned**:
- ⚠️ **SIEMPRE guardar en Engram después de decisiones importantes**
- ⚠️ **mem_session_summary al cerrar sesión es OBLIGATORIO**
- ⚠️ **No esperar a que pregunten, guardar proactively**

- --

### Error 3: Hooks en Conflicto

* *When**: hooks/pre_tool y post_tool interactuando

* *What Happened**:
Scripts con paths incorrectos o lógica conflictiva causaban errores en cascada.

* *Solución**:
- Validar paths con config_paths.py
- Orden correcto de ejecución
- Logs claros para debugging

* *Learned**:
- ⚠️ **Scripts necesitan paths relativos al workdir**
- ⚠️ **Validar antes de ejecutar hooks**
- ⚠️ **Orden de hooks importa**

- --

### Error 4: Duplicación Masiva de Skills

* *When**: Múltiples sesiones creando skills

* *What Happened**:
Mismas skills en hasta 4 ubicaciones:
- `02_High_Value/`
- `03_Utilities/`
- `05_Gentleman_System/`
- `07_Every/`

* *Skills Duplicadas Detectadas**:

| Skill                                 | Ubicaciones                 | Canonical                 |
|---------------------------------------|-----------------------------|---------------------------|
| Brainstorming                         | 3                           | `07_Every/`               |
| Writing_Plans                         | 3                           | `07_Every/`               |
| Executing_Plans                       | 3                           | `07_Every/`               |
| Test_Driven_Development               | 4                           | `07_Every/`               |
| Systematic_Debugging                  | 3                           | `07_Every/`               |
| Skill_Creator                         | 6                           | `07_Every/`               |
| Mqp_Client                            | 3                           | `07_Every/`               |

* *Solución**:
- Canonical version: `07_Every/`
- Duplicados movidos a `10_Backup/`
- Numeración PERFECTA sin huecos

- --

## 📚 ERRORES MENORES (Y SUS FIXES)

### Error 5: Numeración Inconsistente

* *Problema**: `04_Product_Manager/03_Branch_Pr` y `03_Executing_Plans` (mismo número)

* *Fix**: Reenumerate de 01-08 con secuencia PERFECTA

### Error 6: CRLF en Git

* *Problema**: Archivos con CRLF causando warnings en git

* *Fix**:
```bash
git config core.autocrlf false
git add --renormalize .
```

### Error 8: Rutas Absolutas en Logs (Fragilidad del Sistema)

* *What Happened*:
La persistencia de rutas absolutas en los logs del sistema causaba falsos positivos durante la validación de integridad y fragilidad ante cambios de entorno.

* *Solución*:
Se establece el uso obligatorio de rutas relativas al `PROJECT_ROOT` en todos los scripts de logs y validación del motor (04_Operations/).

* *Learned*:
- ⚠️ **Las rutas absolutas son enemigas de la portabilidad**
- ⚠️ **Uso OBLIGATORIO de rutas relativas al `PROJECT_ROOT`**
- ⚠️ **Normalización de rutas después de cada sesión**

- --

## 🎓 LECCIONES APRENDIDAS

### Lección 1: Plan Mode es Sagrado

> "En Plan Mode solo lectura, no ejecutar sin aprobación"

El intento de mover skills sin plan escrito casi destruye el sistema. Ahora:
- ✅ Siempre escribir plan primero
- ✅ Mostrar mapeo al usuario
- ✅ Esperar "GO" antes de ejecutar
- ✅ Ejecutar perfil por perfil con verificación

### Lección 2: Engram es tu Amigo

> "SIEMPRE guardar en Engram después de decisiones"

El contexto se pierde. Las decisiones se olvidan. Engram sobrevive a sesiones y compaction.

* *Protocolo**:
1. Decisión importante → `mem_save`
2. Cierre de sesión → `mem_session_summary`
3. Compacción → `mem_session_summary` IMMEDIATAMENTE

### Lección 3: Orchestrator Mode Previene Caos

> "You are a COORDINATOR, not an EXECUTOR"

Ejecutar inline causa:
- Context bloat
- State loss
- Decisiones sin persistencia

* *Protocolo**:
1. ¿Necesito leer/escribir código? → DELEGATE
2. ¿Es "solo un pequeño cambio"? → STILL DELEGATE
3. ¿Puedo responder con short answer? → DO THAT

### Lección 4: Canonical Version Previene Duplicación

> "Usar versión canonical de 07_Every/, mover resto a backup"

Duplicar skills causa:
- Confusión sobre cuál usar
- Inconsistencias entre versiones
- Mantenimiento en múltiples lugares

* *Solución**:
- Un solo origen de verdad
- Backup como referencia histórica
- Canonical claramente identificado

- --

## 🛡️ PROTOCOLOS DE PREVENCIÓN

### Protocolo 1: Antes de Mover Archivos

```markdown
1. [ ] Leer estructura actual
2. [ ] Crear plan escrito detallado
3. [ ] Mapear ORIGEN → DESTINO
4. [ ] Verificar numeración PERFECTA
5. [ ] Mostrar plan al usuario
6. [ ] Esperar "GO"
7. [ ] Ejecutar perfil por perfil
8. [ ] Verificar después de cada batch
9. [ ] Commit atómico al final
```

### Protocolo 2: Antes de Cerrar Sesión

```markdown
1. [ ] Pure Green: todo commiteado
2. [ ] mem_session_summary llamado
3. [ ] No cambios unstaged
4. [ ] Hook de voz/notificación ejecutado
5. [ ] Resumen al usuario
```

### Protocolo 3: Después de Compaction

```markdown
1. [ ] mem_session_summary IMMEDIATAMENTE
2. [ ] mem_context para recuperar
3. [ ] Continuar trabajo
```

- --

## 📊 MÉTRICAS DE ERRORES

| Error                            | Severidad                 | Status                    | Prevention                          |
|----------------------------------|---------------------------|---------------------------|-------------------------------------|
| Migración sin plan               | 🔴 CRÍTICA                 | ✅ FIXED                   | Protocolo plan mode                 |
| Numeración rota                  | 🟠 ALTA                    | ✅ FIXED                   | Convenciones strictas               |
| Duplicación skills               | 🟠 ALTA                    | ✅ FIXED                   | Canonical version                   |
| Context perdido                  | 🟡 MEDIA                   | ✅ MITIGATED               | mem_save protocol                   |
| CRLF warnings                    | 🟢 BAJA                    | ✅ FIXED                   | git config                          |

- --

## 🔮 ACCIONES FUTURAS

- [ ] Hook de naming enforcement (validar convenciones)
- [ ] Script de validación de estructura
- [ ] Dashboard de skills con métricas
- [ ] Automated backup antes de cambios mayores

- --

## 🔥 ERRORES MATRIX RECARGADO (25 Mar)

### Error 9: OpenCode Skills No Invocan

* *When*: Intentar usar `/ce:plan` en OpenCode
* *What Happened*: Skills mostraban contenido en vez de ejecutar
* *Problema*: OpenCode v1.3.2 tenía bug - skills sin argumentos no invocaban
* *Solución*:
  - Actualizar a OpenCode v1.6.0+
  - O usar con argumentos: `/ce:plan "algo"`
  - Skills van en `~/.config/opencode/skills/gentleman/` (global)
* *Learned*:
  - ⚠️ **OpenCode busca skills en ~/.config/opencode/skills/, no .opencode/**
  - ⚠️ **Skills deben copiarse a ubicación GLOBAL para funcionar**

### Error 10: Archivos Mal Ubicados en Active

* *When*: Organizar 07_Memory_Brain
* *What Happened*: `13_Anthropic_Skills_Implementation_Plan.md` quedó en 00_Active/
* *Problema*: Es plan de auditoría (24 Mar pre-Matrix Recargado), no referencia activa
* *Solución*: Mover a 03_Archive_Memory/2026-03-24/
* *Learned*:
  - ⚠️ **Plans van a Archive, no Active**
  - ⚠️ **Active = referencia diaria, Archive = histórico**

### Lección 6: Matrix Recargado = Ecosistema Completo

> "Gentleman = MANOS, CE = CEREBRO"

**Ecosistema actual:**
- **Gentleman** (~139 skills): Frameworks, Testing, DevOps, Marketing
- **CE** (131 componentes): 23+ agents review, 41 skills workflow, investigación

**Workflow Ideal:**
```
1. /ce:ideate → Descubrir oportunidades
2. /ce:brainstorm → Explorar enfoques
3. Gentleman → Escribir código
4. /ce:review → Validar con 23+ agents
5. /ce:work → Ejecutar plan
6. /ce:compound → Documentar learnings
```

- --

* Documento creado: 2026-03-21*
* Actualizado: 2026-03-25 - Matrix Recargado*
