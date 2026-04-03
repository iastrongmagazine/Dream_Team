import type { Metadata } from "next";
import Link from "next/link";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Trophy } from "lucide-react";

export const metadata: Metadata = {
  title: "Competiciones",
  description: "Competiciones del Platzi FC: tablas, calendarios y estadísticas.",
};

const competitions = [
  { name: "Liga Nacional", slug: "liga-nacional", type: "Liga", season: "2025-2026", position: "1°", points: 58 },
  { name: "Copa Nacional", slug: "copa-nacional", type: "Copa", season: "2025-2026", position: "Cuartos", points: null },
  { name: "Supercopa", slug: "supercopa", type: "Supercopa", season: "2025-2026", position: "Campeón", points: null },
];

export default function CompeticionPage() {
  return (
    <div className="py-8">
      <h1 className="text-3xl font-bold mb-2">Competiciones</h1>
      <p className="text-foreground-secondary mb-8">Temporada 2025-2026</p>
      <div className="grid gap-4 md:grid-cols-3">
        {competitions.map((comp) => (
          <Link key={comp.slug} href={`/competicion/${comp.slug}`}>
            <Card className="group hover:shadow-md transition-shadow h-full">
              <CardHeader className="flex flex-row items-center gap-3">
                <Trophy className="h-8 w-8 text-primary shrink-0" />
                <div>
                  <CardTitle className="group-hover:text-primary transition-colors">{comp.name}</CardTitle>
                  <p className="text-xs text-muted mt-0.5">{comp.type} · {comp.season}</p>
                </div>
              </CardHeader>
              <CardContent>
                <p className="text-sm text-foreground-secondary">
                  {comp.points ? `Posición: ${comp.position} · ${comp.points} pts` : `Estado: ${comp.position}`}
                </p>
              </CardContent>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}
