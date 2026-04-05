# OIM SEO & SEM Strategy — Research Document

> **Proyecto**: Office Installations Mayen (OIM)  
> **Sector**: Ingeniería de Gestión de Espacios Corporativos  
> **Ubicación**: Atlanta, GA  
> **Fecha**: Abril 2026

---

## 1. Competidores Atlanta (Análisis SEO)

| Competidor | Dominio | Fortalezas SEO |
|-------------|----------|----------------|
| **GFI Atlanta** | gfiatl.com | Local SEO fuerte, contenido extenso |
| **Office Installation Solutions** | oisoffice.com | GBP optimizado, reseñas |
| **Atlanta Office Interiors** | atlantaofficeinteriors.com | Portfolio visual, servicios claros |
| **OSI Atlanta** | osiatlanta.com | Claims "#1 installer in Georgia" |
| **Workplace Installation Group** | workplaceofficefurniture.com | Servicio en toda Southeast |

---

## 2. Keywords Estratégicas

### Primary Keywords (Alto Volumen)
| Keyword | Intent | Dificultad |
|---------|--------|------------|
| office furniture installation Atlanta | Comercial | Media |
| corporate office relocation Atlanta | Comercial | Media-Alta |
| office furniture reconfiguration Atlanta | Comercial | Baja |
| workspace installation services Atlanta | Comercial | Baja |

### Secondary Keywords (Nicho)
| Keyword | Intent | Dificultad |
|---------|--------|------------|
| cubicle installation Atlanta | Comercial | Baja |
| conference room setup Atlanta | Comercial | Baja |
| office furniture assembly Atlanta | Comercial | Media |
| commercial furniture installers Atlanta | Comercial | Media |

### Long-tail Keywords (Alta Conversión)
| Keyword | Intent |
|---------|--------|
| office furniture installation company Atlanta | Comercial |
| corporate space management services Atlanta | Comercial |
| office relocation company Atlanta Georgia | Comercial |
| professional furniture installation Atlanta | Comercial |

---

## 3. SEO On-Page Strategy

### 3.1 Meta Tags
```html
<title>OIM | Office Installations Mayen — Atlanta Corporate Space Engineering</title>
<meta name="description" content="+8 years experience in Atlanta. Installation, reconfiguration, relocation, and project management for corporate spaces. Engineering workspaces that perform. Call +1 (470) 595-0121">
```

### 3.2 Estructura H1/H2/H3
```html
<!-- Homepage -->
<h1>Engineering Workspaces That Perform</h1>
<h2>Installation</h2>
<h2>Reconfiguration</h2>
<h2>Relocation</h2>
<h2>Project Management</h2>

<!-- Service Pages -->
<h1>Office Furniture Installation Atlanta</h1>
<h2>Workstations & Critical Assets</h2>
<h3>Why Choose OIM for Installation</h3>
```

### 3.3 Schema Markup (LocalBusiness)
```json
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "name": "Office Installations Mayen",
  "alternateName": "OIM",
  "description": "Ingeniería de Gestión de Espacios Corporativos. Installation, reconfiguration, relocation, and project management in Atlanta, GA.",
  "url": "https://oimayen.com",
  "telephone": "+1 (470) 595-0121",
  "email": "Oiminstalllc@gmail.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Atlanta, GA",
    "addressLocality": "Atlanta",
    "addressRegion": "GA",
    "addressCountry": "US"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "33.7490",
    "longitude": "-84.3880"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "opens": "08:00",
    "closes": "18:00"
  },
  "priceRange": "$$",
  "areaServed": {
    "@type": "GeoCircle",
    "geoRadius": "50",
    "geoMidpoint": {
      "@type": "GeoCoordinates",
      "latitude": "33.7490",
      "longitude": "-84.3880"
    }
  },
  "serviceType": [
    "Office Furniture Installation",
    "Office Reconfiguration",
    "Office Relocation",
    "Corporate Project Management"
  ],
  "award": "+8 Years Experience",
  "review": {
    "@type": "Review",
    "reviewRating": {
      "@type": "Rating",
      "ratingValue": "5"
    }
  }
}
```

### 3.4 Keywords en Content
| Página | Keywords Primarias | Keywords Secundarias |
|--------|-------------------|---------------------|
| Home | office furniture installation Atlanta, corporate space management | workspace engineering, facility management |
| Installation | workstation installation, cubicle setup, conference room assembly | ergonomic furniture Atlanta, office furniture mounting |
| Reconfiguration | office redesign Atlanta, workspace optimization, furniture rearrangement | new office architecture, workspace redesign |
| Relocation | office move Atlanta, corporate relocation, office transit | safe disassembly, reinstallation services |
| Project Management | enterprise office installation, corporate project Atlanta | fast turnaround, large scale office |

---

## 4. SEO Técnica

### 4.1 Performance (Core Web Vitals)
| Métrica | Target | Implementación |
|---------|--------|----------------|
| LCP | < 2.5s | Next.js Image optimization, lazy load |
| FID | < 100ms | Framer Motion isolated components |
| CLS | < 0.1 | min-h-[100dvh] en hero sections |
| TTFB | < 600ms | Vercel hosting, edge caching |

### 4.2 Mobile-First
- Responsive design mandatory
- Touch-friendly CTAs (min 44px)
- Hamburger menu para móvil
- Accelerated Mobile Pages (AMP) no necesario con Next.js

### 4.3 SEO Technical Checklist
- [ ] sitemap.xml automático con Next.js
- [ ] robots.txt configurado
- [ ] canonical URLs
- [ ] hreflang para multilingual (si aplica)
- [ ] JSON-LD Schema en todas las páginas
- [ ] Open Graph tags para social
- [ ] Twitter Card meta tags

---

## 5. Google Business Profile (GBP)

### 5.1 Optimización GBP
| Campo | Contenido |
|-------|-----------|
| **Nombre** | Office Installations Mayen |
| **Categoría Principal** | Office Furniture Store |
| **Categorías Secundarias** | Furniture Rental Service, Office Equipment Supplier |
| **Descripción** | +8 years specializing in corporate space engineering. Installation, reconfiguration, relocation, and project management for workspaces in Atlanta, GA. |
| **Dirección** | Atlanta, GA (área de servicio) |
| **Phone** | +1 (470) 595-0121 |
| **Website** | oimayen.com |
| **Email** | Oiminstalllc@gmail.com |
| **Horario** | Mon-Fri 8am-6pm |
| **Servicios** | Installation, Reconfiguration, Relocation, Project Management |

### 5.2 GBP Posts (Mensual)
- Before/After proyectos
- Nuevos clientes/case studies
- Awards o certificaciones
- Festividades locales (Atlanta events)

### 5.3 Reviews Strategy
- Solicitar reseñas después de cada proyecto
- Responder TODAS las reseñas (positivas y negativas)
- incentivación: "Déjenos una reseña y получите..."

---

## 6. Link Building Strategy

### 6.1 Backlinks de Autoridad Local
| Fuente | Tipo | Prioridad |
|--------|------|-----------|
| Atlanta Business Chronicle | PR/News | Alta |
| Atlanta Magazine | Guest Post | Alta |
| Georgia Chamber of Commerce | Directory | Media |
| Better Business Bureau (BBB) | Listing | Alta |
| Houzz / Yelp / Thumbtack | Reviews | Media |

### 6.2 Directorios Locales
- [ ] Atlanta Business Directory
- [ ] Georgia Manufacturers Directory
- [ ] LinkedIn Company Page
- [ ] Crunchbase (si aplica)
- [ ] Clutch.co (B2B reviews)

### 6.3 Content Marketing (Backlinks)
- Blog: "5 Signs Your Office Needs Reconfiguration"
- Blog: "How to Plan a Corporate Office Move in Atlanta"
- Blog: "What to Look for in an Office Furniture Installer"
- Guide: "Corporate Space Management Handbook" ( gated)

---

## 7. SEM / PPC Strategy

### 7.1 Google Ads Estructura

```
Campaign: Office Furniture Installation Atlanta
├── Ad Group: Installation Services
│   ├── Keywords: office furniture installation Atlanta, 
│   │             commercial furniture installation Atlanta
│   └── Ads: 3-4 ads con highlight de diferenciadores
│
├── Ad Group: Relocation Services  
│   ├── Keywords: office relocation Atlanta, corporate move Atlanta
│   └── Ads: 3-4 ads enfatizando "zero downtime"
│
└── Ad Group: Reconfiguration
    ├── Keywords: office reconfiguration Atlanta, workspace redesign
    └── Ads: 3-4 ads con "human flow analysis"
```

### 7.2 Keywords para PPC (Alto Intent)
| Keyword | CPC Est. | Conversión Est. |
|---------|----------|----------------|
| office furniture installation Atlanta | $8-15 | Alta |
| corporate office relocation Atlanta | $12-20 | Alta |
| office furniture installer Atlanta | $10-18 | Alta |
| office setup services Atlanta | $6-12 | Media |

### 7.3 Remarketing
- Display ads para visitantes del sitio
- Retargeting lista de profesionales de oficina
- LinkedIn ads para decision-makers de empresas

### 7.4 Budget Suggestion
| Fase | Budget Mensual | Duración |
|------|----------------|----------|
| Setup | $1,500-2,500 | 3 meses |
| Scaling | $2,500-5,000 | 6 meses |
| Maintenance | $1,500-2,000 | Indefinido |

---

## 8. Social Media SEO

### 8.1 Instagram (@oimayen)
- Bio optimizada con keywords
- Hashtags locales: #AtlantaOffice #GeorgiaBusiness #OfficeFurniture
- Hashtags de industria: #OfficeInstallation #CorporateSpace #WorkspaceDesign
- Posts con location tagging
- Stories con CTAs

### 8.2 LinkedIn
- Company Page optimizada
- Publicaciones con keywords
- Empleados como ambassadors
- LinkedIn Articles sobre industria

### 8.3 YouTube (Opcional)
- "Behind the Project" videos
- Time-lapse de instalaciones
- Client testimonials

---

## 9. Analytics & Tracking

### 9.1 Google Stack
| Herramienta | Propósito |
|-------------|-----------|
| Google Analytics 4 | Tracking completo |
| Google Search Console | SEO monitoring, keywords |
| Google Tag Manager | Eventos custom |
| Google Merchant Center | (si aplica e-commerce) |

### 9.2 KPIs a Monitorear
| Métrica | Target |
|---------|--------|
| Organic traffic growth | +20% mensual |
| Keyword rankings (top 10) | 15+ keywords |
| Local pack visibility | #1-3 en Atlanta |
| GBP visibility | Map pack #1 |
| Conversion rate (web) | > 3% |
| Phone calls from GBP | > 50/month |
| CTR (ads) | > 4% |

---

## 10. Timeline de Implementación

| Mes | Acciones SEO/SEM |
|-----|------------------|
| **Mes 1** | GBP setup, On-page SEO, Schema, Technical SEO |
| **Mes 2** | Content marketing, link building inicial, social setup |
| **Mes 3** | Google Ads launch, remarketing setup |
| **Mes 4-6** | Optimización basada en datos, scaling PPC |
| **Mes 7-12** | Dominio local, expansión a surrounding areas |

---

## 11. Diferenciación vs Competidores

| Competidor | Su SEO | Ours |
|------------|--------|------|
| GFI | Generic, no diferenciación | Engineering-focused copy |
| OIS | Productos primero | Servicios primero, resultados después |
| OSI | "#1" claim sin evidencia | Métricas reales: +8 years, 200+ projects |
| Workplace | Solo ventas | Engineering approach, proposal de valor única |

---

## 12. Quick Wins (Implementar Primero)

1. ✅ Google Business Profile optimizado
2. ✅ Schema markup en homepage
3. ✅ Meta tags con keywords locales
4. ✅ NAP consistency en todos los directorios
5. ✅ GBP posts mensuales
6. ✅ Página de servicios con keywords
7. ✅ Blog content started

---

*Documento vivo — Actualizar según resultados*