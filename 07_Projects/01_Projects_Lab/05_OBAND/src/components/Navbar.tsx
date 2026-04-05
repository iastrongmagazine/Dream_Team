"use client";

import { motion } from "framer-motion";
import { Menu, X, ArrowUpRight } from "lucide-react";
import { useState } from "react";
import Link from "next/link";

const NAV_LINKS = [
  { href: "#servicios", label: "Servicios" },
  { href: "#proyectos", label: "Proyectos" },
  { href: "#nosotros", label: "Nosotros" },
  { href: "#contacto", label: "Contacto" },
];

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="fixed top-0 left-0 w-full z-50 flex items-center justify-between px-6 md:px-8 py-4 md:py-6 backdrop-blur-md bg-black/20 border-b border-glass-border">
      <div className="flex items-center gap-8">
        <Link href="/" className="text-2xl font-bold tracking-tighter font-heading hover:text-accent transition-colors">
          OIM<span className="text-neutral-500">.</span>
        </Link>
        <div className="hidden md:flex items-center gap-6 text-sm font-medium tracking-tight text-neutral-400">
          {NAV_LINKS.map((link) => (
            <Link key={link.href} href={link.href} className="hover:text-white transition-colors">
              {link.label}
            </Link>
          ))}
        </div>
      </div>

      <div className="hidden md:flex items-center gap-4">
        <Link 
          href="#contacto" 
          className="px-5 py-2.5 rounded-full bg-accent text-black text-sm font-bold flex items-center gap-2 hover:bg-accent-hover transition-all hover:scale-105"
        >
          Iniciar Proyecto <ArrowUpRight className="w-4 h-4" />
        </Link>
      </div>

      {/* Mobile Toggle */}
      <button 
        type="button"
        className="md:hidden p-2 text-white" 
        onClick={() => setIsOpen(!isOpen)}
        aria-label="Toggle menu"
        aria-expanded={isOpen}
        aria-controls="mobile-menu"
      >
        {isOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
      </button>

      {/* Mobile Menu Overlay */}
      {isOpen && (
        <motion.div 
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
        id="mobile-menu"
        aria-label="Menú móvil"
        className="absolute top-full left-0 w-full bg-black border-b border-glass-border p-8 flex flex-col gap-6 md:hidden z-40"
        >
          {NAV_LINKS.map((link) => (
            <Link 
              key={link.href} 
              href={link.href} 
              className="text-xl font-bold"
              onClick={() => setIsOpen(false)}
            >
              {link.label}
            </Link>
          ))}
          <Link href="#contacto" className="text-xl font-bold text-accent" onClick={() => setIsOpen(false)}>
            Contacto
          </Link>
        </motion.div>
      )}
    </nav>
  );
}
