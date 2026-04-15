# Ejemplo INCORRECTO (Bad Example)

## Escenario

**Contexto:** Un agente crea una skill sin seguir los estándares.

**Trigger:** "Rápido, necesito una skill para Python"

## Proceso Incorrecto

### 1. Sin Análisis Previo

```bash
# El agente crea la skill sin planificar
mkdir 01_Core/03_Skills/25_Python_Helper
touch 01_Core/03_Skills/25_Python_Helper/SKILL.md
```

### 2. Frontmatter Incompleto

```yaml
---
name: python
description: Python skill
# ❌ PROBLEMAS:
# - Descripción vaga
# - Falta categoría Anthropic
# - Sin author
# - Sin version
# - Sin tags
---
```

### 3. Contenido Sin Estructura

```markdown
# Python Skill

Esta skill es para Python.

## Uso

```python
print("hola")
```

## Más info

Ver docs de Python.
```

❌ **PROBLEMAS:**
- Sin estructura clara
- Sin ejemplos concretos
- Sin triggers específicos
- Sin referencias

### 4. Código Inseguro (MALO)

```python
# ANTES: Credenciales hardcodeadas (MALO)
# Pattern: SECRET_KEY = "literal-string"

# DESPUÉS: Usar variables de entorno
def create_token(user_id):
    secret = os.environ.get("JWT_SECRET")
    return jwt.encode({"sub": user_id}, secret, algorithm="HS256")

# ANTES: Sin validación (MALO)
# Pattern: return data.method()

# DESPUÉS: Validar inputs
def process(data):
    if not data:
        raise ValueError("Data required")
    return data.upper()
```

### 5. Sin Examples

```
25_Python_Helper/
├── SKILL.md
# ❌ PROBLEMA: No hay examples/
```

### 6. Sin Security Scan

```bash
# ❌ NUNCA hacer esto:
# Integrar sin validar seguridad
```

## Resultado

- ❌ Score: 35% (Failed)
- ❌ Security: 2 CRITICAL, 3 HIGH
- ❌ Documentación incompleta
- ❌ Sin ejemplos
- ❌ No integrar

---

## Correcciones Necesarias

| Problema          | Solución                                        |
|-------------------|-------------------------------------------------|
| Descripción vaga  | Seguir template de descripción específica       |
| Sin categoría     | Añadir `category: 1-9`                          |
| Código inseguro   | Usar variables de entorno, validar inputs       |
| Sin examples/     | Crear examples/good_example.md y bad_example.md |
| Sin security scan | Ejecutar skill_security_scan.py                 |

---

**Key Takeaway:** El shortcut termina costando más. Siempre seguir el proceso completo.
