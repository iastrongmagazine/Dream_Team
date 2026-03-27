# Design Rules

## Baseline Configuration
- DESIGN_VARIANCE: 8 (1=Symmetry, 10=Chaos)
- MOTION_INTENSITY: 6 (1=Static, 10=Cinematic)
- VISUAL_DENSITY: 4 (1=Airy, 10=Packed)

## Architecture Rules

### Dependency Verification
NEVER assume library exists. Check package.json first.

### Framework
- React/Next.js with Server Components
- Global state ONLY in Client Components
- Isolate interactive UI as leaf components

### Styling
- Tailwind CSS for 90% of styling
- Check Tailwind version (v3 vs v4)
- Grid over Flex-Math

### Anti-Emoji Policy
NEVER use emojis. Use Radix/Phosphor icons or SVG.

### Responsiveness
- Standard breakpoints (sm, md, lg, xl)
- max-w-[1400px] mx-auto for containment
- min-h-[100dvh] NOT h-screen
- CSS Grid, not flex percentage math

## Typography Rules

### Display/Headlines
- text-4xl md:text-6xl tracking-tighter leading-none
- Use Geist, Outfit, Cabinet Grotesk, Satoshi
- NO Inter for premium, NO serif for tech UI

### Body/Paragraphs
- text-base text-gray-600 leading-relaxed max-w-[65ch]

## Color Rules

### Constraints
- Max 1 Accent Color
- Saturation < 80%
- NO purple/AI aesthetic ("LILA BAN")
- One palette per project
