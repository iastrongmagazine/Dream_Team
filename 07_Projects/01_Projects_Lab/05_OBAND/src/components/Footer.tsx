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
    { href: "/privacidad", label: "Privacidad" },
    { href: "/terminos", label: "Terminos" },
  ],
};

export default function Footer() {
  return (
    <footer className="w-full py-16 px-6 md:px-12 lg:px-20 border-t border-white/5">
      <div className="max-w-6xl w-full">
        {/* Top section - Minimal grid */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-12 mb-16">
          <div className="md:col-span-1">
            <Link href="/" className="text-xl font-semibold tracking-tight mb-4 block">
              OIM<span className="text-neutral-500">.</span>
            </Link>
            <p className="text-neutral-500 text-sm leading-relaxed max-w-xs">
              Ingenieria de gestion de espacios corporativos.
            </p>
          </div>
          
          <div className="space-y-3">
            <h4 className="text-xs font-medium text-neutral-500 tracking-wide">Navegacion</h4>
            <ul className="space-y-2">
              {FOOTER_LINKS.nav.map((link) => (
                <li key={link.href}>
                  <Link href={link.href} className="text-sm text-neutral-400 hover:text-white transition-colors">
                    {link.label}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          <div className="space-y-4">
            <h4 className="text-xs font-medium text-neutral-500 tracking-wide">Contacto</h4>
            <div className="space-y-2 text-sm text-neutral-400">
              <a href="tel:+14705950121" className="flex items-center gap-2 hover:text-accent transition-colors">
                <Phone className="w-3.5 h-3.5" />
                +1 (470) 595-0121
              </a>
              <a href="mailto:info@oimayen.com" className="flex items-center gap-2 hover:text-accent transition-colors">
                <Mail className="w-3.5 h-3.5" />
                info@oimayen.com
              </a>
              <span className="flex items-center gap-2">
                <MapPin className="w-3.5 h-3.5" />
                Atlanta, Georgia
              </span>
            </div>
          </div>
        </div>

        {/* Bottom - Minimal */}
        <div className="flex flex-col md:flex-row items-center justify-between pt-8 border-t border-white/5 text-xs text-neutral-600">
          <span>&copy; {new Date().getFullYear()} OIM</span>
          <div className="flex gap-6 mt-4 md:mt-0">
            {FOOTER_LINKS.legal.map((link) => (
              <Link key={link.href} href={link.href} className="hover:text-neutral-400 transition-colors">
                {link.label}
              </Link>
            ))}
          </div>
        </div>
      </div>
    </footer>
  );
}
