import type { Metadata } from "next";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Play } from "lucide-react";

export const metadata: Metadata = {
  title: "Videos",
  description: "Videos oficiales del Platzi FC: resúmenes, entrevistas y más.",
};

const mockVideos = [
  { id: "1", title: "Resumen: Platzi FC 3-1 Deportivo Sur", duration: "4:32", category: "Resúmenes", date: "1 Mar 2026" },
  { id: "2", title: "Entrevista post-partido: Sebastián Rojas", duration: "6:15", category: "Entrevistas", date: "1 Mar 2026" },
  { id: "3", title: "Los mejores goles de febrero", duration: "3:48", category: "Highlights", date: "28 Feb 2026" },
  { id: "4", title: "Entrenamiento abierto: preparando el derbi", duration: "2:55", category: "Detrás de cámaras", date: "26 Feb 2026" },
  { id: "5", title: "Resumen: FC Norte 0-2 Platzi FC", duration: "4:10", category: "Resúmenes", date: "25 Feb 2026" },
  { id: "6", title: "Conferencia de prensa: Roberto Sánchez", duration: "8:20", category: "Entrevistas", date: "24 Feb 2026" },
];

export default function VideosPage() {
  return (
    <div className="py-8">
      <h1 className="text-3xl font-bold mb-2">Videos</h1>
      <p className="text-foreground-secondary mb-8">Resúmenes, entrevistas y contenido exclusivo</p>

      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {mockVideos.map((video) => (
          <Card key={video.id} className="group overflow-hidden hover:shadow-md transition-shadow cursor-pointer">
            <div className="relative aspect-video bg-primary/5 flex items-center justify-center">
              <div className="absolute inset-0 bg-black/0 group-hover:bg-black/20 transition-colors flex items-center justify-center">
                <div className="h-12 w-12 rounded-full bg-white/90 flex items-center justify-center opacity-80 group-hover:opacity-100 transition-opacity">
                  <Play className="h-5 w-5 text-primary ml-0.5" />
                </div>
              </div>
              <span className="absolute bottom-2 right-2 rounded bg-black/70 px-1.5 py-0.5 text-xs text-white">
                {video.duration}
              </span>
            </div>
            <CardContent className="p-4">
              <div className="flex items-center gap-2 mb-1.5">
                <Badge variant="outline">{video.category}</Badge>
                <span className="text-xs text-muted">{video.date}</span>
              </div>
              <p className="font-semibold text-sm group-hover:text-primary transition-colors line-clamp-2">{video.title}</p>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
