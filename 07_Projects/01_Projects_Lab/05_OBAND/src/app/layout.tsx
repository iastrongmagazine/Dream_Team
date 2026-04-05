import type { Metadata } from "next";
import { Poppins, DM_Sans } from "next/font/google";
import "./globals.css";

const poppins = Poppins({
  variable: "--font-poppins",
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  display: "swap",
});

const dmSans = DM_Sans({
  variable: "--font-dm-sans",
  subsets: ["latin"],
  weight: ["400", "500", "700"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "OIM | Office Installations Mayen - Atlanta's Premier Corporate Space Experts",
  description: "Office Installations Mayen (OIM) - Expert corporate space installation and management in Atlanta, GA. 8+ years transforming workspaces into productive environments.",
  keywords: ["office installation Atlanta", "corporate furniture Atlanta", "office space optimization", "commercial interior design Atlanta", "OIM office installations", "workspace transformation Atlanta"],
  openGraph: {
    title: "OIM | Office Installations Mayen",
    description: "Atlanta's premier corporate space installation experts. Transforming workspaces into productive environments.",
    url: "https://oimayen.com",
    siteName: "Office Installations Mayen",
    locale: "en_US",
    type: "website",
  },
  alternates: {
    languages: {
      "en-US": "https://oimayen.com",
      "es": "https://oimayen.com?lang=es",
    },
  },
  robots: {
    index: true,
    follow: true,
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={`${poppins.variable} ${dmSans.variable}`}
    >
      <body className="min-h-[100dvh] font-body antialiased">
        <div className="mesh-bg" />
        {children}
      </body>
    </html>
  );
}