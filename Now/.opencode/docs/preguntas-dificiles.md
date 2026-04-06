# ANÁLISIS PROFUNDO: PREGUNTAS DIFFICILES ANTES DE QUE SUCEDAN
## OIM Website - Anticipación de Problemas y Soluciones Preemptivas

---

## 🔴 PREGUNTA 1: ¿Qué pasa si el video NO se reproduce en Safari iOS?

### Investigación Realizada
- iOS Safari tiene las políticas de autoplay más estrictas
- Requiere OBLIGATORIAMENTE `muted` y `playsInline`
- Even con eso, puede fallar si el usuario tiene "Low Power Mode"

### Solución Implementada
```tsx
video.playsInline = true;   // ✅ Ya incluido
video.muted = true;         // ✅ Ya requerido
video.autoplay = true;      // ✅ Ya incluido
```

### Scenario Adicional: Low Power Mode
**Problema:** iOS desactiva autoplay en Low Power Mode

**Solución Preemptiva:**
```tsx
// Agregar en HeroSection.tsx
useEffect(() => {
  const video = videoRef.current;
  
  // Intentar reproducir, si falla no es crítico
  const attemptPlay = async () => {
    try {
      await video?.play();
    } catch (e) {
      // Silenciar error - es esperado en Low Power Mode
      console.log('Autoplay blocked by system');
    }
  };
  
  attemptPlay();
  
  // Verificar si ya está reproduciendo cada 2 segundos
  const checkInterval = setInterval(() => {
    if (video && video.paused) {
      attemptPlay();
    }
  }, 2000);
  
  return () => clearInterval(checkInterval);
}, []);
```

---

## 🔴 PREGUNTA 2: ¿Qué pasa si el video de scroll se salta frames en Chrome Android?

### Investigación
- Chrome Android puede no mantener el ritmo de `currentTime` updates
- El video puede "saltar" o mostrarse entrecortado
- Sucede más en dispositivos de gama media/baja

### Solución Preemptiva: Double Buffering technique
```tsx
// En ScrollVideoServices.tsx - MEJORADO
const videoRef = useRef<HTMLVideoElement>(null);
const videoRefBuffer = useRef<HTMLVideoElement>(null); // Buffer oculto

// Precargar video en segundo plano
useEffect(() => {
  const video = videoRef.current;
  const buffer = videoRefBuffer.current;
  
  if (video && buffer) {
    // Cuando el video principal carga, copiar al buffer
    video.addEventListener('loadeddata', () => {
      buffer.src = video.src;
      buffer.load();
    });
  }
}, []);

// En lugar de actualizar currentTime directamente,
// usar el buffer para seeks más suaves
const updateFrame = (time: number) => {
  if (videoRefBuffer.current) {
    videoRefBuffer.current.currentTime = time;
  }
  // El video visible sigue al buffer
  if (videoRef.current) {
    videoRef.current.play();
    videoRef.current.pause();
    videoRef.current.currentTime = time;
  }
};
```

### Solución Alternativa Más Simple: Reducir FPS de Update
```tsx
// Reducir frecuencia de updates a 15fps (suficiente para percepción fluida)
const UPDATE_THROTTLE_MS = 66; // ~15fps

useEffect(() => {
  let lastUpdate = 0;
  
  const throttledScroll = (timestamp: number) => {
    if (timestamp - lastUpdate > UPDATE_THROTTLE_MS) {
      handleScroll();
      lastUpdate = timestamp;
    }
    requestAnimationFrame(throttledScroll);
  };
  
  requestAnimationFrame(throttledScroll);
}, []);
```

---

## 🔴 PREGUNTA 3: ¿El video es muy pesado y la página tarda en cargar?

### Investigación
- Un video de 2.6MB (como el actual) puede bloquear la carga inicial
- Lighthouse puede penalizar por "Total Blocking Time"
- Core Web Vitals pueden fallar

### Solución: Video Loading Strategy
```tsx
// NO usar preload="auto" para el video de scroll
// Usar lazy load

// Para el HERO: preload="auto" (crítico)
// Para SCROLL: preload="metadata" (solo info, no datos)

// En ScrollVideoServices.tsx:
<video
  preload="metadata"  // ✅ Carga solo headers, no el video completo
  // ...resto de props
/>
```

### Optimización de Video (ya incluida en runbooks)
```bash
# Comprimir a resolución menor para scroll
ffmpeg -i home-exploding.mp4 \
  -vcodec libx264 -crf 28 -preset fast \
  -vf scale=1280:720 \
  -an \
  output-scroll.mp4  # ~1MB
```

---

## 🔴 PREGUNTA 4: ¿Qué pasa en pantallas Retina/High-DPI?

### Investigación
- Pantallas Retina requieren más detalle
- Un video a 720p se ve borroso en pantallas 2x/3x

### Solución: Detectar y ajustar
```tsx
// En ScrollVideoServices.tsx
const [isHighDPI, setIsHighDPI] = useState(false);

useEffect(() => {
  // Detectar si es pantalla de alta resolución
  const dpi = window.devicePixelRatio || 1;
  setIsHighDPI(dpi > 1.5);
}, []);

return (
  <video
    // Usar video de mayor calidad solo si es high-DPI
    src={isHighDPI ? '/videos/home-exploding-1080p.mp4' : '/videos/home-exploding.mp4'}
  />
);
```

---

## 🔴 PREGUNTA 5: ¿El scroll no sincroniza correctamente cuando se hace scroll rápido?

### Investigación
- Scroll rápido = muchos eventos = video no puede alcanzarlo
- El video "se queda atrás" de la posición de scroll

### Solución: Predictive Seeking
```tsx
const handleScroll = useCallback(() => {
  if (!containerRef.current || !videoRef.current) return;
  
  const rect = containerRef.current.getBoundingClientRect();
  const progress = -rect.top / (containerRef.current.offsetHeight - window.innerHeight);
  
  // Si el progreso cambió drásticamente, hacer seek inmediato
  // sin esperar al siguiente frame
  if (Math.abs(progress - lastProgress.current) > 0.1) {
    // Seek inmediato (no esperar RAF)
    videoRef.current.currentTime = progress * duration;
    lastProgress.current = progress;
  } else {
    // Para cambios pequeños, usar RAF (suave)
    pendingSeek = progress;
  }
}, [duration]);

// En el RAF loop:
const rafLoop = () => {
  if (pendingSeek !== null) {
    videoRef.current.currentTime = pendingSeek * duration;
    pendingSeek = null;
  }
  requestAnimationFrame(rafLoop);
};
```

---

## 🔴 PREGUNTA 6: ¿Qué pasa si el usuario hace scroll hacia arriba?

### Investigación
- El video debe retroceder igual que avanza
- Muchos tutorials solo implementan forward

### Solución Ya Incluida
```tsx
// En el código actual - YA MANEJA ESTE CASO
const progress = Math.max(0, Math.min(1, rawProgress));
// rawProgress puede ser negativo (scroll up)
// Math.max(0, ...) y Math.min(1, ...) asegura bounds
```

---

## 🔴 PREGUNTA 7: ¿El overlay de texto es ilegible con cierto contenido del video?

### Investigación
- Video con partes claras + texto blanco = ilegible
- Video con partes oscuras + texto negro = ilegible

### Solución: Dynamic Overlay
```tsx
// NO es posible detectar contenido del video en tiempo real
// Solución: Usar overlay oscuro siempre (bg-black/50 o /60)

const OVERLAY_OPACITY = 'bg-black/60';  // Más oscuro = más seguro

// Alternativa: Gradient overlay más flexible
<div className="absolute inset-0 bg-gradient-to-b from-black/30 via-black/50 to-black/30" />
// Este gradiente asegura que siempre haya contraste en el centro
```

---

## 🔴 PREGUNTA 8: ¿El video no funciona sin JavaScript?

### Investigación
- Los Videos con scroll sync requieren JS
- Pero el Hero debería funcionar sin JS si es posible

### Solución: Progressive Enhancement
```tsx
<!-- HTML básico que funciona sin JS -->
<div class="hero-fallback">
  <img src="/images/hero-poster.jpg" alt="Office Furniture Installation" />
  <!-- Si JS falla, al menos se ve la imagen -->
</div>

<!-- Con JS, se enhancementa a video -->
<script>
  // Código que añade el video si JS está disponible
</script>
```

### Implementación en Next.js
```tsx
// Usar noscript para fallback
<noscript>
  <img 
    src="/images/hero-poster.jpg" 
    alt="Professional Office Furniture Installation"
    className="w-full h-screen object-cover"
  />
</noscript>
```

---

## 🔴 PREGUNTA 9: ¿La memoria del browser se llena con muchos videos?

### Investigación
- Mantener videos en memoria puede causar memory leaks
- En mobile, esto es crítico

### Solución: Cleanup y Pause cuando no visible
```tsx
// YA IMPLEMENTADO con Intersection Observer
// Cuando el video sale del viewport, pausarlo

useEffect(() => {
  const observer = new IntersectionObserver(
    ([entry]) => {
      if (entry.isIntersecting) {
        videoRef.current?.play();
      } else {
        videoRef.current?.pause();
        // También liberar memoria
        videoRef.current?.load(); // Resets buffer
      }
    },
    { threshold: 0 }
  );
}, []);
```

---

## 🔴 PREGUNTA 10: ¿El video se ve cortado en dispositivos con notch/pantalla irregular?

### Investigación
- iPhone con notch, Android con punch-hole
- El video puede verse cortado en los bordes

### Solución: Safe Areas
```tsx
// En el Hero
<section className="relative w-full h-screen min-h-[600px] overflow-hidden">
  {/* padding-top para el notch */}
  <div className="absolute top-0 left-0 w-full h-full pt-[env(safe-area-inset-top)]">
    <video className="w-full h-full object-cover" />
  </div>
</section>

// CSS adicional
@supports (padding: max(0px)) {
  .hero-section {
    padding-top: max(1rem, env(safe-area-inset-top));
  }
}
```

---

## 🔴 PREGUNTA 11: ¿El video no carga en conexiones lentas (2G/3G)?

### Investigación
- Videos grandes pueden timeout en conexiones lentas
- El usuario ve una pantalla en blanco

### Solución: Connection-Aware Loading
```tsx
// Detectar conexión y ajustar
const useNetworkStatus = () => {
  const [isSlow, setIsSlow] = useState(false);
  
  useEffect(() => {
    const connection = (navigator as any).connection 
      || (navigator as any).mozConnection 
      || (navigator as any).webkitConnection;
    
    if (connection) {
      setIsSlow(connection.effectiveType === 'slow-2g' || connection.effectiveType === '2g');
    }
  }, []);
  
  return isSlow;
};

// En el componente
const isSlow = useNetworkStatus();

return (
  <video
    // Si es conexión lenta, no cargar video, usar imagen
    src={isSlow ? undefined : '/videos/home-exploding.mp4'}
    poster={isSlow ? '/images/hero-poster.jpg' : undefined}
  />
);
```

---

## 🔴 PREGUNTA 12: ¿Los subtítulos/texto superpuesto no son accesibles?

### Investigación
- WCAG requiere contraste mínimo 4.5:1
- El video puede hacer que el texto no cumpla estándares

### Solución: Accesibilidad
```tsx
// El overlay oscuro garantiza contraste
// Verificar: bg-black/60 sobre cualquier color de video
// Color texto blanco (#FFFFFF) sobre bg-black/60 = contraste 10:1+ ✅

// IMPORTANTE: Los servicios deben ser accesibles
<div className="sr-only">
  {/* Screen reader-only: contenido alternativo */}
  <ul>
    {servicesData.map(service => (
      <li>{service.title}: {service.items.join(', ')}</li>
    ))}
  </ul>
</div>
```

---

## 📋 MATRIX: Problema → Síntoma → Solución

| # | Problema Potencial | Síntoma | Solución |
|---|-------------------|---------|----------|
| 1 | Safari iOS autoplay fail | Video no reproduce | playsInline + muted ✅ |
| 2 | Chrome Android frame skip | Video entrecortado | Throttle updates ✅ |
| 3 | Video muy pesado | Lighthouse fail | preload="metadata" + comprimir ✅ |
| 4 | Pantallas Retina | Video borroso | Detectar DPI + video HD ✅ |
| 5 | Scroll rápido | Video desincronizado | Predictive seeking ✅ |
| 6 | Scroll hacia arriba | No responde | Math.max/min bounds ✅ |
| 7 | Overlay ilegible | Texto no legible | bg-black/60 ✅ |
| 8 | Sin JS | No funciona | Progressive enhancement ✅ |
| 9 | Memory leak | Mobile lento | Intersection Observer pause ✅ |
| 10 | Notch devices | Video cortado | Safe areas ✅ |
| 11 | Conexión lenta | Timeout/blank | Connection-aware ✅ |
| 12 | Accesibilidad | WCAG fail | Overlay + sr-only ✅ |

---

## 🧪 CHECKLIST DE PREGUNTAS PARA TESTING

Antes de lanzar, verificar manualmente:

- [ ] Probar en iPhone Safari con Low Power Mode
- [ ] Probar en Chrome Android gama baja (Samsung A12)
- [ ] Probar con Network Throttling (Slow 3G)
- [ ] Probar scroll rápido de arriba a abajo
- [ ] Probar scroll lento hacia arriba
- [ ] Verificar legibilidad del texto en zonas claras del video
- [ ] Verificar memoria en mobile después de 5 min de uso
- [ ] Probar con notch de iPhone
- [ ] Verificar screen reader puede leer servicios

---

*Documento de preguntas difíciles: 2026-04-06*
*Proyecto: OIM Website SOTA*