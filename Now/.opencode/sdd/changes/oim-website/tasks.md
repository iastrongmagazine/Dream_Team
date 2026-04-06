# Tasks: OIM Website SOTA

## Phase 1: Project Setup & Infrastructure

- [ ] 1.1 Inicializar Next.js 15: `npx create-next-app@latest oim-website --typescript --tailwind --eslint`
- [ ] 1.2 Configurar tailwind.config.ts con design tokens de Design_Final.md
- [ ] 1.3 Crear `app/globals.css` con Tailwind @theme y custom properties
- [ ] 1.4 Crear `lib/design-tokens.ts` exports de colores y spacing
- [ ] 1.5 Crear `lib/content.ts` con contenido estático OIM
- [ ] 1.6 Copiar video a `public/videos/home-exploding.mp4`
- [ ] 1.7 Generar poster del video con FFmpeg

## Phase 2: Core Components - Hero & Video

- [ ] 2.1 Crear `components/HeroSection.tsx` con video autoplay/muted/loop
- [ ] 2.2 Implementar overlay contraste (bg-black/50)
- [ ] 2.3 Añadir contenido: headline, subheadline, CTA button
- [ ] 2.4 Añadir trust indicators below CTA
- [ ] 2.5 Verificar responsive design (mobile/desktop)
- [ ] 2.6 Verificar autoplay funciona en Chrome/Safari/Firefox
- [ ] 2.7 Verificar poster fallback carga correctamente

## Phase 3: Scroll Video & Services

- [ ] 3.1 Crear `components/ScrollVideoServices.tsx` frame-sync logic
- [ ] 3.2 Implementar Intersection Observer para activar en viewport
- [ ] 3.3 Implementar throttled scroll handler (66ms)
- [ ] 3.4 Crear 4 categorías de servicios con items
- [ ] 3.5 Implementar display progresivo según scroll progress
- [ ] 3.6 Verificar video avanza y retrocede con scroll
- [ ] 3.7 Verificar servicios se muestran correctamente (4 estados)
- [ ] 3.8 Testing performance - verificar no hay lag en mobile

## Phase 4: Additional Sections

- [ ] 4.1 Crear `components/AboutSection.tsx` con tagline y copy
- [ ] 4.2 Crear `components/ProjectGallery.tsx` con 3 categorías
- [ ] 4.3 Crear `components/ContactForm.tsx` con 4 campos + selector idioma
- [ ] 4.4 Crear `components/LanguageSelector.tsx` (ES/EN toggle)
- [ ] 4.5 Integrar todas las secciones en `app/page.tsx`

## Phase 5: Design System Compliance

- [ ] 5.1 Verificar no hay bordes 1px (usar background shifts)
- [ ] 5.2 Verificar gradientes solo en CTA y Hero
- [ ] 5.3 Verificar glassmorphism en overlays (backdrop-blur)
- [ ] 5.4 Verificar corner radius lg/xl (1rem/1.5rem)
- [ ] 5.5 Verificar tonal layering para profundidad
- [ ] 5.6 Verificar texto usa on_surface (#191c1d), no #000000

## Phase 6: Optimization & SEO

- [ ] 6.1 Comprimir video con FFmpeg (crf 28, 720p, sin audio)
- [ ] 6.2 Implementar SEO metadata (title, description, local seo)
- [ ] 6.3 Verificar Core Web Vitals (Lighthouse > 90)
- [ ] 6.4 Implementar lazy loading para imágenes si hay

## Phase 7: Testing & Deployment

- [ ] 7.1 Testing manual: Video hero reproduce correctamente
- [ ] 7.2 Testing manual: Scroll video sincronizado
- [ ] 7.3 Testing manual: Todas las secciones visibles
- [ ] 7.4 Testing responsive: Mobile (320px) hasta Desktop (1920px)
- [ ] 7.5 Configurar Vercel deployment
- [ ] 7.6 Deploy y verificar producción
- [ ] 7.7 Post-deployment: Verificar video carga en producción
