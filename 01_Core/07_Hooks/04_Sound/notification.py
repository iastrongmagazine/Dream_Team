"""
Módulo de notificaciones de sonido para PersonalOS
Uso:
    python notification.py --task-complete
    python notification.py --notify "Mensaje"
    python notification.py --success
    python notification.py --error
"""

import os
import sys
import argparse
import platform

# Forzar encoding UTF-8 para consola Windows
if sys.platform == "win32":
    import io

    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")


def play_sound_windows(sound_type="Asterisk"):
    """Reproducir sonido del sistema Windows."""
    try:
        import winsound
        # FIX: Mapear a los nombres de alias correctos de Windows
        # winsound.PlaySound necesita el STRING del alias, no el flag
        alias_map = {
            "Asterisk":    "SystemAsterisk",
            "Exclamation": "SystemExclamation",
            "Hand":        "SystemHand",
            "Question":    "SystemQuestion",
            "Success":     "SystemAsterisk",
        }
        alias = alias_map.get(sound_type, "SystemAsterisk")
        winsound.PlaySound(alias, winsound.SND_ALIAS)
        return True
    except Exception:
        return False


def play_sound_beep(frequency=800, duration=150):
    """Reproducir beep usando Console.Beep (Windows) o echo (Unix)"""
    try:
        if sys.platform == "win32":
            import winsound

            winsound.Beep(frequency, duration)
        else:
            # Unix - usar beep o tput
            os.system(
                f'echo -e "\\a" > /dev/tty 2>/dev/null'
                if sys.platform != "win32"
                else ""
            )
        return True
    except Exception:
        return False


def task_complete_sound():
    """Sonido de tarea completada - garantizado con doble beep fallback."""
    print("[Sound] Task Complete...")

    if sys.platform == "win32":
        # Intentar sonido del sistema primero
        success = play_sound_windows("Asterisk")
        if not success:
            # FIX: Fallback garantizado - doble beep ascendente
            try:
                import winsound
                winsound.Beep(800, 150)
                winsound.Beep(1100, 200)
            except Exception:
                pass
    else:
        os.system('printf "\\a"')

    print("[OK] Sonido reproducido")


def success_sound():
    """Sonido de éxito"""
    print("✅ [Success]")
    if sys.platform == "win32":
        play_sound_windows("Exclamation")
    else:
        os.system('echo -e "\\a"')


def error_sound():
    """Sonido de error"""
    print("❌ [Error]")
    if sys.platform == "win32":
        play_sound_windows("Hand")
    else:
        os.system('echo -e "\\a"')


def notification(msg):
    """Notificación general"""
    print(f"🔔 [Notification] {msg}")
    if sys.platform == "win32":
        play_sound_windows("Asterisk")
    else:
        os.system('echo -e "\\a"')


def main():
    parser = argparse.ArgumentParser(description="PersonalOS Sound Notifications")
    parser.add_argument(
        "--task-complete", action="store_true", help="Sonido de tarea completada"
    )
    parser.add_argument("--success", action="store_true", help="Sonido de éxito")
    parser.add_argument("--error", action="store_true", help="Sonido de error")
    parser.add_argument("--notify", type=str, help="Notificación con mensaje")
    parser.add_argument("--beep", action="store_true", help="Beep simple")
    args = parser.parse_args()

    if args.task_complete:
        task_complete_sound()
    elif args.success:
        success_sound()
    elif args.error:
        error_sound()
    elif args.notify:
        notification(args.notify)
    elif args.beep:
        play_sound_beep()
    else:
        # Por defecto, sonido de tarea completa
        task_complete_sound()


if __name__ == "__main__":
    main()
