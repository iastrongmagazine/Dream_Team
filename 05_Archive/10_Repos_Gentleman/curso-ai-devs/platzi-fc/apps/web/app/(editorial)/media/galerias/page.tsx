import type { Metadata } from "next";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Camera } from "lucide-react";

export const metadata: Metadata = {
  title: "Galerías",
  description: "Galerías de fotos del Platzi FC.",
};

const mockGalleries = [
  { id: "1", title: "Platzi FC 3-1 Deportivo Sur", photos: 24, date: "1 Mar 2026" },
  { id: "2", title: "Entrenamiento semanal", photos: 18, date: "27 Feb 2026" },
  { id: "3", title: "FC Norte 0-2 Platzi FC", photos: 32, date: "25 Feb 2026" },
  { id: "4", title: "Día del club: celebración", photos: 45, date: "22 Feb 2026" },
  { id: "5", title: "Visita a la comunidad", photos: 15, date: "20 Feb 2026" },
  { id: "6", title: "Sesión de fotos oficial", photos: 28, date: "18 Feb 2026" },
];

export default function GaleriasPage() {
  return (
    <div className="py-8">
      <h1 className="text-3xl font-bold mb-2">Galerías</h1>
      <p className="text-foreground-secondary mb-8">Las mejores imágenes del Platzi FC</p>

      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {mockGalleries.map((gallery) => (
          <Card key={gallery.id} className="group overflow-hidden hover:shadow-md transition-shadow cursor-pointer">
            <div className="relative aspect-[4/3] bg-primary/5 flex items-center justify-center">
              <Camera className="h-10 w-10 text-primary/20" />
              <div className="absolute bottom-2 right-2 flex items-center gap-1 rounded bg-black/70 px-2 py-1 text-xs text-white">
                <Camera className="h-3 w-3" />
                {gallery.photos} fotos
              </div>
            </div>
            <CardContent className="p-4">
              <p className="text-xs text-muted mb-1">{gallery.date}</p>
              <p className="font-semibold text-sm group-hover:text-primary transition-colors">{gallery.title}</p>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
