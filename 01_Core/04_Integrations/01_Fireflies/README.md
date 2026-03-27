# Fireflies Integration

Sync your [Fireflies.ai](https://fireflies.ai) meeting notes and transcripts into your Personal OS Knowledge folder.

## What This Does

- **Search meetings** from Fireflies via MCP
- **Sync meeting summaries** to your local `03_Knowledge/Transcripts/` folder
- **Morning planning** includes recent meeting context
- **Goal alignment** analysis against synced meetings

## Prerequisites

1. **Fireflies MCP Server** configured in your system
2. **Python 3.12+** installed

## Available Tools (via Fireflies MCP)

| Tool                      | Description                       |
| ------------------------- | --------------------------------- |
| `search_meetings`         | Search Fireflies meetings         |
| `get_meeting_details`     | Get full meeting metadata         |
| `get_transcript`          | Retrieve the transcript           |
| `check_new_meetings`      | List meetings since last sync     |

## How Syncing Works

1. `check_new_meetings` identifies meetings not yet in `03_Knowledge/Transcripts/`
2. `sync_meeting_to_local` exports selected meetings as markdown
3. Files are saved to `03_Knowledge/Transcripts/YYYY-MM-DD_Meeting_Title.md`
