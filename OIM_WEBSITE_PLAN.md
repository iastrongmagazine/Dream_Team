# PLAN MAESTRO: OIM Website SOTA (CON CÓDIGO)
## Office Installations Mayen - Sitio Web con Diseño de Vanguardia

---

## 📋 FASE 1: ANÁLISIS Y PREPARACIÓN (COMPLETADO)

### 1.1 Recursos Analizados
- [x] **Guia_Visual_OIM.png** - Referencia visual con estructura, copy y layout
- [x] **Design_Final.md** - Especificaciones de diseño "Editorial Tech-Forward Light Theme"
- [x] **OIM_Website_Content.md** - Contenido textual estructurado
- [x] **Video: Home_exploding_view.mp4** - Copiado a `.opencode/assets/videos/`

### 1.2 Stack Tecnológico Elegido
- **Framework**: Next.js 15 (App Router)
- **Lenguaje**: TypeScript
- **Estilos**: Tailwind CSS 4
- **Despliegue**: Vercel
- **Estética**: taste-skill (Apple-limpio, minimal premium)

---

## 🎬 FASE 2: CÓDIGO DE VIDEOS (LISTO PARA USAR)

### 2.1 HERO SECTION: Video Cinematográfico

```tsx
// app/components/HeroSection.tsx
'use client';

import { useRef, useEffect } from 'react';

interface HeroSectionProps {
  videoSrc: string;
  posterSrc?: string;
  children?: React.ReactNode;
}

export default function HeroSection({
  videoSrc,
  posterSrc,
  children
}: HeroSectionProps) {
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    const video = videoRef.current;
    if (video) {
      video.playsInline = true;
      video.muted = true;
      video.loop = true;
      video.autoplay = true;
      
      const playVideo = async () => {
        try {
          await video.play();
        } catch (error) {
          console.log('Autoplay prevented:', error);
        }
      };
      
      video.addEventListener('canplaythrough', playVideo);
      return () => video.removeEventListener('canplaythrough', playVideo);
    }
  }, []);

  return (
    <section className="relative w-full h-screen min-h-[600px] overflow-hidden">
      {/* Video Background */}
      <video
        ref={videoRef}
        className="absolute top-0 left-0 w-full h-full object-cover will-change-transform"
        src={videoSrc}
        poster={posterSrc}
        playsInline
        muted
        loop
        autoPlay
        preload="auto"
        aria-hidden="true"
      />
      
      {/* Dark Overlay for text contrast - AJUSTABLE */}
      <div className="absolute top-0 left-0 w-full h-full bg-black/50 backdrop-blur-sm" />
      
      {/* Content */}
      <div className="relative z-10 flex flex-col items-center justify-center h-full px-4 text-center">
        {children}
      </div>
    </section>
  );
}
```

**Uso:**
```tsx
<HeroSection videoSrc="/videos/home-exploding.mp4">
  <h1 className="text-5xl md:text-7xl font-display text-white mb-6">
    Professional Office Furniture Installation in Atlanta
  </h1>
  <p className="text-xl text-white/90 mb-8 max-w-2xl">
    Since 2018, providing reliable, high-quality furniture assembly and relocation services.
  </p>
  <button className="px-8 py-4 bg-gradient-to-r from-[#FF5F5E] to-[#FF5F5E] text-white rounded-2xl text-lg font-semibold hover:opacity-90">
    Get a Free Quote
  </button>
</HeroSection>
```

---

### 2.2 SCROLL VIDEO SECTION: Frame por Frame + Servicios

```tsx
// app/components/ScrollVideoServices.tsx
'use client';

import { useRef, useEffect, useState, useCallback } from 'react';

interface Service {
  title: string;
  items: string[];
}

const servicesData: Service[] = [
  {
    title: "Office Furniture Installation",
    items: ["Desks & workstations", "Cubicles", "Conference tables", "Chairs & storage units"]
  },
  {
    title: "Office Setup & Reconfiguration",
    items: ["New office setups", "Workspace redesign", "Furniture rearrangement"]
  },
  {
    title: "Disassembly & Moving",
    items: ["Safe disassembly", "Relocation", "Reinstallation"]
  },
  {
    title: "Commercial Projects",
    items: ["Small & large offices", "Corporate environments", "Fast turnaround projects"]
  }
];

interface ScrollVideoServicesProps {
  videoSrc: string;
  scrollHeight?: number; // 200 = 2x viewport height
}

export default function ScrollVideoServices({
  videoSrc,
  scrollHeight = 300
}: ScrollVideoServicesProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const videoRef = useRef<HTMLVideoElement>(null);
  const [duration, setDuration] = useState(0);
  const [isInView, setIsInView] = useState(false);
  const lastProgress = useRef(0);

  useEffect(() => {
    const video = videoRef.current;
    if (video) {
      video.addEventListener('loadedmetadata', () => setDuration(video.duration));
    }
  }, []);

  const handleScroll = useCallback(() => {
    if (!containerRef.current || !videoRef.current || duration === 0) return;

    const rect = containerRef.current.getBoundingClientRect();
    const viewportHeight = window.innerHeight;
    const containerHeight = containerRef.current.offsetHeight;

    // Calculate progress (0 to 1) based on scroll position
    const rawProgress = -rect.top / (containerHeight - viewportHeight);
    const progress = Math.max(0, Math.min(1, rawProgress));

    // Only update if change is significant (performance)
    if (Math.abs(progress - lastProgress.current) > 0.001) {
      videoRef.current.currentTime = progress * duration;
      lastProgress.current = progress;
    }
  }, [duration]);

  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

    // Intersection Observer to activate only when in viewport
    const observer = new IntersectionObserver(
      ([entry]) => setIsInView(entry.isIntersecting),
      { threshold: 0 }
    );
    observer.observe(container);

    window.addEventListener('scroll', handleScroll, { passive: true });
    window.addEventListener('resize', handleScroll, { passive: true });

    return () => {
      observer.disconnect();
      window.removeEventListener('scroll', handleScroll);
      window.removeEventListener('resize', handleScroll);
    };
  }, [handleScroll]);

  // Calculate which service to show based on progress
  const getCurrentServiceIndex = () => {
    if (!containerRef.current || duration === 0) return 0;
    const rect = containerRef.current.getBoundingClientRect();
    const progress = Math.max(0, Math.min(1, -rect.top / (containerRef.current.offsetHeight - window.innerHeight)));
    return Math.min(servicesData.length - 1, Math.floor(progress * servicesData.length));
  };

  const currentServiceIndex = getCurrentServiceIndex();

  return (
    <div 
      ref={containerRef}
      className="relative w-full"
      style={{ height: `${scrollHeight}vh` }}
    >
      {/* Video Background - Sticky */}
      <video
        ref={videoRef}
        className="sticky top-0 left-0 w-full h-screen object-cover"
        src={videoSrc}
        playsInline
        muted
        preload="auto"
        aria-hidden="true"
      />
      
      {/* Services Overlay - Shows progressive content */}
      <div className="absolute top-0 left-0 w-full h-full flex items-center justify-center pointer-events-none">
        <div className="bg-black/60 backdrop-blur-md px-8 py-12 rounded-2xl max-w-2xl w-full mx-4">
          {servicesData.map((service, index) => (
            <div 
              key={service.title}
              className={`transition-opacity duration-500 ${
                index === currentServiceIndex ? 'opacity-100' : 'opacity-0 absolute'
              }`}
            >
              <h2 className="text-3xl md:text-4xl font-display text-white mb-6 text-center">
                {service.title}
              </h2>
              <ul className="space-y-3">
                {service.items.map((item) => (
                  <li key={item} className="flex items-center text-white/90">
                    <span className="w-2 h-2 bg-[#FF5F5E] rounded-full mr-3" />
                    <span className="text-lg">{item}</span>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
```

**Uso:**
```tsx
<ScrollVideoServices 
  videoSrc="/videos/home-exploding.mp4"
  scrollHeight={300} // 3x viewport for all 4 services
/>
```

---

## 📐 FASE 3: ARQUITECTURA Y DISEÑO

### 3.1 Estructura de Componentes

```
src/
├── app/
│   ├── page.tsx                 # Página principal
│   ├── layout.tsx               # Root layout
│   └── globals.css              # Tailwind + custom tokens
├── components/
│   ├── HeroSection.tsx         # Video cinematic background
│   ├── ScrollVideoServices.tsx # Frame-by-frame + servicios
│   ├── AboutSection.tsx        # Historia y propuesta de valor
│   ├── ProjectGallery.tsx      # Categorías: Corporate, Executive, Before/After
│   └── ContactForm.tsx         # Formulario 4 campos + idioma
├── lib/
│   ├── design-tokens.ts        # Colores, spacing, typography
│   └── content.ts             # Contenido OIM
└── public/
    └── videos/
        └── home-exploding.mp4  # Video para hero y scroll
```

### 3.2 Design System - Design_Final.md

**Colores:**
| Token | Hex | Uso |
|-------|-----|-----|
| `surface` | #f8f9fa | Canvas/base |
| `surface-container-low` | #f3f4f5 | Section layer |
| `surface-container-lowest` | #ffffff | Cards |
| `primary` | #FF5F5E | CTAs, gradientes |
| `secondary` | #00B4FF | Sky blue |
| `on_surface` | #191c1d | Texto principal |

**Reglas Críticas:**
- ❌ NO bordes sólidos 1px → USAR background shifts
- ❌ NO más de un gradiente por vista
- ❌ NO texto negro puro (#000000) → USAR on_surface (#191c1d)
- ✅ USAR glassmorphism (backdrop-blur) en overlays
- ✅ USAR radios lg (1rem) o xl (1.5rem)

---

## 🚀 FASE 4: IMPLEMENTACIÓN STEP BY STEP

### Step 1: Setup Proyecto
- [ ] Inicializar Next.js 15 + TypeScript + Tailwind
- [ ] Configurar design tokens
- [ ] Copiar video a `/public/videos/`

### Step 2: Hero Section
- [ ] Implementar HeroSection.tsx con código proporcionado
- [ ] Ajustar overlay (bg-black/50) para legibilidad
- [ ] Verificar texto legible sobre video

### Step 3: Scroll Video + Servicios
- [ ] Implementar ScrollVideoServices.tsx con código proporcionado
- [ ] Verificar sincronización scroll-video
- [ ] Verificar 4 servicios aparecen progresivamente

### Step 4: Secciones Restantes
- [ ] About Section
- [ ] Project Gallery
- [ ] Contact Form (4 campos)
- [ ] Language Selector ES/EN

### Step 5: Optimización
- [ ] Compresión videos (FFmpeg)
- [ ] SEO local
- [ ] Core Web Vitals

### Step 6: Deployment Vercel
- [ ] Deploy y testing

---

## ✅ CHECKLIST DE CALIDAD

### Código Hero
- [ ] autoplay, muted, loop, playsinline
- [ ] preload="auto" + poster
- [ ] will-change-transform
- [ ] Overlay contraste adjustable

### Código Scroll
- [ ] Intersection Observer para activate
- [ ] Throttled update (no cada pixel)
- [ ] 4 servicios muestran progresivamente
- [ ] No causa lag/jank

### Diseño (Design_Final.md)
- [ ] No bordes 1px
- [ ] Gradientes solo en Hero y CTA
- [ ] Glassmorphism en overlays
- [ ] Radios lg/xl

---

## 📊 NOTAS DE INVESTIGACIÓN APLICADA

### Hallazgos:
1. **Hero**: playsinline para iOS, will-change para GPU, poster fallback
2. **Scroll**: requestAnimationFrame + Intersection Observer = mejor performance
3. **Alternativas**: GSAP ScrollTrigger (heavy), WebCodecs (experimental), CSS Scroll-Timeline (soporte limitado)

---

*Plan con código: 2026-04-06*
*Proyecto: OIM Website SOTA*