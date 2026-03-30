# Scenario: Spec para Auth Login

## Trigger

Proposal aprobada → "Pasemos a specs"

## Spec Generado

```yaml
specs:
  - id: REQ-001
    description: >
      El usuario debe poder hacer login con email y password
    acceptance:
      - Login exitoso con credenciales válidas
      - Error con credenciales inválidas
      - Rate limiting después de 5 intentos

  - id: REQ-002
    description: >
      El sistema debe retornar JWT después de login exitoso
    acceptance:
      - Token tiene 15 min de expiración
      - Token contiene user_id
      - Token es válido para requests subsiguientes

scenarios:
  - id: SCN-001
    description: Login exitoso
    given: Usuario registrado con email test@test.com
    when: Envía POST /auth/login con credenciales válidas
    then: Retorna 200 con JWT token

  - id: SCN-002
    description: Login con password incorrecto
    given: Usuario registrado
    when: Envía password incorrecto
    then: Retorna 401 Unauthorized

  - id: SCN-003
    description: Rate limiting
    given: 5 intentos fallidos
    when: Intento 6to
    then: Retorna 429 Too Many Requests
```
