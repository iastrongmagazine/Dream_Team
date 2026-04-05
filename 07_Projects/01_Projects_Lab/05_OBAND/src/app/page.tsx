"use client";

import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import Services from "@/components/Services";
import Stats from "@/components/Stats";
import Projects from "@/components/Projects";
import About from "@/components/About";
import Contact from "@/components/Contact";
import Footer from "@/components/Footer";
import { ArrowRight } from "lucide-react";
import { motion } from "framer-motion";

const springTransition = {
  type: "spring" as const,
  stiffness: 300,
  damping: 30,
};

export default function Home() {
  return (
    <main className="relative min-h-screen bg-background text-foreground selection:bg-accent selection:text-white">
      {/* Navbar Global */}
      <Navbar />

      {/* Hero Section */}
      <Hero />

      {/* Services Section */}
      <Services />

      {/* Stats Section */}
      <Stats />

      {/* Projects Grid */}
      <Projects />

      {/* About Section */}
      <About />

      {/* Contact Section */}
      <Contact />

      {/* CTA Section */}
      <section className="py-40 px-6 md:px-8 relative overflow-hidden">
        <div className="mesh-bg opacity-30" />
        <div className="max-w-4xl mx-auto text-center space-y-12 z-10 relative">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ ...springTransition, duration: 0.8 }}
          >
            <h2 className="text-5xl md:text-8xl font-black tracking-tighter font-heading leading-none">
              Listo para <span className="text-accent underline">Transformar</span>?
            </h2>
          </motion.div>
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ ...springTransition, duration: 0.8, delay: 0.2 }}
          >
            <p className="text-xl text-muted font-light max-w-2xl mx-auto">
              Unite a las empresas que ya transformaron sus espacios de trabajo. 
              Hablemos de tu proximo proyecto.
            </p>
          </motion.div>
          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            transition={{ ...springTransition, duration: 0.8, delay: 0.4 }}
            className="flex justify-center"
          >
            <a 
              href="#contacto" 
              className="px-12 py-6 bg-accent text-black font-black rounded-3xl hover:bg-accent-hover transition-all transform hover:scale-105 text-lg flex items-center gap-2"
            >
              Iniciar Proyecto <ArrowRight className="w-5 h-5" />
            </a>
          </motion.div>
        </div>
      </section>

      {/* Footer Global */}
      <Footer />
    </main>
  );
}