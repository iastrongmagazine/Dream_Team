import { HeroSection } from '@/components/HeroSection';
import { ScrollVideoServices } from '@/components/ScrollVideoServices';

/**
 * OIM Website - Office Installations Mayen
 * 
 * SOTA website with:
 * - Cinematic video hero with auto-play
 * - Frame-by-frame scroll video sync
 * - "Editorial Tech-Forward Light Theme" per taste-skill
 * 
 * DESIGN_VARIANCE: 8 (Asymmetric layout)
 * MOTION_INTENSITY: 6 (Fluid CSS animations)
 * VISUAL_DENSITY: 4 (Art Gallery mode - spacious)
 */
export default function Home() {
  return (
    <main className="flex flex-col">
      {/* Hero Section - Video Background - Asymmetric per taste-skill */}
      <HeroSection videoSrc="/videos/home-exploding.mp4">
        <div className="max-w-xl">
          <h1 className="text-4xl md:text-5xl lg:text-6xl font-semibold text-white mb-6 tracking-tight leading-[1.1]">
            Professional Office Furniture Installation in Atlanta
          </h1>
          <p className="text-lg md:text-xl text-white/80 mb-8 max-w-lg leading-relaxed">
            Since 2018, providing reliable, high-quality furniture assembly and relocation services for businesses across Georgia.
          </p>
          <button className="px-8 py-4 bg-white text-zinc-950 rounded-full text-base font-medium hover:bg-white/90 transition-all active:scale-[0.98]">
            Get a Free Quote
          </button>
        </div>
      </HeroSection>

      {/* Scroll Video Services Section */}
      <ScrollVideoServices 
        videoSrc="/videos/home-exploding.mp4"
        scrollHeight={300}
      />
    </main>
  );
}