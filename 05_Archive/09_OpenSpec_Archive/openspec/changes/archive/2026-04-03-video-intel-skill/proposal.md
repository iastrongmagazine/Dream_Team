# Proposal: Video_Intel Skill

## Intent

Create an AI agent skill that extracts structured knowledge from YouTube videos and GitHub repositories to build implementation plans. The skill will analyze video content (using test video https://www.youtube.com/live/3psHUg6KzOo?si=Y6bZACLup04IfPCF as primary target), parse repository code, and synthesize methodologies into actionable implementation guides verified against the operating system.

## Scope

### In Scope
- YouTube video transcription and analysis via yt-dlp + whisper
- GitHub repository cloning and code extraction
- Methodologies and prompts identification from video content
- Demo/sandbox environment detection and verification
- OS capability detection (tools, libraries, commands available)
- Implementation plan generation with dependency resolution

### Out of Scope
- Real-time video streaming analysis
- Multi-language transcription beyond English/Spanish
- Automated code execution (only verification, not execution)
- CI/CD integration

## Approach

Build a modular skill with three core components:
1. **Video Analyzer**: yt-dlp for metadata extraction, whisper for transcription, GPT/Claude for content parsing
2. **Repo Scanner**: git clone + AST parsing for code structure extraction
3. **Synthesis Engine**: Combine video insights + repo code → implementation plan

Initial implementation: CLI-based with modular functions for easy integration into agent workflows.

## Affected Areas

| Area | Impact | Description |
|------|--------|-------------|
| `.agent/02_Skills/` | New | Create `Video_Intel/` skill directory |
| `skills/` | New | Core analysis scripts |

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|-------------|
| Video API rate limits | Medium | Cache transcriptions, use existing yt-dlp |
| Whisper accuracy | Medium | Validate with manual spot-check |
| OS verification failures | Low | Graceful degradation, user override |

## Rollback Plan

- Remove `.agent/02_Skills/Video_Intel/` directory
- Delete any cached transcription files
- No database or persistent state changes required

## Dependencies

- yt-dlp (video download/metadata)
- openai-whisper (transcription)
- gh CLI (repo access)
- Existing agent skills framework

## Success Criteria

- [ ] Test video analyzed and transcribed successfully
- [ ] At least one methodology extracted and documented
- [ ] GitHub repo cloning works with provided test URL
- [ ] OS verification reports available tools correctly
- [ ] Implementation plan generated with clear steps
