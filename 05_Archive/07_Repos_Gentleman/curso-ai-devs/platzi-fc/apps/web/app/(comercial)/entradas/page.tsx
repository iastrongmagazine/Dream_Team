import type { Metadata } from "next";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Badge } from "@/components/ui/badge";
import { Ticket, MapPin, Calendar } from "lucide-react";

export const metadata: Metadata = {
  title: "Entradas",
  description: "Compra entradas para los partidos del Platzi FC.",
};

const upcomingMatches = [
  { id: "1", opponent: "Real Ejemplo", date: "8 Mar 2026 · 20:00h", venue: "Platzi Arena", competition: "Liga Nacional", priceFrom: 25 },
  { id: "2", opponent: "Atlético Centro", date: "22 Mar 2026 · 18:30h", venue: "Platzi Arena", competition: "Liga Nacional", priceFrom: 20 },
  { id: "3", opponent: "Unión Este", date: "5 Abr 2026 · 20:00h", venue: "Platzi Arena", competition: "Copa Nacional", priceFrom: 30 },
];

export default function EntradasPage() {
  return (
    <div className="py-8">
      <div className="mb-8">
        <h1 className="text-3xl font-bold">Entradas</h1>
        <p className="mt-1 text-foreground-secondary">Compra tus entradas para los próximos partidos en casa</p>
      </div>

      <div className="grid gap-4 mb-12">
        {upcomingMatches.map((match) => (
          <Card key={match.id} className="hover:shadow-md transition-shadow">
            <CardContent className="flex flex-col gap-4 p-5 sm:flex-row sm:items-center sm:justify-between">
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-1">
                  <Badge variant="outline">{match.competition}</Badge>
                </div>
                <h2 className="text-lg font-bold">Platzi FC vs {match.opponent}</h2>
                <div className="flex flex-wrap gap-4 mt-2 text-sm text-muted">
                  <span className="flex items-center gap-1"><Calendar className="h-3.5 w-3.5" /> {match.date}</span>
                  <span className="flex items-center gap-1"><MapPin className="h-3.5 w-3.5" /> {match.venue}</span>
                </div>
              </div>
              <div className="flex items-center gap-4 shrink-0">
                <p className="text-sm text-muted">Desde <span className="text-lg font-bold text-foreground">{match.priceFrom}€</span></p>
                <Button variant="primary">
                  <Ticket className="mr-2 h-4 w-4" /> Comprar
                </Button>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      <Card className="bg-primary text-white">
        <CardHeader>
          <CardTitle className="text-white">Abonos de Temporada</CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-white/70 mb-4">Asegura tu asiento para todos los partidos de casa. Los abonados disfrutan de descuentos exclusivos y acceso prioritario.</p>
          <Button variant="secondary">Ver planes de abono</Button>
        </CardContent>
      </Card>
    </div>
  );
}
