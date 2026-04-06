# Design: OIM Website SOTA

## Technical Approach

El sitio web usará Next.js 15 App Router con TypeScript y Tailwind CSS 4. El componente Hero usará video HTML5 con autoplay, mientras que ScrollVideoServices usará requestAnimationFrame + Intersection Observer para sincronización frame-by-frame. El diseño seguirá Design_Final.md con tonal layering en lugar de bordes sólidos.

## Architecture Decisions

### Decision: Video Implementation Strategy

**Choice**: Vanilla HTML5 Video API con React hooks
**Alternatives considered**: 
- GSAP ScrollTrigger (heavy dependency, 140KB+)
- WebCodecs API (experimental, soporte limitado)
- CSS Scroll-Timeline (solo Chrome, no Safari)
**Rationale**: Sin dependencias adicionales, control total, mejor compatibilidad cross-browser

### Decision: Scroll Sync Performance

**Choice**: Throttled updates con requestAnimationFrame + Intersection Observer
**Alternatives considered**:
- Direct scroll event listener (causa jank)
- Debounced updates (too slow feedback)
- RAF sin throttle (performance issues)
**Rationale**: 66ms throttle balance entre smoothness y performance, Intersection Observer activa solo cuando es visible

### Decision: Services Display Logic

**Choice**: Progress-based visibility usando Math.floor(progress * categories.length)
**Alternatives considered**:
- Fixed scroll points (less fluid)
- Separate video por categoría (more setup, more video files)
**Rationale**: Smooth transition, single video source, progressive reveal

### Decision: Design Tokens Implementation

**Choice**: Tailwind CSS 4 con @theme extension
**Alternatives considered**:
- CSS Variables + Tailwind (duplication)
- Styled-components (dependency)
- Vanilla CSS modules (no Next.js pattern)
**Rationale**: Next.js + Tailwind standard, @theme clean organization

## File Changes

| File | Action | Description |
|------|--------|-------------|
| `app/layout.tsx` | Create | Root layout con fonts + metadata |
| `app/page.tsx` | Create | Página principal |
| `app/globals.css` | Create | Tailwind + custom tokens |
| `components/HeroSection.tsx` | Create | Video hero con overlay |
| `components/ScrollVideoServices.tsx` | Create | Frame-sync + servicios |
| `components/AboutSection.tsx` | Create | About content |
| `components/ProjectGallery.tsx` | Create | Gallery categorías |
| `components/ContactForm.tsx` | Create | Form 4 campos |
| `components/LanguageSelector.tsx` | Create | ES/EN toggle |
| `lib/design-tokens.ts` | Create | Color/spacing tokens |
| `lib/content.ts` | Create | Contenido OIM static |
| `public/videos/home-exploding.mp4` | Copy | Video asset |
| `public/images/hero-poster.jpg` | Create | Video fallback |

## Interfaces / Contracts

```typescript
// HeroSection props
interface HeroSectionProps {
  videoSrc: string;
  posterSrc?: string;
  children?: React.ReactNode;
}

// ScrollVideoServices props
interface Service {
  title: string;
  items: string[];
}

interface ScrollVideoServicesProps {
  videoSrc: string;
  scrollHeight?: number; // default 300
  services: Service[];
}
```

## Data Flow

```
Page Load
    │
    ▼
HeroSection
    │ autoplay
    ▼
Video plays muted loop
    │
    ▼
User scrolls ──► ScrollVideoServices
    │                    │
    │ getBoundingClientRect()
    │                    ▼
    │            Calculate progress (0-1)
    │                    │
    │                    ▼
    │            video.currentTime = progress * duration
    │                    │
    │                    ▼
    │            Display service based on progress
    │                    │
    ▼                    ▼
Continue to About/Contact/Gallery sections
```

## Testing Strategy

| Layer | What to Test | Approach |
|-------|-------------|----------|
| Unit | Component renders, props passed | Jest + React Testing Library |
| Integration | Scroll sync accuracy | Playwright (scroll + verify frame) |
| E2E | Full flow, mobile responsive | Playwright multi-device |

## Migration / Rollback

**No migration required** - proyecto nuevo greenfield.

**Rollback procedure:**
1. Vercel: promote previous deployment
2. Emergency: cambiar video por imagen estática
3. Emergency: deshabilitar ScrollVideo, usar servicios estáticos

## Open Questions

- [ ] ¿Preferred method para video compression - FFmpeg local o servicio cloud?
- [ ] ¿Generar poster desde el video o crear manualmente?
- [ ] ¿Contenido About section exactamente como en OIM_Website_Content.md?
