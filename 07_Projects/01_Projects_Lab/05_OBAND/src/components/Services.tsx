"use client";

import { motion } from "framer-motion";
import { Sofa, Ruler, PenTool, Package } from "lucide-react";

const SERVICES = [
  {
    icon: Sofa,
    title: "Amueblamiento Corporativo",
    description: "Seleccion y suministro de mobiliario de alta calidad para espacios de trabajo modernos.",
  },
  {
    icon: Ruler,
    title: "Diseno de Espacios",
    description: "Planificacion y distribucion estrategica de ambientes corporativos maximizando productividad.",
  },
  {
    icon: PenTool,
    title: "Gestion de Proyectos",
    description: "Coordinacion integral desde la conceptualizacion hasta la instalacion final.",
  },
  {
    icon: Package,
    title: "Logistica e Instalacion",
    description: "Transporte, montaje y configuracion de equipamiento con garantias de calidad.",
  },
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
    transition: { staggerChildren: 0.1 }
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

export default function Services() {
  return (
    <section id="servicios" className="w-full py-24 md:py-32 px-6 md:px-12 lg:px-20 max-w-7xl mx-auto">
      {/* Section Header - Left aligned, minimal */}
      <motion.div 
        variants={staggerChildren}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
        className="mb-20"
      >
        <motion.div variants={fadeInUp} className="mb-4">
          <span className="text-xs font-medium tracking-widest text-neutral-500 uppercase">
            Servicios
          </span>
        </motion.div>
        <motion.h2 variants={fadeInUp} className="text-3xl md:text-5xl font-semibold tracking-tight text-white mb-6">
          Soluciones integrales
        </motion.h2>
        <motion.p variants={fadeInUp} className="max-w-xl text-neutral-400 leading-relaxed">
          Transformacion de espacios corporativos con resultados que superan expectativas.
        </motion.p>
      </motion.div>

      {/* Services - 2 column asymmetric grid (no 4-card layout) */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-16">
        {SERVICES.map((service, index) => (
          <motion.div
            key={service.title}
            variants={fadeInUp}
            initial="hidden"
            whileInView="visible"
            viewport={{ once: true }}
            transition={{ delay: index * 0.1 }}
            className="group"
          >
            <div className="flex items-start gap-6">
              <div className="flex-shrink-0 w-12 h-12 rounded-2xl bg-white/5 border border-white/10 flex items-center justify-center group-hover:bg-accent/10 group-hover:border-accent/30 transition-all duration-300">
                <service.icon className="w-5 h-5 text-neutral-400 group-hover:text-accent transition-colors" />
              </div>
              <div>
                <h3 className="text-lg font-medium text-white mb-2">{service.title}</h3>
                <p className="text-neutral-500 text-sm leading-relaxed max-w-sm">
                  {service.description}
                </p>
              </div>
            </div>
          </motion.div>
        ))}
      </div>
    </section>
  );
}