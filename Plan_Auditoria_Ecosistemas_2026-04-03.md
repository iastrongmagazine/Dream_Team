# PLAN MAESTRO v2.0: Auditoria Ecosistemas + Bootstrap AOLI Web
# Atlanta Office Liquidators - atlantaofficeliquidators.com

**Version:** 2.0 | **Fecha:** 2026-04-03 | **Estado:** Pendiente proximo reset

---

## OBJETIVO DUAL

1. **Auditar** ecosistemas PersonalOS v6.1 - validar que todo funciona
2. **Arrancar** proyecto web AOLI con stack SOTA

**Principio:** La auditoria es el runway para el proyecto web. Cada skill validada es una herramienta lista para AOLI.

---

## CONTEXTO PROYECTO WEB

- **Cliente:** Atlanta Office Liquidators (AOLI)
- **Web actual:** atlantaofficeliquidators.com
- **Rubro:** Liquidacion mobiliario de oficina - compra/venta muebles usados
- **Mercado:** Atlanta metro - empresas que cierran/mudan + compradores B2B y hogares
- **Objetivo:** Generar leads de liquidacion + catalogo inventario vendible

---

## STACK SOTA 2026

### Core
| Tecnologia | Version | Por que |
|------------|---------|--------|
| Next.js | 15 | App Router, PPR, Partial Pre-rendering |
| React | 19 | Server Components, use() hook, Server Actions |
| TypeScript | 5 strict | Const types pattern, zero any |
| Tailwind CSS | 4 | CSS-first config, @theme directive |

### CMS + DB
| Tecnologia | Por que |
|------------|--------|
| Payload CMS v3 | TypeScript-native, panel cliente, sin vendor lock-in |
| Drizzle ORM | TS-first, mas liviano que Prisma |
| Neon | PostgreSQL serverless, escala a cero |

### Features
| Tecnologia | Uso |
|------------|----|
| Better Auth | Auth admin panel - reemplaza NextAuth |
| Resend + React Email | Emails cotizacion, confirmaciones |
| Uploadthing | Upload fotos inventario |
| Cloudinary | Optimizacion imagenes |
| React Hook Form + Zod 4 | Validacion forms |
| Meilisearch | Busqueda inventario typo-tolerant |
| Claude API + AI SDK 5 | Asistente cotizacion conversacional IA |
| Vercel | Deploy + Edge Network + Analytics |
| Vitest + Playwright | Unit + E2E testing |
| Schema.org JSON-LD | LocalBusiness + Product SEO |

---

## ARQUITECTURA DE PAGINAS



---

## SKILLS PERSONALOS USADOS EN AOLI

| Skill | Path | Uso |
|-------|------|----|
| Next.js 15 | 05_Vibe_Coding/02_Nextjs_15/ | Framework principal |
| React 19 | 05_Vibe_Coding/01_React_19/ | Server Components |
| TypeScript | 05_Vibe_Coding/05_TypeScript/ | Todo el codebase |
| Tailwind 4 | 05_Vibe_Coding/03_Tailwind_4/ | Estilos |
| Zod 4 | 05_Vibe_Coding/07_Zod_4/ | Validacion forms |
| AI SDK 5 | 05_Vibe_Coding/08_Ai_Sdk_5/ | Asistente cotizacion |
| Playwright | 06_Testing/08_E2e_Testing/ | E2E testing |
| DevOps | 07_DevOps/ | Deploy Vercel |
| SEO SOTA | 17_SEO_SOTA_Master/ | SEO local Atlanta |
| Product Design | 04_Product_Design/ | UI/UX premium |
| SDD | 01_Agent_Teams_Lite/ | Gestion del proyecto |

---

## FASE 0 - MCP LIVE CONNECTIVITY [NUEVA - 5 min]

Si alguno falla: diagnosticar antes de continuar. No desperdiciar creditos con MCPs rotos.



---

## FASE 1 - INVENTARIO AUTOMATIZADO (15 min)

0



---

## FASE 2 - VALIDACION DOCUMENTACION (20 min)



---

## FASE 3 - VALIDACION FUNCIONAL (60 min)

### 3.1 Stack Web AOLI - P0 CRITICO


### 3.2 SDD end-to-end - P0 CRITICO


### 3.3 Hillary Life OS - P1


### 3.4 CE Compound Engineering - P1


### 3.5 Scripts HUBs - P1


### 3.6 GGA Guardian Angel - P1


### 3.7 Engram end-to-end - P1


### 3.8 Agents - P1


### 3.9 N8N + Integraciones - P2


---

## FASE 4 - VALIDACION INTEGRACION (20 min)



---

## FASE 5 - REPORTE (15 min)



Severity: CRITICAL / WARNING / SUGGESTION

---

## FASE 6 - BOOTSTRAP PROYECTO AOLI [EL OBJETIVO REAL]



---

## PRIORIZACION CON LIMITE DE CREDITOS

| Prioridad | Fases | Tiempo | Bloquea AOLI? |
|-----------|-------|--------|---------------|
| P0 - siempre | Fase 0 + 3.1 + 3.2 | 30 min | SI |
| P1 - si hay creditos | Fases 1, 2, 3.3-3.8 | 60 min | Parcialmente |
| P2 - nice to have | Fases 3.9, 4 | 30 min | NO |
| P3 - si sobra | Fase 5 | 15 min | NO |
| GOAL - el objetivo | Fase 6 Bootstrap | 45 min | ES el proyecto |

**Regla de oro:** Si hay que elegir entre documentar mas y arrancar Fase 6, arrancar Fase 6.

---

## CRITERIOS DE EXITO

### Sistema:
- [ ] MCPs criticos responden (Fase 0 = 100%)
- [ ] Stack web skills validas (Fase 3.1 = 9/9)
- [ ] SDD end-to-end funciona
- [ ] GGA corre en commits

### Proyecto AOLI:
- [ ] Repo aoli-web en GitHub
- [ ] Next.js 15 + Payload + Drizzle corriendo local
- [ ] Primer deploy Vercel activo
- [ ] SDD init ejecutado sobre el proyecto

---

## OUTPUT ESPERADO DEL PROXIMO RESET



---

## NOTAS TECNICAS AOLI

### SEO Local - critico
- Keywords: office furniture liquidation Atlanta, used office furniture Atlanta
- Schema.org LocalBusiness + area de cobertura Atlanta metro
- Core Web Vitals: LCP < 2.5s con Cloudinary
- next-sitemap para sitemap automatico

### Asistente IA - diferenciador SOTA
- claude-haiku-4-5 (velocidad + costo bajo)
- Flujo: cuantas personas + que muebles + necesita pickup
- Genera cotizacion estimada con streaming
- Envia por email via Resend: cliente + AOLI team

### Inventario - core del negocio
- Payload CMS: titulo, categoria, precio, estado, fotos, disponible
- Descripcion auto-generada por Claude si esta vacia
- Meilisearch indexa via webhook al publicar en Payload
- Frontend: filtros categoria + rango precio + estado

---

*Think Different PersonalOS v6.1*
*AOLI Web Project - Stack SOTA 2026*
*Actualizado: 2026-04-03 v2.0*
