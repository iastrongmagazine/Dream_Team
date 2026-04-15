# Quick Capture Skill — Technical Design

> "Simple is better. No ceremony, no complexity. Just capture and move on." — Anti-system philosophy

## Overview

The Quick Capture skill transforms free-form user input into persistent markdown files with YAML frontmatter. It extracts metadata automatically (timestamp, tags, type), generates unique filenames, and writes to the inbox directory. Zero external dependencies — pure file operation.

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      Quick Capture Skill                    │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Input: "reunión con cliente 3pm [trabajo, reunion]"      │
│                           │                                  │
│                           ▼                                  │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐   │
│  │   PARSE     │───▶│  PROCESS    │───▶│    SAVE     │   │
│  │             │    │             │    │             │   │
│  │ - extract   │    │ - detect    │    │ - generate  │   │
│  │   tags      │    │   type      │    │   filename  │   │
│  │ - clean     │    │ - slugify   │    │ - write .md  │   │
│  │   content   │    │ - validate  │    │             │   │
│  └─────────────┘    └─────────────┘    └─────────────┘   │
│                           │                                  │
│                           ▼                                  │
│         inbox/2026-03-31-1430-reunion-con-cliente.md        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### Components

| Component   | Responsibility                                   | Public API                                 |
|-------------|--------------------------------------------------|--------------------------------------------|
| `Parser`    | Extract tags, clean content, detect markers      | `parse(input): {content, tags, markers}`   |
| `Processor` | Detect type (task/insight), slugify, validate    | `process(parsed): {slug, type, validated}` |
| `Saver`     | Generate filename, write file, handle collisions | `save(processed, content): filePath`       |

---

## Key Decisions

### 1. Filename Generation

**Pattern**: `inbox/YYYY-MM-DD-HHmm-{slug}.md`

**Slugification rules**:
- Lowercase only
- Replace spaces with hyphens
- Remove special characters (keep alphanumeric and hyphens)
- Truncate to 50 characters max
- If slug is empty after cleaning, use "captura" as fallback

**Collision handling**:
- If filename exists, append random 4-char suffix: `inbox/2026-03-31-1430-captura-a1b2.md`

```typescript
function generateFilename(input: string, timestamp: Date): string {
  const slug = slugify(extractTitle(input), { maxLength: 50 });
  const date = format(timestamp, 'yyyy-MM-dd-HHmm');
  const base = slug || 'captura';
  return `inbox/${date}-${base}.md`;
}
```

### 2. Tag Parsing

**Format**: `[tag1, tag2, tag3]` anywhere in input

**Rules**:
- Extract all bracketed content
- Split by comma
- Trim whitespace from each tag
- Lowercase all tags
- Remove duplicates
- If no tags found, empty array `[]`

```typescript
function extractTags(input: string): string[] {
  const bracketRegex = /\[([^\]]+)\]/g;
  const matches = [...input.matchAll(bracketRegex)];
  const tags = matches.flatMap(m => m[1].split(','));
  return [...new Set(tags.map(t => t.trim().toLowerCase()))];
}
```

**Examples**:
- `"comprar leche [compras]"` → `["compras"]`
- `"reunión [trabajo, reunion]"` → `["trabajo", "reunion"]`
- `"nota sin tags"` → `[]`

### 3. Insight vs Task Detection

**Detection strategy**:
1. Check for explicit markers first
2. Fall back to verb analysis

**Explicit markers** (case-insensitive):
- `insight:` → type: insight
- `idea:` → type: insight
- `nota:` → type: insight
- `recordar:` → type: task
- `hacer:` → type: task
- `comprar:` → type: task

**Verb detection fallback** (if no marker):
- If input starts with common action verbs → type: task
- Common action verbs: `comprar`, `hacer`, `llamar`, `enviar`, `revisar`, `crear`, `actualizar`, `agendar`, `recordar`, `terminar`

**Edge case**: If no marker and no action verb detected → type: insight

```typescript
function detectType(input: string): 'task' | 'insight' {
  const lower = input.toLowerCase();
  
  // Check explicit markers
  if (lower.startsWith('insight:') || lower.startsWith('idea:') || lower.startsWith('nota:')) {
    return 'insight';
  }
  if (lower.startsWith('recordar:') || lower.startsWith('hacer:') || lower.startsWith('comprar:')) {
    return 'task';
  }
  
  // Fallback: action verbs
  const actionVerbs = ['comprar', 'hacer', 'llamar', 'enviar', 'revisar', 'crear', 'actualizar', 'agendar', 'recordar', 'terminar'];
  const firstWord = lower.split(' ')[0];
  if (actionVerbs.includes(firstWord)) {
    return 'task';
  }
  
  // Default to insight
  return 'insight';
}
```

### 4. Frontmatter Default Values

```yaml
---
created: 2026-03-31T14:30:00Z
source: text
type: task
tags: []
---
```

| Field     | Default                    | Source                                |
|-----------|----------------------------|---------------------------------------|
| `created` | Current ISO 8601 timestamp | System time at execution              |
| `source`  | `text`                     | Input channel (text, voice, shortcut) |
| `type`    | `task`                     | Detected from content analysis        |
| `tags`    | `[]`                       | Extracted from `[tag]` patterns       |

**Note**: `source` can be overridden by invoking context (voice input sets `source: voice`, keyboard shortcut sets `source: shortcut`). Default is `text` when invoked directly.

---

## File Structure

```
01_Quick_Capture/
├── SKILL.md              # This file — skill definition & execution
├── inbox/                # Captured items directory (created on first run)
└── examples/
    └── sample_capture.md # Example output for reference
```

### inbox/ directory

- Created automatically on first capture
- Contains only `.md` files
- Files named by timestamp + slug
- No subdirectories (flat structure)

---

## Output Format

```markdown
---
created: 2026-03-31T14:30:00Z
source: text
type: task
tags: ["trabajo", "reunion"]
---

# Reunión con cliente 3pm

reunión con cliente 3pm
```

**Formatting rules**:
1. Title extracted from first line, used for slug
2. Body contains original content (with tags removed from visible text)
3. Blank line between frontmatter and body
4. No additional markdown formatting applied to body (verbatim)

---

## Implementation Notes

### No External Dependencies

Pure file system operations only:
- Read/write files
- Generate timestamps
- Parse strings

### Error Handling

| Scenario                | Behavior                       |
|-------------------------|--------------------------------|
| Inbox directory missing | Create it automatically        |
| Write permission denied | Error message, no file created |
| Invalid YAML in body    | Wrap in code block or escape   |
| Empty input             | Error: "Captura vacía"         |

### Logging

Minimal logging — only errors. No success messages (anti-system philosophy).

---

## Related Artifacts

- **Proposal**: `.atl/openspec/changes/quick-capture/proposal.md`
- **Spec**: `.atl/openspec/changes/quick-capture/specs/quick-capture/spec.md`

---

## Changelog

| Date       | Change         | Author   |
|------------|----------------|----------|
| 2026-03-31 | Initial design | Hillary  |
