import type { Metadata } from "next";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ playerSlug: string }>;
}): Promise<Metadata> {
  const { playerSlug } = await params;
  return {
    title: `Jugador: ${playerSlug}`,
    description: `Perfil del jugador ${playerSlug} del Platzi FC.`,
  };
}

export default async function PlayerDetailPage({
  params,
}: {
  params: Promise<{ playerSlug: string }>;
}) {
  const { playerSlug } = await params;

  return (
    <div className="py-8">
      {/* Player Header */}
      <div className="rounded-xl bg-primary p-8 text-white mb-8">
        <div className="flex flex-col items-center gap-6 md:flex-row">
          <div className="h-32 w-32 rounded-full bg-white/10 flex items-center justify-center text-5xl font-bold text-secondary shrink-0">
            9
          </div>
          <div>
            <Badge variant="default" className="bg-secondary text-primary-dark mb-2">Delantero</Badge>
            <h1 className="text-3xl font-bold">Sebastián Rojas</h1>
            <p className="text-white/60 mt-1">Colombia · #9 · 26 años</p>
          </div>
        </div>
      </div>

      {/* Stats + Bio */}
      <div className="grid gap-6 md:grid-cols-3">
        <div className="md:col-span-2 space-y-6">
          <Card>
            <CardHeader>
              <CardTitle>Estadísticas Temporada 2025-2026</CardTitle>
            </CardHeader>
            <CardContent>
              <div className="grid grid-cols-2 gap-4 sm:grid-cols-4">
                {[
                  { label: "Partidos", value: "23" },
                  { label: "Goles", value: "14" },
                  { label: "Asistencias", value: "7" },
                  { label: "Min. jugados", value: "1,890" },
                  { label: "Tiros a puerta", value: "42" },
                  { label: "Amarillas", value: "3" },
                  { label: "Rojas", value: "0" },
                  { label: "Rating", value: "7.8" },
                ].map((stat) => (
                  <div key={stat.label} className="rounded-lg bg-surface-alt p-3 text-center">
                    <p className="text-2xl font-bold text-primary">{stat.value}</p>
                    <p className="text-xs text-muted mt-1">{stat.label}</p>
                  </div>
                ))}
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle>Biografía</CardTitle>
            </CardHeader>
            <CardContent>
              <p className="text-foreground-secondary leading-relaxed">
                Sebastián Rojas es el máximo goleador del Platzi FC en la temporada actual.
                Nacido en Medellín, Colombia, se formó en las categorías inferiores del club
                antes de debutar con el primer equipo en 2022. Su velocidad y capacidad de
                definición lo convierten en una de las mayores amenazas ofensivas de la liga.
              </p>
            </CardContent>
          </Card>
        </div>

        <div className="space-y-6">
          <Card>
            <CardHeader>
              <CardTitle>Datos personales</CardTitle>
            </CardHeader>
            <CardContent className="space-y-3">
              {[
                { label: "Fecha de nacimiento", value: "15/03/1999" },
                { label: "Nacionalidad", value: "Colombia" },
                { label: "Altura", value: "1.82 m" },
                { label: "Peso", value: "76 kg" },
                { label: "Pie hábil", value: "Derecho" },
              ].map((item) => (
                <div key={item.label} className="flex justify-between text-sm">
                  <span className="text-muted">{item.label}</span>
                  <span className="font-medium">{item.value}</span>
                </div>
              ))}
            </CardContent>
          </Card>
        </div>
      </div>
    </div>
  );
}
