"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { ChevronRight } from "lucide-react";

const labelMap: Record<string, string> = {
  partidos: "Partidos",
  equipo: "Equipo",
  staff: "Cuerpo Técnico",
  femenino: "Femenino",
  cantera: "Cantera",
  competicion: "Competición",
  noticias: "Noticias",
  comunicados: "Comunicados",
  media: "Media",
  videos: "Videos",
  galerias: "Galerías",
  entradas: "Entradas",
  abonos: "Abonos",
  estadio: "Estadio",
  tienda: "Tienda",
  club: "Club",
  historia: "Historia",
  identidad: "Identidad",
  directiva: "Directiva",
  fundacion: "Fundación",
  transparencia: "Transparencia",
  contacto: "Contacto",
  fans: "Fans",
  sponsors: "Sponsors",
  academy: "Academy",
  busqueda: "Búsqueda",
  terminos: "Términos",
  privacidad: "Privacidad",
  cookies: "Cookies",
  accesibilidad: "Accesibilidad",
};

function segmentToLabel(segment: string): string {
  return labelMap[segment] || segment.charAt(0).toUpperCase() + segment.slice(1).replace(/-/g, " ");
}

export function Breadcrumbs() {
  const pathname = usePathname();
  const segments = pathname.split("/").filter(Boolean);

  if (segments.length === 0) return null;

  const crumbs = segments.map((seg, i) => ({
    label: segmentToLabel(seg),
    href: "/" + segments.slice(0, i + 1).join("/"),
    isLast: i === segments.length - 1,
  }));

  return (
    <nav aria-label="Breadcrumb" className="py-3">
      <ol className="flex items-center gap-1 text-sm text-muted">
        <li>
          <Link href="/" className="hover:text-foreground transition-colors">
            Inicio
          </Link>
        </li>
        {crumbs.map((crumb) => (
          <li key={crumb.href} className="flex items-center gap-1">
            <ChevronRight className="h-3.5 w-3.5" />
            {crumb.isLast ? (
              <span className="font-medium text-foreground" aria-current="page">
                {crumb.label}
              </span>
            ) : (
              <Link href={crumb.href} className="hover:text-foreground transition-colors">
                {crumb.label}
              </Link>
            )}
          </li>
        ))}
      </ol>
    </nav>
  );
}
