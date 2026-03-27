# SPEC.md - Macano Restaurant Management System

## 1. Project Overview

**Project Name:** Macano Restaurant Management System
**Type:** Web Application + Mobile App
**Core Functionality:** Sistema integral de gestión para restaurante en Margarita, Venezuela - incluyendo gestión de personal, proveedores, inventario, cocina, comando, clientes y marketing.
**Target Users:** Gerente general, chef, meseros, cajero, proveedores.

---

## 2. UI/UX Specification

### Layout Structure

**Dashboard Principal:**
- Sidebar navigation (izquierda)
- Header con búsqueda y notificaciones
- Área de contenido principal
- Quick actions flotante

**Responsive:**
- Desktop: 1200px+
- Tablet: 768px - 1199px
- Mobile: < 768px

### Visual Design

**Color Palette:**
- Primary: #1E3A5F (Azul profundo - mar)
- Secondary: #F4A261 (Arena - playa)
- Accent: #E76F51 (Corales - atardecer)
- Success: #2A9D8F (Verde agua)
- Warning: #E9C46A (Dorado)
- Background: #FAFAFA
- Text: #264653

**Typography:**
- Headings: "Poppins", sans-serif
- Body: "Open Sans", sans-serif
- Sizes: H1: 32px, H2: 24px, H3: 18px, Body: 14px

**Spacing:**
- Base: 8px
- Margins: 16px, 24px, 32px
- Border radius: 8px (cards), 4px (buttons)

### Components

- Cards con sombras suaves
- Tablas con zebra striping
- Formularios con validaciones
- Gráficos interactivos
- Notificaciones toast
- Modales para confirmaciones

---

## 3. Functionality Specification

### Módulos

#### 01_Gestion (Dashboard)
- KPIs en tiempo real
- Accesos directos
- Alertas y notificaciones

#### 02_Personal
- Organigrama interactivo
- Gestión de horarios
- Evaluaciones de desempeño
- Plan de training

#### 03_Proveedores
- Directorio completo
- Pedidos y entregas
- Control de calidad
- Historial de precios

#### 04_Logistica
- Inventario en tiempo real
- Alertas de stock mínimo
- Control de costos
- Órdenes de compra

#### 05_Cocina
- Catálogo de menú
- Recetas con fotos
- Control de porciones
- Higiene y normas

#### 06_Comando
- Tickets en tiempo real
- Tiempos por plato
- Priorización automática
- Quality control

#### 07_Clientes
- Base de datos CRM
- Sistema de reservas
- Historial de pedidos
- Programa de fidelización

#### 08_Marketing
- Gestión de redes sociales
- Calendario de contenido
- Campañas promocionales
- Análisis de engagement

#### 09_Reportes
- Reportes diarios/semanales/mensuales
- Gráficos interactivos
- Exportación PDF/Excel
- KPIs y métricas

---

## 4. Acceptance Criteria

### Must Have
- [ ] Dashboard con KPIs funcionales
- [ ] CRUD completo de personal
- [ ] Gestión de proveedores
- [ ] Control de inventario
- [ ] Menú con precios
- [ ] Tickets de cocina en tiempo real
- [ ] Base de clientes
- [ ] Reportes básicos

### Nice to Have
- [ ] App móvil
- [ ] Integración con redes sociales
- [ ] Reservas online
- [ ] Programa de fidelización
- [ ] Control de caja y gastos

---

## 5. Technical Stack

- **Frontend:** React 19 + Tailwind CSS
- **State:** Zustand
- **Backend:** Django DRF (API)
- **Database:** PostgreSQL
- **Testing:** Playwright

---

## 6. Timeline

**Semana 1:** Fundamentos + Módulos 01-05
**Semana 2:** Módulos 06-09 + Testing + Deploy

---

*Creado: 16/03/2026*
*Metodología: SDD*
