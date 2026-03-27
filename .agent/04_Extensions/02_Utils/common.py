import os
import subprocess
import time
import json

# Global state file for task counter
_STATE_FILE = os.path.join(".claude", "history", "sessions", "voice_state.json")
_LAST_NOTIFICATION_TIME = 0

def _load_state():
    """Load voice notification state from file."""
    try:
        if os.path.exists(_STATE_FILE):
            with open(_STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    except:
        pass
    return {"task_count": 0}

def _save_state(state):
    """Save voice notification state to file."""
    try:
        os.makedirs(os.path.dirname(_STATE_FILE), exist_ok=True)
        with open(_STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, indent=2)
    except:
        pass

def should_speak(priority="normal"):
    """
    Determines if a voice notification should be spoken based on:
    - Environment variable ENABLE_VOICE_NOTIFICATIONS (default: True)
    - Task counter (notify every 2 tasks for normal priority)
    - Cooldown timer (prevent notifications within 5 seconds)
    - Priority level (high priority always speaks)

    Args:
        priority: "high" (always speak), "normal" (every 2 tasks), "low" (never)

    Returns:
        bool: True if should speak, False otherwise
    """
    global _LAST_NOTIFICATION_TIME

    # Check if voice is globally disabled
    if os.environ.get("ENABLE_VOICE_NOTIFICATIONS", "1") == "0":
        return False

    # High priority always speaks (e.g., ritual completion, errors)
    if priority == "high":
        return True

    # Low priority never speaks
    if priority == "low":
        return False

    # Check cooldown (5 seconds) - High priority ignores cooldown for immediate feedback
    current_time = time.time()
    if priority != "high" and current_time - _LAST_NOTIFICATION_TIME < 5:
        return False

    # Normal priority: check task counter (every 2 tasks)
    state = _load_state()
    state["task_count"] = state.get("task_count", 0) + 1

    should_notify = (state["task_count"] % 2 == 0)

    _save_state(state)

    if should_notify:
        _LAST_NOTIFICATION_TIME = current_time

    return should_notify

def speak(text, priority="normal"):
    """
    Sintetiza voz usando PowerShell (SAPI o System.Speech) de forma no bloqueante.

    Args:
        text: Text to speak
        priority: "high" (always speak), "normal" (every 2 tasks), "low" (never)
    """
    # Check if we should speak based on smart logic
    if not should_speak(priority):
        return

    # Limpiar texto de comillas para evitar errores de inyección en PS
    clean_text = text.replace("'", "").replace('"', "")

    # Comando robusto que intenta System.Speech y cae a SAPI.SpVoice si falla
    # Se usa Popen para no bloquear el proceso principal del hook
    ps_command = (
        f"Add-Type -AssemblyName System.Speech -ErrorAction SilentlyContinue; "
        f"$speaker = New-Object System.Speech.Synthesis.SpeechSynthesizer -ErrorAction SilentlyContinue; "
        f"if ($speaker) {{ $speaker.Speak('{clean_text}') }} "
        f"else {{ (New-Object -ComObject SAPI.SpVoice).Speak('{clean_text}') }}"
    )

    try:
        subprocess.Popen(["powershell.exe", "-Command", ps_command],
                         stdout=subprocess.DEVNULL,
                         stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Error al intentar activar voz: {e}")

def visual_alert(text):
    """Muestra una alerta visual (msg.exe o MessageBox fallback)."""
    # Use full path for msg.exe and run in background to avoid blocking
    msg_path = os.path.join(os.environ.get('SystemRoot', 'C:\\Windows'), 'System32', 'msg.exe')
    if os.path.exists(msg_path):
        subprocess.Popen([msg_path, "*", text])
    else:
        # Fallback to PowerShell pop-up if msg.exe is missing
        clean_text = text.replace("'", "")
        ps_command = f"Add-Type -AssemblyName PresentationFramework; [System.Windows.MessageBox]::Show('{clean_text}', 'Claude Code Notification')"
        subprocess.Popen(["powershell.exe", "-Command", ps_command])

def log_to_json(hook_name, data):
    """Registra datos del hook en un archivo JSON específico."""
    import json
    from datetime import datetime

    log_path = os.path.join(".claude", "history", "sessions", f"{hook_name}.json")
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "data": data
    }

    # Append to JSON list
    try:
        if os.path.exists(log_path) and os.path.getsize(log_path) > 0:
            with open(log_path, "r", encoding="utf-8") as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(log_entry)

        with open(log_path, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Error escribiendo log JSON: {e}")
