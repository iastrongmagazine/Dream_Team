# Delta for Video_Intel Documentation

## Purpose

This delta spec documents updates to SKILL.md for the Video_Intel skill, adding Engram integration, explicit workflow documentation, video registry clarification, knowledge migration documentation, and expanded gotchas.

## ADDED Requirements

### Requirement: Engram Integration

The Video_Intel skill SHALL integrate with Engram for persistent memory storage using topic_key `unicorn/video-intel-skill`.

#### Scenario: Skill saves extracted knowledge to Engram

- GIVEN a video analysis has completed and extracted methodologies
- WHEN the skill calls `engram_mem_save()` with `topic_key: "unicorn/video-intel-skill"`
- THEN the extracted knowledge SHALL be persisted across sessions
- AND future invocations MAY retrieve prior analysis context

#### Scenario: Skill retrieves prior context from Engram

- GIVEN a user requests analysis of a video previously processed
- WHEN the skill calls `engram_mem_search()` with `topic_key: "unicorn/video-intel-skill"`
- THEN prior extraction results SHALL be retrieved for context

### Requirement: 9-Step Workflow Documentation

The SKILL.md SHALL document the complete 9-step workflow that the skill executes internally.

#### Scenario: Video analysis workflow executes

- GIVEN a user invokes the skill with a YouTube URL
- WHEN the workflow executes through all 9 steps
- THEN each step SHALL be traceable in the output logs

**The 9 Steps:**
1. **Video URL Validation** - Validate YouTube URL format
2. **Metadata Extraction** - Fetch video metadata via yt-dlp
3. **Transcript Download** - Download available subtitles
4. **Transcript Processing** - Clean and normalize text
5. **Methodology Extraction** - Identify techniques via NLP
6. **Demo URL Detection** - Extract sandbox/playground URLs
7. **Repository Scan (Optional)** - Clone and analyze code if provided
8. **OS Verification** - Check available tools against user OS
9. **Plan Synthesis** - Generate executable implementation plan

### Requirement: Video Registry Purpose

The `video_registry.py` module SHALL be documented as the global registry for tracking all analyzed videos.

#### Scenario: Registry tracks video analysis state

- GIVEN multiple video analyses have been performed
- WHEN `video_registry.py` is queried for history
- THEN it SHALL return metadata for all previously analyzed videos

#### Scenario: Global registry prevents duplicate processing

- GIVEN the same video URL is submitted for analysis
- WHEN the registry checks for existing entry
- THEN it SHALL return cached results instead of re-processing
- AND the user SHALL be notified of existing analysis

### Requirement: Knowledge Migration

The skill SHALL automatically migrate extracted knowledge to `02_Knowledge/05_Unicorn/` directory.

#### Scenario: Extracted knowledge persists to Unicorn

- GIVEN a video analysis completes successfully
- WHEN the synthesis engine finalizes output
- THEN extracted methodologies SHALL be written to `02_Knowledge/05_Unicorn/`
- AND subsequent skill invocations MAY read from this location

#### Scenario: Migration preserves folder structure

- GIVEN multiple videos are analyzed
- WHEN knowledge migrates to Unicorn directory
- THEN each video SHALL have its own subdirectory with:
  - `transcript.md` - Cleaned transcript
  - `methodologies.md` - Extracted techniques
  - `plan.md` - Implementation plan

### Requirement: Expanded Gotchas

The SKILL.md SHALL include 12 gotchas (expanded from 8), documenting known limitations and edge cases.

#### Scenario: User encounters gotcha condition

- GIVEN a gotcha condition exists in the current implementation
- WHEN the skill encounters this condition during execution
- THEN it SHALL log a warning with guidance
- AND the user SHALL see the warning in output

**The 12 Gotchas:**
1. **yt-dlp requerido** - Without `yt-dlp` installed, metadata extraction fails
2. **Subtítulos requeridos** - Only transcribes videos with available subtitles
3. **git requerido** - Repository scanner needs `git` installed
4. **Autenticación GitHub** - Private repos require `gh auth login` or SSH keys
5. **Timeout en videos largos** - Videos over 1 hour may timeout during download
6. **Modelos whisper** - Default `base` model; use `medium` for accuracy
7. **URLs de demo** - Only detects URLs in transcript, not metadata
8. **Metodologías limitadas** - NLP is simple; manual review recommended
9. **Cache de registry** - Large video histories may impact lookup performance
10. **Encoding UTF-8** - Transcript processing requires UTF-8 encoding
11. **API rate limits** - YouTube API may throttle repeated requests
12. **Disk space** - Repository cloning requires significant disk space

## MODIFIED Requirements

### Requirement: Gotchas Section Expansion

The existing "⚠️ Gotchas" section in SKILL.md SHALL be expanded from 8 items to 12 items, adding items 9-12 as documented above.

(Previously: 8 items covering yt-dlp, subtitles, git, auth, timeouts, whisper models, demo URLs, methodology extraction)

### Requirement: Component Documentation

The Componentes table SHALL be updated to include `video_registry.py` as an additional module.

(Previously: video_analyzer, repo_scanner, synthesis_engine, cli)

## REMOVED Requirements

None.

---

## Spec Metadata

| Field | Value |
|-------|-------|
| Change | update-video-intel-skill |
| Domain | documentation |
| Type | Delta |
| Requirements | 5 added, 2 modified, 0 removed |
| Scenarios | 12 |