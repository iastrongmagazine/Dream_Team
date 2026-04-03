---
name: recording-mode
description: "Use when user wants to record meetings, conversations, or voice notes with automatic anonymization. Trigger: user says 'record this', 'transcribe meeting', 'anonymize recording', or 'voice note'."
---

# Recording Mode — Anonimización Automática

> "Graba sin exponer. Procesa sin comprometer." — Anti-system philosophy

## Overview

Sistema completo: transcripción + anonimización PII + almacenamiento + indexación.

```
Audio → TRANSCRIBE → ANONYMIZE → STORE → INDEX
```

---

## Inputs

### Audio Sources: microphone, file, screen, stream

### Config Privacidad (templates/privacidad.md)

```markdown
## PII a Anonimizar
| Tipo      | Pattern                                       | Token     |
|-----------|-----------------------------------------------|-----------|
| Email     | r'\b[\w.-]+@[\w.-]+\.\w+\b'                   | [EMAIL]   |
| Teléfono  | r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b'              | [TEL]     |
| Nombre    | r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'               | [PERSONA] |
| SSN       | r'\b\d{3}-\d{2}-\d{4}\b'                      | [SSN]     |
| Tarjeta   | r'\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b' | [TARJETA] |
| Dirección | r'\b\d+\s[\w\s]+\s(st                         | av        | calle)\b'          | [DIRECCION] |
| IP        | r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'     | [IP]      |
| Password  | r'\b(pass                                     | password  | pwd)\s*[:=]\s*\S+' | [PASSWORD]  |

## Niveles: basic (2), standard (5), strict (8)
## Retención: Audio 30d, Transcript 90d, Anonimized indefinite
```

---

## Proceso

### 1. Transcripción
```python
model = load_whisper_model('small')  # Recommended
result = model.transcribe(audio, word_timestamps=True)
```
| Model     | Speed   | Accuracy   |
|-----------|---------|------------|
| tiny      | ~10x    | Basic      |
| base      | ~7x     | Good       |
| **small** | ~4x     | Very Good  |
| medium    | ~2x     | Excellent  |
| large     | 1x      | Best       |

### 2. Detección PII
```python
def detect_pii(text, config):
    for pattern in config.patterns:
        matches = re.finditer(pattern, text)
        if should_anonymize(match, context):
            pii_locations.append({'type': pii_type, 'match': match.group()})
    return deduplicate_overlaps(pii_locations)
```

### 3. Anonimización
```python
def anonymize(text, pii_locations):
    for pii in sorted(pii_locations, key=lambda x: x['start'], reverse=True):
        text = text.replace(pii['match'], get_token(pii['type']))
    return text
```

### 4. Almacenamiento
```markdown
---
created: 2026-03-31T14:30:00Z
type: transcription
anonymized: true
privacy_level: strict
duration: 45min
---
[00:00] [PERSONA] inicia
[00:05] Se discute [PROYECTO] con [EMAIL]
```

---

## Output

1. **Transcripción anonymized** - Segura para compartir
2. **Resumen ejecutivo** - Puntos clave, decisiones, action items
3. **Metadata indexable** - Sin PII, searchable

---

## Gotchas & Edge Cases

### A. Captura
1. Audio ruido (SNR<10dB): Warn "Calidad muy baja"
2. Formato no soportado: Fail + sugerir conversión
3. Duración excesiva (>4hr): Warn + dividir
4. Audio silencioso (>50% silence): Warn
5. Multi-speaker: [HABLANTE_1], [HABLANTE_2]
6. Idioma mixto: Warn en metadata

### B. Transcripción
7. Model load fail: Fallback a smaller model
8. Timeout: Chunk en 10min segmentos
9. Caracteres especiales: UTF-8 correct
10. Code-switching: Warn si idioma cambia
11. Audio truncado: "[INCOMPLETO]" en timestamp

### C. PII Detection
12. False positives: "El CEO" → verificar contexto
13. False negatives: "mi jefe" → no detectado, warn
14. Accented names: "José", "María" → normalizar
15. Context ambiguity: "Madrid" ciudad/dirección → contexto

### D. Anonimización
16. Name consistency: Mismo nombre → mismo token
17. Unicode normalization: "café" → "cafe"
18. Nested: Order matters

### E. Privacidad
19. No consent: Warn + marcar metadata
20. Legal: GDPR, CCPA compliance

### F. Storage
21. Large files (>100MB): Compress before store
22. Disk full: Verify before write
23. Corrupt files: Skip + log

### G. Indexing
24. Search false positives: Buscar nombre → encontrar anonymized
25. Search optimization: Index sin tokens PII

### H. Sistema
26. API rate limits: Handle cloud limits
27. Network offline: Fallback local model
28. Permission denied: Error claro

---

## File Structure

```
04_Recording_Mode/
├── SKILL.md
├── templates/privacidad.md
├── recordings/.gitkeep
├── transcripts/
└── examples/transcript_example.md
```

---

## Implementation

| Scenario                 | Behavior         |
|--------------------------|------------------|
| Audio format unsupported | Fail             |
| PII detection timeout    | Warning          |
| Storage full             | Fail             |
| Model load fail          | Fallback smaller |
| Network offline          | Queue/local      |

---

## Changelog

| Date       | Change              |
|------------|---------------------|
| 2026-03-31 | Initial design v1.0 |
