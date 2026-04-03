# Tasks: Video_Intel Skill Implementation

## Phase 1: Foundation / Infrastructure

- [x] 1.1 Create `.agent/03_Skills/00_Video_Intel/` directory structure
- [x] 1.2 Create `.agent/03_Skills/00_Video_Intel/__init__.py` with package metadata
- [x] 1.3 Set up requirements.txt with dependencies: yt-dlp, whisper, click, astor

## Phase 2: Video Analyzer Module

- [x] 2.1 Create `video_analyzer.py` with `VideoAnalyzer` class
- [x] 2.2 Implement `download_metadata()` using yt-dlp
- [x] 2.3 Implement `transcribe()` using whisper (decide model: base vs medium)
- [x] 2.4 Implement `extract_transcript()` from downloaded subs
- [x] 2.5 Add error handling for unavailable/private/region-locked videos

## Phase 3: Repository Scanner Module

- [x] 3.1 Create `repo_scanner.py` with `RepoScanner` class
- [x] 3.2 Implement `clone_repo()` using git to temp directory
- [x] 3.3 Implement `parse_ast()` to extract imports, functions, classes
- [x] 3.4 Implement `generate_code_map()` returning JSON structure
- [x] 3.5 Add error handling for invalid/private repos and auth requirements

## Phase 4: Synthesis Engine Module

- [x] 4.1 Create `synthesis_engine.py` with `SynthesisEngine` class
- [x] 4.2 Implement `extract_methodologies()` using NLP patterns
- [x] 4.3 Implement `extract_demo_urls()` with URL regex patterns
- [x] 4.4 Implement `verify_os_capabilities()` checking tool availability
- [x] 4.5 Implement `generate_implementation_plan()` combining all data
- [x] 4.6 Add graceful degradation for partial data scenarios

## Phase 5: CLI Interface

- [x] 5.1 Create `cli.py` with Click framework
- [x] 5.2 Implement `analyze` command with video_url argument
- [x] 5.3 Add `--repo`, `--output`, `--format`, `--verbose` options
- [x] 5.4 Implement JSON and markdown output formats
- [x] 5.5 Add `--help` flag with usage documentation

## Phase 6: SKILL.md Definition

- [x] 6.1 Create `SKILL.md` with trigger patterns
- [x] 6.2 Document: "analyze video", "extract from youtube", "implementation plan from video"
- [x] 6.3 Add skill metadata: description, triggers, examples

## Phase 7: Integration Testing

- [ ] 7.1 Run full pipeline with test video URL https://www.youtube.com/live/3psHUg6KzOo?si=Y6bZACLup04IfPCF
- [ ] 7.2 Verify transcript extraction produces text file with timestamps
- [ ] 7.3 Verify metadata extraction (title, duration, channel)
- [ ] 7.4 Test methodology extraction from transcript
- [ ] 7.5 Test OS verification reports available tools correctly
- [ ] 7.6 Verify implementation plan generation with clear steps
