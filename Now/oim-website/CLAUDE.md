# CLAUDE.md — OIM Website (oim-website)

> Sub-proyecto del PersonalOS Think Different v6.1
> Workspace raíz: `Think_Different/Now/oim-website/`

---

## Stack

| Tecnología     | Versión  | Notas                              |
|----------------|----------|------------------------------------|
| Next.js        | 16.2.2   | App Router + Turbopack             |
| React          | 19       | Server + Client components         |
| TypeScript     | strict   | `tsconfig.json` strict mode        |
| Tailwind       | v4       | `@import "tailwindcss"` + `@theme` |
| Font           | Geist    | `next/font/google`, display:swap   |

## Estructura de Componentes

```
src/
├── app/
│   ├── layout.tsx          — SEO SOTA + LocalBusiness JSON-LD + Geist
│   ├── page.tsx            — Entry point: nav glass + todas las secciones
│   └── globals.css         — Tailwind v4 + @theme OIM tokens
└── components/
    ├── HeroSection.tsx         — named export, video bg, dual gradient overlay
    ├── ScrollVideoServices.tsx — named export, RAF frame-by-frame, glassmorphism
    ├── AboutSection.tsx        — default export, split 2-col, IntersectionObserver
    ├── ProjectGallery.tsx      — default export, grid asimétrico
    ├── ContactForm.tsx         — default export, split layout
    └── LanguageSelector.tsx    — default export, EN/ES switch
```

## Reglas Críticas

- `min-h-[100dvh]` — NUNCA `h-screen` (iOS Safari viewport bug)
- NO `backdrop-blur` en overlay del Hero — borroneá el video
- Tailwind v4: NO usar `@tailwind base/components/utilities` (es sintaxis v3)
- Videos: `public/videos/Interior_Design.mp4` y `Home_exploding_view.mp4`
- Exports: `HeroSection` y `ScrollVideoServices` son **named exports**; el resto **default**

## SEO

- `og-image.jpg` (1200×630) — PENDIENTE crear
- `apple-touch-icon.png` (180×180) — PENDIENTE crear
- `favicon.ico` — usar existente

## Comandos

```bash
npm run dev     # Turbopack dev server en localhost:3000
npm run build   # Production build
npm run lint    # ESLint
```

---

*OIM Atlanta — Office Furniture Installation | oimatlanta.com*
