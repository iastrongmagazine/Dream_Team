# PLAN-OIM-WEBSITE — Rediseño Completo

> **Proyecto**: Office Installations Mayen (OIM)  
> **Sector**: Ingeniería de Gestión de Espacios Corporativos  
> **Ubicación**: Atlanta, GA  
> **Contacto**: Jose P Mayen — +1 (470) 595-0121 — Oiminstalllc@gmail.com  
> **Experiencia**: +8 años  
> **Instagram**: @oimayen

---

## 1. Stack Tecnológico

| Componente | Tecnología |
|------------|------------|
| Framework | Next.js 16.2.2 |
| UI | React 19.2.4 |
| Styling | Tailwind CSS 4 |
| Motion | Framer Motion |
| Testing | Vitest (TDD Strict) |
| Validación | Zod |

---

## 2. Configuración Pendiente (EJECUTAR PRIMERO)

### 2.1 Instalar Vitest (TDD Mode)
```bash
npm install -D vitest @vitejs/plugin-react @testing-library/react @testing-library/jest-dom jsdom
```

### 2.2 Actualizar package.json
- Name: `"oim-website"`
- Version: `"1.0.0"`

### 2.3 Actualizar AGENTS.md
Agregar reglas OIM:
- Copy standard: "El buen diseño es honesto" (Rams 10%)
- Sector: Ingeniería de Gestión de Espacios Corporativos
- Next.js 16 rules apply

---

## 3. Documentos a Crear

| # | Archivo | Descripción |
|---|---------|-------------|
| 1 | `docs/OIM-COPY-MASTER.md` | Copy maestro por sección web |
| 2 | `docs/OIM-DESIGN-SYSTEM.md` | Sistema de diseño (colores, tipografía, componentes) |
| 3 | `00_Recursos_Varios/OIM-VALUE-PROPOSITION.md` | Propuesta de valor convertida del HTML |

---

## 4. Sistema de Diseño

### 4.1 Paleta de Colores
| Role | Color | Hex |
|------|-------|-----|
| Background | Negro profundo | `#0A0A0A` |
| Surface | Gris oscuro | `#141414` |
| Text Primary | Blanco | `#FFFFFF` |
| Text Secondary | Gris medio | `#A1A1A1` |
| Accent Primary | Naranja industrial | `#F97316` |
| Accent Secondary | Verde lima | `#84CC16` |

### 4.2 Tipografía
| Elemento | Fuente | Peso | Tamaño |
|----------|--------|------|--------|
| Headlines | Poppins | 700-900 | 48-72px |
| Subheadlines | Poppins | 500 | 20-24px |
| Body | DM Sans | 400 | 16px |
| Labels | Poppins | 600 | 12px (uppercase) |
| Botones | Poppins | 600 | 14px |

### 4.3 Layout
```
Navbar (fixed, glass) → Hero → Services (4 cards) → Stats → Projects → About → CTA/Contact → Footer
```

---

## 5. Estructura de Ejecución

### Fase 1: Setup
- [ ] Instalar Vitest + configurar vite.config.ts
- [ ] Actualizar package.json
- [ ] Actualizar AGENTS.md

### Fase 2: Diseño
- [ ] Actualizar globals.css con tokens OIM
- [ ] Implementar tipografía (Poppins + DM Sans via Google Fonts)
- [ ] Crear/actualizar componentes

### Fase 3: Contenido
- [ ] Integrar copy maestro en cada sección
- [ ] Agregar fotos de proyectos (@oimayen)
- [ ] SEO + Schema LocalBusiness

### Fase 4: Testing (TDD)
- [ ] RED: Escribir test que falla
- [ ] GREEN: Implementar componente
- [ ] REFACTOR: Optimizar código

---

## 6. Copy Principles (Rams 10%)

> **"El buen diseño es honesto"**
> - Sin adjetivos vacíos ("best", "amazing", "premier")
> - Los números demuestran: "+8 YEARS", "200+ PROJECTS", "100% ON-TIME"
> - Copy sirve al usuario, no al ego

---

## 7. Secciones Web (Copy Maestro)

### 7.1 Navbar
- Logo: `OIM`
- Links: `Projects | Services | About | Contact`
- CTA: `Start a Project →`

### 7.2 Hero
- Tagline: `ATLANTA, GA — EST. 2018`
- Headline: `Engineering Workspaces That Perform`
- Subheadline: `Ingeniería de Gestión de Espacios Corporativos. Transformamos infraestructura en rendimiento medible.`
- CTAs: `View Our Work` | `Get a Quote`

### 7.3 Services (4 cards)
| # | Label | Title | Copy |
|---|-------|-------|------|
| 1 | INSTALLATION | Workstations & Critical Assets | High-fidelity integration of ergonomic stations, modular cubicles, and conference systems. We engineer for performance, not just assembly. |
| 2 | RECONFIGURATION | Adaptive Space Engineering | Evolutionary environment redesign based on human flow analysis. From ground-up implementation to strategic furniture rearrangement. |
| 3 | RELOCATION | Precision Transit & Disassembly | Technical disassembly preserving asset lifespan. Minimized risk, maximized uptime. Full reinstallation at new locations. |
| 4 | PROJECT MANAGEMENT | Enterprise-Scale Execution | From boutique startups to multinational deployments. We deliver on time, on spec, with zero tolerance for downtime. |

### 7.4 Stats
`+8 YEARS — EXPERIENCE — IN ATLANTA`  
`200+ — PROJECTS — COMPLETED`  
`100% — ON-TIME — DELIVERY`  
`FORTUNE 500 — CLIENTS — TRUST US`

### 7.5 Projects
Label: `SELECTED WORK`  
Headline: `Built for Performance`

### 7.6 About
Label: `BACKGROUND`  
Headline: `8+ Years of Precision`  
Copy: Founded by Jose P Mayen — Atlanta-based specialists in corporate space engineering. We don't just install furniture. We optimize the environment where decisions are made.

Valores: PRECISION | RELIABILITY | PERFORMANCE

### 7.7 CTA/Contact
Label: `LET'S TALK`  
Headline: `Ready to Optimize Your Space?`  
Contact: +1 (470) 595-0121 | Oiminstalllc@gmail.com | Atlanta, GA  
CTA: `Start a Conversation →`

### 7.8 Footer
Logo: `OIM` | Tagline: `Engineering Workspaces That Perform`
Links: Services, Company, Contact
Social: Instagram, LinkedIn

---

## 8. UX Writing (Microcopy)

| Contexto | Antes (Genérico) | Después (SOTA) |
|----------|------------------|----------------|
| Primary CTA | "Get Started" | "View Our Work" |
| Secondary CTA | "Contact Us" | "Get a Quote" |
| Form Submit | "Submit" | "Send Message" |
| Form: Name | "Name" | "Your Name" |
| Form: Email | "Email" | "Work Email" |
| Form: Message | "Message" | "Tell Us About Your Project" |
| Success | "Thank you" | "Message received. We'll be in touch within 24 hours." |

---

## 9. SEO & Schema

- **Meta Title**: `OIM | Office Installations Mayen — Atlanta Corporate Space Engineering`
- **Meta Description**: `+8 years experience in Atlanta. Installation, reconfiguration, relocation, and project management for corporate spaces. Engineering workspaces that perform.`
- **Schema**: `LocalBusiness / ProfessionalService`
- **Keywords**: office furniture installation Atlanta, corporate space management, facility management Atlanta, office relocation Atlanta, workspace engineering

---

## 10. Assets Requeridos

| Asset | Estado | Fuente |
|-------|--------|--------|
| Fotos proyectos | ❌ Pendiente | Instagram @oimayen |
| Logo clientes | ❌ Pendiente | Pedir a Jose |
| Foto equipo/Jose | ❌ Pendiente | Pedir a Jose |
| Iconos servicios | ✅ Listo | Lucide React: HardHat, Move, Settings, Users |

---

## 11. Inspiración Visual (Referencias Analizadas)

| # | ElementoTomado | Fuente |
|---|-----------------|--------|
| 1 | Tipografía Poppins | Imagen 3 (Brand Board) |
| 2 | Cards de Servicios | Imagen 4, 5 (Visionary) |
| 3 | Sección Estadísticas | Imagen 4 |
| 4 | Trust Bar (Logos) | Imagen 2 |
| 5 | Subrayado/Trazo énfasis | Imagen 1 |
| 6 | Estructura copy | Imagen 6 (propuesta_de_valor) |

---

## 12. Propuesta de Valor (del HTML)

> **Manifiesto**: "No movemos muebles. Ejecutamos proyectos."
> 
> **Declaración de posicionamiento**: "Somos el equipo que se hace responsable del resultado completo. No de una parte del proceso: del proyecto entero, de principio a fin."
> 
> **Lo que el cliente compra**:
> - Certeza (proceso no falla)
> - Control sin carga (delegar sin perder visibilidad)
> - Reputación intacta (proyecto sale bien)
> 
> **El dolor del mercado**:
> - Crews que no cumplen
> - Coordinación fragmentada
> - Costos que aparecen después
> 
> **Diferenciador**: "No somos el crew que instala. Somos el equipo que garantiza que funciona."

---

## 13. Diferenciación SOTA vs Competidores Atlanta

| Competidor | OIM |
|------------|-----|
| Stock photos | Fotos reales de proyectos |
| "Best service" vacío | Métricas + evidencia |
| Genérico | Branding industrial único |
| Template básico | Animaciones custom |

---

## 14. Próximos Steps

1. ✅ Plan creado
2. ⏳ Ejecutar Fase 1 (Setup)
3. ⏳ Crear documentos (copy, design system)
4. ⏳ Implementar redesign
5. ⏳ Testing TDD
6. ⏳ Deploy

---

*Documento vivo — Actualizar según avance*