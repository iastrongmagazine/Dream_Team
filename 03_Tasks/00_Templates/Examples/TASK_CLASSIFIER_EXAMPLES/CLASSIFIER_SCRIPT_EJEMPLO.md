# Task Classifier - Ejemplo de Uso

## Script Usage

```bash
# Ejemplo 1: Tarea simple
python 04_ENGINE/08_Scripts_Os/59_Task_Classifier.py "Fix typo en README" 1 1
# Output: CORTO (score: 4)

# Ejemplo 2: Feature medio
python 04_ENGINE/08_Scripts_Os/59_Task_Classifier.py "Agregar endpoint de usuarios" 4 5
# Output: MEDIO (score: 9)

# Ejemplo 3: Sistema complejo
python 04_ENGINE/08_Scripts_Os/59_Task_Classifier.py "Reestructurar sistema de autenticación con breaking changes" 12 20
# Output: SOTA (score: 15)
```
