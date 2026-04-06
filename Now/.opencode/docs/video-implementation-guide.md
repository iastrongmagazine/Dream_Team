# Documentación Técnica: Implementación de Videos para OIM Website

## Resumen
Este documento detalla la implementación técnica de dos efectos de video especializados para el sitio web de Office Installations Mayen (OIM):
1. **Hero Section**: Video cinematográfico de fondo automático
2. **Scroll Video Section**: Video que avanza frame por frame según el scroll del usuario

---

## 1. HERO SECTION: Video Cinematográfico de Fondo

### Descripción
El Hero es la sección superior de la página que muestra un video de alta calidad como fondo, con contenido superpuesto (headline, subheadline, CTA). El video debe:
- Reproducirse automáticamente al cargar la página
- Estar muteado (silenciado) por defecto
- Reproducirse en bucle infinito
- Ocupar el viewport completo
- Ser responsivo y funcionar en todos los dispositivos

### Especificaciones del Video
- **Formato**: MP4 (H.264) con fallback WebM
- **Resolución recomendada**: 1920x1080 (Full HD)
- **Peso máximo**: 5-8 MB para carga inicial rápida
- **Duración sugerida**: 10-30 segundos en bucle

### Implementación en React/Next.js

```tsx
// components/HeroVideo.tsx
'use client';

import { useRef, useEffect } from 'react';

interface HeroVideoProps {
  videoSrc: string;
  posterSrc?: string;
  overlay?: boolean;
  children?: React.ReactNode;
}

export default function HeroVideo({
  videoSrc,
  posterSrc,
  overlay = true,
  children
}: HeroVideoProps) {
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    const video = videoRef.current;
    if (video) {
      // Configuración para reproducción automática
      video.playsInline = true;
      video.muted = true;
      video.loop = true;
      video.autoplay = true;
      
      // Intentar reproducir al cargar
      const playVideo = async () => {
        try {
          await video.play();
        } catch (error) {
          console.log('Autoplay prevented by browser:', error);
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
        className="absolute top-0 left-0 w-full h-full object-cover"
        src={videoSrc}
        poster={posterSrc}
        playsInline
        muted
        loop
        autoPlay
        preload="auto"
        aria-hidden="true"
      />
      
      {/* Optional Dark Overlay for text readability */}
      {overlay && (
        <div className="absolute top-0 left-0 w-full h-full bg-black/40" />
      )}
      
      {/* Content Overlay */}
      <div className="relative z-10 flex flex-col items-center justify-center h-full px-4 text-center">
        {children}
      </div>
    </section>
  );
}

// Usage / Ejemplo de uso
/*
<HeroVideo 
  videoSrc="/videos/interior-design-hero.mp4"
  posterSrc="/videos/interior-design-hero-poster.jpg"
>
  <h1 className="text-5xl md:text-7xl font-display text-white mb-6">
    Professional Office Furniture Installation in Atlanta
  </h1>
  <p className="text-xl text-white/90 mb-8 max-w-2xl">
    Since 2018, providing reliable, high-quality furniture assembly and relocation services.
  </p>
  <button className="px-8 py-4 bg-gradient-to-r from-[#FF5F5E] to-[#FF5F5E] text-white rounded-2xl text-lg font-semibold hover:opacity-90 transition-opacity">
    Get a Free Quote
  </button>
</HeroVideo>
*/
```

### Estilos CSS (Tailwind + Custom)

```css
/* styles/hero.css */
@layer components {
  .hero-section {
    @apply relative w-full h-screen min-h-[600px] overflow-hidden;
  }
  
  .hero-video {
    @apply absolute top-0 left-0 w-full h-full object-cover;
  }
  
  .hero-overlay {
    @apply absolute top-0 left-0 w-full h-full bg-black/30 
           flex items-center justify-center;
  }
  
  .hero-content {
    @apply relative z-10 px-4 text-center max-w-4xl;
  }
}
```

### Consideraciones de Rendimiento
1. **Preload**: Usar `preload="auto"` para cargar el video inmediatamente
2. **Poster**: Incluir una imagen estática como fallback mientras carga el video
3. **Compresión**: Comprimir el video usando HandBrake o FFmpeg:
   ```bash
   ffmpeg -i input.mp4 -vcodec libx264 -crf 23 -preset medium -vf scale=1920:1080 -acodec aac -b:a 128k output.mp4
   ```
4. **Fallback**: Proporcionar imagen estática si el navegador no soporta video

---

## 2. SCROLL VIDEO SECTION: Video Frame por Frame

### Descripción
Esta sección muestra un video que se sincroniza directamente con la posición de scroll del usuario. A medida que el usuario hace scroll hacia abajo, el video avanza frame por frame, creando una experiencia inmersiva y cinematográfica.

### Cómo Funciona
1. El video se carga pero se pausa en el frame 0
2. Se calcula el progreso de scroll de la sección (0% a 100%)
3. El progreso se convierte en tiempo de reproducción del video
4. Se usa `video.currentTime` para avanzar/retroceder el frame

### Especificaciones del Video
- **Formato**: MP4 (preferido) o WebM
- **FPS**: 24-30 fps (estándar de cine)
- **Resolución**: 1920x1080 o superior
- **Duración**: 5-15 segundos ideal para sección de scroll
- **Encoding**: Sin audio (el audio no se usa y ocupa espacio)

### Implementación en React/Next.js

```tsx
// components/ScrollVideo.tsx
'use client';

import { useRef, useEffect, useState, useCallback } from 'react';

interface ScrollVideoProps {
  videoSrc: string;
  height?: string;
  frameRate?: number;
  scrollHeight?: number; // Porcentaje extra de scroll (default 200%)
}

export default function ScrollVideo({
  videoSrc,
  height = '100vh',
  frameRate = 30,
  scrollHeight = 200
}: ScrollVideoProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const videoRef = useRef<HTMLVideoElement>(null);
  const [videoDuration, setVideoDuration] = useState(0);
  const [isLoaded, setIsLoaded] = useState(false);

  // Cargar metadata del video
  useEffect(() => {
    const video = videoRef.current;
    if (video) {
      video.addEventListener('loadedmetadata', () => {
        setVideoDuration(video.duration);
        setIsLoaded(true);
      });
    }
  }, []);

  // Calcular y actualizar el frame según el scroll
  const handleScroll = useCallback(() => {
    if (!containerRef.current || !videoRef.current || !isLoaded || videoDuration === 0) return;

    const container = containerRef.current;
    const rect = container.getBoundingClientRect();
    const containerHeight = container.offsetHeight;
    
    // Calcular cuánto ha scrollado el usuario a través de la sección
    // Cuando el top del contenedor entra en el viewport, startScroll = 0
    // Cuando el bottom del contenedor sale del viewport, endScroll = 1
    const scrollStart = -rect.top;
    const scrollEnd = scrollStart + window.innerHeight;
    
    // Progreso de scroll dentro de la sección (0 a 1)
    const rawProgress = scrollStart / (containerHeight - window.innerHeight);
    const progress = Math.max(0, Math.min(1, rawProgress));
    
    // Convertir progreso a tiempo de video
    const currentTime = progress * videoDuration;
    
    // Actualizar el frame del video
    videoRef.current.currentTime = currentTime;
  }, [isLoaded, videoDuration]);

  // Configurar event listeners de scroll
  useEffect(() => {
    window.addEventListener('scroll', handleScroll, { passive: true });
    window.addEventListener('resize', handleScroll, { passive: true });
    
    // Initial check
    handleScroll();
    
    return () => {
      window.removeEventListener('scroll', handleScroll);
      window.removeEventListener('resize', handleScroll);
    };
  }, [handleScroll]);

  return (
    <div 
      ref={containerRef}
      className="relative w-full"
      style={{ height: `${scrollHeight}vh` }}
    >
      <video
        ref={videoRef}
        className="sticky top-0 left-0 w-full h-screen object-cover"
        src={videoSrc}
        playsInline
        muted
        preload="auto"
        aria-hidden="true"
      />
    </div>
  );
}

// Usage / Ejemplo de uso
/*
<ScrollVideo 
  videoSrc="/videos/interior-design-scroll.mp4"
  frameRate={30}
  scrollHeight={300} // 3x la altura del viewport
/>
*/
```

### Implementación Alternativa con Intersection Observer (Más Precisa)

```tsx
// components/ScrollVideoPrecise.tsx
'use client';

import { useRef, useEffect, useState, useCallback } from 'react';

interface ScrollVideoPreciseProps {
  videoSrc: string;
  scrollMultiplier?: number; // Cuántas veces el viewport para hacer scroll
}

export default function ScrollVideoPrecise({
  videoSrc,
  scrollMultiplier = 2
}: ScrollVideoPreciseProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const videoRef = useRef<HTMLVideoElement>(null);
  const [duration, setDuration] = useState(0);
  const [isInView, setIsInView] = useState(false);

  useEffect(() => {
    const video = videoRef.current;
    if (video) {
      video.addEventListener('loadedmetadata', () => {
        setDuration(video.duration);
      });
    }
  }, []);

  useEffect(() => {
    const container = containerRef.current;
    const video = videoRef.current;
    
    if (!container || !video || duration === 0) return;

    const observer = new IntersectionObserver(
      ([entry]) => {
        setIsInView(entry.isIntersecting);
      },
      {
        threshold: 0, // Activar cuando cualquier parte sea visible
        rootMargin: '0px'
      }
    );

    observer.observe(container);

    const handleScroll = () => {
      if (!isInView) return;

      const rect = container.getBoundingClientRect();
      const viewportHeight = window.innerHeight;
      const containerHeight = container.offsetHeight;
      
      // Calcular progreso basado en cuánto ha pasado el usuario por la sección
      // Empezar cuando el contenedor entra en el viewport
      const startOffset = 0;
      const endOffset = containerHeight - viewportHeight;
      
      const scrollY = window.scrollY;
      const elementTop = rect.top + scrollY;
      
      const relativeScroll = scrollY - elementTop + viewportHeight;
      const progress = Math.max(0, Math.min(1, relativeScroll / (containerHeight - viewportHeight)));
      
      // Mapear progreso a tiempo del video
      const seekTime = progress * duration;
      video.currentTime = seekTime;
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    
    return () => {
      observer.disconnect();
      window.removeEventListener('scroll', handleScroll);
    };
  }, [duration, isInView]);

  return (
    <div 
      ref={containerRef}
      className="relative w-full"
      style={{ height: `${scrollMultiplier * 100}vh` }}
    >
      <video
        ref={videoRef}
        className="sticky top-0 left-0 w-full h-screen object-cover"
        src={videoSrc}
        playsInline
        muted
        preload="auto"
      />
    </div>
  );
}
```

### Versión Vanilla JavaScript (Sin Framework)

```javascript
// scroll-video.js

class ScrollVideo {
  constructor(element, videoSrc, options = {}) {
    this.element = element;
    this.video = element.querySelector('video');
    this.options = {
      scrollHeight: options.scrollHeight || 200, // % del viewport
      frameRate: options.frameRate || 30,
      smooth: options.smooth || false,
      ...options
    };
    
    this.duration = 0;
    this.isVisible = false;
    
    this.init();
  }
  
  async init() {
    // Cargar video
    this.video.src = this.videoSrc;
    await this.video.play();
    this.video.pause();
    
    this.video.addEventListener('loadedmetadata', () => {
      this.duration = this.video.duration;
      this.update();
    });
    
    // Scroll listener
    window.addEventListener('scroll', () => this.update(), { passive: true });
    window.addEventListener('resize', () => this.update(), { passive: true });
    
    // Intersection Observer para rendimiento
    this.observer = new IntersectionObserver(
      ([entry]) => {
        this.isVisible = entry.isIntersecting;
        if (this.isVisible) this.update();
      },
      { threshold: 0 }
    );
    this.observer.observe(this.element);
  }
  
  update() {
    if (!this.isVisible || this.duration === 0) return;
    
    const rect = this.element.getBoundingClientRect();
    const viewportHeight = window.innerHeight;
    const elementHeight = this.element.offsetHeight;
    
    // Calcular progreso (0 a 1)
    const scrollProgress = -rect.top / (elementHeight - viewportHeight);
    const progress = Math.max(0, Math.min(1, scrollProgress));
    
    // Sincronizar con tiempo del video
    this.video.currentTime = progress * this.duration;
  }
}

// Uso:
const scrollVideoElement = document.querySelector('[data-scroll-video]');
new ScrollVideo(scrollVideoElement, '/videos/video.mp4', {
  scrollHeight: 250,
  frameRate: 30
});
```

---

## 3. GUÍA DE OPTIMIZACIÓN DE VIDEOS

### Herramientas Recomendadas
- **FFmpeg**: Compresión de video profesional
- **HandBrake**: Interfaz gráfica para compresión
- **Clideo**: Herramienta online para compresión básica

### Comandos FFmpeg para Optimización

```bash
# Compresión para Hero Video (máximo 5MB, 1080p)
ffmpeg -i input.mp4 \
  -vcodec libx264 -crf 26 -preset fast \
  -vf scale=1920:1080:force_original_aspect_ratio=decrease \
  -acodec aac -b:a 96k \
  -movflags +faststart \
  hero-output.mp4

# Compresión para Scroll Video (máximo 3MB, 1080p)
ffmpeg -i input.mp4 \
  -vcodec libx264 -crf 28 -preset fast \
  -vf scale=1920:1080:force_original_aspect_ratio=decrease \
  -an \
  -movflags +faststart \
  scroll-output.mp4

# Generar WebM para browsers modernos
ffmpeg -i input.mp4 \
  -codec:v libvpx-vp9 -crf 30 -b:v 0 \
  -vf scale=1920:1080 \
  -codec:a libopus -b:a 64k \
  output.webm
```

### Checklist de Optimización
- [ ] Video压缩至目标大小
- [ ] Eliminar audio si no es necesario
- [ ] Usar codec H.264 (compatibilidad máxima)
- [ ] Añadir `movflags +faststart` para streaming
- [ ] Generar poster/image de fallback
- [ ] Probar en dispositivos reales

---

## 4. CHECKLIST DE IMPLEMENTACIÓN

### Hero Video
- [ ] Video reproducirse automáticamente
- [ ] Estar muteado por defecto
- [ ] Reproducirse en bucle
- [ ] Ser responsivo (mobile/tablet/desktop)
- [ ] Tener overlay oscuro para legibilidad del texto
- [ ] Incluir poster como fallback
- [ ] Cargar rápido (preload + compresión)

### Scroll Video
- [ ] Sincronizarse con scroll del usuario
- [ ] Avanzar frame por frame linealmente
- [ ] Funcionar al hacer scroll hacia arriba y abajo
- [ ] Ser responsivo
- [ ] No causar jank o lag
- [ ] Tener fallback de imagen si no carga

### Diseño (Design_Final.md Compliance)
- [ ] No usar bordes sólidos de 1px (usar background shifts)
- [ ] Usar gradientes solo en CTAs y Hero
- [ ] Aplicar Glassmorphism en headers flotantes
- [ ] Usar radios de bordes lg (1rem) o xl (1.5rem)
- [ ] Mantener hierarchy visual con tonal layering
- [ ] No usar texto negro puro (#000000), usar on_surface (#191c1d)

---

## 5. RECURSOS ADICIONALES

### Bibliotecas Recomendadas
- **ScrollyVideo.js**: Biblioteca dedicada para sincronización video-scroll
- **GSAP ScrollTrigger**: Para animaciones complejas con video
- **Locomotive Scroll**: Smooth scroll con soporte para video

### Referencias
- [WebCodecs Scroll Sync (GitHub)](https://github.com/diffusionstudio/webcodecs-scroll-sync)
- [Tutorial: Video Scroll Synchronization](https://lionkeng.medium.com/a-tutorial-webcodecs-video-scroll-synchronization-8b251e1a1708)
- [Creating a Video Scroll Animation with Vanilla JS](https://javascript.plainenglish.io/creating-a-video-scroll-animation-with-frames-using-vanilla-js-7112b3c22b48)

---

*Documento generado para el proyecto OIM Website - Implementación SOTA*
*Fecha: 2026-04-06*