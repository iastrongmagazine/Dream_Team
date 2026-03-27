// ==========================================
// Platzi FC — Domain Types
// ==========================================

// --- Core Entities ---

export interface Season {
  id: string;
  name: string;
  slug: string;
  startDate: string;
  endDate: string | null;
  isCurrent: boolean;
}

export interface Competition {
  id: string;
  name: string;
  slug: string;
  shortName: string | null;
  competitionType: "league" | "cup" | "friendly" | "supercup";
  country: string | null;
  logoUrl: string | null;
  seasonId: string;
}

export interface Team {
  id: string;
  name: string;
  slug: string;
  shortName: string | null;
  logoUrl: string | null;
  city: string | null;
  country: string | null;
  foundedYear: number | null;
  website: string | null;
  isOwnTeam: boolean;
}

export interface Match {
  id: string;
  competitionId: string;
  seasonId: string;
  matchday: number | null;
  homeTeamId: string;
  awayTeamId: string;
  homeScore: number | null;
  awayScore: number | null;
  status: "scheduled" | "live" | "finished" | "postponed" | "cancelled";
  playedAt: string | null;
  stadiumId: string | null;
  referee: string | null;
  attendance: number | null;
  summary: string | null;
  // Resolved relations (optional)
  homeTeam?: Team;
  awayTeam?: Team;
  competition?: Competition;
  stadium?: Stadium;
}

export interface Player {
  id: string;
  firstName: string;
  lastName: string;
  slug: string;
  displayName: string | null;
  photoUrl: string | null;
  teamId: string | null;
  position: "goalkeeper" | "defender" | "midfielder" | "forward" | null;
  jerseyNumber: number | null;
  nationality: string | null;
  dateOfBirth: string | null;
  heightCm: number | null;
  weightKg: number | null;
  preferredFoot: "left" | "right" | "both" | null;
  bio: string | null;
  isActive: boolean;
}

export interface PlayerStats {
  id: string;
  playerId: string;
  matchId: string | null;
  seasonId: string | null;
  competitionId: string | null;
  minutesPlayed: number;
  goals: number;
  assists: number;
  yellowCards: number;
  redCards: number;
  shots: number;
  shotsOnTarget: number;
  passes: number;
  passAccuracy: number | null;
  tackles: number;
  saves: number;
  isStarter: boolean;
  rating: number | null;
}

export interface Standing {
  id: string;
  competitionId: string;
  seasonId: string;
  teamId: string;
  position: number | null;
  played: number;
  won: number;
  drawn: number;
  lost: number;
  goalsFor: number;
  goalsAgainst: number;
  goalDifference: number;
  points: number;
  form: string | null;
  // Resolved
  team?: Team;
}

export interface Staff {
  id: string;
  firstName: string;
  lastName: string;
  slug: string;
  displayName: string | null;
  photoUrl: string | null;
  teamId: string | null;
  role: string;
  nationality: string | null;
  dateOfBirth: string | null;
  bio: string | null;
  isActive: boolean;
}

export interface Stadium {
  id: string;
  name: string;
  slug: string | null;
  address: string | null;
  city: string | null;
  capacity: number | null;
  mapEmbed: string | null;
  contactPhone: string | null;
  contactEmail: string | null;
}

// --- CMS / Editorial Entities ---

export interface Article {
  id: string;
  title: string;
  slug: string;
  excerpt: string | null;
  content: string | null;
  authorId: string | null;
  status: "draft" | "published";
  publishedAt: string | null;
  tags: string[];
  isFeatured: boolean;
}

export interface Sponsor {
  id: string;
  name: string;
  slug: string | null;
  website: string | null;
  logoUrl: string | null;
  tier: string | null;
  description: string | null;
  startDate: string | null;
  endDate: string | null;
  active: boolean;
}

export interface Product {
  id: string;
  sku: string | null;
  name: string;
  slug: string | null;
  description: string | null;
  price: number;
  currency: string;
  inventoryCount: number;
  isActive: boolean;
  categories: string[];
}

// --- Navigation ---

export interface NavigationItem {
  id: string;
  title: string;
  slug: string | null;
  url: string | null;
  parentId: string | null;
  orderIndex: number;
  location: "main" | "footer" | "secondary";
  visible: boolean;
  openInNewTab: boolean;
  children?: NavigationItem[];
}
