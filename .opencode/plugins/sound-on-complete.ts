/**
 * sound-on-complete - Sound automation plugin for OpenCode
 * 
 * Plays sound when tools complete or session becomes idle.
 * Uses correct OpenCode plugin signature matching notify.ts pattern.
 */

import type { Plugin } from "@opencode-ai/plugin"
import type { Event } from "@opencode-ai/sdk"

interface ToolInput {
	tool: string
	sessionID: string
	callID: string
}

interface SessionEvent {
	type: string
	properties: Record<string, unknown>
}

/**
 * Play sound using PowerShell on Windows, afplay on macOS
 * Uses Bun.spawn for command execution (like notify.ts)
 */
function playSound(): void {
	const platform = process.platform

	let cmd: string[]

	if (platform === "win32") {
		// Windows: SystemAsterisk via winsound (doble beep ascendente como fallback)
		cmd = [
			"powershell.exe",
			"-NoProfile",
			"-NonInteractive",
			"-Command",
			"try { [System.Media.SystemSounds]::Asterisk.Play() } catch { [Console]::Beep(800,150); [Console]::Beep(1100,200) }",
		]
	} else if (platform === "darwin") {
		// macOS: afplay system beep
		cmd = ["afplay", "/System/Library/Sounds/Glass.aiff"]
	} else {
		// Linux: paplay
		cmd = ["paplay", "/usr/share/sounds/gnome/defaults/alerts/glass.ogg"]
	}

	// Use Bun.spawn — pipe stderr para poder ver errores en logs
	const proc = Bun.spawn(cmd, {
		stdout: "pipe",
		stderr: "pipe",
	})
	proc.unref()
}

export const SoundOnCompletePlugin: Plugin = async (ctx) => {
	const { client } = ctx
	
	console.log("[SOUND-PLUGIN] Initialized!")
	
	// Hook: fires after each tool completes
	const handleToolAfter = async (input: ToolInput) => {
		console.log("[SOUND] Tool after:", input.tool)
		playSound()
	}
	
	// Fallback: fires when session becomes idle
	const handleEvent = async ({ event }: { event: Event }) => {
		const runtimeEvent = event as SessionEvent
		
		if (runtimeEvent.type === "session.idle") {
			const sessionID = runtimeEvent.properties.sessionID
			console.log("[SOUND] Session idle:", sessionID)
			playSound()
		}
	}
	
	return {
		"tool.execute.after": handleToolAfter,
		event: handleEvent,
	}
}

export default SoundOnCompletePlugin
