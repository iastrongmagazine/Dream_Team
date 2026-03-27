import sys
import os
from pathlib import Path

# Add path to find utils
sys.path.append(os.path.abspath("09_System/hooks"))

try:
    from utils.common import speak
    print("Import exitoso. Probando voz...")
    speak("Prueba de diagnóstico de voz Invictus.")
except ImportError as e:
    print(f"Error de importación: {e}")
except Exception as e:
    print(f"Error general: {e}")
