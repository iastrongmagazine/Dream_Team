# Tasks: Sound Automation in OpenCode

## Phase 1: Plugin Rewrite

- [x] 1.1 Rewrite `.opencode/plugins/sound-on-complete.ts` with correct signature: `Plugin = async (ctx) => { ... }` matching notify.ts pattern
- [x] 1.2 Extract `client` from `ctx` parameter to access OpenCode context
- [x] 1.3 Replace node:child_process spawn with Bun.spawn for command execution
- [x] 1.4 Replace Python subprocess with PowerShell `[console]::Beep()` for Windows compatibility

## Phase 2: Hook Implementation

- [x] 2.1 Implement `tool.execute.after` hook to trigger sound on tool completion
- [x] 2.2 Add logging for tool completion to verify hook fires: `console.log("[SOUND] Tool after:", input.tool)`
- [x] 2.3 Implement `event` handler for `session.idle` fallback when session becomes idle
- [x] 2.4 Add logging for session idle events: `console.log("[SOUND] Session idle:", sessionID)`

## Phase 3: Testing

- [ ] 3.1 Load plugin in OpenCode and verify `[SOUND-PLUGIN] Initialized!` log appears
- [ ] 3.2 Run any OpenCode tool and verify `tool.execute.after` fires (check log)
- [ ] 3.3 Verify sound plays after tool completion (hear system beep)
- [ ] 3.4 Test Windows compatibility: confirm PowerShell beep executes without errors

## Phase 4: Verification

- [ ] 4.1 Verify against success criteria: plugin loads, sound plays on tool complete
- [ ] 4.2 Verify session.idle fallback triggers sound when session goes idle
- [ ] 4.3 Clean up any debug logging if needed, keep minimal console.log for debugging
