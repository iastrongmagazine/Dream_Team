# Anti-Pattern: Verificación Superficial

## Problema

❌ **No verificar realmente contra specs**

```python
# Verificación mala
def verify_implementation():
    # No verifica nada!
    return True
```

## Por qué está mal

1. Specs no se cumplen sin validación real
2. Bugs llegan a producción
3. Technical debt invisible

## Solución Correcta

✅ **Verificación sistemática**

```python
# Verificación buena
def verify_implementation(user_repo, spec):
    # 1. Verificar schema
    assert user_repo.has_field('id')
    assert user_repo.has_field('email')
    assert user_repo.has_field('password_hash')
    
    # 2. Verificar constraints
    assert user_repo.id.is_uuid()
    assert user_repo.email.is_unique()
    
    # 3. Verificar tests
    assert test_coverage > 80%
```

---

**Rule:** Verification must be evidence-based, not assumed.
