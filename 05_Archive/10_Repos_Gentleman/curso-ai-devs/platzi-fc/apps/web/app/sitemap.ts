import type { MetadataRoute } from "next";

export default function sitemap(): MetadataRoute.Sitemap {
  const baseUrl = "https://platzifc.com";

  const staticPages = [
    "",
    "/partidos",
    "/equipo",
    "/equipo/staff",
    "/competicion",
    "/noticias",
    "/media/videos",
    "/media/galerias",
    "/entradas",
    "/tienda",
    "/club/historia",
    "/club/estadio",
    "/club/fundacion",
    "/club/contacto",
  ];

  return staticPages.map((path) => ({
    url: `${baseUrl}${path}`,
    lastModified: new Date(),
    changeFrequency: path === "" ? "daily" : "weekly",
    priority: path === "" ? 1.0 : 0.8,
  }));
}
