# Delta for UI/Hero Video

## ADDED Requirements

### Requirement: Hero Video Background

The hero section MUST display a full-viewport video background that plays automatically when the page loads.

- GIVEN the user navigates to the homepage
- WHEN the page loads
- THEN the video MUST autoplay, muted, and loop infinitely
- AND the video MUST play inline on mobile (playsInline attribute)

- GIVEN the user is on a mobile device with autoplay restrictions
- WHEN the video cannot autoplay
- THEN the system MUST display a poster image as fallback

- GIVEN the video is playing
- WHEN the user scrolls down
- THEN the video MUST continue playing behind the content

### Requirement: Hero Content Overlay

The hero section MUST display text content with sufficient contrast against the video background.

- GIVEN a video playing in the hero background
- WHEN content is displayed
- THEN there MUST be an overlay with minimum bg-black/50 opacity
- AND text MUST have minimum WCAG 2.1 AA contrast ratio (4.5:1)

- GIVEN the hero content is displayed
- THEN it MUST include:
  - Headline: "Professional Office Furniture Installation in Atlanta"
  - Subheadline: "Since 2018, providing reliable, high-quality furniture assembly and relocation services..."
  - CTA Button: "Get a Free Quote"

### Requirement: Trust Indicators

The hero MUST display trust indicators below the CTA.

- GIVEN the hero is rendered
- THEN the following indicators MUST be visible:
  - ✓ 8+ Years Experience
  - ✓ Bilingual Service (English & Español)
  - ✓ Licensed & Insured
  - ✓ Serving Atlanta & Surrounding Areas

---

## ADDED Requirements - Scroll Video

### Requirement: Frame-by-Frame Scroll Sync

The scroll video section MUST synchronize video playback position with scroll position.

- GIVEN the user begins scrolling down the page
- WHEN the scroll video section enters the viewport
- THEN the video currentTime MUST update proportionally to scroll progress

- GIVEN the scroll position changes
- WHEN the user scrolls up or down
- THEN the video MUST seek to the corresponding frame (advance or rewind)

- GIVEN the user scrolls quickly
- THEN the video updates MUST be throttled to prevent performance issues (minimum 66ms between updates)

### Requirement: Progressive Services Display

The scroll section MUST display 4 service categories progressively based on scroll position.

- GIVEN scroll progress is at 0%
- WHEN the section is visible
- THEN the first service category MUST be displayed: "Office Furniture Installation"

- GIVEN scroll progress is between 0-25%
- THEN the first category MUST be visible

- GIVEN scroll progress is between 25-50%
- THEN the second category MUST be displayed: "Office Setup & Reconfiguration"

- GIVEN scroll progress is between 50-75%
- THEN the third category MUST be displayed: "Disassembly & Moving"

- GIVEN scroll progress is between 75-100%
- THEN the fourth category MUST be displayed: "Commercial Projects"

### Requirement: Services Content

Each service category MUST display its title and list items.

- GIVEN a service category is active
- THEN the title MUST be displayed (e.g., "Office Furniture Installation")
- AND all items in that category MUST be listed

Service categories:
1. Office Furniture Installation: Desks & workstations, Cubicles, Conference tables, Chairs & storage units
2. Office Setup & Reconfiguration: New office setups, Workspace redesign, Furniture rearrangement
3. Disassembly & Moving: Safe disassembly, Relocation, Reinstallation
4. Commercial Projects: Small & large offices, Corporate environments, Fast turnaround projects

---

## ADDED Requirements - Design System

### Requirement: No-Line Rule

The UI MUST NOT use solid 1px borders to define sections or containers.

- GIVEN a component is rendered
- THEN it MUST NOT have border: 1px solid
- AND structure MUST be achieved through background shifts or spacing

### Requirement: Glassmorphism

Floating elements (headers, overlays) MUST use glassmorphism effect.

- GIVEN a floating header or overlay is rendered
- THEN it MUST use backdrop-blur with minimum 24px blur
- AND background MUST be surface color at 70% opacity

### Requirement: Corner Radius

Cards and interactive elements MUST use large corner radii.

- GIVEN a card or button is rendered
- THEN it MUST use border-radius of lg (1rem) or xl (1.5rem)
- AND MUST NOT use standard 4px or 8px corners