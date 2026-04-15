# Ejemplo CORRECTO (Good Example)

## Escenario

**Contexto:** Un usuario quiere crear una nueva skill para PersonalOS.

**Trigger:** "Quiero crear una skill para manejar autenticación JWT"

## Proceso Correcto

### 1. Análisis Inicial

```bash
# El agente identifica la necesidad
- Tipo: Library/API Reference (Categoría 1)
- Scope: Autenticación JWT en Python
- Requisitos: Seguridad, validación, refresh tokens
```

### 2. Uso del Template

```bash
# Copiar template
cp -r 01_Core/03_Skills/SKILL_TEMPLATE/ 01_Core/03_Skills/25_JWT_Auth/
```

### 3. Personalización del Frontmatter

```yaml
---
name: jwt-auth
description: >
  Manejo de autenticación JWT para APIs Python.
  Úsalo cuando: (1) implementes login/register,
  (2) necesites middleware de autenticación,
  (3) manejes refresh tokens.
  NO usar para: OAuth2 (ver skill dedicada).
author: gentleman-programming
version: 1.0.0
category: 1
tags: [auth, jwt, security, python]
---
```

### 4. Implementación con Seguridad

```python
# scripts/jwt_handler.py - Ejemplo BUENO (CORRECTO)

import jwt
import os
from datetime import datetime, timedelta
from typing import Optional

class JWTAuth:
    def __init__(self, secret_key: str = None, algorithm: str = "HS256"):
        # CORRECTO: Usar env vars o parámetro, nunca hardcoded
        # Pattern: var = param or os.environ.get("KEY")
        self.secret_key = secret_key or os.environ.get("JWT_SECRET")
        self.algorithm = algorithm

    def create_token(self, user_id: str, expires_in: int = 3600) -> str:
        """Crear token JWT de forma segura."""
        payload = {
            "sub": user_id,
            "exp": datetime.utcnow() + timedelta(seconds=expires_in),
            "iat": datetime.utcnow()
        }
        return jwt.encode(payload, self.secret_key, algorithm=self.algorithm)

    def verify_token(self, token: str) -> Optional[dict]:
        """Verificar token JWT con manejo de errores."""
        try:
            return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
        except jwt.ExpiredSignatureError:
            logger.warning("Token expired")
            return None
        except jwt.InvalidTokenError as e:
            logger.error(f"Invalid token: {e}")
            return None
```

### 5. Ejemplos Documentados

```markdown
## examples/good_example.md

### Login básico (CORRECTO)
```python
# Usar variable de entorno o parámetro
auth = JWTAuth()  # Lee JWT_SECRET del entorno
token = auth.create_token(user_id="123")
```

### Verificar token (CORRECTO)
```python
payload = auth.verify_token(token)
if payload:
    user_id = payload["sub"]
```
```

## Resultado

- ✅ Score: 92% (Excellent)
- ✅ Security: 0 CRITICAL, 0 HIGH
- ✅ Documentación completa
- ✅ Ejemplos claros
- ✅ Listo para producción

---

**Key Takeaway:** Seguir el template + validar seguridad = Skill de calidad
