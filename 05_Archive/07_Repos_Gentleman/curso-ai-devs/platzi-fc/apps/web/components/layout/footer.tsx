import Link from "next/link";
import { footerNav } from "./nav-data";
import { NewsletterForm } from "./newsletter-form";

function FooterSection({ title, links }: { title: string; links: { label: string; href: string }[] }) {
  return (
    <div>
      <h3 className="mb-3 text-sm font-semibold uppercase tracking-wider text-white">
        {title}
      </h3>
      <ul className="space-y-2">
        {links.map((link) => (
          <li key={link.href}>
            <Link
              href={link.href}
              className="text-sm text-white/60 hover:text-white transition-colors"
            >
              {link.label}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export function Footer() {
  return (
    <footer className="border-t border-white/10 bg-primary-dark">
      <div className="mx-auto max-w-7xl px-4 py-12">
        <div className="grid grid-cols-2 gap-8 md:grid-cols-4 lg:grid-cols-5">
          {/* Brand */}
          <div className="col-span-2 md:col-span-4 lg:col-span-1">
            <div className="flex items-center gap-2 mb-4">
              <div className="flex h-9 w-9 items-center justify-center rounded-full bg-secondary text-primary-dark font-bold text-sm">
                PFC
              </div>
              <span className="text-lg font-bold text-white">Platzi FC</span>
            </div>
            <p className="text-sm text-white/50 max-w-xs">
              El club del futuro. Pasión, tecnología y comunidad unidos en un solo equipo.
            </p>
          </div>

          <FooterSection title="Enlaces" links={footerNav.quickLinks} />
          <FooterSection title="Club" links={footerNav.club} />
          <FooterSection title="Legal" links={footerNav.legal} />
          <FooterSection title="Redes" links={footerNav.social} />
        </div>

        {/* Newsletter */}
        <div className="mt-10 rounded-lg border border-white/10 bg-white/5 p-6">
          <div className="flex flex-col items-start gap-4 sm:flex-row sm:items-center sm:justify-between">
            <div>
              <h3 className="text-sm font-semibold text-white">Newsletter</h3>
              <p className="mt-1 text-sm text-white/50">
                Recibe las últimas noticias y ofertas del club.
              </p>
            </div>
            <NewsletterForm />
          </div>
        </div>

        {/* Bottom */}
        <div className="mt-8 flex flex-col items-center justify-between gap-4 border-t border-white/10 pt-8 sm:flex-row">
          <p className="text-xs text-white/40">
            &copy; {new Date().getFullYear()} Platzi FC. Todos los derechos reservados.
          </p>
          <p className="text-xs text-white/40">
            Hecho con pasión por la comunidad Platzi.
          </p>
        </div>
      </div>
    </footer>
  );
}
