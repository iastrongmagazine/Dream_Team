# 🍽️ Macano Restaurant - Technical Specification

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React 19 + Vite |
| Styling | Tailwind CSS 4 |
| State | Zustand 5 |
| Backend | Django DRF 5.x |
| Database | PostgreSQL |
| Testing | Playwright |
| Container | Docker |

---

## Project Structure

```
APP/
├── frontend/          # React 19 + Vite
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── stores/
│   │   ├── api/
│   │   └── hooks/
│   ├── tests/
│   └── package.json
│
├── backend/          # Django DRF
│   ├── macano/
│   │   ├── modules/
│   │   │   ├── gestion/
│   │   │   ├── personal/
│   │   │   ├── proveedores/
│   │   │   ├── logistica/
│   │   │   ├── cocina/
│   │   │   ├── comando/
│   │   │   ├── clientes/
│   │   │   ├── marketing/
│   │   │   └── reportes/
│   │   └── core/
│   ├── requirements.txt
│   └── manage.py
│
└── docker-compose.yml
```

---

## Dashboard Features (Priority 1)

1. **KPIs en tiempo real**
   - Ventas diarias
   - Clientes atendidos
   - Ticket promedio
   - Occupancy

2. **Alertas**
   - Stock mínimo inventario
   - Pedidos pendientes
   - Reservas del día

3. **Accesos directos**
   - Nuevo pedido
   - Ver inventario
   - Agregar cliente

---

## API Endpoints (Priority 1)

### Dashboard
- `GET /api/dashboard/kpis` - KPIs del día
- `GET /api/dashboard/alerts` - Alertas activas

### Inventario
- `GET /api/inventario/` - Listar items
- `POST /api/inventario/` - Agregar item
- `PUT /api/inventario/{id}/` - Actualizar stock

### Pedidos
- `GET /api/pedidos/` - Listar pedidos
- `POST /api/pedidos/` - Crear pedido
- `PUT /api/pedidos/{id}/status/` - Actualizar estado

---

## UI Components

- DashboardLayout
- KPICard
- AlertCard
- QuickActionButton
- DataTable
- SearchBar
- Modal

---

*Created: 17/03/2026*
*Methodology: SDD - Silicon Valley Standards*
