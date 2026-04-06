# Proposal: OIM Website SOTA

## Intent

Crear un sitio web profesional de vanguardia para Office Installations Mayen (OIM) en Atlanta, implementando un diseño "Editorial Tech-Forward Light Theme" con video hero cinematográfico y scroll frame-by-frame mostrando servicios. El objetivo es generar una experiencia premium que Posicione a OIM como líder en instalación de muebles de oficina en Atlanta, destacando su experiencia desde 2018 y servicio bilingüe.

## Scope

### In Scope
- Next.js 15 App Router con TypeScript y Tailwind CSS 4
- Hero Section con video background cinematográfico (autoplay, muted, loop)
- Scroll Video Section con frame-by-frame sincronizado al scroll
- 4 categorías de servicios mostrados progresivamente durante scroll
- Sistema de diseño siguiendo Design_Final.md (No-Line, Glass & Gradient, Tonal)
- Deployment en Vercel
- SEO local ("Office Furniture Installation Atlanta")
- Selector de idioma ES/EN

### Out of Scope
- Backend/CMS para gestión de contenido (futuro)
- Blog o sección de noticias
- Chat en vivo
- Integración con CRM o email marketing
- Multilingual completo (solo selector ES/EN)

## Approach

1. **Setup**: Inicializar Next.js 15 con TypeScript y Tailwind CSS 4
2. **Diseño**: Implementar tokens de Design_Final.md (colores, spacing, typography)
3. **Hero**: Componente con video background, overlay contraste, contenido superpuesto
4. **Scroll Video**: Frame-by-frame sync usando requestAnimationFrame + Intersection Observer
5. **Servicios**: 4 categorías con items mostrados según progreso de scroll
6. **Secciones adicionales**: About, Gallery, Contact (form 4 campos)
7. **Optimización**: Compresión videos, Core Web Vitals, SEO
8. **Deploy**: Vercel con configuración óptima

## Affected Areas

| Area | Impact | Description |
|------|--------|-------------|
| `Now/.opencode/` | New | Proyecto Next.js 15 completo |
| `app/components/HeroSection.tsx` | New | Video hero cinematic |
| `app/components/ScrollVideoServices.tsx` | New | Frame-sync + servicios |
| `app/page.tsx` | New | Página principal |
| `lib/design-tokens.ts` | New | Sistema de diseño |
| `public/videos/` | New | Videos optimizados |

## Risks

| Risk | Likelihood | Mitigation |
|------|------------|------------|
| Video no carga en Safari iOS | Medium | playsInline + muted + poster fallback |
| Scroll lag en dispositivos lentos | Medium | Throttled updates + video compresión |
| Lighthouse performance fail | Low | preload="metadata" + lazy load |
| Autoplay bloqueado por browser | Low | Botón play fallback |

## Rollback Plan

1. Revertir en Vercel a deploy anterior
2. Cambiar video por imagen estática en HeroSection
3. Deshabilitar ScrollVideo, usar grid estática de servicios
4. Comando: `vercel deployments > promote previous`

## Dependencies

- Node.js 18+ (Next.js 15 requirement)
- Cuenta Vercel configurada
- Video: home-exploding.mp4 (ya disponible en assets)

## Success Criteria

- [ ] Video hero reproduce automáticamente en Chrome/Safari/Firefox
- [ ] Scroll video sincroniza correctamente (avanza y retrocede)
- [ ] 4 categorías de servicios visibles durante scroll
- [ ] Lighthouse Performance > 90
- [ ] WCAG 2.1 AA contrast ratio (overlay)
- [ ] Responsive en mobile (320px+) hasta desktop (1920px+)
- [ ] Deploy exitoso en Vercel