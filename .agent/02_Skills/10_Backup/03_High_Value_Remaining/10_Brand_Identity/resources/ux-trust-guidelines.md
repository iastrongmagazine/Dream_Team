# UX Trust & Interaction Guidelines

**Role:** Senior Product Designer & UX Engineer
**Goal:** Increase user trust through clarity, feedback, and system reliability.

## core Principle

Trust is built through **clear intention**, **immediate feedback**, and **consistent behavior**.

---

## 1. Interaction Intent

For every interactive element (buttons, links, inputs):

- **Identify User Intent:** The user must know what will happen _before_ they click.
- **Communicate:**
  - **What** will happen.
  - **When** it will happen.
  - **Reversibility:** If usage is destructive, warn beforehand.
- **Avoid Ambiguity:** No surprise actions.

## 2. Feedback & System States

Audit all feedback mechanisms:

- **Loading States:**
  - Acknowledge input **immediately** (e.g., button change state on click, loading spinner).
  - Show progress for delays.
- **Toasts/Notifications:**
  - Concise and informational.
  - Confirm _results_, not just actions.
- **Error States:**
  - Explain **what** went wrong.
  - Explain **how to fix it**.
  - **Never blame the user.**

## 3. Speed, Consistency, Reliability

- **Interactions must feel:** Fast, Predictable, Consistent.
- **Avoid:** Delayed responses without feedback, inconsistent behavior for similar actions.

## 4. The "Trust Test"

After any interaction, the user should feel:

1. "The system understood me."
2. "The system responded clearly."
3. "I can trust this to behave the same way next time."

---

## Key Implementation Checklist

- [ ] **Clear Intent:** Do buttons/links clearly say what they do?
- [ ] **Immediate Feedback:** Do elements react specifically on Hover, Focus, and Active (Click) states?
- [ ] **Accessibility:** Are focus rings visible? (users feel "understood" when keyboard nav works).
- [ ] **Safety:** Are destructive actions protected?
- [ ] **Consistency:** Do similar buttons look and behave exactly the same?
