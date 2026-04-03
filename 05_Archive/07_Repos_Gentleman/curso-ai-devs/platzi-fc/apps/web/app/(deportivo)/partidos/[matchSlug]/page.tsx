import type { Metadata } from "next";
import Link from "next/link";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { MapPin, Clock, Users, Ticket } from "lucide-react";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ matchSlug: string }>;
}): Promise<Metadata> {
  const { matchSlug } = await params;
  return {
    title: `Partido: ${matchSlug}`,
    description: `Detalle del partido ${matchSlug} del Platzi FC.`,
  };
}

export default async function MatchDetailPage({
  params,
}: {
  params: Promise<{ matchSlug: string }>;
}) {
  const { matchSlug } = await params;

  return (
    <div className="py-8">
      {/* Scoreboard */}
      <div className="rounded-xl bg-primary p-8 text-white text-center mb-8">
        <div className="flex items-center justify-between gap-2 mb-2">
          <Badge variant="default" className="bg-white/20 text-white">Liga Nacional</Badge>
          <span className="text-sm text-white/60">Jornada 24</span>
        </div>
        <div className="flex items-center justify-center gap-8 my-6">
          <div className="text-center">
            <div className="h-16 w-16 mx-auto rounded-full bg-white/10 flex items-center justify-center text-2xl font-bold text-secondary">
              PFC
            </div>
            <p className="mt-2 font-semibold">Platzi FC</p>
          </div>
          <div className="flex items-center gap-3">
            <span className="text-5xl font-bold">3</span>
            <span className="text-2xl text-white/40">-</span>
            <span className="text-5xl font-bold">1</span>
          </div>
          <div className="text-center">
            <div className="h-16 w-16 mx-auto rounded-full bg-white/10 flex items-center justify-center text-2xl font-bold">
              DS
            </div>
            <p className="mt-2 font-semibold">Deportivo Sur</p>
          </div>
        </div>
        <Badge variant="default" className="bg-success text-white">Finalizado</Badge>
      </div>

      {/* Match Info */}
      <div className="grid gap-4 md:grid-cols-3 mb-8">
        <Card>
          <CardContent className="flex items-center gap-3 p-4">
            <Clock className="h-5 w-5 text-primary shrink-0" />
            <div>
              <p className="text-sm text-muted">Fecha y hora</p>
              <p className="font-medium">1 Mar 2026 · 20:00h</p>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="flex items-center gap-3 p-4">
            <MapPin className="h-5 w-5 text-primary shrink-0" />
            <div>
              <p className="text-sm text-muted">Estadio</p>
              <p className="font-medium">Platzi Arena</p>
            </div>
          </CardContent>
        </Card>
        <Card>
          <CardContent className="flex items-center gap-3 p-4">
            <Users className="h-5 w-5 text-primary shrink-0" />
            <div>
              <p className="text-sm text-muted">Asistencia</p>
              <p className="font-medium">32,450</p>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Tabs placeholder */}
      <div className="flex gap-1 border-b border-border mb-6">
        {["Resumen", "Estadísticas", "Alineaciones", "Minuto a minuto"].map((tab, i) => (
          <button
            key={tab}
            className={`px-4 py-2.5 text-sm font-medium transition-colors ${i === 0 ? "border-b-2 border-primary text-primary" : "text-muted hover:text-foreground"}`}
          >
            {tab}
          </button>
        ))}
      </div>

      {/* Summary placeholder */}
      <Card>
        <CardContent className="p-6">
          <h2 className="text-lg font-semibold mb-4">Resumen del partido</h2>
          <p className="text-foreground-secondary leading-relaxed">
            Platzi FC se impuso con autoridad ante Deportivo Sur con un contundente 3-1.
            El equipo verde tomó la iniciativa desde el primer minuto y se fue al descanso
            con una ventaja de 2-0 gracias a los goles del capitán en los minutos 15 y 38.
            En la segunda parte, Deportivo Sur descontó al 62&apos;, pero Platzi FC sentenció
            el encuentro al 78&apos; con un gran gol de su delantero estrella.
          </p>
        </CardContent>
      </Card>

      {/* CTA Entradas */}
      <div className="mt-8 text-center">
        <Link href="/entradas">
          <Button variant="secondary" size="lg">
            <Ticket className="mr-2 h-5 w-5" />
            Comprar entradas para el próximo partido
          </Button>
        </Link>
      </div>
    </div>
  );
}
