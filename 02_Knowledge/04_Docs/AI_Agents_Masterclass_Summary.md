# AI Agents Masterclass (Remy Gasill Summary)

This document synthesizes key concepts from Remy Gasill's crash course on mastering AI agents for deep productivity.

## 1. Chat vs. Agents
* **Chat Model:** Question → Answer (Ping-pong format). 
* **Agent:** Goal → Result. You give the agent a task, and it repeatedly plans and executes until completion.

## 2. The Agent Loop (Observe → Think → Act)
1. **Observe:** The agent receives a prompt and reads uploaded sources/files (context).
2. **Think:** It reasons about what to do next based on the prompt and its findings.
3. **Act:** It writes code, researches, or calls tools. 
*The loop continues iterating until the agent fulfills the completion parameters set out in the goal.*

## 3. Agent Harnesses (The "Cars")
Agent Harnesses are the applications that facilitate the Agent Loop. Examples: *Claude Code, Cursor (Codeex), Antigravity, OpenClaw, Manis, Co-Work.* Once you understand the core mechanics of agents (steering, pedals), you can "drive" any harness.

An agent fundamentally consists of:
* The LLM (The Brain)
* The Loop (Continuous action)
* Connectors (Tools via MCP)
* Context (Folders/Files)

## 4. Context Engineering over Prompt Engineering
With Chat UIs, users relied heavily on "Mega Prompts." With Agents, the focus shifts to **Context Engineering**.
* You build a root system prompt file (e.g., `agents.md`, `claude.md`, or `gemini.md`) tailored to the specific agent role (Executive Assistant, Media Buyer, Head of Marketing, etc.).
* *Contents:* Role definition, about the business, target audience, tool preferences (e.g., use Notion for PM, Stripe for links), style, and tone.
* With rich context pre-loaded, your prompts become incredibly simple (e.g., "Summarize my inbox and draft email responses").

## 5. The Memory System (`memory.md`)
Agent environments (unlike persistent Chat UIs) start "blank" in each session. To ensure agents learn preferences over time:
* Maintain a `memory.md` file.
* Inject a rule in `agents.md` like: *"Read `memory.md`. When I correct you or you learn something new about my preferences, update the relevant section in `memory.md` so you remember it for future sessions."*
* This creates an automatic compounding effect that reduces errors across weeks and months.

## 6. Model Context Protocol (MCP)
Before MCP, making an LLM speak to an external API (like Slack or Notion) was a massive custom integration task. MCP acts as a universal translator.
* Secures and standardizes how agents talk to tools.
* Unlocks workflows that access live data: Calendar, Gmail, Notion, Stripe, Granola (Meeting Notes).

## 7. Skills (SOPs for AI)
Skills package a recurring manual process into an automated workflow (a Markdown file). *If you explain it once, you never have to explain it again.*
* **How to create:** 
  1. *Feedback loop:* Co-pilot a process manually step-by-step. Once successful, ask the agent to "use your skill creator to package what we just did into a skill file."
  2. *Top-down logic:* Provide a transcript of a specific process/course (e.g., "Viral Hooks") and ask the Agent to turn it into a skill.
* **Examples of Skills:**
  * `daily_brief`: Summarizes calendar, inbox, and sets up your day (Can be scheduled via cron-jobs).
  * `ads_analyst`: Scrapes a Facebook Ads library URL, analyzes copy and landing pages, and compiles a comprehensive Notion report.
  * `network_referral`: A quick skill linking meeting notes to drafting a referral email to a specific contractor with pre-loaded info.
* **Global vs. Project Skills:** Global skills run everywhere (e.g., a "truncate text" skill). Project skills are restricted to specific folders/agents (e.g., `ads_analyst` belongs only to the Marketing folder).
