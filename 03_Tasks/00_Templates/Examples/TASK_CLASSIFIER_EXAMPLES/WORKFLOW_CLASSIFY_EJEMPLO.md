# Workflow Classify Task - Ejemplo

## Session

**User:** /classify-task

**AI:** Cual es la tarea?

**User:** Agregar backups automaticos antes de sincronizar

**AI:**
| Pregunta                       | Opciones                       |
|--------------------------------|--------------------------------|
| Tiempo estimado?               | <2h / 2-8h / 8h+               |
| Archivos?                      | 1-2 / 3-10 / 10+               |

**User:** 2 horas, 3 archivos

**AI:**
```
## Clasificacion

| Criterio                  | Valor                 | Template                 |
|---------------------------|-----------------------|--------------------------|
| Esfuerzo                  | 2h                    | MEDIO                    |
| Archivos                  | 3                     | MEDIO                    |
| Complejidad               | Media                 | MEDIO                    |

**Template:** MEDIO
```

**User:** Confirmado

**AI:** Aplicando template 04_Task_Template_Medio.md
```
