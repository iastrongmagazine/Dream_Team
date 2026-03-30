# Anti-Pattern: Task sin Dependencias

## Problema

❌ **Crear tareas sin identificar dependencias**

```yaml
tasks:
  - id: TASK-001
    description: Crear modelo User
    dependencies: []
  - id: TASK-002
    description: Crear AuthService
    dependencies: []  # ❌ MALO: Depende de TASK-001!
```

## Por qué está mal

1. Ejecución en orden incorrecto
2. Errores de implementación
3. Rework necesario

## Solución Correcta

✅ **Mapear todas las dependencias**

```yaml
tasks:
  - id: TASK-001
    description: Crear modelo User
    dependencies: []
  - id: TASK-002
    description: Crear AuthService
    dependencies: [TASK-001]  # ✅ CORRECTO
```

---

**Regla:** Siempre documentar dependencias explícitamente.
