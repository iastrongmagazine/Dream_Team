# Auditoría Completa del Proyecto — PersonalOS v6.1

Este plan describe el proceso para auditar integralmente el sistema `Think_Different`, asegurando que cumpla con los estándares "Pure Green" y SOTA definidos en el núcleo de PersonalOS.

## User Review Required

> [!IMPORTANT]
> - La auditoría profunda (`profundo`) puede tomar varios minutos ya que utiliza ejecución paralela.
> - Se actualizarán los archivos `tree.txt` para reflejar la realidad arquitectónica actual.
> - Si se detectan archivos huérfanos o enlaces rotos, se informará para su resolución o se aplicará `gr --apply` bajo supervisión.

## Proposed Changes

### [Fase 1] Diagnóstico Inicial y Auditoría Dimensional
- Ejecutar `01_Auditor_Hub.py estructura` para validar las 8 carpetas base.
- Ejecutar `01_Auditor_Hub.py skills` para validar las categorías en `01_Core/03_Skills`.
- Ejecutar `01_Auditor_Hub.py health` para monitorear la salud global del sistema.

### [Fase 2] Auditoría Profunda y Guardian
- Ejecutar `01_Auditor_Hub.py profundo` para un análisis exhaustivo.
- Ejecutar el comando `gr` (System Guardian) para detección de:
    - Archivos huérfanos.
    - Enlaces rotos.
    - Ghost files (punteros sin archivo).
    - Inconsistencias de nombres (XX_Nombre).

### [Fase 3] Sincronización de Documentación
- Actualizar `README.md` con el estado post-auditoría.
- Sincronizar `00_Winter_is_Coming/AGENTS.md` si hay nuevas herramientas o cambios en el flujo.
- Generar nuevos mapas `tree.txt` en el root y dimensiones clave.
- Validar el `SCRIPTS_INDEX.md` para asegurar que todos los HUBs estén mapeados.

### [Fase 4] Certificación "Pure Green"
- Consolidar resultados en un reporte final de auditoría.
- Persistir los hallazgos en Engram para memoria a largo plazo.

## Open Questions

- ¿Deseas que aplique correcciones automáticas (`gr --apply`) si se detectan errores menores de nomenclatura o enlaces?
- ¿Tienes alguna dimensión específica (e.g. `07_Projects`) que requiera atención especial?

## Verification Plan

### Automated Tests
- `python 08_Scripts_Os/01_Auditor_Hub.py health` al finalizar.
- Verificación manual de los archivos `tree.txt` generados.

### Manual Verification
- Revisión de la jerarquía de directorios contra el mapa arquitectónico esperado.
