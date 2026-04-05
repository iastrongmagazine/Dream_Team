"use client";

import { motion } from "framer-motion";
import Image from "next/image";
import { MapPin, Calendar } from "lucide-react";

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
  stiffness: 100,
  damping: 20,
};

const staggerChildren = {
  hidden: { opacity: 0 },
  visible: { 
    opacity: 1,
    transition: { staggerChildren: 0.12 }
  }
};

const fadeInUp = {
  hidden: { opacity: 0, y: 40 },
  visible: { 
    opacity: 1, 
    y: 0,
    transition: { ...springTransition, duration: 0.8 }
  }
};

export default function Projects() {
  return (
    <section id="proyectos" className="w-full py-24 md:py-32 px-6 md:px-12 lg:px-20 max-w-7xl mx-auto">
      {/* Section Header - minimal, left aligned */}
      <motion.div 
        variants={staggerChildren}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
        className="mb-16 md:mb-24"
      >
        <motion.div variants={fadeInUp} className="mb-4">
          <span className="text-xs font-medium tracking-widest text-neutral-500 uppercase">
            Proyectos
          </span>
        </motion.div>
        <motion.h2 variants={fadeInUp} className="text-3xl md:text-5xl font-semibold tracking-tight text-white mb-6">
          Trabajos recientes
        </motion.h2>
        <motion.p variants={fadeInUp} className="max-w-xl text-neutral-400 leading-relaxed">
          Proyectos de amueblamiento corporativo ejecutados con precision e ingenieria de primer nivel.
        </motion.p>
      </motion.div>

      {/* Asymmetric Grid - NO 3-column card layout */}
      <motion.div 
        variants={staggerChildren}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
        className="grid grid-cols-1 md:grid-cols-12 gap-6 md:gap-8"
      >
        {PROJECTS.map((project, index) => (
          <motion.div
            key={project.id}
            variants={fadeInUp}
            className={`group relative cursor-pointer ${
              // Asymmetric layout: first 2 items span 7 cols, next 2 span 5 cols
              index < 2 
                ? 'md:col-span-7' 
                : index < 4 
                  ? 'md:col-span-5' 
                  : 'md:col-span-6'
            }`}
          >
            <div className="relative aspect-[16/10] md:aspect-[4/3] overflow-hidden rounded-2xl bg-white/5">
              <Image 
                src={project.image} 
                alt={project.title}
                fill
                sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
                className="object-cover opacity-60 group-hover:opacity-100 group-hover:scale-105 transition-all duration-700"
                loading={index < 2 ? "eager" : "lazy"}
              />
              {/* Minimal overlay on hover */}
              <div className="absolute inset-0 bg-gradient-to-t from-black/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
            </div>

            {/* Content below image - no cards, just spacing */}
            <div className="mt-4 md:mt-6">
              <h3 className="text-lg md:text-xl font-medium text-white mb-2">{project.title}</h3>
              <div className="flex items-center gap-4 text-xs text-neutral-500">
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
      </motion.div>
    </section>
  );
}
