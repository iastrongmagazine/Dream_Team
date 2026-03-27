import type { Metadata } from "next";
import Link from "next/link";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Users } from "lucide-react";

export const metadata: Metadata = {
  title: "Equipo",
  description: "Plantilla del primer equipo del Platzi FC.",
};

const positions = ["Porteros", "Defensas", "Centrocampistas", "Delanteros"] as const;

const mockPlayers = [
  { id: "1", name: "Carlos Martínez", position: "Porteros", number: 1, nationality: "Colombia", slug: "carlos-martinez" },
  { id: "2", name: "Andrés López", position: "Porteros", number: 13, nationality: "México", slug: "andres-lopez" },
  { id: "3", name: "Diego Ramírez", position: "Defensas", number: 2, nationality: "Argentina", slug: "diego-ramirez" },
  { id: "4", name: "Lucas Torres", position: "Defensas", number: 4, nationality: "Colombia", slug: "lucas-torres" },
  { id: "5", name: "Felipe Herrera", position: "Defensas", number: 5, nationality: "Chile", slug: "felipe-herrera" },
  { id: "6", name: "Juan García", position: "Defensas", number: 3, nationality: "Perú", slug: "juan-garcia" },
  { id: "7", name: "Mateo Silva", position: "Centrocampistas", number: 8, nationality: "Colombia", slug: "mateo-silva" },
  { id: "8", name: "Santiago Cruz", position: "Centrocampistas", number: 10, nationality: "Argentina", slug: "santiago-cruz" },
  { id: "9", name: "Pablo Moreno", position: "Centrocampistas", number: 6, nationality: "México", slug: "pablo-moreno" },
  { id: "10", name: "Sebastián Rojas", position: "Delanteros", number: 9, nationality: "Colombia", slug: "sebastian-rojas" },
  { id: "11", name: "Nicolás Vargas", position: "Delanteros", number: 11, nationality: "Ecuador", slug: "nicolas-vargas" },
  { id: "12", name: "Tomás Fernández", position: "Delanteros", number: 7, nationality: "Uruguay", slug: "tomas-fernandez" },
];

export default function EquipoPage() {
  return (
    <div className="py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold">Primer Equipo</h1>
        <p className="mt-1 text-foreground-secondary">Plantilla temporada 2025-2026</p>
      </div>

      {positions.map((pos) => {
        const players = mockPlayers.filter((p) => p.position === pos);
        return (
          <section key={pos} className="mb-10">
            <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
              <Users className="h-5 w-5 text-primary" />
              {pos}
            </h2>
            <div className="grid grid-cols-2 gap-4 sm:grid-cols-3 lg:grid-cols-4">
              {players.map((player) => (
                <Link key={player.id} href={`/equipo/${player.slug}`}>
                  <Card className="group overflow-hidden hover:shadow-md transition-shadow h-full">
                    <div className="aspect-[3/4] bg-primary/5 flex items-center justify-center">
                      <span className="text-5xl font-bold text-primary/10">{player.number}</span>
                    </div>
                    <CardContent className="p-4">
                      <p className="font-semibold group-hover:text-primary transition-colors">{player.name}</p>
                      <div className="flex items-center gap-2 mt-1">
                        <Badge variant="outline" className="text-xs">{player.nationality}</Badge>
                        <span className="text-xs text-muted">#{player.number}</span>
                      </div>
                    </CardContent>
                  </Card>
                </Link>
              ))}
            </div>
          </section>
        );
      })}
    </div>
  );
}
