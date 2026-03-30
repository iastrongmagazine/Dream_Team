# Scenario: Tasks para Auth

## Trigger

Design aprobado → "Desglosemos en tareas"

## Tasks Generado

```yaml
tasks:
  - id: TASK-001
    description: Crear modelo User en DB
    spec_ref: REQ-001
    design_ref: data_model.User
    dependencies: []
    status: pending

  - id: TASK-002
    description: Implementar JWT TokenService
    spec_ref: REQ-002
    design_ref: architecture.TokenService
    dependencies: []
    status: pending

  - id: TASK-003
    description: Crear AuthService con login logic
    spec_ref: REQ-001
    design_ref: architecture.AuthService
    dependencies: [TASK-001, TASK-002]
    status: pending

  - id: TASK-004
    description: Crear endpoint POST /auth/login
    spec_ref: REQ-001
    design_ref: api./auth/login
    dependencies: [TASK-003]
    status: pending

  - id: TASK-005
    description: Implementar rate limiting
    spec_ref: REQ-001
    design_ref: security.rate-limit
    dependencies: [TASK-004]
    status: pending

  - id: TASK-006
    description: Tests de integración para login
    spec_ref: REQ-001
    design_ref: testing.integration
    dependencies: [TASK-005]
    status: pending
```

## Outcome

✅ 6 tasks ready → Start implementation
