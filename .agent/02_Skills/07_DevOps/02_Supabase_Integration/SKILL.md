# 23_Supabase Integration

## Esencia Original
> **Propósito:** Implementar backends con Supabase — Auth RLS, PostgreSQL + pg_vector, Realtime, Edge Functions, Storage S3-compatible
> **Flujo:** Configurar proyecto → DB schema → Auth setup → Edge Functions → Deploy

## Triggers on: devops, deployment, infrastructure.
Cuando el usuario menciona: "supabase", "postgres", "database setup", "auth", "realtime", "edge functions supabase", "pg vector", "vector search", "rlS", "storage supabase"

## Overview
Skill para implementar backends completos con Supabase: autenticación RLS, PostgreSQL con pg_vector para búsqueda semántica, realtime subscriptions, Edge Functions en Deno, y Storage S3-compatible. SOTA 2025-2026 para proyectos AI-ready.

## SOTA Stack (2025-2026)

### Core Features
- **Authentication**: RLS Policies, MFA, SSO (Google, GitHub, SAML), TOTP, Passkeys
- **Database**: PostgreSQL 16+, pg_vector 0.7+, Row Level Security
- **Realtime**: Presence, Broadcast, Postgres Changes (CDC)
- **Edge Functions**: Deno 2.x, TypeScript strict mode, edge runtime global
- **Storage**: S3-compatible, image transformations, CDN with auto-format
- **Vector Search**: pg_vector con HNSW index, embeddings via OpenAI/Cohere

## Workflow

### Step 1: Setup & Connection

```bash
# CLI installation
npm install -g supabase

# Initialize project
supabase init

# Login to Supabase
supabase login

# Link to project
supabase link --project-ref <project-ref>

# Start local development
supabase start
supabase status

# Generate types from schema
supabase gen types typescript --project-id <project-id> > types/supabase.ts
```

**Environment setup (.env.local):**
```bash
NEXT_PUBLIC_SUPABASE_URL=https://your-project.supabase.co
NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_SERVICE_ROLE_KEY=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
SUPABASE_JWT_SECRET=your-jwt-secret-min-32-chars
```

### Step 2: Auth Implementation

**SOTA Pattern: Edge-ready auth with RLS + Middleware**

```typescript
// lib/auth.ts - Edge-compatible auth client
import { createClient } from '@supabase/supabase-js'
import type { Database } from '@/types/supabase'

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL!
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!

export const createServerClient = (cookies: {
  getAll: () => { name: string; value: string }[]
  setAll: (cookies: { name: string; value: string; options?: object }[]) => void
}) => {
  return createClient<Database>(supabaseUrl, supabaseAnonKey, {
    auth: {
      flowType: 'pkce',
      persistSession: false,
      autoRefreshToken: false,
    },
    global: {
      headers: {
        cookie: cookies.getAll()
          .map(c => `${c.name}=${c.value}`)
          .join('; '),
      },
    },
    cookies: {
      getAll: cookies.getAll,
      setAll: cookies.setAll,
    },
  })
}

// lib/middleware.ts - Next.js middleware for auth
import { createServerClient } from '@/lib/auth'
import { NextResponse, type NextRequest } from 'next/server'

export async function middleware(request: NextRequest) {
  let supabase = createServerClient({
    getAll: () => request.cookies.getAll(),
    setAll: () => {},
  })

  const { data: { user } } = await supabase.auth.getUser()
  const { pathname } = request.nextUrl

  // Protected routes
  const protectedPaths = ['/dashboard', '/settings', '/profile']
  if (protectedPaths.some(p => pathname.startsWith(p)) && !user) {
    return NextResponse.redirect(new URL('/login', request.url))
  }

  return NextResponse.next()
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)'],
}
```

**Auth with MFA (TOTP):**
```typescript
// Enable MFA for user
const { data, error } = await supabase.auth.mfa.enroll({
  factorType: 'totp',
})

// Verify MFA challenge
const { challengeAndVerify } = await supabase.auth.mfa.challengeAndVerify({
  factorId: factorId,
  code: '123456',
})
```

**Social Auth (SSO):**
```typescript
// OAuth providers
const { data, error } = await supabase.auth.signInWithOAuth({
  provider: 'google', // or 'github', 'azure', 'okta'
  options: {
    redirectTo: `${process.env.NEXT_PUBLIC_SITE_URL}/auth/callback`,
    scopes: 'email profile openid',
  },
})

// SAML SSO for enterprise
const { data, error } = await supabase.auth.signInWithSSO({
  provider: 'saml',
  options: {
    redirectTo: `${process.env.NEXT_PUBLIC_SITE_URL}/auth/callback`,
  },
})
```

### Step 3: Database Schema

**SOTA: PostgreSQL with pg_vector + RLS**

```sql
-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "vector";
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Enable RLS on all tables
ALTER TABLE profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
ALTER TABLE embeddings ENABLE ROW LEVEL SECURITY;
ALTER TABLE conversations ENABLE ROW LEVEL SECURITY;

-- Profiles table
CREATE TABLE profiles (
  id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
  email TEXT UNIQUE NOT NULL,
  full_name TEXT,
  avatar_url TEXT,
  mfa_enabled BOOLEAN DEFAULT false,
  metadata JSONB DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- Documents with metadata for filtering
CREATE TABLE documents (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  metadata JSONB DEFAULT '{}',
  embedding VECTOR(1536),
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- Conversations for AI context
CREATE TABLE conversations (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  user_id UUID REFERENCES profiles(id) ON DELETE CASCADE,
  title TEXT,
  model TEXT DEFAULT 'gpt-4',
  tokens_used INT DEFAULT 0,
  metadata JSONB DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT now(),
  updated_at TIMESTAMPTZ DEFAULT now()
);

-- Messages with vector embeddings
CREATE TABLE messages (
  id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
  conversation_id UUID REFERENCES conversations(id) ON DELETE CASCADE,
  role TEXT NOT NULL CHECK (role IN ('user', 'assistant', 'system')),
  content TEXT NOT NULL,
  embedding VECTOR(1536),
  metadata JSONB DEFAULT '{}',
  created_at TIMESTAMPTZ DEFAULT now()
);

-- Indexes for performance
CREATE INDEX idx_documents_user_id ON documents(user_id);
CREATE INDEX idx_documents_embedding ON documents USING HNSW (embedding vector_cosine_ops);
CREATE INDEX idx_messages_conversation_id ON messages(conversation_id);
CREATE INDEX idx_messages_embedding ON messages USING HNSW (embedding vector_cosine_ops);

-- RLS Policies

-- Profiles: Users can only see/edit their own profile
CREATE POLICY "Users can view own profile"
  ON profiles FOR SELECT
  USING (auth.uid() = id);

CREATE POLICY "Users can update own profile"
  ON profiles FOR UPDATE
  USING (auth.uid() = id);

-- Documents: Users only access their own documents
CREATE POLICY "Users manage own documents"
  ON documents FOR ALL
  USING (auth.uid() = user_id);

-- Conversations: Users only access their own conversations
CREATE POLICY "Users manage own conversations"
  ON conversations FOR ALL
  USING (auth.uid() = user_id);

-- Messages: Users only access messages in their conversations
CREATE POLICY "Users manage own messages"
  ON messages FOR ALL
  USING (
    EXISTS (
      SELECT 1 FROM conversations c
      WHERE c.id = conversation_id AND c.user_id = auth.uid()
    )
  );

-- Helper function to update timestamps
CREATE OR REPLACE FUNCTION update_updated_at()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Apply triggers
CREATE TRIGGER profiles_updated_at
  BEFORE UPDATE ON profiles
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER documents_updated_at
  BEFORE UPDATE ON documents
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();

CREATE TRIGGER conversations_updated_at
  BEFORE UPDATE ON conversations
  FOR EACH ROW EXECUTE FUNCTION update_updated_at();
```

**Vector Search with pg_vector (HNSW):**
```typescript
// lib/vector.ts - Embedding generation and similarity search
import { createClient } from '@supabase/supabase-js'
import OpenAI from 'openai'

const openai = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
})

export async function generateEmbedding(text: string): Promise<number[]> {
  const response = await openai.embeddings.create({
    model: 'text-embedding-3-small', // 1536 dimensions
    input: text,
  })
  return response.data[0].embedding
}

export async function semanticSearch(
  supabase: ReturnType<typeof createClient>,
  query: string,
  match_threshold: number = 0.7,
  match_count: number = 5
) {
  const queryEmbedding = await generateEmbedding(query)

  const { data: results, error } = await supabase.rpc('match_documents', {
    query_embedding: queryEmbedding,
    match_threshold,
    match_count,
  })

  return results
}

// RPC function for vector search (create in Supabase dashboard)
export const matchDocumentsSQL = `
CREATE OR REPLACE FUNCTION match_documents(
  query_embedding VECTOR(1536),
  match_threshold FLOAT DEFAULT 0.7,
  match_count INT DEFAULT 5
)
RETURNS TABLE (
  id UUID,
  content TEXT,
  metadata JSONB,
  similarity FLOAT
)
LANGUAGE plpgsql
AS $$
BEGIN
  RETURN QUERY
  SELECT
    d.id,
    d.content,
    d.metadata,
    1 - (d.embedding <=> query_embedding) AS similarity
  FROM documents d
  WHERE 1 - (d.embedding <=> query_embedding) > match_threshold
  ORDER BY d.embedding <=> query_embedding
  LIMIT match_count;
END;
$$;
```

### Step 4: Realtime Subscriptions

**SOTA: Presence + Broadcast + Postgres Changes**

```typescript
// lib/realtime.ts - Comprehensive realtime patterns

// Postgres Changes (CDC) - Listen to database changes
export function subscribeToMessages(
  supabase: ReturnType<typeof createClient>,
  conversationId: string,
  onMessage: (payload: RealtimePostgresChangesPayload<Message>) => void
) {
  const channel = supabase
    .channel(`messages:${conversationId}`)
    .on(
      'postgres_changes',
      {
        event: '*',
        schema: 'public',
        table: 'messages',
        filter: `conversation_id=eq.${conversationId}`,
      },
      (payload) => onMessage(payload as RealtimePostgresChangesPayload<Message>)
    )
    .subscribe()

  return () => supabase.removeChannel(channel)
}

// Presence for collaborative features
export function setupPresence(
  supabase: ReturnType<typeof createClient>,
  roomId: string,
  user: { id: string; name: string; avatar?: string }
) {
  const channel = supabase.channel(`room:${roomId}`, {
    config: {
      presence: {
        key: user.id,
      },
    },
  })

  channel
    .on('presence', { event: 'sync' }, () => {
      const state = channel.presenceState()
      console.log('Online users:', Object.keys(state).length)
    })
    .on('presence', { event: 'join' }, ({ key, newPresences }) => {
      console.log('User joined:', key, newPresences)
    })
    .on('presence', { event: 'leave' }, ({ key, leftPresences }) => {
      console.log('User left:', key, leftPresences)
    })
    .subscribe(async (status) => {
      if (status === 'SUBSCRIBED') {
        await channel.track({
          id: user.id,
          name: user.name,
          avatar: user.avatar,
          online_at: new Date().toISOString(),
        })
      }
    })

  return channel
}

// Broadcast for low-latency messaging
export function setupBroadcast(
  supabase: ReturnType<typeof createClient>,
  roomId: string
) {
  const channel = supabase.channel(`broadcast:${roomId}`)

  channel
    .on('broadcast', { event: 'cursor' }, ({ payload }) => {
      console.log('Cursor update:', payload)
    })
    .on('broadcast', { event: 'typing' }, ({ payload }) => {
      console.log('User typing:', payload)
    })
    .subscribe()

  const broadcastCursor = (position: { x: number; y: number }) => {
    channel.send({
      type: 'broadcast',
      event: 'cursor',
      payload: position,
    })
  }

  return { channel, broadcastCursor }
}

// Full realtime provider for React/Next.js
export class RealtimeProvider {
  private channels: Map<string, RealtimeChannel> = new Map()
  private supabase: ReturnType<typeof createClient>

  constructor(supabase: ReturnType<typeof createClient>) {
    this.supabase = supabase
  }

  subscribeToConversation(conversationId: string, callbacks: {
    onInsert?: (msg: Message) => void
    onUpdate?: (msg: Message) => void
    onDelete?: (msg: Message) => void
  }) {
    const channel = this.supabase
      .channel(`conversation:${conversationId}`)
      .on('postgres_changes', {
        event: 'INSERT',
        schema: 'public',
        table: 'messages',
        filter: `conversation_id=eq.${conversationId}`,
      }, (payload) => callbacks.onInsert?.(payload.new as Message))
      .on('postgres_changes', {
        event: 'UPDATE',
        schema: 'public',
        table: 'messages',
        filter: `conversation_id=eq.${conversationId}`,
      }, (payload) => callbacks.onUpdate?.(payload.new as Message))
      .on('postgres_changes', {
        event: 'DELETE',
        schema: 'public',
        table: 'messages',
        filter: `conversation_id=eq.${conversationId}`,
      }, (payload) => callbacks.onDelete?.(payload.old as Message))
      .subscribe()

    this.channels.set(`conversation:${conversationId}`, channel)
    return () => this.unsubscribe(`conversation:${conversationId}`)
  }

  unsubscribe(channelName: string) {
    const channel = this.channels.get(channelName)
    if (channel) {
      this.supabase.removeChannel(channel)
      this.channels.delete(channelName)
    }
  }

  cleanup() {
    this.channels.forEach((channel) => this.supabase.removeChannel(channel))
    this.channels.clear()
  }
}
```

### Step 5: Edge Functions

**SOTA: Deno 2.x runtime, TypeScript strict, edge deployment**

```typescript
// supabase/functions/generate-summary/index.ts
// Deno Edge Function for AI-powered document summarization
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'
import OpenAI from 'https://esm.sh/openai@4'

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  try {
    const supabaseClient = createClient(
      Deno.env.get('SUPABASE_URL') ?? '',
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? '',
      { auth: { persistSession: '' } }
    )

    const openai = new OpenAI({
      apiKey: Deno.env.get('OPENAI_API_KEY') ?? '',
    })

    const { documentId, userId } = await req.json()

    // Fetch document (RLS bypass with service role)
    const { data: document, error: docError } = await supabaseClient
      .from('documents')
      .select('*')
      .eq('id', documentId)
      .eq('user_id', userId)
      .single()

    if (docError || !document) {
      return new Response(JSON.stringify({ error: 'Document not found' }), {
        status: 404,
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
      })
    }

    // Generate summary with OpenAI
    const completion = await openai.chat.completions.create({
      model: 'gpt-4o-mini',
      messages: [
        {
          role: 'system',
          content: 'You are a helpful assistant that summarizes documents concisely.',
        },
        {
          role: 'user',
          content: `Summarize this document in 3-5 bullet points:\n\n${document.content}`,
        },
      ],
      max_tokens: 500,
    })

    const summary = completion.choices[0]?.message?.content ?? ''

    // Store summary in database
    await supabaseClient
      .from('documents')
      .update({ 
        metadata: { ...document.metadata, summary, summarized_at: new Date().toISOString() }
      })
      .eq('id', documentId)

    return new Response(JSON.stringify({ summary }), {
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    })
  } catch (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { ...corsHeaders, 'Content-Type': 'application/json' },
    })
  }
})
```

**Embedding generation edge function:**
```typescript
// supabase/functions/generate-embeddings/index.ts
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'
import OpenAI from 'https://esm.sh/openai@4'

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  const supabaseClient = createClient(
    Deno.env.get('SUPABASE_URL') ?? '',
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
  )

  const openai = new OpenAI({
    apiKey: Deno.env.get('OPENAI_API_KEY') ?? '',
  })

  const { documents } = await req.json()

  const results = await Promise.all(
    documents.map(async (doc: { id: string; content: string }) => {
      const embedding = await openai.embeddings.create({
        model: 'text-embedding-3-small',
        input: doc.content,
      })

      await supabaseClient
        .from('documents')
        .update({ embedding: embedding.data[0].embedding })
        .eq('id', doc.id)

      return { id: doc.id, status: 'embedded' }
    })
  )

  return new Response(JSON.stringify({ results }), {
    headers: { ...corsHeaders, 'Content-Type': 'application/json' },
  })
})
```

**Batch RAG function:**
```typescript
// supabase/functions/rag-search/index.ts
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'
import OpenAI from 'https://esm.sh/openai@4'

Deno.serve(async (req) => {
  const { query, user_id, top_k = 5 } = await req.json()

  const supabaseClient = createClient(
    Deno.env.get('SUPABASE_URL') ?? '',
    Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? ''
  )

  const openai = new OpenAI({
    apiKey: Deno.env.get('OPENAI_API_KEY') ?? '',
  })

  // Generate query embedding
  const queryEmbedding = await openai.embeddings.create({
    model: 'text-embedding-3-small',
    input: query,
  })

  // Semantic search
  const { data: documents, error } = await supabaseClient.rpc('match_documents', {
    query_embedding: queryEmbedding.data[0].embedding,
    match_threshold: 0.7,
    match_count: top_k,
  })

  if (error) {
    return new Response(JSON.stringify({ error: error.message }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' },
    })
  }

  // Build context for LLM
  const context = documents
    .map((doc: any, i: number) => `[${i + 1}] ${doc.content}`)
    .join('\n\n')

  // Generate answer
  const completion = await openai.chat.completions.create({
    model: 'gpt-4o',
    messages: [
      {
        role: 'system',
        content: 'You are a helpful AI assistant. Use the provided context to answer the user question. If the context is insufficient, say so.',
      },
      {
        role: 'user',
        content: `Context:\n${context}\n\nQuestion: ${query}`,
      },
    ],
  })

  return new Response(JSON.stringify({
    answer: completion.choices[0]?.message?.content,
    sources: documents,
  }), {
    headers: { 'Content-Type': 'application/json' },
  })
})
```

### Step 6: Storage

**SOTA: S3-compatible with transformations and signed URLs**

```typescript
// lib/storage.ts - Complete storage patterns

export class StorageManager {
  private supabase: ReturnType<typeof createClient>
  private bucket = 'user-files'

  constructor(supabase: ReturnType<typeof createClient>) {
    this.supabase = supabase
  }

  async uploadFile(
    file: File | Blob,
    path: string,
    options?: {
      contentType?: string
      upsert?: boolean
      cacheControl?: number
    }
  ) {
    const { data, error } = await this.supabase.storage
      .from(this.bucket)
      .upload(path, file, {
        contentType: options?.contentType ?? file.type,
        upsert: options?.upsert ?? false,
        cacheControl: options?.cacheControl ?? 3600,
      })

    if (error) throw error
    return data
  }

  async uploadWithTransform(
    file: File | Blob,
    path: string,
    transformations: {
      width?: number
      height?: number
      quality?: number
      format?: 'webp' | 'avif' | 'original'
      resize?: 'cover' | 'contain' | 'fill' | 'inside' | 'outside'
    }
  ) {
    // Upload original
    const uploadData = await this.uploadFile(file, path)

    // Generate transformed URL
    const { data: urlData } = this.supabase.storage
      .from(this.bucket)
      .getPublicUrl(uploadData.path)

    const transformParams = new URLSearchParams()
    if (transformations.width) transformParams.set('width', String(transformations.width))
    if (transformations.height) transformParams.set('height', String(transformations.height))
    if (transformations.quality) transformParams.set('quality', String(transformations.quality))
    if (transformations.format) transformParams.set('format', transformations.format)
    if (transformations.resize) transformParams.set('resize', transformations.resize)

    return {
      original: urlData.publicUrl,
      transformed: `${urlData.publicUrl}?${transformParams.toString()}`,
      path: uploadData.path,
    }
  }

  async getSignedUrl(path: string, expiresIn = 3600) {
    const { data, error } = await this.supabase.storage
      .from(this.bucket)
      .createSignedUrl(path, expiresIn)

    if (error) throw error
    return data.signedUrl
  }

  async getSignedUploadUrl(path: string) {
    const { data, error } = await this.supabase.storage
      .from(this.bucket)
      .createSignedUploadUrl(path)

    if (error) throw error
    return data
  }

  async deleteFile(path: string) {
    const { error } = await this.supabase.storage
      .from(this.bucket)
      .remove([path])

    if (error) throw error
  }

  async listFiles(prefix: string) {
    const { data, error } = await this.supabase.storage
      .from(this.bucket)
      .list(prefix, {
        limit: 100,
        sortBy: { column: 'name', order: 'asc' },
      })

    if (error) throw error
    return data
  }

  async downloadFile(path: string) {
    const { data, error } = await this.supabase.storage
      .from(this.bucket)
      .download(path)

    if (error) throw error
    return data
  }
}

// Direct upload with progress tracking
export async function uploadWithProgress(
  supabase: ReturnType<typeof createClient>,
  bucket: string,
  path: string,
  file: File,
  onProgress?: (progress: number) => void
) {
  const chunkSize = 6 * 1024 * 1024 // 6MB chunks
  const totalChunks = Math.ceil(file.size / chunkSize)

  for (let i = 0; i < totalChunks; i++) {
    const start = i * chunkSize
    const end = Math.min(start + chunkSize, file.size)
    const chunk = file.slice(start, end)

    const { error } = await supabase.storage.from(bucket).uploadBinaryContinuable(
      path,
      new Uint8Array(await chunk.arrayBuffer()),
      {
        offset: start,
        upsert: i === 0,
      }
    )

    if (error) throw error
    onProgress?.(Math.round(((i + 1) / totalChunks) * 100))
  }

  return { path }
}
```

## AI Integration

**Complete RAG Pipeline for Think Different AI:**

```typescript
// lib/rag.ts - RAG implementation with Supabase
import { createClient } from '@supabase/supabase-js'
import OpenAI from 'openai'

export class ThinkDifferentRAG {
  private supabase: ReturnType<typeof createClient>
  private openai: OpenAI
  private embeddingModel = 'text-embedding-3-small'
  private chatModel = 'gpt-4o'

  constructor(supabase: ReturnType<typeof createClient>) {
    this.supabase = supabase
    this.openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY })
  }

  async indexDocument(
    userId: string,
    title: string,
    content: string,
    metadata: Record<string, any> = {}
  ) {
    const embedding = await this.openai.embeddings.create({
      model: this.embeddingModel,
      input: content,
    })

    const { data, error } = await this.supabase
      .from('documents')
      .insert({
        user_id: userId,
        title,
        content,
        metadata,
        embedding: embedding.data[0].embedding,
      })
      .select()
      .single()

    if (error) throw error
    return data
  }

  async search(query: string, userId: string, topK = 5) {
    const queryEmbedding = await this.openai.embeddings.create({
      model: this.embeddingModel,
      input: query,
    })

    const { data, error } = await this.supabase.rpc('match_documents', {
      query_embedding: queryEmbedding.data[0].embedding,
      match_threshold: 0.7,
      match_count: topK,
    })

    if (error) throw error

    const filteredResults = (data as any[]).filter(doc => doc.user_id === userId)
    return filteredResults
  }

  async chat(query: string, userId: string, conversationId?: string) {
    const contextDocs = await this.search(query, userId)

    const context = contextDocs
      .map((doc, i) => `[Source ${i + 1}]: ${doc.content}`)
      .join('\n\n')

    const messages: OpenAI.Chat.ChatCompletionMessageParam[] = [
      {
        role: 'system',
        content: `You are an AI assistant integrated with Think Different AI system. 
Use the provided context to answer questions accurately. If the context doesn't contain 
relevant information, say so rather than hallucinating.

Context:
${context}`,
      },
      { role: 'user', content: query },
    ]

    const completion = await this.openai.chat.completions.create({
      model: this.chatModel,
      messages,
      temperature: 0.7,
      max_tokens: 2000,
    })

    const answer = completion.choices[0]?.message?.content ?? ''

    if (conversationId) {
      await this.supabase.from('messages').insert([
        { conversation_id: conversationId, role: 'user', content: query, embedding: [] },
        { conversation_id: conversationId, role: 'assistant', content: answer, embedding: [] },
      ])
    }

    return {
      answer,
      sources: contextDocs,
      tokens: completion.usage?.total_tokens ?? 0,
    }
  }
}
```

## MCP Server

**Configuración para `.mcp.json`:**

```json
{
  "mcpServers": {
    "supabase": {
      "transport": "streamableHttp",
      "url": "https://mcp.supabase.com/mcp",
      "headers": {
        "Authorization": "Bearer sbp_YOUR_SERVICE_ROLE_KEY"
      }
    }
  }
}
```

**Comandos útiles MCP Supabase:**
```bash
# Listar tablas
supabase mcp list-tables

# Consultar datos
supabase mcp query "SELECT * FROM profiles LIMIT 10"

# Ver RLs policies
supabase mcp list-policies

# Estadísticas de base de datos
supabase mcp stats
```

## Resources

- [Supabase Docs](https://supabase.com/docs)
- [pg_vector](https://github.com/pgvector/pgvector)
- [Supabase Edge Functions](https://supabase.com/docs/guides/functions)
- [Supabase Realtime](https://supabase.com/docs/guides/realtime)
- [Row Level Security](https://supabase.com/docs/guides/auth/row-level-security)
- [OpenAI Embeddings](https://platform.openai.com/docs/guides/embeddings)
- [Deno Deploy](https://deno.com/deploy)
- [Supabase Storage](https://supabase.com/docs/guides/storage)


## ⚠️ Gotchas

- **[ERROR]**: Error común
  - **Solución**: Cómo evitar

## 💾 State Persistence
Guardar en:
- `02_Operations/` — Estado activo
