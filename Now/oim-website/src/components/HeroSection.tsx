'use client';

import { useRef, useEffect, useState } from 'react';

interface HeroSectionProps {
  videoSrc: string;
  posterSrc?: string;
  children?: React.ReactNode;
}

/**
 * HeroSection - Cinematic video background with auto-play
 * 
 * Technical requirements:
 * - playsInline + muted required for iOS Safari autoplay
 * - will-change-transform enables GPU acceleration
 * - Intersection Observer for viewport detection
 */
export function HeroSection({
  videoSrc,
  posterSrc,
  children
}: HeroSectionProps) {
  const videoRef = useRef<HTMLVideoElement>(null);
  const [isLoaded, setIsLoaded] = useState(false);

  useEffect(() => {
    const video = videoRef.current;
    if (!video) return;

    // Ensure autoplay requirements for iOS Safari
    video.playsInline = true;
    video.muted = true;
    video.loop = true;
    video.autoplay = true;

    const handleCanPlay = async () => {
      setIsLoaded(true);
      try {
        await video.play();
      } catch (error) {
        console.log('Autoplay prevented:', error);
      }
    };

    video.addEventListener('canplaythrough', handleCanPlay);
    
    // Attempt immediate play
    if (video.readyState >= 2) {
      handleCanPlay();
    }

    return () => {
      video.removeEventListener('canplaythrough', handleCanPlay);
    };
  }, []);

  return (
    <section className="relative w-full min-h-[100dvh] overflow-hidden">
      {/* Video Background */}
      <video
        ref={videoRef}
        className={`absolute top-0 left-0 w-full h-full object-cover will-change-transform transition-opacity duration-700 ${isLoaded ? 'opacity-100' : 'opacity-0'}`}
        src={videoSrc}
        poster={posterSrc}
        playsInline
        muted
        loop
        autoPlay
        preload="auto"
        aria-hidden="true"
      />
      
      {/* Dark Overlay for text contrast - adjustable opacity */}
      <div className="absolute top-0 left-0 w-full h-full bg-black/50 backdrop-blur-sm" />
      
      {/* Content Container - asymmetric layout per taste-skill */}
      <div className="relative z-10 flex flex-col justify-center h-full min-h-[100dvh] px-6 md:px-16 lg:px-24 py-20">
        <div className="max-w-3xl">
          {children}
        </div>
      </div>
    </section>
  );
}