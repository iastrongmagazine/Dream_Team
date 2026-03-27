# Anthropic Skills Framework (v4.1 Elite)

> Basado en Lessons from Building Claude Code (Thariq Shihipar) + Kevin绍兴 YouTube
> **Última actualización**: 2026-03-24 — Post-Audit completado

---

## 🎯 Core Principle: Steering Distribution

Skills no son solo atajos; son **funciones de fuerza** que sacan a Claude de la "zona promedio" (distribución predeterminada) y lo llevan hacia soluciones específicas, creativas y adaptadas a nuestro OS.

> "Don't State the Obvious" - Enfocarse en información que sale al modelo de su "default thinking"

---

## 📚 9 Tipos de Skills (Categorización Anthropic)

| #   | Tipo                                   | Descripción                        | Ejemplo PersonalOS                 |
|-----|----------------------------------------|------------------------------------|------------------------------------|
| 1   | **Library & API Reference**            | Cómo usar libs/CLIs correctamente  | `skill-creator`, `sdd-*`           |
| 2   | **Product Verification**               | Cómo testear/verificar código      | `playwright`, `e2e-testing`        |
| 3   | **Data Fetching & Analysis**           | Conectar a datos y monitoreo       | `analytics-tracking`               |
| 4   | **Business Process & Team Automation** | Workflows repetitivos en 1 comando | `weekly-review`, `morning-standup` |
| 5   | **Code Scaffolding & Templates**       | Generar boilerplate                | `prd`, `jira-epic`                 |
| 6   | **Code Quality & Review**              | Enforzar quality inside org        | `technical-review`, `pr-review`    |
| 7   | **CI/CD & Deployment**                 | Fetch, push, deploy código         | `github-pr`, `branch-pr`           |
| 8   | **Runbooks**                           | Síntoma → Investigación → Reporte  | `oncall-runner`, `debug-*`         |
| 9   | **Infrastructure Operations**          | Mantenimiento y operaciones        | `system-guardian`                  |

---

## 🏗️ Estructura de Skill Elite

### 1. Description Field Is For the Model (NO para humanos)
- No es "marketing" - es **cuándo activar esta skill**
- Keywords semánticos que el usuario *realmente dice*
- Ejemplo BUENO: `triggers on: weekly planning, review progress, reflect on goals`
- Ejemplo MALO: `A comprehensive tool for monitoring...`

### 2. Gotchas Section (El activo más valioso)
- Documentar errores pasados evita que Claude repita fallos
- Es como entrenar a un empleado junior
- Construir incrementalmente con cada ejecución

### 3. Progressive Disclosure
- No saturar `SKILL.md` (< 200 líneas ideal)
- Usar `references/` para docs pesadas
- Usar `scripts/` para código reutilizable
- Usar `assets/` para templates

### 4. Scripts & Code Generation
- Dar scripts pre-construidos = Claude compone en vez de reconstruir boilerplate
- Reducir tokens y errores de lógica

---

## 🛡️ Operación y Seguridad

### On-Demand Hooks
- Hooks que solo se activan cuando la skill se llama
- Útiles para operaciones sensibles (prod, DB, etc.)
- Ejemplo: `/careful` - bloquea `rm -rf`, `DROP TABLE` solo cuando necesitas

### State Persistence
- Usar `${CLAUDE_PLUGIN_DATA}` para datos estables
- O logs/ JSON para continuidad entre ejecuciones
- Ejemplo: `standup-post` guarda `standups.log` para comparar con anterior

### Goal-Oriented vs Rigid
- NO dar recetas rígidas
- Dar información + flexibilidad para adaptar
- "Prepare interview questions for this role" > "Write 5 behavioral questions"

---

## 📋 Checklist de Skill Elite

- [ ] Descripción con triggers semánticos (no marketing)
- [ ] Gotchas section con errores comunes
- [ ] Progressive disclosure (references/, scripts/, assets/)
- [ ] Scripts para automatización
- [ ] State persistence si es necesario
- [ ] On-demand hooks si es sensible
- [ ] Goal-oriented, no rigid recipes

---

## 🔄 Flywheel de Mejora Continua

1. **Ejecutar skill** → Claude comete error
2. **Documentar error** en Gotchas
3. **Re-ejecutar** → Mejor resultado
4. **Repetir** → Skill se vuelve más valiosa

> "Most of ours began as a few lines and a single gotcha, and got better because people kept adding to them as Claude hit new edge cases." - Thariq Shihipar

---

*Actualizado: 2026-03-24 v4.1*
