# Jira MCP Commands

## Create Epic

```json
{
  "project_key": "PROWLER",
  "summary": "[EPIC] Feature name",
  "issue_type": "Epic",
  "additional_fields": {
    "customfield_10359": {"value": "UI"}
  }
}
```

## Update Work Item Description (Wiki Markup)

```json
{
  "customfield_10363": "h2. Feature Overview\n\nOverview text\n\nh2. Requirements\n\n*Section*\n* Item 1\n* Item 2"
}
```

## Create Child Task

```json
{
  "project_key": "PROWLER",
  "summary": "[FEATURE] Task name",
  "issue_type": "Task",
  "additional_fields": {
    "parent": "PROWLER-XXX",
    "customfield_10359": {"value": "UI"}
  }
}
```

## Workflow Transitions

```
Backlog (10037) → To Do (14) → In Progress (11) → Done (21)
                → Blocked (10)
```

## Wiki Markup Cheat Sheet

| Markdown | Jira Wiki |
|----------|-----------|
| `## Header` | `h2. Header` |
| `**bold**` | `*bold*` |
| `- item` | `* item` |
| `- [ ] task` | `* [ ] task` |
