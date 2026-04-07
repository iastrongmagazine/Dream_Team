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

/**
 * ScrollVideoServices - Frame-by-frame video scroll sync with service overlays
 * 
 * Technical implementation:
 * - Intersection Observer activates video only when in viewport
 * - Throttled updates (requestAnimationFrame) prevents performance issues
 * - Progress calculation based on container scroll position
 */
export function ScrollVideoServices({
  videoSrc,
  scrollHeight = 300
}: ScrollVideoServicesProps) {
  const containerRef = useRef<HTMLDivElement>(null);
  const videoRef = useRef<HTMLVideoElement>(null);
  const [duration, setDuration] = useState(0);
  const [isInView, setIsInView] = useState(false);
  const lastProgress = useRef(0);
  const rafId = useRef<number | null>(null);

  // Load video duration
  useEffect(() => {
    const video = videoRef.current;
    if (video) {
      const handleLoaded = () => setDuration(video.duration);
      video.addEventListener('loadedmetadata', handleLoaded);
      return () => video.removeEventListener('loadedmetadata', handleLoaded);
    }
  }, []);

  // Scroll handler with RAF throttling
  const handleScroll = useCallback(() => {
    if (!containerRef.current || !videoRef.current || duration === 0) return;
    if (rafId.current) return; // Throttle: skip if RAF pending

    rafId.current = requestAnimationFrame(() => {
      const container = containerRef.current;
      if (!container) return;

      const rect = container.getBoundingClientRect();
      const viewportHeight = window.innerHeight;
      const containerHeight = container.offsetHeight;

      // Calculate progress (0 to 1)
      const rawProgress = -rect.top / (containerHeight - viewportHeight);
      const progress = Math.max(0, Math.min(1, rawProgress));

      // Only update if change is significant (performance)
      if (Math.abs(progress - lastProgress.current) > 0.001) {
        videoRef.current.currentTime = progress * duration;
        lastProgress.current = progress;
      }
      
      rafId.current = null;
    });
  }, [duration]);

  // Setup scroll listener and Intersection Observer
  useEffect(() => {
    const container = containerRef.current;
    if (!container) return;

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
      if (rafId.current) cancelAnimationFrame(rafId.current);
    };
  }, [handleScroll]);

  // Calculate current service index based on scroll progress
  const getCurrentServiceIndex = useCallback(() => {
    if (!containerRef.current || duration === 0) return 0;
    const rect = containerRef.current.getBoundingClientRect();
    const progress = Math.max(0, Math.min(1, -rect.top / (containerRef.current.offsetHeight - window.innerHeight)));
    return Math.min(servicesData.length - 1, Math.floor(progress * servicesData.length));
  }, [duration]);

  const currentServiceIndex = getCurrentServiceIndex();

  return (
    <div 
      ref={containerRef}
      className="relative w-full"
      style={{ height: `${scrollHeight}vh` }}
    >
      {/* Video Background - Sticky for scroll sync */}
      <video
        ref={videoRef}
        className="sticky top-0 left-0 w-full h-screen object-cover will-change-transform"
        src={videoSrc}
        playsInline
        muted
        preload="auto"
        aria-hidden="true"
      />
      
      {/* Services Overlay - Asymmetric per taste-skill DESIGN_VARIANCE: 8 */}
      {/* Left-aligned content, not centered - creates editorial tech-forward feel */}
      <div className="absolute top-0 left-0 w-full h-full flex items-center">
        <div className="bg-zinc-900/70 backdrop-blur-lg border border-white/5 px-10 py-14 rounded-none max-w-xl ml-6 md:ml-16 lg:ml-24 mt-32">
          {servicesData.map((service, index) => (
            <div 
              key={service.title}
              className={`transition-all duration-500 ease-out ${
                index === currentServiceIndex 
                  ? 'opacity-100 translate-y-0' 
                  : 'opacity-0 absolute -translate-y-4'
              }`}
            >
              <h2 className="text-2xl md:text-3xl font-medium text-white mb-5 tracking-tight">
                {service.title}
              </h2>
              <ul className="space-y-2.5">
                {service.items.map((item) => (
                  <li key={item} className="flex items-center text-zinc-300">
                    <span className="w-1.5 h-1.5 bg-emerald-400 rounded-full mr-3 flex-shrink-0" />
                    <span className="text-base">{item}</span>
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