# Design: Sound Automation in OpenCode

## Technical Approach

Fix the broken sound-on-complete plugin by rewriting it to match OpenCode's plugin signature pattern (as demonstrated in `notify.ts`). The key changes involve:

1. **Correct plugin signature**: Accept `ctx` parameter with client object
2. **Proper command execution**: Use `Bun.spawn` instead of raw `node:child_process/spawn`
3. **Test hooks systematically**: Verify `tool.execute.after` fires, fallback to `session.idle`
4. **Windows-compatible**: Use PowerShell for sound (more reliable than Python on Windows)

## Architecture Decisions

### Decision: Plugin Signature Format

**Choice**: Follow `notify.ts` pattern - `Plugin = async (ctx) => { ... }`
**Alternatives considered**: Use different signature or function form
**Rationale**: The existing `notify.ts` plugin loads successfully, proving this pattern works with OpenCode. The broken `sound-on-complete.ts` uses incorrect empty param signature `async ()`.

### Decision: Command Execution Method

**Choice**: Use `Bun.spawn` (as used in notify.ts), not raw `spawn` from node:child_process
**Alternatives considered**: 
- Raw `node:child_process/spawn` (current - BROKEN)
- PowerShell `Start-Process` approach
- Direct `[console]::Beep()` call
**Rationale**: Bun.spawn is already used in the codebase (notify.ts line 128) and is the runtime available inside OpenCode plugins. Node's child_process may not be properly initialized in the plugin context.

### Decision: Hook Priority

**Choice**: Test `tool.execute.after` first, fall back to `session.idle` event
**Alternatives considered**: Use only `session.idle`, use `tool.execute.before`
**Rationale**: The proposal's Option A is most appropriate - `tool.execute.after` fires per-tool completion (ideal for feedback), while `session.idle` only fires when session becomes idle (less granular but more reliable).

### Decision: Windows Sound Implementation

**Choice**: PowerShell `[console]::Beep()` - single command, no Python dependency
**Alternatives considered**:
- Python with winsound (current, requires python installed)
- External .wav file playback (requires file path)
- PowerShell `Beep` cmdlet
**Rationale**: PowerShell is guaranteed to exist on Windows. Single command is simpler than Python subprocess. The Beep frequency/duration can be tuned.

## Data Flow

```
OpenCode Runtime
       │
       ▼
┌──────────────────┐
│ Plugin (ctx)     │──► Access: client, config
│                  │
│ Return hooks:    │
│ - tool.execute   │
│ - event          │
└──────────────────┘
       │
       ▼ (hook fires)
┌──────────────────┐
│ playSound()     │──► Bun.spawn(["powershell", "-Command", "..."])
└──────────────────┘
       │
       ▼
┌──────────────────┐
│ Windows plays    │
│ system beep      │
└──────────────────┘
```

## File Changes

| File | Action | Description |
|------|--------|-------------|
| `.opencode/plugins/sound-on-complete.ts` | Modify | Rewrite with correct signature + Bun.spawn + PowerShell beep |

## Interfaces / Contracts

```typescript
import type { Plugin } from "@opencode-ai/plugin"

// Correct plugin signature - accepts ctx parameter
export const SoundOnCompletePlugin: Plugin = async (ctx) => {
  const { client } = ctx  // Destructure client from context
  
  console.log("[SOUND-PLUGIN] Initialized!")
  
  // Hook: fires after each tool completes
  // Input shape: { tool: string, sessionID: string, callID: string }
  const handleToolAfter = async (input: { tool: string; sessionID: string; callID: string }) => {
    console.log("[SOUND] Tool completed:", input.tool)
    playSound()
  }
  
  // Fallback: fires when session becomes idle
  const handleEvent = async ({ event }: { event: { type: string; properties: Record<string, unknown> } }) => {
    if (event.type === "session.idle") {
      console.log("[SOUND] Session idle")
      playSound()
    }
  }
  
  return {
    "tool.execute.after": handleToolAfter,
    event: handleEvent,
  }
}

// Sound playback using Bun.spawn + PowerShell
function playSound(): void {
  // PowerShell [console]::Beep(440, 200) - 440Hz for 200ms
  const proc = Bun.spawn(["powershell", "-Command", "[console]::Beep(440, 200)"], {
    stdout: "ignore",
    stderr: "ignore",
  })
  proc.unref()
}
```

## Testing Strategy

| Layer | What to Test | Approach |
|-------|-------------|----------|
| Manual | Plugin loads | Look for `[SOUND-PLUGIN] Initialized!` in OpenCode log |
| Manual | tool.execute.after fires | Run any OpenCode tool, check log for `[SOUND] Tool after:` |
| Manual | Sound plays | Hear system beep after tool completes |
| Manual | session.idle fallback | Wait for session to go idle, verify sound plays |
| Manual | Windows compatibility | Confirm sound plays on Windows 10/11 |

## Migration / Rollout

No migration required. This is a single-file plugin change.

## Open Questions

- [ ] Does OpenCode provide `ctx.$` (backtick template) for command execution? The notify.ts doesn't use it - need to verify if it's available
- [ ] Is `Bun.spawn` available in all OpenCode runtime contexts, or only in certain modes?
- [ ] What sound frequency/duration feels "complete" - currently using 440Hz/200ms (1/4 second beep)