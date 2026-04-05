"use client";

import { motion } from "framer-motion";
import { CheckCircle2, Target, Heart, Lightbulb } from "lucide-react";

const VALUES = [
  {
    icon: Target,
    title: "Precision",
    description: "Cada proyecto se ejecuta con exactitud milimetrica y control de calidad riguroso.",
  },
  {
    icon: Heart,
    title: "Compromiso",
    description: "Devocion total con cada cliente, desde la primera reunion hasta el seguimiento post-entrega.",
  },
  {
    icon: Lightbulb,
    title: "Innovacion",
    description: "Busqueda constante de soluciones nuevas que optimizen espacios y costos.",
  },
];

const BENEFITS = [
  "Disenos personalizados adaptados a la cultura de la empresa",
  "Materiales premium con garantias extendidas",
  "Equipo tecnico certificado con capacitacion continua",
  "Gestion de proyectos AGILE",
  "Soporte y mantenimiento post-instalacion",
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

export default function About() {
  return (
    <section id="nosotros" className="w-full py-24 md:py-32 px-6 md:px-12 lg:px-20 max-w-7xl mx-auto">
      <motion.div 
        variants={staggerChildren}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
        className="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24"
      >
        {/* Left Column - Story */}
        <motion.div variants={fadeInUp}>
          <div className="mb-4">
            <span className="text-xs font-medium tracking-widest text-neutral-500 uppercase">
              Nosotros
            </span>
          </div>
          <h2 className="text-3xl md:text-5xl font-semibold tracking-tight text-white mb-8">
            Ingenieria al Servicio de <span className="text-accent">Espacios</span>
          </h2>
          <div className="space-y-6 text-neutral-400 leading-relaxed">
            <p>
              OIM nacio con una vision clara: transformar la manera en que las empresas 
              habitan sus espacios de trabajo. Con mas de una decada de experiencia, 
              hemos evolucionado de ser un proveedor de mobiliario a convertirnos en 
              socios estrategicos de transformacion corporativa.
            </p>
            <p>
              Nuestra metodologia combina ingenieria estructural con diseño centrado 
              en el usuario. No amueblamos oficinas creamos ecosistemas laborales 
              que potencian la productividad, el bienestar y la identidad organizacional.
            </p>
          </div>
        </motion.div>

        {/* Right Column - Values & Benefits */}
        <motion.div variants={fadeInUp} className="space-y-12">
          {/* Values - NO cards, just spacing */}
          <div className="space-y-8">
            <h3 className="text-lg font-medium text-white">Nuestros Pilares</h3>
            <div className="space-y-6">
              {VALUES.map((value, index) => (
                <motion.div
                  key={value.title}
                  initial={{ opacity: 0, x: 20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: index * 0.1, ...springTransition }}
                  className="flex items-start gap-4"
                >
                  <div className="flex-shrink-0 w-10 h-10 rounded-xl bg-white/5 flex items-center justify-center">
                    <value.icon className="w-4 h-4 text-accent/80" />
                  </div>
                  <div>
                    <h4 className="font-medium text-white mb-1">{value.title}</h4>
                    <p className="text-sm text-neutral-500">{value.description}</p>
                  </div>
                </motion.div>
              ))}
            </div>
          </div>

          {/* Benefits - NO cards, simple list with border-t */}
          <div className="space-y-4">
            <h3 className="text-lg font-medium text-white">Por Que Elegirnos</h3>
            <ul className="space-y-3">
              {BENEFITS.map((benefit, index) => (
                <li key={index} className="flex items-start gap-3 py-2 border-b border-white/5">
                  <CheckCircle2 className="w-4 h-4 text-accent/60 flex-shrink-0 mt-0.5" />
                  <span className="text-neutral-400 text-sm">{benefit}</span>
                </li>
              ))}
            </ul>
          </div>
        </motion.div>
      </motion.div>
    </section>
  );
}