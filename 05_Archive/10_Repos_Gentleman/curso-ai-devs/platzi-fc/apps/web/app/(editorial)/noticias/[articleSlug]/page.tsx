import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Badge } from "@/components/ui/badge";
import { Card, CardContent } from "@/components/ui/card";
import { Clock, ArrowLeft } from "lucide-react";
import { getNewsBySlug, getRelatedNews } from "@/lib/supabase/queries";

function formatDate(dateStr: string | null) {
  if (!dateStr) return "";
  return new Date(dateStr).toLocaleDateString("es-CO", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
}

export async function generateMetadata({
  params,
}: {
  params: Promise<{ articleSlug: string }>;
}): Promise<Metadata> {
  const { articleSlug } = await params;
  const article = await getNewsBySlug(articleSlug);
  if (!article) return { title: "Noticia no encontrada" };
  return {
    title: article.title,
    description: article.excerpt ?? `Lee la noticia completa: ${article.title}`,
  };
}

export default async function ArticleDetailPage({
  params,
}: {
  params: Promise<{ articleSlug: string }>;
}) {
  const { articleSlug } = await params;
  const article = await getNewsBySlug(articleSlug);

  if (!article) notFound();

  const related = await getRelatedNews(article.slug, article.tags ?? [], 3);

  const paragraphs: string[] = (article.content ?? "")
    .split("\n\n")
    .filter((p: string) => p.trim().length > 0);

  return (
    <article className="py-8">
      <Link href="/noticias" className="inline-flex items-center gap-1 text-sm text-primary hover:underline mb-6">
        <ArrowLeft className="h-4 w-4" /> Volver a noticias
      </Link>

      <header className="mb-8">
        <div className="flex items-center gap-3 mb-3">
          <Badge variant="default">{article.tags?.[0] ?? "General"}</Badge>
          <span className="flex items-center gap-1 text-sm text-muted">
            <Clock className="h-3.5 w-3.5" /> {formatDate(article.published_at)}
          </span>
        </div>
        <h1 className="text-3xl font-bold lg:text-4xl">{article.title}</h1>
        {article.excerpt && (
          <p className="mt-3 text-lg text-foreground-secondary">{article.excerpt}</p>
        )}
      </header>

      <div className="aspect-video rounded-xl bg-primary/5 flex items-center justify-center mb-8">
        <span className="text-muted text-sm">Imagen destacada del artículo</span>
      </div>

      <div className="prose prose-lg max-w-none">
        {paragraphs.map((paragraph: string, i: number) => (
          <p key={i} className="text-foreground-secondary leading-relaxed mb-4">
            {paragraph}
          </p>
        ))}
      </div>

      {related.length > 0 && (
        <Card className="mt-8">
          <CardContent className="p-6">
            <h2 className="font-semibold mb-2">Artículos relacionados</h2>
            <ul className="space-y-2">
              {related.map((rel) => (
                <li key={rel.id}>
                  <Link href={`/noticias/${rel.slug}`} className="text-sm text-primary hover:underline">
                    {rel.title}
                  </Link>
                </li>
              ))}
            </ul>
          </CardContent>
        </Card>
      )}
    </article>
  );
}
