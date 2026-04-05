"use client";

import { motion } from "framer-motion";
import { List, X, ArrowUpRight } from "lucide-react";
import { useState } from "react";
import Link from "next/link";

const springTransition = {
  type: "spring" as const,
  stiffness: 100,
  damping: 20,
};

const NAV_LINKS = [
  { href: "#servicios", label: "Servicios" },
  { href: "#proyectos", label: "Proyectos" },
  { href: "#nosotros", label: "Nosotros" },
  { href: "#contacto", label: "Contacto" },
];

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="fixed top-0 left-0 w-full z-50 flex items-center justify-between px-6 md:px-12 py-5 md:py-6 backdrop-blur-xl bg-background/60 border-b border-white/5">
      <div className="flex items-center gap-12">
        <Link href="/" className="text-xl font-semibold tracking-tight hover:text-accent transition-colors">
          OIM<span className="text-neutral-500">.</span>
        </Link>
        <div className="hidden md:flex items-center gap-8 text-sm font-medium text-neutral-400">
          {NAV_LINKS.map((link) => (
            <Link key={link.href} href={link.href} className="hover:text-white transition-colors duration-300">
              {link.label}
            </Link>
          ))}
        </div>
      </div>

      <div className="hidden md:flex items-center gap-4">
        <Link 
          href="#contacto" 
          className="px-5 py-2.5 rounded-full bg-accent text-black text-sm font-semibold flex items-center gap-2 hover:bg-accent-hover transition-all duration-300 active:scale-[0.98]"
        >
          Iniciar Proyecto <ArrowUpRight className="w-4 h-4" />
        </Link>
      </div>

      {/* Mobile Toggle */}
      <button 
        type="button"
        className="md:hidden p-2 text-white/80 hover:text-white transition-colors" 
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Toggle menu"
        aria-expanded={isOpen}
        aria-controls="mobile-menu"
      >
        {isOpen ? <X className="w-5 h-5" /> : <List className="w-5 h-5" />}
      </button>

      {/* Mobile Menu Overlay */}
      {isOpen && (
        <motion.div 
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ ...springTransition, duration: 0.4 }}
          id="mobile-menu"
          aria-label="Menú móvil"
          className="absolute top-full left-0 w-full bg-surface-elevated border-b border-white/5 p-6 flex flex-col gap-5 md:hidden z-40"
        >
          {NAV_LINKS.map((link, index) => (
            <motion.div
              key={link.href}
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ ...springTransition, delay: index * 0.1 }}
            >
              <Link 
                href={link.href} 
                className="text-lg font-medium"
                onClick={() => setIsOpen(false)}
              >
                {link.label}
              </Link>
            </motion.div>
          ))}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ ...springTransition, delay: NAV_LINKS.length * 0.1 }}
          >
            <Link href="#contacto" className="text-lg font-medium text-accent" onClick={() => setIsOpen(false)}>
              Contacto
            </Link>
          </motion.div>
        </motion.div>
      )}
    </nav>
  );
}
