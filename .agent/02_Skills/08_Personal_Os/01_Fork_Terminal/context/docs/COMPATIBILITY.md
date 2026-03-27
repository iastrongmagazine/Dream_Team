# Notas de Compatibilidad - Fork Terminal Skill

## Problema identificado: Timeout en Windows

### Error reportado:

```
timeout: invalid time interval '/t'
Try 'timeout --help' for more information.
```

### Causa:

El comando `timeout /t 10` es específico de CMD de Windows, pero cuando el terminal forked usa Git Bash u otro shell Unix-like, intenta ejecutar el comando Unix `timeout` que tiene una sintaxis diferente.

### Solución:

Usar comandos que sean compatibles con CMD de Windows nativo:

#### ✅ Comandos compatibles:

```bash
# Pausar y esperar input del usuario
pause

# Mostrar mensaje y pausar
echo Presiona cualquier tecla para continuar... && pause

# Listar archivos
dir /b
dir /s

# Cambiar directorio y ejecutar comando
cd directorio && comando
```

#### ❌ Evitar en comandos forked:

```bash
# Timeout estilo Unix (no funciona en CMD)
timeout /t 10

# Sleep estilo Unix
sleep 10
```

### Alternativa para delays:

Si necesitas un delay en CMD de Windows, usa:

```bash
# Windows CMD timeout (sin /t cuando se ejecuta desde bash)
timeout 10

# O usa ping como workaround
ping 127.0.0.1 -n 10 > nul
```

## Pruebas exitosas:

1. ✅ `echo` con múltiples comandos
2. ✅ `pause` para mantener ventana abierta
3. ✅ `dir` con flags de Windows
4. ✅ `cd` y ejecución de comandos encadenados

## Recomendación:

Para máxima compatibilidad en los cookbooks, usar comandos nativos de CMD de Windows o asegurarse de que los comandos sean cross-compatible entre shells.
