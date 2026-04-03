# Video Intel - Video Registry

A registry of analyzed videos for the Video_Intel skill.

## Format

| Date | Video URL | Title | Status | Plan File |
|------|----------|-------|--------|-----------|
| 2026-04-03 | https://www.youtube.com/live/3psHUg6KzOo?si=Y6bZACLup04IfPCF | TEST_VIDEO | pending | - |

## Usage

Add new videos to this registry when analyzing:

```markdown
| YYYY-MM-DD | VIDEO_URL | TITLE | status | plan_file |
```

## Status Options

- `pending` - Video queued for analysis
- `analyzing` - Currently being processed
- `completed` - Analysis complete, plan generated
- `failed` - Analysis failed (check error)

## Notes

- Video registry is maintained in project root
- Analysis plans are saved as `implementation_plan.md` or custom path
