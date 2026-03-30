# Scenario 01: Inicialización Básica

## Trigger

Usuario: "Vamos a trabajar en un nuevo proyecto de React. Iniciemos SDD."

## Proceso

```
1. Detect stack → package.json encontrado → React + TypeScript
2. Detectar convenciones → ESLint, Prettier, conventional commits
3. Seleccionar backend → Engram (default)
4. Crear estructura → sdd-init/ nuevo-proyecto/
```

## Output Esperado

```
✅ Stack detectado: React 19, TypeScript, Tailwind
✅ Convenciones: conventional-commits, ESLint
✅ Backend: Engram
✅ Estructura creada: sdd-init/nuevo-proyecto/
```

## Artifact Generado

```yaml
# sdd-init/nuevo-proyecto/state.yaml
project: nuevo-proyecto
backend: engram
stack:
  - react: 19
  - typescript: 5.x
  - tailwind: 4.x
conventions:
  - conventional-commits
  - eslint
  - prettier
created: 2026-03-30
```
