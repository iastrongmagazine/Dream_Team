import winsound
import json
import os
import time


def get_config_path():
    """Obtiene la ruta del config desde varias ubicaciones posibles"""
    possible_paths = [
        os.path.join(os.path.dirname(__file__), "..", "07_Installer", "config.json"),
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "05_System",
            "04_Env",
            "display_config.json",
        ),
        os.path.join(
            os.path.dirname(__file__), "..", "..", "05_System", "04_Env", "config.json"
        ),
    ]

    for config_path in possible_paths:
        if os.path.exists(config_path):
            return config_path

    return None


CONFIG_PATH = get_config_path()


def play_sound():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            config = json.load(f)
            side = config.get("side", "left")

            if side == "left":
                # Single Chime (A4 tone, 440Hz)
                winsound.Beep(440, 300)
            elif side == "right":
                # Double Chime
                winsound.Beep(440, 200)
                time.sleep(0.1)
                winsound.Beep(440, 200)
    else:
        # Default
        winsound.Beep(440, 300)


if __name__ == "__main__":
    play_sound()
