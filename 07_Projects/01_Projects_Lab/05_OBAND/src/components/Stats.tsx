"use client";

import { motion } from "framer-motion";
import { Building2, Users, Award, Clock } from "lucide-react";

const STATS = [
  { icon: Building2, value: "150+", label: "Proyectos Entregados" },
  { icon: Users, value: "8+", label: "Anos de Experiencia" },
  { icon: Award, value: "98%", label: "Satisfaccion del Cliente" },
  { icon: Clock, value: "500+", label: "Espacios Optimizados" },
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
  hidden: { opacity: 0, y: 20 },
  visible: { 
    opacity: 1, 
    y: 0,
    transition: { ...springTransition, duration: 0.6 }
  }
};

export default function Stats() {
  return (
    <section className="w-full py-20 px-6 md:px-12 lg:px-20 border-y border-white/5">
      <motion.div 
        variants={staggerChildren}
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true }}
        className="max-w-6xl mx-auto grid grid-cols-2 md:grid-cols-4 gap-8 md:gap-12"
      >
        {STATS.map((stat, index) => (
          <motion.div
            key={stat.label}
            variants={fadeInUp}
            className="flex flex-col items-start md:items-center"
          >
            <div className="flex items-center gap-3 mb-3">
              <stat.icon className="w-4 h-4 text-accent/60" />
              <span className="text-2xl md:text-3xl font-semibold text-white">
                {stat.value}
              </span>
            </div>
            <span className="text-xs text-neutral-500 tracking-wide">
              {stat.label}
            </span>
          </motion.div>
        ))}
      </motion.div>
    </section>
  );
}