import winsound
import sys


def play_success_sound():
    """Sonido de tarea exitosa: doble beep armónico"""
    winsound.Beep(1000, 200)  # Frecuencia alta
    winsound.Beep(1500, 400)  # Frecuencia más alta, mayor duración


if __name__ == "__main__":
    play_success_sound()
