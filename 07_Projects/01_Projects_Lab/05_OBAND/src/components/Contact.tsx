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
  hidden: { opacity: 0, y: 30 },
  visible: { 
    opacity: 1, 
    y: 0,
    transition: { ...springTransition, duration: 0.8 }
  }
};

export default function Contact() {
  const [formData, setFormData] = useState<FormData>(initialFormData);
  const [errors, setErrors] = useState<FormErrors>({});
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isSubmitted, setIsSubmitted] = useState(false);

  const validateForm = (): boolean => {
    const newErrors: FormErrors = {};

    if (!formData.nombre.trim()) {
      newErrors.nombre = "El nombre es requerido";
    } else if (formData.nombre.trim().length < 2) {
      newErrors.nombre = "El nombre debe tener al menos 2 caracteres";
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!formData.email.trim()) {
      newErrors.email = "El email es requerido";
    } else if (!emailRegex.test(formData.email)) {
      newErrors.email = "Ingresa un email valido";
    }

    if (formData.telefono.trim()) {
      const phoneRegex = /^[+]?[(]?[0-9]{1,4}[)]?[-\s./0-9]{8,}$/;
      if (!phoneRegex.test(formData.telefono.trim())) {
        newErrors.telefono = "Ingresa un numero valido";
      }
    }

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

    await new Promise((resolve) => setTimeout(resolve, 1500));

    setIsSubmitting(false);
    setIsSubmitted(true);
    
    setTimeout(() => {
      setFormData(initialFormData);
      setIsSubmitted(false);
    }, 3000);
  };

  const handleChange = (field: keyof FormData, value: string) => {
    setFormData((prev) => ({ ...prev, [field]: value }));
    if (errors[field as keyof FormErrors]) {
      setErrors((prev) => ({ ...prev, [field]: undefined }));
    }
  };

  return (
    <section id="contacto" className="w-full py-24 md:py-32 px-6 md:px-12 lg:px-20 border-y border-white/5">
      <div className="max-w-6xl mx-auto">
        <motion.div 
          variants={staggerChildren}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true }}
          className="grid grid-cols-1 lg:grid-cols-2 gap-16 lg:gap-24"
        >
          {/* Left Column - Info */}
          <motion.div variants={fadeInUp}>
            <div className="mb-4">
              <span className="text-xs font-medium tracking-widest text-neutral-500 uppercase">
                Contacto
              </span>
            </div>
            <h2 className="text-3xl md:text-5xl font-semibold tracking-tight text-white mb-6">
              Hablemos de tu <span className="text-accent">Proyecto</span>
            </h2>
            <p className="text-neutral-400 leading-relaxed mb-10">
              Estamos listos para transformar tu espacio. Contactanos en menos de 24 horas.
            </p>

            <div className="space-y-6">
              <div className="flex items-center gap-4">
                <Phone className="w-4 h-4 text-neutral-500" />
                <div>
                  <p className="text-xs text-neutral-500 tracking-wide mb-1">Telefono</p>
                  <a href="tel:+14705950121" className="text-sm font-medium hover:text-accent transition-colors">
                    +1 (470) 595-0121
                  </a>
                </div>
              </div>

              <div className="flex items-center gap-4">
                <Mail className="w-4 h-4 text-neutral-500" />
                <div>
                  <p className="text-xs text-neutral-500 tracking-wide mb-1">Email</p>
                  <a href="mailto:info@oimayen.com" className="text-sm font-medium hover:text-accent transition-colors">
                    info@oimayen.com
                  </a>
                </div>
              </div>

              <div className="flex items-center gap-4">
                <MapPin className="w-4 h-4 text-neutral-500" />
                <div>
                  <p className="text-xs text-neutral-500 tracking-wide mb-1">Ubicacion</p>
                  <p className="text-sm font-medium">Atlanta, Georgia</p>
                </div>
              </div>
            </div>
          </motion.div>

          {/* Right Column - Form - Minimal inputs, no card styling */}
          <motion.div variants={fadeInUp}>
            <form onSubmit={handleSubmit} className="space-y-6">
              <div className="space-y-2">
                <label htmlFor="nombre" className="text-xs font-medium text-neutral-500 tracking-wide">
                  Nombre Completo *
                </label>
                <input
                  type="text"
                  id="nombre"
                  value={formData.nombre}
                  onChange={(e) => handleChange("nombre", e.target.value)}
                  className={`w-full px-4 py-3 rounded-xl bg-white/5 border ${errors.nombre ? "border-red-500/50" : "border-white/10"} focus:border-accent focus:outline-none transition-colors text-white placeholder:text-neutral-600 text-sm`}
                  placeholder="Juan Perez"
                />
                {errors.nombre && (
                  <p className="text-red-500/70 text-xs">{errors.nombre}</p>
                )}
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-2">
                  <label htmlFor="email" className="text-xs font-medium text-neutral-500 tracking-wide">
                    Email *
                  </label>
                  <input
                    type="email"
                    id="email"
                    value={formData.email}
                    onChange={(e) => handleChange("email", e.target.value)}
                    className={`w-full px-4 py-3 rounded-xl bg-white/5 border ${errors.email ? "border-red-500/50" : "border-white/10"} focus:border-accent focus:outline-none transition-colors text-white placeholder:text-neutral-600 text-sm`}
                    placeholder="juan@empresa.cl"
                  />
                  {errors.email && (
                    <p className="text-red-500/70 text-xs">{errors.email}</p>
                  )}
                </div>

                <div className="space-y-2">
                  <label htmlFor="telefono" className="text-xs font-medium text-neutral-500 tracking-wide">
                    Telefono
                  </label>
                  <input
                    type="tel"
                    id="telefono"
                    value={formData.telefono}
                    onChange={(e) => handleChange("telefono", e.target.value)}
                    className="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 focus:border-accent focus:outline-none transition-colors text-white placeholder:text-neutral-600 text-sm"
                    placeholder="+56 9 1234 5678"
                  />
                </div>
              </div>

              <div className="space-y-2">
                <label htmlFor="empresa" className="text-xs font-medium text-neutral-500 tracking-wide">
                  Empresa
                </label>
                <input
                  type="text"
                  id="empresa"
                  value={formData.empresa}
                  onChange={(e) => handleChange("empresa", e.target.value)}
                  className="w-full px-4 py-3 rounded-xl bg-white/5 border border-white/10 focus:border-accent focus:outline-none transition-colors text-white placeholder:text-neutral-600 text-sm"
                  placeholder="Nombre de tu empresa"
                />
              </div>

              <div className="space-y-2">
                <label htmlFor="mensaje" className="text-xs font-medium text-neutral-500 tracking-wide">
                  Mensaje *
                </label>
                <textarea
                  id="mensaje"
                  rows={4}
                  value={formData.mensaje}
                  onChange={(e) => handleChange("mensaje", e.target.value)}
                  className={`w-full px-4 py-3 rounded-xl bg-white/5 border ${errors.mensaje ? "border-red-500/50" : "border-white/10"} focus:border-accent focus:outline-none transition-colors text-white placeholder:text-neutral-600 resize-none text-sm`}
                  placeholder="Cuentanos sobre tu proyecto..."
                />
                {errors.mensaje && (
                  <p className="text-red-500/70 text-xs">{errors.mensaje}</p>
                )}
              </div>

              <button
                type="submit"
                disabled={isSubmitting || isSubmitted}
                className="w-full py-4 px-6 bg-accent text-black font-semibold rounded-full flex items-center justify-center gap-2 hover:bg-accent-hover transition-all duration-300 disabled:opacity-50 disabled:cursor-not-allowed active:scale-[0.98]"
              >
                {isSubmitting ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    Enviando...
                  </>
                ) : isSubmitted ? (
                  <>
                    <CheckCircle2 className="w-4 h-4" />
                    Enviado
                  </>
                ) : (
                  <>
                    <Send className="w-4 h-4" />
                    Enviar Mensaje
                  </>
                )}
              </button>
            </form>
          </motion.div>
        </motion.div>
      </div>
    </section>
  );
}