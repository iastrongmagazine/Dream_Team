# Scenario: Anti-Pattern - Scope Creep

## Problema

❌ **Agregar features fuera de scope**

```
Usuario: "Ya que estás en auth, agrega OAuth2 también"
Agente: *Agrega OAuth2 sin approval*
```

## Por qué está mal

1. Scope creep sin documentación
2. No hay specs para nuevas features
3. Verification no puede validar
4. Timeline se extiende indefinidamente

## Solución Correcta

✅ **Registrar como nuevo change**

```
Agente: "Interesante feature. Para mantener calidad:
1. Creemos una nueva proposal para OAuth2
2. Aprobemos el scope actual primero
3. Luego planificamos OAuth2"
```

---

**Regla:** Una change = un scope definido. Siempre pedir approval para expansions.
