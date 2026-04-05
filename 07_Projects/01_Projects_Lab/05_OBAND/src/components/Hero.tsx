"use client";

import { motion } from "framer-motion";
import { ArrowRight, Factory } from "lucide-react";

const springTransition = {
  type: "spring" as const,
  stiffness: 300,
  damping: 30,
};

export default function Hero() {
  return (
    <section className="relative min-h-screen flex flex-col items-center justify-center px-6 pt-32 pb-20 text-white overflow-hidden">
      {/* Hero Content */}
      <div className="z-10 max-w-5xl w-full flex flex-col items-center text-center space-y-8">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ ...springTransition, duration: 0.8 }}
          className="flex items-center gap-2 px-4 py-2 rounded-full glass border border-glass-border backdrop-blur-md mb-4"
        >
          <Factory className="w-4 h-4 text-accent" />
          <span className="text-xs font-medium tracking-widest uppercase text-accent">
            Ingenieria de Espacios
          </span>
        </motion.div>

        <motion.h1 
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ ...springTransition, duration: 1, delay: 0.2 }}
          className="text-5xl md:text-8xl lg:text-9xl font-bold tracking-tighter font-heading"
        >
          Office <span className="text-accent underline decoration-accent/30 underline-offset-8">Installations</span>
          <br />
          <span className="text-4xl md:text-6xl lg:text-7xl">Mayen</span>
        </motion.h1>

        <motion.p
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ ...springTransition, duration: 1, delay: 0.5 }}
          className="max-w-2xl text-lg md:text-xl text-muted font-light leading-relaxed"
        >
          Expertos en amueblamiento y optimizacion de espacios corporativos. 
          Transformamos ambientes de trabajo en experiencias productivas y modernas.
        </motion.p>

        <motion.div 
          initial={{ opacity: 0, scale: 0.95 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ ...springTransition, duration: 0.8, delay: 0.8 }}
          className="flex flex-wrap items-center justify-center gap-4 mt-8"
        >
          <a 
            href="#proyectos" 
            className="px-10 py-5 bg-accent text-black font-extrabold rounded-2xl flex items-center gap-3 hover:bg-accent-hover transition-all transform hover:scale-105"
          >
            Ver Proyectos <ArrowRight className="w-5 h-5" />
          </a>
          
          <a 
            href="#contacto" 
            className="px-10 py-5 glass border border-glass-border rounded-2xl font-bold backdrop-blur-md hover:bg-glass-hover transition-all"
          >
            Contactar
          </a>
        </motion.div>
      </div>
    </section>
  );
}
