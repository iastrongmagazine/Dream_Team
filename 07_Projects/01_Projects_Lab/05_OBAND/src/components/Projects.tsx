"use client";

import { motion } from "framer-motion";
import Image from "next/image";
import { ArrowUpRight, MapPin, Calendar } from "lucide-react";

interface Project {
  id: number;
  title: string;
  location: string;
  year: string;
  image: string;
  tags: string[];
}

const PROJECTS: Project[] = [
  {
    id: 1,
    title: "Corporate Headquarters",
    location: "Atlanta, GA",
    year: "2024",
    image: "https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&q=80&w=800",
    tags: ["Office", "15,000 sqft", "Enterprise"]
  },
  {
    id: 2,
    title: "Tech Campus Expansion",
    location: "Alpharetta, GA",
    year: "2024",
    image: "https://images.unsplash.com/photo-1497366811353-6870744d04b2?auto=format&fit=crop&q=80&w=800",
    tags: ["Open Space", "8,500 sqft", "Technology"]
  },
  {
    id: 3,
    title: "Financial Center Renovation",
    location: "Midtown Atlanta",
    year: "2023",
    image: "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&q=80&w=800",
    tags: ["Restructuring", "12,000 sqft", "Finance"]
  },
  {
    id: 4,
    title: "Healthcare Corp HQ",
    location: "Atlanta Perimeter",
    year: "2023",
    image: "https://images.unsplash.com/photo-1497215842964-222b430dc094?auto=format&fit=crop&q=80&w=800",
    tags: ["Corporate", "10,000 sqft", "Healthcare"]
  },
  {
    id: 5,
    title: "Law Firm Office",
    location: "Buckhead, Atlanta",
    year: "2024",
    image: "https://images.unsplash.com/photo-1462826303086-329426d1aef5?auto=format&fit=crop&q=80&w=800",
    tags: ["Traditional", "6,000 sqft", "Legal"]
  },
  {
    id: 6,
    title: "Startup Innovation Hub",
    location: "Atlanta Tech Village",
    year: "2024",
    image: "https://images.unsplash.com/photo-1527192491265-7e15c55b1ed2?auto=format&fit=crop&q=80&w=800",
    tags: ["Modern", "4,500 sqft", "Startup"]
  }
];

const springTransition = {
  type: "spring" as const,
  stiffness: 300,
  damping: 30,
};

export default function Projects() {
  return (
    <section id="proyectos" className="w-full py-32 px-6 md:px-8 max-w-7xl mx-auto">
      <div className="flex flex-col md:flex-row items-end justify-between mb-20 gap-8">
        <div className="max-w-2xl">
          <h2 className="text-4xl md:text-6xl font-bold tracking-tighter font-heading mb-6">
            Proyectos Recientes
          </h2>
          <p className="text-muted text-lg leading-relaxed font-light">
            Una seleccion curada de proyectos de amueblamiento corporativo ejecutados con precision 
            e ingenieria de primer nivel. Cada espacio transformado es una oportunidad de excelencia.
          </p>
        </div>
        <button 
          type="button"
          className="text-sm font-bold uppercase tracking-widest border-b border-accent pb-1 text-accent transition-all hover:pr-4 cursor-pointer"
        >
          Ver Todos los Proyectos
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        {PROJECTS.map((project, i) => (
          <motion.div 
            key={project.id}
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ ...springTransition, duration: 0.8, delay: i * 0.1 }}
            className="group relative flex flex-col gap-6 cursor-pointer"
          >
            <div className="relative aspect-[4/3] overflow-hidden rounded-3xl glass border border-glass-border">
              <div className="absolute inset-0 bg-gradient-to-br from-accent/10 to-transparent transition-opacity group-hover:opacity-0 z-10" />
              <Image 
                src={project.image} 
                alt={project.title}
                fill
                sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
                className="object-cover grayscale opacity-40 group-hover:grayscale-0 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700"
                loading={i === 0 ? "eager" : "lazy"}
                decoding="async"
                priority={i === 0}
              />
              
              <div className="absolute top-6 right-6 flex gap-2">
                <div className="p-3 rounded-full bg-black/40 backdrop-blur-md border border-white/10 opacity-0 transform translate-y-2 group-hover:opacity-100 group-hover:translate-y-0 transition-all duration-500 delay-100">
                  <ArrowUpRight className="w-4 h-4 text-white" />
                </div>
              </div>
            </div>

            <div className="px-2">
              <div className="flex flex-wrap gap-2 mb-4">
                {project.tags.map(tag => (
                  <span key={tag} className="text-[10px] font-bold uppercase tracking-widest px-2 py-1 glass border border-glass-border rounded-md text-neutral-400">
                    {tag}
                  </span>
                ))}
              </div>
              <h3 className="text-2xl font-bold mb-2 font-heading">{project.title}</h3>
              <div className="flex items-center gap-4 text-sm text-muted">
                <span className="flex items-center gap-1">
                  <MapPin className="w-3 h-3" />
                  {project.location}
                </span>
                <span className="flex items-center gap-1">
                  <Calendar className="w-3 h-3" />
                  {project.year}
                </span>
              </div>
            </div>
          </motion.div>
        ))}
      </div>
    </section>
  );
}
