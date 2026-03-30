# Anti-Pattern: No Archivar Cambio

## Problema

❌ **No archivar después de completar**

```
Usuario: "Listo, verified y mergeado. Fin."
Agente: *No hace archive*
```

## Por qué está mal

1. Specs no se consolidan
2. Perdemos trace del change
3. Knowledge no se compounding

## Solución Correcta

✅ **Siempre archivar**

```
Agente: "Voy a archivar el change para consolidar specs."
*Ejecuta sdd-archive*
*Genera lessons_learned*
*Actualiza main specs*
```

---

**Regla:** SDD cycle no está completo hasta archivar.
