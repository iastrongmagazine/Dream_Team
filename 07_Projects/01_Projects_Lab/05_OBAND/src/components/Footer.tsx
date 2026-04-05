import Link from "next/link";
import { Phone, Mail, MapPin } from "lucide-react";

const FOOTER_LINKS = {
  nav: [
    { href: "#servicios", label: "Servicios" },
    { href: "#proyectos", label: "Proyectos" },
    { href: "#nosotros", label: "Nosotros" },
    { href: "#contacto", label: "Contacto" },
  ],
  legal: [
    { href: "/privacidad", label: "Politica de Privacidad" },
    { href: "/terminos", label: "Terminos de Servicio" },
  ],
};

export default function Footer() {
  return (
    <footer className="w-full py-20 px-6 md:px-8 border-t border-glass-border">
      <div className="max-w-7xl w-full grid grid-cols-1 md:grid-cols-4 gap-12 mb-16">
        <div className="col-span-1 md:col-span-2">
          <Link href="/" className="text-3xl font-black tracking-tighter font-heading mb-6 block">
            OIM<span className="text-accent">.</span>
          </Link>
          <p className="text-muted max-w-sm leading-relaxed mb-6">
            Expertos en ingenieria de gestion de espacios corporativos. 
            Transformamos ambientes de trabajo en experiencias productivas.
          </p>
          <div className="flex flex-col gap-3 text-sm text-muted">
            <a href="tel:+14705950121" className="flex items-center gap-2 hover:text-accent transition-colors">
              <Phone className="w-4 h-4" />
              +1 (470) 595-0121
            </a>
            <a href="mailto:info@oimayen.com" className="flex items-center gap-2 hover:text-accent transition-colors">
              <Mail className="w-4 h-4" />
              info@oimayen.com
            </a>
            <span className="flex items-center gap-2">
              <MapPin className="w-4 h-4" />
              Atlanta, Georgia
            </span>
          </div>
        </div>
        
        <div className="space-y-4">
          <h4 className="font-bold uppercase tracking-widest text-xs text-neutral-400">Navegacion</h4>
          <ul className="space-y-2 text-sm">
            {FOOTER_LINKS.nav.map((link) => (
              <li key={link.href}>
                <Link href={link.href} className="hover:text-accent transition-colors">
                  {link.label}
                </Link>
              </li>
            ))}
          </ul>
        </div>

        <div className="space-y-4">
          <h4 className="font-bold uppercase tracking-widest text-xs text-neutral-400">Legal</h4>
          <ul className="space-y-2 text-sm">
            {FOOTER_LINKS.legal.map((link) => (
              <li key={link.href}>
                <Link href={link.href} className="hover:text-accent transition-colors">
                  {link.label}
                </Link>
              </li>
            ))}
          </ul>
        </div>
      </div>

      <div className="w-full flex flex-col md:flex-row items-center justify-between pt-12 border-t border-glass-border/30 text-neutral-600 text-xs font-mono tracking-widest uppercase">
        <span>&copy; {new Date().getFullYear()} OIM // Todos los Derechos Reservados</span>
        <div className="flex gap-6 mt-4 md:mt-0">
          <a 
            href="https://www.linkedin.com/company/oimayen" 
            target="_blank" 
            rel="noopener noreferrer"
            className="hover:text-white transition-colors"
          >
            LinkedIn
          </a>
          <a 
            href="https://instagram.com/oimayen" 
            target="_blank" 
            rel="noopener noreferrer"
            className="hover:text-white transition-colors"
          >
            Instagram
          </a>
        </div>
      </div>
    </footer>
  );
}
