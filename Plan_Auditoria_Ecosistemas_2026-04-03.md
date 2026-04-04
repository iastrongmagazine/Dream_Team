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

- **`/` (Home):** Hero B2B, llamada a la acción principal, listado destacado de liquidaciones y Chat/Bot de cotización rápida.
- **`/inventory`:** Catálogo de productos con filtros por categoría comercial, estado y precio (vía Meilisearch).
  - **`/inventory/[id]`:** Detalle del lote/producto, galería HD, dimensiones e información de contacto/"Quiero este lote".
- **`/services/liquidation`:** Landing page especializada B2B para captación de clientes que liquidan oficinas.
- **`/about`:** Información corporativa de AOLI, equipo y credibilidad (Social Proof).
- **`/admin` (Payload v3):** Panel interno (CMS) para gestión total: subida rápida Uploadthing de fotos, edición de lotes y visualización.
- **`/api/*`:** Endpoints para Server Actions e integración backend (AI SDK 5, Stripe, Meilisearch webhooks).

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

1. **Test MCP `engram`:** Recuperar context o hacer search de reglas previas (`mem_context`).
2. **Test MCP `context7`:** Obtener el ID más reciente para Next.js o Payload (`resolve-library-id`).
3. **Validación General:** Verificar acceso file system / edición iterativa al repo Think_Different.

---

## FASE 1 - INVENTARIO AUTOMATIZADO (15 min)

1. **Definir Collections en Payload v3:** Crear esquemas de `Products`, `Categories` y `Media`.
2. **Setup Meilisearch Webhooks:** Configurar Lifecycle hooks (`afterChange`, `afterDelete`) para replicación indexada de Payload a Meili.
3. **Prompt Ingeniería (Catalogación):** Definir script/prompt mediante el cual Claude va a auto-completar descripciones y extraer specs de las fotos subidas.

---

## FASE 2 - VALIDACION DOCUMENTACION (20 min)

1. **Auditar Skills (05_Vibe_Coding):** Comprobar que `.md` de Next.js, TypeScript y Tailwind existen y tienen las reglas de 2026.
2. **Auditar Reglas SOTA:** Confirmar que no hay referencias cruzadas desactualizadas (ej. NextAuth en vez de BetterAuth).
3. **Verificar Pilar 0:** Revisar si los estándares de plan-first y comunicación en español están propagados en la carpeta `01_Core`.

---

## FASE 3 - VALIDACION FUNCIONAL (60 min)

### 3.1 Stack Web AOLI - P0 CRITICO
- Setup base: Probar comando de instalación (Skeletons / Next+Tailwind).
- Rutas Bajas: Validar compilado inicial en local mediante `npm run dev`.

### 3.2 SDD end-to-end - P0 CRITICO
- Lanzar `sdd-init` sobre subdirectorio de AOLI web.
- Probar la lectura y guardado de issues simulados vía MCP / Engram.

### 3.3 Hillary Life OS - P1
- Validar conectividad de integraciones legacy si afecta o se retroalimenta.

### 3.4 CE Compound Engineering - P1
- Verificar disponibilidad del plugin CE interactivo y rubricas de confianza en la CLI.

### 3.5 Scripts HUBs - P1
- Lanzar testeo genérico en Python/TS HUBs.

### 3.6 GGA Guardian Angel - P1
- Activar dry-run pre-commit hook de GGA para comprobar el linting de strict TS.

### 3.7 Engram end-to-end - P1
- Crear y buscar un recuerdo (topic test) via `mem_save` -> `mem_search`.

### 3.8 Agents - P1
- Comprobar sub-agentes duales (Judgment Day) con una tarea menor simulada.

### 3.9 N8N + Integraciones - P2
- Revisar status de N8N automations de base.

---

## FASE 4 - VALIDACION INTEGRACION (20 min)

1. **Testing de Cotización IA:** Conectar AI SDK 5 con mock de Database (Postgres) para validar Streaming UI.
2. **Emailing:** Probar integración de Resend o simular envío para los request de cotizaciones.
3. **SEO Local:** Correr scripts de genado XML schema.org e insert de tags via Next Metadata rules.

---

## FASE 5 - REPORTE (15 min)

1. Generar consolidado markdown de los estatus (Fase 0-4).
2. Taguear incidentes y fallos con Severidad (CRITICAL / WARNING / SUGGESTION).
3. Cerrar iteración de ecosistemas vía `mem_session_summary`.

Severity: CRITICAL / WARNING / SUGGESTION

---

## FASE 6 - BOOTSTRAP PROYECTO AOLI [EL OBJETIVO REAL]

1. Inicialización Git Repo: `aoli-web-platform` en directorio correspondiente de PersonalOS.
2. Scaffold de Next.js 15, Drizzle, y Tailwind 4 con Strict TypeScript configuration.
3. Setup the Base UI Theme (Tokens) para AOLI en `globals.css` / Tailwind.
4. Conexión de Drizzle con Neon DB remota (`db push`).
5. Configurar Vercel Dashboard (Deploy Automático de rama Master).

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

1. **Repo AOLI Inicializado:** Push funcional en master de la arquitectura Next.js sin errores de build ni TS lints.
2. **Dashboard Cargo:** Acceso local a Payload CMS con tablas de inventario en blanco conectadas a base de datos externa Neon DB.
3. **Vercel Deploy:** URL temporal funcional comprobando la integración del Pipeline.
4. **Resumen de Sistema:** Un reporte limpio del estado de SDD, Engram, y GGA (Fases de la auditoría) con resolución de impedimentos.

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
