"use client";

import { motion, useScroll, useTransform } from "framer-motion";
import { useState, useEffect } from "react";
import { List, X, ArrowUpRight } from "phosphor-react";

interface NavItem {
  label: string;
  href: string;
}

const navItems: NavItem[] = [
  { label: "Proyectos", href: "#work" },
  { label: "Sobre Mí", href: "#about" },
  { label: "Contacto", href: "#contact" },
];

/**
 * Navigation - SOTA Design per taste-skill
 * Glassmorphism with inner border refraction, asymmetric
 */
export function Navigation() {
  const [isOpen, setIsOpen] = useState(false);
  const [mounted, setMounted] = useState(false);
  const { scrollY } = useScroll();

  // Navbar background opacity on scroll
  const navBgOpacity = useTransform(scrollY, [0, 100], [0, 1]);
  const navBlur = useTransform(scrollY, [0, 100], [0, 20]);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) return null;

  return (
    <>
      {/* Fixed navigation - glassmorphism */}
      <motion.nav
        className="fixed top-0 left-0 right-0 z-50 px-4 md:px-8 py-4"
        initial={{ y: -100 }}
        animate={{ y: 0 }}
        transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
      >
        {/* Glassmorphism background */}
        <motion.div
          className="absolute inset-0 bg-zinc-50/80 dark:bg-zinc-950/80 rounded-full"
          style={{
            opacity: navBgOpacity,
            backdropFilter: `blur(${navBlur}px)`,
          }}
        />
        
        {/* Inner border for refraction effect */}
        <div className="absolute inset-0 border border-white/10 dark:border-white/5 rounded-full pointer-events-none" />

        <div className="container-premium relative">
          <div className="flex items-center justify-between">
            {/* Logo - left aligned */}
            <motion.a
              href="#"
              className="font-display text-xl font-semibold tracking-tight text-zinc-900 dark:text-zinc-50 hover:text-emerald-600 dark:hover:text-emerald-400 transition-colors"
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
            >
              Elena
            </motion.a>

            {/* Desktop Navigation - right aligned */}
            <div className="hidden md:flex items-center gap-8">
              {navItems.map((item, i) => (
                <motion.a
                  key={item.href}
                  href={item.href}
                  className="font-body text-sm text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100 transition-colors relative group"
                  initial={{ opacity: 0, y: -10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: 0.1 * i + 0.3, ease: [0.16, 1, 0.3, 1] }}
                >
                  {item.label}
                  {/* Underline effect */}
                  <motion.span
                    className="absolute -bottom-1 left-0 h-[1px] bg-emerald-500"
                    initial={{ width: 0 }}
                    whileHover={{ width: "100%" }}
                    transition={{ duration: 0.3, ease: [0.16, 1, 0.3, 1] }}
                  />
                </motion.a>
              ))}

              {/* CTA Button */}
              <motion.a
                href="#contact"
                className="inline-flex items-center gap-2 px-5 py-2.5 font-body text-sm font-medium bg-zinc-900 dark:bg-zinc-100 text-zinc-50 dark:text-zinc-900 rounded-full hover:bg-emerald-600 dark:hover:bg-emerald-500 transition-colors"
                whileHover={{ scale: 1.02 }}
                whileTap={{ scale: 0.98 }}
              >
                <span>Hablemos</span>
                <ArrowUpRight weight="bold" className="w-3.5 h-3.5" />
              </motion.a>
            </div>

            {/* Mobile menu button */}
            <motion.button
              className="md:hidden p-2 text-zinc-900 dark:text-zinc-50"
              onClick={() => setIsOpen(!isOpen)}
              whileTap={{ scale: 0.95 }}
            >
              {isOpen ? (
                <X weight="bold" className="w-6 h-6" />
              ) : (
                <List weight="bold" className="w-6 h-6" />
              )}
            </motion.button>
          </div>
        </div>
      </motion.nav>

      {/* Mobile menu overlay */}
      <motion.div
        className="fixed inset-0 z-40 md:hidden"
        initial={{ opacity: 0 }}
        animate={{ opacity: isOpen ? 1 : 0 }}
        pointerEvents={isOpen ? "auto" : "none"}
      >
        {/* Backdrop */}
        <div
          className="absolute inset-0 bg-zinc-950/50 backdrop-blur-sm"
          onClick={() => setIsOpen(false)}
        />

        {/* Menu panel - slide in from right */}
        <motion.div
          className="absolute top-0 right-0 bottom-0 w-[280px] bg-zinc-50 dark:bg-zinc-950 pt-20 px-6 pb-8"
          initial={{ x: "100%" }}
          animate={{ x: isOpen ? 0 : "100%" }}
          transition={{ type: "spring", stiffness: 300, damping: 30 }}
        >
          <div className="flex flex-col gap-6">
            {navItems.map((item, i) => (
              <motion.a
                key={item.href}
                href={item.href}
                className="font-display text-2xl font-semibold text-zinc-900 dark:text-zinc-50"
                onClick={() => setIsOpen(false)}
                initial={{ opacity: 0, x: 20 }}
                animate={{ opacity: isOpen ? 1 : 0, x: isOpen ? 0 : 20 }}
                transition={{ delay: i * 0.1 }}
              >
                {item.label}
              </motion.a>
            ))}

            {/* Mobile CTA */}
            <motion.a
              href="#contact"
              className="inline-flex items-center gap-2 mt-4 px-6 py-3 font-body text-sm font-medium bg-emerald-600 text-white rounded-full"
              onClick={() => setIsOpen(false)}
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: isOpen ? 1 : 0, x: isOpen ? 0 : 20 }}
              transition={{ delay: 0.3 }}
            >
              <span>Hablemos</span>
              <ArrowUpRight weight="bold" className="w-4 h-4" />
            </motion.a>
          </div>
        </motion.div>
      </motion.div>
    </>
  );
}