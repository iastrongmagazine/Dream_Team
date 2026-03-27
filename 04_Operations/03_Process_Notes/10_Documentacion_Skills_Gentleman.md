# Documentación de Skills Gentleman (PersonalOS)

Este reporte documenta las capacidades (skills) instaladas en el sistema Gentleman para el desarrollo basado en especificaciones (SDD) y otras tareas automatizadas.

## Resumen de Skills

| Skill                          | Propósito                                                                                     |
|--------------------------------|-----------------------------------------------------------------------------------------------|
| `go-testing`                   | Patrones de testing para Go, incluyendo unit, integration y TUI (Bubbletea).                  |
| `sdd-apply`                    | Implementación de tareas de cambio siguiendo specs y diseño.                                  |
| `sdd-archive`                  | Sincronización de specs delta y archivado de cambios completados.                             |
| `sdd-design`                   | Creación de documentos de diseño técnico y decisiones de arquitectura.                        |
| `sdd-explore`                  | Investigación de código, ideas y requisitos antes de comprometerse a un cambio.               |
| `sdd-init`                     | Inicialización del contexto SDD, detección de stack y backend de persistencia.                |
| `sdd-propose`                  | Creación de propuestas de cambio con intención, alcance y enfoque.                            |
| `sdd-spec`                     | Escritura de especificaciones (delta specs) con requisitos y escenarios.                      |
| `sdd-tasks`                    | Desglose de cambios en checklists de tareas de implementación.                                |
| `sdd-verify`                   | Validación de implementación contra specs, diseño y tareas.                                   |
| `skill-creator`                | Creación de nuevas skills para agentes AI.                                                    |
| `skill-one`                    | Skill de ejemplo.                                                                             |
| `disabled-skill`               | Skill con invocación de modelo deshabilitada.                                                 |

## Escenario de Uso (SDD Workflow)

Para una nueva funcionalidad en PersonalOS:
1. `/sdd-init`: Inicializar el proyecto.
2. `/sdd-explore`: Investigar el código existente.
3. `/sdd-propose`: Proponer el cambio.
4. `/sdd-spec`: Definir los requisitos (delta specs).
5. `/sdd-design`: Diseñar la arquitectura.
6. `/sdd-tasks`: Desglosar las tareas.
7. `/sdd-apply`: Implementar (usando `go-testing` si es necesario).
8. `/sdd-verify`: Validar.
9. `/sdd-archive`: Archivar.
