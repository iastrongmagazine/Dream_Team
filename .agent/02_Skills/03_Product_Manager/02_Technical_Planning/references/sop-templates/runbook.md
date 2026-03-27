# Runbook: [Incident Type]

> **Severity:** [P1/P2/P3] | **Response Time:** [X minutes] | **Escalate To:** [Team]

## Definition of Done

- [ ] Incident resolved
- [ ] Root cause identified
- [ ] Post-mortem scheduled
- [ ] Team notified

## Detection

**Symptoms:**
- [Symptom 1]
- [Symptom 2]

**Alerts:**
- [Alert name/link]

## Immediate Actions

1. **Acknowledge** the alert
2. **Assess** impact (users affected, services down)
3. **Communicate** in #incidents channel

## Investigation

### Step 1: Check Recent Changes
```bash
git log --oneline -10
```

### Step 2: Check Logs
```bash
kubectl logs [pod-name] --tail=100
```

### Step 3: Check Metrics
[Link to dashboard]

## Resolution

### Option A: Rollback
```bash
git revert [commit-hash]
```

### Option B: Hotfix
[Steps]

### Option C: Scale
```bash
kubectl scale deployment [name] --replicas=[n]
```

## Escalation

If not resolved in [X] minutes, escalate to:
- [Team lead]
- [On-call engineer]
