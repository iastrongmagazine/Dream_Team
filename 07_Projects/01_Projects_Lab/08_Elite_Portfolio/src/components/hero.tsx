"use client";

import { motion, useScroll, useTransform, useSpring } from "framer-motion";
import { ArrowRight, ArrowDown } from "phosphor-react";

interface HeroProps {
  name: string;
  role: string;
  tagline?: string;
  onScrollToWork?: () => void;
}

/**
 * Hero Component - SOTA Design per taste-skill
 * DESIGN_VARIANCE: 8 (Asymmetric, Artsy)
 * MOTION_INTENSITY: 6 (Framer Motion fluid)
 * VISUAL_DENSITY: 4 (Art Gallery/Airy)
 */
export function Hero({ name, role, tagline, onScrollToWork }: HeroProps) {
  const { scrollY } = useScroll();

  // Parallax effects
  const y1 = useTransform(scrollY, [0, 500], [0, 200]);
  const y2 = useTransform(scrollY, [0, 500], [0, 120]);
  const opacity = useTransform(scrollY, [0, 400], [1, 0]);
  const scale = useTransform(scrollY, [0, 400], [1, 0.92]);

  // Spring physics for scroll indicator
  const scrollYSpring = useSpring(scrollY, { stiffness: 100, damping: 30 });

  // Split name into letters for stagger reveal
  const nameLetters = name.split("");

  return (
    <section className="relative min-h-[100dvh] flex items-center overflow-hidden">
      {/* Background - Zinc base, NO pure black */}
      <motion.div 
        className="absolute inset-0 bg-zinc-50 dark:bg-zinc-950"
        style={{ y: y1 }}
      />

      {/* Ambient orbs - Emerald accent, desaturated */}
      <motion.div 
        className="absolute top-[20%] -left-[10%] w-[600px] h-[600px] bg-emerald-500/5 rounded-full blur-3xl"
        animate={{
          x: [0, 80, 0],
          y: [0, 40, 0],
        }}
        transition={{
          duration: 25,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />
      <motion.div 
        className="absolute bottom-[10%] -right-[10%] w-[500px] h-[500px] bg-emerald-500/3 rounded-full blur-3xl"
        animate={{
          x: [0, -60, 0],
          y: [0, -40, 0],
        }}
        transition={{
          duration: 30,
          repeat: Infinity,
          ease: "easeInOut",
        }}
      />

      {/* Main content - ASYMMETRIC layout (DESIGN_VARIANCE: 8) */}
      <div className="container-premium relative z-10 py-20 md:py-32">
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-8 items-center">
          {/* Left side - Content (7 columns) */}
          <div className="lg:col-span-7">
            <motion.div 
              className="max-w-2xl"
              style={{ opacity, scale }}
            >
              {/* Role - uppercase tracking */}
              <motion.p 
                className="font-body text-sm md:text-base tracking-[0.25em] uppercase text-emerald-600 dark:text-emerald-400 mb-6"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: 0.2, ease: [0.16, 1, 0.3, 1] }}
              >
                {role}
              </motion.p>

              {/* Name - letter by letter reveal with spring */}
              <h1 className="font-display text-5xl md:text-7xl lg:text-8xl font-semibold tracking-tight mb-6 text-zinc-900 dark:text-zinc-50">
                <motion.span
                  className="inline-flex"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  transition={{ duration: 0.8, ease: "easeOut" }}
                >
                  {nameLetters.map((letter, i) => (
                    <motion.span
                      key={i}
                      initial={{ opacity: 0, y: 40, rotateX: -40 }}
                      animate={{ opacity: 1, y: 0, rotateX: 0 }}
                      transition={{
                        duration: 0.5,
                        delay: 0.3 + i * 0.03,
                        ease: [0.16, 1, 0.3, 1],
                      }}
                      className="inline-block"
                    >
                      {letter === " " ? "\u00A0" : letter}
                    </motion.span>
                  ))}
                </motion.span>
              </h1>

              {/* Tagline - elegant, max-width for readability */}
              {tagline && (
                <motion.p 
                  className="font-body text-lg md:text-xl lg:text-2xl text-zinc-500 dark:text-zinc-400 leading-relaxed mb-10 max-w-xl"
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.6, delay: 0.8, ease: [0.16, 1, 0.3, 1] }}
                >
                  {tagline}
                </motion.p>
              )}

              {/* CTA Buttons - asymmetric placement */}
              <motion.div 
                className="flex flex-col sm:flex-row gap-4"
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.6, delay: 1, ease: [0.16, 1, 0.3, 1] }}
              >
                <motion.button
                  className="inline-flex items-center justify-center gap-2 px-8 py-4 font-body text-sm font-medium tracking-tight bg-emerald-600 text-white rounded-full transition-all duration-300 hover:bg-emerald-700 hover:shadow-lg hover:shadow-emerald-500/20 active:translate-y-[1px]"
                  whileHover={{ scale: 1.02 }}
                  whileTap={{ scale: 0.98 }}
                >
                  <span>Ver Proyectos</span>
                  <motion.span
                    animate={{ x: [0, 4, 0] }}
                    transition={{
                      duration: 1.5,
                      repeat: Infinity,
                      ease: "easeInOut",
                    }}
                  >
                    <ArrowRight weight="bold" className="w-4 h-4" />
                  </motion.span>
                </motion.button>
                
                <motion.button
                  className="inline-flex items-center justify-center px-8 py-4 font-body text-sm font-medium tracking-tight border border-zinc-300 dark:border-zinc-700 text-zinc-900 dark:text-zinc-100 rounded-full transition-all duration-300 hover:bg-zinc-100 dark:hover:bg-zinc-800 active:translate-y-[1px]"
                  whileHover={{ scale: 1.02 }}
                  whileTap={{ scale: 0.98 }}
                >
                  Contactar
                </motion.button>
              </motion.div>
            </motion.div>
          </div>

          {/* Right side - Visual element (5 columns) - ASYMMETRIC */}
          <div className="lg:col-span-5 hidden lg:block">
            <motion.div
              className="relative"
              initial={{ opacity: 0, scale: 0.9 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 1, delay: 0.5, ease: [0.16, 1, 0.3, 1] }}
            >
              {/* Abstract visual representation */}
              <div className="relative aspect-[4/5]">
                {/* Glassmorphism card with inner border refraction */}
                <motion.div 
                  className="absolute inset-0 rounded-[2.5rem] overflow-hidden"
                  style={{ y: y2 }}
                >
                  {/* Background image placeholder */}
                  <div className="absolute inset-0 bg-gradient-to-br from-zinc-200 to-zinc-300 dark:from-zinc-800 dark:to-zinc-900">
                    {/* Abstract lines */}
                    <svg className="absolute inset-0 w-full h-full opacity-30" viewBox="0 0 400 500" preserveAspectRatio="none">
                      <defs>
                        <linearGradient id="lineGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                          <stop offset="0%" stopColor="#059669" stopOpacity="0.5" />
                          <stop offset="100%" stopColor="#059669" stopOpacity="0.1" />
                        </linearGradient>
                      </defs>
                      <path 
                        d="M0,100 Q200,50 400,150 T400,350 Q200,450 0,400" 
                        fill="none" 
                        stroke="url(#lineGradient)" 
                        strokeWidth="1"
                      />
                      <path 
                        d="M0,200 Q150,150 300,250 T400,450" 
                        fill="none" 
                        stroke="url(#lineGradient)" 
                        strokeWidth="0.5"
                      />
                    </svg>
                  </div>
                  
                  {/* Glass overlay with inner border */}
                  <div className="absolute inset-0 bg-gradient-to-t from-zinc-900/60 via-transparent to-transparent" />
                  <div className="absolute inset-0 border border-white/10 rounded-[2.5rem] shadow-[inset_0_1px_0_rgba(255,255,255,0.1)]" />
                  
                  {/* Floating accent element */}
                  <motion.div
                    className="absolute top-8 right-8 w-16 h-16 rounded-full bg-emerald-500/20 backdrop-blur-sm border border-emerald-500/30"
                    animate={{
                      scale: [1, 1.1, 1],
                    }}
                    transition={{
                      duration: 3,
                      repeat: Infinity,
                      ease: "easeInOut",
                    }}
                  />
                </motion.div>

                {/* Decorative offset element */}
                <motion.div 
                  className="absolute -bottom-4 -right-4 w-full h-full rounded-[2.5rem] border border-emerald-500/20 -z-10"
                  initial={{ opacity: 0, x: 20, y: 20 }}
                  animate={{ opacity: 1, x: 0, y: 0 }}
                  transition={{ duration: 0.8, delay: 1.2, ease: [0.16, 1, 0.3, 1] }}
                />
              </div>
            </motion.div>
          </div>
        </div>
      </div>

      {/* Scroll indicator - bottom center */}
      <motion.div
        className="absolute bottom-8 left-1/2 -translate-x-1/2"
        style={{ opacity: useTransform(scrollYSpring, [0, 100], [1, 0]) }}
      >
        <motion.button
          onClick={onScrollToWork}
          className="flex flex-col items-center gap-3 text-zinc-400 hover:text-zinc-600 dark:hover:text-zinc-300 transition-colors"
          aria-label="Scroll to work"
          animate={{ y: [0, 8, 0] }}
          transition={{
            duration: 2,
            repeat: Infinity,
            ease: "easeInOut",
          }}
        >
          <span className="font-body text-xs tracking-[0.2em] uppercase">Scroll</span>
          <ArrowDown weight="bold" className="w-4 h-4" />
        </motion.button>
      </motion.div>
    </section>
  );
}