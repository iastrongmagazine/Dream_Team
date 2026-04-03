export interface NavItem {
  label: string;
  href: string;
  children?: NavItem[];
}

export const mainNav: NavItem[] = [
  { label: "Inicio", href: "/" },
  {
    label: "Partidos",
    href: "/partidos",
    children: [
      { label: "Calendario", href: "/partidos" },
      { label: "Resultados", href: "/partidos?view=results" },
      { label: "Competición", href: "/competicion" },
    ],
  },
  {
    label: "Equipo",
    href: "/equipo",
    children: [
      { label: "Primer Equipo", href: "/equipo" },
      { label: "Cuerpo Técnico", href: "/equipo/staff" },
      { label: "Femenino", href: "/equipo/femenino" },
      { label: "Cantera", href: "/equipo/cantera" },
    ],
  },
  {
    label: "Noticias",
    href: "/noticias",
    children: [
      { label: "Últimas", href: "/noticias" },
      { label: "Comunicados", href: "/noticias/comunicados" },
    ],
  },
  {
    label: "Media",
    href: "/media/videos",
    children: [
      { label: "Videos", href: "/media/videos" },
      { label: "Fotos", href: "/media/galerias" },
    ],
  },
  {
    label: "Entradas",
    href: "/entradas",
    children: [
      { label: "Comprar", href: "/entradas" },
      { label: "Abonos", href: "/entradas/abonos" },
      { label: "Info Estadio", href: "/entradas/estadio" },
    ],
  },
  { label: "Tienda", href: "/tienda" },
  {
    label: "Club",
    href: "/club/historia",
    children: [
      { label: "Historia", href: "/club/historia" },
      { label: "Estadio", href: "/club/estadio" },
      { label: "Fundación", href: "/club/fundacion" },
      { label: "Transparencia", href: "/club/transparencia" },
      { label: "Contacto", href: "/club/contacto" },
    ],
  },
];

export const footerNav = {
  quickLinks: [
    { label: "Partidos", href: "/partidos" },
    { label: "Equipo", href: "/equipo" },
    { label: "Noticias", href: "/noticias" },
    { label: "Tienda", href: "/tienda" },
    { label: "Entradas", href: "/entradas" },
  ],
  club: [
    { label: "Historia", href: "/club/historia" },
    { label: "Estadio", href: "/club/estadio" },
    { label: "Fundación", href: "/club/fundacion" },
    { label: "Contacto", href: "/club/contacto" },
  ],
  legal: [
    { label: "Términos", href: "/terminos" },
    { label: "Privacidad", href: "/privacidad" },
    { label: "Cookies", href: "/cookies" },
    { label: "Accesibilidad", href: "/accesibilidad" },
  ],
  social: [
    { label: "Twitter / X", href: "#" },
    { label: "Instagram", href: "#" },
    { label: "YouTube", href: "#" },
    { label: "Facebook", href: "#" },
    { label: "TikTok", href: "#" },
  ],
};
