# Audit Criteria Checklist

## Skill Quality Standards

### 1. Description & Triggers

- [ ] Description has semantic triggers (not marketing text)
- [ ] Triggers match user's actual phrases
- [ ] Example GOOD: "weekly planning, weekly review, reflect on progress"
- [ ] Example BAD: "A comprehensive tool for monitoring..."

### 2. Gotchas Section

- [ ] Has Gotchas section
- [ ] Minimum 3 common errors documented
- [ ] Each gotcha has "Por qué" and "Solución"
- [ ] Gotchas are specific to this skill

### 3. Progressive Disclosure

- [ ] SKILL.md < 200 lines
- [ ] Has references/ folder
- [ ] References point to detailed docs
- [ ] Scripts are in scripts/ folder

### 4. YAML Frontmatter

- [ ] Valid YAML frontmatter (---)
- [ ] Has name field
- [ ] Has description field

### 5. Workflow

- [ ] Has "When to Use" section
- [ ] Has clear workflow steps
- [ ] Output format documented

### 6. Scripts

- [ ] Scripts folder exists
- [ ] Scripts are executable
- [ ] Scripts handle errors gracefully

### 7. State Persistence

- [ ] Mentions state persistence
- [ ] Specifies storage location

### 8. Esencia Original

- [ ] Has "Esencia Original" section
- [ ] Documents original workflow/purpose
- [ ] Doesn't deviate from original intent

## Scoring

| Score | Criteria |
|-------|----------|
| 90-100% | Excellent |
| 70-89% | Good |
| 50-69% | Needs Improvement |
| < 50% | Failed |

## Audit Process

1. Run `audit-skills.py`
2. Review PASS/FAIL for each criteria
3. Run `validate-essence.py`
4. Run `fix-missing.py` if needed
5. Re-audit after fixes
