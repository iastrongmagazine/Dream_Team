# SPEC.md — Jesús Obando CV Web Portfolio

> **Proyecto:** Dos versiones web del CV profesional de Jesús Alfonso Obando
> **Versión:** 2.0
> **Fecha:** 2026-03-23
> **Stack SOTA:** Next.js 15 + React 19 + Tailwind CSS v4 + Motion + shadcn/ui + TypeScript 5.5

---

## 1. Concept & Vision

### Propósito
Crear un portfolio web profesional que presente a Jesús Alfonso Obando como candidato de alto nivel para roles en AI/ML, Data Engineering y Backend Development en empresas FAANG y startups de Silicon Valley.

### Producto Final
Dos versiones web complementarias:
1. **FelixStyle Portfolio** — Minimalista premium con interacciones elegantes
2. **SOTA CV Web** — ATS-optimizado, profesional, listo para aplicar

### Personalidad de Marca
- **Profesional pero memorable** — No es un CV genérico
- **Tecnología + Industria** — Une Oil & Gas con AI/ML
- **Premium pero accesible** — Diseño de Silicon Valley sin ser pretencioso
- **Confianza + Innovación** — Muestra expertise real con impacto medible

---

## 2. Design Language (Taste Skills)

### FelixStyle — Premium Creative (taste-skill)
```
DESIGN_VARIANCE: 8    (Asymmetric/Artsy)
MOTION_INTENSITY: 6   (Fluid CSS + Framer Motion)
VISUAL_DENSITY: 4    (Daily App Mode)
```

**Aesthetic**: Bento 2.0 Paradigm, Liquid Glass, Magnetic Buttons, Perpetual Micro-Interactions
- Bento Grid asymmetric layouts
- Split Screen Hero sections
- Glassmorphism con inner refraction
- Spring Physics animations (stiffness: 100, damping: 20)
- Premium fonts: Geist, Satoshi, Cabinet Grotesk

### SOTA CV — Editorial Minimalism (minimalist-skill)
```
Style: Premium Utilitarian Minimalism & Editorial
Palette: Warm Monochrome + Spot Pastels
```

**Aesthetic**: Notion/Linear meets editorial
- Typography: Geist Sans + Editorial Serif (Playfair/Lyon)
- Borders: 1px solid #EAEAEA
- Motion: Ultra-subtle (600ms fade, staggered reveals)
- Accents: Muted pastels only
- Icons: Phosphor Icons (Bold weight)

### Color Palettes

#### FelixStyle
```css
/* Light Mode - Premium */
--bg: #FAFAFA
--card: #FFFFFF
--text: #0A0A0A
--text-muted: #71717A
--accent: #2563EB (Electric Blue)
--accent-glow: rgba(37, 99, 235, 0.15)

/* Dark Mode */
--bg-dark: #09090B
--card-dark: #18181B
--text-dark: #FAFAFA
--accent-dark: #3B82F6
```

#### SOTA CV
```css
/* Monochrome Base */
--canvas: #FFFFFF
--bone: #F7F6F3
--border: #EAEAEA
--charcoal: #111111
--muted: #787774

/* Spot Pastels */
--pastel-red: #FDEBEC
--pastel-blue: #E1F3FE
--pastel-green: #EDF3EC
--pastel-yellow: #FBF3DB
```

### Color Palette

```css
/* Light Mode */
--bg-primary: #f8f9fa
--bg-card: rgba(255, 255, 255, 0.95)
--text-primary: #1a1a1a
--text-secondary: #4a4a4a
--accent-blue: #0066ff
--accent-glow: rgba(0, 102, 255, 0.3)
--border: #e0e0e0

/* Dark Mode */
--bg-primary-dark: #0a0a0a
--bg-card-dark: rgba(26, 26, 26, 0.95)
--text-primary-dark: #e0e0e0
--text-secondary-dark: #999999
--accent-blue-dark: #4d94ff
--accent-glow-dark: rgba(77, 148, 255, 0.4)
--border-dark: #2a2a2a

/* Accent Colors (Company Links) */
--adplist: #4169e1
--packdat: #ff6b35
--gotrade: #2a9d8f
--passpod: #666666
```

### Typography

```css
/* System Fonts (no loading) */
font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text",
             "Helvetica Neue", Helvetica, Arial, sans-serif;

/* Headers */
font-weight: 600-700
font-size: 2.5rem (h1), 1.5rem (h2), 1.25rem (h3)

/* Body */
font-weight: 400
font-size: 1rem (16px)
line-height: 1.8
```

### Spatial System

```css
--space-xs: 4px
--space-sm: 8px
--space-md: 16px
--space-lg: 24px
--space-xl: 32px
--space-2xl: 48px
--space-3xl: 64px

/* Card */
border-radius: 24px
padding: 60px 40px
max-width: 900px

/* Responsive breakpoints */
--mobile: 768px
--tablet: 1024px
--desktop: 1280px
```

### Motion Philosophy

| Element          | Animation            | Duration   | Easing                       |
|------------------|----------------------|------------|------------------------------|
| Page transitions | Fade out/in          | 180ms      | ease-out                     |
| Theme toggle     | Slide + color change | 400ms      | cubic-bezier(0.4, 0, 0.2, 1) |
| Hover effects    | Scale + glow         | 300ms      | ease                         |
| Scroll progress  | Width %              | 100ms      | linear                       |
| Card entrance    | Fade + translateY    | 500ms      | ease-out                     |

### Visual Assets
- **Icons:** Lucide React (consistent, minimal)
- **Photos:** headshot.png (80x80, rounded corners)
- **Backgrounds:** Solid colors + gradients (no heavy images)
- **Decorative:** Subtle shadows, glassmorphism blur

---

## 3. Layout & Structure

### Site Architecture

```
jesus-obando-cv/
├── app/
│   ├── layout.tsx              # Root layout con providers
│   ├── page.tsx                # Landing (selector de versiones)
│   ├── felix/
│   │   └── page.tsx            # Versión FelixStyle
│   └── sota/
│       └── page.tsx            # Versión SOTA ATS
├── components/
│   ├── ThemeToggle.tsx
│   ├── ScrollProgress.tsx
│   ├── GlassCard.tsx
│   ├── Section.tsx
│   └── Footer.tsx
├── lib/
│   ├── data.ts                 # Data del CV
│   └── utils.ts                 # Helpers
├── styles/
│   └── globals.css              # Tailwind + custom CSS
└── public/
    ├── headshot.jpg
    ├── og-image.png
    └── favicon.svg
```

### Page Structures

#### Landing Page (Selector)
```
┌─────────────────────────────────────────┐
│  [Logo]                     [Theme]    │
├─────────────────────────────────────────┤
│                                         │
│         JESÚS ALFONSO OBANDO            │
│         Portfolio Web                   │
│                                         │
│    ┌─────────────────────────────┐     │
│    │   🎨 FelixStyle Portfolio  │     │
│    │   Minimalista Premium      │     │
│    └─────────────────────────────┘     │
│                                         │
│    ┌─────────────────────────────┐     │
│    │   📄 SOTA CV Web           │     │
│    │   ATS-Optimized            │     │
│    └─────────────────────────────┘     │
│                                         │
└─────────────────────────────────────────┘
```

#### FelixStyle Page
```
┌─────────────────────────────────────────┐
│  [scroll progress bar - 3px top]        │
├─────────────────────────────────────────┤
│                                         │
│  ┌───────────────────────────────────┐  │
│  │  [photo]              [controls]  │  │
│  │                                   │  │
│  │  JESÚS ALFONSO OBANDO            │  │
│  │  AI Engineer · Oil & Gas         │  │
│  │                                   │  │
│  │  At the intersection of           │  │
│  │  industrial expertise and          │  │
│  │  digital innovation.               │  │
│  │                                   │  │
│  │  ─────────────────────────────     │  │
│  │                                   │  │
│  │  WORK                             │  │
│  │  [Experience cards with links]    │  │
│  │                                   │  │
│  │  SKILLS                           │  │
│  │  [Categorized skills grid]        │  │
│  │                                   │  │
│  │  PROJECTS                         │  │
│  │  [Project cards]                  │  │
│  │                                   │  │
│  │  EDUCATION                        │  │
│  │  [Education + Certifications]      │  │
│  │                                   │  │
│  │  ─────────────────────────────     │  │
│  │  [Contact info + Social links]    │  │
│  └───────────────────────────────────┘  │
│                                         │
└─────────────────────────────────────────┘
```

#### SOTA CV Page
```
┌─────────────────────────────────────────┐
│  [scroll progress bar - 3px top]        │
├─────────────────────────────────────────┤
│                                         │
│  ┌───────────────────────────────────┐  │
│  │  Header: Name + Title + Contact   │  │
│  │  ─────────────────────────────     │  │
│  │                                   │  │
│  │  PROFESSIONAL SUMMARY             │  │
│  │  [3-4 lines impact statement]     │  │
│  │                                   │  │
│  │  EXPERIENCE                       │  │
│  │  [Reverse chronological]          │  │
│  │  - Company + Dates                │  │
│  │  - Metrics-driven bullets         │  │
│  │                                   │  │
│  │  TECHNICAL SKILLS                 │  │
│  │  [By category]                   │  │
│  │                                   │  │
│  │  EDUCATION                        │  │
│  │  [Degrees + Institutions]        │  │
│  │                                   │  │
│  │  CERTIFICATIONS                   │  │
│  │  [Organized by category]         │  │
│  │                                   │  │
│  │  PROJECTS                         │  │
│  │  [AI projects with tech stack]    │  │
│  │                                   │  │
│  │  ─────────────────────────────     │  │
│  │  [Download PDF] [LinkedIn]        │  │
│  └───────────────────────────────────┘  │
│                                         │
└─────────────────────────────────────────┘
```

---

## 4. Features & Interactions

### Core Features

#### Theme Toggle
- **Ubicación:** Corner superior derecho
- **Comportamiento:** Toggle entre light/dark mode
- **Persistencia:** localStorage + system preference
- **Animación:** Slide con sol/luna (CSS puro)

#### Scroll Progress Indicator
- **Ubicación:** Top de la página, fixed
- **Comportamiento:** Barra que crece con scroll
- **Estilo:** Gradiente azul (#0066ff → #00ccff), 3px height

#### Glass Card Container
- **Ubicación:** Contenedor principal
- **Estilo:** background rgba(255,255,255,0.95), backdrop-filter blur(10px)
- **Sombra:** 0 8px 32px rgba(0,0,0,0.1)
- **Border radius:** 24px

#### Hover Effects
- **Links:** text-shadow glow effect
- **Icons:** scale(1.15) + translateY(-2px)
- **Cards:** subtle scale + shadow

#### Experience Cards (FelixStyle)
- **Links a empresas:** Colores distintivos por empresa
- **Icons:** Pequeños iconos SVG junto a nombres
- **Hover:** Glow effect sutil

### Interactions

| Element      | Action      | Result                         |
|--------------|-------------|--------------------------------|
| Theme toggle | Click       | Theme cambia + animación slide |
| Scroll       | Scroll down | Progress bar crece             |
| Link         | Hover       | Glow + underline shimmer       |
| Icon         | Hover       | Scale + lift                   |
| Button       | Hover       | Background change              |
| Card         | Hover       | Shadow intensifies             |

### Edge Cases
- **No JS:** Contenido visible, sin animaciones
- **Print:** Layout optimizado para PDF
- **Reduced motion:** Respetar prefers-reduced-motion
- **Mobile:** Touch-friendly targets (min 44px)

---

## 5. Component Inventory

### ThemeToggle
```
States: light | dark
Style: Custom toggle switch 70x34px
Animation: Slide + icon change (400ms)
Icons: Sun/Moon (CSS)
```

### ScrollProgress
```
Position: fixed top-0 left-0
Height: 3px
Color: linear-gradient(90deg, #0066ff, #00ccff)
Width: dynamic (0-100%)
```

### GlassCard
```
Background: rgba(255,255,255,0.95)
Backdrop-filter: blur(10px)
Border-radius: 24px
Padding: 60px 40px (desktop), 40px 24px (mobile)
Shadow: 0 8px 32px rgba(0,0,0,0.1)
```

### ExperienceCard
```
Layout: Company icon + name + role + dates + bullets
Links: Colored by company
Hover: Glow effect
```

### SkillBadge
```
Style: Pill/tag
Background: --accent-blue con opacity
Border-radius: full
Padding: 4px 12px
```

### CertificationCard
```
Layout: Icon + name + issuer + year
Category: Grouped by type
```

### ProjectCard
```
Layout: Name + description + tech stack
Link: GitHub/demo optional
```

### Footer
```
Content: Contact info + social links
Style: Minimal, border-top
Links: Icon + text
```

---

## 6b. Tailwind CSS v4 Configuration

```css
/* styles/globals.css */
@import "tailwindcss";

@theme {
  /* Colors - Brand palette */
  --color-background: oklch(0.98 0.01 250);
  --color-foreground: oklch(0.15 0.03 250);
  --color-primary: oklch(0.55 0.25 250);
  --color-primary-foreground: oklch(0.98 0.01 250);
  --color-secondary: oklch(0.96 0.02 200);
  --color-muted: oklch(0.92 0.01 250);
  --color-accent: oklch(0.65 0.20 180);

  /* Dark mode colors */
  --color-background-dark: oklch(0.12 0.02 250);
  --color-foreground-dark: oklch(0.92 0.01 250);

  /* Company colors */
  --color-adplist: #4169e1;
  --color-packdat: #ff6b35;
  --color-gotrade: #2a9d8f;
  --color-passpod: #666666;

  /* Typography */
  --font-sans: 'Inter', system-ui, -apple-system, sans-serif;
  --font-mono: 'JetBrains Mono', monospace;

  /* Spacing */
  --spacing-card: 3.5rem;

  /* Radius */
  --radius-lg: 1.5rem;
  --radius-md: 1rem;
  --radius-sm: 0.5rem;
}

/* Base styles */
@layer base {
  * {
    border-color: oklch(0.9 0.01 250);
  }

  html {
    scroll-behavior: smooth;
  }

  body {
    background-color: var(--color-background);
    color: var(--color-foreground);
    font-family: var(--font-sans);
    line-height: 1.8;
  }
}

/* Glass card effect */
@layer components {
  .glass-card {
    background: oklch(100% 0 0 / 0.95);
    backdrop-filter: blur(12px);
    border-radius: var(--radius-lg);
    box-shadow: 0 8px 32px oklch(0 0 0 / 0.1);
  }

  .dark .glass-card {
    background: oklch(0.15 0.02 250 / 0.95);
  }
}

/* Scroll progress bar */
.scroll-progress {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  background: linear-gradient(90deg, #0066ff, #00ccff);
  z-index: 50;
  transition: width 100ms linear;
}

/* Theme toggle animation */
.theme-toggle {
  transition: transform 400ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

## 6c. React 19 & Next.js 15 Patterns

### Typed Routes (Next.js 15.5+)
```tsx
// app/felx/page.tsx - Typed route
import Link from 'next/link'

// Type safety automático
<Link href="/felix">FelixStyle</Link>
<Link href="/sota">SOTA</Link>
```

### Motion Animations
```tsx
import { motion } from 'motion'
import { useAutoAnimate } from '@formkit/auto-animate'

// Page entrance
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.5, ease: 'easeOut' }}
>

// List animations
const [parent] = useAutoAnimate()
<div ref={parent}>
  {items.map(item => <Item key={item.id} />)}
</div>
```

### Dark Mode (next-themes)
```tsx
// app/layout.tsx
import { ThemeProvider } from 'next-themes'

export default function RootLayout({ children }) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body>
        <ThemeProvider attribute="class" defaultTheme="system">
          {children}
        </ThemeProvider>
      </body>
    </html>
  )
}
```

---

## 6. Technical Approach

### Framework & Tools (Stack SOTA 2026)

| Component     | Choice               | Reason                                            |
|---------------|----------------------|---------------------------------------------------|
| Framework     | Next.js 15           | App Router, Turbopack (10x faster), typed routes  |
| Language      | TypeScript 5.5       | Inferred type predicates, satisfies, const params |
| Styling       | Tailwind CSS v4      | Oxide engine (7x faster), CSS-first config        |
| Animation     | Motion + AutoAnimate | Motion: gestures, transitions; AutoAnimate: lists |
| UI Components | shadcn/ui            | Radix primitives, owned code, no dependencies     |
| Theme         | next-themes          | Dark/light con CSS variables                      |
| Icons         | Lucide React         | Consistent, tree-shakeable                        |
| Deploy        | Vercel               | Zero config, Edge, CDN                            |

### Architecture (SOTA 2026)

```
app/
├── layout.tsx          # Root layout con providers (theme, fonts)
├── page.tsx            # Landing selector
├── felix/
│   └── page.tsx        # FelixStyle version
└── sota/
    └── page.tsx        # SOTA ATS version

components/
├── ui/                 # shadcn/ui components (copied, owned)
│   ├── button.tsx
│   ├── card.tsx
│   ├── badge.tsx
│   ├── separator.tsx
│   ├── scroll-area.tsx
│   └── mode-toggle.tsx
├── sections/           # Custom sections
│   ├── Header.tsx      # Photo + intro
│   ├── Experience.tsx  # Company cards con colores
│   ├── Skills.tsx      # Pills por categoría
│   ├── Projects.tsx    # Project cards
│   ├── Education.tsx   # Degrees + certs
│   └── Footer.tsx      # Contact + links
└── index.ts

lib/
├── data.ts             # CV data (single source of truth)
└── utils.ts           # cn() helper, formatters

styles/
└── globals.css         # Tailwind v4 @theme config
```

### Data Model

```typescript
interface Person {
  name: string
  title: string
  email: string
  phone: string
  location: string
  linkedin: string
  github?: string
}

interface Experience {
  company: string
  role: string
  period: string
  bullets: string[]
  metrics?: { label: string; value: string }[]
}

interface Skill {
  category: string
  items: string[]
}

interface Certification {
  name: string
  issuer: string
  year: number
  category: 'ai' | 'industrial' | 'pm' | 'hse'
}

interface Project {
  name: string
  description: string
  techStack: string[]
  status: 'production' | 'concept'
}

interface CVData {
  person: Person
  summary: string
  experience: Experience[]
  education: { degree: string; institution: string; year: string }[]
  skills: Skill[]
  certifications: Certification[]
  projects: Project[]
  languages: { language: string; level: string }[]
}
```

### SEO & Meta

```typescript
// metadata per page
export const metadata = {
  title: 'Jesús Obando | AI Engineer & Petroleum Specialist',
  description: 'AI/ML Engineer with 17+ years combining Oil & Gas expertise with digital transformation. Targeting FAANG and top tech companies.',
  openGraph: {
    title: 'Jesús Obando Portfolio',
    description: 'AI Engineer | Petroleum Engineering | Project Manager',
    images: ['/og-image.png']
  }
}
```

### Performance Targets

| Metric      | Target   |
|-------------|----------|
| LCP         | < 2.5s   |
| FID         | < 100ms  |
| CLS         | < 0.1    |
| Bundle size | < 100kb  |
| Lighthouse  | > 90     |

---

## 7. Content — Jesús Obando Data

### Personal Info
```typescript
const person = {
  name: 'Jesús Alfonso Obando Ramones',
  title: 'AI/ML Engineer & Petroleum Engineering Specialist',
  email: 'esjesusobando@outlook.com',
  phone: '+58 0422 425 4131',
  location: 'Venezuela (Remote-friendly)',
  linkedin: 'linkedin.com/in/jesús-o-532697329',
  github: 'github.com/jesusobando'
}
```

### Summary
```
Hybrid AI/ML Engineer and Petroleum Engineering Specialist with 17+ years
combining industrial operations with digital transformation. Expert in
LLM orchestration, RAG pipelines, and AI agent architecture. Led
initiatives achieving 95% reduction in analysis time and 30%
productivity gains.
```

### Experience
```typescript
const experience = [
  {
    company: 'Independent',
    role: 'AI Workflow Architect & Developer',
    period: '2024 – Present',
    bullets: [
      'Designed Universal_Doc_Reader_Elite + Batch_Doc_Processor_Elite with LLM integrations',
      'Achieved 95% reduction in manual document analysis time (66+ docs)',
      'Built PersonalOS Ecosystem with 11+ specialized AI skills'
    ]
  },
  {
    company: 'Tech Industry',
    role: 'Project Manager & Digital Strategist',
    period: '2019 – 2024',
    bullets: [
      'Led digital transformation for 5 years',
      '30% increase in team delivery speed with AI tools',
      'GTM strategy and growth marketing'
    ]
  },
  {
    company: 'PDVSA',
    role: 'Well Planner / Directional Design Engineer',
    period: '2016 – 2019',
    bullets: [
      'Optimized ROP by 15% through BHA selection',
      'Saved $200k+ NPV per well',
      'Coordinated with Halliburton'
    ]
  },
  {
    company: 'PDVSA',
    role: 'Operations Engineer',
    period: '2011 – 2016',
    bullets: [
      '0 LTI (Lost Time Injury) record',
      '12% NPT reduction ($150k/year savings)'
    ]
  },
  {
    company: 'Saman',
    role: 'Drilling Fluids Engineer',
    period: '2008 – 2011',
    bullets: [
      '20% torque/drag reduction',
      'API compliance'
    ]
  }
]
```

### Skills
```typescript
const skills = [
  { category: 'AI & Data', items: ['Python', 'SQL', 'LLM Orchestration', 'RAG', 'LangChain', 'Claude Code', 'Prompt Engineering'] },
  { category: 'Cloud', items: ['AWS', 'Docker', 'CI/CD', 'REST APIs', 'FastAPI'] },
  { category: 'Oil & Gas', items: ['Well Planning', 'Directional Design', 'BHA Selection', 'HSE', 'IADC WellCAP'] },
  { category: 'PM', items: ['Agile', 'Scrum', 'Business Analysis', 'GTM'] }
]
```

### Certifications
```typescript
const certifications = [
  { name: 'IADC WellCAP', issuer: 'IADC', year: 2014, category: 'industrial' },
  { name: 'AI Day - IA Generativa', issuer: 'Webpositer', year: 2025, category: 'ai' },
  { name: 'Big School AI', issuer: 'Big School', year: 2025, category: 'ai' },
  { name: 'Google Data Analytics', issuer: 'Coursera', year: 2022, category: 'ai' },
  { name: 'Python Fundamentals', issuer: 'Platzi', year: 2024, category: 'ai' },
  { name: 'Project Manager & Business Analyst', issuer: 'Domestika', year: 2024, category: 'pm' }
]
```

### Projects
```typescript
const projects = [
  {
    name: 'PersonalOS Ecosystem',
    description: 'AI-powered productivity system with modular agents',
    techStack: ['Python', 'LangChain', 'Chroma', 'Claude API', 'FastAPI'],
    status: 'production'
  },
  {
    name: 'OilBrain Pro',
    description: 'ML model for drilling optimization',
    techStack: ['Python', 'scikit-learn', 'Pandas'],
    status: 'concept'
  },
  {
    name: 'DrillQuery',
    description: 'RAG-powered NLP interface for technical docs',
    techStack: ['Python', 'LangChain', 'Vector DB'],
    status: 'concept'
  }
]
```

---

## 8. Version Differences

### FelixStyle vs SOTA

| Aspect   | FelixStyle             | SOTA                |
|----------|------------------------|---------------------|
| Purpose  | Impression/branding    | Application/ATS     |
| Design   | Visual, creative       | Professional, clean |
| Content  | Narrative/storytelling | Metrics/direct      |
| Format   | Multi-section          | Classic CV          |
| Keywords | Embedded               | Prominent           |
| CTA      | Social links           | Download PDF        |
| Length   | 1-2 pages              | 1 page              |

### When to Use Each

| Situation         | Use        |
|-------------------|------------|
| Networking        | FelixStyle |
| Applying to jobs  | SOTA       |
| LinkedIn bio link | Either     |
| Recruiter meeting | FelixStyle |
| ATS submission    | SOTA       |

---

## 9. Implementation Phases

### Phase 1: Setup & Shared Components
- [ ] Next.js 15 project setup
- [ ] Tailwind CSS v4 configuration
- [ ] Theme system (light/dark)
- [ ] ThemeToggle component
- [ ] ScrollProgress component
- [ ] GlassCard component
- [ ] CV data file (lib/data.ts)

### Phase 2: FelixStyle Version
- [ ] Layout structure
- [ ] Header with photo
- [ ] Experience section with company colors
- [ ] Skills section (categorized pills)
- [ ] Projects section
- [ ] Education & Certifications
- [ ] Footer with contact

### Phase 3: SOTA Version
- [ ] Layout structure
- [ ] Header (classic CV style)
- [ ] Professional Summary
- [ ] Experience (reverse chronological)
- [ ] Technical Skills (organized)
- [ ] Education
- [ ] Certifications (by category)
- [ ] Projects
- [ ] Download PDF button

### Phase 4: Polish
- [ ] Animations (Framer Motion)
- [ ] Hover effects
- [ ] Mobile responsive
- [ ] Print styles
- [ ] SEO metadata
- [ ] OG images

### Phase 5: Deploy
- [ ] Vercel deployment
- [ ] Custom domain (optional)
- [ ] Analytics setup

---

## 10. File Structure (Final - Inside Focus_Now_Lab)

```
Focus_Now_Lab/
├── Portfolio/                    # ← NUEVO PROYECTO
│   ├── app/
│   │   ├── layout.tsx
│   │   ├── page.tsx            # Landing selector
│   │   ├── felix/
│   │   │   └── page.tsx       # FelixStyle version
│   │   └── sota/
│   │       └── page.tsx       # SOTA ATS version
│   ├── components/
│   │   ├── ui/                 # shadcn components
│   │   │   ├── button.tsx
│   │   │   ├── card.tsx
│   │   │   ├── badge.tsx
│   │   │   ├── separator.tsx
│   │   │   ├── scroll-area.tsx
│   │   │   └── mode-toggle.tsx
│   │   └── sections/
│   │       ├── Header.tsx
│   │       ├── Experience.tsx
│   │       ├── Skills.tsx
│   │       ├── Projects.tsx
│   │       ├── Education.tsx
│   │       └── Footer.tsx
│   ├── lib/
│   │   ├── data.ts             # CV data
│   │   └── utils.ts            # cn() helper
│   ├── styles/
│   │   └── globals.css         # Tailwind v4 @theme
│   ├── public/
│   │   ├── headshot.jpg        # Foto profesional
│   │   ├── og-image.png        # Open Graph
│   │   └── favicon.svg
│   ├── components.json          # shadcn config
│   ├── next.config.ts
│   ├── tsconfig.json
│   ├── package.json
│   └── README.md
├── Resumen/                     # CV source data
│   ├── CV_MASTER_2026_Jesus_Obando.md
│   └── CV_SOTA_2026_MASTER_FINAL.md
├── SPEC.md                      # This spec
└── README.md
```

---

## 11. Dependencies (SOTA 2026)

```json
{
  "name": "jesus-obando-cv",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev --turbopack",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "^15.0.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0",
    "motion": "^11.0.0",
    "@formkit/auto-animate": "^0.9.0",
    "next-themes": "^0.4.0",
    "lucide-react": "^0.400.0",
    "clsx": "^2.0.0",
    "tailwind-merge": "^2.0.0",
    "class-variance-authority": "^0.7.0"
  },
  "devDependencies": {
    "typescript": "^5.5.0",
    "@types/react": "^19.0.0",
    "@types/node": "^20.0.0",
    "tailwindcss": "^4.0.0",
    "@tailwindcss/postcss": "^4.0.0",
    "eslint": "^9.0.0",
    "eslint-config-next": "^15.0.0"
  }
}
```

### Instalación shadcn/ui:
```bash
# En el directorio del proyecto
npx shadcn@latest init

# Agregar componentes
npx shadcn@latest add button card badge separator scroll-area
npx shadcn@latest add mode-toggle
```
```

---

## 12. Success Criteria

- [ ] Both versions load < 2s
- [ ] Theme toggle works + persists
- [ ] Scroll progress accurate
- [ ] Mobile responsive (tested)
- [ ] Print-friendly version
- [ ] SEO metadata correct
- [ ] No console errors
- [ ] Lighthouse > 90
- [ ] GitHub repo clean

---

## 13. Out of Scope

- Backend/API routes
- Authentication
- CMS integration
- Blog section
- Multi-language (EN only v1)
- PDF generation (manual export)
- Contact form

---

*Document Version: 1.0*
*Last Updated: 2026-03-23*
