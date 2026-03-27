import type { Metadata } from "next";
import Link from "next/link";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import { Newspaper } from "lucide-react";
import { getAllNews } from "@/lib/supabase/queries";

export const metadata: Metadata = {
  title: "Noticias",
  description: "Últimas noticias del Platzi FC.",
};

function formatDate(dateStr: string | null) {
  if (!dateStr) return "";
  return new Date(dateStr).toLocaleDateString("es-CO", {
    day: "numeric",
    month: "short",
    year: "numeric",
  });
}

export default async function NoticiasPage() {
  const articles = await getAllNews();
  const featured = articles.find((a) => a.is_featured) ?? articles[0] ?? null;
  const rest = articles.filter((a) => a.id !== featured?.id);

  return (
    <div className="py-8">
      <h1 className="text-3xl font-bold mb-8">Noticias</h1>

      {featured && (
        <Link href={`/noticias/${featured.slug}`} className="block mb-8">
          <Card className="group overflow-hidden hover:shadow-lg transition-shadow md:flex">
            <div className="aspect-video md:aspect-auto md:w-1/2 bg-primary/5 flex items-center justify-center">
              <Newspaper className="h-16 w-16 text-primary/20" />
            </div>
            <div className="flex-1 p-6">
              <Badge variant="default" className="mb-2">{featured.tags?.[0] ?? "General"}</Badge>
              <h2 className="text-2xl font-bold group-hover:text-primary transition-colors mb-2">{featured.title}</h2>
              <p className="text-foreground-secondary mb-3">{featured.excerpt}</p>
              <span className="text-sm text-muted">{formatDate(featured.published_at)}</span>
            </div>
          </Card>
        </Link>
      )}

      <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
        {rest.map((article) => (
          <Link key={article.slug} href={`/noticias/${article.slug}`}>
            <Card className="group overflow-hidden hover:shadow-md transition-shadow h-full">
              <div className="aspect-video bg-primary/5 flex items-center justify-center">
                <Newspaper className="h-10 w-10 text-primary/20" />
              </div>
              <CardHeader className="p-4 pb-2">
                <div className="flex items-center gap-2 mb-1">
                  <Badge variant="outline">{article.tags?.[0] ?? "General"}</Badge>
                  <span className="text-xs text-muted">{formatDate(article.published_at)}</span>
                </div>
                <CardTitle className="text-base group-hover:text-primary transition-colors">{article.title}</CardTitle>
              </CardHeader>
              <CardContent className="p-4 pt-0">
                <p className="text-sm text-foreground-secondary line-clamp-2">{article.excerpt}</p>
              </CardContent>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}
