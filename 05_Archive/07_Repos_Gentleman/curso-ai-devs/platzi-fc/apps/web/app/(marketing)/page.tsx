import Link from "next/link";
import type { Metadata } from "next";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import {
  Calendar,
  Trophy,
  Newspaper,
  ShoppingBag,
  Ticket,
  Users,
  ArrowRight,
  Play,
} from "lucide-react";
import {
  getNextMatch,
  getRecentResults,
  getFeaturedNews,
  getStandings,
  getSponsors,
} from "@/lib/supabase/queries";

export const metadata: Metadata = {
  title: "Platzi FC — El Club del Futuro",
  description:
    "Sitio oficial del Platzi FC. Noticias, partidos, equipo, entradas y tienda.",
};

// eslint-disable-next-line @typescript-eslint/no-explicit-any
function unwrap(val: any): any {
  return Array.isArray(val) ? val[0] ?? null : val ?? null;
}

function formatDate(dateStr: string | null) {
  if (!dateStr) return "";
  return new Date(dateStr).toLocaleDateString("es-CO", {
    weekday: "long",
    day: "numeric",
    month: "long",
  });
}

function formatTime(dateStr: string | null) {
  if (!dateStr) return "";
  return new Date(dateStr).toLocaleTimeString("es-CO", {
    hour: "2-digit",
    minute: "2-digit",
  });
}

function formatShortDate(dateStr: string | null) {
  if (!dateStr) return "";
  return new Date(dateStr).toLocaleDateString("es-CO", {
    day: "numeric",
    month: "short",
  });
}

type NextMatch = Awaited<ReturnType<typeof getNextMatch>>;

function HeroSection({ match }: { match: NextMatch }) {
  if (!match) {
    return (
      <section className="relative bg-primary text-white">
        <div className="mx-auto max-w-7xl px-4 py-20 lg:py-28 text-center">
          <h1 className="text-4xl font-bold tracking-tight lg:text-6xl">Platzi FC</h1>
          <p className="mt-4 text-lg text-white/70">El Club del Futuro</p>
        </div>
      </section>
    );
  }

  const home = unwrap(match.home_team) as { name: string; short_name: string | null } | null;
  const away = unwrap(match.away_team) as { name: string; short_name: string | null } | null;
  const comp = unwrap(match.competition) as { name: string; short_name: string | null } | null;
  const stad = unwrap(match.stadium) as { name: string } | null;

  return (
    <section className="relative bg-primary text-white">
      <div className="mx-auto max-w-7xl px-4 py-20 lg:py-28">
        <div className="grid gap-8 lg:grid-cols-2 lg:items-center">
          <div>
            <Badge variant="default" className="mb-4 bg-secondary text-primary-dark font-semibold">
              Próximo Partido
            </Badge>
            <h1 className="text-4xl font-bold tracking-tight lg:text-6xl">
              {home?.name ?? "Local"} vs {away?.name ?? "Visitante"}
            </h1>
            <p className="mt-4 text-lg text-white/70">
              {formatDate(match.played_at)} · {formatTime(match.played_at)}
              {stad ? ` · ${stad.name}` : ""}
            </p>
            <p className="mt-2 text-white/50">
              {comp?.name ?? ""}
              {match.matchday ? ` · Jornada ${match.matchday}` : ""}
            </p>
            <div className="mt-8 flex flex-wrap gap-4">
              <Link href="/entradas">
                <Button variant="secondary" size="lg">
                  <Ticket className="mr-2 h-5 w-5" />
                  Comprar Entradas
                </Button>
              </Link>
              <Link href="/partidos">
                <Button variant="outline" size="lg" className="border-white/30 text-white hover:bg-white/10 hover:text-white">
                  Ver Calendario
                </Button>
              </Link>
            </div>
          </div>
          <div className="hidden lg:flex lg:justify-center">
            <div className="flex h-64 w-64 items-center justify-center rounded-full bg-white/5 border border-white/10">
              <div className="text-center">
                <div className="text-6xl font-bold text-secondary">{home?.short_name ?? "LOC"}</div>
                <div className="mt-2 text-sm text-white/50">vs</div>
                <div className="mt-1 text-2xl font-bold text-white/80">{away?.short_name ?? "VIS"}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

type RecentMatch = Awaited<ReturnType<typeof getRecentResults>>[number];

function RecentResults({ results }: { results: RecentMatch[] }) {
  if (results.length === 0) return null;

  return (
    <section className="py-16">
      <div className="mx-auto max-w-7xl px-4">
        <div className="flex items-center justify-between mb-8">
          <h2 className="text-2xl font-bold">Resultados Recientes</h2>
          <Link href="/partidos?view=results" className="inline-flex items-center gap-1 text-sm font-medium text-primary hover:underline">
            Ver todos <ArrowRight className="h-4 w-4" />
          </Link>
        </div>
        <div className="grid gap-4 md:grid-cols-3">
          {results.map((match) => {
            const home = unwrap(match.home_team) as { name: string; is_own_team: boolean } | null;
            const away = unwrap(match.away_team) as { name: string; is_own_team: boolean } | null;
            const comp = unwrap(match.competition) as { name: string; short_name: string | null } | null;
            return (
              <Card key={match.id} className="hover:shadow-md transition-shadow">
                <CardContent className="p-5">
                  <p className="text-xs text-muted mb-3">
                    {comp?.short_name ?? comp?.name ?? ""} · {formatShortDate(match.played_at)}
                  </p>
                  <div className="flex items-center">
                    <span className={`flex-1 truncate text-right text-sm font-medium ${home?.is_own_team ? "text-primary font-bold" : ""}`}>
                      {home?.name ?? "Local"}
                    </span>
                    <div className="flex items-center gap-2 rounded-md bg-surface-alt px-3 py-1 mx-3 shrink-0">
                      <span className="text-lg font-bold">{match.home_score ?? 0}</span>
                      <span className="text-muted">-</span>
                      <span className="text-lg font-bold">{match.away_score ?? 0}</span>
                    </div>
                    <span className={`flex-1 truncate text-sm font-medium ${away?.is_own_team ? "text-primary font-bold" : ""}`}>
                      {away?.name ?? "Visitante"}
                    </span>
                  </div>
                </CardContent>
              </Card>
            );
          })}
        </div>
      </div>
    </section>
  );
}

type NewsItem = Awaited<ReturnType<typeof getFeaturedNews>>[number];

function FeaturedNews({ news }: { news: NewsItem[] }) {
  if (news.length === 0) return null;

  return (
    <section className="bg-surface-alt py-16">
      <div className="mx-auto max-w-7xl px-4">
        <div className="flex items-center justify-between mb-8">
          <h2 className="text-2xl font-bold">Noticias Destacadas</h2>
          <Link href="/noticias" className="inline-flex items-center gap-1 text-sm font-medium text-primary hover:underline">
            Ver todas <ArrowRight className="h-4 w-4" />
          </Link>
        </div>
        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-4">
          {news.map((article) => (
            <Link key={article.id} href={`/noticias/${article.slug}`}>
              <Card className="group overflow-hidden hover:shadow-md transition-shadow h-full">
                <div className="aspect-video bg-primary/5 flex items-center justify-center">
                  <Newspaper className="h-10 w-10 text-primary/20" />
                </div>
                <CardHeader className="p-4 pb-2">
                  <div className="flex items-center gap-2 mb-1">
                    <Badge variant="outline">{article.tags?.[0] ?? "General"}</Badge>
                    <span className="text-xs text-muted">{formatShortDate(article.published_at)}</span>
                  </div>
                  <CardTitle className="text-base group-hover:text-primary transition-colors line-clamp-2">
                    {article.title}
                  </CardTitle>
                </CardHeader>
                <CardContent className="p-4 pt-0">
                  <p className="text-sm text-foreground-secondary line-clamp-2">{article.excerpt}</p>
                </CardContent>
              </Card>
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}

type StandingRow = Awaited<ReturnType<typeof getStandings>>[number];

function StandingsPreview({ standings }: { standings: StandingRow[] }) {
  if (standings.length === 0) return null;

  return (
    <section className="py-16">
      <div className="mx-auto max-w-7xl px-4">
        <div className="flex items-center justify-between mb-8">
          <h2 className="text-2xl font-bold">Clasificación</h2>
          <Link href="/competicion" className="inline-flex items-center gap-1 text-sm font-medium text-primary hover:underline">
            Tabla completa <ArrowRight className="h-4 w-4" />
          </Link>
        </div>
        <Card>
          <CardContent className="p-0">
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-border">
                  <th className="px-4 py-3 text-left font-medium text-muted" scope="col">#</th>
                  <th className="px-4 py-3 text-left font-medium text-muted" scope="col">Equipo</th>
                  <th className="px-4 py-3 text-center font-medium text-muted" scope="col">PJ</th>
                  <th className="px-4 py-3 text-center font-medium text-muted" scope="col">DG</th>
                  <th className="px-4 py-3 text-center font-medium text-muted" scope="col">Pts</th>
                </tr>
              </thead>
              <tbody>
                {standings.map((row) => {
                  const team = unwrap(row.team) as { name: string; is_own_team: boolean } | null;
                  const isOwn = team?.is_own_team ?? false;
                  const diff = row.goal_difference ?? 0;
                  return (
                    <tr
                      key={row.id}
                      className={`border-b border-border last:border-0 ${isOwn ? "bg-accent" : ""}`}
                    >
                      <td className="px-4 py-3 font-medium">{row.position}</td>
                      <td className={`px-4 py-3 ${isOwn ? "font-bold text-primary" : ""}`}>
                        {team?.name ?? "—"}
                      </td>
                      <td className="px-4 py-3 text-center text-muted">{row.played}</td>
                      <td className="px-4 py-3 text-center text-muted">
                        {diff > 0 ? `+${diff}` : diff}
                      </td>
                      <td className="px-4 py-3 text-center font-bold">{row.points}</td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </CardContent>
        </Card>
      </div>
    </section>
  );
}

function QuickLinks() {
  const links = [
    { icon: Calendar, label: "Partidos", href: "/partidos", desc: "Calendario y resultados" },
    { icon: Users, label: "Equipo", href: "/equipo", desc: "Plantilla y cuerpo técnico" },
    { icon: Trophy, label: "Competición", href: "/competicion", desc: "Tablas y estadísticas" },
    { icon: Ticket, label: "Entradas", href: "/entradas", desc: "Compra tus tickets" },
    { icon: ShoppingBag, label: "Tienda", href: "/tienda", desc: "Productos oficiales" },
    { icon: Play, label: "Media", href: "/media/videos", desc: "Videos y galerías" },
  ];

  return (
    <section className="bg-primary text-white py-16">
      <div className="mx-auto max-w-7xl px-4">
        <h2 className="text-2xl font-bold mb-8 text-center">Explora Platzi FC</h2>
        <div className="grid grid-cols-2 gap-4 md:grid-cols-3 lg:grid-cols-6">
          {links.map((item) => (
            <Link
              key={item.href}
              href={item.href}
              className="group flex flex-col items-center gap-3 rounded-lg border border-white/10 bg-white/5 p-6 text-center transition-colors hover:bg-white/10"
            >
              <item.icon className="h-8 w-8 text-secondary" />
              <div>
                <div className="font-semibold">{item.label}</div>
                <div className="mt-1 text-xs text-white/50">{item.desc}</div>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </section>
  );
}

type SponsorItem = Awaited<ReturnType<typeof getSponsors>>[number];

function SponsorsBar({ sponsors }: { sponsors: SponsorItem[] }) {
  if (sponsors.length === 0) return null;

  return (
    <section className="py-12 border-t border-border">
      <div className="mx-auto max-w-7xl px-4">
        <p className="text-center text-xs font-medium uppercase tracking-wider text-muted mb-6">
          Patrocinadores Oficiales
        </p>
        <div className="flex flex-wrap items-center justify-center gap-8">
          {sponsors.map((sponsor) => (
            <a
              key={sponsor.id}
              href={sponsor.website ?? "#"}
              target="_blank"
              rel="noopener noreferrer"
              className="flex h-12 w-32 items-center justify-center rounded-md bg-surface-alt text-xs font-medium text-muted hover:bg-surface-alt/80 transition-colors"
            >
              {sponsor.name}
            </a>
          ))}
        </div>
      </div>
    </section>
  );
}

export default async function HomePage() {
  const [nextMatch, recentResults, featuredNews, standings, sponsors] =
    await Promise.all([
      getNextMatch(),
      getRecentResults(),
      getFeaturedNews(),
      getStandings(),
      getSponsors(),
    ]);

  return (
    <>
      <HeroSection match={nextMatch} />
      <RecentResults results={recentResults} />
      <FeaturedNews news={featuredNews} />
      <StandingsPreview standings={standings} />
      <QuickLinks />
      <SponsorsBar sponsors={sponsors} />
    </>
  );
}
