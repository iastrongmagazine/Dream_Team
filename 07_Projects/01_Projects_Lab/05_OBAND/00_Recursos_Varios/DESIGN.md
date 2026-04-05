# Design System Specification: Editorial Tech-Forward Light Theme

## 1. Overview & Creative North Star
### The Creative North Star: "The Chromatic Curator"
This design system is built on the philosophy of **"The Chromatic Curator."** It rejects the notion of the "generic SaaS dashboard" in favor of a high-end, editorial experience that feels both human and mathematically precise. 

We achieve this by blending an airy, "white-space-first" layout with high-energy, vibrant chromatic accents. We move away from rigid, boxed-in grids toward a layout that breathes through **intentional asymmetry** and **tonal depth**. The goal is to make every interface feel like a curated gallery piece—clean, professional, and sophisticated, yet pulsing with the energy of its coral and sky-blue gradients.

---

## 2. Colors & Tonal Architecture
The palette is a sophisticated interplay of deep blacks, ethereal whites, and high-vibrancy accents.

### The "No-Line" Rule
**Strict Mandate:** Designers are prohibited from using 1px solid borders to define sections or containers. 
Structure must be achieved through:
- **Background Shifts:** Using `surface-container-low` against a `surface` background.
- **Negative Space:** Leveraging generous padding to imply boundaries.
- **Shadow Anchors:** Using soft, ambient light to lift an element rather than "boxing" it.

### Surface Hierarchy & Nesting
Treat the UI as a physical stack of premium materials. Use the `surface-container` tiers to create depth:
1.  **Base Layer:** `surface` (#f8f9fa) – The canvas.
2.  **Section Layer:** `surface-container-low` (#f3f4f5) – To group related content.
3.  **Elevated Layer:** `surface-container-lowest` (#ffffff) – For interactive cards or primary focal points to create a "pop-out" effect against the slightly darker base.

### The "Glass & Gradient" Rule
To inject "soul" into the tech-forward aesthetic:
- **Signature Gradients:** Primary CTAs and Hero elements should utilize a linear gradient from `primary` (#b3272d) to `primary_container` (#ff5f5e).
- **Glassmorphism:** For floating menus or overlays, use a background of `surface` at 70% opacity with a `24px` backdrop-blur. This ensures the vibrant sky-blue (`secondary`) and coral accents bleed through the interface, keeping it feeling light and integrated.

---

## 3. Typography
The typography system uses a pairing of **Plus Jakarta Sans** (for character and authority) and **Inter** (for high-readability utility).

*   **Display & Headline (Plus Jakarta Sans):** These are your "Editorial" voices. Use `display-lg` (3.5rem) with tight letter-spacing for high-impact hero sections.
*   **Titles & Body (Inter):** These are your "Informational" voices. `title-lg` (1.375rem) provides a clear entry point into content blocks, while `body-md` (0.875rem) ensures long-form content is effortless to scan.
*   **Visual Hierarchy:** Always maintain a high contrast between headlines and body text. If a headline is `on_surface` (#191c1d), ensure the body text utilizes a slightly softer `on_surface_variant` (#5a413f) to create a sophisticated, layered reading experience.

---

## 4. Elevation & Depth
Depth is not an effect; it is information. We use **Tonal Layering** to communicate hierarchy.

### The Layering Principle
Instead of a drop shadow, place a `surface-container-highest` card inside a `surface` layout. The subtle shift from #e1e3e4 to #f8f9fa is enough to signify a new layer to the human eye without visual clutter.

### Ambient Shadows
When an element must float (e.g., a dropdown or a primary modal):
- **Blur:** 32px to 64px.
- **Opacity:** 4% - 6%.
- **Color:** Use a tinted shadow. Instead of pure black, use a semi-transparent `on_surface` (#191c1d) to mimic how light actually behaves in a room.

### The "Ghost Border" Fallback
If an element lacks enough contrast against its background, use a **Ghost Border**:
- **Token:** `outline_variant` (#e1bebc).
- **Opacity:** 15%.
- **Rule:** Never use a 100% opaque border.

---

## 5. Components

### Buttons
- **Primary:** Gradient fill (`primary` to `primary_container`), `on_primary` text, and `xl` (1.5rem) rounded corners.
- **Secondary:** `secondary_container` (#00b3fe) background with `on_secondary_container` (#004260) text.
- **Tertiary:** No background. Use `primary` text with a subtle `primary_fixed` hover state.

### Cards & Lists
- **The Divider Ban:** Do not use horizontal lines. Separate list items using 12px of vertical white space or by alternating background tones between `surface_container_low` and `surface`.
- **Corner Radius:** All cards must use `lg` (1rem) or `xl` (1.5rem) corner radii to maintain the "friendly" brand promise.

### Input Fields
- **Style:** Use the `surface_container_lowest` (#ffffff) as the field background. 
- **States:** On focus, the "Ghost Border" should transition to a 100% opaque `secondary` (#006591) Sky Blue glow (4px spread).

### Chips & Tags
- **Filter Chips:** Use `secondary_fixed` (#c9e6ff) with `on_secondary_fixed` text for a soft, tech-forward pill shape.

---

## 6. Do's and Don'ts

### Do
- **Do** use intentional asymmetry. A large display headline can be left-aligned while the body text is tucked into a narrower column on the right.
- **Do** lean into the "Airy" feel. If you think there is enough white space, add 20% more.
- **Do** use Glassmorphism for mobile navigation bars and top-level web headers.

### Don't
- **Don't** use pure #000000 for text. Use `on_surface` (#191c1d) to keep the "Light" theme's tonal balance.
- **Don't** use standard 4px or 8px corners. This system requires the "Premium" feel of `12px-16px` (`lg` to `xl`) radii.
- **Don't** use sharp, high-contrast shadows. If the shadow is clearly visible as a "shape," it is too heavy.
- **Don't** use more than one gradient-filled element per view. Gradients are for "Moments of Truth" (CTAs, Logo, Hero). Use flat tonal shifts for everything else.