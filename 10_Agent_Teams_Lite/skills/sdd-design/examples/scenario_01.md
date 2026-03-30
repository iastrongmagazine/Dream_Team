# Scenario: Design para Auth

## Trigger

Specs aprobadas → "Ahora el diseño técnico"

## Design Generado

```yaml
architecture:
  components:
    - name: AuthController
      responsibility: Manejar requests HTTP de auth
      dependencies: [AuthService, TokenService]
    - name: AuthService
      responsibility: Lógica de negocio de auth
      dependencies: [UserRepository, TokenService]
    - name: TokenService
      responsibility: Crear/verificar JWT tokens
      dependencies: []

data_model:
  - entity: User
    fields:
      - name: id
        type: UUID
      - name: email
        type: string
      - name: password_hash
        type: string
      - name: created_at
        type: timestamp

api:
  - endpoint: /auth/login
    method: POST
    request:
      type: object
      properties:
        email: string
        password: string
    response:
      type: object
      properties:
        access_token: string
        refresh_token: string

decisions:
  - id: ADR-001
    title: "Usar JWT con refresh tokens"
    decision: "Implementar JWT access + refresh token rotation"
    rationale: "Balance entre seguridad y UX"
```

## Outcome

✅ Design aprobado → Listo para tasks
