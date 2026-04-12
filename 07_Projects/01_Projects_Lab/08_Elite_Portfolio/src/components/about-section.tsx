"use client";

import { motion, useScroll, useTransform } from "framer-motion";
import { useRef } from "react";

const stats = [
  { value: "12+", label: "Años de Experiencia" },
  { value: "47", label: "Proyectos Completados" },
  { value: "23", label: "Clientes Felices" },
  { value: "4", label: "Premios de Diseño" },
];

const highlights = [
  "Diseño residencial de lujo",
  "Espacios comerciales innovadores",
  "Renovaciones patrimoniales",
  "Consultoría arquitectónica",
];

/**
 * AboutSection - SOTA Design per taste-skill
 * Split 2-column layout (DESIGN_VARIANCE: 8), stats 2x2 grid
 */
export function AboutSection() {
  const containerRef = useRef<HTMLDivElement>(null);
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start end", "end start"],
  });

  // Parallax for image
  const y = useTransform(scrollYProgress, [0, 1], [50, -50]);

  return (
    <section id="about" className="py-24 md:py-32 bg-zinc-100 dark:bg-zinc-900">
      <div ref={containerRef} className="container-premium">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-16 items-center">
          {/* Left column - Image (5 columns) */}
          <motion.div
            className="lg:col-span-5"
            initial={{ opacity: 0, x: -40 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-100px" }}
            transition={{ duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
          >
            <div className="relative">
              {/* Main image - asymmetric */}
              <motion.div className="relative aspect-[4/5] rounded-[2.5rem] overflow-hidden">
                <img
                  src="https://picsum.photos/seed/about1/800/1000"
                  alt="Arquitecta profesional"
                  className="w-full h-full object-cover"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-zinc-900/40 via-transparent to-transparent" />
              </motion.div>

              {/* Offset decorative element */}
              <motion.div
                className="absolute -bottom-6 -right-6 w-2/3 h-2/3 rounded-[2rem] border-2 border-emerald-500/30 -z-10"
                style={{ y }}
              />

              {/* Floating stat card - glassmorphism */}
              <motion.div
                className="absolute -bottom-4 -left-4 md:-left-8 p-6 rounded-[1.5rem] bg-zinc-50/90 dark:bg-zinc-800/90 backdrop-blur-xl border border-white/20 dark:border-white/10 shadow-xl"
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: 0.4, duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
              >
                <p className="font-display text-4xl font-semibold text-emerald-600 dark:text-emerald-400">
                  12+
                </p>
                <p className="font-body text-sm text-zinc-500 dark:text-zinc-400">
                  Años de experiencia
                </p>
              </motion.div>
            </div>
          </motion.div>

          {/* Right column - Content (7 columns) */}
          <motion.div
            className="lg:col-span-7"
            initial={{ opacity: 0, x: 40 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true, margin: "-100px" }}
            transition={{ duration: 0.8, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
          >
            {/* Section label */}
            <p className="font-body text-sm tracking-[0.2em] uppercase text-emerald-600 dark:text-emerald-400 mb-4">
              Sobre Mí
            </p>

            {/* Heading */}
            <h2 className="font-display text-4xl md:text-5xl lg:text-6xl font-semibold tracking-tight text-zinc-900 dark:text-zinc-50 mb-6">
              Creando espacios que{" "}
              <span className="text-emerald-600 dark:text-emerald-400">
                inspiran
              </span>
            </h2>

            {/* Description */}
            <div className="space-y-4 mb-10">
              <p className="font-body text-lg text-zinc-600 dark:text-zinc-300 leading-relaxed">
                Mi enfoque combina la funcionalidad con la estética, creando espacios que 
                cuentan historias y responden a las necesidades reales de quienes los habitan.
              </p>
              <p className="font-body text-lg text-zinc-600 dark:text-zinc-300 leading-relaxed">
                Cada proyecto es una oportunidad para transformar visiónes en realidades 
                tangibles, donde cada detalle está pensado para generar bienestar y personalidad.
              </p>
            </div>

            {/* Stats grid - 2x2 */}
            <div className="grid grid-cols-2 gap-4 mb-10">
              {stats.map((stat, i) => (
                <motion.div
                  key={stat.label}
                  className="p-6 rounded-[1.5rem] bg-zinc-50 dark:bg-zinc-800 border border-zinc-200 dark:border-zinc-700"
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: 0.3 + i * 0.1, duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
                >
                  <p className="font-display text-3xl font-semibold text-zinc-900 dark:text-zinc-50 mb-1">
                    {stat.value}
                  </p>
                  <p className="font-body text-sm text-zinc-500 dark:text-zinc-400">
                    {stat.label}
                  </p>
                </motion.div>
              ))}
            </div>

            {/* Highlights - vertical list */}
            <div className="space-y-3">
              {highlights.map((highlight, i) => (
                <motion.div
                  key={highlight}
                  className="flex items-center gap-3"
                  initial={{ opacity: 0, x: 20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: 0.6 + i * 0.1, duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
                >
                  <span className="w-2 h-2 rounded-full bg-emerald-500" />
                  <span className="font-body text-zinc-600 dark:text-zinc-300">
                    {highlight}
                  </span>
                </motion.div>
              ))}
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
}