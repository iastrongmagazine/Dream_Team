"use client";

import { motion } from "framer-motion";
import { ArrowRight, ArrowDown } from "lucide-react";

const springTransition = {
  type: "spring" as const,
  stiffness: 100,
  damping: 20,
};

const staggerChildren = {
  hidden: { opacity: 0 },
  visible: { 
    opacity: 1,
    transition: { staggerChildren: 0.15 }
  }
};

const fadeInUp = {
  hidden: { opacity: 0, y: 30 },
  visible: { 
    opacity: 1, 
    y: 0,
    transition: { ...springTransition, duration: 0.8 }
  }
};

export default function Hero() {
  return (
    <section className="relative min-h-[100dvh] flex flex-col justify-center px-6 md:px-12 lg:px-20 pt-32 pb-20 text-white overflow-hidden">
      {/* Decorative minimal elements */}
      <div className="absolute top-40 right-10 w-64 h-64 bg-accent/5 rounded-full blur-3xl pointer-events-none" />
      <div className="absolute bottom-20 left-20 w-48 h-48 bg-accent/3 rounded-full blur-2xl pointer-events-none" />
      
      {/* Hero Content - Left aligned with asymmetric spacing */}
      <motion.div 
        variants={staggerChildren}
        initial="hidden"
        animate="visible"
        className="max-w-4xl w-full"
      >
        <motion.div variants={fadeInUp} className="mb-6">
          <span className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/5 border border-white/10 text-xs font-medium tracking-wide text-neutral-400">
            <span className="w-1.5 h-1.5 rounded-full bg-accent animate-pulse" />
            Ingenieria de Espacios
          </span>
        </motion.div>

        <motion.h1 
          variants={fadeInUp}
          className="text-4xl md:text-6xl lg:text-7xl font-semibold tracking-tight leading-[1.1] mb-8"
        >
          Office <span className="text-accent">Installations</span>
          <br />
          <span className="text-3xl md:text-5xl lg:text-6xl text-neutral-400">Mayen</span>
        </motion.h1>

        <motion.p
          variants={fadeInUp}
          className="max-w-xl text-lg md:text-xl text-neutral-400 leading-relaxed mb-10"
        >
          Expertos en amueblamiento y optimizacion de espacios corporativos. 
          Transformamos ambientes de trabajo en experiencias productivas y modernas.
        </motion.p>

        <motion.div 
          variants={fadeInUp}
          className="flex flex-wrap gap-4"
        >
          <a 
            href="#proyectos" 
            className="inline-flex items-center gap-2 px-8 py-4 bg-accent text-black font-semibold rounded-full hover:bg-accent-hover transition-all duration-300 active:scale-[0.98]"
          >
            Ver Proyectos <ArrowRight className="w-4 h-4" />
          </a>
          
          <a 
            href="#contacto" 
            className="inline-flex items-center gap-2 px-8 py-4 bg-white/5 border border-white/10 rounded-full font-medium text-white/80 hover:bg-white/10 hover:text-white transition-all duration-300"
          >
            Contactar
          </a>
        </motion.div>
      </motion.div>

      {/* Scroll indicator - minimal */}
      <motion.div 
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1.5, duration: 0.8 }}
        className="absolute bottom-10 left-1/2 -translate-x-1/2 flex flex-col items-center gap-2 text-neutral-500"
      >
        <span className="text-xs tracking-widest">SCROLL</span>
        <motion.div
          animate={{ y: [0, 8, 0] }}
          transition={{ repeat: Infinity, duration: 2, ease: "easeInOut" }}
        >
          <ArrowDown className="w-4 h-4" />
        </motion.div>
      </motion.div>
    </section>
  );
}
