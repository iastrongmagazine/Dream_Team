---
name: video-intel
description: >
  Extrae conocimiento estructurado de videos de YouTube y repositorios de GitHub.
  Genera planes de implementacion verificados contra capacidades del OS.
  Trigger: "analizar video", "extraer de youtube", "plan de implementacion desde video",
  "transcribir video", "analizar repositorio", "extraer metodologias"
metadata:
  author: personalos
  version: "0.1"
  status: production
---

# Video Intel

## Estado

Skill en PRODUCCION. Ubicacion: `01_Core/03_Skills/19_Video_Intel/`

## Esencia Original

**Proposito:** Transformar contenido audiovisual (YouTube) y codigo (GitHub) en planes de accion ejecutables y verificados contra el sistema operativo del usuario.

**Por que existe esta skill:**
- Los videos de YouTube contienen conocimiento valioso pero no estructurado
- Las metodologias y tecnicas se demuestran pero no se documentan
- Los desarrolladores necesitan extraer pasos accionables desde videos
- El conocimiento debe verificarse contra lo que el usuario realmente tiene instalado

**Caso de uso principal:**
1. Usuario proporciona URL de video de YouTube
2. Skill transcribe y extrae metodologias
3. Opcional: proporciona URL de repositorio para contexto de codigo
4. Skill genera plan de implementacion con pasos verificables
5. Verifica herramientas requeridas contra el OS del usuario

## Triggers

| Pattern | Cuando usar |
|---------|-------------|
| "analizar video" | Extraer contenido de YouTube |
| "extraer de youtube" | Transcribir video |
| "plan de implementacion desde video" | Generar pasos desde video |
| "transcribir video" | Obtener transcripcion |
| "analizar repositorio" | Escanear codigo de GitHub |
| "extraer metodologias" | Identificar tecnicas en transcript |

## Modo de Uso

### CLI Basico

```bash
# Analizar video
python -m video_intel.cli analyze "https://www.youtube.com/watch?v=..."

# Con repositorio
python -m video_intel.cli analyze "VIDEO_URL" --repo "https://github.com/user/repo"

# Salida JSON
python -m video_intel.cli analyze "VIDEO_URL" --format json -o plan.json
```

### Como Modulo Python

```python
from video_intel import SynthesisEngine

engine = SynthesisEngine()
result = engine.synthesize(
    video_url="https://youtube.com/...",
    repo_url="https://github.com/..."
)

print(result["steps"])
print(result["prerequisites"])
```

## Componentes

| Modulo | Proposito |
|--------|-----------|
| `video_analyzer.py` | yt-dlp + whisper para metadata y transcripcion |
| `repo_scanner.py` | git clone + AST parsing para analisis de codigo |
| `synthesis_engine.py` | Combina datos y genera plan |
| `cli.py` | Interfaz Click para CLI |

## Output

El resultado incluye:

```json
{
  "prerequisites": [{"tool": "python", "action": "install"}],
  "steps": [{"description": "...", "category": "technique"}],
  "verification": [{"type": "demo", "url": "..."}],
  "complexity": "medium|high|low",
  "components": {
    "video": {"title": "...", "channel": "..."},
    "methodologies": [{"name": "...", "steps": [...], "tools": [...]}],
    "demo_urls": [{"url": "...", "type": "sandbox|playground"}],
    "os_verification": {"available": [...], "missing": [...]}
  }
}
```

## ⚠️ Gotchas

- **yt-dlp requerido**: Sin `yt-dlp` instalado, la extraccion de metadata falla. Instalar con `pip install yt-dlp`
- **Subtítulos requeridos**: Solo transcribe si el video tiene subtitles disponibles. Videos sin subtitles no se pueden transcribir
- **git requerido**: El scanner de repos necesita `git` instalado en el sistema
- **Autenticacion GitHub**: Repos privados requieren `gh auth login` o configurar SSH keys
- **Timeout en videos largos**: Videos de mas de 1 hora pueden timeout en descarga
- **Modelos whisper**: Por defecto usa modelo `base`. Para mayor precision usar `medium` (mas lento)
- **URLs de demo**: Solo detecta URLs en el transcript, no en metadata
- **Metodologias limitadas**: NLP simple - no extrae todo perfectamente. Revisar manualmente

## Recursos

- **Templates**: Ver [scripts/](scripts/) para modulos Python
- **Documentacion**: Ver [references/](references/) para guías adicionales

## Dependencies

```
yt-dlp>=2024.8.6
whisper>=20231117
click>=8.1.7
astor>=0.8.1
tiktoken>=0.7.0
```

## Notas

- Categoria: 19_ provisional - evaluar si va a 11_Doc_Processing
- Output en markdown generado en raíz del proyecto como `implementation_plan.md`
- El workspace usa directorio temporal que se limpia automaticamente
