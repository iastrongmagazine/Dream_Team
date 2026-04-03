import type { Metadata } from "next";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Calendar, Filter } from "lucide-react";

export const metadata: Metadata = {
  title: "Partidos",
  description: "Calendario de partidos y resultados del Platzi FC.",
};

const mockMatches = [
  { id: "1", home: "Platzi FC", away: "Real Ejemplo", homeScore: null, awayScore: null, date: "8 Mar 2026 · 20:00h", competition: "Liga Nacional", matchday: 24, status: "scheduled" as const },
  { id: "2", home: "FC Norte", away: "Platzi FC", homeScore: null, awayScore: null, date: "15 Mar 2026 · 18:30h", competition: "Copa Nacional", matchday: null, status: "scheduled" as const },
  { id: "3", home: "Platzi FC", away: "Deportivo Sur", homeScore: 3, awayScore: 1, date: "1 Mar 2026", competition: "Liga Nacional", matchday: 23, status: "finished" as const },
  { id: "4", home: "FC Norte", away: "Platzi FC", homeScore: 0, awayScore: 2, date: "25 Feb 2026", competition: "Copa Nacional", matchday: null, status: "finished" as const },
  { id: "5", home: "Platzi FC", away: "Atlético Centro", homeScore: 1, awayScore: 1, date: "18 Feb 2026", competition: "Liga Nacional", matchday: 22, status: "finished" as const },
];

export default function PartidosPage() {
  return (
    <div className="py-8">
      <div className="flex flex-col gap-6 sm:flex-row sm:items-center sm:justify-between mb-8">
        <div>
          <h1 className="text-3xl font-bold">Partidos</h1>
          <p className="mt-1 text-foreground-secondary">Calendario y resultados del Platzi FC</p>
        </div>
        <div className="flex items-center gap-2">
          <button className="inline-flex items-center gap-2 rounded-md border border-border px-3 py-2 text-sm hover:bg-surface-alt transition-colors">
            <Filter className="h-4 w-4" />
            Filtros
          </button>
        </div>
      </div>

      <div className="space-y-3">
        {mockMatches.map((match) => (
          <Card key={match.id} className="hover:shadow-md transition-shadow">
            <CardContent className="flex items-center gap-4 p-4 sm:p-5">
              <div className="hidden sm:flex sm:flex-col sm:items-center sm:w-20 sm:shrink-0">
                <Calendar className="h-4 w-4 text-muted mb-1" />
                <span className="text-xs text-muted text-center">{match.date}</span>
              </div>
              <div className="flex-1 min-w-0">
                <div className="flex items-center gap-2 mb-1 sm:hidden">
                  <span className="text-xs text-muted">{match.date}</span>
                </div>
                <div className="flex items-center gap-3">
                  <span className={`flex-1 truncate text-right text-sm font-medium ${match.home === "Platzi FC" ? "text-primary font-bold" : ""}`}>
                    {match.home}
                  </span>
                  {match.status === "finished" ? (
                    <div className="flex items-center gap-1.5 rounded bg-surface-alt px-3 py-1 shrink-0">
                      <span className="text-base font-bold">{match.homeScore}</span>
                      <span className="text-muted">-</span>
                      <span className="text-base font-bold">{match.awayScore}</span>
                    </div>
                  ) : (
                    <Badge variant="info" className="shrink-0">Próximo</Badge>
                  )}
                  <span className={`flex-1 truncate text-sm font-medium ${match.away === "Platzi FC" ? "text-primary font-bold" : ""}`}>
                    {match.away}
                  </span>
                </div>
              </div>
              <div className="hidden md:block md:w-36 md:shrink-0 md:text-right">
                <Badge variant="outline">{match.competition}</Badge>
                {match.matchday && (
                  <span className="block mt-1 text-xs text-muted">Jornada {match.matchday}</span>
                )}
              </div>
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}
