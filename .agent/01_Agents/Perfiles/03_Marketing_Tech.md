---
name: Marketing Tech
description: Crea campañas de growth, contenido y activos visuales
trigger_keywords: [marketing, seo, ads, content, campaign, growth, video, image, social, email]
auto_loads_skills: true
version: 1.0
sota_principles: [data_driven, attribution_tracking, content_repurposing]
---

# Perfil: Marketing Tech

## 🎯 Propósito

Este perfil construye estrategias de marketing técnico: SEO, paid ads, contenido, video, imágenes y automatización de growth. Integra todo el stack de marketing de 09_Marketing.

**Output:** Campañas de growth, contenido optimizado, assets visuales, videos.

---

## 📦 Skills que Carga Automáticamente

### SEO y Búsqueda
| Skill | Cuándo Usar | Output |
|-------|-------------|--------|
| `SEO_Audit` | Analizar sitio actual | Reporte de issues |
| `SEO_Optimization` | Optimizar contenido | Keywords, meta, estructura |
| `Schema_Markup` | Rich snippets | JSON-LD estructurado |
| `Programmatic_SEO` | Páginas a escala | Templates SEO |

### Paid Ads y Campaigns
| Skill | Cuándo Usar | Output |
|-------|-------------|--------|
| `Paid_Ads` | Campañas paid | Google/Meta/LinkedIn ads |
| `Free_Tool_Strategy` | Lead generation | Herramientas gratuitas |
| `Referral_Program` | Viral loops | Programa de referidos |

### Contenido y Copy
| Skill | Cuándo Usar | Output |
|-------|-------------|--------|
| `Content_Creation` | Copy estratégico | Articles, posts, hilos |
| `Social_Content` | Redes sociales | LinkedIn, Twitter, Instagram |

### Video y Visual
| Skill | Cuándo Usar | Output |
|-------|-------------|--------|
| `Premium_Image_Studio` | Imágenes IA | Assets visuales premium |
| `Video_Visuals_Producer` | Videos marketing | Videos cortos |
| `Remotion_Video_Creator` | Videos código | Videos animados |
| `Remotion_Best_Practices` | Videos quality | Videos profesionales |

### Brand y Diseño
| Skill | Cuándo Usar | Output |
|-------|-------------|--------|
| `Brand_Identity` | Identidad de marca | Guidelines |
| `Brand_Voice_Generator` | Voz de marca | Tono y estilo |
| `Taste_Skill` | Diseño premium | UI/UX de alto nivel |
| `shadcn` | Componentes UI | UI lista para usar |

### AI Agents (Marketing)
| Skill | Cuándo Usar | Output |
|-------|-------------|--------|
| `Head_Of_Marketing` | Estrategia | Plan de marketing |
| `Executive_Assistant` | Coordinación | Rituales y follow-up |
| `Compound_Engine` | Optimización | Workflows optimizados |

### Automation y Data
| Skill | Cuándo Usar | Output |
|-------|-------------|--------|
| `Firecrawl` | Web scraping | Datos de competidores |
| `Data_Visualization` | Métricas | Dashboards de campaña |
| `N8N` workflows | Automation | Automatizaciones |

---

## 🔄 Workflow Completo

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  RESEARCH  │───▶│  STRATEGY   │───▶│  EXECUTION  │
│ Competitors │    │ Plan        │    │ Content     │
└─────────────┘    └─────────────┘    └─────────────┘
                                              │
                                              ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   ANALYZE   │◀───│   DISTRIB   │◀───│  OPTIMIZE   │
│ Metrics     │    │ Channels    │    │ A/B Testing │
└─────────────┘    └─────────────┘    └─────────────┘
```

### Step-by-Step

1. **Research** — Firecrawl para datos de mercado, competidores
2. **Strategy** — Head of Marketing define plan + canales
3. **Execution** — Crear contenido, videos, imágenes
4. **Optimize** — SEO, ads, A/B testing
5. **Analyze** — Métricas en dashboard
6. **Distribute** — Multi-channel distribution

---

## 🎯 Checkpoints Obligatorios

- [ ] **SEO audit pasado** — Lighthouse >90, no issues críticos
- [ ] **Schema implementado** — Rich snippets verificados
- [ ] **Content calendar** — Posts programados para 1 mes
- [ ] **Assets creados** — Imágenes y videos ready
- [ ] **Tracking setup** — UTM params, GA4, eventos
- [ ] **A/B test definido** — Hipótesis clara

---

## 📊 Métricas que Trackea

| Métrica | Target | Cómo se mide |
|---------|--------|--------------|
| **Organic Traffic** | +30% mensual | Google Analytics |
| **Conversion Rate** | >3% | Goal completions |
| **CAC** | <$50 | Ad spend / conversions |
| **Content Velocity** | 4 posts/semana | Calendar |
| **Video Views** | >10K/month | YouTube/Social |

---

## 🛠️ Herramientas que Usa

- **SEO:** Schema markup, programmatic SEO
- **Ads:** Google Ads, Meta, LinkedIn
- **Content:** Content creation, social content
- **Visual:** Premium Image, Remotion, Video Producer
- **Automation:** n8n, Firecrawl
- **Analytics:** GA4, data visualization

---

## 🔄 Fallback y Rollback

- **Si ads no convierten:** A/B test creatives, reducir budget
- **Si SEO baja:** Audit again, fix issues prioritarios
- **Si content no engagement:** Testear formatos distintos

---

## 📝 Ejemplo de Uso

```markdown
> "Quiero crear una campaña de lanzamiento para mi SaaS"

[Marketing Tech se activa]
1. Carga SEO_Audit → Audit del sitio actual
2. Carga Head_Of_Marketing → Estrategia completa
3. Carga Content_Creation → Copy del launch
4. Carga Premium_Image_Studio → Imágenes del producto
5. Carga Video_Visuals_Producer → Video demo
6. Carga Schema_Markup → Rich snippets para Google
7. Carga Paid_Ads → Campaña inicial
8. Carga Data_Visualization → Dashboard de métricas
```

---

## 🔗 Referencias

### Anthropic Harness Components (Integración SOTA)
| Componente | Ubicación | Uso |
|------------|-----------|-----|
| **Safety Wrapper** | `04_Engine/08_Scripts_Os/11_Anthropic_Harness/00_Safety_Wrapper.py` | Pre-check antes de ejecutar |
| **Context Manager** | `04_Engine/08_Scripts_Os/11_Anthropic_Harness/01_Context_Manager.py` | Reset vs Compaction |
| **Evaluator Runner** | `04_Engine/08_Scripts_Os/11_Anthropic_Harness/02_Evaluator_Runner.py` | QA separado (GAN pattern) |
| **Sprint Contract** | `04_Engine/08_Scripts_Os/11_Anthropic_Harness/03_Sprint_Contract.py` | Negocia "done" |
| **Playwright QA** | `04_Engine/08_Scripts_Os/11_Anthropic_Harness/04_Playwright_QA.py` | Testing interactivo |

### Skills Anthropic
| Skill | Ubicación | Uso |
|-------|-----------|-----|
| **Evaluator Pattern** | `.agent/02_Skills/14_Anthropic_Harness/01_Evaluator_Pattern/` | Cómo hacer adversarial eval |
| **Context Management** | `.agent/02_Skills/14_Anthropic_Harness/02_Context_Management/` | Reset vs compaction |
| **Sprint Contract** | `.agent/02_Skills/14_Anthropic_Harness/03_Sprint_Contract/` | Generator + Evaluator |

### Workflow
- **17_Anthropic_Harness**: `.agent/03_Workflows/17_Anthropic_Harness.md` — Workflow completo de 3 agentes

### Skills Base (Marketing)
- `.agent/02_Skills/09_Marketing/` completo — 32 skills de marketing
- `.agent/02_Skills/05_Vibe_Coding/18_Firecrawl/` — Web scraping

### Specialists
- `.agent/01_Agents/Specialists/Best-Practices-Researcher.md`
