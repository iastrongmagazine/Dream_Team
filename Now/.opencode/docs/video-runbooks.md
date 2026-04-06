# RUNBOOKS DE RESPALDO: OIM Website
## Procedimientos de Emergencia y Fallback

---

## 📕 RUNBOOK 1: Video No Carga - Fallback de Imagen

### Síntoma
El video de fondo no carga o no se reproduce en ciertos navegadores/dispositivos.

### Solución Automática
El componente ya incluye `poster` como fallback:

```tsx
<video
  poster="/images/hero-poster.jpg"  // Fallback automático
  src="/videos/home-exploding.mp4"
/>
```

### Pasos de Implementación

**Step 1: Generar poster del video**
```bash
# Extraer primer frame como imagen
ffmpeg -i home-exploding.mp4 -ss 00:00:01 -vframes 1 hero-poster.jpg
```

**Step 2: Comprimir poster**
```bash
# Optimizar para web
ffmpeg -i hero-poster.jpg -q:v 2 -vf scale=1920:1080 hero-poster.jpg
```

**Step 3: Verificar tamaños**
- Poster: < 200KB
- Video: < 5MB

### Verificación
```bash
# Lista de verificación:
- [ ] Poster se muestra mientras carga video
- [ ] Poster se muestra si video falla
- [ ] En mobile: verificar iOS Safari
- [ ] En desktop: verificar Firefox sin aceleración hardware
```

---

## 📕 RUNBOOK 2: Autoplay Bloqueado por Browser

### Síntoma
El video no reproduce automáticamente en Chrome/Safari mobile.

### Causa
Browsers bloquean autoplay sin interacción del usuario.

### Solución Implementada
```tsx
// En HeroSection.tsx - ya incluido
video.muted = true;  // REQUERIDO para autoplay
video.playsInline = true;  // Para iOS
```

### Verificación Manual
| Browser | Comportamiento Esperado |
|---------|------------------------|
| Chrome Desktop | Autoplay funciona (muted) |
| Safari iOS | Autoplay funciona (muted + playsInline) |
| Firefox | Autoplay funciona (muted) |
| Mobile Chrome | Puede requerir tap - mostrar botón "Play" |

### Fallback Adicional: Botón Play
```tsx
// Si autoplay falla, mostrar botón de play
const [showPlayButton, setShowPlayButton] = useState(false);

useEffect(() => {
  const video = videoRef.current;
  video.play().catch(() => {
    setShowPlayButton(true); // Mostrar botón
  });
}, []);

{showPlayButton && (
  <button onClick={() => videoRef.current?.play()}>
    ▶ Play Video
  </button>
)}
```

---

## 📕 RUNBOOK 3: Scroll Video Jank/Lag

### Síntoma
El video frame-by-frame causa lag o saltos durante el scroll.

### Causas Posibles
1. Actualización en cada pixel de scroll
2. No usar requestAnimationFrame
3. Video muy grande
4. Sin Intersection Observer

### Solución Ya Implementada
```tsx
// ScrollVideoServices.tsx - optimización ya incluida:
// 1. Solo actualizar si cambio > 0.001
if (Math.abs(progress - lastProgress.current) > 0.001) {
  videoRef.current.currentTime = progress * duration;
}

// 2. Intersection Observer - solo ejecutar cuando visible
const observer = new IntersectionObserver(
  ([entry]) => setIsInView(entry.isIntersecting)
);
```

### Pasos de Optimización Adicional

**Step 1: Comprimir video más**
```bash
# Reducir calidad manteniendo 30fps
ffmpeg -i input.mp4 -vcodec libx264 -crf 28 -preset fast -an output.mp4
# -an = sin audio (no necesario para scroll)
# -crf 28 = calidad media-baja (aceptable para background)
```

**Step 2: Reducir FPS del video**
```bash
# Convertir a 24fps (cine estándar)
ffmpeg -i input.mp4 -r 24 output.mp4
```

**Step 3: Verificar performance**
```bash
# Lighthouse > Performance > 90
# Revisar "Total Blocking Time" < 300ms
```

---

## 📕 RUNBOOK 4: Browser Compatibility

### Matriz de Soporte

| Feature | Chrome | Firefox | Safari | Edge |
|---------|--------|---------|--------|------|
| Video autoplay | ✅ | ✅ | ✅ | ✅ |
| playsInline | ✅ | ✅ | ✅ | ✅ |
| IntersectionObserver | ✅ | ✅ | ✅ | ✅ |
| will-change | ✅ | ✅ | ✅ | ✅ |
| backdrop-blur | ✅ | ✅ | ✅ | ✅ |

### Fallbacks por Browser

**Safari < 14:**
```css
/* Fallback si backdrop-blur no funciona */
.hero-overlay {
  background: rgba(0, 0, 0, 0.5); /* Fallback sólido */
  -webkit-backdrop-filter: blur(10px); /* Old Safari */
}
```

**Firefox < 70:**
```css
/* will-change fallback */
.hero-video {
  transform: translateZ(0); /* Force GPU */
}
```

---

## 📕 RUNBOOK 5: Optimización de Videos

### Comandos FFmpeg de Emergencia

**Compresión máxima (para lento connection)**
```bash
ffmpeg -i input.mp4 \
  -vcodec libx264 -crf 30 -preset veryfast \
  -vf scale=1280:720 \
  -an -movflags +faststart \
  output-small.mp4
```

**Calidad alta (para desktop)**
```bash
ffmpeg -i input.mp4 \
  -vcodec libx264 -crf 22 -preset slow \
  -vf scale=1920:1080 \
  -acodec aac -b:a 128k \
  -movflags +faststart \
  output-hd.mp4
```

**Generar WebM (Chrome moderno)**
```bash
ffmpeg -i input.mp4 \
  -codec:v libvpx-vp9 -crf 30 -b:v 0 \
  -vf scale=1920:1080 \
  -codec:a libopus -b:a 64k \
  output.webm
```

### Checklist de Optimización
- [ ] Video < 5MB para hero
- [ ] Video < 3MB para scroll (sin audio)
- [ ] Poster < 200KB
- [ ] Formato: MP4 (H.264)
- [ ] Sin audio innecesario
- [ ] `movflags +faststart` para streaming

---

## 📕 RUNBOOK 6: Deployment Vercel - Fallback

### Si el deployment falla

**Error: "Function Span Limit Exceeded"**
```bash
# Reducir tamaño del video antes de subir
# Verificar con:
ls -lh public/videos/
```

**Error: Video no carga en producción**
```bash
# Verificar que el video está en la carpeta correcta
# Debe estar en: /public/videos/home-exploding.mp4

# Verificar en Vercel Dashboard:
# Settings > General > Build & Development Settings
# Output Directory: .next (para Next.js)
```

**Error: 404 en video**
```bash
# Verificar ruta correcta en componente
# Debe ser: src="/videos/home-exploding.mp4"
# NO: src="./videos/..." o src="../videos/..."
```

---

## 📕 RUNBOOK 7: Testing Cross-Device

### Lista de Dispositivos de Prueba

| Dispositivo | Resolución | Browser | Prioridad |
|-------------|------------|---------|-----------|
| iPhone 14 | 390x844 | Safari | 🔴 Alta |
| iPhone SE | 375x667 | Safari | 🟡 Media |
| Pixel 7 | 412x915 | Chrome | 🔴 Alta |
| Samsung S23 | 360x780 | Chrome | 🟡 Media |
| iPad Pro | 1024x1366 | Safari | 🟡 Media |
| Desktop HD | 1920x1080 | Chrome | 🔴 Alta |
| Desktop HD | 1920x1080 | Firefox | 🟡 Media |
| Desktop HD | 1920x1080 | Safari | 🟡 Media |

### Checklist de Testing
- [ ] Video reproduce automáticamente en todos
- [ ] Texto legible en el hero
- [ ] Scroll video sincronizado en mobile
- [ ] No hay lag en scroll (verificar con lighthouse)
- [ ] Formato responsive (no cortado en mobile)

---

## 📕 RUNBOOK 8: Rollback Procedure

### Si algo sale mal después del deployment

**Step 1: Revertir a versión anterior**
```bash
# En Vercel Dashboard
# Deploys > Click en deploy anterior > "Promote to Production"
```

**Step 2: Verificar videos locales**
```bash
# Asegurar que videos existen en public/videos/
ls -la public/videos/
```

**Step 3: Emergency - Quitar video y usar imagen**
```tsx
// Cambiar temporalmente en HeroSection.tsx
<div className="absolute top-0 left-0 w-full h-full bg-cover bg-center" 
     style={{ backgroundImage: 'url(/images/hero-fallback.jpg)' }} />
```

---

## 📊 RESUMEN: Quick Reference

| Problema | Solución | Runbook |
|----------|----------|---------|
| Video no carga | Usar poster fallback | #1 |
| Autoplay falla | Muted + playsInline | #2 |
| Scroll lag | Comprimir + throttle | #3 |
| Browser old | CSS fallbacks | #4 |
| Deployment fail | Verificar rutas | #6 |
| Todo falla | Rollback | #8 |

---

*Runbooks actualizados: 2026-04-06*
*Proyecto: OIM Website SOTA*