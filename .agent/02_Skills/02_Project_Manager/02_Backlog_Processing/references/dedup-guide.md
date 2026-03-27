# Backlog Deduplication Guide

## Why Deduplication Matters

Duplicate tasks waste time, create confusion, and dilute focus. Every task should exist exactly once.

## How to Deduplicate

### Step 1: Check Existing Tasks

Before creating a new task, search `02_Operations/01_Active_Tasks/` for:

1. **Similar titles** - Check if the new task already exists
2. **Same goal** - Multiple tasks pointing to the same objective
3. **Sub-task** - Whether the new item is a sub-task of an existing one

### Step 2: Calculate Similarity

| Similarity | Action |
|------------|--------|
| >80% | Merge as sub-task |
| 50-80% | Add reference to existing task |
| <50% | Create as new task |

### Step 3: Mark Duplicates

If duplicate found:
- Add `duplicate_of: filename.md` in metadata
- Link from new item to existing task
- Suggest merging to user

## Common Duplicate Patterns

1. **Same task, different wording**
   - "Follow up with James" vs "Message James about API"
   
2. **Parent task and sub-task**
   - "Build login" vs "Create login form UI"

3. **Research vs Action**
   - "Research AI search" vs "Add AI to search feature"

---

*Part of Backlog Processing Skill - Progressive Disclosure*
