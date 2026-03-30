# Scenario: Archive de Auth Complete

## Trigger

Verification aprobada → "Archivemos el cambio"

## Proceso de Archive

```
1. Merge specs:
   - Copiar specs/auth/spec.md → specs/main/auth/
   - Actualizar índice

2. Merge design:
   - Copiar design/auth/adr.md → design/main/
   - Actualizar architecture.md

3. Cleanup:
   - Archivar artifacts temporales
   - Limpiar branches merging
   
4. Generar reporte:
   - Consolidar lessons learned
   - Documentar siguiente steps
```

## Archive Report Generado

```yaml
archive_report:
  change: implement-auth-system
  status: completed
  completed_at: 2026-03-30T14:00:00Z
  
  artifacts_merged:
    - specs/main/auth/login.md
    - specs/main/auth/register.md
    - design/main/auth/adr-001.md
    
  summary:
    features_added:
      - Login con JWT
      - Registro de usuarios
      - Rate limiting
    bugs_fixed: []
    breaking_changes: none
    
  lessons_learned:
    - JWT refresh tokens son necesarios para UX
    - Rate limiting debe ser configurable
    
  next_steps:
    - Implementar OAuth2 en siguiente change
    - Agregar 2FA para mayor seguridad
```

## Outcome

✅ Cambio archivado → SDD cycle complete
