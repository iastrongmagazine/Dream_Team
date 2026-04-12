import type { Metadata } from "next";
import { Geist, Outfit } from "next/font/google";
import "./globals.css";

const geist = Geist({
  subsets: ["latin"],
  variable: "--font-geist",
  display: "swap",
});

const outfit = Outfit({
  subsets: ["latin"],
  variable: "--font-outfit",
  display: "swap",
});

export const metadata: Metadata = {
  title: {
    template: "%s | Elena - Portfolio de Arquitectura",
    default: "Elena - Portfolio de Arquitectura y Diseño de Interiores",
  },
  description: "Arquitecta y diseñadora de interiores creando espacios que inspiran, funcionan y perduran en el tiempo. Proyectos residenciales y comerciales.",
  keywords: ["arquitectura", "diseño de interiores", "portfolio", "diseño residencial", "diseño comercial", "espacios premium"],
  authors: [{ name: "Elena" }],
  openGraph: {
    title: "Elena - Portfolio de Arquitectura y Diseño",
    description: "Creando espacios que inspiran, funcionan y perduran en el tiempo.",
    type: "website",
    locale: "es_ES",
    url: "https://elena-portfolio.com",
    siteName: "Elena Portfolio",
    images: [
      {
        url: "/og-image.jpg",
        width: 1200,
        height: 630,
        alt: "Elena - Portfolio de Arquitectura",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "Elena - Portfolio de Arquitectura y Diseño",
    description: "Creando espacios que inspiran, funcionan y perduran en el tiempo.",
  },
  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="es" suppressHydrationWarning>
      <body className={`${geist.variable} ${outfit.variable} antialiased bg-zinc-50 text-zinc-950 dark:bg-zinc-950 dark:text-zinc-50`}>
        {children}
      </body>
    </html>
  );
}