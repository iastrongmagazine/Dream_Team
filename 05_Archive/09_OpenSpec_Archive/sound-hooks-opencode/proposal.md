# Proposal: Sound Automation in OpenCode

## Intent

Fix sound automation so OpenCode plays sounds when tools complete. Current plugin exists but doesn't work due to incorrect plugin format and missing context.

## Scope

### In Scope
- Fix plugin structure to match OpenCode's expected format
- Verify hooks `tool.execute.before/after` work for sound triggering
- Test `session.idle` event as fallback
- Ensure Windows-compatible sound playback

### Out of Scope
- Multiple sound variations
- Sound customization UI
- Integration with other notification systems

## Approach

**Recommended: Option A - Fix Plugin Format + Test Hooks**

1. Rewrite plugin to use correct OpenCode signature with context params
2. Use context-provided `$` for command execution instead of raw `spawn`
3. Test `tool.execute.after` hook first (most reliable)
4. Fallback to `session.idle` if tool hooks don't fire

**Alternative Approaches:**

| Option | Description | Pros | Cons |
|--------|-------------|------|------|
| A | Fix plugin format + test tool hooks | Native approach, no extra deps | May not fire on every tool |
| B | Use session.idle event only | Reliable session events | Only fires on session idle, not per-tool |
| C | Custom tool wrapper (call sound after each tool) | Full control | Requires user to call wrapper tool |
| D | Polling approach (check active tools) | Works always | Inefficient, complex |

## Affected Areas

| Area | Impact | Description |
|------|--------|-------------|
| `.opencode/plugins/sound-on-complete.ts` | Modified | Rewrite with correct OpenCode format |
| `.opencode/opencode.jsonc` | No Change | Already configured correctly |

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|-------------|
| Tool hooks don't fire in all scenarios | Medium | Test with session.idle fallback |
| Windows sound not playing | Low | Test multiple approaches (powershell, python) |
| Context params undefined | Medium | Add logging to verify context received |

## Rollback Plan

1. Revert `.opencode/plugins/sound-on-complete.ts` to backup
2. Remove plugin entry from `.opencode/opencode.jsonc`
3. OpenCode will restart without plugin

## Dependencies

- None (all native OpenCode hooks)

## Success Criteria

- [ ] Plugin loads (see "[SOUND-PLUGIN] Initialized!" log)
- [ ] Sound plays when a tool completes (via tool.execute.after hook)
- [ ] OR Sound plays when session becomes idle (via session.idle event)
- [ ] Works on Windows platform
