# Video Intel - Technical Reference

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     CLI (Click)                                 │
├─────────────────────────────────────────────────────────────────┤
│                  SynthesisEngine                                │
│  ┌──────────────────┐    ┌──────────────────┐                  │
│  │  VideoAnalyzer   │    │    RepoScanner    │                 │
│  │  ─────────────── │    │  ─────────────── │                 │
│  │  yt-dlp          │    │  git clone       │                 │
│  │  whisper         │    │  AST parse       │                 │
│  └──────────────────┘    └──────────────────┘                  │
├─────────────────────────────────────────────────────────────────┤
│  Methodology Extraction + OS Verification + Plan Generation     │
└─────────────────────────────────────────────────────────────────┘
```

## Video Analysis Pipeline

### Step 1: Metadata Extraction

```python
from video_intel import VideoAnalyzer

analyzer = VideoAnalyzer()
metadata = analyzer.download_metadata("https://youtube.com/...")
# Returns: {title, duration, channel, upload_date, description, ...}
```

### Step 2: Transcription

```python
# Downloads subtitles via yt-dlp
transcript_path = analyzer.transcribe("https://youtube.com/...", model="base")
```

### Step 3: Transcript Extraction

```python
# Parses VTT/SRT to plain text
transcript = analyzer.extract_transcript("https://youtube.com/...")
```

## Repository Scanning Pipeline

### Step 1: Clone

```python
from video_intel import RepoScanner

scanner = RepoScanner()
repo_path = scanner.clone_repo("https://github.com/user/repo")
```

### Step 2: AST Analysis

```python
code_map = scanner.generate_code_map(repo_path)
# Returns: {files, file_tree, summary}
```

## Synthesis Pipeline

```python
from video_intel import SynthesisEngine

engine = SynthesisEngine()
result = engine.synthesize(
    video_url="https://youtube.com/...",
    repo_url="https://github.com/..."
)
```

### Output Schema

```typescript
interface ImplementationPlan {
  prerequisites: Array<{
    tool: string;
    action: "install" | "update";
    description: string;
  }>;
  steps: Array<{
    description: string;
    category: "technique" | "demo" | "setup";
    methodology: string;
  }>;
  verification: Array<{
    type: "demo" | "completion" | "note";
    url?: string;
    description: string;
  }>;
  complexity: "low" | "medium" | "high";
  components: {
    video: VideoMetadata;
    transcript: string;
    methodologies: Methodology[];
    demo_urls: DemoUrl[];
    repo: RepoInfo | null;
    os_verification: OSVerification;
  };
}
```

## Error Handling

| Error | Cause | Solution |
|-------|-------|----------|
| "Video is private" | Video no es público | Proporcionar video público |
| "yt-dlp not installed" | Falta dependencia | `pip install yt-dlp` |
| "Repository requires auth" | Repo privado | `gh auth login` |
| "Failed to clone" | URL inválida | Verificar URL de repo |

## OS Verification

El motor verifica las siguientes herramientas:

- **Lenguajes**: python, node, go, rust, java
- **Frameworks**: react, vue, angular, nextjs, docker
- **Cloud**: aws, gcp, azure, vercel
- **AI**: openai, anthropic, claude

Para agregar herramientas, modificar `verify_os_capabilities()` en `synthesis_engine.py`.
