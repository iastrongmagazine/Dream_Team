# Anti-Pattern: Inicialización Prematura

## Problema

❌ **Saltar directamente a implementación sin inicializar SDD**

```bash
# MALO: Usuario quiere empezar a codear inmediatamente
Usuario: "No necesito SDD, solo ayúdame a crear el componente"
Agente: *Empieza a escribir código sin contexto*
```

## Por qué está mal

1. Sin contexto → decisiones tomadas sin trazabilidad
2. No hay forma de verificar contra specs
3. Historial perdido para future reference
4. Dificulta code review

## Solución Correcta

✅ **Inicializar SDD primero, luego trabajar**

```bash
# BIEN: Inicializar contexto primero
Agente: "Para mantener calidad y trazabilidad, inicialicemos SDD primero.
¿Tienes un nombre para el change?"
Usuario: "feature-user-auth"
Agente: *Inicializa SDD* → *Trabaja con contexto*
```

---

**Regla:** Siempre inicializar SDD para trabajos sustanciales (>1 hora).
