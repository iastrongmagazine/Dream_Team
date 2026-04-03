# Design: Video_Intel Skill

## Technical Approach

Build a modular Python skill with three core components: Video Analyzer (yt-dlp + whisper), Repo Scanner (git clone + AST parsing), and Synthesis Engine (combines video + repo data → implementation plan). CLI-based with JSON/markdown output, designed for agent workflow integration.

## Architecture Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| **Language** | Python | yt-dlp, whisper, AST libraries have mature Python SDKs; aligns with existing OS skills |
| **CLI Framework** | Click | Lightweight, existing pattern in PersonalOS; supports subcommands and hooks |
| **Output Format** | JSON + Markdown | JSON for programmatic use; Markdown for human readability |
| **Caching** | File-based (temp dir) | Simple, no external DB; transcriptions cached as .txt files |
| **Error Handling** | Graceful degradation | Partial failures don't block entire pipeline; clear error messages |

## Data Flow

```
YouTube URL ──▶ Video Analyzer ──▶ Transcript + Metadata
                                              │
GitHub URL ──▶ Repo Scanner ──▶ Code Map      │  Synthesis Engine  ──▶ Implementation Plan
                                              │
                                    OS Verification ──▶ Tool Availability
```

**Pipeline stages:**
1. **Video Analyzer**: `yt-dlp --write-subs --write-auto-subs` → extract metadata → whisper for transcription → output .txt
2. **Repo Scanner**: `git clone` to temp → AST parse for imports/functions → generate code map JSON
3. **Synthesis Engine**: Receive all inputs → identify methodologies → extract demo URLs → verify against OS → output plan

## File Changes

| File | Action | Description |
|------|--------|-------------|
| `.agent/03_Skills/00_Video_Intel/SKILL.md` | Create | Main skill definition and trigger patterns |
| `.agent/03_Skills/00_Video_Intel/video_analyzer.py` | Create | yt-dlp + whisper transcription module |
| `.agent/03_Skills/00_Video_Intel/repo_scanner.py` | Create | Git clone + AST parsing module |
| `.agent/03_Skills/00_Video_Intel/synthesis_engine.py` | Create | Plan generation + OS verification |
| `.agent/03_Skills/00_Video_Intel/cli.py` | Create | Click-based CLI entry point |
| `.agent/03_Skills/00_Video_Intel/__init__.py` | Create | Package init |

## Interfaces / Contracts

```python
# CLI Interface
@cli.command()
@click.argument('video_url')
@click.option('--repo', '-r', help='GitHub repository URL')
@click.option('--output', '-o', default='implementation_plan.md')
@click.option('--format', '-f', type=click.Choice(['json', 'markdown']), default='markdown')
@click.option('--verbose', '-v', is_flag=True)
def analyze(video_url, repo, output, format, verbose):
    """Analyze YouTube video and optional repo to generate implementation plan."""
    pass

# Output Schema (JSON)
{
    "video": {"title": "...", "duration": "...", "channel": "..."},
    "transcript": "...",
    "methodologies": [{"name": "...", "steps": [...], "tools": [...]}],
    "demo_urls": [{"url": "...", "type": "..."}],
    "os_verification": {"available": [...], "missing": [...]},
    "implementation_plan": {"prerequisites": [...], "steps": [...], "complexity": "..."}
}
```

## Testing Strategy

| Layer | What to Test | Approach |
|-------|-------------|----------|
| Unit | VideoAnalyzer.download(), RepoScanner.clone() | Mock yt-dlp, git; assert calls |
| Integration | Full pipeline with test video | Use provided test URL |
| E2E | CLI end-to-end | Verify output format, error handling |

## Migration / Rollout

No migration required. New skill creation — no existing data affected.

## Open Questions

- [ ] **Whisper model selection**: Use `base` for speed or `medium` for accuracy?
- [ ] **AST parsing depth**: Parse to file-level only or include function bodies?
- [ ] **LLM integration**: Use OpenAI, Claude, or both for methodology extraction?