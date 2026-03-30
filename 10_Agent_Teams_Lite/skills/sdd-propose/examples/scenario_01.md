# Scenario: Proposal para Auth System

## Trigger

Usuario: "Formalicemos la propuesta para el sistema de autenticación"

## Proposal Generado

```yaml
change: implement-auth-system
intent: >
  El sistema actual no tiene autenticación robusta.
  Los usuarios no pueden hacer login de forma segura.
  Necesitamos implementar JWT auth con refresh tokens.

scope:
  in:
    - Login con email/password
    - Registro de usuarios
    - JWT access tokens
    - Refresh token rotation
    - Logout
  out:
    - OAuth2/Social login
    - 2FA
    - Password reset

approach:
  1. Crear modelos de usuario en DB
  2. Implementar JWT handler
  3. Crear endpoints de auth
  4. Añadir middleware de verificación
  5. Tests de integración

risks:
  - Token expiry: Usar refresh tokens
  - XSS: HttpOnly cookies
  - Brute force: Rate limiting
```

## Outcome

✅ Proposal aprobada por el usuario
✅ Listo para spec
