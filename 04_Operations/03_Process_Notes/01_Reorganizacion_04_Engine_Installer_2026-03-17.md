# 19_Reorganizacion_04_Engine_Installer_2026-03-17

## Objetivo

Reorganizar la estructura del 04_Engine y crear un installer para migrar PersonalOS a otras máquinas.

## Contexto Previo

- Scripts sueltos en 04_Engine/ (00_ a 65_)
- Rutas hardcodeadas en algunos scripts (58, 59)
- No había forma de migrar PersonalOS a otra PC

## Acciones Realizadas

### 1. Enumeración de 04_Engine

- Corregir numeración de scripts (00, 64, 65)
- Scripts workflow: 00_Context_Reset, 00_Context_Switcher
- Scripts especiales: 64_Campanilla, 65_CTX_Generator

### 2. Crear Installer (07_Installer)

- `installer.py` - Entry point con dual mode (migrate/new)
- `config.json` - Tu configuración existente
- `config.template.json` - Template para nuevos usuarios
- `.mcp.template.json` - Template de MCPs con placeholders
- `scripts/detect_machine.py` - Detecta si es la misma PC
- `scripts/setup_dependencies.py` - Instala dependencias
- `scripts/configure_paths.py` - Configura rutas y APIs
- `scripts/validate.py` - Valida instalación

### 3. Mover Scripts a 08_Scripts_Os

- 65 scripts Python movidos de 04_Engine/ a 04_Engine/08_Scripts_Os/
- Actualizar rutas hardcodeadas en 58 y 59 para usar config.json

### 4. Actualizar Referencias

- 60_Fast_Vision.py
- 55_Avengers_Workflow.py
- 54_Commit_Guard.py
- 52_Safe_Commit.py
- 33_Parallel_Audit_Pro.py

### 5. Documentación

- README.md de 04_Engine actualizado
- README.md de 07_Installer creado

## Edge Cases Resueltos

| Edge Case                         | Solución                          |
|-----------------------------------|-----------------------------------|
| Rutas hardcodeadas                | Usar config.json                  |
| API keys inválidas                | Re-input automático               |
| .mcp.json existente               | Merge inteligente                 |
| Retry descargas                   | 3 intentos                        |
| Validar rutas                     | Antes de escribir                 |

## Resultados

- ✅ Stack validado (13_Validate_Stack.py PASS)
- ✅ Commits realizados
- ✅ Push a origin/main

## Pendientes

- Ninguno por ahora

## Lecciones

- Importante mapear dependencias antes de mover archivos
- Rutas dinámicas con config_paths.py evitan problemas
- El installer permite portabilidad total de PersonalOS
