# Exploration: Video_Intel Skill

## Context

El usuario quiere investigar y pensar a través de la creación de una skill "Video_Intel" que analiza contenido de YouTube/GitHub y se integra en PersonalOS.

## Current State

### Skills Existentes Relacionadas

| Skill | Propósito | Estado |
|-------|-----------|--------|
| `Video_Visuals_Producer` | Crear contenido de video, guiones, assets | Activa (`.claude/04_Skills/`) |
| `Quick_Capture` | Captura rápida a markdown con parsing | Referencia de patrón |
| `Skill_Creator` | Crear nuevas skills | Referencia para estructura |
| `Firecrawl` | Web scraping | Referencia para scraping |

### Estructura de Skills en PersonalOS

- **Ubicación**: `01_Core/03_Skills/` (numeradas 00-18)
- **Template**: `01_Core/03_Skills/SKILL_TEMPLATE/SKILL.md`
- **Patrón de nomenclatura**: `XX_Nombre_Skill/SKILL.md`

## Affected Areas

| Archivo/Directorio | Por qué se afecta |
|--------------------|-------------------|
| `01_Core/03_Skills/` | Nueva skill agregado |
| `01_Core/05_Mcp/` | Potencial integración MCP |
| `01_Core/09_Server/` | Backend para análisis |
| `.agent/02_Skills/` | Registro de skills |

## Approaches

### 1. Transcript-Based Video Intelligence (RECOMENDADA)

Extrae transcripts de YouTube y procesa con análisis de contenido.

**Pros:**
- APIs maduras: `youtube-transcript-api`, `yt-dlp`
- Sin costo (no requiere API key de YouTube)
- Transcripts ya tienen estructura semántica
- Compatible con flujos existentes de análisis de texto

**Cons:**
- Solo funciona si el video tiene subtitles automáticos o manual
- No extrae metadata rica (likes, views) sin API key
- Limitado a YouTube

**Esfuerzo:** Medium

### 2. GitHub Repository Intelligence

Analiza repositorios de GitHub (readme, código, issues) para inteligencia de proyectos.

**Pros:**
- APIs públicas bien documentadas (GitHub REST API)
- Información rica: repos, commits, issues, PRs
- GitHub es fuente primaria de código técnico

**Cons:**
- Requires GitHub token para evitar rate limits
- Contenido técnico específico, no general

**Esfuerzo:** Medium

### 3. Multi-Source Unified Intelligence

Combina YouTube + GitHub + web scraping en una skill unificada.

**Pros:**
- Cobertura completa de fuentes de contenido técnico
- Sinergia entre video y código

**Cons:**
- Más complejo de implementar
- Múltiples fuentes = más puntos de falla
- Mayor mantenimiento

**Esfuerzo:** High

## Recommendation

**Approach 1: Transcript-Based Video Intelligence** como MVP.

### Justificación

1. **Simplicidad**: Transcript API es simple y sin autenticación
2. **Valor inmediato**: YouTube es la fuente #1 de contenido educativo
3. **Patrón existente**: Se alinea con `Quick_Capture` (input → parse → save)
4. **Extensibilidad**: Fácil agregar GitHub después

### Scope MVP

```
Video_Intel (v1.0.0)
├── Input: YouTube URL
├── Process: Extract transcript + basic analysis
├── Output: Markdown con summary, timestamps, key topics
└── Storage: PersonalOS inbox/ o carpeta dedicada
```

### Features v1.0.0

- [ ] YouTube URL → Video ID extraction
- [ ] Transcript fetch via `youtube-transcript-api`
- [ ] Basic summary generation (topics, key moments)
- [ ] Save as markdown con frontmatter
- [ ] Error handling para videos sin transcript

## Risks

- **Rate limits**: YouTube puede limitar requests
- **Transcript availability**: No todos los videos tienen subtitles
- **Processing time**: Videos largos = más tiempo
- **Content quality**: Transcripts automáticos pueden tener errores

## Ready for Proposal

**SÍ** — La exploración está lista para pasar a fase de Proposal.

### Siguiente paso sugerido

Crear `/sdd-propose video-intel-skill` con:
- Propósito claro: "Skill para extraer y analizar transcripts de YouTube"
- Scope: MVP focalizado en YouTube transcript extraction
- Approach: Script Python + skill wrapper
- Integración: `01_Core/03_Skills/19_Video_Intel/`

---

*Exploration completed: 2026-04-03*
*Requested by: User*
*Artifact: sdd/video-intel-skill/explore*