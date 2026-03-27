# 🎯 Parallel Orchestration Skill

> **Orquestación Multi-Agente con Monitoreo de Terminales Visibles**

El skill está listo y funcional.

## Estructura

| Directorio  | Propósito                                   |
| ----------- | ------------------------------------------- |
| **tools/**  | Scripts de orquestación y logs de ejecución |
| **SKILL.md** | Documentación completa                      |

## 📚 Documentación Completa

Para detalles completos, ver [SKILL.md](SKILL.md)

## 🔗 Relación con Otros Skills

- Usa **fork-terminal** (#22) para spawning de terminales
- Complementa **dispatching-parallel-agents** (#11) para orquestación visible
- Integra con **verification-before-completion** (#14) para validación

## 🎯 Cuándo Usar

Usa este skill cuando:
- Distribuyes trabajo entre múltiples agentes
- Necesitas monitoreo en tiempo real
- Tareas complejas multi-paso requieren visibilidad
- Se necesita reporte consolidado

**Alternativa**: Usa #11 dispatching-parallel-agents para paralelización en background sin necesidad de monitoreo.

---

**Created**: 2026-01-22
**Status**: ✅ Ready for Use
