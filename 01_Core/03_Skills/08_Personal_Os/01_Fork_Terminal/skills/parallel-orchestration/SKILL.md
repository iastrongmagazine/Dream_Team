---
name: parallel-orchestration
description: ALWAYS use when distributing work across multiple agents. Launches visible terminal instances using fork-terminal, displays progress, and generates consolidated reports. Required for complex multi-step tasks.
---

# Parallel Orchestration with Fork-Terminal

## Overview

This skill ALWAYS activates when distributing work across multiple agents. It uses `.claude/skills/fork-terminal/tools/fork_terminal.py` to launch visible CMD terminals for each agent, allowing real-time monitoring and generating comprehensive reports.

**Core Principle:** Visible execution + Consolidated reporting

## When to Use

ALWAYS use this when:

- Validating multiple components simultaneously
- Testing multiple skills or features
- Running distributed verification tasks
- Complex tasks that can be parallelized
- User explicitly requests to "see the instances"

## Skill Priority

**CRITICAL:** Always read from `.claude/skills/` FIRST, then `.agent/skills/` as fallback.

Priority order:

1. `.claude/skills/` (Primary - user's custom skills)
2. `.agent/skills/` (Secondary - standard skills)

## The Pattern

### 1. Identify Independent Tasks

Break work into parallel streams with no shared state:

- Validation tasks (structure, docs, resources)
- Testing tasks (unit, integration, E2E)
- Build tasks (compile, bundle, deploy)
- Analysis tasks (metrics, dependencies, coverage)

### 2. Launch Fork-Terminal Agents

For each independent task:

```bash
python ".claude/skills/fork-terminal/tools/fork_terminal.py" "
  echo === AGENT N: TASK NAME === &&
  cd <working_directory> &&
  <commands> &&
  echo AGENT N COMPLETE &&
  pause
"
```

**Key Elements:**

- `echo === AGENT N: TASK NAME ===` - Clear header
- `cd <working_directory>` - Navigate to workspace
- `<commands>` - Actual work
- `echo AGENT N COMPLETE` - Success marker
- `pause` - Keep terminal open for inspection

### 3. Visual Monitoring

Each agent opens in a **visible CMD window**:

- User can see real-time progress
- Errors are immediately visible
- No hidden background failures
- Easy to debug issues

### 4. Generate Report

After all agents execute, create `MULTI_AGENT_<TASK>_REPORT.md`:

```markdown
# MULTI-AGENT <TASK> REPORT

**Generated:** <timestamp>
**Agents Deployed:** <count>

## Agent Tasks

| Agent   | Task   | Status | Terminal     |
| ------- | ------ | ------ | ------------ |
| Agent 1 | <Task> | ✅     | CMD Window 1 |

...

## Results

[Detailed findings from each agent]

## Summary

[Overall status and metrics]
```

### 5. Display Report

Open final terminal showing the consolidated report:

```bash
python ".claude/skills/fork-terminal/tools/fork_terminal.py" "
  cat <REPORT_FILE> &&
  pause
"
```

## Example: Skills Validation

```bash
# Agent 1: Structure validation
python ".claude/skills/fork-terminal/tools/fork_terminal.py" "
  echo === AGENT 1: SKILL STRUCTURE === &&
  cd .claude/skills &&
  bash validate-skills.sh &&
  pause
"

# Agent 2: Documentation check
python ".claude/skills/fork-terminal/tools/fork_terminal.py" "
  echo === AGENT 2: DOCUMENTATION === &&
  cd .claude/skills &&
  ls -lh *.md &&
  pause
"

# Agent 3: Resources validation
python ".claude/skills/fork-terminal/tools/fork_terminal.py" "
  echo === AGENT 3: RESOURCES === &&
  find .claude/skills -name 'resources' -type d &&
  pause
"

# Final: Generate and show report
# [Create MULTI_AGENT_VALIDATION_REPORT.md]
python ".claude/skills/fork-terminal/tools/fork_terminal.py" "
  cat MULTI_AGENT_VALIDATION_REPORT.md &&
  pause
"
```

## Report Template

Every orchestration MUST end with a report containing:

1. **Header**
   - Timestamp
   - Task type
   - Agent count

2. **Agent Summary Table**
   - Agent number
   - Task assigned
   - Status (✅/❌)
   - Terminal window reference

3. **Detailed Results**
   - Per-agent findings
   - Errors/warnings
   - Metrics collected

4. **Overall Summary**
   - Success rate
   - Quality score
   - Next steps

5. **Execution Log**
   - Launch timestamps
   - Completion times
   - Total duration

## Commands Checklist

For each orchestration session:

- [ ] Identify N independent tasks
- [ ] Launch N fork-terminal agents (visible terminals)
- [ ] Wait for execution (terminals stay open)
- [ ] Collect results from each agent
- [ ] Generate `MULTI_AGENT_<TASK>_REPORT.md`
- [ ] Open final terminal showing report
- [ ] Keep all terminals open for user inspection

## Key Benefits

1. **Visibility** - User sees all agent progress in real-time
2. **Debugging** - Errors visible immediately in their terminal
3. **Parallel** - Tasks execute simultaneously
4. **Documentation** - Comprehensive report generated
5. **Transparency** - No hidden background processes

## Integration with Other Skills

Use this skill in combination with:

- `dispatching-parallel-agents` (for task decomposition logic)
- `verification-before-completion` (before claiming success)
- `systematic-debugging` (if agents encounter issues)

## Red Flags

**Never:**

- Run agents in background without visible terminals
- Skip the final consolidated report
- Close terminals before user reviews them
- Claim success without checking ALL agent outputs

**Always:**

- Use fork-terminal for parallel work
- Keep terminals open for inspection
- Generate comprehensive reports
- Respect `.claude/` priority over `.agent/`

## Priority Directive

**CRITICAL:** When searching for skills or resources:

```
1. Check .claude/skills/<skill-name>/ FIRST
2. If not found, check .agent/skills/<skill-name>/
3. If not found in either, notify user
```

This ensures user customizations in `.claude/` always take precedence.
