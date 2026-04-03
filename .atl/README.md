# .atl/ — SDD Registry

Directorio de artefactos del sistema SDD (Spec-Driven Development).

## Contenido

| Archivo/Carpeta | Proposito |
|-----------------|-----------|
| skill-registry.md | Registro de skills del proyecto (referencia rapida) |
| openspec/ | Artefactos SDD activos e historicos |
| openspec/config.yaml | Configuracion global de SDD para este proyecto |
| openspec/changes/ | Cambios SDD por nombre de change |

## Changes Activos

| Change | Estado | Descripcion |
|--------|--------|-------------|
| sound-hooks-opencode | proposal | Fix hooks de sonido para OpenCode (pendiente spec) |

## Fuentes de Verdad

- Skills: 01_Core/03_Skills/
- Registry principal: 02_Knowledge/04_Docs/99_ATL/skill-registry.md
- Reglas: 01_Core/01_Rules/

## Uso

# Proposal: Fix Sound Hooks for OpenCode in Think Different OS

## Intent

Make sound play after each task/tool completion in OpenCode. User uses OpenCode (not Claude Code), but hooks are configured in Claude Code format in `.claude/settings.local.json`. The current config uses Claude Code's hook format with `PostToolUse` events, which OpenCode does not support.

## Scope

### In Scope
- Identify correct configuration method for OpenCode hooks OR implement alternative solution
- Ensure sound plays on tool completion in OpenCode environment
- Maintain compatibility with existing PowerShell sound script

### Out of Scope
- Modifying the sound script itself (already works when run manually)
- Supporting other AI editors (Cursor, Windsurf)
- Adding new sound events beyond tool completion

## Approach

Three options identified for resolving OpenCode hook incompatibility:

### Option A: OpenCode Native Hooks (PREFERRED)
Find OpenCode's native hook configuration and convert the current hooks.

**Pros:**
- Native integration, no extra overhead
- Follows OpenCode's intended design

**Cons:**
- OpenCode's hook support is limited/experimental
- May require research on correct format and location

### Option B: Python Wrapper Integration
Integrate sound call directly into Python scripts that run in hooks (e.g., `post_tool_use.py`).

**Pros:**
- Works reliably across both Claude Code and OpenCode
- Centralizes all post-tool logic in one place

**Cons:**
- Requires modifying existing Python hook scripts
- Adds dependency on sound script within Python logic

### Option C: OpenCode Plugin for Sound
Create a custom OpenCode plugin that triggers sound on tool completion.

**Pros:**
- Official OpenCode extension mechanism
- Full control over behavior

**Cons:**
- More complex to implement and maintain
- Requires TypeScript/JS development

## Affected Areas

| Area | Impact | Description |
|------|--------|-------------|
| `.claude/settings.local.json` | Modified | Hook config (Claude Code format - won't work in OpenCode) |
| `.agent/04_Extensions/hooks/04_Sound/task-complete-sound.ps1` | Existing | Working sound script (tested manually) |
| `.agent/04_Extensions/hooks/02_Post_Tool/post_tool_use.py` | Modified | Add sound call to Python hook |
| `01_Core/05_Mcp/opencode.json` | Modified | Add hook configuration if OpenCode supports it |

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| OpenCode lacks hook support | Medium | Fall back to Option B (Python wrapper) |
| Sound doesn't play in background | Low | Use async/non-blocking call in Python |
| Conflicting hooks between editors | Low | Use conditional detection of environment |

## Rollback Plan

1. Revert changes to `post_tool_use.py` 
2. Restore original `.claude/settings.local.json` if modified
3. Remove any OpenCode plugin additions if Option C was attempted

## Dependencies

- Verify OpenCode hook support via documentation
- Confirm Python 3 is available in OpenCode execution environment

## Success Criteria

- [ ] Sound plays after tool execution completes in OpenCode
- [ ] Works without manual intervention after each tool use
- [ ] No performance degradation in tool execution time
- [ ] Manual test of sound script still works independently

*PersonalOS v6.1 — Actualizado: 2026-04-03*
