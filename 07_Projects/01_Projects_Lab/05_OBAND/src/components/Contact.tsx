"use client";

import { useState, FormEvent } from "react";
import { motion } from "framer-motion";
import { Phone, Mail, MapPin, Send, Loader2, CheckCircle2 } from "lucide-react";

interface FormData {
  nombre: string;
  email: string;
  telefono: string;
  empresa: string;
  mensaje: string;
}

interface FormErrors {
  nombre?: string;
  email?: string;
  telefono?: string;
  mensaje?: string;
}

const initialFormData: FormData = {
  nombre: "",
  email: "",
  telefono: "",
  empresa: "",
  mensaje: "",
};

const springTransition = {
  type: "spring" as const,
  stiffness: 300,
  damping: 30,
};

export default function Contact() {
  const [formData, setFormData] = useState<FormData>(initialFormData);
  const [errors, setErrors] = useState<FormErrors>({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  const validateForm = (): boolean => {
    const newErrors: FormErrors = {};

    // Nombre validation
    if (!formData.nombre.trim()) {
      newErrors.nombre = "El nombre es requerido";
    } else if (formData.nombre.trim().length < 2) {
      newErrors.nombre = "El nombre debe tener al menos 2 caracteres";
    }

    // Email validation
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email.trim()) {
      newErrors.email = "El email es requerido";
    } else if (!emailRegex.test(formData.email)) {
      newErrors.email = "Ingresa un email valido";
    }

    // Telefono validation (optional but validate if provided)
    if (formData.telefono.trim()) {
      const phoneRegex = /^[+]?[(]?[0-9]{1,4}[)]?[-\s./0-9]{8,}$/;
      if (!phoneRegex.test(formData.telefono.trim())) {
        newErrors.telefono = "Ingresa un numero valido";
      }
    }

    // Mensaje validation
    if (!formData.mensaje.trim()) {
      newErrors.mensaje = "El mensaje es requerido";
    } else if (formData.mensaje.trim().length < 10) {
      newErrors.mensaje = "El mensaje debe tener al menos 10 caracteres";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    
    if (!validateForm()) {
      return;
    }

    setIsSubmitting(true);

    // Simulate form submission (in production, use Server Actions or API)
    await new Promise((resolve) => setTimeout(resolve, 1500));

    setIsSubmitting(false);
    setIsSubmitted(true);
    
    // Reset form after showing success
    setTimeout(() => {
      setFormData(initialFormData);
      setIsSubmitted(false);
    }, 3000);
  };

  const handleChange = (field: keyof FormData, value: string) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
    // Clear error when user starts typing
    if (errors[field as keyof FormErrors]) {
      setErrors((prev) => ({ ...prev, [field]: undefined }));
    }
  };

  return (
    <section id="contacto" className="w-full py-32 px-6 md:px-8 bg-glass/5 border-y border-glass-border">
      <div className="max-w-7xl mx-auto">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24">
          {/* Left Column - Info */}
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ ...springTransition, duration: 0.8 }}
          >
            <h2 className="text-4xl md:text-6xl font-bold tracking-tighter font-heading mb-6">
              Hablemos de tu <span className="text-accent">Proyecto</span>
            </h2>
            <p className="text-muted text-lg leading-relaxed mb-10">
              Estamos listos para transformar tu espacio. Cuéntanos sobre tu proyecto 
              y te contactaremos en menos de 24 horas.
            </p>

            <div className="space-y-6 mb-10">
              <div className="flex items-center gap-4">
                <div className="p-3 bg-accent/10 rounded-xl">
                  <Phone className="w-5 h-5 text-accent" />
                </div>
                <div>
                  <p className="text-sm text-muted uppercase tracking-widest mb-1">Telefono</p>
                  <a href="tel:+14705950121" className="text-lg font-medium hover:text-accent transition-colors">
                    +1 (470) 595-0121
                  </a>
                </div>
              </div>

              <div className="flex items-center gap-4">
                <div className="p-3 bg-accent/10 rounded-xl">
                  <Mail className="w-5 h-5 text-accent" />
                </div>
                <div>
                  <p className="text-sm text-muted uppercase tracking-widest mb-1">Email</p>
                  <a href="mailto:info@oimayen.com" className="text-lg font-medium hover:text-accent transition-colors">
                    info@oimayen.com
                  </a>
                </div>
              </div>

              <div className="flex items-center gap-4">
                <div className="p-3 bg-accent/10 rounded-xl">
                  <MapPin className="w-5 h-5 text-accent" />
                </div>
                <div>
                  <p className="text-sm text-muted uppercase tracking-widest mb-1">Ubicacion</p>
                  <p className="text-lg font-medium">Atlanta, Georgia</p>
                </div>
              </div>

              <div className="flex items-center gap-4">
                <div className="p-3 bg-accent/10 rounded-xl">
                  <svg className="w-5 h-5 text-accent" fill="currentColor" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
                </div>
                <div>
                  <p className="text-sm text-muted uppercase tracking-widest mb-1">Instagram</p>
                  <a href="https://instagram.com/oimayen" target="_blank" rel="noopener noreferrer" className="text-lg font-medium hover:text-accent transition-colors">
                    @oimayen
                  </a>
                </div>
              </div>
            </div>
          </motion.div>

          {/* Right Column - Form */}
          <motion.div
            initial={{ opacity: 0, x: 20 }}
            whileInView={{ opacity: 1, x: 0 }}
            viewport={{ once: true }}
            transition={{ ...springTransition, duration: 0.8, delay: 0.2 }}
          >
            <form onSubmit={handleSubmit} className="space-y-6">
              {/* Nombre */}
              <div className="space-y-2">
                <label htmlFor="nombre" className="text-sm font-medium text-muted">
                  Nombre Completo *
                </label>
                <input
                  type="text"
                  id="nombre"
                  value={formData.nombre}
                  onChange={(e) => handleChange("nombre", e.target.value)}
                  className={`w-full px-4 py-3 rounded-xl bg-glass border ${errors.nombre ? "border-red-500" : "border-glass-border"} focus:border-accent focus:outline-none transition-colors text-white placeholder:text-neutral-600`}
                  placeholder="Juan Perez"
                />
                {errors.nombre && (
                  <p className="text-red-500 text-sm">{errors.nombre}</p>
                )}
              </div>

              {/* Email & Telefono Row */}
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <label htmlFor="email" className="text-sm font-medium text-muted">
                    Email *
                  </label>
                  <input
                    type="email"
                    id="email"
                    value={formData.email}
                    onChange={(e) => handleChange("email", e.target.value)}
                    className={`w-full px-4 py-3 rounded-xl bg-glass border ${errors.email ? "border-red-500" : "border-glass-border"} focus:border-accent focus:outline-none transition-colors text-white placeholder:text-neutral-600`}
                    placeholder="juan@empresa.cl"
                  />
                  {errors.email && (
                    <p className="text-red-500 text-sm">{errors.email}</p>
                  )}
                </div>

                <div className="space-y-2">
                  <label htmlFor="telefono" className="text-sm font-medium text-muted">
                    Telefono
                  </label>
                  <input
                    type="tel"
                    id="telefono"
                    value={formData.telefono}
                    onChange={(e) => handleChange("telefono", e.target.value)}
                    className={`w-full px-4 py-3 rounded-xl bg-glass border ${errors.telefono ? "border-red-500" : "border-glass-border"} focus:border-accent focus:outline-none transition-colors text-white placeholder:text-neutral-600`}
                    placeholder="+56 9 1234 5678"
                  />
                  {errors.telefono && (
                    <p className="text-red-500 text-sm">{errors.telefono}</p>
                  )}
                </div>
              </div>

              {/* Empresa */}
              <div className="space-y-2">
                <label htmlFor="empresa" className="text-sm font-medium text-muted">
                  Empresa
                </label>
                <input
                  type="text"
                  id="empresa"
                  value={formData.empresa}
                  onChange={(e) => handleChange("empresa", e.target.value)}
                  className="w-full px-4 py-3 rounded-xl bg-glass border border-glass-border focus:border-accent focus:outline-none transition-colors text-white placeholder:text-neutral-600"
                  placeholder="Nombre de tu empresa"
                />
              </div>

              {/* Mensaje */}
              <div className="space-y-2">
                <label htmlFor="mensaje" className="text-sm font-medium text-muted">
                  Mensaje *
                </label>
                <textarea
                  id="mensaje"
                  rows={4}
                  value={formData.mensaje}
                  onChange={(e) => handleChange("mensaje", e.target.value)}
                  className={`w-full px-4 py-3 rounded-xl bg-glass border ${errors.mensaje ? "border-red-500" : "border-glass-border"} focus:border-accent focus:outline-none transition-colors text-white placeholder:text-neutral-600 resize-none`}
                  placeholder="Cuentanos sobre tu proyecto..."
                />
                {errors.mensaje && (
                  <p className="text-red-500 text-sm">{errors.mensaje}</p>
                )}
              </div>

              {/* Submit Button */}
              <button
                type="submit"
                disabled={isSubmitting || isSubmitted}
                className="w-full py-4 px-6 bg-accent text-black font-bold rounded-xl flex items-center justify-center gap-2 hover:bg-accent-hover transition-all disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {isSubmitting ? (
                  <>
                    <Loader2 className="w-5 h-5 animate-spin" />
                    Enviando...
                  </>
                ) : isSubmitted ? (
                  <>
                    <CheckCircle2 className="w-5 h-5" />
                    Enviado exitosamente
                  </>
                ) : (
                  <>
                    <Send className="w-5 h-5" />
                    Enviar Mensaje
                  </>
                )}
              </button>
            </form>
          </motion.div>
        </div>
      </div>
    </section>
  );
}