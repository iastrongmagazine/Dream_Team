---
name: fireflies-sync
description: Sync new Fireflies meetings to local Knowledge folder.
---

# Fireflies Sync

Check for new Fireflies meetings and sync them to your local 03_Knowledge/Transcripts folder.

## Instructions

### Step 1: Check for New Meetings
Call `check_new_meetings` via Fireflies MCP.

### Step 2: Resumen y Sincronización
Para cada reunión encontrada:
1. Generar un resumen de la reunión.
2. Validar si debe sincronizarse según los **Goals** (`00_Core/GOALS.md`) y **Conocimientos** actuales.
3. Si es relevante, llamar a `sync_meeting_to_local`.

### Step 3: Integración en Morning Planning
Este proceso debe ser invocado por el script de `04_Engine/08_Scripts_Os/14_Morning_Standup.py` [PENDIENTE DE VALIDACIÓN: Morning_Planning.py no existe, ¿debería ser Morning_Standup.py?].
