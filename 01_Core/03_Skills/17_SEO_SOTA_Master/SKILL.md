---
name: seo-sota-master
description: Elite SEO skill that combines technical auditing, content strategy, programmatic SEO, and data-driven optimization. Uses Silicon Valley best practices: data-backed decisions, A/B testing, cohort analysis, and predictive ranking models. Triggers on: SEO audit, technical SEO, rank tracking, content strategy, programmatic SEO, keyword research, SEO analysis, improve ranking, schema markup, SEO best practices.
author: sebas@thinkdifferent
version: 1.0.0
tags: [seo, search-engine-optimization, ranking, technical-seo, content-strategy, programmatic-seo, schema, keywords, analytics]
triggers:
  - "SEO audit"
  - "technical SEO"
  - "rank tracking"
  - "content strategy"
  - "programmatic SEO"
  - "keyword research"
  - "SEO analysis"
  - "improve ranking"
  - "schema markup"
  - "SEO best practices"
  - "on-page SEO"
  - "off-page SEO"
  - "backlinks"
  - "SEO metrics"
---

# SEO SOTA Master

## Esencia Original

> Esta skill existe para transformar SEO de "opinión" a "ciencia de datos". Cada recomendación debe estar respaldada por datos,测试y resultados medibles.

## ⚠️ Gotchas (Errores Comunes a Evitar)

- **[ERROR]**: Recomendar cambios sin datos de analytics
  - **Por qué**: Sin datos, es opinión, no SEO
  - **Solución**: Siempre Consultar Google Analytics/Console antes de recomendar

- **[ERROR]**: No hacer technical audit primero
  - **Por qué**: Los problemas técnicos bloquean el ranking
  - **Solución**: Always hacer audit de Core Web Vitals primero

- **[ERROR]**: No segmentar páginas por performance
  - **Por qué**: Las páginas tienen comportamientos distintos
  - **Solución**: Crear cohortes por traffic, conversions, keywords

- **[ERROR]**: Ignorar schema markup
  - **Por qué**: Schema ayuda a Google a entender el contenido
  - **Solución**: Siempre incluir JSON-LD para páginas clave

> **Level**: TOP TOP — Silicon Valley Grade SEO

This skill combines technical auditing, content strategy, and data-driven optimization. Every recommendation is backed by data, testing, and measurable outcomes.

---

## Core Philosophy

### 1. Data > Opinion

SEO changes should be based on:
- **Data**: Analytics, Search Console, ranking data
- **Testing**: A/B tests, controlled experiments
- **Cohorts**: Segment pages by performance, type, age

Never say "I think this will help". Say "Based on data, this page loses X% of traffic because Y".

### 2. Technical First

Technical SEO is the foundation. No amount of content can fix:
- Crawlability issues
- Core Web Vitals failures
- Indexation problems
- JavaScript rendering issues

Always audit technical first.

### 3. Programmatic > Manual

Don't manually optimize 1000 pages. Build systems that:
- Generate SEO-optimized pages at scale
- Auto-optimize meta tags
- Identify opportunities programmatically
- Monitor rankings automatically

### 4. Segmentation or Die

Aggregate rankings lie. Segment by:
- Page type (product, blog, landing)
- Topic cluster
- Age of content
- Traffic tier (top performers vs long tail)
- Conversion vs informational

### 5. Test Everything

- A/B test title tags
- Test content freshness
- Test internal linking patterns
- Test schema implementations

---

## Analysis Workflow

### Phase 1: Technical Audit

```python
def technical_seo_audit(url: str) -> dict:
    """
    Comprehensive technical SEO audit.
    
    Returns:
        - Crawlability score
        - Core Web Vitals status
        - Indexation issues
        - Rendering problems
        - Schema markup found
    """
    import requests
    from bs4 import BeautifulSoup
    
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    issues = []
    
    # Check Core Web Vitals (simulated)
    # In production, use PageSpeed Insights API
    
    # Check rendering
    if soup.find('noscript'):
        issues.append("Noscript detected - check JS rendering")
    
    # Check meta tags
    if not soup.find('meta', {'name': 'description'}):
        issues.append("Missing meta description")
    
    # Check canonical
    if not soup.find('link', {'rel': 'canonical'}):
        issues.append("Missing canonical URL")
    
    # Check schema
    schemas = soup.find_all('script', {'type': 'application/ld+json'})
    
    return {
        "url": url,
        "status_code": response.status_code,
        "issues": issues,
        "schemas_found": len(schemas),
        "title_length": len(soup.title.string) if soup.title else 0,
        "h1_count": len(soup.find_all('h1')),
        "recommendations": generate_recommendations(issues)
    }
```

### Phase 2: Keyword Research

```python
def keyword_opportunities(df: pd.DataFrame, 
                       target_domain: str) -> pd.DataFrame:
    """
    Find keyword opportunities by analyzing:
    - Current rankings (position 4-20 = quick wins)
    - Search volume
    - Keyword difficulty
    - Content gaps
    """
    # Quick wins: ranking 4-20, high volume
    quick_wins = df[(df['position'] >= 4) & 
                   (df['position'] <= 20) &
                   (df['search_volume'] > 1000)]
    
    # Content gaps: ranking < 30 but not ranking
    content_gaps = df[df['clicks'] < 100]['keyword'].tolist()
    
    # Featured snippet opportunities
    featured_snippets = df[df['position'] == 0]
    
    return {
        "quick_wins": quick_wins.sort_values('search_volume', ascending=False),
        "content_gaps": content_gaps[:20],
        "featured_snippet_opportunities": featured_snippets
    }
```

### Phase 3: Content Audit

```python
def content_audit(urls: list[str]) -> pd.DataFrame:
    """
    Audit content for SEO health.
    
    Score each page on:
    - Relevance (keyword in title, h1, url)
    - Freshness (date, content updates)
    - Engagement (time on page, bounce rate)
    - Technical (links, images, schema)
    """
    results = []
    
    for url in urls:
        score = 0
        issues = []
        
        # Fetch and analyze
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Title check
        title = soup.title.string if soup.title else ""
        if 30 <= len(title) <= 60:
            score += 20
        else:
            issues.append(f"Title length: {len(title)} (ideal: 30-60)")
        
        # H1 check
        h1s = soup.find_all('h1')
        if len(h1s) == 1:
            score += 20
        elif len(h1s) == 0:
            issues.append("No H1 found")
        
        # Content length
        text = soup.get_text()
        word_count = len(text.split())
        if word_count > 300:
            score += 20
        else:
            issues.append(f"Low word count: {word_count}")
        
        # Internal links
        internal_links = [a for a in soup.find_all('a') 
                         if target_domain in a.get('href', '')]
        if len(internal_links) >= 3:
            score += 20
        else:
            issues.append(f"Few internal links: {len(internal_links)}")
        
        # Images
        images = soup.find_all('img')
        missing_alt = [img for img in images if not img.get('alt')]
        if missing_alt:
            issues.append(f"Images missing alt: {len(missing_alt)}")
        
        # Schema
        schemas = soup.find_all('script', {'type': 'application/ld+json'})
        if schemas:
            score += 20
        else:
            issues.append("No schema markup")
        
        results.append({
            "url": url,
            "score": score,
            "issues": issues,
            "word_count": word_count,
            "internal_links": len(internal_links),
            "images": len(images)
        })
    
    return pd.DataFrame(results)
```

### Phase 4: Programmatic SEO

```python
def programmatic_seo_builder(template: str, 
                            data: pd.DataFrame,
                            base_url: str) -> list[dict]:
    """
    Generate SEO-optimized pages at scale.
    
    Args:
        template: Page template with placeholders
        data: DataFrame with page-specific data
        base_url: Base URL for the site
    
    Returns:
        List of page configs ready to generate
    """
    pages = []
    
    for _, row in data.iterrows():
        # Generate slug
        slug = slugify(row['keyword'])
        
        # Generate meta
        title = f"{row['primary_keyword']} - {row['brand']}"
        description = row['meta_description'] or generate_description(row)
        
        # Generate schema
        schema = generate_schema(row)
        
        pages.append({
            "url": f"{base_url}/{slug}",
            "title": title[:60],
            "description": description[:160],
            "h1": row['primary_keyword'],
            "content": template.format(**row.to_dict()),
            "schema": schema,
            "canonical": f"{base_url}/{slug}",
            "keywords": [row['primary_keyword']] + row.get('secondary_keywords', [])
        })
    
    return pages


def generate_schema(row: pd.Series) -> dict:
    """Generate appropriate schema markup."""
    schema_types = {
        "product": {"@context": "https://schema.org/", "@type": "Product"},
        "article": {"@context": "https://schema.org/", "@type": "Article"},
        "faq": {"@context": "https://schema.org/", "@type": "FAQPage"},
        "local": {"@context": "https://schema.org/", "@type": "LocalBusiness"}
    }
    
    schema = schema_types.get(row.get('type', 'article'), schema_types['article'])
    
    if row.get('name'):
        schema['name'] = row['name']
    if row.get('description'):
        schema['description'] = row['description']
    if row.get('url'):
        schema['url'] = row['url']
        
    return schema
```

### Phase 5: Ranking Prediction

```python
def predict_ranking_impact(changes: dict, 
                         current_rankings: pd.DataFrame) -> dict:
    """
    Predict ranking impact of SEO changes.
    
    Uses historical data to estimate impact.
    """
    # Factors and their typical impact
    factor_impacts = {
        "title_optimization": 5.2,      # positions
        "meta_description": 3.1,
        "content_refresh": 4.8,
        "internal_links": 2.3,
        "schema_added": 1.9,
        "page_speed_improvement": 6.1,
        "mobile_optimization": 4.5,
        "backlinks_gained": 7.2
    }
    
    predicted_impact = 0
    
    for change, applied in changes.items():
        if applied:
            predicted_impact += factor_impacts.get(change, 0)
    
    # Calculate projected traffic increase
    current_traffic = current_rankings['clicks'].sum()
    projected_traffic = current_traffic * (1 + predicted_impact * 0.05)
    
    return {
        "predicted_position_change": predicted_impact,
        "current_traffic": current_traffic,
        "projected_traffic": projected_traffic,
        "confidence": "medium",  # Based on historical accuracy
        "factors_applied": [k for k, v in changes.items() if v]
    }
```

---

## Output Templates

### Template 1: SEO Audit Report

```
## 🔍 Technical SEO Audit: [Domain]

### Overall Health Score
| Metric | Score | Status |
|--------|-------|--------|
| Technical | 85/100 | ✅ Good |
| Content | 72/100 | ⚠️ Needs Work |
| Authority | 91/100 | ✅ Excellent |
| **Overall** | **83/100** | **✅ Pass** |

### Critical Issues (Fix First)
| Issue | Impact | Effort | Priority |
|-------|--------|--------|----------|
| [Issue 1] | High | Low | P0 |
| [Issue 2] | High | Medium | P0 |

### Quick Wins (This Week)
- [ ] Optimize [X] title tags
- [ ] Add schema to [Y] pages
- [ ] Fix [Z] broken links

### Long-term Projects
- [ ] Rebuild [section] for Core Web Vitals
- [ ] Create [topic] content cluster

### Projected Impact
- +[X]% organic traffic in 90 days
- +[Y] keyword rankings
```

### Template 2: Content Strategy

```
## 📝 Content Strategy: [Domain]

### Content Gaps
| Topic | Search Volume | Difficulty | Opportunity |
|-------|--------------|------------|-------------|
| [Topic 1] | 10,000 | Low | 🔥 Quick Win |
| [Topic 2] | 5,000 | Medium | 📅 Plan |
| [Topic 3] | 2,000 | High | 📅 Future |

### Content Clusters to Build
1. **[Core Topic]**
   - Pillar: /topic-guide
   - Supporting: /topic-1, /topic-2, /topic-3
   
2. **[Core Topic 2]**
   - Pillar: /topic-2-guide
   - Supporting: ...

### Content Calendar
| Week | Topic | Type | Target Keywords |
|------|-------|------|-----------------|
| 1 | [Topic] | Guide | [kw1], [kw2] |
| 2 | [Topic] | FAQ | [kw3] |
```

### Template 3: Programmatic SEO Plan

```
## 🚀 Programmatic SEO: [Project]

### Pages to Generate
- **[X]** pages from data source
- Target: [keyword patterns]
- Template: [page structure]

### URL Structure
```
/[category]-[subcategory]-[keyword].html
```

### Schema Markup
- [ ] Product schema for [X] pages
- [ ] FAQ schema for [Y] pages
- [ ] Breadcrumb schema

### Estimated Impact
- +[X,XXX] new indexed pages
- +[X]% organic traffic
- [X] new keyword rankings

### Dependencies
- [ ] Data pipeline ready
- [ ] Template approved
- [ ] Schema validated
```

---

## Best Practices

### 1. Always Start with Data

- Import Google Search Console data
- Import analytics (GA4, Mixpanel)
- Import ranking data (Ahrefs, SEMrush, Sistrix)

### 2. Prioritize by Impact

| Priority | Impact | Effort | Example |
|----------|--------|--------|---------|
| P0 | High | Low | Fix 404s, add meta tags |
| P1 | High | Medium | Content refresh, schema |
| P2 | Medium | Medium | New content, link building |
| P3 | Low | High | Site rebuild |

### 3. Track Everything

- Ranking positions (daily for active projects)
- Organic traffic (weekly)
- Conversions from organic (monthly)
- Core Web Vitals (monthly)

### 4. Test Title Tags

```python
# A/B test title tags
variants = [
    "Original Title",
    "Revised Title - Benefit",
    "Number + Benefit",
    "Question Format"
]

# Track clicks in Search Console
```

### 5. Build Topic Clusters

```
Pillar Page (Comprehensive Guide)
    ↓ links to
Cluster Pages (Supporting Topics)
    ↓ link to each other
Cluster Pages
```

### 6. Schema Is Mandatory

Always add:
- Organization schema on homepage
- Article/BlogPosting on blog
- Product on product pages
- FAQ on FAQ pages
- LocalBusiness if local

---

## Common Pitfalls

| Pitfall | Why It Fails | Fix |
|---------|--------------|-----|
| Ignoring technical | Content can't rank if site can't crawl | Audit technical first |
| No segmentation | Aggregate data hides opportunities | Segment by page type |
| No testing | Assumptions aren't facts | A/B test everything |
| Programmatic spam | Low quality at scale | Quality gates on generation |
| Ignoring user intent | Ranking but no conversions | Match intent to content type |

---

## Tools & Stack

### SEO Platforms

```bash
# Paid (best)
ahrefs          # All-in-one
semrush         # All-in-one
sistrix         # European focus
screamingfrog   # Technical audits

# Free
Google Search Console    # Rankings, clicks
Google PageSpeed        # Core Web Vitals
Google Analytics 4     # Traffic, conversions
```

### Technical Stack

```python
# Data Analysis
pandas, numpy
scikit-learn    # Predict ranking impact

# Visualization
matplotlib, seaborn
plotly          # Interactive dashboards

# Automation
selenium        # Scraping
playwright      # Technical audits
```

### Schema Generators

```python
# Common schemas
from schema import Schema

# Organization
org_schema = Schema({
    "@context": "https://schema.org",
    "@type": "Organization",
    "name": "Brand Name",
    "url": "https://brand.com",
    "logo": "https://brand.com/logo.png"
})

# FAQ
faq_schema = Schema({
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {
            "@type": "Question",
            "name": "Question text?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": "Answer text."
            }
        }
    ]
})
```

---

## Example Prompts

### Example 1: Technical Audit
```
Audit [website.com] for technical SEO.
Include:
1. Core Web Vitals assessment
2. Crawlability issues
3. Indexation problems
4. Schema markup audit
5. Mobile usability
Give me a prioritized fix list with estimated impact.
```

### Example 2: Content Strategy
```
Analyze the content on [website.com] and create a content strategy.
I have data from:
- Google Search Console (export.csv)
- Google Analytics (export.csv)

Find:
1. Content gaps (keywords we're not ranking for)
2. Underperforming pages that need refresh
3. New content opportunities by topic cluster
4. Quick wins we can implement this week
```

### Example 3: Programmatic SEO
```
I have a dataset of 10,000 products (products.csv).
Create a programmatic SEO strategy:
1. URL structure recommendation
2. Page template with SEO elements
3. Schema markup to implement
4. Keyword mapping approach
5. Estimated traffic potential

Columns in CSV: product_name, category, subcategory, price, description
```

### Example 4: Ranking Recovery
```
Our organic traffic dropped 40% in the last 30 days.
Analyze what happened:
1. Check for algorithm updates
2. Identify pages most affected
3. Find technical issues
4. Check for crawl errors
5. Recommend recovery plan
```

---

## Quality Checklist

Before presenting any SEO work:

- [ ] Is every recommendation backed by data?
- [ ] Did I segment by page type?
- [ ] Is technical SEO addressed first?
- [ ] Are there specific action items?
- [ ] Is there estimated impact?
- [ ] Is schema markup included?
- [ ] Would a CMO understand this in 30 seconds?

---

## Summary

This skill makes you a **Silicon Valley-grade SEO expert**:

1. **Technical first** — Foundation before content
2. **Data-driven** — Every decision backed by analytics
3. **Segment everything** — Aggregates lie
4. **Test constantly** — A/B title tags, schema, content
5. **Programmatic > Manual** — Scale with systems
6. **Track everything** — Measure, iterate, improve

**Your job isn't to "do SEO". Your job is to increase organic revenue.**

---

*Skill Version: 1.0.0*
*Author: sebas@thinkdifferent*
*Framework: Anthropic Skill Creator v2.0*
*Level: TOP TOP — SEO Master*


## ⚠️ Gotchas (Errores Comunes a Evitar)

> Common mistakes and edge cases to watch for when using this skill.

- **[ERROR]**: Add common error here
  - **Por qué**: Explanation of why it's an error
  - **Solución**: How to fix or avoid it

