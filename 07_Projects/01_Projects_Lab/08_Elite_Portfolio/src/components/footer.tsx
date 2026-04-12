"use client";

import { motion } from "framer-motion";
import { InstagramLogo, LinkedinLogo, DribbbleLogo } from "phosphor-react";

const socialLinks = [
  { icon: InstagramLogo, href: "#", label: "Instagram" },
  { icon: LinkedinLogo, href: "#", label: "LinkedIn" },
  { icon: DribbbleLogo, href: "#", label: "Dribbble" },
];

/**
 * Footer - SOTA Design per taste-skill
 * Minimal, elegant, left-aligned
 */
export function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="py-12 md:py-16 bg-zinc-100 dark:bg-zinc-900 border-t border-zinc-200 dark:border-zinc-800">
      <div className="container-premium">
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between gap-8">
          {/* Left - Brand */}
          <motion.div
            className="flex flex-col gap-4"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
          >
            <a
              href="#"
              className="font-display text-2xl font-semibold tracking-tight text-zinc-900 dark:text-zinc-50"
            >
              Elena
            </a>
            <p className="font-body text-sm text-zinc-500 dark:text-zinc-400 max-w-xs">
              Creando experiencias digitales extraordinarias que inspiran y transforman.
            </p>
          </motion.div>

          {/* Center - Navigation */}
          <motion.div
            className="flex flex-wrap gap-6"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.1, duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
          >
            <a
              href="#work"
              className="font-body text-sm text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100 transition-colors"
            >
              Proyectos
            </a>
            <a
              href="#about"
              className="font-body text-sm text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100 transition-colors"
            >
              Sobre Mí
            </a>
            <a
              href="#contact"
              className="font-body text-sm text-zinc-600 dark:text-zinc-400 hover:text-zinc-900 dark:hover:text-zinc-100 transition-colors"
            >
              Contacto
            </a>
          </motion.div>

          {/* Right - Social + Copyright */}
          <motion.div
            className="flex flex-col items-start md:items-end gap-4"
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.2, duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
          >
            {/* Social links */}
            <div className="flex items-center gap-4">
              {socialLinks.map((social, i) => (
                <motion.a
                  key={social.label}
                  href={social.href}
                  aria-label={social.label}
                  className="w-10 h-10 rounded-full bg-zinc-200 dark:bg-zinc-800 flex items-center justify-center text-zinc-600 dark:text-zinc-400 hover:bg-emerald-500 hover:text-white transition-colors"
                  whileHover={{ scale: 1.05 }}
                  whileTap={{ scale: 0.95 }}
                >
                  <social.icon weight="bold" className="w-4 h-4" />
                </motion.a>
              ))}
            </div>

            {/* Copyright */}
            <p className="font-body text-xs text-zinc-400 dark:text-zinc-500">
              © {currentYear} Elena. Todos los derechos reservados.
            </p>
          </motion.div>
        </div>
      </div>
    </footer>
  );
}