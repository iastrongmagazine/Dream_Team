"use client";

import { motion } from "framer-motion";
import { ArrowUpRight } from "@phosphor-icons/react";

interface Project {
  id: string;
  title: string;
  category: string;
  description: string;
  image: string;
}

const projects: Project[] = [
  {
    id: "1",
    title: "Residencia Moderna",
    category: "Arquitectura Residencial",
    description: "Diseño integral de vivienda unifamiliar con énfasis en espacios abiertos y conexión con la naturaleza.",
    image: "https://picsum.photos/seed/proj1/800/1000",
  },
  {
    id: "2",
    title: "Espacio Corporativo",
    category: "Diseño de Interiores",
    description: "Ambientación de oficinas empresariales con áreas de trabajo colaborativo y zonas de descanso.",
    image: "https://picsum.photos/seed/proj2/800/600",
  },
  {
    id: "3",
    title: "Villa Costera",
    category: "Arquitectura Residencial",
    description: "Residencia de lujo con vistas panorámicas al mar, diseñada para maximizar la iluminación natural.",
    image: "https://picsum.photos/seed/proj3/800/800",
  },
  {
    id: "4",
    title: "Loft Urbano",
    category: "Diseño de Interiores",
    description: "Renovación de espacio industrial convertido en vivienda contemporánea de estilo minimalista.",
    image: "https://picsum.photos/seed/proj4/800/1200",
  },
  {
    id: "5",
    title: "Jardín Zen",
    category: "Paisajismo",
    description: "Diseño de espacio exterior inspirado en la filosofía zen japonesa con vegetación nativa.",
    image: "https://picsum.photos/seed/proj5/800/600",
  },
];

const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.15,
    },
  },
};

const itemVariants = {
  hidden: { opacity: 0, y: 40 },
  visible: {
    opacity: 1,
    y: 0,
    transition: {
      duration: 0.6,
      ease: [0.16, 1, 0.3, 1],
    },
  },
};

/**
 * ProjectsGrid - SOTA Design per taste-skill
 * Asymmetric grid (DESIGN_VARIANCE: 8), no 3-column layouts
 */
export function ProjectsGrid() {
  return (
    <section id="work" className="py-24 md:py-32 bg-zinc-50 dark:bg-zinc-950">
      <div className="container-premium">
        {/* Section header - left aligned, NOT centered */}
        <motion.div
          className="mb-16 md:mb-24"
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: "-100px" }}
          transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
        >
          <p className="font-body text-sm tracking-[0.2em] uppercase text-emerald-600 dark:text-emerald-400 mb-4">
            Portafolio
          </p>
          <h2 className="font-display text-4xl md:text-5xl lg:text-6xl font-semibold tracking-tight text-zinc-900 dark:text-zinc-50 mb-6">
            Proyectos Destacados
          </h2>
          <p className="font-body text-lg text-zinc-500 dark:text-zinc-400 max-w-xl leading-relaxed">
            Una selección de trabajos que representan mi visión de diseño: espacios que inspiran, funcionan y perduran.
          </p>
        </motion.div>

        {/* Asymmetric grid - 7+5+12 pattern (DESIGN_VARIANCE: 8) */}
        <motion.div
          className="grid grid-cols-1 md:grid-cols-12 gap-6 md:gap-8"
          variants={containerVariants}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: "-50px" }}
        >
          {/* Project 1 - Large (7 columns) */}
          <motion.div
            className="md:col-span-7"
            variants={itemVariants}
          >
            <ProjectCard project={projects[0]} size="large" />
          </motion.div>

          {/* Project 2 - Medium (5 columns) */}
          <motion.div
            className="md:col-span-5"
            variants={itemVariants}
          >
            <ProjectCard project={projects[1]} size="medium" />
          </motion.div>

          {/* Project 3 - Medium (5 columns) */}
          <motion.div
            className="md:col-span-5"
            variants={itemVariants}
          >
            <ProjectCard project={projects[2]} size="medium" />
          </motion.div>

          {/* Project 4 - Large (7 columns) */}
          <motion.div
            className="md:col-span-7"
            variants={itemVariants}
          >
            <ProjectCard project={projects[3]} size="large" />
          </motion.div>

          {/* Project 5 - Full width */}
          <motion.div
            className="md:col-span-12"
            variants={itemVariants}
          >
            <ProjectCard project={projects[4]} size="wide" />
          </motion.div>
        </motion.div>
      </div>
    </section>
  );
}

/**
 * ProjectCard - Individual project component
 * Glassmorphism hover, magnetic button
 */
function ProjectCard({ project, size }: { project: Project; size: "large" | "medium" | "wide" }) {
  const sizeClasses = {
    large: "aspect-[7/8]",
    medium: "aspect-square",
    wide: "aspect-[16/9]",
  };

  return (
    <motion.div
      className={`group relative ${sizeClasses[size]} overflow-hidden rounded-[2rem] cursor-pointer`}
      whileHover={{ scale: 0.99 }}
      transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
    >
      {/* Image */}
      <img
        src={project.image}
        alt={project.title}
        className="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105"
      />

      {/* Gradient overlay */}
      <div className="absolute inset-0 bg-gradient-to-t from-zinc-900/90 via-zinc-900/30 to-transparent" />

      {/* Content - positioned bottom left */}
      <div className="absolute inset-0 p-6 md:p-8 flex flex-col justify-end">
        {/* Category - uppercase tracking */}
        <motion.p
          className="font-body text-xs tracking-[0.2em] uppercase text-emerald-400 mb-2"
          initial={{ opacity: 0, y: 10 }}
          whileHover={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.3 }}
        >
          {project.category}
        </motion.p>

        {/* Title */}
        <h3 className="font-display text-2xl md:text-3xl font-semibold text-white mb-2">
          {project.title}
        </h3>

        {/* Description - visible on hover */}
        <motion.p
          className="font-body text-sm text-zinc-300 max-w-sm mb-4"
          initial={{ opacity: 0, y: 10 }}
          whileHover={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.3, delay: 0.1 }}
        >
          {project.description}
        </motion.p>

        {/* Arrow button - appears on hover */}
        <motion.div
          className="inline-flex"
          initial={{ opacity: 0, scale: 0.8 }}
          whileHover={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.3, delay: 0.2 }}
        >
          <span className="inline-flex items-center justify-center w-10 h-10 rounded-full bg-white/20 backdrop-blur-sm border border-white/30 text-white hover:bg-emerald-500 hover:border-emerald-500 transition-colors">
            <ArrowUpRight weight="bold" className="w-5 h-5" />
          </span>
        </motion.div>
      </div>

      {/* Glassmorphism border on hover */}
      <div className="absolute inset-0 rounded-[2rem] border border-white/0 group-hover:border-white/20 transition-colors duration-500 pointer-events-none" />
    </motion.div>
  );
}