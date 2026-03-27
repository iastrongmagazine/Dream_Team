# Script para reproducir un sonido cuando se usa TodoWrite
# Se ejecuta después de cada llamada a la herramienta TodoWrite

# Reproducir sonido del sistema de Windows
# Opciones disponibles:
# - Asterisk (información general)
# - Beep (alerta)
# - Exclamation (advertencia)
# - Hand (error/stop)
# - Question (pregunta)

try {
    # Reproducir sonido de éxito/completado
    [System.Media.SystemSounds]::Asterisk.Play()

    # Alternativas para personalizar:
    # Doble beep ascendente:
    # [Console]::Beep(800, 150)
    # [Console]::Beep(1000, 150)

    # Beep de notificación más largo:
    # [Console]::Beep(1200, 300)
} catch {
    # Silenciosamente ignorar errores para no interrumpir Claude Code
}

exit 0
