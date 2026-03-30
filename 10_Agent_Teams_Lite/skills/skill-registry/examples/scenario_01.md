# Scenario: Registro de Nueva Skill

## Trigger

Nueva skill creada → "Actualicemos el registry"

## Proceso

```
1. Escanear directorio:
   - 01_Core/03_Skills/
   
2. Extraer metadata:
   - Parsear SKILL.md frontmatter
   - Extraer name, description, category
   
3. Generar registry:
   - Crear registry.yaml
   - Actualizar SKILLS_INDEX.md
```

## Registry Generado

```yaml
registry:
  version: 2.0
  updated: 2026-03-30T10:00:00Z
  
  skills:
    - name: sdd-init
      path: 10_Agent_Teams_Lite/skills/sdd-init
      category: 5
      tags: [sdd, workflow]
      triggers: ["sdd init", "iniciar sdd"]
      description: Inicializa contexto SDD
      
    - name: react-19
      path: 01_Core/03_Skills/gentleman/02_Work/01_React_19
      category: 1
      tags: [react, frontend]
      triggers: ["react 19", "react compiler"]
      description: React 19 patterns
      
    # ... más skills
```

## Búsqueda de Skills

```bash
# Buscar por categoría
grep "category: 1" **/SKILL.md

# Buscar por tag
grep "tags:.*sdd" **/SKILL.md

# Buscar por trigger
grep "sdd init" **/SKILL.md
```
