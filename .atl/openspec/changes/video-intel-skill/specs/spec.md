# Video_Intel Skill Specification

## Purpose

Create an AI agent skill that extracts structured knowledge from YouTube videos and GitHub repositories to generate actionable implementation plans verified against the operating system's capabilities.

---

## ADDED Requirements

### Requirement: Video Transcription Pipeline

The skill **MUST** provide a video transcription pipeline that extracts text content from YouTube videos for analysis.

#### Scenario: Successful Video Transcription

- GIVEN a valid YouTube video URL (e.g., https://www.youtube.com/live/3psHUg6KzOo?si=Y6bZACLup04IfPCF)
- WHEN the skill executes the transcription workflow (yt-dlp metadata → whisper transcription → text output)
- THEN the system **MUST** produce a text file containing the full video transcript with timestamps
- AND **MUST** extract video metadata (title, duration, channel, upload date)

#### Scenario: Transcription Failure Handling

- GIVEN a YouTube video that is unavailable, private, or region-locked
- WHEN the transcription pipeline fails
- THEN the skill **MUST** return an error with clear message indicating failure reason
- AND **MUST NOT** create partial transcription files

---

### Requirement: Repository Code Extraction

The skill **MUST** provide repository scanning capability to clone and analyze GitHub repositories.

#### Scenario: Successful Repo Clone

- GIVEN a valid GitHub repository URL
- WHEN the skill executes repository cloning and AST parsing
- THEN the system **MUST** produce a structured code map (file tree, import dependencies, key functions)
- AND **MUST** store cloned repo in temporary directory for analysis

#### Scenario: Invalid or Private Repo

- GIVEN a GitHub URL that is invalid, private, or requires authentication
- WHEN the repo scanning fails
- THEN the skill **MUST** detect authentication requirements and prompt for gh CLI auth
- AND **MUST** provide clear error messages for access failures

---

### Requirement: Methodology Extraction

The skill **MUST** analyze video transcripts to identify and extract methodologies, prompts, and key techniques demonstrated.

#### Scenario: Methodology Identification

- GIVEN a video transcript with clear methodologies or techniques
- WHEN the skill performs NLP analysis on transcript content
- THEN the system **MUST** extract at minimum: methodology name, key steps, code examples shown, tool requirements
- AND **MUST** categorize extracted items as: technique, prompt, demo, or tool reference

#### Scenario: Multiple Methodologies in Video

- GIVEN a video containing multiple distinct methodologies
- WHEN the analysis identifies more than one methodology
- THEN the skill **MUST** create a numbered list of each methodology with separate extraction details
- AND **MUST** identify the sequence/timing where each methodology appears in the video

---

### Requirement: Demo Environment Detection

The skill **MUST** identify and document demo environments, sandbox URLs, or interactive examples shown in video content.

#### Scenario: Demo URL Detection

- GIVEN video transcript containing URLs to demo environments, CodePen, StackBlitz, or similar
- WHEN the skill parses transcript for URL patterns
- THEN the system **MUST** extract each unique demo URL with associated context
- AND **MUST** classify the demo type (sandbox, playground, live demo, documentation)

#### Scenario: No Demo Environments Found

- GIVEN a video with no demo environments or interactive examples
- WHEN the analysis completes
- THEN the skill **MUST** output "No demo environments detected" in the results
- AND **MUST** note this in the implementation plan (no demo verification needed)

---

### Requirement: OS Capability Verification

The skill **MUST** verify detected tools and requirements against the operating system's available capabilities.

#### Scenario: OS Tool Detection

- GIVEN a list of required tools from video analysis (e.g., Node.js, Python, Docker)
- WHEN the skill executes OS verification checks
- THEN the system **MUST** report which tools are available, missing, or need installation
- AND **MUST** provide version information for available tools

#### Scenario: Missing Required Tools

- GIVEN analysis requires tools not available on the OS
- WHEN verification completes
- THEN the skill **MUST** list missing dependencies with installation hints
- AND **MUST** flag these as blockers in the implementation plan

---

### Requirement: Implementation Plan Generation

The skill **MUST** synthesize extracted knowledge into actionable implementation plans.

#### Scenario: Complete Implementation Plan

- GIVEN successful extraction of: transcript, methodologies, repo code, demo URLs, OS verification
- WHEN the synthesis engine processes all data
- THEN the system **MUST** produce a structured implementation plan with: prerequisite steps, core implementation sequence, verification checklist, estimated complexity

#### Scenario: Partial Data Availability

- GIVEN some extraction components fail (e.g., no repo available, transcription incomplete)
- WHEN synthesis attempts to create plan
- THEN the skill **MUST** generate plan with available data
- AND **MUST** clearly indicate which components are missing or incomplete

---

### Requirement: CLI Interface

The skill **MUST** provide a command-line interface for agent workflow integration.

#### Scenario: Basic CLI Execution

- GIVEN the skill is invoked with video URL and optional repo URL
- WHEN the CLI parses arguments and executes pipeline
- THEN the system **MUST** output structured JSON or markdown results
- AND **MUST** support flags for output format (json/markdown), verbose mode, and output file path

#### Scenario: Help and Usage

- GIVEN user invokes skill with `--help` or `-h`
- WHEN the CLI displays usage information
- THEN the skill **MUST** show: required arguments, optional flags, examples, and output format options

---

## MODIFIED Requirements

No existing requirements modified. This is a new skill.

---

## REMOVED Requirements

No existing requirements removed.

---

## Coverage Summary

| Category | Coverage |
|----------|----------|
| Happy Paths | ✅ Video transcription, repo clone, methodology extraction, OS verification, plan generation |
| Edge Cases | ✅ Invalid URLs, private repos, missing tools, partial failures |
| Error States | ✅ API failures, auth requirements, network errors, malformed inputs |
| Testable | ✅ Each scenario has clear Given/When/Then for automated testing |

---

## Next Step

Ready for design (sdd-design). If design already exists, ready for tasks (sdd-tasks).