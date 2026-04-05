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
    description: "Transporte, montje y configuracion de equipamiento con garantias de calidad.",
  },
];

const springTransition = {
  type: "spring" as const,
  stiffness: 300,
  damping: 30,
};

export default function Services() {
  return (
    <section id="servicios" className="w-full py-32 px-6 md:px-8 max-w-7xl mx-auto">
      <div className="flex flex-col md:flex-row items-end justify-between mb-20 gap-8">
        <div className="max-w-2xl">
          <h2 className="text-4xl md:text-6xl font-bold tracking-tighter font-heading mb-6">
            Nuestros Servicios
          </h2>
          <p className="text-muted text-lg leading-relaxed font-light">
            Soluciones integrales para la transformacion de espacios corporativos. 
            Cada servicio esta diseñado para entregar resultados que superan expectativas.
          </p>
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {SERVICES.map((service, i) => (
          <motion.div
            key={service.title}
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ ...springTransition, duration: 0.6, delay: i * 0.1 }}
            className="group p-8 rounded-3xl glass border border-glass-border hover:bg-glass-hover transition-all duration-300"
          >
            <div className="p-4 bg-accent/10 rounded-2xl w-fit mb-6 group-hover:bg-accent/20 transition-colors">
              <service.icon className="w-8 h-8 text-accent" />
            </div>
            <h3 className="text-xl font-bold mb-3 font-heading">{service.title}</h3>
            <p className="text-muted text-sm leading-relaxed">{service.description}</p>
          </motion.div>
        ))}
      </div>
    </section>
  );
}