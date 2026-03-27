---
name: claude-blog-researcher
description: Research Claude AI announcements and updates from official blog
---

# Claude Blog Researcher

Use this skill to research Claude AI announcements from https://claude.com/blog/category/announcements

## Steps

1. **Fetch announcements page**: Use webfetch to get `https://claude.com/blog/category/announcements`
2. **Identify posts**: Extract all post titles, dates, and URLs from the page
3. **Fetch key posts**: Use webfetch on individual posts for detailed content
4. **Extract information**:
   - Title
   - Date
   - Summary
   - Key features/announcements
   - Impact on PersonalOS
5. **Generate document**: Create structured markdown with timeline and features

## Output Location

Save to: `03_Knowledge/01_Research_Knowledge/Claude_AI_Announcements_2026.md`

## Document Structure

```markdown
# Claude AI - Super Context Document

## Overview
[Resumen de announcements]

## Timeline de Releases
| Fecha | Announcement | Impacto |
|-------|-------------|---------|
| YYYY-MM | [título] | [descripción] |

## Features Anunciadas
### 2026
- [Feature]: [descripción]

## Integración con PersonalOS
[Cómo usar estas features]

## Links
[Todos los links a posts]
```

## Tips

- Fetch 5-10 most recent posts for detailed content
- Prioritize Claude Code, Agents, and Platform announcements
- Note pricing and availability for each feature
