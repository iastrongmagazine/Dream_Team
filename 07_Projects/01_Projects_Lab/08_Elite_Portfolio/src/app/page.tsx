import { Hero } from "@/components/hero";
import { Navigation } from "@/components/navigation";
import { ProjectsGrid } from "@/components/projects-grid";
import { AboutSection } from "@/components/about-section";
import { ContactSection } from "@/components/contact-section";
import { Footer } from "@/components/footer";

/**
 * HomePage - Server Component
 * SOTA Design per taste-skill
 * DESIGN_VARIANCE: 8 (Asymmetric, Artsy)
 * MOTION_INTENSITY: 6 (Framer Motion fluid)
 * VISUAL_DENSITY: 4 (Art Gallery/Airy)
 */
export default function HomePage() {
  return (
    <main className="min-h-screen bg-zinc-50 dark:bg-zinc-950">
      <Navigation />
      
      <Hero 
        name="Elena"
        role="Arquitecta y Diseñadora"
        tagline="Creando espacios que inspiran, funcionan y perduran en el tiempo."
      />
      
      <ProjectsGrid />
      
      <AboutSection />
      
      <ContactSection />
      
      <Footer />
    </main>
  );
}