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
    description: "Devoción total con cada cliente, desde la primera reunion hasta el seguimiento post-entrega.",
  },
  {
    icon: Lightbulb,
    title: "Innovacion",
    description: "Busqueda constante de soluciones nuevas que optimizen espacios y costos.",
  },
];

const BENEFITS = [
  "Custom designs tailored to company culture",
  "Premium materials with extended warranties",
  "Certified technical team with ongoing training",
  "AGILE project management methodology",
  "Post-installation support and maintenance",
];

const springTransition = {
  type: "spring" as const,
  stiffness: 300,
  damping: 30,
};

export default function About() {
  return (
    <section id="nosotros" className="w-full py-32 px-6 md:px-8 max-w-7xl mx-auto">
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24">
        {/* Left Column - Story */}
        <motion.div
          initial={{ opacity: 0, x: -20 }}
          whileInView={{ opacity: 1, x: 0 }}
          viewport={{ once: true }}
          transition={{ ...springTransition, duration: 0.8 }}
        >
          <h2 className="text-4xl md:text-6xl font-bold tracking-tighter font-heading mb-8">
            Ingenieria al Servicio de <span className="text-accent">Espacios</span>
          </h2>
          <div className="space-y-6 text-muted leading-relaxed">
            <p>
              OIM nacio con una vision clara: transformar la manera en que las empresas 
              habitan sus espacios de trabajo. Con mas de una decada de experiencia, 
              hemos evolucionado de ser un proveedor de mobiliario a convertirnos en 
              socios estratégicos de transformacion corporativa.
            </p>
            <p>
              Nuestra metodologia combina ingenieria estructural con diseño centrado 
              en el usuario. No amueblamos oficinas — creamos ecosistemas laborales 
              que potencian la productividad, el bienestar y la identidad organizacional.
            </p>
            <p>
              Cada proyecto es una oportunidad de demostrar que la excellence no es 
              un lujo, es un estandar.
            </p>
          </div>
        </motion.div>

        {/* Right Column - Values & Benefits */}
        <motion.div
          initial={{ opacity: 0, x: 20 }}
          whileInView={{ opacity: 1, x: 0 }}
          viewport={{ once: true }}
          transition={{ ...springTransition, duration: 0.8, delay: 0.2 }}
          className="space-y-10"
        >
          {/* Values */}
          <div className="space-y-6">
            <h3 className="text-2xl font-bold font-heading">Nuestros Pilares</h3>
            <div className="space-y-4">
              {VALUES.map((value, i) => (
                <motion.div
                  key={value.title}
                  initial={{ opacity: 0, y: 10 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ ...springTransition, duration: 0.5, delay: 0.3 + i * 0.1 }}
                  className="flex gap-4 p-4 rounded-2xl glass border border-glass-border"
                >
                  <div className="p-2 bg-accent/10 rounded-xl h-fit">
                    <value.icon className="w-5 h-5 text-accent" />
                  </div>
                  <div>
                    <h4 className="font-bold mb-1">{value.title}</h4>
                    <p className="text-sm text-muted">{value.description}</p>
                  </div>
                </motion.div>
              ))}
            </div>
          </div>

          {/* Benefits */}
          <div className="space-y-4">
            <h3 className="text-2xl font-bold font-heading">Por Que Elegirnos</h3>
            <ul className="space-y-3">
              {BENEFITS.map((benefit, i) => (
                <li key={i} className="flex items-start gap-3">
                  <CheckCircle2 className="w-5 h-5 text-accent flex-shrink-0 mt-0.5" />
                  <span className="text-muted">{benefit}</span>
                </li>
              ))}
            </ul>
          </div>
        </motion.div>
      </div>
    </section>
  );
}