# Design Archetypes

## Vibe & Texture (Pick 1)

### 1. Ethereal Glass (SaaS / AI / Tech)
- Deepest OLED black (#050505)
- Radial mesh gradients (purple/emerald orbs)
- Vantablack cards with backdrop-blur-2xl
- White/10 hairlines
- Wide geometric Grotesk typography

### 2. Editorial Luxury (Lifestyle / Real Estate)
- Warm creams (#FDFBF7), muted sage, espresso
- High-contrast Variable Serif for headings
- CSS noise/film-grain overlay (opacity-0.03)
- Physical paper feel

### 3. Soft Structuralism (Consumer / Health)
- Silver-grey or white backgrounds
- Massive bold Grotesk typography
- Airy, floating components
- Soft, diffused ambient shadows

## Layouts (Pick 1)

### 1. Asymmetrical Bento
- Masonry-like CSS Grid
- Varying card sizes (col-span-8 row-span-2)
- Mobile: single column stack

### 2. Z-Axis Cascade
- Physical cards stacked
- Varying depths of field
- Subtle rotation (-2deg, 3deg)
- Mobile: remove rotations, stack vertically

### 3. Editorial Split
- Massive typography left (w-1/2)
- Interactive cards right
- Mobile: full-width vertical stack

## Mobile Override
- Below 768px: w-full, px-4, py-8
- min-h-[100dvh] NOT h-screen
