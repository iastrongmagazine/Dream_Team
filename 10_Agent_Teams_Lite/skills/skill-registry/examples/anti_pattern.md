# Anti-Pattern: Skills Sin Registro

## Problema

❌ **Crear skill y no registrarla**

```
Agente: *Crea nueva skill*
Usuario: "¿Cómo la encuentro?"
Agente: "No sé, busca en los folders"
```

## Por qué está mal

1. Skills no son discoverables
2. Duplicación de effort
3. Inconsistencia en el sistema

## Solución Correcta

✅ **Registrar siempre**

```
Agente: *Crea nueva skill*
Agente: *Ejecuta skill-registry para actualizar*
Agente: *Nueva skill visible en el índice*
```

---

**Regla:** Nueva skill = actualizar registry.
