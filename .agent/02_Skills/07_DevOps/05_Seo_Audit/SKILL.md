# 24 SEO Audit

## Esencia Original
> **Propósito:** Auditar sitios web para problemas SEO — technical SEO, on-page, performance
> **Flujo:** Configurar audit → Ejecutar crawls → Analizar resultados → Generar reporte


## Trigger Triggers on: devops, deployment, infrastructure.
Cuando el usuario menciona: "seo", "audit", "core web vitals", "lighthouse", "schema markup", "indexing", "search console", "sitemap", "robots", "webmaster"

## Overview
Skill para auditorías SEO técnicas comprehensivas usando SOTA tools 2025-2026. Integración con Lighthouse CI, Chrome DevTools MCP, y Playwright MCP para automation completa.

---

## SOTA Stack (2025-2026)

### Audit Tools
| Tool | Purpose | Best For |
|------|---------|----------|
| **Lighthouse CI** | Core Web Vitals, Performance, PWA | CI/CD pipelines |
| **Screaming Frog v21+** | Crawling, SEO audit, AI analysis | Large sites |
| **Google Search Console API** | Métricas reales de búsqueda | Rankings reales |
| **axe DevTools** | Accesibilidad WCAG 2.2 | Compliance |
| **Schema Markup Validator** | JSON-LD validation | Structured data |
| **PageSpeed Insights API** | Field data + Lab data | Real user metrics |

### CLI Installation
```bash
# Lighthouse CI
npm install -g @lhci/cli

# Screaming Frog (requires license, CLI mode)
screaming-frog seo spider --crawl https://example.com

# Google APIs
npm install googleapis

# axe-core for Playwright
npm install @axe-core/playwright
```

---

## Core Web Vitals (2025-2026)

| Metric | Full Name | Target | What It Measures |
|--------|-----------|--------|------------------|
| **LCP** | Largest Contentful Paint | < 2.5s | Loading performance |
| **INP** | Interaction to Next Paint | < 200ms | Responsiveness (replaced FID 2024) |
| **CLS** | Cumulative Layout Shift | < 0.1 | Visual stability |

### INP vs FID
- **FID** (First Input Delay): Solo medía el primer input
- **INP**: Mide todas las interacciones durante la page lifetime
- INP es más estricto: cualquier interacción lenta cuenta

---

## SEO Checklist

### On-Page SEO
- [ ] **Title tags**: < 60 chars, keyword al inicio, únicos por página
- [ ] **Meta descriptions**: < 160 chars, CTA incluido, únicas
- [ ] **Header hierarchy**: Un solo H1, H2-H6 jerárquicos
- [ ] **Schema markup JSON-LD**: Article, Product, FAQ según tipo de página
- [ ] **Alt text**: Descriptivo, incluye keywords, sin "image of"
- [ ] **Canonical URLs**: Auto-set, sin duplicates
- [ ] **Internal links**: Contextuales, con anchor text optimizado
- [ ] **External links**: Nofollow para links paid/external no confiable

### Technical SEO
- [ ] **Sitemap.xml**: Generado automáticamente, < 50K URLs, gzipped
- [ ] **Robots.txt**: Allow/disallow correcto, sitemap declarado
- [ ] **SSL/HTTPS**: Certificate válido, mixed content fix
- [ ] **Mobile-first**: Diseño responsive, viewport correcto
- [ ] **Page speed**: FCP < 1.8s, LCP < 2.5s, TBT < 200ms
- [ ] **No render-blocking**: CSS/JS crítico inline, resto deferred
- [ ] **hreflang tags**: Correctos para multilingual sites
- [ ] **404 handling**: Custom 404 page, redirects 301 para moved pages

### Performance & Assets
- [ ] **Images**: WebP/AVIF, srcset para responsive, < 100KB hero images
- [ ] **Lazy loading**: Native `loading="lazy"` para below-fold images
- [ ] **CDN**: Cloudflare/Fastly para assets estáticos
- [ ] **Caching**: Cache-Control headers, immutable para hashed assets
- [ ] **Minification**: HTML, CSS, JS minified en producción
- [ ] **Font loading**: `font-display: swap`, preload critical fonts

### Indexing & Crawling
- [ ] **Crawl budget**: No pages duplicadas, no infinite crawl traps
- [ ] **JavaScript rendering**: Server-side o pre-rendering para SPAs
- [ ] **Core Web Vitals pasables**: INP < 200ms (crítico para Googlebot)
- [ ] **Log file analysis**: Crawl frequency, crawl errors

---

## Workflow

### Step 1: Lighthouse CI Setup

```yaml
# .lighthouserc.yml - Configuración SOTA 2025
ci:
  collect:
    url: ["http://localhost:3000"]
    numberOfRuns: 3
    startServerCommand: "npm run start"
    startServerReadyPattern: "Local:.*http://\[::\]:3000"
    startServerReadyTimeout: 30000
    settings:
      preset: desktop
      throttling:
        rttMs: 40
        throughputKbps: 10240
        cpuSlowdownMultiplier: 1
      formFactor: desktop
      screenEmulation:
        mobile: false
        width: 1440
        height: 900
        deviceScaleFactor: 1
        disabled: false
  assert:
    preset: lighthouse:recommended
    assertions:
      categories:performance:
        minScore: 0.9
      categories:accessibility:
        minScore: 0.9
      categories:best-practices:
        minScore: 0.9
      categories:seo:
        minScore: 0.9
      lcp: ["warn", {maxNumericValue: 2500}]
      inp: ["error", {maxNumericValue: 200}]
      cls: ["error", {maxNumericValue: 0.1}]
      first-contentful-paint: ["warn", {maxNumericValue: 1800}]
      total-blocking-time: ["warn", {maxNumericValue: 200}]
  upload:
    target: temporary-public-storage
    reportBackupFolder: .lighthouseci
```

```json
// package.json scripts
{
  "scripts": {
    "lh:audit": "lhci autorun",
    "lh:build": "npm run build && lhci autorun",
    "lh:server": "lhci server --port 9001"
  }
}
```

### Step 2: MCP Integration

#### Chrome DevTools MCP - Page Analysis
```javascript
// MCP tool: npx @modelcontextprotocol/server-chrome-devtools
// O usa puppeteer con axe-core directamente

import puppeteer from 'puppeteer';
import AxeBuilder from '@axe-core/playwright';

async function auditPage(url) {
  const browser = await puppeteer.launch({ headless: 'new' });
  const page = await browser.newPage();
  
  await page.goto(url, { waitUntil: 'networkidle0' });
  
  // Get Core Web Vitals via CDP
  const metrics = await page.metrics();
  const cwv = await page.evaluate(() => {
    return new Promise((resolve) => {
      new PerformanceObserver((list) => {
        const entries = list.getEntries();
        const lastEntry = entries[entries.length - 1];
        resolve({
          LCP: lastEntry.startTime,
          CLS: performance.getEntriesByType('layout-shift').reduce((sum, entry) => sum + entry.value, 0)
        });
      }).observe({ entryTypes: ['largest-contentful-paint', 'layout-shift'] });
    });
  });
  
  // Accessibility audit
  const accessibilityResults = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa'])
    .analyze();
  
  await browser.close();
  
  return { metrics, cwv, accessibility: accessibilityResults };
}
```

#### Playwright MCP - Crawl & Audit
```javascript
// MCP tool: @modelcontextprotocol/server-playwright
// Para crawl comprehensivo con auditoría inline

import { chromium } from 'playwright';

async function crawlAndAudit(baseUrl) {
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: 1920, height: 1080 },
    userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
  });
  
  const page = await context.newPage();
  const results = { pages: [], errors: [] };
  
  // Set up interception para collect failed requests
  page.on('requestfailed', request => {
    results.errors.push({
      url: request.url(),
      failure: request.failure()?.errorText
    });
  });
  
  // Collect all links
  const links = new Set();
  page.on('response', response => {
    if (response.status() >= 300 && response.status() < 400) {
      links.add(response.url());
    }
  });
  
  // Start crawling
  await page.goto(baseUrl, { waitUntil: 'domcontentloaded' });
  
  // Get all internal links
  const internalLinks = await page.$$eval('a[href]', anchors => 
    anchors
      .map(a => a.href)
      .filter(h => h.startsWith(baseUrl))
      .filter((v, i, a) => a.indexOf(v) === i)
  );
  
  // Audit each page
  for (const link of internalLinks.slice(0, 50)) { // Limit para demo
    try {
      await page.goto(link, { waitUntil: 'networkidle' });
      
      const audit = await page.evaluate(() => {
        const getMeta = (name) => document.querySelector(`meta[name="${name}"]`)?.content;
        const getOG = (prop) => document.querySelector(`meta[property="og:${prop}"]`)?.content;
        
        return {
          title: document.title,
          h1: document.querySelector('h1')?.textContent?.trim(),
          metaDesc: getMeta('description'),
          ogTitle: getOG('title'),
          canonical: document.querySelector('link[rel="canonical"]')?.href,
          schemaTypes: [...document.querySelectorAll('script[type="application/ld+json"]')]
            .map(s => JSON.parse(s.textContent)?.['@type'])
            .filter(Boolean),
          imagesWithoutAlt: [...document.querySelectorAll('img')]
            .filter(img => !img.alt).length,
          linksInternal: [...document.querySelectorAll('a[href]')]
            .filter(a => a.href.startsWith(window.location.origin)).length,
        };
      });
      
      results.pages.push({ url: link, ...audit });
    } catch (e) {
      results.errors.push({ url: link, error: e.message });
    }
  }
  
  await browser.close();
  return results;
}
```

### Step 3: Schema Markup (JSON-LD SOTA 2025-2026)

```html
<!-- Article Schema - Blog posts -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title Here",
  "description": "Meta description for SEO",
  "image": "https://example.com/og-image.jpg",
  "author": {
    "@type": "Person",
    "name": "Author Name",
    "url": "https://example.com/author"
  },
  "publisher": {
    "@type": "Organization",
    "name": "Site Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  },
  "datePublished": "2025-03-18",
  "dateModified": "2025-03-18",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://example.com/article"
  }
}
</script>

<!-- FAQ Schema - FAQ pages -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "¿Cómo mejorar el SEO de mi sitio?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Para mejorar el SEO necesitas optimizar velocidad, contenido, y backlinks..."
      }
    },
    {
      "@type": "Question",
      "name": "¿Qué son los Core Web Vitals?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Los Core Web Vitals son métricas de Google que miden..."
      }
    }
  ]
}
</script>

<!-- Product Schema - E-commerce -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "description": "Product description",
  "image": ["https://example.com/img1.jpg", "https://example.com/img2.jpg"],
  "brand": {
    "@type": "Brand",
    "name": "Brand Name"
  },
  "sku": "SKU-123",
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "Seller Name"
    }
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "124"
  }
}
</script>

<!-- HowTo Schema - Tutorials -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "Cómo optimizar Core Web Vitals",
  "description": "Guía paso a paso para mejorar métricas de rendimiento",
  "totalTime": "PT30M",
  "estimatedCost": {
    "@type": "MonetaryAmount",
    "currency": "USD",
    "value": "0"
  },
  "tool": [
    {
      "@type": "HowToTool",
      "name": "Lighthouse CI"
    }
  ],
  "step": [
    {
      "@type": "HowToStep",
      "name": "Configurar Lighthouse CI",
      "text": "Instala y configura Lighthouse CI en tu proyecto",
      "image": "https://example.com/step1.jpg"
    },
    {
      "@type": "HowToStep",
      "name": "Optimizar LCP",
      "text": "Mejora el Largest Contentful Paint optimizando imágenes y CSS"
    }
  ]
}
</script>

<!-- BreadcrumbList - Navegación -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Inicio",
      "item": "https://example.com"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Categoría",
      "item": "https://example.com/categoria"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Artículo Actual"
    }
  ]
}
</script>
```

### Step 4: Google Search Console API Integration

```javascript
// Integration con GSC API para métricas reales
import { google } from 'googleapis';

const searchconsole = google.searchconsole('v1');

async function getSearchAnalytics(siteUrl) {
  const auth = new google.auth.GoogleAuth({
    credentials: JSON.parse(process.env.GOOGLE_SERVICE_ACCOUNT),
    scopes: ['https://www.googleapis.com/auth/webmasters.readonly']
  });
  
  const client = await auth.getClient();
  google.options({ auth: client });
  
  const response = await searchconsole.searchanalytics.query({
    siteUrl: siteUrl,
    requestBody: {
      startDate: '2025-01-01',
      endDate: '2025-03-18',
      dimensions: ['query', 'page', 'country', 'device'],
      rowLimit: 25000,
      aggregationType: 'byPage'
    }
  });
  
  return response.data.rows.map(row => ({
    query: row.keys[0],
    page: row.keys[1],
    clicks: row.clicks,
    impressions: row.impressions,
    ctr: row.ctr,
    position: row.position
  }));
}
```

### Step 5: Automation Scripts

```bash
#!/bin/bash
# seo-audit.sh - Audit completo automation

set -e

echo "🔍 Iniciando SEO Audit..."

# 1. Lighthouse CI
echo "📊 Ejecutando Lighthouse CI..."
npm run lh:audit || echo "⚠️  Lighthouse falló"

# 2. Check sitemap
echo "🗺️  Validando sitemap..."
curl -s "https://example.com/sitemap.xml" | head -100

# 3. Check robots.txt
echo "🤖 Verificando robots.txt..."
curl -s "https://example.com/robots.txt"

# 4. Validate schema markup
echo "📝 Validando JSON-LD..."
npm run validate:schema

# 5. Screaming Frog (si está instalado)
if command -v screaming-frog &> /dev/null; then
  echo "🦊 Crawling con Screaming Frog..."
  screaming-frog seo spider --crawl https://example.com --output-folder ./seo-report
fi

echo "✅ Audit completado. Revisar reportes en ./seo-report"
```

---

## AI-Powered SEO Analysis

### Claude API Integration para Content Analysis

```javascript
// Usar Claude para analizar contenido y sugerir mejoras SEO
import Anthropic from '@anthropic-ai/sdk';

const anthropic = new Anthropic();

async function analyzeContentSEO(content, targetKeyword) {
  const message = await anthropic.messages.create({
    model: "claude-opus-4-5",
    max_tokens: 1024,
    messages: [{
      role: "user",
      content: `Analiza el siguiente contenido para SEO y da recomendaciones específicas:

Título de página: ${content.title}
Meta description: ${content.metaDesc}
H1: ${content.h1}
Palabra clave objetivo: ${targetKeyword}
Contenido (primeros 500 chars): ${content.body.substring(0, 500)}

Proporciona:
1. Score SEO (0-100)
2. Densidad de palabra clave actual vs recomendada
3. Mejoras en titles, meta, headers
4. Sugerencias de contenido faltante
5. Entidades detectadas para Schema markup`
    }]
  });
  
  return message.content;
}
```

### Keyword Research con AI

```javascript
async function generateKeywordClusters(seedKeyword, competitorUrls) {
  const message = await anthropic.messages.create({
    model: "claude-opus-4-5",
    max_tokens: 2048,
    messages: [{
      role: "user",
      content: `Para la palabra clave seed: "${seedKeyword}"

Genera:
1. 20 keywords relacionadas con search volume estimado
2. Clusteriza en 5 categorías temáticas
3. Para cada cluster: keyword principal, secundarias, y tipo de contenido recomendado
4. Basado en los competidores: ${competitorUrls.join(', ')}

Formato: JSON con structure para keyword mapping en CMS`
    }]
  });
  
  return JSON.parse(message.content[0].text);
}
```

---

## Validation Commands

```bash
# Schema Markup Validation
curl -X POST "https://validator.schema.org/validate" \
  -H "Content-Type: application/json" \
  -d '{"jsonld": "..."}'

# Lighthouse CLI
npx lighthouse https://example.com --preset=desktop --output=html --output-path=./report.html

# Check redirect chains
curl -Is https://example.com/page | grep -i location

# Mobile-friendly test
curl "https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run?key=API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'

# Check Core Web Vitals field data
curl "https://chromeuxreport.googleapis.com/v1/records:queryRecord?key=CrUX_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "origin": "https://example.com",
    "metrics": ["largest_contentful_paint", "interaction_to_next_paint", "cumulative_layout_shift"]
  }'
```

---

## MCP Server Configuration

```json
// .cursor/mcp.json - Agregar servers necesarios
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-chrome-devtools"]
    },
    "playwright": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-playwright"]
    },
    "puppeteer": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-puppeteer"]
    }
  }
}
```

---

## Resources

| Resource | URL | Purpose |
|----------|-----|---------|
| Web.dev | https://web.dev | Core Web Vitals guides |
| Lighthouse CI | https://github.com/GoogleChrome/lighthouse-ci | CI/CD integration |
| Schema.org | https://schema.org | Structured data docs |
| Rich Results Test | https://search.google.com/test/rich-results | Validate schema |
| PageSpeed Insights | https://pagespeed.web.dev | Real user metrics |
| Search Console | https://search.google.com/search-console | Site performance |
| Screaming Frog | https://www.screamingfrog.co.uk/seo-spider | Site crawling |
| GTmetrix | https://gtmetrix.com | Performance analysis |
| WebPageTest | https://webpagetest.org | Detailed page analysis |
| CrUX API | https://developer.chrome.com/docs/crux | Field data API |
| WCAG Guidelines | https://www.w3.org/WAI/WCAG22/quickref | Accessibility standards |

---

## Quick Reference - Common Fixes

| Issue | Quick Fix |
|-------|-----------|
| LCP > 2.5s | Preload hero image, optimize to WebP/AVIF, lazy load below-fold |
| INP > 200ms | Break long tasks, defer non-critical JS, use web workers |
| CLS > 0.1 | Set dimensions on images/video, reserve space for ads, avoid insertAfter |
| Missing meta | Use Next.js Metadata API or react-helmet |
| No schema | Add JSON-LD script tag en HEAD, usa Schema.org types |
| Slow TTFB | Enable CDN, caching, optimize server response |
| Mixed content | Force HTTPS, update all http:// links to https:// |
| Duplicate content | Set canonical tags, fix URL parameters en Search Console |


## ⚠️ Gotchas

- **[ERROR]**: Error común
  - **Solución**: Cómo evitar

## 💾 State Persistence
Guardar en:
- `02_Operations/` — Estado activo
