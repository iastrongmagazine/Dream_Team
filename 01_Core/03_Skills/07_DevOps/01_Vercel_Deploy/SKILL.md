# 26 Vercel Deploy

## Esencia Original
> **Propósito:** Deploy aplicaciones en Vercel usando SOTA features — Edge Functions, Serverless, ISR, Preview Deployments
> **Flujo:** Configurar proyecto → Build → Preview → Deploy production

## Triggers on: devops, deployment, infrastructure.
Cuando el usuario menciona: "vercel", "deploy", "edge", "serverless", "preview", "hosting"

## Overview
Skill para deployments en Vercel usando SOTA features 2025-2026

## SOTA Stack (2025-2026)

### Vercel Products
| Feature | Use Case | SOTA? |
|---------|----------|-------|
| **Edge Functions** | Low latency, global | ✅ V8 isolates |
| **Serverless Functions** | Complex logic | ✅ Node 20+ |
| **ISR** | Static + Dynamic | ✅ On-demand |
| **Fluid Compute** | Active CPU pricing | ✅ 2025 new |
| **Preview Deployments** | Per-branch URLs | ✅ Built-in |
| **Monorepo** | Multiple apps | ✅ Turborepo |

### Runtimes
- **Edge**: V8 isolates, TypeScript, 128MB, <1ms cold start
- **Node.js**: Serverless, full Node API
- **Go/Python**: Serverless only
- **Bun**: Preview (experimental)

### Deployment Types

#### 1. Next.js (Recommended)
```json
// vercel.json
{
  "framework": "nextjs",
  "buildCommand": "npm run build",
  "outputDirectory": ".next"
}
```

#### 2. Static Site
```json
{
  "buildCommand": "npm run build",
  "outputDirectory": "dist"
}
```

#### 3. Monorepo
```json
{
  "rootDirectory": ".",
  "projects": [
    { "path": "apps/web" },
    { "path": "apps/api" }
  ]
}
```

## Workflow

### Step 1: Setup Vercel CLI
```bash
npm i -g vercel
vercel login
```

### Step 2: Configure
```bash
# Link project
vercel link

# Environment variables
vercel env add NEXT_PUBLIC_SUPABASE_URL
vercel env add NEXT_PUBLIC_ANTHROPIC_API_KEY
```

### Step 3: Deploy
```bash
# Development
vercel dev

# Preview (per branch)
vercel

# Production
vercel --prod
```

### Step 4: Edge Functions
```typescript
// SOTA: Edge runtime con streaming
export const runtime = 'edge';

export default async function handler(req: Request) {
  return new Response('Hello from Edge!', {
    headers: { 'Content-Type': 'text/plain' }
  });
}
```

### Step 5: ISR Pattern
```typescript
// Incremental Static Regeneration
export async function getStaticProps() {
  return {
    props: { data },
    revalidate: 60 // seconds
  };
}
```

### Step 6: Environment Strategy
```bash
# Development (.env.local)
# Preview (Vercel auto)
# Production (vercel env pull)
```

## Monorepo Setup

### Turborepo Integration
```json
// turbo.json
{
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "!.next/cache/**"]
    }
  }
}
```

### Root vercel.json
```json
{
  "rootDirectory": ".",
  "buildCommand": "npm run build",
  "installCommand": "npm install"
}
```

## CI/CD Integration

### GitHub Actions
```yaml
name: Vercel Production
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm install && npm run build
      - uses: amondnet/vercel-action@v25
        with:
          vercel-token: ${{ secrets.VERCEL_TOKEN }}
          vercel-org-id: ${{ secrets.ORG_ID }}
          vercel-project-id: ${{ secrets.PROJECT_ID }}
```

## Performance SOTA

### Edge Caching
```typescript
// Cache-Control headers
export function headers() {
  return [
    {
      source: '/api/:path*',
      headers: [
        { key: 'Cache-Control', value: 's-maxage=60, stale-while-revalidate' }
      ]
    }
  ];
}
```

### Bundle Optimization
```typescript
// next.config.js
module.exports = {
  compiler: { removeConsole: process.env.NODE_ENV === 'production' },
  experimental: { optimizeCss: true }
};
```

## Resources
- [Vercel Docs](https://vercel.com/docs)
- [Edge Functions](https://vercel.com/docs/functions/edge-functions)
- [ISR](https://vercel.com/docs/app/building-your-application/data-fetching/incremental-static-regeneration)
- [Monorepo](https://vercel.com/docs/monorepos)


## ⚠️ Gotchas

- **[ERROR]**: Error común
  - **Solución**: Cómo evitar

## 💾 State Persistence
Guardar en:
- `02_Operations/` — Estado activo
