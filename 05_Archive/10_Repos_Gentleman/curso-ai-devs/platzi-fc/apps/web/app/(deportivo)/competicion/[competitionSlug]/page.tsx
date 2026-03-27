import type { Metadata } from "next";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

export async function generateMetadata({
  params,
}: {
  params: Promise<{ competitionSlug: string }>;
}): Promise<Metadata> {
  const { competitionSlug } = await params;
  return { title: `Competición: ${competitionSlug}` };
}

const standings = [
  { pos: 1, team: "Platzi FC", played: 23, won: 18, drawn: 4, lost: 1, gf: 52, ga: 24, pts: 58 },
  { pos: 2, team: "Real Ejemplo", played: 23, won: 17, drawn: 4, lost: 2, gf: 48, ga: 26, pts: 55 },
  { pos: 3, team: "Deportivo Sur", played: 23, won: 15, drawn: 5, lost: 3, gf: 40, ga: 25, pts: 50 },
  { pos: 4, team: "Atlético Centro", played: 23, won: 14, drawn: 5, lost: 4, gf: 38, ga: 26, pts: 47 },
  { pos: 5, team: "FC Norte", played: 23, won: 13, drawn: 5, lost: 5, gf: 35, ga: 27, pts: 44 },
  { pos: 6, team: "Unión Este", played: 23, won: 11, drawn: 6, lost: 6, gf: 30, ga: 28, pts: 39 },
];

export default async function CompetitionDetailPage({
  params,
}: {
  params: Promise<{ competitionSlug: string }>;
}) {
  await params;

  return (
    <div className="py-8">
      <h1 className="text-3xl font-bold mb-2">Liga Nacional</h1>
      <p className="text-foreground-secondary mb-8">Temporada 2025-2026 · Clasificación</p>

      <Card>
        <CardHeader>
          <CardTitle>Tabla de Posiciones</CardTitle>
        </CardHeader>
        <CardContent className="p-0">
          <div className="overflow-x-auto">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-border bg-surface-alt">
                  <th className="px-4 py-3 text-left font-medium text-muted" scope="col">#</th>
                  <th className="px-4 py-3 text-left font-medium text-muted" scope="col">Equipo</th>
                  <th className="px-4 py-3 text-center font-medium text-muted" scope="col">PJ</th>
                  <th className="px-4 py-3 text-center font-medium text-muted" scope="col">PG</th>
                  <th className="px-4 py-3 text-center font-medium text-muted" scope="col">PE</th>
                  <th className="px-4 py-3 text-center font-medium text-muted" scope="col">PP</th>
                  <th className="px-4 py-3 text-center font-medium text-muted" scope="col">GF</th>
                  <th className="px-4 py-3 text-center font-medium text-muted" scope="col">GC</th>
                  <th className="px-4 py-3 text-center font-medium text-muted" scope="col">Pts</th>
                </tr>
              </thead>
              <tbody>
                {standings.map((row) => (
                  <tr key={row.pos} className={`border-b border-border last:border-0 ${row.team === "Platzi FC" ? "bg-accent font-semibold" : ""}`}>
                    <td className="px-4 py-3">{row.pos}</td>
                    <td className={`px-4 py-3 ${row.team === "Platzi FC" ? "text-primary" : ""}`}>{row.team}</td>
                    <td className="px-4 py-3 text-center">{row.played}</td>
                    <td className="px-4 py-3 text-center">{row.won}</td>
                    <td className="px-4 py-3 text-center">{row.drawn}</td>
                    <td className="px-4 py-3 text-center">{row.lost}</td>
                    <td className="px-4 py-3 text-center">{row.gf}</td>
                    <td className="px-4 py-3 text-center">{row.ga}</td>
                    <td className="px-4 py-3 text-center font-bold">{row.pts}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
