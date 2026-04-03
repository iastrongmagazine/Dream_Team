import { supabase } from "./client";

// ==========================================
// Home Page Queries
// ==========================================

/** Next scheduled match with home/away teams, competition, and stadium */
export async function getNextMatch() {
  const { data, error } = await supabase
    .from("matches")
    .select(
      `
      id, matchday, home_score, away_score, status, played_at,
      home_team:teams!matches_home_team_id_fkey ( id, name, short_name, slug ),
      away_team:teams!matches_away_team_id_fkey ( id, name, short_name, slug ),
      competition:competitions ( id, name, short_name, slug ),
      stadium:stadiums ( id, name, slug )
    `
    )
    .eq("status", "scheduled")
    .order("played_at", { ascending: true })
    .limit(1)
    .single();

  if (error) {
    console.error("getNextMatch error:", error.message);
    return null;
  }
  return data;
}

/** Last 3 finished matches involving our team */
export async function getRecentResults(limit = 3) {
  const { data, error } = await supabase
    .from("matches")
    .select(
      `
      id, matchday, home_score, away_score, status, played_at,
      home_team:teams!matches_home_team_id_fkey ( id, name, short_name, slug, is_own_team ),
      away_team:teams!matches_away_team_id_fkey ( id, name, short_name, slug, is_own_team ),
      competition:competitions ( id, name, short_name )
    `
    )
    .eq("status", "finished")
    .order("played_at", { ascending: false })
    .limit(limit);

  if (error) {
    console.error("getRecentResults error:", error.message);
    return [];
  }
  return data ?? [];
}

/** Top N standings for the current league */
export async function getStandings(limit = 5) {
  const { data, error } = await supabase
    .from("standings")
    .select(
      `
      id, position, played, won, drawn, lost,
      goals_for, goals_against, goal_difference, points, form,
      team:teams ( id, name, short_name, slug, is_own_team )
    `
    )
    .order("position", { ascending: true })
    .limit(limit);

  if (error) {
    console.error("getStandings error:", error.message);
    return [];
  }
  return data ?? [];
}

/** Active sponsors ordered by tier (gold first) */
export async function getSponsors() {
  const { data, error } = await supabase
    .from("sponsors")
    .select("id, name, slug, website, tier")
    .eq("active", true)
    .order("tier", { ascending: true });

  if (error) {
    console.error("getSponsors error:", error.message);
    return [];
  }
  return data ?? [];
}

/** Featured news for home page (latest 4 published articles) */
export async function getFeaturedNews(limit = 4) {
  const { data, error } = await supabase
    .from("news")
    .select("id, title, slug, excerpt, published_at, is_featured, tags")
    .eq("status", "published")
    .is("deleted_at", null)
    .order("published_at", { ascending: false })
    .limit(limit);

  if (error) {
    console.error("getFeaturedNews error:", error.message);
    return [];
  }
  return data ?? [];
}

// ==========================================
// Noticias Page Queries
// ==========================================

/** All published news articles */
export async function getAllNews() {
  const { data, error } = await supabase
    .from("news")
    .select("id, title, slug, excerpt, published_at, is_featured, tags")
    .eq("status", "published")
    .is("deleted_at", null)
    .order("published_at", { ascending: false });

  if (error) {
    console.error("getAllNews error:", error.message);
    return [];
  }
  return data ?? [];
}

/** Single news article by slug */
export async function getNewsBySlug(slug: string) {
  const { data, error } = await supabase
    .from("news")
    .select("id, title, slug, excerpt, content, published_at, is_featured, tags")
    .eq("slug", slug)
    .eq("status", "published")
    .is("deleted_at", null)
    .single();

  if (error) {
    console.error("getNewsBySlug error:", error.message);
    return null;
  }
  return data;
}

/** Related articles (same tags, excluding current) */
export async function getRelatedNews(currentSlug: string, tags: string[], limit = 3) {
  const { data, error } = await supabase
    .from("news")
    .select("id, title, slug")
    .eq("status", "published")
    .is("deleted_at", null)
    .neq("slug", currentSlug)
    .overlaps("tags", tags)
    .order("published_at", { ascending: false })
    .limit(limit);

  if (error) {
    console.error("getRelatedNews error:", error.message);
    return [];
  }
  return data ?? [];
}
