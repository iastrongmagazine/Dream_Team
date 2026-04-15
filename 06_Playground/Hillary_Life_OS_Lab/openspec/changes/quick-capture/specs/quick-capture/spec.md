# Quick Capture Skill Specification

## Purpose

The Quick Capture skill provides frictionless task and idea capture for the Hillary Life OS system. It receives free-form input (text or dictation) and persists it as a markdown file with YAML frontmatter in the inbox directory, enabling rapid thought capture without interrupting workflow.

## Requirements

### Requirement: Skill Execution

The Quick Capture skill MUST accept free-form text input from the user and transform it into a persisted markdown capture.

The skill SHALL extract the following metadata automatically:

- **timestamp**: ISO 8601 formatted creation time
- **source**: origin of the capture (text, voice, shortcut)
- **tags**: optional array of user-provided or auto-detected tags

The skill MUST generate a unique filename based on timestamp and a slugified version of the content.

### Requirement: Input Processing

The skill SHALL parse input to detect the following patterns:

- Tags embedded in brackets (e.g., `[trabajo]`, `[personal, reunion]`)
- Insight markers (e.g., "insight:", "idea:", "nota:")
- Content that appears to be an action item (verbs in infinitive)

The skill SHOULD NOT require any specific input format — free text MUST be accepted.

### Requirement: Output Format

The skill MUST write markdown files with valid YAML frontmatter.

The output file path MUST follow the pattern: `inbox/YYYY-MM-DD-HHmm-{slug}.md`

The frontmatter MUST include:

```yaml
---
created: 2026-03-31T12:00:00Z
source: text
tags: []
---
```

The body section MUST contain the original input content verbatim.

### Requirement: Source Detection

The skill MUST default to `source: text` when input comes directly from user message.

The skill SHOULD support `source: voice` when invoked via voice input.

The skill SHOULD support `source: shortcut` when invoked via keyboard shortcut.

### Requirement: Insight Classification

When the input contains no actionable task (no verb indicating action), the skill MUST set `type: insight` in the frontmatter.

When the input contains an actionable task, the skill MUST set `type: task` in the frontmatter.

## Scenarios

### Scenario: Simple Task Capture

- GIVEN the user sends "comprar leche"
- WHEN the Quick Capture skill processes the input
- THEN the system MUST create file `inbox/2026-03-31-1200-comprar-leche.md`
- AND the frontmatter MUST include `created: {timestamp}`, `source: text`, `tags: []`, `type: task`
- AND the body MUST contain "comprar leche"

### Scenario: Task with Tags

- GIVEN the user sends "reunión con cliente 3pm [trabajo, reunion]"
- WHEN the Quick Capture skill processes the input
- THEN the system MUST extract tags `["trabajo", "reunion"]` from the input
- AND the frontmatter MUST include those tags in the tags array
- AND the body MUST contain "reunión con cliente 3pm" (without tags)

### Scenario: Insight Capture

- GIVEN the user sends "idea: el sol sale por el este"
- WHEN the Quick Capture skill processes the input
- THEN the frontmatter MUST include `type: insight`
- AND the filename slug MUST reflect "idea-el-sol-sale-por-el-este"

### Scenario: Voice Input Source

- GIVEN the user invokes Quick Capture via voice command
- WHEN the skill receives the transcribed input
- THEN the frontmatter MUST include `source: voice`
- AND the processing follows the same rules as text input

### Scenario: Duplicate Timestamp Protection

- GIVEN two captures occur within the same minute
- WHEN the second capture attempts to use the same filename pattern
- THEN the system MUST append a random suffix to ensure uniqueness
- AND the filename pattern becomes `YYYY-MM-DD-HHmmss-{slug}.md`

### Scenario: Invalid YAML Characters

- GIVEN the user input contains colons or special YAML characters
- WHEN the skill writes the frontmatter
- THEN the body content MUST remain unchanged (verbatim)
- AND the frontmatter values MUST be properly quoted if needed

## Out of Scope

The following are explicitly NOT in scope for this specification:

- Automatic categorization or prioritization of tasks
- Integration with external APIs or services
- GUI interface — this skill operates via CLI/agent only
- Due dates or scheduling functionality
- Task completion tracking

## Success Criteria

- [ ] Skill accepts free-form text input
- [ ] Output files are created in inbox/ directory
- [ ] Filename follows YYYY-MM-DD-HHmm-{slug}.md pattern
- [ ] Frontmatter contains created, source, tags, type fields
- [ ] Tags are extracted when provided in [tag] format
- [ ] Insight type is set when input contains no action verb
- [ ] Voice and shortcut sources are supported
