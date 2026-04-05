# OIM Website Redesign Plan

## Phase 1: Analysis (before any code)

### Current State Review
- Tech: Next.js 16 + React 19 + Tailwind CSS 4 + Framer Motion
- Colors: #0A0A0A (background), #F97316 (accent), #FFFFFF (foreground), #A3A3A3 (muted)
- Fonts: Poppins (headings), DM Sans (body)
- Sections: Navbar, Hero, Services, Stats, Projects, About, Contact, CTA, Footer

### Visual Thesis
**"Industrial luxury meets editorial minimalism"**
- Dark background with warm orange accent (not overused)
- Typography-forward design (big, bold headlines with generous whitespace)
- Photography as hero content - real office spaces, not stock
- Motion that feels architectural, not decorative

### Content Plan
1. **Hero** - Brand statement + one strong visual
2. **Services** - 4 columns, minimal, icon + title only
3. **Stats** - 4 numbers, horizontal, subtle
4. **Projects** - 3-6 images, masonry or asymmetric grid, no text overload
5. **About** - Split: story left, values right
6. **Contact** - Left: info, Right: form (minimal fields)
7. **CTA** - One line + button

### Interaction Plan
1. **Entrance**: Staggered fade-up on hero (Framer Motion spring)
2. **Scroll**: Subtle parallax on project images
3. **Hover**: Scale + brightness on project cards
4. **Navigation**: Smooth scroll, active state indicator

---

## Phase 2: Implementation (iterate per section)

### Priority Order
1. **Hero** - Most important first impression
2. **Projects** - Visual proof of work
3. **Services** - What they do
4. **About** - Trust building
5. **Contact** - Conversion
6. **Stats, CTA, Footer** - Supporting

### Rules for Each Section
- **NO**: borders, cards, excessive shadows, gradients
- **YES**: whitespace, typography hierarchy, photography, subtle motion
- Keep the orange accent - but use it sparingly (buttons, links only)

### Quality Checklist
- [ ] Mobile-first (test at 375px)
- [ ] Framer Motion spring (no linear/ease defaults)
- [ ] Semantic HTML (nav, main, section)
- [ ] WCAG contrast on text
- [ ] Images optimized

---

## Phase 3: Verification

### Before declaring done
1. Take screenshot of each section
2. Review against visual thesis
3. Check mobile view
4. Verify all links work
5. Run tests: `npm run test:run`

---

## References
- Design inspiration: Apple, Stripe, Notion, Linear
- Tailwind CSS 4 theme already configured
- Framer Motion already in use