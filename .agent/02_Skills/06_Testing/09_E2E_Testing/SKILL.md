---
name: e2e-testing-skill
description: > Triggers on: testing, QA, quality, validation.
  End-to-end testing with Playwright. Includes page object models, visual testing, and cross-browser testing.
  Trigger: e2e testing, end-to-end, Playwright, visual testing, cross-browser, browser automation, UI testing.
license: Apache-2.0
metadata:
  author: gentleman-programming
  version: "1.0"
---

# E2E Testing Skill — Playwright & Browser Automation

## When to Use

- Testing full user flows
- Cross-browser compatibility testing
- Visual regression testing
- Performance testing in real browsers
- Accessibility testing
- API testing through browser

## Critical Patterns

### 1. E2E Test Scope

```
┌─────────────────────────────────────────────────────────────────┐
│                    E2E TEST SCOPE                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                    USER BROWSER                          │   │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐                 │   │
│  │  │  Login  │→ │ Dashboard│→ │  Data   │                 │   │
│  │  │  Page   │  │   Page   │  │  Grid   │                 │   │
│  │  └─────────┘  └─────────┘  └─────────┘                 │   │
│  └─────────────────────────────────────────────────────────┘   │
│                              │                                 │
│                    ┌─────────┴─────────┐                      │
│                    │   EXTERNAL APIs │                      │
│                    └─────────┬─────────┘                      │
│                              │                                 │
│                    ┌─────────┴─────────┐                      │
│                    │    DATABASE       │                      │
│                    └───────────────────┘                      │
│                                                                 │
│  E2E Tests: Slow, Brittle, High Confidence                    │
│  Use sparingly for critical paths only                         │
└─────────────────────────────────────────────────────────────────┘
```

### 2. Page Object Model (POM)

```python
from playwright.sync_api import Page, Locator
from dataclasses import dataclass

@dataclass
class LoginPage:
    page: Page
    
    @property
    def email_input(self) -> Locator:
        return self.page.get_by_label("Email")
    
    @property
    def password_input(self) -> Locator:
        return self.page.get_by_label("Password")
    
    @property
    def submit_button(self) -> Locator:
        return self.page.get_by_role("button", name="Sign In")
    
    @property
    def error_message(self) -> Locator:
        return self.page.get_by_role("alert")
    
    def login(self, email: str, password: str) -> "DashboardPage":
        self.email_input.fill(email)
        self.password_input.fill(password)
        self.submit_button.click()
        return DashboardPage(self.page)

@dataclass
class DashboardPage:
    page: Page
    
    @property
    def greeting(self) -> Locator:
        return self.page.get_by_role("heading", name=lambda t: "Welcome")
    
    @property
    def user_menu(self) -> Locator:
        return self.page.get_by_role("button", name="User Menu")
```

### 3. Selector Priority Hierarchy

```python
# BEST (Most reliable)
page.get_by_role("button", name="Submit")          # ARIA role
page.get_by_label("Email")                          # Form label
page.get_by_placeholder("Search...")                # Placeholder
page.get_by_test_id("submit-button")                 # data-testid

# GOOD (Reliable)
page.locator("button:has-text('Submit')")            # Text content
page.locator("form button.primary")                 # CSS class

# AVOID (Fragile)
page.locator("button:nth-child(2)")                 # Position
page.locator("div > span > button")                  # Deep DOM
page.locator("[class*='submit']")                    # Partial class
page.locator("xpath=//button")                       # XPath (only if necessary)
```

## Code Examples

### Playwright Configuration (SOTA)

```python
# playwright.config.py
from playwright.sync_api import sync_playwright
import pytest

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=True,
            args=["--disable-dev-shm-usage"]
        )
        yield browser
        browser.close()

@pytest.fixture(scope="session")
def context(browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        locale="en-US",
        timezone_id="America/New_York",
        permissions=["geolocation"],
        extra_http_headers={
            "Authorization": "Bearer test-token"
        }
    )
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()

# Enable tracing for debugging
@pytest.fixture
def trace_page(page):
    page.context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True
    )
    yield page
    page.context.tracing.stop(
        path="trace.zip"
    )
```

### Visual Testing

```python
from playwright.sync_api import Page, expect
import pytest

def test_visual_regression(page: Page):
    """Compare screenshot against baseline."""
    page.goto("https://example.com/dashboard")
    
    # Wait for animations to complete
    page.wait_for_load_state("networkidle")
    
    # Take full page screenshot
    screenshot = page.screenshot(
        full_page=True,
        animations="disabled"
    )
    
    # Compare with baseline
    assert screenshot == page.screenshot_from_path(
        "tests/visual/baseline/dashboard.png"
    )

def test_component_visual(page: Page):
    """Test individual component visuals."""
    page.goto("https://example.com")
    
    # Test specific component
    component = page.locator(".pricing-card")
    
    expect(component).toHaveScreenshot("pricing-card.png")
```

### Accessibility Testing

```python
def test_accessibility(page: Page):
    """Automated accessibility checks with axe."""
    page.goto("https://example.com/pricing")
    
    # Run axe-core accessibility test
    results = page.run_and_get_axe_results()
    
    # Filter critical violations
    critical = [v for v in results.violations 
                if v.impact in ("critical", "serious")]
    
    assert len(critical) == 0, (
        f"Found {len(critical)} critical accessibility issues: "
        f"{[v.id for v in critical]}"
    )

def test_keyboard_navigation(page: Page):
    """Test keyboard-only navigation."""
    page.goto("https://example.com")
    
    # Tab through interactive elements
    page.keyboard.press("Tab")  # Focus first element
    assert page.evaluate("document.activeElement.tagName") == "BUTTON"
    
    page.keyboard.press("Tab")  # Next element
    assert page.evaluate("document.activeElement.tagName") == "INPUT"
    
    # Test focus trap in modal
    page.locator("[aria-haspopup='dialog']").click()
    modal = page.locator('[role="dialog"]')
    expect(modal).to_be_focused()
```

## Commands

```bash
# Install browsers
playwright install --with-deps chromium

# Run tests
playwright test

# Run with UI
playwright test --ui

# Visual comparison
playwright test --update-snapshots

# Cross-browser testing
playwright test --project=chromium
playwright test --project=firefox
playwright test --project=webkit

# Generate test
playwright codegen https://example.com

# Debug with trace
playwright show-trace trace.zip
```

## Resources

- **Playwright**: https://playwright.dev/
- **Playwright Test**: https://playwright.dev/docs/test-configuration
- **axe-core**: https://github.com/dequelabs/axe-core
- **Visual Regression Tracker**: https://github.com/VisualRegressionTracker/VisualRegressionTracker

## Esencia Original
> **Propósito:** 09_E2E_Testing - propósito del skill
> **Flujo:** Pasos principales del flujo de trabajo

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Error común
  - **Por qué**: Explicación
  - **Solución**: Cómo evitar

## 📁 Progressive Disclosure

> Para información detallada:
- [references/guide.md](references/guide.md) — Guía completa

## 🛠️ Scripts

- [scripts/run.py](scripts/run.py) — Script principal

## 💾 State Persistence

Guardar en:
-  — Evaluaciones
-  — Documentación

