/**
 * sound-on-complete - MINIMAL VERSION
 * Solo reproduce sonido, sin dependencies complejas
 */

import { spawn } from "node:child_process"
import type { Plugin } from "@opencode-ai/plugin"

// Force immediate sound test
function playSound(): void {
	// Test sound directly
	try {
		const py = spawn("python", ["-c", "import winsound; [winsound.Beep(440, 100) for _ in range(3)]"], {
			detached: true,
			stdio: "ignore",
		})
		py.unref()
		console.log("[SOUND] Beep triggered!")
	} catch(e) {
		console.log("[SOUND] Error:", e)
	}
}

export const SoundOnCompletePlugin: Plugin = async () => {
	console.log("[SOUND-PLUGIN] Initialized!")
	
	return {
		"tool.execute.before": async (input) => {
			console.log("[SOUND] Tool before:", input.tool)
		},
		
		"tool.execute.after": async (input) => {
			console.log("[SOUND] Tool after:", input.tool)
			playSound()
		},
		
		event: async ({ event }) => {
			const e = event as { type: string }
			if (e.type === "session.idle" || e.type === "session.status") {
				console.log("[SOUND] Session event:", e.type)
				playSound()
			}
		}
	}
}

export default SoundOnCompletePlugin